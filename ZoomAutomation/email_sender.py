import smtplib
from email.message import EmailMessage

class EmailSender:
    def __init__(self, from_address, to_address, password, subject, body):
        self.from_address = "sarusan.ganesh@gmail.com"
        self.to_address = "sarusan.g99@gmail.com"
        self.password = "usccvvlooqeisnet" # app password provided by google to bypass 2fa
        self.subject = "python test"
        self.body = "i sent this from python"

    def send_email(self):
        msg = EmailMessage()
        msg["From"] = self.from_address
        msg["To"] = self.to_address
        msg["Subject"] = self.subject
        msg.set_content(self.body)

        if attachments:
            for file_path in attachments:
                file = Path(file_path)
                if file.exists():
                    with open(file, "rb") as f:
                        file_data = f.read()
                        file_name = file.name
                        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
                else:
                    print(f"file not found: {file_path}")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(self.from_address, self.password)

        server.send_message(msg)


