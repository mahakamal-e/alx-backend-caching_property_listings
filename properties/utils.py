from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Retrieve all Property objects.
    Cache them in Redis for 1 hour (3600 sec).
    """
    properties = cache.get("all_properties")
    if properties is None:
        properties = list(Property.objects.values("id", "title", "description", "price"))
        cache.set("all_properties", properties, 3600)
    return properties
