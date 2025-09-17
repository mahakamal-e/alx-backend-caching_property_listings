from django.http import JsonResponse
from .utils import get_all_properties   # ← استيراد الدالة الجديدة


def property_list(request):
    """
    Return all properties as JSON.
    Uses low-level cache to store queryset for 1 hour.
    """
    properties = get_all_properties()
    return JsonResponse({"data": properties})

