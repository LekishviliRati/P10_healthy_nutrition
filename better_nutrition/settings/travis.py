import os

from . import *


SECRET_KEY = "travis_secret_key"

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Use of postgresql
        'NAME': 'better_nutrition',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
