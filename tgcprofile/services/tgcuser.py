from __future__ import unicode_literals

from ..models import TGCUser


def get_tgcuser_by_pk(pk):
    """
    Gets a ``TGCUser`` by it's integer ``pk``

    Args:
        pk (int, long): The ``pk`` for the user

    Returns:
        TGCUser
    """
    return TGCUser.objects.get(pk=pk)


def get_tgcuser_by_email(email):
    """
    Get a ``TGCUser`` by it's ``email``
    Args:
        email (str, unicode): An email address

    Returns:
        TGCUser
    """
    return TGCUser.objects.get(email__iexact=email.lower())


def deactivate_tgcuser(tgcuser):
    """
    Sets the ``is_active`` flag to ``False`` for the given ``TGCUser``

    Args:
        tgcuser (TGCUser): The ``TGCUser`` to deactivate

    Returns:
        TGCUser
    """
    tgcuser.is_active = False
    tgcuser.save(update_fields=["is_active"])
