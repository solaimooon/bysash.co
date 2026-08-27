from openai import OpenAI
from pathlib import Path
import base64


# --------------------------------------------------
# OpenAI Client
# --------------------------------------------------

client = OpenAI(
    base_url="https://api.gapgpt.app/v1",
    api_key="sk-6GGez5l7aPcbRIr8YVIkL4eXsE2cwLLMH5GHRCdnMJCQ4tZY",
)


# --------------------------------------------------
# Input Image
# --------------------------------------------------

image_path = Path(
    r"C:\Users\solai\Desktop\actk1r411wd2.jpg"
)


# --------------------------------------------------
# Send Image + Prompt
# --------------------------------------------------

with image_path.open("rb") as image_file:

    result = client.images.edit(
        model="gpt-image-2",

        image=image_file,

        prompt="""
        Edit this product photo for a professional fashion e-commerce store.

        Keep the clothing product itself unchanged.

        Remove the existing background and replace it with
        a clean, premium, minimal studio background.

        Improve lighting and image quality while keeping
        the original product appearance realistic.

        Do not change the color, shape, design, or details of the clothing.
        """,

        size="1024x1024",
    )


# --------------------------------------------------
# Get Base64 Image
# --------------------------------------------------

image_base64 = result.data[0].b64_json


if not image_base64:
    raise ValueError("No image data returned by API.")


# --------------------------------------------------
# Decode Base64
# --------------------------------------------------

image_bytes = base64.b64decode(image_base64)


# --------------------------------------------------
# Save Output
# --------------------------------------------------

output_path = Path(
    r"C:\Users\solai\Desktop\edited-product.png"
)


with output_path.open("wb") as output_file:

    output_file.write(image_bytes)


print("Image generated successfully.")
print(f"Output: {output_path}")