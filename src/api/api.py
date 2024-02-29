# -*- coding: utf-8 -*-
"""
  @Description
  @Author Chris
  @Date 2024/2/27
"""
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.entity import Session, HumanQuestion
from src.bot.bot import ChatBot

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Load environment variables
load_dotenv()
# Create conversation bot
bot = ChatBot()


@app.get("/session/{session_id}")
async def find_session(session_id: str):
    messages = [{'role': message.type, 'content': message.content} for message in bot.chat_history.messages]
    return Session(session_id=session_id, messages=messages)


@app.post("/chat")
async def chat(human_question: HumanQuestion):
    return bot.chat(human_question.content)


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
