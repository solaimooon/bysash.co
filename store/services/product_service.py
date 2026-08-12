from django.db.models import QuerySet

from store.models import Product


class ProductService:

    @staticmethod
    def base_queryset() -> QuerySet:
        return (
            Product.objects
            .filter(
                status="published",
            )
            .select_related("brand")
            .prefetch_related(
                "categories",
                "images",
            )
            .order_by("-created_at")
        )

    @classmethod
    def latest(cls) -> QuerySet:
        return cls.base_queryset().order_by("-created_at")

    @classmethod
    def featured(cls) -> QuerySet:
        return cls.base_queryset().filter(
            is_featured=True
        )

    @classmethod
    def by_category(cls, category_slug):
        return cls.base_queryset().filter(
            categories__slug=category_slug
        )

    @classmethod
    def by_brand(cls, brand_slug):
        return cls.base_queryset().filter(
            brand__slug=brand_slug
        )

    @classmethod
    def list_products(cls):
        """
        Return all published products.
        """
        return cls.base_queryset().order_by("-created_at")