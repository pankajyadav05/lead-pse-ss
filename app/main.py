from prometheus_client import start_http_server, Summary, Counter, Gauge
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds',
                       'Time spent processing request')
UPDATE_COUNT = Counter('update_count', 'Number of updates')
RANDOM_SUM = Gauge('random_sum', 'Sum of generated random numbers')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)
    random_num = random.random()
    RANDOM_SUM.inc(random_num)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
        UPDATE_COUNT.inc(1)
