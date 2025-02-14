# Redis Pub/Sub Chat Application

🚀 **Real-time chat application using FastAPI, Redis Pub/Sub, WebSockets, and Docker**

## 📌 Features

- **Real-time messaging** with Redis Pub/Sub.
- **FastAPI-based backend** for handling WebSockets.
- **Simple frontend UI** using HTML, CSS, and JavaScript.
- **Dockerized environment** for easy deployment.
- **Works in multiple browser tabs** seamlessly.

---

## 📂 Project Structure

```
redis-chat-app/
├── backend/               # Backend service (Python, FastAPI)
│   ├── main.py            # WebSocket & API logic
│   ├── pubsub.py          # Redis Pub/Sub logic
│   ├── requirements.txt   # Python dependencies
│   ├── Dockerfile         # Docker configuration for backend
│   ├── .gitignore         # Ignore virtual environment & Python cache files
├── frontend/              # Frontend UI (HTML, CSS, JS)
│   ├── index.html         # Chat interface
│   ├── script.js          # Handles WebSocket connections
│   ├── style.css          # UI Styling
│   ├── Dockerfile         # Docker configuration for frontend
├── .gitignore             # Ignore unnecessary files globally
├── docker-compose.yml     # Docker Compose for multi-container setup
├── README.md              # Project documentation
```

---

## 🛠️ Getting Started (Local Development)

### 1️⃣ Prerequisites

Before contributing, ensure you have the following installed:

- **Python 3.10+**
- **Docker & Docker Compose**
- **Git**

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/Jay-GitHubs/redis-chat-app.git
cd redis-chat-app
```

### 3️⃣ Run the Application Using Docker

```sh
docker compose up --build
```

This will:

- Start a **Redis container**.
- Start the **FastAPI backend** on `http://localhost:8000`.
- Start the **Frontend UI** on `http://localhost:8080`.

### 4️⃣ Open the Chat UI

- Open [**http://localhost:8080**](http://localhost:8080) in **two browser tabs**.
- Start chatting! 📨💬

---

## 👨‍💻 Local Development (Without Docker)

If you prefer to run the app without Docker:

### 1️⃣ Start Redis

If Redis **is not installed**, run it using Docker:

```sh
docker run -d --name redis-server -p 6379:6379 redis
```

Or install **Redis locally**:

- macOS: `brew install redis`
- Ubuntu: `sudo apt install redis`
- Windows: [Download Redis](https://github.com/microsoftarchive/redis/releases)

### 2️⃣ Create a Virtual Environment

```sh
cd backend
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3️⃣ Run the Backend

```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 4️⃣ Open `frontend/index.html` in a Browser

Use **VS Code Live Server** or a simple Python server:

```sh
cd frontend
python3 -m http.server 8080
```

---

## 🤝 Contributing

Want to improve this project? Follow these steps:

### 1️⃣ Fork and Clone the Repository

```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/redis-chat-app.git
cd redis-chat-app
```

### 2️⃣ Create a New Branch

```sh
git checkout -b feature-your-feature-name
```

### 3️⃣ Make Your Changes

- Add new features or fix bugs.

### 4️⃣ Commit and Push Your Changes

```sh
git add .
git commit -m "Added new feature: ..."
git push origin feature-your-feature-name
```

### 5️⃣ Open a Pull Request

- Go to GitHub and **create a pull request**.
- Wait for review and merge.

---

## 🐛 Troubleshooting

### WebSocket Connection Issues

**Error:** `WebSocket is closed, cannot send message ❌`\
**Fix:** Ensure the backend is running properly:

```sh
docker restart chat-backend
```

### Redis Connection Errors

**Error:** `Error 111 connecting to localhost:6379`\
**Fix:** Use the correct Redis hostname in `backend/pubsub.py`:

```python
self.redis_client = redis.StrictRedis(host="redis", port=6379, decode_responses=True)
```

Then restart the app:

```sh
docker compose down
docker compose up --build
```

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 🎯 Next Steps

Want to extend this project? Consider adding:

- **User Authentication** (JWT or OAuth)
- **Chat History Storage** (MongoDB, PostgreSQL)
- **Private Chat Rooms**
- **Scalability (Redis Cluster)**

🚀 **Happy Coding!** 🎉

