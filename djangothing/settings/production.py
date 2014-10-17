from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('daverog', 'Your email'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangothing',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}