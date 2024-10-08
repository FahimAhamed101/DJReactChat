from django.core.exceptions import ValidationError
from PIL import Image
import os

def validate_icon_image_size(image):
    if image:
        with Image.open(image) as img:
            if img.width > 80 or img.height > 80 :
                raise ValidationError(f"The maximum allowed image size is 70x70 px. your image size = {img.size}")


def validate_image_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    if not ext.lower() in valid_extensions:
        raise ValidationError(f"Unsupported image format. Supported formats = {valid_extensions}")