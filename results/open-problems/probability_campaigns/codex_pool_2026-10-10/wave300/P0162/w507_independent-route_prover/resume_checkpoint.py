from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()
receipt = {
    "utc": now,
    "author_agent": "w507",
    "reviewer": "w509",
    "verdict": "KEEP",
    "scope": "ATTEMPT.md L1-L7: restriction ledger, bent-selector obstruction, arbitrary bent-base extension, exact influence range, parity-twist counterexample, character translation identity",
    "evidence": {
        "verdicts": "~/brain_workers/w509/REVIEW_VERDICTS.jsonl",
        "proof_check": "~/brain_workers/w509/REVIEW_PACKET.md",
        "additional_adversarial_check": "~/brain_workers/w508/CORE_PROOF_AUDIT.md",
        "additional_adversarial_scope": "L1-L3 only"
    },
    "parent_problem_solved": False,
    "hardest_remaining_gap": "Dimension-free good-coordinate selection or aggregate entropy charge for every Boolean function",
    "served_model_author": "UNKNOWN",
    "served_model_referee": "UNKNOWN",
    "different_model_gate": "UNVERIFIED",
    "ingestion": "UNVERIFIED",
    "retrieval": "UNVERIFIED"
}
with (root / "RESUME_RESULTS.jsonl").open("a", encoding="utf-8") as out:
    out.write(json.dumps(receipt, ensure_ascii=False) + "\n")
(root / "REVIEW_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
previous = (root / "STATUS.md").read_text(encoding="utf-8")
log = previous.split("\n\n", 1)[1] if "\n\n" in previous else previous
(root / "STATUS.md").write_text(
    "STATE: WORKING\n"
    "NEXT: Build the scoped integration handoff with artifact hashes and review evidence, then send it to codex-01a12190.\n\n"
    + now + ": Resumed after network drop; recorded w509 KEEP L1-L7 and w508 KEEP L1-L3. General FEI remains unproved; response-side served-model and integration gates remain unverified.\n"
    + log, encoding="utf-8"
)
print(json.dumps({"saved": "REVIEW_RECEIPT.json", "result_row": "RESUME_RESULTS.jsonl", "scope": "L1-L7"}))
