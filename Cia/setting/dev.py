from Cia.settings import *
from decouple import config


# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'captcha',
    'allauth',
    'allauth.account',
    'django_summernote',
    'taggit',
    'sweetify',
    'website',
    'blog',
    'compressor',
    'rcssmin',
    'rjsmin',
    'robots',
    "debug_toolbar",
    
    
]

if DEBUG:
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DEV_ENGINE',default='django.db.backends.sqlite3'),
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


EMAIL_BACKEND = config('EMAIL_BACKEND_DEV', default="django.core.mail.backends.console.EmailBackend")

X_FRAME_OPSTIONS = 'SAMEORIGIN'

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

if DEBUG:
    INTERNAL_IPS = [
        # ...
        "127.0.0.1",
        # ...
    ]