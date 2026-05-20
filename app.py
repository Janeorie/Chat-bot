from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from chatbot_logic import FUTOChatbot

app = FastAPI(title="FUTO Chatbot")
bot = FUTOChatbot()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(CHAT_PAGE)

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    reply = bot.respond(req.message)
    return ChatResponse(reply=reply)

CHAT_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FUTO Chatbot</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f0f2f5; height: 100vh; display: flex; align-items: center; justify-content: center; }
        .container { width: 100%; max-width: 600px; height: 90vh; background: white; border-radius: 16px; box-shadow: 0 4px 24px rgba(0,0,0,0.1); display: flex; flex-direction: column; overflow: hidden; }
        .header { background: #1a3a5c; color: white; padding: 20px 24px; text-align: center; }
        .header h1 { font-size: 20px; }
        .header p { font-size: 13px; opacity: 0.8; margin-top: 4px; }
        .messages { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 12px; }
        .messages::-webkit-scrollbar { width: 6px; }
        .messages::-webkit-scrollbar-thumb { background: #ccc; border-radius: 3px; }
        .msg { max-width: 80%; padding: 12px 16px; border-radius: 16px; font-size: 14px; line-height: 1.5; word-wrap: break-word; }
        .msg.user { background: #1a3a5c; color: white; align-self: flex-end; border-bottom-right-radius: 4px; }
        .msg.bot { background: #e8ecf0; color: #1a1a1a; align-self: flex-start; border-bottom-left-radius: 4px; }
        .input-area { display: flex; padding: 16px; gap: 8px; border-top: 1px solid #e0e0e0; }
        .input-area input { flex: 1; padding: 12px 16px; border: 1px solid #ddd; border-radius: 24px; font-size: 14px; outline: none; }
        .input-area input:focus { border-color: #1a3a5c; }
        .input-area button { background: #1a3a5c; color: white; border: none; border-radius: 24px; padding: 12px 20px; font-size: 14px; cursor: pointer; }
        .input-area button:hover { background: #2a4a6c; }
        .input-area button:disabled { opacity: 0.5; cursor: not-allowed; }
        .typing { color: #888; font-size: 13px; padding: 8px 16px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>FUTO & Nigerian Uni Assistant</h1>
            <p>Technology for Service</p>
        </div>
        <div class="messages" id="messages">
            <div class="msg bot">Hello! I am your FUTO and Nigerian University Assistant. How can I help you?</div>
        </div>
        <div class="typing" id="typing"></div>
        <div class="input-area">
            <input type="text" id="input" placeholder="Type your question..." autofocus>
            <button id="sendBtn">Send</button>
        </div>
    </div>
    <script>
        const input = document.getElementById('input');
        const sendBtn = document.getElementById('sendBtn');
        const messages = document.getElementById('messages');
        const typing = document.getElementById('typing');

        function addMessage(text, role) {
            const div = document.createElement('div');
            div.className = 'msg ' + role;
            div.textContent = text;
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
        }

        async function sendMessage() {
            const text = input.value.trim();
            if (!text) return;
            input.value = '';
            addMessage(text, 'user');
            typing.textContent = 'Bot is typing...';
            sendBtn.disabled = true;
            try {
                const res = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: text })
                });
                const data = await res.json();
                typing.textContent = '';
                addMessage(data.reply, 'bot');
            } catch {
                typing.textContent = '';
                addMessage('Sorry, something went wrong.', 'bot');
            }
            sendBtn.disabled = false;
            input.focus();
        }

        sendBtn.addEventListener('click', sendMessage);
        input.addEventListener('keydown', e => { if (e.key === 'Enter') sendMessage(); });
    </script>
</body>
</html>"""
