"""This is the code used in the hda module to trigger the upload of the input data to Google Drive."""
import os
import sys
import hou
import time
from importlib import reload
import week3.gdrive_uploader as gdrive_uploader
reload(gdrive_uploader)

def save_and_upload_file():
    file_path = hou.pwd().parm("sopoutput").evalAsString()
    file_name = os.path.basename(file_path)

    for child in hou.pwd().children():
        if child.name() == "rop_geometry":
            print(f"Saving to {file_path}")
            child.parm("execute").pressButton()
    upload_file_wrapper(file_path, file_name)

def upload_file_wrapper(file_path, file_name):
    # Wait for the file to exist with a timeout of 10s
    timeout = 10
    start_time = time.time()
    while not os.path.exists(file_path):
        if time.time() - start_time > timeout:
            print(f"Timeout: File {file_name} did not exist after {timeout} seconds.")
            sys.exit()
        time.sleep(0.1)  # Check every 100ms

    print(f"Uploading {file_path} to Google Drive...")
    gdrive_uploader.upload_file(file_path, file_name)
    print("Done!")