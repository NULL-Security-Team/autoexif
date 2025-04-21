<p align="center">
  <a href="https://github.com/sircryptic/autoexif">
    <img src="https://github.com/user-attachments/assets/f9d8050a-7310-4f45-a05a-c2ad4e5194f5" alt="AutoExif"
  </a>

<p align="center">
  <a href="https://github.com/sircryptic/autoexif/stargazers"><img src="https://img.shields.io/github/stars/sircryptic/autoexif.svg" alt="GitHub Stars"></a>
  <a href="https://github.com/sircryptic/autoexif/network"><img src="https://img.shields.io/github/forks/sircryptic/autoexif.svg" alt="GitHub Forks"></a>
  <a href="https://github.com/sircryptic/autoexif/watchers"><img src="https://img.shields.io/github/watchers/sircryptic/autoexif.svg?style=social" alt="GitHub Watchers"></a>
  <br>
  <a href="https://github.com/SirCryptic/autoexif/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License"></a>
</p>

# AutoExif CLI w/TUI

A super user-friendly CLI tool for extracting and manipulating metadata from files and URLs.

## 🚀 Features

- Read metadata from images and videos
- Extract metadata from local files and URLs
- Wipe specific metadata (e.g., GPS)
- Super Easy setup for Windows & Linux Distro's

### Q/A
- Q: Where is the original bash version? 
- A: [Here](https://github.com/SirCryptic/autoexif/tree/orginal---bash)

<h1 align="left">Preview</h1>

<center>

<details>
  <summary>Click to expand!</summary>

- Linux

![image](https://github.com/user-attachments/assets/854ed46c-a446-4c0a-9e10-abe24ee08fc1)

![image](https://github.com/user-attachments/assets/f10c7b29-b82e-4134-a481-f04b3c5f2390)

![image](https://github.com/user-attachments/assets/051a4a2c-e672-4c84-933c-272d43e4dcb2)

- Windows

![image](https://github.com/user-attachments/assets/9d7eae94-889a-424d-b808-102f4f066ab2)

  ![autoexif-cli](https://github.com/user-attachments/assets/936b15a6-4b41-4b3c-b788-fc71069851b0)

![autoexif-cl1](https://github.com/user-attachments/assets/2458ee5c-d239-40e9-bdbb-c9b96597f5fb)

</center>

## 📦 Installation

Install via pip:
```
pip install autoexif
```

or build & install yourself from source.

### 1. Clone the repository

```bash
git clone https://github.com/SirCryptic/autoexif.git
cd autoexif
```

### 2. Install Python and dependencies
Make sure you have Python 3.11+ installed.
```bash
pip install -r requirements.txt
```

### 3. Install the CLI tool

windows
```bash
python setup.py install
```

linux
```bash
sudo python3 setup.py install
```

- Windows: Copies exiftool.exe and exiftool_files.zip to C:\Users<YourUser>\AppData\Local\autoexif, extracting the zip.
- Linux: Auto-installs ExifTool using your system's package manager or downloads it to ~/.autoexif/ if needed.

## 🛠️ Usage
Get started with:
```bash
autoexif help
```

- Short Version Of `help`
```bash
autoexif --help
```

- Open TUI
```bash
autoexif
```

## 📷 Examples
Read metadata from an image in the current directory:

```bash
autoexif read
```

Read metadata from a specific image:
```bash
autoexif read sample.jpg
```

Read detailed metadata:
```bash
autoexif read sample.jpg --detailed
```

Read metadata from a URL:
```bash
autoexif read https://example.com/image.jpg
```

Wipe GPS data:
```bash
autoexif wipe sample.jpg --type gps
```

Extract GPS from a video:
```bash
autoexif gps video.mp4
```

Get thumbnail metadata:
```bash
autoexif thumbnail sample.jpg
```

Get expert-level metadata:
```bash
autoexif expert sample.jpg
```
# 📌 Notes
- Windows: Installation copies exiftool.exe and exiftool_files.zip to
C:\Users\<YourUser>\AppData\Local\autoexif\
and extracts the required files.
- Linux: Auto-installs ExifTool using your system's package manager or downloads it to ~/.autoexif/ if needed.

- Ethical Use: Only process files and URLs you are authorized to access.

- Help: Run `autoexif help` for more details and usage options.

#
Made with ❤️ by SirCryptic
