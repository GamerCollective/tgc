from ..models import Membership


def get_memberships_for_tgcuser(tgcuser):
    """
    Get all the memberships for a given ``tgcuser`` instance.

    Args:
        tgcuser (tgcprofile.models.TGCUser): A tgcuser

    Returns:
        queryset
    """
    return Membership.objects.filter(member=tgcuser)


def create_membership(tgcuser, collective):
    """
    Create a ``Membership`` record for the given ``tgcuser`` and ``collective``

    Args:
        tgcuser (tgcprofile.models.TGCUser): A tgcuser
        collective (collective.models.Collective): A collective

    Returns:
        Membership
    """
    return Membership.objects.create(member=tgcuser, collective=collective)
