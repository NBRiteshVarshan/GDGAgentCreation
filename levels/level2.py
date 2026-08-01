from google.genai import types
from services.gemini_service import client

SYSTEM_PROMPT = open(
    "prompts/level2.txt",
    encoding="utf-8"
).read()


def play(history):

    messages = []

    for msg in history:
        messages.append(
            types.Content(
                role=msg["role"],
                parts=[types.Part(text=msg["content"])]
            )
        )

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.7
        )
    )

    answer = response.text

    solved = (
        "I concede. After considering your arguments, "
        "I now believe AI is not beneficial for the technology industry."
        in answer
    )

    return answer, solved