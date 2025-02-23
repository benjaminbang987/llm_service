from prometheus_client import Counter, Histogram, start_http_server
import time

# Define Prometheus metrics
REQUEST_COUNT = Counter("llm_api_requests_total", "Total number of API requests")
REQUEST_LATENCY = Histogram("llm_api_request_latency_seconds", "Request latency in seconds")

def setup_metrics():
    """Start Prometheus metrics server on a separate port."""
    start_http_server(8001)  # Expose metrics at :8001
    # Note: In production, use a sidecar or external Prometheus instance

def track_request(func):
    """Decorator to monitor request count and latency."""
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        REQUEST_COUNT.inc()
        result = await func(*args, **kwargs)
        REQUEST_LATENCY.observe(time.time() - start_time)
        return result
    return wrapper