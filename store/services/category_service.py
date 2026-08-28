from django.db.models import Count, Q

from store.models import Category


class CategoryService:

    @classmethod
    def get_categories_page(cls):

        return (
            Category.objects
            .filter(
                parent__isnull=True,
            )
            .annotate(
                product_count=Count(
                    "products",
                    filter=Q(
                        products__status="published",
                        products__is_active=True,
                    ),
                    distinct=True,
                )
            )
            .order_by(
                "sort_order",
                "name",
            )
        )