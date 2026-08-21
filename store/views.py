from django.views.generic import TemplateView, ListView,DetailView

from store.services.product_service import ProductService
from store.models import Category,Product,Brand
from django.http import Http404

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

    model = Product
    template_name = "store/shop.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        queryset = ProductService.list_products()

        category_slug = self.request.GET.get("category")
        brand_slug = self.request.GET.get("brand")

        if category_slug:
            queryset = queryset.filter(
                categories__slug=category_slug
            )

        if brand_slug:
            queryset = queryset.filter(
                brand__slug=brand_slug
            )

        return queryset.distinct()

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

        context["selected_category"] = self.request.GET.get("category")
        context["selected_brand"] = self.request.GET.get("brand")

        return context


class ProductDetailView(DetailView):

    model = Product

    template_name = "store/product.html"

    context_object_name = "product"

    slug_field = "slug"

    slug_url_kwarg = "slug"

    def get_object(self, queryset=None):

        product = ProductService.get_detail(
            self.kwargs["slug"]
        )

        if product is None:
            raise Http404("Product not found.")

        return product

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["variant_attributes"] = (
            ProductService.get_variant_attributes(
                self.object
            )
        )
        context["variants_data"] = (
            ProductService.get_variants_data(
                self.object
            )
        )

        return context