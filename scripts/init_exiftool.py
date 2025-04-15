from pathlib import Path
import shutil
import sys

def init_exiftool():
    """Initialize ExifTool for Windows."""
    if "win" not in sys.platform.lower():
        print("This script is for Windows only. On Linux, run: sudo apt install libimage-exiftool-perl")
        return
    resource_dir = Path("src/resources")
    exiftool_src = resource_dir / "exiftool.exe"
    if not exiftool_src.exists():
        print(f"Error: {exiftool_src} not found. Download from https://exiftool.org/ and place in src/resources")
        sys.exit(1)
    dest = Path("data/exiftool.exe")
    dest.parent.mkdir(exist_ok=True)
    shutil.copy(exiftool_src, dest)
    print(f"ExifTool copied to {dest}")

if __name__ == "__main__":
    init_exiftool()