"""This is the code used in the hda module to trigger the upload of the input data to Google Drive."""

import os
from importlib import reload
import hou #type: ignore
from week3 import gdrive_uploader
reload(gdrive_uploader)


def save_and_upload_file() -> None:
    """Save the file to disk with the rop_geometry node and upload it to Google Drive."""
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
