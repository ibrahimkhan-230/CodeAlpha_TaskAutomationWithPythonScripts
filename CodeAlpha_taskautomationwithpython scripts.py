# Task Automation With Python Scipts
# Move all .jpg files from a folder to a new folder. 

import os
import shutil

source_folder = input("Enter the source folder path: ").strip()
destination_folder = input("Enter the destination folder path: ").strip()

# Create destination if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

moved_files = 0

for file_name in os.listdir(source_folder):
    if file_name.lower().endswith('.jpg'):
        src = os.path.join(source_folder, file_name)
        dst = os.path.join(destination_folder, file_name)
        shutil.move(src, dst)
        moved_files += 1

print(f"Moved {moved_files} JPG files to '{destination_folder}'.")