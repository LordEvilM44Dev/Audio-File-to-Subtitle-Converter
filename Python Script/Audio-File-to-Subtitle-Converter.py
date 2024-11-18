import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import time

def process_audio(audio_path, output_folder, pause_threshold=1.0):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_path)

    audio_chunks = split_on_silence(audio, 
                                    min_silence_len=1000,
                                    silence_thresh=-40,
                                    keep_silence=500)
    
    subtitles = []
    total_duration = 0.0

    os.makedirs(output_folder, exist_ok=True)

    for i, chunk in enumerate(audio_chunks):
        chunk_path = os.path.join(output_folder, f"clip_{i}.wav")
        chunk.export(chunk_path, format="wav")

        with sr.AudioFile(chunk_path) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                duration = len(chunk) / 1000
                start_time = total_duration
                formatted_duration = time.strftime("%M:%S", time.gmtime(start_time))

                subtitles.append({
                    "duration": formatted_duration,
                    "text": text,
                    "speaker": "Unknown",
                    "audio_file": chunk_path
                })

                total_duration += duration

            except sr.UnknownValueError:
                subtitles.append({
                    "duration": time.strftime("%M:%S", time.gmtime(total_duration)),
                    "text": "(inaudible)",
                    "speaker": "Unknown",
                    "audio_file": None
                })

    return subtitles

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.flac *.ogg")])
    if file_path:
        global subtitle_data, output_folder_path
        output_folder_path = filedialog.askdirectory(title="Select Folder to Save Audio Clips")
        if not output_folder_path:
            messagebox.showwarning("Warning", "No folder selected. Operation canceled.")
            return

        subtitle_data = process_audio(file_path, output_folder_path)
        output_text.delete(1.0, tk.END)

        for subtitle in subtitle_data:
            output_text.insert(tk.END, f'[DURATION="{subtitle["duration"]}"]\n')
            output_text.insert(tk.END, f'[SPEAKER="{subtitle["speaker"]}"]\n')
            output_text.insert(tk.END, f'[SUBTITLE="{subtitle["text"]}"]\n\n')

def edit_speaker_names():
    if subtitle_data:
        for subtitle in subtitle_data:
            speaker_name = simpledialog.askstring(
                "Speaker Name",
                f"Enter speaker name for text: \"{subtitle['text']}\""
            )
            if speaker_name:
                subtitle["speaker"] = speaker_name

        output_text.delete(1.0, tk.END)
        for subtitle in subtitle_data:
            output_text.insert(tk.END, f'[DURATION="{subtitle["duration"]}"]\n')
            output_text.insert(tk.END, f'[SPEAKER="{subtitle["speaker"]}"]\n')
            output_text.insert(tk.END, f'[SUBTITLE="{subtitle["text"]}"]\n\n')

def download_file():
    if subtitle_data:
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if save_path:
            with open(save_path, "w") as f:
                for subtitle in subtitle_data:
                    f.write(f'[DURATION="{subtitle["duration"]}"]\n')
                    f.write(f'[SPEAKER="{subtitle["speaker"]}"]\n')
                    f.write(f'[SUBTITLE="{subtitle["text"]}"]\n')
                    if subtitle["audio_file"]:
                        f.write(f'[AUDIO_FILE="{os.path.relpath(subtitle["audio_file"], os.path.dirname(save_path))}"]\n\n')
            messagebox.showinfo("Success", "File and audio clips saved successfully!")

root = tk.Tk()
root.title("Audio to Subtitle Converter")

upload_button = tk.Button(root, text="Upload Audio", command=upload_file)
upload_button.pack(pady=10)

edit_button = tk.Button(root, text="Edit Speaker Names", command=edit_speaker_names)
edit_button.pack(pady=10)

output_text = tk.Text(root, height=20, width=50)
output_text.pack(pady=10)

download_button = tk.Button(root, text="Download .txt File", command=download_file)
download_button.pack(pady=10)

subtitle_data = None
output_folder_path = None

root.mainloop()
