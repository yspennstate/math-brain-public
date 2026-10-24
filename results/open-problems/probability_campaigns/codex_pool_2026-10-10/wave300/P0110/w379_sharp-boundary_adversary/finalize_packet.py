"""Finalize draft metadata and receipts; does not ingest or write any live store."""
from datetime import datetime, timezone
from pathlib import Path
import difflib
import json
import re

ROOT = Path(__file__).resolve().parent


def read(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def write(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


reviews = []
review_path = Path(r"~\brain_workers\w380\CLAIMS.jsonl")
for line in review_path.open(encoding="utf-8-sig"):
    row = json.loads(line)
    if row.get("claim_id") in {"w380-review-w379-C1", "w380-review-w379-C2"}:
        assert row.get("verdict") == "KEEP"
        reviews.append(row)
assert len(reviews) == 2
(ROOT / "REFEREE_VERDICTS.jsonl").write_text(
    "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in reviews), encoding="utf-8"
)

claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
claims = [row for row in claims if row.get("id") != "w379-P0110-C3"]
for row in claims:
    row["status"] = "independently checked proof"
    row["review_status"] = "KEEP"
    row["review_evidence"] = str(review_path)
    row["remaining_gap"] = "No gap found in this auxiliary result by w380. Original P0110, centered fluctuation transfer, and interior-direction comparisons remain unresolved; audit account/model provenance is for the coordinator before ingestion."
measure = read("MEASUREMENTS.json")
assert measure["status"] == "PASS" and measure["total_configurations"] == 320
claims.append({
    "id": "w379-P0110-C3",
    "status": "numerical evidence",
    "statement": "The exact finite two-path graph checker passes all 64 fair {1,2} configurations at n=2 and all 256 at n=3 against Dijkstra. At n=3 it finds exactly one strictly cheaper detour and mean saving 1/256; twenty separated n=3 blocks share no edges.",
    "assumptions": ["finite graph containing only the direct axial path and disjoint height-one detour", "weights range over all assignments in {1,2}"],
    "source": {"type": "owner-own-work", "path": "MEASUREMENTS.json", "command": measure["command"]},
    "proof_or_counterexample": "Exhaustive finite edge assignments and independent Dijkstra distances; verify_detour.py. Infinite-volume conclusion instead uses C2's reviewed proof.",
    "independent_reviewer": "w380",
    "review_status": "w380 separately reproduced the n=3 event probability and 1/1280 bound; the full 320-case Dijkstra receipt is the author's run",
    "remaining_gap": "Finite checks alone do not prove an exponent or the infinite-lattice claim.",
})
(ROOT / "CLAIMS.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in claims), encoding="utf-8")

store = read("STORE_TARGET_ROWS.json")
assert len(store["rows"]) == 2
target = next(r for r in store["rows"] if r["title"].startswith("Open problem:"))
target_meta = json.loads(target["metadata_json"])
logical = target_meta["logical_id"]
assert logical == "math:probability.core:open-problem-p0110-an-iid-fpp-law-with-proved-kpz-exponent-relation"

source = read("SOURCE_STATUS.json")
old_primary = source["primary_target"]
if "alternate_primary_revision" not in source:
    source["alternate_primary_revision"] = {
        "url": old_primary["url"], "version": old_primary["version_read"],
        "location": old_primary["location"], "exact_question": old_primary["exact_question"], "equation_number": "4.13"
    }
source["primary_target"].update({
    "url": "https://arxiv.org/pdf/1511.03262v2",
    "version_read": "arXiv:1511.03262v2, 2016; PDF dated September 26, 2016",
    "location": "Question 22, Section 4.3 printed pp.88-89; question also reproduced in summary printed p.147; equation (4.19)",
    "exact_question": "Find a distribution of passage times where (4.19) holds.",
    "version_warning": "Both revisions directly checked: the 2015 author-hosted PDF uses (4.13), while arXiv v2 uses (4.19). Do not mix numbering.",
    "recovered_catalog_statement": "Exhibit a nondegenerate iid undirected FPP law with well-defined fluctuation and wandering exponents satisfying chi=2xi-1.",
    "catalog_statement_source": {"node_id": target["id"], "logical_id": logical, "read_only_receipt": "STORE_TARGET_ROWS.json"},
})
source["additional_primary_checks"] = [
    {"url": "https://arxiv.org/abs/1109.0523", "title": "A simplified proof of the relation between scaling exponents in first-passage percolation", "scope": "Auffinger-Damron prove chi<=2xi-1 under existence of Chatterjee's exponents without the nearly-gamma assumption. This is still a conditional exponent result."},
    {"url": "https://arxiv.org/abs/2604.01214", "title": "Rotationally invariant first passage percolation: Breaking the n/log n variance barrier", "scope": "Basu-Sidoravicius-Sly (2026) give Var T=O(n^(1-epsilon)) for a rotationally invariant Riemannian planar model. The abstract does not exhibit the fixed iid nearest-neighbor lattice law or exact exponent relation sought by P0110."},
]
source["prior_checks"].update({
    "exact_id_search": "Recovered exact target and prior attempt from two exported nodes, then verified both node IDs in the current read-only population SQLite store. No exact P0110 match in the named H/I attempts or Lean tree; no KPZ/FPP title match in the named H/I text artifacts. Original target requires a nondegenerate law.",
    "prior_attempt": "The existing 2026-09-07 attempt is a conditional curvature balance n^(2xi-1), or kappa*xi-(kappa-1); its own statement says exponent existence and passage-time replacement error control remain unproved. It is a concept with truth_status unverified, not a solved theorem.",
    "owner_solved_or_retired_status": "No solved status in the exact target/prior-attempt nodes checked; current openness remains UNKNOWN after bounded checks.",
})
source["review_state"] = "w380 independently KEEP C1/C2; REFEREE_VERDICTS.jsonl stores the receipts. w379 directly KEEP w378 L1/L2. Coordinator still must verify account/model provenance before ingestion. No original-target proof is claimed."
write("SOURCE_STATUS.json", source)

bundle = read("bundle_001.json")
for e in bundle["entries"]:
    e["namespace"] = "probability.percolation"
    e["source"]["revision"] = "2026-10-10-w380-keep-draft"
    e["statement"] = e["statement"].replace(
        "DRAFT AUTHOR DERIVATION, INDEPENDENT REFEREE PENDING:",
        "DRAFT MATHEMATICAL DERIVATION, INDEPENDENTLY CHECKED BY w380 (KEEP); COORDINATOR INTEGRATION PENDING:"
    ).replace("the pending author detour derivation", "the independently checked detour derivation").replace(
        "This is a pending special-case obstruction", "This is an independently checked special-case obstruction"
    )
    e["title"] = e["title"].replace("Draft author proof:", "Reviewed draft:")
for r in bundle["relations"]:
    if r["kind"] == "refutes":
        r["rationale"] = "The independently checked positive lower linear rate contradicts an almost-sure o(N) raw axial restriction error in the stated nonconstant-law class; differently centered or interior-direction bridges are outside both endpoints."
bundle["relations"] = [r for r in bundle["relations"] if r.get("to_existing_logical") != logical]
bundle["relations"].append({
    "from_key": "linear-gap", "to_existing_logical": logical, "kind": "semantic_association",
    "rationale": "This independently checked raw axial restriction obstruction identifies a failing auxiliary route relevant to the existing existential fixed-law KPZ target. It neither proves nor refutes that original problem. Both target and prior conditional attempt were read by exact ID from the read-only store."
})
entry = next(e for e in bundle["entries"] if e["key"] == "linear-gap")
edge_row = {
    "id": "w379-P0110-E1", "status": "DRAFT", "relation_kind": "semantic_association",
    "from_key": entry["key"], "from_statement_quote": entry["statement"], "from_source": "INDEPENDENT.md; w380 KEEP",
    "to_existing_logical": logical, "to_statement_quote": target["body"], "to_source": "STORE_TARGET_ROWS.json, exact node " + target["id"],
    "rationale": bundle["relations"][-1]["rationale"],
    "independent_reviewer": "w380 checked the mathematical C2 endpoint; relation/provenance landing remains for coordinator",
}
(ROOT / "EDGE_EVIDENCE.jsonl").write_text(json.dumps(edge_row, ensure_ascii=False) + "\n", encoding="utf-8")

keys = {e["key"] for e in bundle["entries"]}
allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
adj = {k: [] for k in keys}
for e in bundle["entries"]:
    assert re.fullmatch(r"[a-z][a-z0-9]*(\.[a-z][a-z0-9]*)*", e["namespace"])
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", e["logical_name"])
    assert e["kind"] in {"definition", "concept"} and e["proof_text"] is None
    assert e["source"]["license"] == "owner-own-work"
for r in bundle["relations"]:
    assert r["kind"] in allowed and r["from_key"] in keys
    assert ("to_key" in r) != ("to_existing_logical" in r)
    if "to_key" in r:
        assert r["to_key"] in keys
    else:
        assert r["to_existing_logical"] == logical
    if r["kind"] == "depends_on":
        adj[r["from_key"]].append(r["to_key"])
def visit(k, active, seen):
    assert k not in active
    if k in seen:
        return
    for child in adj[k]:
        visit(child, active | {k}, seen)
    seen.add(k)
seen = set()
for k in keys:
    visit(k, set(), seen)

body = json.dumps(bundle, indent=2, ensure_ascii=False) + "\n"
(ROOT / "bundle_001.json").write_text(body, encoding="utf-8")
dest = Path(r"~\math-brain-inbox\w379\bundle_001.json")
assert dest.exists(), "Do not silently recreate a draft moved by an integrator"
part = dest.with_suffix(".part")
part.write_text(body, encoding="utf-8")
part.replace(dest)
patch = "".join(difflib.unified_diff([], body.splitlines(keepends=True), fromfile="a/math-brain-inbox/w379/bundle_001.json", tofile="b/math-brain-inbox/w379/bundle_001.json"))
(ROOT / "patches" / "01_p0110_draft_bundle.diff").write_text(patch, encoding="utf-8")
receipt = {
    "prepared": True, "submitted": {"state": True, "path": str(dest), "at": datetime.now(timezone.utc).isoformat()},
    "reviewed": {"state": True, "reviewer": "w380", "verdict": "KEEP C1 and C2", "evidence": str(review_path), "scope": "Mathematical author proof checked; cross-account and served-model provenance not certified by worker."},
    "ingested": {"state": "not observed", "integrator_run_by_worker": False},
    "retrievable": {"state": "not tested for new draft"},
    "validation": {"status": "PASS", "command": "python -X utf8 ~/brain_workers/w379/finalize_packet.py", "entries": len(bundle["entries"]), "relations": len(bundle["relations"]), "depends_on_acyclic": True, "existing_target_exact_id_verified_read_only": True, "draft_kinds": "one definition, three concepts"},
    "live_store_mutated_by_worker": False,
}
write("BUNDLE_STATUS.json", receipt)
hooks = [json.loads(l) for l in (ROOT / "HOOK_PROPOSALS.jsonl").read_text(encoding="utf-8").splitlines() if l]
for h in hooks:
    h["evidence"] = h["evidence"].replace("(referee pending)", "(w380 independently KEEP)")
    assert len(h["text"]) <= 300
(ROOT / "HOOK_PROPOSALS.jsonl").write_text("".join(json.dumps(h, ensure_ascii=False) + "\n" for h in hooks), encoding="utf-8")
print(json.dumps({"status": "PASS", "reviewed_claims": 2, "claims_rows": len(claims), "draft_entries": len(bundle["entries"]), "draft_relations": len(bundle["relations"]), "hook_proposals_staged": len(hooks), "target_live_id_verified": target["id"]}, indent=2))
