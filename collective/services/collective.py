from ..models import Collective


def get_collective_by_pk(pk):
    """
    Get a ``Collective`` by it's integer ``pk``

    Args:
        pk (long, int): The ``pk`` of the ``Collective``

    Returns:
        Collective
    """
    return Collective.objects.get(pk=pk)


def add_tgcuser_to_collective(member, collective):
    """
    Adds a given ``tgcuser`` to ``collective``

    Args:
        member (tgcprofile.models.TGCUser): A user
        collective (Collective):

    Returns:
        bool
    """
    from .membership import create_membership

    membership = create_membership(member, collective)
    collective.membership_set.add(membership)
