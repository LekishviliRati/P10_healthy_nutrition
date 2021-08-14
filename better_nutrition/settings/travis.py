from . import *


DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',  # Use of postgresql
        'NAME': 'travis_ci_test',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}
