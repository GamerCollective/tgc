from ..models import Identity


def get_identity_by_pk(pk):
    """
    Get an ``Identity`` by it's integer pk.

    Args:
        pk (int, long): A pk

    Returns:
        Identity
    """
    return Identity.objects.get(pk=pk)


def get_identities_for_user(tgcuser):
    """
    Get the ``Identity``s for a given user.

    Args:
        tgcuser (tgcuser): A user

    Returns:
        QuerySet[TGCUser]
    """
    return Identity.objects.filter(user=tgcuser)
