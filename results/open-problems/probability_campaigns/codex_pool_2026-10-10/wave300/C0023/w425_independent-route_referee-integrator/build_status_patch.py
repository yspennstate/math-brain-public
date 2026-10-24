"""Build a reviewable one-line C0023 status correction without touching the source."""

from hashlib import sha256
from pathlib import Path
import json

source = Path("~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl")
target = Path(__file__).parent / "patches" / "01_c0023_status.diff"

with source.open(encoding="utf-8") as stream:
    for number, record in enumerate(stream, 1):
        if number == 23:
            break
    else:
        raise RuntimeError("C0023 line missing")

old = record.rstrip("\r\n")
data = json.loads(old)
assert data["problem_id"] == "C0023"
assert data["current_status"] == "no_resolution_found_in_documented_search"
assert data["verification"] == "unreviewed"
new = old.replace(
    '"current_status": "no_resolution_found_in_documented_search"',
    '"current_status": "claimed_solved_pending_independent_formal_audit"',
    1,
).replace(
    '"verification": "unreviewed"',
    '"verification": "source_statement_checked_formal_claim_not_independently_rebuilt"',
    1,
)
assert old != new
new_data = json.loads(new)
assert new_data["problem_id"] == "C0023"
assert new_data["historical_status"] == data["historical_status"]
assert new_data["result_status"] == data["result_status"]
assert new_data["status_search"] == data["status_search"]
assert new_data["current_status"] == "claimed_solved_pending_independent_formal_audit"

target.parent.mkdir(parents=True, exist_ok=True)
live = source.as_posix()
patch = f"--- a/{live}\n+++ b/{live}\n@@ -23 +23 @@\n-{old}\n+{new}\n"
target.write_text(patch, encoding="utf-8")
print("line=23 old_sha256=" + sha256(old.encode()).hexdigest())
print("new_sha256=" + sha256(new.encode()).hexdigest())
print("patch=" + str(target))
