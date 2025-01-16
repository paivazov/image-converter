import os
import re
import uuid
from pathlib import Path

SAVE_DIR = "converted_images"


def create_filename_path(image_name: str, output_format: str) -> dict:
    dirname = os.getcwd()
    unique_code = str(uuid.uuid4())[:8]
    filename = re.match(r"(.*)\.\w+", image_name).group(1)
    converted_filename = f"{filename}_{unique_code}.{output_format}"
    return {"name": converted_filename, "full_path": os.path.join(dirname, SAVE_DIR, converted_filename)}


def create_save_dir():
    """
    Creating a directory for saving if it's not exist yet.
    """
    converted_images_dir = Path("converted_images")
    converted_images_dir.mkdir(parents=True, exist_ok=True)
