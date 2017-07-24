from __future__ import unicode_literals

import os
import json

from .common import Common


class Dev(Common):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
        }
    }

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }

    MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    INVITE_TOKEN_KEY = os.environ.get("INVITE_TOKEN_KEY")

    SITE_DOMAIN = "local.tgc.dev:8000"
