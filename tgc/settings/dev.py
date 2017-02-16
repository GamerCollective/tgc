from __future__ import unicode_literals

import os
import json

from .common import Common


class Dev(Common):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
        }
    }

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }

    with open(PROJECT_ROOT + "/.secrets") as fp:
        secrets = json.load(fp)
    MAILGUN_API_KEY = secrets["MAILGUN_API_KEY"]
    SECRET_KEY = secrets["SECRET_KEY"]
    INVITE_TOKEN_KEY = secrets["INVITE_TOKEN_KEY"]

    SITE_DOMAIN = "localhost:8000"
