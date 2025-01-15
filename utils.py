import asyncio
import io
import os
import re
import uuid

from PIL import Image


async def save_image(image_data: bytes, output_format: str, full_path: str):
    """
    Emulation of async image conversion saving by executing a synchronous operation in a separate thread.
    """
    await asyncio.to_thread(_save_image, image_data, output_format, full_path)


def _save_image(image_data: bytes, output_format: str, full_path: str):
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
    return {"name": converted_filename, "full_path": os.path.join(dirname, "converted_images", converted_filename)}
