import os
from django.conf import settings
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "bysash.settings",
)

import django

django.setup()


from pathlib import Path

from ai.services.image_service import AIImageService


service = AIImageService()


image_path = Path(
    r"C:\Users\solai\Desktop\images.jpg"
)


prompt = """
Edit this product photo for a professional fashion e-commerce store.

Keep the clothing product itself unchanged.

Remove the existing background and replace it with
a clean, premium, minimal studio background.

Improve lighting and image quality while keeping
the original product appearance realistic.

Do not change the color, shape, design, or details
of the clothing.
"""


image_bytes = service.edit_image(
    image_path=image_path,
    prompt=prompt,
)


output_path = Path(
    r"C:\Users\solai\Desktop\service-test.png"
)


with output_path.open("wb") as output_file:

    output_file.write(image_bytes)


print(
    f"Image saved: {output_path}"
)

print("BASE URL:", settings.GAPGPT_BASE_URL)
print("KEY EXISTS:", bool(settings.GAPGPT_API_KEY))
print("KEY PREFIX:", settings.GAPGPT_API_KEY[:10] if settings.GAPGPT_API_KEY else None)