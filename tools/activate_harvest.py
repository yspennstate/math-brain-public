"""Quality gate for harvested .part bundles: filter, re-slug, then activate.

Drops entries whose statement is a stub (ends in a colon, too short, or ends
mid-word without sentence punctuation), re-derives logical_name from the
RETURNED page title when a redirect changed the topic, dedupes within the
draft, and renames the cleaned draft from .part to .json so the watching
integrator picks it up. Prints what was dropped and why.
"""

from __future__ import annotations

import json
import os
import re
import sys

MIN_LEN = 120


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return ("wiki-" + slug)[:80]


def healthy(statement: str) -> str | None:
    s = statement.strip()
    if len(s) < MIN_LEN:
        return "too-short"
    if s.endswith(":"):
        return "ends-with-colon-stub"
    if not re.search(r"[.!?]\s*$", s):
        return "no-terminal-sentence"
    # math-stripped holes: the REST extract drops formulas, leaving grammatical gaps
    if re.search(r"\s[,.;]", s):
        return "hole-space-before-punctuation"
    if re.search(r"\b(one has|reads|denoted by|given by|defined as|defined by|equal to)\s*(where|[,.])", s, re.I):
        return "hole-missing-formula"
    if re.search(r"\b(in|of|to|from|over|by|with)\s+(has|is|are|was|be|can|converges|holds|satisfies)\b", s):
        return "hole-preposition-verb-gap"
    return None


def activate(part_path: str) -> None:
    with open(part_path, encoding="utf-8") as fh:
        draft = json.load(fh)
    kept = []
    seen = set()
    for entry in draft["entries"]:
        why = healthy(entry["statement"])
        if why:
            print(f"DROP {entry['title']}: {why}")
            continue
        slug = slugify(entry["title"])
        entry["logical_name"] = slug
        entry["key"] = slug[:60]
        if slug in seen:
            print(f"DROP {entry['title']}: duplicate-after-reslug")
            continue
        seen.add(slug)
        kept.append(entry)
    dropped = len(draft["entries"]) - len(kept)
    draft["entries"] = kept
    draft["relations"] = []
    out = part_path[: -len(".part")] + ".json"
    tmp = out + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(draft, fh, indent=1)
    os.replace(tmp, out)
    os.remove(part_path)
    print(f"ACTIVATED {out}: kept {len(kept)}, dropped {dropped}")


if __name__ == "__main__":
    for path in sys.argv[1:]:
        activate(path)
