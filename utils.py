import re
import os
import uuid


def create_filename_path(image_name: str, output_format: str) -> dict:
    dirname = os.getcwd()
    unique_code = str(uuid.uuid4())[:8]
    filename = re.match(r"(.*)\.\w+", image_name).group(1)
    converted_filename = f"{filename}_{unique_code}.{output_format}"
    return {"name": converted_filename, "full_path": os.path.join(dirname, "converted_images", converted_filename)}
