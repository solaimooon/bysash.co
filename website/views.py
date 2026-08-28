from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView
from store.services.product_service import ProductService
from store.models import Category,Product,Brand
from django.http import Http404
from website.models import HeroSlider
from django.shortcuts import redirect
from .models import ContactMessage

class HomeView(TemplateView):
    template_name = "store/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sliders"] = (
            HeroSlider.objects
            .filter(is_active=True)
            .order_by("sort_order", "-created_at")
        )

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


from django.contrib import messages
from django.db import DatabaseError, transaction
from django.shortcuts import redirect
from django.views.generic import TemplateView

from .models import ContactMessage


class ContactUSView(TemplateView):
    template_name = "contact.html"

    def post(self, request, *args, **kwargs):

        full_name = request.POST.get("full_name", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        # بررسی فیلدهای ضروری
        if not full_name or not phone or not subject or not message:
            messages.error(
                request,
                "لطفاً تمام فیلدهای الزامی را به‌درستی تکمیل کنید."
            )
            return redirect("website:contact")

        try:
            with transaction.atomic():
                ContactMessage.objects.create(
                    full_name=full_name,
                    phone=phone,
                    email=email,
                    subject=subject,
                    message=message,
                )

        except DatabaseError:
            messages.error(
                request,
                "در حال حاضر امکان ثبت پیام وجود ندارد. لطفاً دوباره تلاش کنید."
            )
            return redirect("website:contact")

        except Exception:
            messages.error(
                request,
                "خطایی در ثبت پیام رخ داد. لطفاً بعداً دوباره تلاش کنید."
            )
            return redirect("website:contact")

        messages.success(
            request,
            "پیام شما با موفقیت ثبت شد. به‌زودی با شما تماس می‌گیریم."
        )

        return redirect("website:contact")













