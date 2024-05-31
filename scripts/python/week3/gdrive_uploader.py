import os
import sys
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def upload_file(file_path, file_name):
    # Check if the file exists.
    if not os.path.exists(file_path):
        print(f"{file_name} does not exist.")
        sys.exit()

    # Create a GoogleAuth instance with client secrets file.
    gauth = GoogleAuth(settings_file=os.path.join(os.path.dirname(__file__), "settings.yaml"))
    gauth.LocalWebserverAuth()
    
    # Create GoogleDrive instance with authenticated GoogleAuth instance.
    drive = GoogleDrive(gauth)

    # Set the file content and upload the file.
    file1 = drive.CreateFile({"title": file_name})
    file1.SetContentFile(file_path)
    print(f"Uploading {file_path} to Google Drive...")
    file1.Upload()
    print(f"Uploaded title: {file1['title']}, id: {file1['id']}")

