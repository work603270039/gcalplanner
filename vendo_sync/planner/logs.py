"""Rich-based logger setup + helpers for writing run artefacts."""

from __future__ import annotations

from pathlib import Path

from rich.console import Console

console = Console()


def init_run_dir(base: Path) -> Path:
    """Create `runs/<TIMESTAMP>` directory and return its Path."""
    # TODO: implement – stub
    return base
