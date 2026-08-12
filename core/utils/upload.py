import os
import uuid

from django.utils import timezone

from django.utils.deconstruct import deconstructible

@deconstructible
class UploadToPath:
    def __init__(self, folder_name):
        self.folder_name = folder_name

    def __call__(self, instance, filename):
        ext = os.path.splitext(filename)[1].lower()

        filename = f"{uuid.uuid4()}{ext}"

        today = timezone.now()

        return os.path.join(
            self.folder_name,
            str(today.year),
            f"{today.month:02}",
            filename,
        )