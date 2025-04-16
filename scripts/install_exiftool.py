import subprocess
import sys
import os
import urllib.request
import tarfile
import shutil
from pathlib import Path

def check_exiftool():
    """Check if ExifTool is installed."""
    return shutil.which("exiftool") is not None

def try_package_manager():
    """Try installing ExifTool with available package managers."""
    package_managers = [
        {"cmd": "apt", "install": "apt install -y libimage-exiftool-perl", "update": "apt update"},
        {"cmd": "dnf", "install": "dnf install -y perl-image-exiftool", "update": "dnf makecache"},
        {"cmd": "pacman", "install": "pacman -S --noconfirm perl-image-exiftool", "update": "pacman -Syy"},
        {"cmd": "zypper", "install": "zypper install -y perl-Image-ExifTool", "update": "zypper refresh"},
        {"cmd": "apk", "install": "apk add exiftool", "update": "apk update"}
    ]
    
    for pm in package_managers:
        if shutil.which(pm["cmd"]):
            print(f"Trying {pm['cmd']}...")
            try:
                subprocess.run(f"sudo {pm['update']}", shell=True, check=True, capture_output=True, text=True)
                subprocess.run(f"sudo {pm['install']}", shell=True, check=True, capture_output=True, text=True)
                if check_exiftool():
                    print(f"ExifTool installed successfully via {pm['cmd']}.")
                    return True
                print(f"{pm['cmd']} failed to install ExifTool.")
            except subprocess.CalledProcessError as e:
                print(f"{pm['cmd']} failed: {e.stderr}")
    return False

def install_exiftool_manually():
    """Install ExifTool manually to ~/.autoexif."""
    print("Installing ExifTool manually to ~/.autoexif...")
    try:
        exiftool_dir = Path.home() / ".autoexif"
        exiftool_dir.mkdir(exist_ok=True)
        tar_path = exiftool_dir / "exiftool.tar.gz"
        urllib.request.urlretrieve("https://exiftool.org/Image-ExifTool-12.76.tar.gz", tar_path)
        
        with tarfile.open(tar_path, "r:gz") as tar:
            tar.extractall(exiftool_dir)
        
        exiftool_bin = exiftool_dir / "Image-ExifTool-12.76" / "exiftool"
        exiftool_bin.chmod(0o755)
        
        target_bin = Path("/usr/local/bin/exiftool")
        subprocess.run(f"sudo ln -sf {exiftool_bin} {target_bin}", shell=True, check=True, capture_output=True)
        
        tar_path.unlink()
        if check_exiftool():
            print("ExifTool installed successfully.")
            return True
        raise RuntimeError("Manual ExifTool installation failed.")
    except Exception as e:
        print(f"Manual install failed: {e}")
        return False

def install_exiftool():
    """Install ExifTool on Linux."""
    if check_exiftool():
        print("ExifTool already installed.")
        return
    
    if try_package_manager():
        return
    
    if install_exiftool_manually():
        return
    
    raise RuntimeError("Failed to install ExifTool. Try manually: sudo apt install libimage-exiftool-perl (Ubuntu/Mint), sudo dnf install perl-image-exiftool (Fedora), or sudo pacman -S perl-image-exiftool (Arch).")