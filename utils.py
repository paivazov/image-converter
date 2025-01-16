import asyncio
import io
import os
import re
import uuid
from pathlib import Path

from PIL import Image

SAVE_DIR = "converted_images"


async def async_save_image(image_data: bytes, output_format: str, full_path: str):
    """
    Emulation of async image conversion saving by executing a synchronous operation in a separate thread.
    """
    await asyncio.to_thread(save_image, image_data, output_format, full_path)


def save_image(image_data: bytes, output_format: str, full_path: str):
    """
    Sync image conversion and saving.
    """
    with Image.open(io.BytesIO(image_data)) as logo:
        logo.convert("RGB").save(full_path, format=output_format)


def create_filename_path(image_name: str, output_format: str) -> dict:
    """
    Creates a unique file name and path for saving the converted image.
    """
    dirname = os.getcwd()
    unique_code = str(uuid.uuid4())[:8]
    filename = re.match(r"(.*)\.\w+", image_name).group(1)
    converted_filename = f"{filename}_{unique_code}.{output_format}"
    return {"name": converted_filename, "full_path": os.path.join(dirname, SAVE_DIR, converted_filename)}


def create_save_dir():
    """
    Creating a directory for saving if it's not exist yet.
    """
    converted_images_dir = Path(SAVE_DIR)
    converted_images_dir.mkdir(parents=True, exist_ok=True)
