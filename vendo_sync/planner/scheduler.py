"""Main scheduling algorithm – v1.0: no task splitting."""

from __future__ import annotations

from datetime import datetime, timedelta, time
from pathlib import Path
from typing import List

from .candidate_fetcher import Candidate
from .calendar_utils import find_first_fit, get_busy_intervals


def schedule(
    service,
    source_cal: str,
    target_cal: str,
    horizon_days: int,
    work_start: time,
    work_end: time,
    min_gap: timedelta,
    run_dir: Path,
) -> None:
    """High-level orchestration – produces before/after/diff JSON files."""
    # TODO: implement – stub
    pass
