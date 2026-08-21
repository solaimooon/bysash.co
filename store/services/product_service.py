from django.db.models import QuerySet
from django.db.models import Prefetch
from store.models import (
    Product,
    Variant,
    VariantAttribute,
)


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

    @classmethod
    def get_by_slug(cls, slug):
        return (
            cls.base_queryset()
            .filter(slug=slug)
            .first()
        )

    @classmethod
    def get_detail(cls, slug):
        return (
            cls.base_queryset()
            .filter(
                slug=slug,
                status="published",
                is_active=True,
            )
            .prefetch_related(
                "images",
                Prefetch(
                    "variants",
                    queryset=Variant.objects
                    .filter(is_active=True)
                    .prefetch_related(
                        Prefetch(
                            "variant_attributes",
                            queryset=VariantAttribute.objects
                            .select_related(
                                "attribute_value__attribute"
                            )
                        )
                    )
                )
            )
            .select_related(
                "brand",
            )
            .first()
        )

    @classmethod
    def get_variant_attributes(cls, product):
        attributes = {}

        for variant in product.variants.all():

            for variant_attribute in variant.variant_attributes.all():

                attribute_value = variant_attribute.attribute_value
                attribute = attribute_value.attribute

                if not attribute.is_active:
                    continue

                attribute_type = attribute.attribute_type

                if attribute_type not in attributes:
                    attributes[attribute_type] = {
                        "attribute": attribute,
                        "values": [],
                    }

                if attribute_value not in attributes[attribute_type]["values"]:
                    attributes[attribute_type]["values"].append(
                        attribute_value
                    )

        return attributes

    @classmethod
    def get_variants_data(cls, product):

        variants = []

        for variant in product.variants.all():

            attributes = {}

            for variant_attribute in variant.variant_attributes.all():
                attribute_value = variant_attribute.attribute_value
                attribute = attribute_value.attribute

                attributes[attribute.attribute_type] = {
                    "id": attribute_value.id,
                    "value": attribute_value.value,
                }

            variants.append({
                "id": variant.id,
                "sku": variant.sku,
                "price": variant.price,
                "discount_price": variant.discount_price,
                "stock": variant.stock,
                "is_default": variant.is_default,
                "attributes": attributes,
            })

        return variants