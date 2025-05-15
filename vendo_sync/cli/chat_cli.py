"""Interactive REPL (:run, :auto, :logs, …) – skeleton only."""

from __future__ import annotations

import typer

app = typer.Typer(help="Vendo Sync Planner REPL")


@app.command()
def run(
    dry_run: bool = typer.Option(False, "--dry-run", "-d", help="Don't write to Google Calendar"),
):
    """Plan tasks from backlog into calendar."""
    typer.echo("Run not yet implemented – scaffold only.")


if __name__ == "__main__":
    app()
