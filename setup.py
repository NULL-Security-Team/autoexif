import os
import sys
import shutil
import zipfile
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstallCommand(install):
    """Custom install command to setup ExifTool."""
    def run(self):
        if "win" in sys.platform.lower():
            try:
                appdata_dir = Path(os.getenv("LOCALAPPDATA", os.path.expanduser("~\\AppData\\Local"))) / "autoexif"
                appdata_dir.mkdir(exist_ok=True)
                
                resource_base = Path(__file__).parent / "src/resources"
                exiftool_src = resource_base / "exiftool.exe"
                zip_src = resource_base / "exiftool_files.zip"
                
                if exiftool_src.exists():
                    shutil.copy(exiftool_src, appdata_dir / "exiftool.exe")
                else:
                    print("Error: exiftool.exe not found in src/resources. Download from https://exiftool.org/.")
                    sys.exit(1)
                
                if zip_src.exists():
                    shutil.copy(zip_src, appdata_dir / "exiftool_files.zip")
                    dll_path = appdata_dir / "exiftool_files"
                    dll_path.mkdir(exist_ok=True)
                    try:
                        with zipfile.ZipFile(appdata_dir / "exiftool_files.zip", "r") as zip_ref:
                            for member in zip_ref.namelist():
                                zip_ref.extract(member, dll_path)
                    except zipfile.BadZipFile:
                        print("Error: exiftool_files.zip is corrupt. Replace with a valid zip from https://exiftool.org/.")
                        sys.exit(1)
                    if not dll_path.exists():
                        print("Error: Failed to create exiftool_files directory in C:\\Users\\<YourUser>\\AppData\\Local\\autoexif.")
                        sys.exit(1)
                    if not any(dll_path.glob("perl5*.dll")):
                        print("Error: exiftool_files.zip does not contain Perl DLLs. Download a valid zip from https://exiftool.org/.")
                        sys.exit(1)
                    if not (dll_path / "lib").exists():
                        print("Error: exiftool_files.zip does not contain lib/ directory. Download a valid zip from https://exiftool.org/.")
                        sys.exit(1)
                else:
                    print("Error: exiftool_files.zip not found in src/resources. Download from https://exiftool.org/.")
                    sys.exit(1)
                
                if not (appdata_dir / "exiftool.exe").exists():
                    print("Error: Failed to copy exiftool.exe to C:\\Users\\<YourUser>\\AppData\\Local\\autoexif.")
                    sys.exit(1)
            except Exception as e:
                print(f"Error copying ExifTool files: {e}")
                sys.exit(1)
        elif "linux" in sys.platform.lower():
            try:
                from scripts.install_exiftool import install_exiftool
                install_exiftool()
            except Exception as e:
                print(f"Error installing ExifTool on Linux: {e}")
                sys.exit(1)
        
        install.run(self)

# Read README.md with UTF-8 encoding
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="autoexif",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["click", "requests", "prompt_toolkit"],
    package_data={
        "autoexif": [
            "src/resources/exiftool.exe",
            "src/resources/exiftool_files.zip",
            "scripts/install_exiftool.py"
        ],
    },
    entry_points={
        "console_scripts": [
            "autoexif=src.cli:cli",
        ],
    },
    cmdclass={
        "install": CustomInstallCommand,
    },
    author="SirCryptic",
    description="CLI tool for easy metadata extraction and manipulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
