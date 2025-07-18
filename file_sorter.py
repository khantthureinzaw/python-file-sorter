import os
import shutil
import sys

"""
Python File Sorter

This script automatically sorts files in a target folder into categorized subfolders based on file extensions.

Usage:
    python file_sorter.py [optional: path_to_target_folder]
"""

TARGET_FOLDER = sys.argv[1] if len(sys.argv) > 1 else input("Enter folder path: ")

if not os.path.exists(TARGET_FOLDER):
    print("The specified folder does not exist.")
    exit(1)


FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Books': ['.epub'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.ogg'],
    'Archives': ['.zip', '.rar'],
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

def sort_files():
    for root, dirs, files in os.walk(TARGET_FOLDER):
        for item in files:
            item_path = os.path.join(root, item)
            _, ext = os.path.splitext(item)
            category = get_category(ext)
    
            # Determine if file is in correct folder
            current_folder = os.path.basename(os.path.dirname(item_path))
            if category == current_folder:
                continue # Already in correct folder
    
            # Build the destination folder path
            category_folder = os.path.join(TARGET_FOLDER, category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)
    
            new_location = os.path.join(category_folder, item)
    
            # Handle duplicate filename conflicts
            if os.path.exists(new_location):
                base, extension = os.path.splitext(item)
                counter = 1
                while True:
                    new_name = f'{base}_{counter}{extension}'
                    new_location = os.path.join(category_folder, new_name)
    
                    if not os.path.exists(new_location):
                        print(f'Duplicate filename detected. Renamed {item} to {new_name}')
                        break
                    counter += 1
    
            shutil.move(item_path, new_location)
            print(f"Moved {item} -> {category}/")

if __name__ == "__main__":
    sort_files()