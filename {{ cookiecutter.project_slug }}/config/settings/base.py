"""
Django settings for {{ cookiecutter.project_name }} project.
"""

from pathlib import Path

{%- if cookiecutter.use_bootstrap == "y" %}

from django.contrib.messages import constants as messages{% endif %}
from config import env

# Reading environment variables


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_DIR = BASE_DIR / "config"
APPS_DIR = BASE_DIR / "apps"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "SECRET_KEY",
    default="django-insecure-s_!(-mt*(!omlw-&fn+&%+!i7knohfnh7ke2g9l=e696gh9!by"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])


# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites']

THIRD_PARTY_APPS = [
    "django_extensions",             
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    {%- if cookiecutter.use_bootstrap == "y" %}
    "crispy_forms",
    "crispy_bootstrap5",{% elif cookiecutter.use_bootstrap == "y" %}
    "crispy_forms",
    "crispy_tailwind",{% endif %}
    {%- if cookiecutter.use_bootstrap == "y" or cookiecutter.use_tailwindcss == "y" %}
    'webpack_boilerplate',{% endif %}
    ]

LOCAL_APPS = [
    "apps.pages",
    "apps.users",
    "apps.{{ cookiecutter.project_slug.lower() }}"
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": env.db(
        default="sqlite:///db.sqlite3",
    )
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",# noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",# noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",# noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",# noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "{{ cookiecutter.language }}"

TIME_ZONE = "{{ cookiecutter.timezone }}"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache.
# See https://docs.djangoproject.com/en/4.1/ref/contrib/staticfiles/#manifeststaticfilesstorage # noqa
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"# noqa

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [APPS_DIR / "static"]

{%- if cookiecutter.use_bootstrap == "y" or cookiecutter.use_tailwindcss == "y" %}

# Configuration of python-webpack-boilerplate
WEBPACK_LOADER = {
    'MANIFEST_FILE': APPS_DIR / "static" / "manifest.json",
}{% endif %}

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "media/"


ADMINS = [
    ('{{ cookiecutter.author_name }}', '{{ cookiecutter.email }}'),
]
MANAGERS = ADMINS

# Email configuration
EMAIL_SUBJECT_PREFIX = '[{{ cookiecutter.project_name }}] '
DEFAULT_FROM_EMAIL = '{{ cookiecutter.email }}'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

{%- if cookiecutter.use_bootstrap == "y" or cookiecutter.use_tailwindcss == "y" %}

# Configuration de Django Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = {% if cookiecutter.use_bootstrap == "y" %}"bootstrap5"{% elif cookiecutter.use_tailwindcss == "y" %}"tailwind"{% endif %}
CRISPY_TEMPLATE_PACK = {% if cookiecutter.use_bootstrap == "y" %}"bootstrap5"{% elif cookiecutter.use_tailwindcss == "y" %}"tailwind"{% endif %}{% endif %}

# Configuration de of the authentication
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "pages:home"
LOGOUT_REDIRECT_URL = "pages:home"
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': env('google_client_id'),
            'secret': env('google_secret'),
            'key': env('google_key')
        }
    }
}

SITE_ID = 1

{%- if cookiecutter.use_bootstrap == "y" %}

# Configuration of message tags
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
 }{% endif %}
