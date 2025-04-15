import click
import sys
from pathlib import Path
from .exiftool import ExifTool
from .operations import MetadataOperations
from .utils import validate_path, validate_url, find_image_in_directory

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """AutoExif CLI - Easy metadata extraction and manipulation.

    Run 'autoexif help' for usage instructions and examples.
    """
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

@cli.command()
def help():
    """Show detailed help with examples."""
    help_text = """
AutoExif CLI v1.0 - Metadata Tool by SirCryptic

Easily extract, wipe, or analyze metadata from images, videos, or URLs.
Perfect for beginners and pentesters!

Usage:
  autoexif <command> [options] <path>

Commands:
  help           Show this help message with examples
  read           Extract basic or detailed metadata
  wipe           Remove metadata (GPS, all, Photoshop, or custom)
  gps            Extract GPS data from images or videos
  thumbnail      Analyze thumbnail metadata
  expert         Extract metadata from all ExifTool tag groups

Examples:
  - Read metadata from an image in current directory:
    autoexif read
  - Read metadata from a specific image:
    autoexif read sample.jpg
  - Read detailed metadata:
    autoexif read sample.jpg --detailed
  - Read metadata from a URL:
    autoexif read https://example.com/image.jpg
  - Wipe all metadata:
    autoexif wipe sample.jpg --type all --comment "Cleaned"
  - Wipe GPS data:
    autoexif wipe sample.jpg --type gps
  - Extract video GPS:
    autoexif gps video.mp4
  - Get thumbnail metadata:
    autoexif thumbnail sample.jpg
  - Extract all tag groups:
    autoexif expert sample.jpg

Tips:
  - For 'read', omit path to use an image in the current directory.
  - Path can be a local file (e.g., sample.jpg) or URL (for 'read' and 'thumbnail').
  - Use --detailed for more metadata.
  - On Linux, install exiftool: sudo apt install libimage-exiftool-perl
  - On Windows, ensure exiftool.exe is in C:\\Users\\<YourUser>\\AppData\\Local\\autoexif\\

Ethical Use:
  Only process files or URLs you have permission to analyze.
    """
    click.echo(help_text)

@cli.command()
@click.argument("path", required=False)
@click.option("--detailed", is_flag=True, help="Extract detailed metadata")
def read(path, detailed):
    """Extract metadata from a file or URL.

    Example: autoexif read sample.jpg --detailed
    """
    try:
        ops = MetadataOperations()
        if not path:
            current_dir = Path.cwd()
            image_path = find_image_in_directory(current_dir)
            if not image_path:
                click.echo("No image found in current directory. Try specifying a file or URL!", err=True)
                return
            click.echo(f"Reading metadata from file: {image_path.name}...")
            result = ops.read_metadata(str(image_path), detailed)
        elif path.startswith("http"):
            if not validate_url(path):
                click.echo("Oops, that URL looks invalid! Try something like https://example.com/image.jpg.", err=True)
                return
            click.echo("Fetching metadata from URL...")
            result = ops.read_web_metadata(path)
        else:
            abs_path = Path(path).resolve()
            if not validate_path(abs_path):
                click.echo(f"Oops, file not found: {path}. Check the file exists in the current directory or provide a full path!", err=True)
                return
            click.echo("Reading metadata from file...")
            result = ops.read_metadata(str(abs_path), detailed)
        
        if result:
            click.echo(result)
        else:
            click.echo("No metadata found. Try a different file or URL!")
    except Exception as e:
        click.echo(f"Error: {str(e)}. On Windows, check C:\\Users\\<YourUser>\\AppData\\Local\\autoexif\\exiftool.exe and exiftool_files\\. On Linux: sudo apt install libimage-exiftool-perl.", err=True)

@cli.command()
@click.argument("path")
@click.option("--type", type=click.Choice(["gps", "all", "photoshop", "custom"]), default="all", help="Metadata type to wipe")
@click.option("--comment", help="Add a custom comment after wiping")
@click.option("--custom-type", help="Specific metadata type to wipe (e.g., JFIF) for --type custom")
def wipe(path, type, comment, custom_type):
    """Wipe metadata from a local file.

    Example: autoexif wipe sample.jpg --type gps
    """
    try:
        if path.startswith("http"):
            click.echo("Sorry, wiping metadata works only with local files, not URLs!", err=True)
            return
        abs_path = Path(path).resolve()
        if not validate_path(abs_path):
            click.echo(f"Oops, file not found: {path}. Check the file exists in the current directory or provide a full path!", err=True)
            return
        if type == "custom" and not custom_type:
            click.echo("Please specify a --custom-type (e.g., JFIF) for custom wiping!", err=True)
            return
        click.echo(f"Wiping {type} metadata...")
        ops = MetadataOperations()
        result = ops.wipe_metadata(str(abs_path), type, comment, custom_type)
        if result:
            click.echo(result)
        else:
            click.echo("Failed to wipe metadata. Check the file!")
    except Exception as e:
        click.echo(f"Error: {str(e)}. On Windows, check C:\\Users\\<YourUser>\\AppData\\Local\\autoexif\\exiftool.exe and exiftool_files\\. On Linux: sudo apt install libimage-exiftool-perl.", err=True)

@cli.command()
@click.argument("path")
def gps(path):
    """Extract GPS data from an image or video.

    Example: autoexif gps video.mp4
    """
    try:
        if path.startswith("http"):
            click.echo("Sorry, GPS extraction works only with local files, not URLs!", err=True)
            return
        abs_path = Path(path).resolve()
        if not validate_path(abs_path):
            click.echo(f"Oops, file not found: {path}. Check the file exists in the current directory or provide a full path!", err=True)
            return
        click.echo("Extracting GPS data...")
        ops = MetadataOperations()
        result = ops.extract_gps(str(abs_path))
        if result:
            click.echo(result)
        else:
            click.echo("No GPS data found. Try another file!")
    except Exception as e:
        click.echo(f"Error: {str(e)}. On Windows, check C:\\Users\\<YourUser>\\AppData\\Local\\autoexif\\exiftool.exe and exiftool_files\\. On Linux: sudo apt install libimage-exiftool-perl.", err=True)

@cli.command()
@click.argument("path")
def thumbnail(path):
    """Extract thumbnail metadata from an image.

    Example: autoexif thumbnail sample.jpg
    """
    try:
        ops = MetadataOperations()
        if path.startswith("http"):
            if not validate_url(path):
                click.echo("Oops, that URL looks invalid! Try something like https://example.com/image.jpg.", err=True)
                return
            click.echo("Fetching thumbnail metadata from URL...")
            result = ops.extract_thumbnail(path, is_url=True)
        else:
            abs_path = Path(path).resolve()
            if not validate_path(abs_path):
                click.echo(f"Oops, file not found: {path}. Check the file exists in the current directory or provide a full path!", err=True)
                return
            click.echo("Extracting thumbnail metadata...")
            result = ops.extract_thumbnail(str(abs_path), is_url=False)
        
        if result:
            click.echo(result)
        else:
            click.echo("No thumbnail metadata found. Try another image!")
    except Exception as e:
        click.echo(f"Error: {str(e)}. On Windows, check C:\\Users\\<YourUser>\\AppData\\Local\\autoexif\\exiftool.exe and exiftool_files\\. On Linux: sudo apt install libimage-exiftool-perl.", err=True)

@cli.command()
@click.argument("path")
def expert(path):
    """Extract metadata from all ExifTool tag groups.

    Example: autoexif expert sample.jpg
    """
    try:
        if path.startswith("http"):
            click.echo("Sorry, expert mode works only with local files, not URLs!", err=True)
            return
        abs_path = Path(path).resolve()
        if not validate_path(abs_path):
            click.echo(f"Oops, file not found: {path}. Check the file exists in the current directory or provide a full path!", err=True)
            return
        click.echo("Extracting metadata from all tag groups...")
        ops = MetadataOperations()
        result = ops.expert_metadata(str(abs_path))
        if result:
            click.echo(result)
        else:
            click.echo("No metadata extracted. Try another file!")
    except Exception as e:
        click.echo(f"Error: {str(e)}. On Windows, check C:\\Users\\<YourUser>\\AppData\\Local\\autoexif\\exiftool.exe and exiftool_files\\. On Linux: sudo apt install libimage-exiftool-perl.", err=True)

if __name__ == "__main__":
    cli()