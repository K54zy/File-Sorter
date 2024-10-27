import os
import shutil
from pathlib import Path

# Set the Downloads directory path
DOWNLOADS_DIR = Path.home() / "Downloads"

def create_folder(folder_path):
    """Creates a folder if it doesn't exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def file_sorter():
    """
    Sorts files in the Downloads directory into subdirectories based on their extensions.
    """
    # Create a dictionary to map file extensions to their respective directories
    extension_dirs = {
        "Documents": [".txt", ".doc", ".docx", ".pdf", ".odt", ".rtf"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Audio": [".mp3", ".wav", ".ogg", ".flac", ".aac"],
        "Zip": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Executables": [".exe", ".msi"],
        "Spreadsheets": [".xls", ".xlsx", ".ods"],
        "Presentations": [".ppt", ".pptx", ".odp"],
        "Others": []  # Catch-all for unknown extensions
    }

    # Iterate through files in the Downloads directory
    for filename in os.listdir(DOWNLOADS_DIR):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Find the corresponding directory for the file extension
        for dir_name, extensions in extension_dirs.items():
            if file_ext in extensions:
                # Create the directory if it doesn't exist
                folder_path = DOWNLOADS_DIR / dir_name
                create_folder(folder_path)

                # Move the file to the corresponding directory
                shutil.move(DOWNLOADS_DIR / filename, folder_path / filename)
                print(f"Moved {filename} to {dir_name}")
                break
        else:
            # If the extension is unknown, move it to the 'Others' directory
            folder_path = DOWNLOADS_DIR / "Others"
            create_folder(folder_path)
            shutil.move(DOWNLOADS_DIR / filename, folder_path / filename)
            print(f"Moved {filename} to Others")

if __name__ == "__main__":
    file_sorter()