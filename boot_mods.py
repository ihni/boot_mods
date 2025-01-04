import os
import shutil

def copy_mods_with_prompts(mods_folder):
    try:
        # Step 1: Prompt to delete existing mods in the parent folder
        existing_files = [
            f for f in os.listdir(mods_folder)
            if os.path.isfile(os.path.join(mods_folder, f))
        ]
        
        if existing_files:
            print("The following files already exist in the main mods folder:")
            for file in existing_files:
                print(f" - {file}")
            
            delete_choice = input("Do you want to delete these files? (y/n): ").strip().lower()
            if delete_choice == 'y':
                for file in existing_files:
                    file_path = os.path.join(mods_folder, file)
                    os.remove(file_path)
                    print(f"Deleted: {file}")
        
        # Step 2: Copy files from subfolders to the parent folder
        for root, _, files in os.walk(mods_folder):
            if root == mods_folder:
                continue  # Skip the main mods folder itself
            
            print(f"\nProcessing folder: {root}")
            for file in files:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(mods_folder, file)
                
                # Check if the file already exists
                if os.path.exists(destination_path):
                    print(f"Duplicate found: {file}")
                    replace_choice = input(f"Do you want to replace {file}? (y/n): ").strip().lower()
                    if replace_choice != 'y':
                        print(f"Skipped: {file}")
                        continue
                
                # Copy the file to the main mods folder
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {file}")
        
        print("\nAll mods have been processed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the current working directory (assumed to be the mods folder)
    mods_folder_path = os.getcwd()
    
    # Check if the current directory is valid
    if os.path.exists(mods_folder_path) and os.path.isdir(mods_folder_path):
        print(f"Working in mods folder: {mods_folder_path}")
        copy_mods_with_prompts(mods_folder_path)
    else:
        print("Invalid mods folder path. Please ensure the script is in the mods folder.")
