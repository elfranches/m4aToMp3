import os
import subprocess

folder_path = '/your/folder/path/'

items = os.listdir(folder_path)

for item in items:
    item_path = os.path.join(folder_path, item)

    if os.path.isfile(item_path) and item.lower().endswith('.m4a'):
        new_name = os.path.splitext(item)[0] + '.mp3'
        new_path = os.path.join(folder_path, new_name)

        # Use FFmpeg to convert the file
        subprocess.run(['ffmpeg', '-i', item_path, new_path])

        print(f"Converted '{item}' to '{new_name}'")
