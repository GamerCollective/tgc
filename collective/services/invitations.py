from __future__ import unicode_literals

from collections import namedtuple
from datetime import timedelta

from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import timezone
import jwt

from common import email_domain, set_invite_token, get_invite_token


Payload = namedtuple("Payload", ["email", "exp", "collective_pk", "inviter_pk"])


def generate_invite_token(email, collective_pk, inviter_pk):
    """
    Generate a one time use JWT to use as an invite token. Caches the token under the given email for validation later.

    Args:
        email (unicode, str): The email address of the invited person
        collective_pk (int): The collective they are being invited to

    Returns:
        str
    """
    expiration_date = timezone.now() + timedelta(hours=24)
    payload = {'email': email, "exp": expiration_date, "collective_pk": collective_pk, "inviter_pk": inviter_pk}
    token = jwt.encode(payload, settings.INVITE_TOKEN_KEY, algorithm='HS256')
    set_invite_token(email, token)
    return token


def get_invite_link(email, collective_pk, inviter_pk):
    """
    Get the full link for an invite

    Args:
        email (unicode, str): The email address of the invited person
        collective_pk (int): The collective they are being invited to
        inviter_pk (int): The pk of the user initiating the invite

    Returns:
        str
    """
    token = generate_invite_token(email, collective_pk, inviter_pk)
    return "{}/{}?token={}".format(settings.SITE_DOMAIN, reverse("accept_invite_view"), token)


def send_invitation_email(email_address, link):
    """
    Send an email to the ``email_address`` of the person being invited. The email will contain a link that is valid for
    24 hours to join a collective.

    Args:
        email_address:
        link:

    Returns:
        requests.Response
    """
    data = {
        "to": email_address,
        "from": "TGC invite@tgc.com",
        "subject": "You've been invited",
        "text": "Here is your link: {}".format(link),
        "html": "Here is your link: {}".format(link)
    }
    return email_domain.send_simple_message(data)


def get_payload_from_token(token):
    """
    Decodes the given ``token`` and returns the payload as a named tuple

    Args:
        token (unicode, str): An invite token (JWT)

    Returns:
        Payload
    """
    return Payload(**jwt.decode(token, settings.INVITE_TOKEN_KEY, algorithms="HS256"))


def validate_token(email, token):
    """
    Attempts to retreive a ``token`` from the cache under the key ``email``. If the token in the cache matches the token
    passed in then the token is valid and the invite can continue

    Args:
        email (unicode, str): The invited user's email
        token (unicode, str): An invite token (JWT)

    Returns:
        bool
    """
    cached_token = get_invite_token(email)
    if cached_token:
        return cached_token == token
    return False
