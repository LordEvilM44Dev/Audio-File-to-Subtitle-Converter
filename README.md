# Audio-File-to-Subtitle-Converter
![License](https://img.shields.io/badge/license-MIT-green.svg)

Python application for converting audio files into subtitles text files, this tool alows users to upload audio files and generate subtitle text, formatted with durations for each spoken segment.

## Overview

Works with https://github.com/LordEvilM44Dev/Unity-Subtitle-System.git

The Audio File to Subtitle Converter script is a Python application designed to simplify the process of converting audio files into text-based subtitles. It uses speech recognition to transcribe spoken words from audio files and formats the output for easy readability.

## Features

Audio File Upload: Select audio files in formats such as ```WAV```, ```MP3```, etc.

Speech Recognition: Leverages the Google Speech Recognition API to transcribe spoken words into text.

Pause Detection: Splits audio based on silence, allowing for more accurate transcription of conversations.

Custom Subtitle Format: Generates subtitles in the format ```[DURATION="MM:SS"]```\n```[SUBTITLE="text here"]```\n.

Download Option: Save the generated subtitles as a .txt file.

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Build as Executable](#build-as-executable)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)


 ## Installation

1. Clone or download this repository.

```bash
git clone https://github.com/LordEvilM44Dev/Unity-Subtitle-System.git
```

## Requirements

To run this application, ensure you have the following dependencies installed:

```tkinter```

```SpeechRecognition```

```pydub```

```ffmpeg``` (required by pydub for audio processing)

You can install the Python dependencies using pip:

```bash
pip install SpeechRecognition pydub
```

## How to Use

1. Upload Audio: Click the "Upload Audio" button to select your audio file.

2. View Subtitles: The transcribed subtitles will appear in the text area.

3. Download Subtitles: Click the "Download .txt File" button to save the subtitles to your computer.

## Build as Executable

If you're using the script directly and want to create an executable for Windows, you can easily build it using PyInstaller. Simply run the following command in your terminal:

```bash
pyinstaller --onefile --windowed your_script.py
```

Replace your_script.py with the name of the Python script. This will generate a standalone .exe file in the dist folder.

## Screenshots

## Contributing
Contributions are welcome! Please follow the guidelines below:
1. Fork the project.
2. Create a new branch ```(git checkout -b feature/your-feature)```.
3. Commit your changes ```(git commit -m 'Add some feature')```.
4. Push to the branch ```(git push origin feature/your-feature)```.
5. Open a pull request.

 ## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
