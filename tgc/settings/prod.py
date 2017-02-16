from __future__ import unicode_literals

import os
import dj_database_url
from .common import Common


class Prod(Common):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
        }
    }
    # Update database configuration with $DATABASE_URL.
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }

    MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    INVITE_TOKEN_KEY = os.environ.get("INVITE_TOKEN_KEY")

    SITE_DOMAIN = "tgc.herokuapp.com"
