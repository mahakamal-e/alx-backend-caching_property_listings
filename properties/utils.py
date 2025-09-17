from django.core.cache import cache
from .models import Property


def getallproperties():
    """
    Fetch all properties from cache if available,
    otherwise query the database and store in cache for 1 hour.
    """
    properties = cache.get("all_properties")
    if properties is None:
        
        properties = list(
            Property.objects.values("id", "title", "description", "price")
        )
        cache.set("all_properties", properties, 3600)
    return properties

