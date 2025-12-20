# Claude Companions Backend

A Python FastAPI backend service that routes chat requests to Anthropic Claude using companion specific system prompts.

The backend focuses on clean separation of concerns, predictable APIs, and an architecture that can be extended into a production service.

---

## Features

- FastAPI based HTTP API
- Companion registry with stable IDs
- Companion specific system prompts
- Claude Messages API integration
- Clear request and response schemas
- Simple in memory conversation storage for prototyping
- Docker support
- Ready for frontend integration

---

## Architecture Overview

```
app/
  api/          HTTP routes and versioning
  core/         configuration and middleware
  domain/       companion definitions and prompts
  schemas/      request and response models
  services/     external service integrations
```

Design goals:

- Backend mirrors frontend companion model
- Prompts live server side and are version controlled
- Frontend never sees raw system prompts
- Easy to swap storage or model providers later

---

## Requirements

- Python 3.11 or newer
- Anthropic API key
- Git
- Optional Docker

---

## Local Development

### Clone and setup

```
git clone <your-repo-url>
cd claude-companions-backend
```

### Create virtual environment

Windows:

```
python -m venv .venv
.venv\Scripts\activate
```

macOS or Linux:

```
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Environment variables

Create a .env file from the example:

```
copy .env.example .env
```

Set at minimum:

```
ANTHROPIC_API_KEY=your_key_here
```

Optional:

```
ANTHROPIC_MODEL=claude-sonnet-4-20250514
MAX_TOKENS=650
ORIGINS=*
```

Notes:
- Do not commit your .env file
- For production, restrict ORIGINS to your frontend domain

---

## Running the Server

```
uvicorn app.main:app --reload --port 8080
```

The API will be available at:

```
http://localhost:8080
```

Interactive docs:

```
http://localhost:8080/docs
```

---

## API Endpoints

### Health Check

```
GET /health
GET /v1/health
```

Returns a simple status response.

---

### List Companions

```
GET /v1/companions
```

Returns the list of supported companions including metadata used by the frontend.

---

### Chat With Companion

```
POST /v1/chat/{companion_id}
```

Request body:

```
{
  "messages": [
    { "role": "user", "content": "Hello" }
  ]
}
```

Response:

```
{
  "companion_id": "cinder",
  "model": "claude-sonnet-4-20250514",
  "text": "response text here"
}
```

---

## Example Requests

List companions:

```bat
curl -s http://localhost:8080/v1/companions
```

Chat:

```bat
curl -s http://localhost:8080/v1/chat/cinder ^
  -H "Content-Type: application/json" ^
  -d "{\"messages\":[{\"role\":\"user\",\"content\":\"Hello\"}]}"
```

---

## Companion IDs

- cinder
- velvet
- vector
- morrow
- quill

Each companion has:

- A fixed identifier
- A personality specific system prompt
- A distinct response style

---

## Docker

### Build image

```
docker build -t claude-companions-backend .
```

### Run container

```
docker run --rm -p 8080:8080 --env-file .env claude-companions-backend
```

---

## Testing

Install development dependencies:

```
pip install -r requirements-dev.txt
```

Run tests:

```
pytest
```

---

## License

MIT License
