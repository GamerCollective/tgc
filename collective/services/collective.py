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


def get_active_collectives():
    """
    Get all active ``Collective``s

    Returns:
        QuerySet[Collective]
    """
    return Collective.objects.filter(is_active=True)


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


def get_collectives_by_tag_names(tags):
    """
    Given a list of tag name's return a queryset of ``Collective``s that match

    Args:
        tags (list[str]):

    Returns:
        QuerySet
    """
    return Collective.objects.filter(tags__name__in=tags).distinct()


def get_collectives_by_tag_pks(tags):
    """
    Given a list of tag pk's return a queryset of ``Collective``s that match

    Args:
        tags (list<int>):

    Returns:
        QuerySet
    """
    return Collective.objects.filter(tags__in=tags).distinct()
