from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property


@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    """
    Return all properties as JSON, cached for 15 min in Redis.
    """
    properties = list(
        Property.objects.values("id", "title", "description", "price")
    )
    return JsonResponse({"data": properties})
