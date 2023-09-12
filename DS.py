import os 
import shutil 

desk_folder='/users/lukapanos/desktop' 

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

desk_files = os.listdir(desk_folder)

for desk_name in desk_files: 
    desk_source=desk_name.split(".")[-1].lower()

    if desk_source in file_categories: 
        category_folder = os.path.join(desk_folder, file_categories[desk_source])
        if not os.path.exists(category_folder):
                os.makedirs(category_folder)

        source_path = os.path.join(desk_folder, desk_name)
        target_path = os.path.join(category_folder, desk_name)

        shutil.move(source_path, target_path)
        print(f"Moved {desk_name} to {category_folder}")

print("File sorting completed.")