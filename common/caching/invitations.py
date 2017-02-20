from __future__ import unicode_literals

from django.core.cache import cache


INVITE_TOKEN_TTL = 24 * 60 * 60  # 24 hours


def set_invite_token(email, token):
    """
    Stores a ``token`` (JWT) under the key ``email`` with a 24 hour TTL.

    Args:
        email (unicode, str): The email of the person that was invited.
        token (str): A token (JWT) generated for an invitation

    """
    cache.set(email, token, INVITE_TOKEN_TTL)


def get_invite_token(email):
    """
    Check the cache for the given email.

    Args:
        email (str, unicode): An email address

    Returns:
        str
    """
    return cache.get(email)


def invalidate_invite_token(email):
    """
    Delete the key for a token so it can't be reused.

    Args:
        email (str, unicode): An email address
    """
    cache.delete(email)
