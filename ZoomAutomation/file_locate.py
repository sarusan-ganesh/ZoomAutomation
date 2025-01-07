import shutil
import os
from pathlib import Path

class FileMover:
   def __init__(self, destination_folder, directory):
      self.directory = Path(directory)
      self.destination_folder = Path(destination_folder)

   def get_most_recent_folder(self):
      all_items_in_directory = [os.path.join(self.directory, d) for d in os.listdir(self.directory) if
                                os.path.isdir(os.path.join(self.directory, d))]
      most_recent_folder = max(all_items_in_directory, key=os.path.getmtime, default=None)
      return Path(most_recent_folder) if most_recent_folder else None

   def move_files(self, file_base_name):
      most_recent_folder = self.get_most_recent_folder()
      moved_files = []

      if most_recent_folder:
         print(f"most recently created folder is: {most_recent_folder}")
         txt_path = most_recent_folder / "meeting_saved_chat.txt"
         mp4_path = next(most_recent_folder.glob("*.mp4"), None)

         if txt_path.exists():
            new_txt_path = self.destination_folder / f"{file_base_name}.txt"
            shutil.move(str(txt_path), str(new_txt_path))
            moved_files.append(str(new_txt_path))
         else:
            print("Text file 'meeting_chat.txt' not found.")

         if mp4_path and mp4_path.exists():
            new_mp4_path = self.destination_folder / f"{file_base_name}.mp4"
            shutil.move(str(mp4_path), str(new_mp4_path))
            moved_files.append(str(new_mp4_path))
         else:
            print("MP4 file not found.")

      else:
         print("No recent folder found in the directory.")

      return moved_files
      
