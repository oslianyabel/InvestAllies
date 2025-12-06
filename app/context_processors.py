from typing import Dict

from .models import SocialLink


def social_links(request) -> Dict[str, object]:
    """Provide active social links to all templates.

    Returns a dict with key `social_links` containing a queryset ordered by `order`.
    """
    links = SocialLink.objects.filter(active=True).order_by("order")
    return {"social_links": links}
