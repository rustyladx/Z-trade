from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.bot import generate_trade_signal

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/signal")
def get_trade_signal():
    signal = generate_trade_signal()
    return signal
