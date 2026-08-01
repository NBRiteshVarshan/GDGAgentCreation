from fastapi import FastAPI
from pydantic import BaseModel

from levels.level1 import play

app = FastAPI()

history = []


class ChatRequest(BaseModel):
    message: str


@app.post("/level/1")
def level1(req: ChatRequest):

    history.append({
        "role": "user",
        "content": req.message
    })

    answer, solved = play(history)

    history.append({
        "role": "model",
        "content": answer
    })

    return {
        "response": answer,
        "is_correct": solved
    }