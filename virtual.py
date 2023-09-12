#This code sorts loose files from my downloads into folders on my desktop ( I eventually used automator to link the script to a command on my keyboard)
import os
import shutil


download_folder = "/users/lukapanos/downloads"

# Specify the destination folder path on your desktop
desktop_folder = "/users/lukapanos/desktop"

# Create dictionaries to map file extensions to folders
file_categories = {
    "pdf": "Documents",
    "docx": "Documents",
    "wfpbundle": "Documents",
    "jpg": "Images",
    "png": "Images",
    "mp4": "Videos",
    "mp3": "Videos",
    "csv": "Documents",
    "dmg": "Documents",
    "rw2": "Documents",
    "wfp": "Documents",
    # Add more mappings here
}

# List files in the download folder
downloaded_files = os.listdir(download_folder)

# Iterate through downloaded files
for filename in downloaded_files:
    file_extension = filename.split(".")[-1].lower()

    if file_extension in file_categories:
        category_folder = os.path.join(desktop_folder, file_categories[file_extension])
        if not os.path.exists(category_folder):
                os.makedirs(category_folder)

        source_path = os.path.join(download_folder, filename)
        target_path = os.path.join(category_folder, filename)

        shutil.move(source_path, target_path)
        print(f"Moved {filename} to {category_folder}")

print("File sorting completed.")

