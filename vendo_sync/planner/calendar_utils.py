"""Utilities for working with Google Calendar free/busy slots."""

from __future__ import annotations

from datetime import datetime, timedelta, time
from typing import List, Tuple


def get_busy_intervals(service, calendar_id: str, start: datetime, end: datetime) -> List[Tuple[datetime, datetime]]:
    """Return list of busy intervals within [start, end)."""
    # TODO: implement – stub
    return []


def find_first_fit(busy: List[Tuple[datetime, datetime]], duration: timedelta, work_start: time, work_end: time, min_gap: timedelta) -> datetime | None:
    """Greedy search: return start time for first slot that fits the task or None."""
    # TODO: implement – stub
    return None
