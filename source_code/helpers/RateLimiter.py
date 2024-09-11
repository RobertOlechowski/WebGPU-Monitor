import time
from datetime import datetime


class RateLimiter:
    def __init__(self, delay):
        self._delay = delay
        self.last_call = datetime.fromisoformat("1971-01-01")

    def call_wait(self):
        _delta = (datetime.now() - self.last_call).total_seconds()
        _wait_time = self._delay - _delta
        if _wait_time <= 0:
            self.last_call = datetime.now()
            return
        time.sleep(_wait_time)
        self.last_call = datetime.now()
