"""Coordinator-only bookkeeping for actual, already-executed agent operations.

Read one JSON object from stdin: ``new`` is one actual successful spawn row;
``updates`` maps three-digit agent numbers to already-confirmed field changes.
This script never launches agents or infers completion from an existing file.
"""
from pathlib import Path
import datetime
import json
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    path = root / "execution_ledger.json"
    ledger = json.loads(path.read_text())
    change = json.load(sys.stdin)
    rows = ledger["agents"]
    by_number = {row["number"]: row for row in rows}
    if "new" in change:
        row = change["new"]
        assert row["number"] not in by_number, "Duplicate actual agent number"
        assert row["task_name"] not in {x["task_name"] for x in rows}
        assert int(row["number"]) == len(rows) + 1
        assert row["model"] == "gpt-6-astra"
        assert row["reasoning_effort"] == "max"
        assert row["status"] == "running"
        rows.append(row)
        by_number[row["number"]] = row
    for number, updates in change.get("updates", {}).items():
        row = by_number[number]
        assert not (row.get("immutable") and updates.get("status", "completed") != "completed")
        if updates.get("status") == "completed":
            report = root / row["report_path"]
            assert report.is_file() and report.stat().st_size > 0
            updates["immutable"] = True
        row.update(updates)
    assert len(rows) <= ledger["requested_total"] == 100
    assert sorted(int(row["number"]) for row in rows) == list(range(1, len(rows) + 1))
    active = [row["number"] for row in rows if int(row["number"]) >= 12 and row["status"] == "running"]
    assert len(active) <= ledger["worker_concurrency_cap"] == 5
    ledger["actual_successful_spawns_recorded"] = len(rows)
    ledger["completed_worker_reports"] = sum(int(row["number"]) >= 12 and row["status"] == "completed" for row in rows)
    ledger["updated"] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    path.write_text(json.dumps(ledger, indent=2) + "\n")
    print(json.dumps({"actual_agents": len(rows), "completed_workers": ledger["completed_worker_reports"], "active_workers": active}))


if __name__ == "__main__":
    main()
