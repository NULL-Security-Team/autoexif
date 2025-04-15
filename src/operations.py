import requests
from .exiftool import ExifTool

class MetadataOperations:
    def __init__(self):
        self.exiftool = ExifTool()

    def read_metadata(self, path, detailed=False):
        """Read metadata from a local file."""
        args = ["-G", "-"] if detailed else [path]
        return self.exiftool.run(args, input_data=open(path, "rb").read() if detailed else None)

    def read_web_metadata(self, url):
        """Read metadata from a URL."""
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return self.exiftool.run(["-fast", "-"], input_data=response.content)

    def wipe_metadata(self, path, type="all", comment=None, custom_type=None):
        """Wipe metadata from a file."""
        args = []
        if type == "gps":
            args.append("-gps:all=")
        elif type == "photoshop":
            args.append("-Photoshop:All=")
        elif type == "custom" and custom_type:
            args.append(f"-{custom_type}:all=")
        else:
            args.append("-all=")
        if comment:
            args.append(f"-comment={comment}")
        args.append(path)
        return self.exiftool.run(args)

    def extract_gps(self, path):
        """Extract GPS data from a file."""
        return self.exiftool.run(["-gps:all", "-j", path])

    def extract_thumbnail(self, path, is_url=False):
        """Extract thumbnail metadata."""
        if is_url:
            response = requests.get(path, timeout=5)
            response.raise_for_status()
            data = response.content
            args = ["-fast", "-"]
        else:
            data = None
            args = [path]
        thumbnail_data = self.exiftool.run(args + ["-thumbnailimage", "-b"], input_data=data)
        if thumbnail_data:
            return self.exiftool.run(["-"], input_data=thumbnail_data.encode())
        return None

    def expert_metadata(self, path):
        """Extract metadata from all tag groups."""
        return self.exiftool.run(["-a", "-G", "-j", path])