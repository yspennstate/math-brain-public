"""Prepare local review artifacts; never ingest or alter the live store."""
import json
import re
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
CLAIMS = ROOT / "CLAIMS.jsonl"
rows = [json.loads(l) for l in CLAIMS.read_text(encoding="utf-8").splitlines() if l.strip()]
if not any(r["id"] == "w366-C5" for r in rows):
    rows.append({"id": "w366-C5", "problem": "P0104",
                 "statement": "For iid edge weights in [1,1+epsilon] with variance sigma^2 and n epsilon<2, the geodesic from 0 to n e1 is the deterministic straight path before and after independent edge refresh with probability delta. Overlap equals n, Cov(T,T^delta)=(1-delta)n sigma^2, and E[(T-T^delta)^2]=2 delta n sigma^2.",
                 "assumptions": ["undirected nearest-neighbour square lattice", "epsilon>0", "n>=1 integer", "n epsilon<2", "iid weights with that support", "independent edge refresh probability delta in [0,1]"],
                 "source": {"kind": "owner-own-work", "artifact": "LEMMAS.md#c5", "novelty": "not claimed"},
                 "proof_or_counterexample": "Strict support comparison gives the unique straight route in both environments. Compute the covariance of each refreshed edge pair and sum independent deterministic edges.",
                 "independent_reviewer": "w368 assigned; verdict pending",
                 "remaining_gap": "No law-dependent asymptotic chaos estimate follows; this only refutes a law-uniform overlap bridge.",
                 "status": "proved special case", "audit_state": "unreviewed"})
for r in rows:
    r["independent_reviewer"] = "w368 assigned; mathematical verdict pending"
    if r["id"] == "w366-C1":
        r["remaining_gap"] = "No mathematical gap asserted in this fixed-endpoint moment criterion; constants depend on n. No fixed-law KPZ power estimate follows."
CLAIMS.write_text("".join(json.dumps(r, ensure_ascii=False)+"\n" for r in rows), encoding="utf-8")

status = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
store = Path(r"~/math-brain-build/local/population/brain.sqlite3")
connection = sqlite3.connect(store.as_uri()+"?mode=ro", uri=True, timeout=2)
ids = ["claim_32684d2ece2943d218971312722a87f42333b030b9c7a29f034d6c11f31f8f1d",
       "claim_9ffe9930e9d9ed5c9d98ff4d61a32155d942cd754628487fc173a2d2c6493b2f"]
cards = []
for row in connection.execute("SELECT id,title,body,metadata_json FROM nodes WHERE id IN (?,?)", ids):
    cards.append({"id": row[0], "title": row[1], "body": row[2], "metadata": json.loads(row[3])})
connection.close()
assert len(cards) == 2
status["canonical_cards"] = cards
status["original_record"] = {"status": "recovered through canonical P0104 problem and attempt cards",
                             "primary_source": "https://arxiv.org/pdf/1511.03262v2",
                             "locator": "Questions 13 and 15, printed p.37, PDF page index 36",
                             "statement": "Under suitable law hypotheses obtain chi(d)<1/2 for d>=2, chi(2)=1/3, and chi(d)>0 in suitable dimensions.",
                             "source_quote": "under suitable conditions on F",
                             "precision": "Source leaves suitable-law class and asymptotic equivalence convention open; use explicit liminf/limsup for a fixed law in any actual proof.",
                             "provenance_note": "Historical original Codex worktree is absent. The canonical card is curated_secondary with truth_status unverified. Primary v2 statement read directly; no source/hash check is counted as proof."}
status["prior_attempt_digest"] = "Known n/log n variance bounds do not give a strict power exponent; a polynomial saving and a matching lower bound remain missing."
status["named_H_I_lean_checks"] = "Targeted P0104 matches absent; no proof inferred from that absence."
status["formal_check"] = {"performed": False, "receipt": None, "note": "Exact finite arithmetic and author proofs only; no Lean theorem or axiom audit claimed."}
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8")

namespace = "probability.firstpassage"
source = {"source_id": "owner-campaign-w366-p0104-boundary-20261010",
          "url": "file:///~/brain_workers/w366/LEMMAS.md",
          "revision": "2026-10-10-author-proof-awaiting-independent-review",
          "license": "owner-own-work", "excerpt": None}
entries = [{"key": "fpp-definition", "namespace": namespace,
            "logical_name": "iid-square-lattice-first-passage-time-definition",
            "kind": "definition", "title": "Iid square-lattice first-passage time",
            "statement": "On the undirected nearest-neighbour square lattice Z^2 assign iid finite almost surely nonnegative edge weights t_e. For distinct vertices x,y, T(x,y) is the infimum over all finite x-to-y lattice paths of the sum of weights along the path, counting a traversed edge each time it is used.",
            "proof_text": None, "assumptions": ["iid finite almost surely nonnegative edge weights"],
            "domain": "probability theory", "source": source}]
names = {"w366-C1": ("fixed-endpoint-planar-fpp-moment-criterion", "DRAFT: exact fixed-endpoint FPP moment criterion"),
         "w366-C2": ("pareto-planar-fpp-fixed-endpoint-moment-threshold", "DRAFT: sharp Pareto passage-time moment threshold"),
         "w366-C3": ("bounded-planar-fpp-sharp-straight-path-window", "DRAFT: sharp bounded-weight straight-path window"),
         "w366-C4": ("planar-fpp-law-uniform-normalized-variance-bound-obstruction", "DRAFT: obstruction to a variance bound uniform over laws"),
         "w366-C5": ("bounded-planar-fpp-pre-detour-resampling-overlap", "DRAFT: exact geodesic overlap before the detour scale")}
for row in rows:
    logical, title = names[row["id"]]
    entries.append({"key": row["id"].lower(), "namespace": namespace,
                    "logical_name": logical, "kind": "concept", "title": title,
                    "statement": "DRAFT author proof awaiting independent mathematical review; no novelty or P0104 closure claim. " + row["statement"] + " Scope: " + row["remaining_gap"],
                    "proof_text": None, "assumptions": row["assumptions"],
                    "domain": "probability theory", "source": {**source, "url": source["url"]+"#"+row["id"].split("-")[-1].lower()}})
relations = [{"from_key": "w366-c1", "to_key": "fpp-definition", "kind": "depends_on", "rationale": "The moment criterion uses the explicitly defined point-to-point iid square-lattice passage time."},
             {"from_key": "w366-c2", "to_key": "w366-c1", "kind": "depends_on", "rationale": "C2 transfers the Pareto minimum-of-four moment threshold using exactly the equivalence in C1."},
             {"from_key": "w366-c3", "to_key": "fpp-definition", "kind": "depends_on", "rationale": "The straight-path window is a deterministic support specialization of this passage-time definition."},
             {"from_key": "w366-c4", "to_key": "w366-c3", "kind": "depends_on", "rationale": "Setting epsilon=1/n in C3 makes the normalized variance ratio n^(1-beta), disproving a law-uniform prefactor."},
             {"from_key": "w366-c5", "to_key": "w366-c3", "kind": "depends_on", "rationale": "Strict n epsilon<2 in C3 makes both environments' geodesics the same deterministic path."},
             {"from_key": "w366-c4", "to_existing_logical": "math:probability.core:open-problem-p0104-subdiffusive-and-kpz-passage-time-fluctuation-exponents", "kind": "semantic_association", "rationale": "The existing P0104 card seeks asymptotic fluctuation exponents under suitable fixed-law assumptions. This auxiliary obstruction concerns a stronger law-uniform estimate and does not refute that target."}]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w366", "bundle_slug": "p0104-sharp-moment-and-crossover-boundaries-w366-001", "entries": entries, "relations": relations}
assert len(entries) <= 200
keys = {e["key"] for e in entries}
for e in entries:
    assert e["kind"] in {"concept", "definition"} and e["proof_text"] is None
    assert e["source"]["license"].startswith("owner-own-work")
    assert re.fullmatch("[a-z0-9]+(?:-[a-z0-9]+)*", e["logical_name"])
    assert re.fullmatch("[a-z][a-z0-9]*(?:\.[a-z][a-z0-9]*)*", e["namespace"])
for r in relations:
    assert r["from_key"] in keys and ("to_existing_logical" in r or r["to_key"] in keys)
edges = [(r["from_key"], r["to_key"]) for r in relations if r["kind"] == "depends_on"]
def visit(key, ancestors):
    assert key not in ancestors, "dependency cycle"
    for left, right in edges:
        if left == key: visit(right, ancestors|{key})
for key in keys: visit(key, set())
(ROOT / "bundle_001.json").write_text(json.dumps(bundle, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")

hook = {"id": "probability-w366-01", "area": "math", "event": "stage-start",
        "cue": "A claimed FPP variance or geodesic-overlap power saving uses a prefactor and starting scale uniform over all bounded iid edge laws, or lets the law change while claiming a fixed-law exponent.",
        "fire_when": "Use epsilon=1/n in Uniform[1,1+epsilon] as a purported counterexample to the fixed-law chi=1/3 conjecture; or claim a law-uniform normalized variance/overlap power saving.",
        "silent_when": "Keep F fixed, state law-dependent constants and crossover scale, and prove a fixed-law asymptotic estimate beyond that scale.",
        "text": "Pin the edge law before taking n to infinity. For weights in [1,1+epsilon], n epsilon<=2 forces the straight-path sum; at n epsilon<2 its geodesic overlap stays n even after full refresh. Changing epsilon with n tests law-uniformity, not a fixed-law KPZ exponent.",
        "evidence": "~/brain_workers/w366/LEMMAS.md C3-C5; MEASUREMENTS.json: 3504 exact finite configurations, 0 losses in 2336 cases at or below the boundary; normalized ratios 2,4,8.", "proposer": "w366"}
assert len(hook["text"]) <= 300
hook_line = json.dumps(hook, ensure_ascii=False)+"\n"
(ROOT / "HOOK_PROPOSALS.jsonl").write_text(hook_line, encoding="utf-8")
patchdir = ROOT / "patches"
patchdir.mkdir(exist_ok=True)
for number, filename, target in [(1, "HOOK_PROPOSALS.jsonl", "~/primary_directive/hooks1000/proposals/probability-w366.jsonl"),
                                  (2, "bundle_001.json", "~/math-brain-inbox/w366/bundle_001.json")]:
    ls = (ROOT / filename).read_text(encoding="utf-8").splitlines()
    diff = f"--- a/{target}\n+++ b/{target}\n@@ -0,0 +1,{len(ls)} @@\n"+"".join("+"+l+"\n" for l in ls)
    (patchdir / f"{number:02d}_{'probability_hook' if number == 1 else 'draft_bundle'}.diff").write_text(diff, encoding="utf-8")
(ROOT / "BUNDLE_VALIDATION.json").write_text(json.dumps({"checked_utc": datetime.now(timezone.utc).isoformat(),
        "command": "python -X utf8 prepare_packet.py", "status": "PASS", "entries": len(entries), "relations": len(relations),
        "concept_results": len(rows), "independent_mathematical_review": False, "ingestion_performed": False,
        "note": "Local structural checks only, not the integrator or a proof audit."}, indent=2), encoding="utf-8")
print(json.dumps({"status": "PASS", "claim_rows": len(rows), "draft_entries": len(entries), "relations": len(relations),
                  "source_cards": len(cards), "local_bundle": str(ROOT / "bundle_001.json")}, indent=2))
