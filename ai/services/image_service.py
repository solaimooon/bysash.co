# import base64
#
# from pathlib import Path
#
# from django.conf import settings
#
# from openai import OpenAI
#
#
# class AIImageService:
#
#     def __init__(self):
#
#         self.client = OpenAI(
#             base_url=settings.GAPGPT_BASE_URL,
#             api_key=settings.GAPGPT_API_KEY,
#         )
#
#     def edit_image(
#             self,
#             image,
#             prompt,
#             size="1024x1024",
#     ):
#         result = self.client.images.edit(
#             model="gpt-image-2",
#             image=image,
#             prompt=prompt,
#             size=size,
#         )
#
#         image_data = result.data[0].b64_json
#
#
#
#         return base64.b64decode(image_data)
#
#     def edit_django_image(
#             self,
#             django_image,
#             prompt,
#             size="1024x1024",
#     ):
#         """
#         Edit a Django ImageField file using GPT Image.
#         """
#
#         django_image.open("rb")
#
#         try:
#
#             result = self.client.images.edit(
#                 model="gpt-image-2",
#                 image=django_image.file,
#                 prompt=prompt,
#                 size=size,
#             )
#
#         finally:
#
#             django_image.close()
#
#         image_data = result.data[0].b64_json
#
#         if not image_data:
#             raise ValueError(
#                 "AI did not return image data."
#             )
#
#         import base64
#
#         return base64.b64decode(image_data)


import base64
import io

from django.conf import settings
from openai import OpenAI


class AIImageService:

    def __init__(self):

        self.client = OpenAI(
            base_url=settings.GAPGPT_BASE_URL,
            api_key=settings.GAPGPT_API_KEY,
        )

    def edit_image(
            self,
            image,
            prompt,
            size="1024x1024",
    ):
        result = self.client.images.edit(
            model="gpt-image-2",
            image=image,
            prompt=prompt,
            size=size,
        )

        image_data = result.data[0].b64_json

        if not image_data:
            raise ValueError(
                "AI did not return image data."
            )

        return base64.b64decode(image_data)

    def edit_django_image(
            self,
            django_image,
            prompt,
            size="1024x1024",
    ):
        """
        Edit a Django ImageField file using GPT Image.
        """

        django_image.open("rb")

        try:
            image_bytes = django_image.read()

            image_file = io.BytesIO(image_bytes)

            result = self.client.images.edit(
                model="gpt-image-2",
                image=image_file,
                prompt=prompt,
                size=size,
            )

        finally:
            django_image.close()

        image_data = result.data[0].b64_json

        if not image_data:
            raise ValueError(
                "AI did not return image data."
            )

        return base64.b64decode(image_data)