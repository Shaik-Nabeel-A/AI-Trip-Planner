from collections import defaultdict
import time

class MetricsTracker:
    def __init__(self):
        self.latencies = defaultdict(list)
        self.counts = defaultdict(int)
        self.errors = defaultdict(int)

    def record_latency(self, name, duration):
        self.latencies[name].append(duration)

    def increment_count(self, name):
        self.counts[name] += 1

    def increment_error(self, name):
        self.errors[name] += 1

    def get_metrics(self):
        return {
            "counts": dict(self.counts),
            "errors": dict(self.errors),
            "avg_latencies": {k: sum(v)/len(v) for k, v in self.latencies.items() if v}
        }

metrics = MetricsTracker()
