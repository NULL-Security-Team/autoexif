<p align="center">
  <a href="https://github.com/sircryptic/autoexif/stargazers"><img src="https://img.shields.io/github/stars/sircryptic/autoexif.svg" alt="GitHub Stars"></a>
  <a href="https://github.com/sircryptic/autoexif/network"><img src="https://img.shields.io/github/forks/sircryptic/autoexif.svg" alt="GitHub Forks"></a>
  <a href="https://github.com/sircryptic/autoexif/watchers"><img src="https://img.shields.io/github/watchers/sircryptic/autoexif.svg?style=social" alt="GitHub Watchers"></a>
  <br>
  <a href="https://github.com/SirCryptic/autoexif/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License"></a>
</p>

# AutoExif CLI

A super user-friendly CLI tool for extracting and manipulating metadata from files and URLs.

## 🚀 Features

- Read metadata from images and videos
- Extract metadata from local files and URLs
- Wipe specific metadata (e.g., GPS)
- Built-in ExifTool setup for Windows

<h1 align="left">Preview</h1>

<center>

<details>
  <summary>Click to expand!</summary>

  ![autoexif-cli](https://github.com/user-attachments/assets/936b15a6-4b41-4b3c-b788-fc71069851b0)

![autoexif-cl1](https://github.com/user-attachments/assets/2458ee5c-d239-40e9-bdbb-c9b96597f5fb)

</center>


## 📦 Installation

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

```bash
python setup.py install
```

### 4. Linux users: Install ExifTool manually

```bash
sudo apt install libimage-exiftool-perl
```

## 🛠️ Usage
Get started with:
```bash
autoexif help
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

- Ethical Use: Only process files and URLs you are authorized to access.

- Help: Run `autoexif help` for more details and usage options.

#
Made with ❤️ by SirCryptic
