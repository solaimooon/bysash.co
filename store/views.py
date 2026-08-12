from django.views.generic import TemplateView, ListView

from store.services.product_service import ProductService
from store.models import Category,product


class HomeView(TemplateView):
    template_name = "store/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sliders"] = []

        context["categories"] = (
            Category.objects
            .all()
            .order_by("name")
        )

        context["featured_products"] = (
            ProductService.featured()[:12]
        )

        for product in context["featured_products"]:
            print(product.cover_image)

        return context


class ProductListView(ListView):

    model = product

    template_name = "store/shop.html"

    context_object_name = "products"

    paginate_by = 12

    def get_queryset(self):
        return ProductService.list_products()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = (
            Category.objects
            .filter(is_active=True)
            .order_by("name")
        )

        context["brands"] = (
            Brand.objects
            .filter(is_active=True)
            .order_by("name")
        )

        return context