import subprocess
import os
import sys
import shutil
import zipfile
from pathlib import Path

class ExifTool:
    def __init__(self):
        self.system = sys.platform.lower()
        self.appdata_dir = Path(os.getenv("LOCALAPPDATA", os.path.expanduser("~\\AppData\\Local"))) / "autoexif" if "win" in self.system else Path.home() / ".autoexif"
        self.exiftool_path = self.setup_exiftool()

    def setup_exiftool(self):
        """Setup ExifTool path."""
        if "win" in self.system:
            data_exiftool = self.appdata_dir / "exiftool.exe"
            dll_path = self.appdata_dir / "exiftool_files"
            if data_exiftool.exists() and dll_path.exists() and any(dll_path.glob("perl5*.dll")):
                return str(data_exiftool)
            
            # Copy from installed package
            try:
                resource_base = getattr(sys, '_MEIPASS', Path(__file__).parent.parent)
                exiftool_src = Path(resource_base) / "resources/exiftool.exe"
                zip_src = Path(resource_base) / "resources/exiftool_files.zip"
                
                self.appdata_dir.mkdir(exist_ok=True)
                
                # Copy exiftool.exe
                if exiftool_src.exists():
                    shutil.copy(exiftool_src, data_exiftool)
                else:
                    raise FileNotFoundError("exiftool.exe not found in C:\\Users\\<YourUser>\\AppData\\Local\\autoexif")
                
                # Copy and extract exiftool_files.zip
                if zip_src.exists():
                    shutil.copy(zip_src, self.appdata_dir / "exiftool_files.zip")
                    try:
                        with zipfile.ZipFile(self.appdata_dir / "exiftool_files.zip", "r") as zip_ref:
                            zip_ref.extractall(self.appdata_dir / "exiftool_files")
                    except zipfile.BadZipFile:
                        raise RuntimeError("exiftool_files.zip is corrupt. Replace it in src/resources/ with a valid zip from https://exiftool.org/.")
                    # Verify extraction
                    if not dll_path.exists():
                        raise RuntimeError("Failed to create exiftool_files directory in C:\\Users\\<YourUser>\\AppData\\Local\\autoexif")
                    if not any(dll_path.glob("perl5*.dll")):
                        raise RuntimeError("No Perl DLLs found in exiftool_files. Ensure exiftool_files.zip contains them.")
                    if not (dll_path / "lib").exists():
                        raise RuntimeError("No lib/ directory found in exiftool_files. Ensure exiftool_files.zip contains it.")
                else:
                    raise FileNotFoundError("exiftool_files.zip not found in package.")
                
                if data_exiftool.exists():
                    return str(data_exiftool)
                else:
                    raise RuntimeError("Failed to copy exiftool.exe to AppData\\Local\\autoexif")
            except Exception as e:
                print(f"Error setting up exiftool: {e}")
            
            # Fallback to system exiftool
            return "exiftool"
        else:
            return "exiftool"

    def run(self, args, input_data=None):
        """Run ExifTool with given arguments."""
        try:
            env = os.environ.copy()
            if "win" in self.system:
                dll_path = self.appdata_dir / "exiftool_files"
                if dll_path.exists():
                    env["PATH"] = f"{dll_path};{env.get('PATH', '')}"
                else:
                    raise RuntimeError("exiftool_files directory not found in C:\\Users\\<YourUser>\\AppData\\Local\\autoexif")
            
            process = subprocess.Popen(
                [self.exiftool_path] + args,
                stdin=subprocess.PIPE if input_data else None,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=False,
                env=env,
                cwd=str(dll_path) if "win" in self.system and dll_path.exists() else None
            )
            stdout, stderr = process.communicate(input=input_data)
            if process.returncode == 0:
                return stdout.decode("utf-8", errors="ignore")
            else:
                raise RuntimeError(f"ExifTool error: {stderr.decode('utf-8', errors='ignore')}")
        except FileNotFoundError:
            raise RuntimeError("ExifTool not found. On Windows, check C:\\Users\\<YourUser>\\AppData\\Local\\autoexif\\exiftool.exe and exiftool_files\\. On Linux, install with: sudo apt install libimage-exiftool-perl")
        except Exception as e:
            raise RuntimeError(f"Failed to run ExifTool: {e}")