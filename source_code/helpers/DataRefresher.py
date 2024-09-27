import threading

from source_code.helpers.RateLimiter import RateLimiter


class DataRefresher:
    def __init__(self, ds, time_period):
        self.rate_limiter = RateLimiter(delay=time_period)
        self.ds = ds
        self._last_result = self.ds.get_data()
        worker_thread = threading.Thread(target=self._worker)
        worker_thread.daemon = True
        worker_thread.start()

    def _worker(self):
        while True:
            try:
                self.rate_limiter.call_wait()
                self._last_result = self.ds.get_data()
            except:
                self._last_result = None

    def get_last_data(self):
        return self._last_result
