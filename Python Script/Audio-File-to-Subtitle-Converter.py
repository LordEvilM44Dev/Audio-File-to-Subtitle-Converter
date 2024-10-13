import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import time

def process_audio(audio_path, pause_threshold=1.0):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_path)
    
    audio_chunks = split_on_silence(audio, 
                                    min_silence_len=1000,
                                    silence_thresh=-40,
                                    keep_silence=500)
    
    subtitles = []
    total_duration = 0.0

    for i, chunk in enumerate(audio_chunks):
        chunk_path = f"chunk{i}.wav"
        chunk.export(chunk_path, format="wav")

        with sr.AudioFile(chunk_path) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                duration = len(chunk) / 1000

                formatted_duration = time.strftime("%M:%S", time.gmtime(total_duration))
                subtitles.append(f'[DURATION="{formatted_duration}"]\n[SUBTITLE="{text}"]\n')

                total_duration += duration

            except sr.UnknownValueError:
                subtitles.append(f'[DURATION="{time.strftime("%M:%S", time.gmtime(total_duration))}"]\n[SUBTITLE="(inaudible)"]\n')
            
        os.remove(chunk_path)

    return subtitles

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.flac *.ogg")])
    if file_path:
        subtitles = process_audio(file_path)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "".join(subtitles))
        global subtitle_data
        subtitle_data = subtitles

def download_file():
    if subtitle_data:
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if save_path:
            with open(save_path, "w") as f:
                f.writelines(subtitle_data)
            messagebox.showinfo("Success", "File saved successfully!")

root = tk.Tk()
root.title("Audio to Subtitle Converter")

upload_button = tk.Button(root, text="Upload Audio", command=upload_file)
upload_button.pack(pady=10)

output_text = tk.Text(root, height=20, width=50)
output_text.pack(pady=10)

download_button = tk.Button(root, text="Download .txt File", command=download_file)
download_button.pack(pady=10)

subtitle_data = None

root.mainloop()
