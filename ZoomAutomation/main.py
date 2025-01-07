from file_locate import FileMover
#from email_sender import EmailSender
#from pathlib import Path

destination = r"C:\Users\saru-\Documents\Always Zen Tutoring"
original_directory = r"C:\Users\saru-\Documents\Zoom"
file_mover = FileMover(destination, original_directory)

file_name = input("Enter the name of the file (without extension): ")
moved_files = file_mover.move_files(file_name)

# Email sending logic
'''
email_content = EmailSender(
    from_address="sarusan.ganesh@gmail.com",
    to_address="sarusan.g99@gmail.com",
    password="usccvvlooqeisnet",  # app password provided by Google
    subject="Python Test",
    body="I sent this from Python, and it includes attachments."
)
email_content.send_email(attachments)
'''

if moved_files:
    print("files moved successfully: ")
    for file in moved_files:
        print(file)
    else:
        print("no files were moved")