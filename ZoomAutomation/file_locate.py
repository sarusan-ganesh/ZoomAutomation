import shutil
from pathlib import Path


mp4_name = input("Enter name of mp4: ")
txt_name = input("Enter name of txt: ")

source_file = Path(r"C:\Users\saru-\Documents\Zoom\2024-12-23 19.59.12 DrJoeAcademyUSL1BSRSN_CHARLIEMON5-6PMPDT8-9PMEDTSTART20240909")
destination_file = Path(fr"C:\Users\saru-\Documents\Always Zen Tutoring\{new_name}")


# Check if the source folder exists and is a directory
if source_file.exists() and source_file.is_dir():
   # Ensure the destination folder exists
   destination_file.parent.mkdir(parents=True, exist_ok=True)  # This ensures the parent folder of Documents exists


   # Move the folder
   shutil.move(str(source_file), str(destination_file))
   print(f"Folder 'FLIGHT DETAILS' moved successfully to {destination_file}")
else:
   print(f"The folder 'FLIGHT DETAILS' does not exist on your Desktop.")

