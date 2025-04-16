import click
import sys
import os
from pathlib import Path
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.history import FileHistory
from .exiftool import ExifTool
from .operations import MetadataOperations
from .utils import validate_path, validate_url, find_image_in_directory

# ANSI-like styles for TUI
style = Style.from_dict({
    'red': '#ff0000 bold',
    'blue': '#0000ff bold',
    'yellow': '#ffff00 bold',
    'green': '#00ff00 bold',
    'magenta': '#ff00ff bold',
    'cyan': '#00ffff bold',
    'reset': '#ffffff',
})

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def run_tui():
    """Run the interactive TUI."""
    history = FileHistory(Path.home() / ".autoexif_history")
    session = PromptSession(history=history, style=style, enable_history_search=True)
    ops = MetadataOperations()
    
    while True:
        clear_screen()
        print("""
                ▌║█║▌│║▌│║▌║▌█║AutoExif▌│║▌║▌│║║▌█║▌║█
┌───────────────────────────────────────────────────────────────────┐
│Exif Tool AutoMated For Easy Conveinience Created by "SirCryptic"  │
└───────────────────────────────────────────────────────────────────┘
┌───────────────────────────────────────────────────────────────────┐
│(1) Read Image MetaData (Basic)                                    │
│(2) Read Image MetaData (Expert)                                   │
│(3) Read Image MetaData (From Website)                             │
│(4) Wipe Data From Image (Except JFIF Groups)                      │
│(5) Wipe All GPS Data From Image                                   │
│(6) Wipe All MetaData From Image (Adds Comment Back In)            │
│(7) Extract GPS from AVCH video                                    │
│(8) Extract Info From Thumbnail                                    │
│(9) Wipe Photoshop MetaData                                        │
│(h) Help                                                           │
├───────────────────────────────────────────────────────────────────┤
│(q) Press q/Q to quit                                              │
└───────────────────────────────────────────────────────────────────┘
""")
        choice = session.prompt("┌─[Auto]──[~]─[Exif]:\n└─────► ", rprompt="", multiline=False).strip().lower()
        
        if choice == 'q':
            clear_screen()
            print("Exiting AutoExif. Goodbye!")
            break
        
        elif choice == '1':
            clear_screen()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘
""")
            file_path = session.prompt("└─────► ").strip()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│                          Extracting Data!                         │
└───────────────────────────────────────────────────────────────────┘
""")
            try:
                if file_path:
                    abs_path = Path(file_path).resolve()
                    if not validate_path(abs_path):
                        print("Error: File not found. Check the path.")
                    else:
                        result = ops.read_metadata(str(abs_path), detailed=False)
                        print(result or "No metadata found.")
                else:
                    current_dir = Path.cwd()
                    image_path = find_image_in_directory(current_dir)
                    if not image_path:
                        print("No image found in current directory.")
                    else:
                        result = ops.read_metadata(str(image_path.resolve()), detailed=False)
                        print(result or "No metadata found.")
                print("""
┌───────────────────────────────────────────────────────────────────┐
│                 Data Extracted Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘
""")
            except Exception as e:
                print(f"Error: {e}")
            session.prompt("└─────► ")
        
        elif choice == '2':
            clear_screen()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘
""")
            file_path = session.prompt("└─────► ").strip()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│                          Extracting Data!                         │
└───────────────────────────────────────────────────────────────────┘
""")
            try:
                abs_path = Path(file_path).resolve()
                if not validate_path(abs_path):
                    print("Error: File not found. Check the path.")
                else:
                    result = ops.read_metadata(str(abs_path), detailed=True)
                    print(result or "No metadata found.")
                print("""
┌───────────────────────────────────────────────────────────────────┐
│                 Data Extracted Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘
""")
            except Exception as e:
                print(f"Error: {e}")
            session.prompt("└─────► ")
        
        elif choice == '3':
            clear_screen()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│          usage example: http://a.domain.com/bigfile.jpg           │
├───────────────────────────────────────────────────────────────────┘
""")
            file_url = session.prompt("└─────► ").strip()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│                          Extracting Data!                         │
└───────────────────────────────────────────────────────────────────┘
""")
            try:
                if not validate_url(file_url):
                    print("Error: Invalid URL.")
                else:
                    result = ops.read_web_metadata(file_url)
                    print(result or "No metadata found.")
                print("""
┌───────────────────────────────────────────────────────────────────┐
│                 Data Extracted Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘
""")
            except Exception as e:
                print(f"Error: {e}")
            session.prompt("└─────► ")
        
        elif choice == '4':
            clear_screen()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘
""")
            file_path = session.prompt("└─────► ").strip()
            data_type = session.prompt("Enter data type to wipe (JFIF/GPS): ").strip()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│                          Wiping Data!                             │
└───────────────────────────────────────────────────────────────────┘
""")
            try:
                abs_path = Path(file_path).resolve()
                if not validate_path(abs_path):
                    print("Error: File not found. Check the path.")
                else:
                    result = ops.wipe_metadata(str(abs_path), type="custom", custom_type=data_type)
                    print(result or "Failed to wipe metadata.")
                print("""
┌───────────────────────────────────────────────────────────────────┐
│                     Data Wiped Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘
""")
            except Exception as e:
                print(f"Error: {e}")
            session.prompt("└─────► ")
        
        elif choice == '5':
            clear_screen()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘
""")
            file_path = session.prompt("└─────► ").strip()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│                          Wiping GPS Data!                         │
└───────────────────────────────────────────────────────────────────┘
""")
            try:
                abs_path = Path(file_path).resolve()
                if not validate_path(abs_path):
                    print("Error: File not found. Check the path.")
                else:
                    result = ops.wipe_metadata(str(abs_path), type="gps")
                    print(result or "Failed to wipe metadata.")
                print("""
┌───────────────────────────────────────────────────────────────────┐
│                     Data Wiped Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘
""")
            except Exception as e:
                print(f"Error: {e}")
            session.prompt("└─────► ")
        
        elif choice == '6':
            clear_screen()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘
""")
            file_path = session.prompt("└─────► ").strip()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│                          Replacing Data!                          │
└───────────────────────────────────────────────────────────────────┘
""")
            try:
                abs_path = Path(file_path).resolve()
                if not validate_path(abs_path):
                    print("Error: File not found. Check the path.")
                else:
                    result = ops.wipe_metadata(str(abs_path), type="all", comment="Protected By NULLSecurity Team - AutoExif")
                    print(result or "Failed to wipe metadata.")
                print("""
┌───────────────────────────────────────────────────────────────────┐
│                     Data Replaced Using AutoExif                  │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘
""")
            except Exception as e:
                print(f"Error: {e}")
            session.prompt("└─────► ")
        
        elif choice == '7':
            clear_screen()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Videos/lulz.m2ts           │
├───────────────────────────────────────────────────────────────────┘
""")
            file_path = session.prompt("└─────► ").strip()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│                          Extracting Data!                         │
└───────────────────────────────────────────────────────────────────┘
""")
            try:
                abs_path = Path(file_path).resolve()
                if not validate_path(abs_path):
                    print("Error: File not found. Check the path.")
                else:
                    result = ops.extract_gps(str(abs_path))
                    print(result or "No GPS data found.")
                print("""
┌───────────────────────────────────────────────────────────────────┐
│                 Data Extracted Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘
""")
            except Exception as e:
                print(f"Error: {e}")
            session.prompt("└─────► ")
        
        elif choice == '8':
            clear_screen()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘
""")
            file_path = session.prompt("└─────► ").strip()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│                          Extracting Data!                         │
└───────────────────────────────────────────────────────────────────┘
""")
            try:
                abs_path = Path(file_path).resolve()
                if not validate_path(abs_path):
                    print("Error: File not found. Check the path.")
                else:
                    result = ops.extract_thumbnail(str(abs_path), is_url=False)
                    print(result or "No thumbnail metadata found.")
                print("""
┌───────────────────────────────────────────────────────────────────┐
│                 Data Extracted Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘
""")
            except Exception as e:
                print(f"Error: {e}")
            session.prompt("└─────► ")
        
        elif choice == '9':
            clear_screen()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│        Delete Photoshop meta information from an image            │
├───────────────────────────────────────────────────────────────────┤
│    (note that the Photoshop information also includes IPTC).      │
└───────────────────────────────────────────────────────────────────┘
""")
            file_path = session.prompt("└─────► ").strip()
            print("""
┌───────────────────────────────────────────────────────────────────┐
│                          Extracting Data!                         │
└───────────────────────────────────────────────────────────────────┘
""")
            try:
                abs_path = Path(file_path).resolve()
                if not validate_path(abs_path):
                    print("Error: File not found. Check the path.")
                else:
                    result = ops.wipe_metadata(str(abs_path), type="photoshop")
                    print(result or "Failed to wipe metadata.")
                print("""
┌───────────────────────────────────────────────────────────────────┐
│                 Data Extracted Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘
""")
            except Exception as e:
                print(f"Error: {e}")
            session.prompt("└─────► ")
        
        elif choice == 'h':
            clear_screen()
            print("""
┌─────────────────────────────────────────────────────────────────────────────┐
│ AutoExif CLI offers an interactive menu (select 1-9) or command-line mode.   │
│ In the menu, enter the option number to process files or URLs.              │
│ For local files, use the file name (e.g., lulz.png) if in the current       │
│ directory, or the full path (e.g., /home/user/Pictures/lulz.png).           │
│ For URLs, provide the full address (e.g., http://example.com/image.jpg).    │
│ Command-line mode: run 'autoexif read lulz.png' or 'autoexif help' for      │
│ details. Use arrow keys to recall previous inputs.                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                  Press ENTER To Go Back To The Main Menu                    │
└─────────────────────────────────────────────────────────────────────────────┘
""")
            session.prompt("└─────► ")
        
        else:
            print("Invalid option. Please try again.")
            session.prompt("Press ENTER to continue... ")

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """AutoExif CLI - Easy metadata extraction and manipulation.

    Run 'autoexif' for interactive menu or 'autoexif help' for commands.
    """
    if ctx.invoked_subcommand is None:
        run_tui()

@cli.command()
def help():
    """Show detailed help with examples."""
    click.echo("""
AutoExif CLI v1.0 - Metadata Tool by SirCryptic

Easily extract, wipe, or analyze metadata from images, videos, or URLs.
Run 'autoexif' for interactive menu.

Interactive Menu:
  Select options 1-9 to process files/URLs.
  Use file names (e.g., lulz.png) or full paths (e.g., C:\\Users\\user\\Pictures\\lulz.png).
  For URLs, use full addresses (e.g., http://example.com/image.jpg).
  Press 'h' for tips, 'q' to quit.

Commands:
  help           Show this help message with examples
  read           Extract basic or detailed metadata
  wipe           Remove metadata (GPS, all, Photoshop, or custom)
  gps            Extract GPS data from images or videos
  thumbnail      Analyze thumbnail metadata
  expert         Extract metadata from all ExifTool tag groups

Examples:
  autoexif read sample.jpg
  autoexif read sample.jpg --detailed
  autoexif read https://example.com/image.jpg
  autoexif wipe sample.jpg --type gps
  autoexif gps video.mp4
  autoexif thumbnail sample.jpg
  autoexif expert sample.jpg

Ethical Use:
  Only process files or URLs you have permission to analyze.
    """)

@cli.command()
@click.argument("path", required=False)
@click.option("--detailed", is_flag=True, help="Extract detailed metadata")
def read(path, detailed):
    """Extract metadata from a file or URL."""
    try:
        ops = MetadataOperations()
        if not path:
            current_dir = Path.cwd()
            image_path = find_image_in_directory(current_dir)
            if not image_path:
                click.echo("No image found in current directory.", err=True)
                return
            click.echo(f"Reading metadata from file: {image_path.name}...")
            result = ops.read_metadata(str(image_path.resolve()), detailed)
        elif path.startswith("http"):
            if not validate_url(path):
                click.echo("Invalid URL.", err=True)
                return
            click.echo("Fetching metadata from URL...")
            result = ops.read_web_metadata(path)
        else:
            abs_path = Path(path).resolve()
            if not validate_path(abs_path):
                click.echo(f"File not found: {path}.", err=True)
                return
            click.echo("Reading metadata from file...")
            result = ops.read_metadata(str(abs_path), detailed)
        
        click.echo(result or "No metadata found.")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@cli.command()
@click.argument("path")
@click.option("--type", type=click.Choice(["gps", "all", "photoshop", "custom"]), default="all", help="Metadata type to wipe")
@click.option("--comment", help="Add a custom comment after wiping")
@click.option("--custom-type", help="Specific metadata type to wipe (e.g., JFIF) for --type custom")
def wipe(path, type, comment, custom_type):
    """Wipe metadata from a local file."""
    try:
        if path.startswith("http"):
            click.echo("Wiping metadata works only with local files.", err=True)
            return
        abs_path = Path(path).resolve()
        if not validate_path(abs_path):
            click.echo(f"File not found: {path}.", err=True)
            return
        if type == "custom" and not custom_type:
            click.echo("Please specify a --custom-type (e.g., JFIF).", err=True)
            return
        click.echo(f"Wiping {type} metadata...")
        ops = MetadataOperations()
        result = ops.wipe_metadata(str(abs_path), type, comment, custom_type)
        click.echo(result or "Failed to wipe metadata.")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@cli.command()
@click.argument("path")
def gps(path):
    """Extract GPS data from an image or video."""
    try:
        if path.startswith("http"):
            click.echo("GPS extraction works only with local files.", err=True)
            return
        abs_path = Path(path).resolve()
        if not validate_path(abs_path):
            click.echo(f"File not found: {path}.", err=True)
            return
        click.echo("Extracting GPS data...")
        ops = MetadataOperations()
        result = ops.extract_gps(str(abs_path))
        click.echo(result or "No GPS data found.")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@cli.command()
@click.argument("path")
def thumbnail(path):
    """Extract thumbnail metadata from an image."""
    try:
        ops = MetadataOperations()
        if path.startswith("http"):
            if not validate_url(path):
                click.echo("Invalid URL.", err=True)
                return
            click.echo("Fetching thumbnail metadata from URL...")
            result = ops.extract_thumbnail(path, is_url=True)
        else:
            abs_path = Path(path).resolve()
            if not validate_path(abs_path):
                click.echo(f"File not found: {path}.", err=True)
                return
            click.echo("Extracting thumbnail metadata...")
            result = ops.extract_thumbnail(str(abs_path), is_url=False)
        
        click.echo(result or "No thumbnail metadata found.")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@cli.command()
@click.argument("path")
def expert(path):
    """Extract metadata from all ExifTool tag groups."""
    try:
        if path.startswith("http"):
            click.echo("Expert mode works only with local files.", err=True)
            return
        abs_path = Path(path).resolve()
        if not validate_path(abs_path):
            click.echo(f"File not found: {path}.", err=True)
            return
        click.echo("Extracting metadata from all tag groups...")
        ops = MetadataOperations()
        result = ops.expert_metadata(str(abs_path))
        click.echo(result or "No metadata extracted.")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

if __name__ == "__main__":
    cli()
