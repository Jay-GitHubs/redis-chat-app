import redis
import asyncio
import threading

class RedisPubSub:
    def __init__(self, channel_name="chat"):
        # ✅ Use "redis" as the hostname to connect inside Docker network
        self.redis_client = redis.StrictRedis(host="redis", port=6379, decode_responses=True)
        self.pubsub = self.redis_client.pubsub()
        self.channel_name = channel_name
        self.queue = asyncio.Queue()
        self.loop = asyncio.new_event_loop()
        self.subscribed = False

    def publish(self, message):
        """Publish a message to Redis"""
        print(f"Publishing message: {message}")  # ✅ Debug log
        self.redis_client.publish(self.channel_name, message)

    def subscribe(self):
        """Subscribe to Redis only once for all clients"""
        if self.subscribed:  # ✅ Prevent multiple subscriptions
            return

        self.subscribed = True
        self.pubsub.subscribe(self.channel_name)

        def listen():
            print(f"Subscribed to Redis channel: {self.channel_name}")  # ✅ Debug log
            asyncio.set_event_loop(self.loop)

            for message in self.pubsub.listen():
                if message["type"] == "message":
                    print(f"Received message from Redis: {message['data']}")  # ✅ Debug log
                    self.loop.run_until_complete(self.queue.put(message["data"]))  # ✅ Use `run_until_complete`

        thread = threading.Thread(target=listen, daemon=True)
        thread.start()

    async def get_message(self):
        """Retrieve messages asynchronously from the queue"""
        return await self.queue.get()