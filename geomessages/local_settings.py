import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {

        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'messages',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
    }
}

DEBUG = True