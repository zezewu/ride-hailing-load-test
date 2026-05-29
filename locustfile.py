import time, random, json
from locust import User, task, between, events
import websocket

class GPSStreamUser(User):
    wait_time = between(0.5, 1.5)

    def on_start(self):
        try:
            self.ws = websocket.create_connection("ws://localhost:8765", timeout=10)
        except Exception as e:
            self.ws = None
            events.request.fire(request_type="WS", name="connect",
                                response_time=0, response_length=0, exception=e)

    def on_stop(self):
        if self.ws:
            self.ws.close()

    @task
    def stream_gps(self):
        if not self.ws:
            return
        payload = json.dumps({
            "driver_id": f"driver_{random.randint(1,2000):04d}",
            "lat": round(40.7128 + random.uniform(-0.1, 0.1), 6),
            "lng": round(-74.0060 + random.uniform(-0.1, 0.1), 6),
            "timestamp": time.time()
        })
        t0 = time.perf_counter()
        try:
            self.ws.send(payload)
            self.ws.recv()
            ms = (time.perf_counter() - t0) * 1000
            events.request.fire(request_type="WS", name="GPS stream",
                                response_time=ms, response_length=len(payload), exception=None)
        except Exception as e:
            ms = (time.perf_counter() - t0) * 1000
            events.request.fire(request_type="WS", name="GPS stream",
                                response_time=ms, response_length=0, exception=e)
            try:
                self.ws = websocket.create_connection("ws://localhost:8765", timeout=5)
            except:
                self.ws = None