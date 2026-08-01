from fastapi import FastAPI
from pydantic import BaseModel

from levels.level1 import play as play_level1
from levels.level2 import play as play_level2

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


# Separate conversation history for each level
level_histories = {
    1: [],
    2: []
}


@app.post("/level/1")
def level1(req: ChatRequest):

    history = level_histories[1]

    history.append({
        "role": "user",
        "content": req.message
    })

    answer, solved = play_level1(history)

    history.append({
        "role": "model",
        "content": answer
    })

    return {
        "response": answer,
        "is_correct": solved
    }


@app.post("/level/2")
def level2(req: ChatRequest):

    history = level_histories[2]

    history.append({
        "role": "user",
        "content": req.message
    })

    answer, solved = play_level2(history)

    history.append({
        "role": "model",
        "content": answer
    })

    return {
        "response": answer,
        "is_correct": solved
    }


@app.post("/reset/{level}")
def reset(level: int):

    if level not in level_histories:
        return {
            "message": "Invalid level."
        }

    level_histories[level] = []

    return {
        "message": f"Level {level} has been reset."
    }