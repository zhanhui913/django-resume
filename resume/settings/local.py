from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS += ("debug_toolbar",)

SECRET_KEY = '#kp*t8+o@q=jr^7kcmxc2@-x8-y78p64br_xh73lzqh0qkp48@'