"""Specific mathematical review actions activated by text or graph context."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True, slots=True)
class ReviewTrigger:
    id: str
    keywords: tuple[str, ...]
    action: str

    def __post_init__(self) -> None:
        if not self.id or not self.keywords or not self.action:
            raise ValueError("trigger id, keywords, and action are required")


@dataclass(frozen=True, slots=True)
class TriggerMatch:
    trigger: ReviewTrigger
    matched_keywords: tuple[str, ...]


def load_triggers(path: str | Path) -> tuple[ReviewTrigger, ...]:
    with Path(path).open("rb") as handle:
        payload = tomllib.load(handle)
    if payload.get("schema_version") != 1:
        raise ValueError("unsupported trigger schema")
    triggers = []
    seen = set()
    for record in payload.get("trigger", []):
        trigger = ReviewTrigger(
            id=record["id"],
            keywords=tuple(record["keywords"]),
            action=record["action"],
        )
        if trigger.id in seen:
            raise ValueError(f"duplicate trigger id: {trigger.id}")
        seen.add(trigger.id)
        triggers.append(trigger)
    return tuple(triggers)


def match_triggers(text: str, triggers: Iterable[ReviewTrigger]) -> list[TriggerMatch]:
    lowered = text.casefold()
    matches = []
    for trigger in triggers:
        keywords = tuple(keyword for keyword in trigger.keywords if keyword.casefold() in lowered)
        if keywords:
            matches.append(TriggerMatch(trigger, keywords))
    return matches
