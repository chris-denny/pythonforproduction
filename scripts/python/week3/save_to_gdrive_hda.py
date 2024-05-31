"""This is the code used in the hda module to trigger the upload of the input data to Google Drive."""
import os
import hou
from importlib import reload
import week3.gdrive_uploader as gdrive_uploader
reload(gdrive_uploader)

def save_and_upload_file():
    # Create file path and name
    file_path = hou.pwd().parm("sopoutput").evalAsString()
    file_name = os.path.basename(file_path)

    # Save the file using the rop_geometry node
    for child in hou.pwd().children():
        if child.name() == "rop_geometry":
            print(f"Saving to {file_path}")
            child.parm("execute").pressButton()

    # Send the file to the uploader
    gdrive_uploader.upload_file(file_path, file_name)