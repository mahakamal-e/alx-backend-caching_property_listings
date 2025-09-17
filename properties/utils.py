from django.core.cache import cache
from .models import Property
import logging

logger = logging.getLogger(__name__)


def get_all_properties():
    """
    Fetch all properties from cache if available,
    otherwise query the database and store in cache for 1 hour.
    """
    properties = cache.get("all_properties")
    if properties is None:
        properties = list(Property.objects.all())
        cache.set("all_properties", properties, 3600)
    return properties


def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and hit ratio.
    """
    client = cache.client.get_client(write=True)
    info = client.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": round(hit_ratio, 2),
    }

    logger.info(f"Redis cache metrics: {metrics}")
    return metrics
