import os
import shutil

# ANSI escape codes for coloring
class Colors:
    RESET = "\033[0m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"

def find_minecraft_mods_dir():
    """
    Locate the .minecraft/mods directory by going up to the parent .minecraft folder
    where the script resides and ensuring the mods folder exists.
    """
    # Get the parent .minecraft directory
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
    minecraft_dir = os.path.abspath(os.path.join(script_dir, ".."))  # Go one level up to .minecraft
    
    # Define the mods folder path in .minecraft
    minecraft_mods_dir = os.path.join(minecraft_dir, "mods")
    if not os.path.exists(minecraft_mods_dir):
        print(f"{Colors.YELLOW}Creating Minecraft mods directory at {minecraft_mods_dir}.{Colors.RESET}")
        os.makedirs(minecraft_mods_dir)
    
    return minecraft_mods_dir

def collect_jar_files(source_dir):
    """Recursively find all .jar files in the source directory."""
    jar_files = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".jar"):
                jar_files.append(os.path.join(root, file))
    return jar_files

def copy_mods_to_minecraft(source_dir, target_dir):
    """Copy all .jar files from source_dir to target_dir."""
    jar_files = collect_jar_files(source_dir)
    if not jar_files:
        print(f"{Colors.RED}No .jar files found in {source_dir}.{Colors.RESET}")
        return