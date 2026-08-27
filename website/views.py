from django.shortcuts import render
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


class AboutVIEW(TemplateView):
    template_name = "about.html"


class ContacUSVIEW(TemplateView):
    template_name = "contact.html"





