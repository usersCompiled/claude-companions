from __future__ import annotations

from anthropic import Anthropic

from app.core.config import settings
from app.domain.companions import CompanionId
from app.domain.prompts import companion_system_prompt
from app.schemas.chat import ChatMsg


def _client() -> Anthropic:
    if not settings.anthropic_api_key:
        raise RuntimeError("Missing ANTHROPIC_API_KEY")
    return Anthropic(api_key=settings.anthropic_api_key)


def ask_claude(companion_id: CompanionId, messages: list[ChatMsg]) -> tuple[str, str]:
    client = _client()
    system = companion_system_prompt(companion_id)

    resp = client.messages.create(
        model=settings.anthropic_model,
        max_tokens=settings.max_tokens,
        system=system,
        messages=[{"role": m.role, "content": m.content} for m in messages],
    )

    parts: list[str] = []
    for block in resp.content:
        if getattr(block, "type", None) == "text":
            parts.append(getattr(block, "text", ""))

    return "\n".join(parts).strip(), settings.anthropic_model
