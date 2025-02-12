from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import json
from pubsub import RedisPubSub

app = FastAPI()
redis_pubsub = RedisPubSub()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to Redis Pub/Sub Chat API!"}

@app.post("/send/")
async def send_message(message: str):
    """API to send messages"""
    redis_pubsub.publish(message)
    return {"status": "Message sent"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    # Ensure Redis is subscribed only once
    redis_pubsub.subscribe()

    async def receive_messages():
        """Continuously send messages from Redis to all WebSocket clients"""
        while True:
            message = await redis_pubsub.get_message()
            print(f"Sending message to WebSocket: {message}")  # ✅ Debug log
            await websocket.send_text(message)

    asyncio.create_task(receive_messages())  # ✅ Keep running in background

    while True:
        try:
            data = await websocket.receive_text()
            print(f"Received message from WebSocket: {data}")  # ✅ Debug log
            redis_pubsub.publish(data)
        except:
            break