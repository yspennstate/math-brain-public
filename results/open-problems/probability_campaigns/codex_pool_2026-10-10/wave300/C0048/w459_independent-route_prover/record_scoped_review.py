"""Record the received peer verdict without auditing the audit or promoting claims."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUDIT = Path("~/brain_workers/w460/AUDIT_W459.md")


def main():
    data = AUDIT.read_bytes()
    assert "Verdict: KEEP L1-L4 in their stated finite or conditional scope." in data.decode("utf-8")
    audit = {"reviewer": "w460", "verdict": "KEEP",
             "scope": "L1-L4 in their stated finite or conditional scope",
             "source_path": AUDIT.as_posix(), "source_sha256": hashlib.sha256(data).hexdigest(),
             "audit_checked_again": False, "independent_route_saved_first": "reported by auditor",
             "parent_conjecture_proved": False, "novelty_claim": False,
             "different_model_or_login_verified": False,
             "served_model_identities": "unavailable", "designated_referee_w461": "pending"}
    (ROOT / "PEER_REVIEW_RECEIPT.json").write_text(json.dumps(audit, indent=2), encoding="utf-8")
    claim_path = ROOT / "CLAIMS.jsonl"
    rows = [json.loads(x) for x in claim_path.read_text(encoding="utf-8").splitlines() if x]
    for row in rows:
        if row["id"] in {"w459-C0048-L1", "w459-C0048-L2", "w459-C0048-L3", "w459-C0048-L4"}:
            row["independent_reviewer"] = "w460 (scoped KEEP); w461 (designated referee pending)"
            row["independent_review_state"] = "one scoped mathematical KEEP; promotion provenance unverified"
            row["peer_review_receipt"] = "PEER_REVIEW_RECEIPT.json"
    claim_path.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in rows), encoding="utf-8")
    source_path = ROOT / "SOURCE_STATUS.json"
    source = json.loads(source_path.read_text(encoding="utf-8"))
    source["scoped_independent_reviews"] = [audit]
    source["independent_review_state"] = "w460 scoped KEEP; designated w461 pending"
    source["reviewed"] = False
    source["reviewed_means"] = "designated referee complete packet review; still pending"
    source_path.write_text(json.dumps(source, indent=2) + "\n", encoding="utf-8")
    receipt_path = ROOT / "REVIEW_RECEIPT.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    for name in receipt["artifact_sha256"]:
        receipt["artifact_sha256"][name] = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    receipt["artifact_sha256"]["PEER_REVIEW_RECEIPT.json"] = hashlib.sha256((ROOT / "PEER_REVIEW_RECEIPT.json").read_bytes()).hexdigest()
    receipt["independent_review_state"] = "w460 scoped KEEP; designated w461 pending"
    receipt["scoped_mathematical_keeps"] = 1
    receipt["different_model_or_login_verified"] = False
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"recorded": "w460 scoped KEEP", "designated_referee": "w461 pending",
                      "claim_rows": len(rows), "no_promotion": True}))


if __name__ == "__main__":
    main()
