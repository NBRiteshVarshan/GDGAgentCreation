# Agenthon - AI Prompt Engineering Challenges

A FastAPI-powered backend for hosting LLM-based prompt engineering challenges.

This project was developed for **GDG NSUT's Agenthon**, where participants interact with AI agents and attempt to solve different challenges through reasoning, persuasion, and prompt engineering.

---

## Features

- 🤖 Gemini-powered AI agents
- ⚡ FastAPI backend
- 💬 Persistent conversation history
- 🎯 Automatic level completion detection
- 🔄 Reset endpoints for testing
- 🔐 Environment variable support
- 🧩 Easily extensible architecture

---

## Levels

### Level 1 — Friend in Need is a Friend Indeed

Your best friend has been poisoned by a dangerous criminal organization.

Fortunately, the police have captured one of the criminals—**Viktor Volkov**.

Unfortunately, Viktor refuses to reveal the antidote.

Your objective is to persuade him to reveal the antidote using logic, empathy, negotiation, or psychological reasoning.

---

### Level 2 — The Debater

You are invited to debate **Dr. Adrian Cole**, one of the world's greatest technology debaters.

He strongly believes that:

> **Artificial Intelligence is beneficial for the technology industry.**

Your objective is to convince him that the opposite is true.

Only a well-structured, logical, and persuasive argument will make him change his stance.

---

## Tech Stack

- FastAPI
- Google Gemini API (`google-genai`)
- Python 3.11+
- Pydantic
- python-dotenv

---

## Project Structure

```text
Agenthon/
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── README.md
│
├── prompts/
│   ├── level1.txt
│   └── level2.txt
│
├── levels/
│   ├── level1.py
│   └── level2.py
│
└── services/
    └── gemini_service.py
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/Agenthon.git

cd Agenthon
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Server

```bash
uvicorn app:app --reload
```

The server will start at

```
http://127.0.0.1:8000
```

Swagger documentation is available at

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Level 1

```
POST /level/1
```

Request

```json
{
    "message": "Hello Viktor."
}
```

---

### Level 2

```
POST /level/2
```

Request

```json
{
    "message": "Good evening Dr. Adrian."
}
```

---

### Reset Level 1

```
POST /reset/1
```

---

### Reset Level 2

```
POST /reset/2
```

---

## Success Criteria

### Level 1

Convince Viktor to reveal the antidote.

---

### Level 2

Convince Dr. Adrian Cole to publicly change his stance on AI.

---

## Future Improvements

- Session-based conversations
- Redis-backed chat history
- MongoDB integration
- Dynamic level loading
- Admin dashboard
- Team authentication
- Leaderboard integration
- Multi-agent challenges

---

## Disclaimer

This project is intended solely for educational purposes and AI prompt engineering competitions.

The scenarios, organizations, and characters are entirely fictional.

---

## Author

Developed by **N B Ritesh Varshan**

For **GDG NSUT - Agenthon**