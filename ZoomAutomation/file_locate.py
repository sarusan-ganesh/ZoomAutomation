import shutil
import os
from pathlib import Path


file_base_name = input("Enter the name of file: ")
mp4_name = f"{file_base_name}.mp4"
txt_name = f"{file_base_name}.txt"

destination_folder = Path(fr"C:\Users\saru-\Documents\Always Zen Tutoring")
directory = r"C:\Users\saru-\Documents\Zoom"
all_items_in_directory = [os.path.join(directory, d) for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
most_recent_folder_str = max(all_items_in_directory, key=os.path.getmtime, default=None)

if most_recent_folder_str:
   # convert to a path object
   most_recent_folder = Path(most_recent_folder_str)
   print(f"most recently created folder is: {most_recent_folder}")

   if most_recent_folder.exists() and most_recent_folder.is_dir():
      # Ensure the destination folder exists
      destination_folder.parent.mkdir(parents=True, exist_ok=True)  # This ensures the parent folder of Documents exists

      #search for each path
      mp4_path = most_recent_folder / mp4_name
      txt_path = most_recent_folder / txt_name

      if mp4_path.exists():
         shutil.move(str(mp4_path), str(destination_folder))
         print(f"Moved mp4 file: {mp4_name} to {destination_folder}")

      else:
         print(f"mp4 file {mp4_name} not found in {most_recent_folder}")

      if txt_path.exists():
         shutil.move(str(txt_path), str(destination_folder))
         print(f"Moved txt file: {txt_name} to {destination_folder}")

      else:
         print(f"txt file {txt_name} not found in {most_recent_folder}")

