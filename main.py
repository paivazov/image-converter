from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pathlib import Path

from utils import create_filename_path, async_save_image

app = FastAPI()


@app.post("/convert")
async def convert_image(output_format: str, image: UploadFile = File()):
    """
    Async endpoint for converting an image to a specified format.
    """
    # Creating a directory for saving if it's not exist yet.
    converted_images_dir = Path("converted_images")
    converted_images_dir.mkdir(parents=True, exist_ok=True)

    # Reading image data
    image_data = await image.read()

    file_info = create_filename_path(image.filename, output_format)
    full_path = file_info["full_path"]

    # Asynchronously image save.
    await async_save_image(image_data, output_format, full_path)

    headers = {'Content-Disposition': f'attachment; filename="{file_info["name"]}"'}
    return FileResponse(full_path, headers=headers)
