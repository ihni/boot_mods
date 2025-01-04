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

    for jar_file in jar_files:
        mod_name = os.path.basename(jar_file)  # Extract only the mod name
        target_path = os.path.join(target_dir, mod_name)
        if os.path.exists(target_path):
            print(f"{Colors.CYAN}Skipping existing mod: {mod_name}{Colors.RESET}")
        else:
            print(f"{Colors.GREEN}Copying {mod_name}{Colors.RESET} to {Colors.BLUE}.minecraft/mods{Colors.RESET}")
            shutil.copy2(jar_file, target_path)

def main():
    # Define the source directory (mod_loader/mods)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_dir = os.path.join(script_dir, "mods")

    if not os.path.exists(source_dir):
        print(f"{Colors.RED}Source mods directory not found: {source_dir}{Colors.RESET}")
        return

    # Find the target directory (.minecraft/mods)
    target_dir = find_minecraft_mods_dir()

    # Copy all mods
    print(f"{Colors.CYAN}Copying mods from {source_dir} to {target_dir}...{Colors.RESET}")
    copy_mods_to_minecraft(source_dir, target_dir)
    print(f"{Colors.GREEN}All mods have been successfully copied!{Colors.RESET}")

if __name__ == "__main__":
    main()
