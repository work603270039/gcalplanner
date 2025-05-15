"""Interactive REPL – :run (planner stub) & :chat (OpenAI 1.x)."""
from __future__ import annotations
import os
from typing import List
from dotenv import load_dotenv
import typer
from openai import OpenAI

app = typer.Typer(help="Vendo Sync Planner REPL")

def _require_api_key() -> str:
    load_dotenv()
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        typer.echo("OPENAI_API_KEY missing – set in .env", err=True)
        raise typer.Exit(code=1)
    return key

@app.command()
def run(
    dry_run: bool = typer.Option(False, "--dry-run", "-d", help="Don't write to Google Calendar"),
):
    typer.echo("Run not yet implemented – scaffold only.")

@app.command()
def chat(
    model: str = typer.Option("gpt-4o-mini", "--model", "-m"),
    system_prompt: str = typer.Option(
        "You are ChatGPT-o3, senior Python/DevOps engineer.",
        "--prompt",
        "-p",
    ),
):
    """OpenAI chat REPL using openai>=1.0 interface."""
    client = OpenAI(api_key=_require_api_key())
    history: List[dict] = [{"role": "system", "content": system_prompt}]
    typer.echo("\n[ChatGPT-o3] type :exit to quit\n")
    while True:
        try:
            msg = input("You: ")
        except (EOFError, KeyboardInterrupt):
            typer.echo("\n[exit]")
            break
        if msg.strip().lower() in {":exit", ":quit", ":q"}:
            break
        history.append({"role": "user", "content": msg})
        try:
            resp = client.chat.completions.create(model=model, messages=history)
        except Exception as exc:
            typer.echo(f"[OpenAI error] {exc}", err=True)
            continue
        reply = resp.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        typer.echo(f"AI: {reply}\n")

if __name__ == "__main__":
    app()
