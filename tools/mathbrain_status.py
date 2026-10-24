"""One-glance status of the population loop. Read-only everywhere."""

from __future__ import annotations

import glob
import json
import os
import sys
import time
from pathlib import Path

BUILD = Path(r"~\math-brain-build")
sys.path.insert(0, str(BUILD / "src"))

from math_brain.store import ResearchStore  # noqa: E402

INBOX = Path(r"~\math-brain-inbox")
LEDGER = BUILD / "local" / "population" / "integration_ledger.jsonl"
STORE = BUILD / "local" / "population" / "brain.sqlite3"
SURFACED = Path.home() / ".claude" / "dreaming" / "surfaced.tsv"


def main() -> int:
    with ResearchStore(STORE) as store:
        nodes = sum(1 for _ in store.iter_nodes())
        edges = sum(1 for _ in store.iter_edges())
    lines = LEDGER.read_text(encoding="utf-8").splitlines() if LEDGER.exists() else []
    ingested = sum(1 for x in lines if '"ingested"' in x)
    rejected = sum(1 for x in lines if '"rejected"' in x)
    last = json.loads(lines[-1]) if lines else {}
    ledger_age_min = None
    if last.get("ts"):
        try:
            age = time.time() - time.mktime(time.strptime(last["ts"], "%Y-%m-%dT%H:%M:%S"))
            ledger_age_min = round(age / 60, 1)
        except ValueError:
            pass
    pending = [p for p in glob.glob(str(INBOX / "*" / "bundle_*.json"))]
    done_names = set()
    for line in lines:
        try:
            done_names.add(json.loads(line)["draft"])
        except Exception:  # noqa: BLE001
            continue
    waiting = [
        p for p in pending
        if f"{Path(p).parent.name}/{Path(p).name}" not in done_names
    ]
    parts = glob.glob(str(INBOX / "*" / "*.part"))
    fired = 0
    if SURFACED.exists():
        fired = sum(
            1 for x in SURFACED.read_text(encoding="utf-8").splitlines()
            if x.endswith("mathbrain")
        )
    print(
        f"store {nodes}n/{edges}e | ledger {ingested} ingested {rejected} rejected "
        f"(last {ledger_age_min} min ago: {last.get('draft', '-')}) | "
        f"inbox waiting {len(waiting)} drafts, {len(parts)} parts | "
        f"real-prompt fires {fired}"
    )
    for p in waiting[:5]:
        print("  waiting:", f"{Path(p).parent.name}/{Path(p).name}")
    if os.environ.get("MATHBRAIN_STATUS_VERBOSE"):
        for line in lines[-3:]:
            print(" ", line[:150])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
