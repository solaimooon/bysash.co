from core.services.slug import generate_unique_slug

# این میکسین برای هر مدلی قابل استفاده است.
# فقط کافی است slug_source را مشخص کنید تا اسلاگ از روی آن ساخته شود.

class SlugMixin:
    slug_field = "slug"
    slug_source = "name"

    def save(self, *args, **kwargs):
        slug_field = getattr(self, "slug_field", "slug")
        slug_source = getattr(self, "slug_source", "name")

        if not hasattr(self, slug_source):
            raise AttributeError(
                f"{self.__class__.__name__} has no attribute '{slug_source}'."
            )

        if not hasattr(self, slug_field):
            raise AttributeError(
                f"{self.__class__.__name__} has no attribute '{slug_field}'."
            )

        slug = getattr(self, slug_field)

        if not slug:
            value = getattr(self, slug_source)

            setattr(
                self,
                slug_field,
                generate_unique_slug(
                    self,
                    value,
                ),
            )

        super().save(*args, **kwargs)