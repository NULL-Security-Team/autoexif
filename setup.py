import os
import sys
import shutil
import zipfile
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstallCommand(install):
    """Custom install command to setup ExifTool and icon."""
    def run(self):
        if "win" in sys.platform.lower():
            try:
                appdata_dir = Path(os.getenv("LOCALAPPDATA", os.path.expanduser("~\\AppData\\Local"))) / "autoexif"
                appdata_dir.mkdir(exist_ok=True)
                
                resource_base = Path(__file__).parent / "src" / "resources"
                exiftool_src = resource_base / "exiftool.exe"
                zip_src = resource_base / "exiftool_files.zip"
                icon_src = resource_base / "icon.png"
                
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
                        print("Error: Failed to create exiftool_files directory.")
                        sys.exit(1)
                    if not any(dll_path.glob("perl5*.dll")):
                        print("Error: exiftool_files.zip does not contain Perl DLLs. Download from https://exiftool.org/.")
                        sys.exit(1)
                    if not (dll_path / "lib").exists():
                        print("Error: exiftool_files.zip does not contain lib/ directory. Download from https://exiftool.org/.")
                        sys.exit(1)
                else:
                    print("Error: exiftool_files.zip not found in src/resources. Download from https://exiftool.org/.")
                    sys.exit(1)
                
                if icon_src.exists():
                    shutil.copy(icon_src, appdata_dir / "icon.png")
                else:
                    print("Warning: icon.png not found in src/resources. Skipping icon installation.")
                
                if not (appdata_dir / "exiftool.exe").exists():
                    print("Error: Failed to copy exiftool.exe.")
                    sys.exit(1)
            except Exception as e:
                print(f"Error copying ExifTool files: {e}")
                sys.exit(1)
        elif "linux" in sys.platform.lower():
            try:
                from scripts.install_exiftool import install_exiftool
                install_exiftool()
                resource_base = Path(__file__).parent / "src" / "resources"
                icon_src = resource_base / "icon.png"
                autoexif_dir = Path.home() / ".autoexif"
                if icon_src.exists():
                    autoexif_dir.mkdir(exist_ok=True)
                    shutil.copy(icon_src, autoexif_dir / "icon.png")
                else:
                    print("Warning: icon.png not found in src/resources. Skipping icon installation.")
            except Exception as e:
                print(f"Error installing ExifTool or icon on Linux: {e}")
                sys.exit(1)
        
        install.run(self)

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="autoexif",
    version="1.0.2",
    packages=['autoexif'] + [f'autoexif.{pkg}' for pkg in find_packages(where='src')],
    package_dir={"autoexif": "src"},
    include_package_data=True,
    install_requires=["click>=8.1.0", "requests>=2.28.0", "prompt_toolkit>=3.0.0"],
    package_data={
        "autoexif": [
            "resources/exiftool.exe",
            "resources/exiftool_files.zip",
            "resources/icon.png",
        ],
    },
    data_files=[
        ("scripts", ["scripts/install_exiftool.py", "scripts/init_exiftool.py"]),
    ],
    entry_points={
        "console_scripts": [
            "autoexif=autoexif.cli:cli",
        ],
    },
    cmdclass={
        "install": CustomInstallCommand,
    },
    author="SirCryptic",
    author_email="sircryptic@protonmail.com",
    description="CLI tool for easy metadata extraction and manipulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SirCryptic/autoexif",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.11",
)
