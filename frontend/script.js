const chatBox = document.getElementById("chat-box");
const messageInput = document.getElementById("message-input");

let ws;
let reconnectAttempts = 0;
const maxReconnectAttempts = 5;  // Prevent infinite reconnect loops

function connectWebSocket() {
    ws = new WebSocket("ws://localhost:8000/ws");

    ws.onopen = function () {
        console.log("WebSocket connected ✅");
        reconnectAttempts = 0; // Reset attempts after successful connection
    };

    ws.onerror = function (event) {
        console.error("WebSocket error ❌:", event);
    };

    ws.onclose = function () {
        console.warn("WebSocket closed ⚠️ Reconnecting...");

        if (reconnectAttempts < maxReconnectAttempts) {
            reconnectAttempts++;
            setTimeout(connectWebSocket, 3000);  // Retry connection in 3 seconds
        } else {
            console.error("WebSocket reconnect failed after multiple attempts ❌");
        }
    };

    ws.onmessage = function (event) {
        console.log("Message received from WebSocket 🔥:", event.data);

        const message = document.createElement("p");
        message.textContent = event.data;
        chatBox.appendChild(message);
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to latest message
    };
}

// Start WebSocket connection
connectWebSocket();

function sendMessage() {
    const message = messageInput.value.trim();
    if (message) {
        if (ws.readyState === WebSocket.OPEN) {  // ✅ Ensure WebSocket is open before sending
            console.log("Sending message 📨:", message);
            ws.send(message);
            messageInput.value = "";
        } else {
            console.warn("WebSocket is closed, cannot send message ❌");
        }
    }
}

// Send message on Enter key
messageInput.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});