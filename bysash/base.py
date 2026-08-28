from pathlib import Path
import os.path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dtzh_4!l61$hi3z@ujmf+)v761g)*4ksu+-bhq-9nto=!r3t&r'
# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    "django.contrib.humanize",
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "pwa",
    'accounts',
    "core",
    "mptt",
    "store",
    'website',
    "ai",
    'django_ckeditor_5',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bysash.urls'
TEMPLATES_DIR = os.path.join(BASE_DIR, 'template')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bysash.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static_dir"]
STATIC_ROOT = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "accounts.User"

# config for cke editor

customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'items': ['heading', '|', 'bold', 'italic', 'link',
                      'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
        }

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
            'sourceEditing',  # خیلی مهم
        ],
        'mediaEmbed': {
            'previewsInData': True, },
        'htmlSupport': {
            'allow': [
                {
                    'name': 'iframe',
                    'attributes': True,
                    'classes': True,
                    'styles': True,
                },
            ]
        },
        'toolbar': {
            'items': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
                      'code', 'subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                      'bulletedList', 'numberedList', 'todoList', '|', 'blockQuote', 'imageUpload', '|',
                      'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                      'insertTable',
                      ],
            'shouldNotGroupWhenFull': 'true'
        },
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side', '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells',
                               'tableProperties', 'tableCellProperties'],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'}
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}

CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff"  # Possible values: "staff", "authenticated", "any"

# get the envoriment variable form .env
load_dotenv()
GAPGPT_API_KEY = os.getenv("GAPGPT_API_KEY")

GAPGPT_BASE_URL = os.getenv(
    "GAPGPT_BASE_URL"
)



# setting for pwa

PWA_APP_NAME = "bysash.co"
PWA_APP_DESCRIPTION = "فروشگاه اینترنتی پوشاک زنانه"
PWA_APP_THEME_COLOR = "#F9C129"
PWA_APP_BACKGROUND_COLOR = "#F9C129"
PWA_APP_DISPLAY = "standalone"
PWA_APP_SCOPE = "/"
PWA_APP_START_URL = "/"

PWA_APP_ICONS = [
    {
        "src": "/static/pwa_image/icon-192.png",
        "sizes": "192x192",
        "type": "image/png",
    },
    {
        "src": "/static/pwa_image/icon-512.png",
        "sizes": "512x512",
        "type": "image/png",
    },
]




# ============================================================
# JAZZMIN — bysash.co
# ============================================================

JAZZMIN_SETTINGS = {

    # --------------------------------------------------------
    # Brand
    # --------------------------------------------------------

    "site_title": "bysash.co | مدیریت فروشگاه",

    "site_header": "bysash.co",

    "site_brand": "bysash.co",

    "site_logo": "pwa_image/icon-192.png",

    "login_logo": "pwa_image/icon-192.png",

    "site_icon": "pwa_image/icon-192.png",

    "welcome_sign": "خوش آمدید به پنل مدیریت bysash.co",

    "copyright": "bysash.co",


    # --------------------------------------------------------
    # Layout
    # --------------------------------------------------------

    "show_sidebar": True,

    "navigation_expanded": True,

    "hide_apps": [],

    "hide_models": [],

    "order_with_respect_to": [
        "shop",
        "orders",
        "products",
        "customers",
        "auth",
    ],


    # --------------------------------------------------------
    # Search
    # --------------------------------------------------------

    "search_model": [
        "shop.Product",
        "orders.Order",
        "accounts.User",
    ],


    # --------------------------------------------------------
    # Icons
    # --------------------------------------------------------

    "icons": {

        # Django
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",

        # محصولات
        "shop": "fas fa-store",
        "shop.Product": "fas fa-box-open",
        "shop.Category": "fas fa-tags",

        # سفارش‌ها
        "orders": "fas fa-shopping-cart",
        "orders.Order": "fas fa-receipt",

        # کاربران
        "accounts": "fas fa-users",
        "accounts.User": "fas fa-user",

        # تنظیمات
        "sites": "fas fa-globe",
    },

    "default_icon_parents": "fas fa-chevron-circle-right",

    "default_icon_children": "fas fa-circle",


    # --------------------------------------------------------
    # Top menu
    # --------------------------------------------------------

    "topmenu_links": [

        {
            "name": "فروشگاه",
            "app": "shop",
            "permissions": ["shop.view_product"],
        },

        {
            "name": "سفارش‌ها",
            "app": "orders",
            "permissions": ["orders.view_order"],
        },

        {
            "name": "کاربران",
            "app": "accounts",
            "permissions": ["accounts.view_user"],
        },

        {
            "name": "مشاهده سایت",
            "url": "/",
            "new_window": True,
            "icon": "fas fa-external-link-alt",
        },
    ],


    # --------------------------------------------------------
    # User menu
    # --------------------------------------------------------

    "usermenu_links": [

        {
            "name": "مشاهده سایت",
            "url": "/",
            "new_window": True,
            "icon": "fas fa-globe",
        },
    ],


    # --------------------------------------------------------
    # Change forms
    # --------------------------------------------------------

    # فرم‌های طولانی را مرتب و حرفه‌ای نگه می‌دارد
    "changeform_format": "horizontal_tabs",

    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },


    # --------------------------------------------------------
    # Related objects
    # --------------------------------------------------------

    "related_modal_active": True,


    # --------------------------------------------------------
    # Language
    # --------------------------------------------------------

    "language_chooser": False,


    # --------------------------------------------------------
    # UI
    # --------------------------------------------------------

    # در محیط production بهتر است خاموش باشد
    "show_ui_builder": False,

    "show_theme_chooser": False,

    "use_google_fonts_cdn": False,


    # --------------------------------------------------------
    # Custom CSS / JS
    # --------------------------------------------------------

    "custom_css": "admin/css/jazzmin-custom.css",

    "custom_js": "admin/js/jazzmin-custom.js",
}


# ============================================================
# JAZZMIN UI TWEAKS
# ============================================================

JAZZMIN_UI_TWEAKS = {

    # تم اصلی
    "theme": "flatly",

    # Light / Dark / System
    # auto = مطابق تنظیمات سیستم کاربر
    "default_theme_mode": "auto",

    # Sidebar
    "sidebar_fixed": True,

    # Navbar
    "navbar_fixed": True,

    # Footer
    "footer_fixed": False,

    # Sidebar حالت فشرده
    "sidebar_nav_compact_style": False,

    # Sidebar کوچک در دسکتاپ
    "sidebar_nav_child_indent": True,

    # رنگ Navbar
    "navbar_small_text": False,

    # متن‌ها
    "body_small_text": False,

    # Breadcrumb
    "actions_sticky_top": True,

    # Form controls
    "form_control_classes": "form-control",

    # Button styles
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}

