# Audio-File-to-Subtitle-Converter
![License](https://img.shields.io/badge/license-MIT-green.svg)

Python application for converting audio files into subtitles text files, this tool alows users to upload audio files and generate subtitle text, formatted with durations for each spoken segment.

## Overview

This script is compatible with the [Unity Subtitle System](https://github.com/LordEvilM44Dev/Unity-Subtitle-System.git) allowing seamless integration of subtitles into Unity projects.

**Note:** This application is designed to work **only on Windows**. Making it compatible with macOS or Linux would require additional effort.

The Audio File to Subtitle Converter script is a Python application designed to simplify the process of converting audio files into text-based subtitles. It uses speech recognition to transcribe spoken words from audio files and formats the output for easy readability.

## Features

Audio File Upload: Select audio files in formats such as ```WAV```, ```MP3```, etc.

Speech Recognition: Leverages the Google Speech Recognition API to transcribe spoken words into text.

Pause Detection: Splits audio based on silence, allowing for more accurate transcription of conversations.

Custom Subtitle Format: Generates subtitles in the format ```[DURATION="MM:SS"]```\n```[SUBTITLE="text here"]```\n.

Download Option: Save the generated subtitles as a .txt file.

## Table of Contents

- [Installation](#installation)
- [🚨Important-Installation🚨](#important-installation)
- [Requirements](#requirements)
- [Compatibility](#compatibility)
- [How to Use](#how-to-use)
- [Build as Executable](#build-as-executable)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)


 ## Installation

 **Compatibility Notice:** This application works on **Windows** only.

1. Clone or download this repository.

```bash
git clone https://github.com/LordEvilM44Dev/Unity-Subtitle-System.git
```

## 🚨IMPORTANT INSTALLATION🚨

To run the executable properly, you need to add FFmpeg to your computer's system ```Path```. Follow these steps carefully:

1. Download FFmpeg for Windows from the official source: [FFMpeg Builds](https://www.gyan.dev/ffmpeg/builds/).
2. After downloading, unzip the file (if necessary) and rename the folder to ```ffmpeg```.
3. Move the ```ffmpeg``` folder to your main storage drive, typically:
```bash
This PC > Loacal Disk (C:)
```
5. Open the Start menu, search for ```System Environment Variables```, and click to open it.
6. Click the ```Environment Variables``` button at the bottom of the window.
7. Under the ```User Variables``` section, select ```Path``` and click the ```Edit``` button.
8. Click New and enter the path to the bin folder inside the FFmpeg directory. For example:
```bash
C:\ffmpeg\bin
```
9. Click OK to save your changes in each window.
10. FFmpeg is now added to your system Path and ready to use.

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

## Compatibility

This application is designed to run on **Windows** only. Currently, there are no plans to support macOS or Linux due to the complexity involved in adapting the code for those platforms.

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

![Screenshot 1 Application ](https://github.com/LordEvilM44Dev/Audio-File-to-Subtitle-Converter/blob/main/Screenshots/screenshot_app.png)
![Screenshot 2 Added Audio File ](https://github.com/LordEvilM44Dev/Audio-File-to-Subtitle-Converter/blob/main/Screenshots/screenshot_audio.png)
![Screenshot 2 The Text File Format ](https://github.com/LordEvilM44Dev/Audio-File-to-Subtitle-Converter/blob/main/Screenshots/screenshot_txt.png)

## Contributing
Contributions are welcome! Please follow the guidelines below:
1. Fork the project.
2. Create a new branch ```(git checkout -b feature/your-feature)```.
3. Commit your changes ```(git commit -m 'Add some feature')```.
4. Push to the branch ```(git push origin feature/your-feature)```.
5. Open a pull request.

 ## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
