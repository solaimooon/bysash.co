import re


def persian_slugify(text: str) -> str:
    """
    Generate Persian slug.
    """

    text = text.strip()

    text = text.replace("_", " ")

    text = re.sub(r"\s+", "-", text)

    text = re.sub(r"[^\w\u0600-\u06FF\-]", "", text)

    text = re.sub(r"-{2,}", "-", text)

    return text.lower()


def generate_unique_slug(instance, value):

    base_slug = persian_slugify(value)

    slug = base_slug

    Model = instance.__class__

    counter = 2

    while (
        Model.objects
        .filter(slug=slug)
        .exclude(pk=instance.pk)
        .exists()
    ):

        slug = f"{base_slug}-{counter}"

        counter += 1

    return slug