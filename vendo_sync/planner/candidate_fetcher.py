"""Fetch backlog events (candidates) from SOURCE_CAL_ID.

Requirements:
* Event **bez** `start.dateTime` → kandydat do zaplanowania
* Metadane w `extendedProperties.private`:
    - duration  (ISO-8601, np. ``PT90M``)
    - priority  (1-5, 1 = najwyższy)
    - deadline  (opcjonalnie, RFC3339)
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Candidate:
    event_id: str
    summary: str
    duration_minutes: int
    priority: int
    deadline: Optional[datetime] = None


def fetch_candidates(service, calendar_id: str) -> List[Candidate]:
    """Return list of backlog tasks to schedule."""
    # TODO: implement API call – stub for scaffold
    return []
