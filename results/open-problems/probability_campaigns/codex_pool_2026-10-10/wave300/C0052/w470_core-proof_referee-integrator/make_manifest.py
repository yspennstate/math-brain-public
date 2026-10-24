"""Hash and validate the scoped referee handoff without touching live stores."""

import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
names = [
    "SOURCE_STATUS.json",
    "ATTEMPT.md",
    "CLAIMS.jsonl",
    "REVIEW_PEERS.md",
    "REVIEW_PACKET.md",
    "ENDPOINT_TREE_OBSTRUCTION.md",
    "REFEREE_RESPONSE.md",
    "STORE_CORRECTIONS.jsonl",
    "REPORT.md",
    "SUBMISSION.json",
]
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
corrections = [json.loads(line) for line in (root / "STORE_CORRECTIONS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len({row["id"] for row in claims}) == len(claims)
assert len(corrections) == 1 and corrections[0]["verdict"] == "FIX"
assert next(row for row in claims if row["id"] == "C0052-reduction-03")["independent_reviewer"].startswith("w473")
submission = json.loads((root / "SUBMISSION.json").read_text(encoding="utf-8"))
bundle = Path(submission["bundle_path"])
assert bundle.exists()
assert hashlib.sha256(bundle.read_bytes()).hexdigest() == submission["bundle_sha256"]
assert not submission["reviewed"] and submission["ingested"] is None and submission["retrievable"] is None
paths = [root / name for name in names] + [bundle]
manifest = {
    "worker": "w470",
    "target": "C0052",
    "parent_problem_solved": False,
    "current_openness": "UNKNOWN",
    "served_model_evidence": "UNAVAILABLE_FROM_THIS_THREAD; requested setting is not an attestation",
    "peer_math_review": "scoped KEEP/FIX in REVIEW_PEERS.md",
    "w473_own_reduction": "FIX endpoint joint law applied; conditional algebra retained",
    "w473_new_tree_lemma": "PENDING",
    "bundle_submitted": True,
    "bundle_reviewed": False,
    "bundle_ingested": None,
    "bundle_retrievable": None,
    "claim_rows": len(claims),
    "store_correction_rows": len(corrections),
    "files": [{"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in paths],
}
(root / "FINAL_MANIFEST.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print(json.dumps({"claim_rows": len(claims), "correction_rows": len(corrections),
                  "hashed_files": len(paths), "bundle_hash_match": True,
                  "w473_reduction_fix_applied": True}, indent=2))
