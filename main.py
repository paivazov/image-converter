from PIL import Image
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

from utils import create_filename_path

app = FastAPI()


@app.post("/convert")
def convert_image(output_format: str, image: UploadFile = File()):
    with Image.open(image.file) as logo:
        image_data = create_filename_path(image.filename, output_format)
        headers = {'Content-Disposition': f'attachment; filename="{image_data["name"]}"'}
        full_path = image_data["full_path"]
        logo.convert('RGB').save(full_path, format=output_format)
    return FileResponse(full_path, headers=headers)
