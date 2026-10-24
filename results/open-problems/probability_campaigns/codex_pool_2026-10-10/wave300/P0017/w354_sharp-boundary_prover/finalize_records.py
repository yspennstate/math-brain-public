import json
from datetime import datetime, timezone
from pathlib import Path

base = Path(__file__).resolve().parent
review = json.loads((base / "REFEREE_VERDICTS.json").read_text(encoding="utf-8"))
verdicts = {row["claim_id"]: row for row in review["records"]}
claims = [json.loads(line) for line in (base / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
for claim in claims:
    verdict = verdicts[claim["id"]]
    assert verdict["verdict"] == "KEEP" and verdict["reviewer"] == "w356"
    claim["independent_reviewer"] = "w356"
    claim["independent_review"] = {"verdict": "KEEP", "status": verdict["status"], "receipt": "REFEREE_VERDICTS.json", "scope": verdict["scope"], "corroboration": "w355/W354_AUDIT.md independently keeps the complete special-case packet", "account_distinctness_verified": False}
    claim["status"] = "independently checked proof"
    claim["remaining_gap"] = "None for the stated special case. This does not resolve the parent KLS target; the worker's full-gradient conditional route remains incomplete."
(base / "CLAIMS.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in claims), encoding="utf-8")
source = json.loads((base / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["review_status"] = "w356 KEEP claims 001-004; w355 independently keeps the complete special-case packet. Mathematical validity of the recent full KLS preprints remains unaudited here."
source["mathematical_review_receipt"] = "REFEREE_VERDICTS.json"
(base / "SOURCE_STATUS.json").write_text(json.dumps(source, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
peer_entries = json.loads((base / "PEER_DRAFT_BOUNDARIES.json").read_text(encoding="utf-8"))
lookup = {(row["peer"], row["key"]): row for row in peer_entries}
canonical = {"p0017-source-context": ("w355", "p0017-status"), "uniform-fiber-proposal": ("w356", "pointwise-bridge"), "mean-fiber-proposal": ("w356", "averaging-bridge"), "simplex-fibers": ("w356", "simplex"), "optimal-directional-common-theorem": ("w356", "weighted"), "triangle-polynomial-d2": ("w356", "triangle-polynomial")}
dedup = []
for own_key, peer_key in canonical.items():
    row = lookup[peer_key]
    dedup.append({"omitted_duplicate": own_key, "canonical_peer": row["peer"], "canonical_draft": row["file"], "canonical_key": row["key"], "canonical_logical": "math:" + row["namespace"] + ":" + row["logical_name"], "supporting_quote": row["statement"], "state": "canonical peer draft; admission and live presence not assumed"})
(base / "DEDUP_MAP.json").write_text(json.dumps({"created_at": datetime.now(timezone.utc).isoformat(), "common_cards_omitted": 6, "retained": ["localized admissible Neumann witness method", "all-dimension polynomial family with full transverse energy"], "canonical": dedup}, indent=2, ensure_ascii=False), encoding="utf-8")
payload = json.loads((base / "drafts" / "bundle_001.json").read_text(encoding="utf-8"))
entries = {row["key"]: row for row in payload["entries"]}
live = json.loads((base / "LIVE_TARGET_RECEIPT.json").read_text(encoding="utf-8"))["rows"]
live_by_id = {row["metadata"]["logical_id"]: row for row in live}
edges = []
for number, relation in enumerate(payload["relations"], 1):
    start = entries[relation["from_key"]]
    if "to_key" in relation:
        end = entries[relation["to_key"]]
        end_id = "math:" + end["namespace"] + ":" + end["logical_name"]
        end_quote = end["statement"]
        end_state = "same draft concept"
    else:
        end_id = relation["to_existing_logical"]
        end_quote = live_by_id[end_id]["body"]
        end_state = "live logical endpoint verified read-only"
    edges.append({"id": f"w354-P0017-edge-{number:03d}", "from_logical": "math:" + start["namespace"] + ":" + start["logical_name"], "from_quote": start["statement"], "to_logical": end_id, "to_quote": end_quote, "to_state": end_state, "kind": relation["kind"], "rationale": relation["rationale"], "status": "draft relation, mathematical special cases peer checked; coordinator relation admission pending"})
(base / "RELATION_EVIDENCE.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in edges), encoding="utf-8")
deferred = []
for own_key, peer_key, kind, why in [("localized-neumann", ("w356", "simplex"), "cites", "Uses the same exact fiber law but supplies the distinct localized admissible witness method."), ("polynomial-family", ("w356", "triangle-polynomial"), "generalizes", "At d=2,k=2 the family reproduces all three energies of the triangle specialization."), ("polynomial-family", ("w356", "averaging-bridge"), "refutes", "The exact directional quotient can exceed the unweighted mean while the transverse energy is explicitly present.")]:
    start = entries[own_key]
    end = lookup[peer_key]
    deferred.append({"from_key": own_key, "to_existing_logical": "math:" + end["namespace"] + ":" + end["logical_name"], "kind": kind, "rationale": why, "from_quote": start["statement"], "to_quote": end["statement"], "status": "NOT SUBMITTED: add only after canonical peer target is verified in the live store"})
(base / "DEFERRED_RELATIONS.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in deferred), encoding="utf-8")
print(json.dumps({"referee_keeps": len(claims), "deduplicated_common_cards": len(dedup), "retained_entries": len(entries), "submitted_relation_evidence_rows": len(edges), "deferred_relations": len(deferred)}, indent=2))
