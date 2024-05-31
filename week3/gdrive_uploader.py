import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_file(file_path, file_name):
    # Create a GoogleAuth instance with client secrets file.
    gauth = GoogleAuth(settings_file="settings.yaml")
    gauth.LocalWebserverAuth()
    
    # Create GoogleDrive instance with authenticated GoogleAuth instance.
    drive = GoogleDrive(gauth)

    # Set the file content and upload the file.
    file1 = drive.CreateFile({"title": file_name})
    file1.SetContentFile(file_path)
    file1.Upload()
    print("title: " + file1["title"] + ", id: " + file1["id"])

# Usage
upload_file(os.path.join(os.getcwd(), "hello.txt"), "hello.txt")
