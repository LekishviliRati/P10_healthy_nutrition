from . import *


# DATABASES = {
#     "default": {
#         'ENGINE': 'django.db.backends.postgresql',  # Use of postgresql
#         'NAME': '',
#         'USER': 'postgres',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Use of postgresql
        'NAME': 'better_nutrition',
        'USER': 'ratilekishvili',
        'PASSWORD': 'diTna7-kyztig*',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}