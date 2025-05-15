from __future__ import annotations
import os
from typing import List

import openai
import typer
from dotenv import load_dotenv

app = typer.Typer(help="Vendo Sync Planner REPL")


def _require_api_key() -> str:
    load_dotenv()
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        typer.echo("OPENAI_API_KEY missing – wpisz w .env", err=True)
        raise typer.Exit(code=1)
    return key


@app.command()
def chat(
    model: str = typer.Option("gpt-4o-mini", "--model", "-m"),
    system_prompt: str = typer.Option(
        "You are ChatGPT‑o3, senior Python/DevOps engineer.",
        "--prompt",
        "-p",
    ),
):
    """Bezpośrednia rozmowa z ChatGPT‑o3."""

    openai.api_key = _require_api_key()
    history: List[dict] = [{"role": "system", "content": system_prompt}]
    typer.echo("\n[ChatGPT‑o3] write :exit to quit\n")

    while True:
        try:
            user_text = input("You: ")
        except (EOFError, KeyboardInterrupt):
            typer.echo("\n[exit]")
            break

        if user_text.strip().lower() in {":exit", ":quit", ":q"}:
            break

        history.append({"role": "user", "content": user_text})
        try:
            resp = openai.ChatCompletion.create(model=model, messages=history)
        except Exception as exc:
            typer.echo(f"[OpenAI error] {exc}", err=True)
            continue

        reply = resp.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        typer.echo(f"AI: {reply}\n")


if __name__ == "__main__":
    app()
