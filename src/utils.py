import re
from pathlib import Path

def validate_path(path):
    """Validate that a file exists and is accessible."""
    try:
        resolved_path = Path(path).resolve()
        return resolved_path.exists() and resolved_path.is_file()
    except (OSError, FileNotFoundError, PermissionError):
        return False

def validate_url(url):
    """Validate URL format."""
    pattern = r"^https?://[^\s/$.?#].[^\s]*$"
    return bool(re.match(pattern, url))

def find_image_in_directory(directory):
    """Find the first image file in the directory."""
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}
    image_files = [f for f in directory.iterdir() if f.is_file() and f.suffix.lower() in image_extensions]
    return image_files[0] if image_files else None