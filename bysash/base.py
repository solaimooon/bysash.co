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
    "unfold",
#    'jazzmin',
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





