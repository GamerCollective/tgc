from ..models import Tag


def get_active_tags():
    """
    Get all active ``Tag``s

    Returns:
        QuerySet
    """
    return Tag.objects.filter(is_active=True)


def get_tag_by_pk(pk):
    """
    Get a ``Tag`` by it's pk.

    Args:
        pk(long, int):

    Returns:
        Tag
    """
    return Tag.objects.get(pk=pk)


def get_tag_by_name(name):
    """
    Get a tag by it's name

    Args:
        name (str, unicode): The tag name

    Returns:
        Tag
    """
    return Tag.objects.get(name=name)
