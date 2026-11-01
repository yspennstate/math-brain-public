"""Refresh receipts, validate drafts locally and finish the scoped worker round."""
import json
from datetime import datetime, timezone
from pathlib import Path
import build_review_packet  # Rebuild local packet from the final existing measurements, not new experiments.

root = Path(__file__).resolve().parent
stamp = datetime.now(timezone.utc).isoformat()
ext = json.loads((root / "EXTENSION_MEASUREMENTS.json").read_text(encoding="utf-8"))
assert ext["status"] == "PASS" and ext["noncanonical_phase_vertex_cases"] == 240
source_path = root / "SOURCE_STATUS.json"
source = json.loads(source_path.read_text(encoding="utf-8"))
source["lane_boundary"] = "Precommit and initial independent derivation preceded peer-proof reads. Later comparison shows L1-L3 overlap w505's canonical witness, so they are reproductions only. Reserved distinct extension: L4-L6 arbitrary bent base/vertex, sign-count invariance, exact local-sensitivity influence range and class extremizer, plus exact refutation of C=2 on the parity-twisted class. No further canonical truth-table runs after overlap discovery."
source["local_evidence"].append({"path": "NARROW_SOURCE_READS.json", "locator": "cited_store_cards[2]", "claim_id": "claim_d15d0160e58b4c9183707be9f49462d2", "status": "unverified",
    "digest": "Existing owner F4 card already states small-influence reduction, a 7.05 restriction-induction floor, and a different monotone per-coordinate obstruction. It is prior context only; no unverified theorem from it is a premise of L4-L6."})
source_path.write_text(json.dumps(source, indent=2) + "\n", encoding="utf-8")

hook = {"id": "p0162-parity-charge-w507-01", "area": "math", "event": "stage-start",
        "cue": "A proof transfers an entropy/influence bound under multiplication by a Walsh character using only unchanged spectral entropy.",
        "fire_when": "Transfer H<=2I from the untwisted bent splice to its full-parity twist; at m=4 I drops from 37/16 to 29/16 while H>2I.",
        "silent_when": "The proof transfers entropy only, uses the exact influence translation identity, or proves that every twisted coordinate has influence exactly 1/2.",
        "text": "Parity twists preserve Fourier entropy but change influence: I(chi_A f)=I(f)+|A|-2 sum_{i in A} I_i(f). For a bent point splice, twisting all four base bits lowers I from 37/16 to 29/16 and breaks a transferred constant-2 bound. Check the influence too.",
        "evidence": "~/brain_workers/w507/ATTEMPT.md L5-L7; EXTENSION_MEASUREMENTS.json 240 phase/vertex controls", "proposer": "w507"}
assert len(hook["text"]) <= 300
(root / "proposals" / "math-w507.jsonl").write_text(json.dumps(hook) + "\n", encoding="utf-8")

source_tag = {"source_id": "owner-work:w507:P0162:bent-splice-exact-range",
              "url": "urn:owner-work:w507:P0162:bent-splice-exact-range", "revision": "2026-10-10-draft-v1",
              "license": "owner-own-work; independent review pending", "excerpt": None}
extra = {"spec": "mathbrain-draft-v1", "author_agent": "w507", "bundle_slug": "p0162-bent-splice-exact-range-w507-002",
         "entries": [{"key": "bent-exact-range", "namespace": "probability.boolean_fourier",
             "logical_name": "bent-point-splice-exact-influence-and-class-extremizer-draft-w507", "kind": "concept",
             "title": "Draft exact influence range and extremizer for bent point splices",
             "statement": "DRAFT author-derived result, independent review pending. Fix even m>=4, N=2^m, and Boolean g on the uniform m-cube with |hat(g)(T)|=1/sqrt(N) for every T. For a vertex a set h=g-2g(a)1_{z=a}, F(z,+1)=g(z), F(z,-1)=h(z), and s_g(a)=#{j:g(a)!=g(a+e_j)}. Then I(F)=m/2+(m+1-2s_g(a))/N; each s=0,...,m is attainable by a character twist of the canonical quadratic bent base. Put R=sqrt(N), K_+=(N+R)/2, K_-=(N-R)/2 and phi(t)=t log_2(1/t), phi(0)=0. H(F)=E_m=K_+phi((R-1)^2/N^2)+K_-phi((R+1)^2/N^2)+Nphi(1/N^2), independent of g and a. At fixed m the sharp class maximum H/I is E_m/[m/2-(m-1)/N], attained by the full-parity twist flipped at zero. At m=4 this example has I=29/16 and H>469/128>2I, so a canonical constant-2 bound does not extend to all bent splices. Every such splice still satisfies H<=3I. These are class results; general FEI is not proved and novelty is not certified.",
             "proof_text": None, "assumptions": ["uniform input", "base-2 spectral entropy", "fixed even m>=4", "flat Boolean Walsh spectrum", "one flipped vertex on one selector branch"],
             "domain": "analysis of Boolean functions", "source": source_tag}],
         "relations": [{"from_key": "bent-exact-range", "to_existing_logical": "math:probability.core:open-problem-p0162-fourier-entropy-versus-total-influence", "kind": "semantic_association", "rationale": "An exact restricted-class entropy/influence calculation with an unproved global FEI gap; no solution or refutation of the parent target."}]}
(root / "DRAFT_BUNDLE_002.json").write_text(json.dumps(extra, indent=2) + "\n", encoding="utf-8")
destination = Path("~/math-brain-inbox/w507/bundle_002.json")
payload = json.dumps(extra, indent=2) + "\n"
if destination.exists():
    assert destination.read_text(encoding="utf-8") == payload
else:
    part = destination.with_name(destination.name + ".part")
    with part.open("x", encoding="utf-8") as stream:
        stream.write(payload)
    part.rename(destination)

bundle_paths = [Path("~/math-brain-inbox/w507/bundle_001.json"), destination]
allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
count_entries = count_relations = 0
for path in bundle_paths:
    bundle = json.loads(path.read_text(encoding="utf-8"))
    assert bundle["spec"] == "mathbrain-draft-v1" and bundle["author_agent"] == "w507"
    assert len(bundle["entries"]) <= 200
    keys = {entry["key"] for entry in bundle["entries"]}
    assert len(keys) == len(bundle["entries"])
    graph = {key: [] for key in keys}
    for entry in bundle["entries"]:
        assert set(("key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source")) <= entry.keys()
        assert entry["kind"] in {"concept", "definition"} and entry["proof_text"] is None
        assert entry["source"]["license"].startswith("owner-own-work")
        assert entry["statement"] and entry["logical_name"].lower() == entry["logical_name"]
    for relation in bundle["relations"]:
        assert relation["kind"] in allowed_relations and relation["from_key"] in keys
        if "to_key" in relation:
            assert relation["to_key"] in keys
            if relation["kind"] == "depends_on":
                graph[relation["from_key"]].append(relation["to_key"])
        else:
            assert relation["to_existing_logical"].startswith("math:")
    visited, active = set(), set()
    def visit(node):
        assert node not in active, "depends_on cycle"
        if node in visited:
            return
        active.add(node)
        for child in graph[node]:
            visit(child)
        active.remove(node)
        visited.add(node)
    for key in keys:
        visit(key)
    count_entries += len(bundle["entries"])
    count_relations += len(bundle["relations"])

claim_rows = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
allowed_status = {"conjecture", "numerical evidence", "sketch", "proved special case", "independently checked proof"}
for claim in claim_rows:
    assert claim["status"] in allowed_status
    for key in ("statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap"):
        assert key in claim
    if claim["id"] in ("w507.P0162.bent-min-split-obstruction", "w507.P0162.canonical-global-bound", "w507.P0162.restriction-ledger"):
        claim["lane_status"] = "Independent reproduction / established identity; overlaps canonical core-adversary w505 material; no novelty claim."
    if claim["id"] == "w507.P0162.bent-splice-influence-range":
        claim["statement"] = claim["statement"].replace("max H(F)/I(F) over this class", "at each fixed m, max H(F)/I(F) over this class")
    if claim["id"] == "w507.P0162.bent-splice-constant-two-fails":
        claim["statement"] = claim["statement"].replace(", although it is valid for the untwisted canonical subclass in the parallel w505 packet", "; no result from w505 is needed as a premise of this counterexample")
(root / "CLAIMS.jsonl").write_text("".join(json.dumps(row) + "\n" for row in claim_rows), encoding="utf-8")

validation = {"status": "PASS", "utc": stamp, "scope": "Local draft schema/labels/relation checks, not live integrator execution or a mathematical referee verdict",
              "bundles": [str(path) for path in bundle_paths], "entries": count_entries, "relations": count_relations,
              "claim_rows": len(claim_rows), "no_unreviewed_theorem_entries": True, "depends_on_acyclic": True,
              "submitted": True, "reviewed": False, "ingested": False, "retrievable": False}
(root / "PACKET_VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
(root / "BRAIN_SUBMISSION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")

with (root / "REVIEW_PACKET.md").open("a", encoding="utf-8") as stream:
    stream.write("\nFinal distinct scope: L4-L6. L1-L3 are an independent reproduction of the canonical witness also derived by w505. L5 derives exact I(F) from local sensitivity and class-max H/I at each fixed dimension; L6 gives an exact C=2 counterexample in the larger arbitrary-bent class. Reproduce only the distinct extension with python -X utf8 ~/brain_workers/w507/verify_extension.py. EXTENSION_MEASUREMENTS.json has 240 noncanonical phase/vertex checks and all local sensitivity values 0..4. Additional one-entry draft: math-brain-inbox/w507/bundle_002.json. PACKET_VALIDATION.json validates seven total entries and nine relations without executing the live integrator.\n")
measure = json.loads((root / "MEASUREMENTS.json").read_text(encoding="utf-8"))
delivery = json.loads((root / "PEER_DELIVERY.json").read_text(encoding="utf-8")) if (root / "PEER_DELIVERY.json").exists() else {"steps": []}
sent = any(step["step"] == "complete-packet-to-referee" and step["exit_code"] == 0 for step in delivery["steps"])
report = f"""The distinct P0162 result is an exact analysis of every bent-base single-point selector splice. Spectral entropy is fixed, while influence is m/2+(m+1-2s_g(a))/2^m. This gives the class extremizer at each fixed dimension. A five-bit parity twist has I=29/16 and H>469/128>2I: a constant-2 bound cannot transfer to the larger class merely because entropy stays fixed. All these splices satisfy H<=3I. The canonical witness overlaps w505 and is reproduction only. General FEI remains unproved; current openness is UNKNOWN and novelty is not claimed.

Reproduce: python -X utf8 verify_obstruction.py; python -X utf8 verify_extension.py. The final runs passed 278 Boolean functions, 1,100 restriction-ledger checks, 256 initial phase/vertex controls, and 240 extension-only cases. Run times were {measure['elapsed_seconds']:.3f} s and {ext['elapsed_seconds']:.3f} s; maximum ledger residual {measure['maximum_float_ledger_residual']:.3g}. On the 11-bit canonical control, the minimum-influence split ratio is 14.323620862 versus 3.978237963 for the best observed split. Exact logarithm comparisons prove the five-bit C=2 counterexample without relying on numerical entropy.

Apply: w509 independently audits ATTEMPT.md L4-L6; the validating coordinator integrates only kept material. Two inbox drafts contain seven concept/definition entries and nine relations. Submitted=true, reviewed=false, ingested=false, retrievable=false. Referee delivery sent={str(sent).lower()}; the mesh database is locked, with local handoffs and receipts in PEER_DELIVERY.json. Hook/progress proposals are staged locally under the folder-only write restriction. No live store or global recall controls changed.

NEXT: Audit the exact bent-splice range and parity-twist counterexample, then pursue a valid good-coordinate or aggregate entropy charge.
"""
(root / "REPORT.md").write_text(report, encoding="utf-8")

handoffs = {"adversary": {"to": "w508", "kind": "statement-first", "path": str(root / "SOURCE_STATUS.json"), "delivered": False},
            "referee": {"to": "w509", "kind": "complete-proof-packet", "path": str(root / "REVIEW_PACKET.md"), "delivered": sent},
            "reason": "Installed team communication tool could not open its locked database. Files are ready for the existing coordinator's retry; no delivery success is asserted."}
(root / "PEER_HANDOFFS.json").write_text(json.dumps(handoffs, indent=2) + "\n", encoding="utf-8")
progress = json.loads((root / "PROGRESS_READY.json").read_text(encoding="utf-8"))
progress["event"] = "P0162: exact arbitrary-bent splice influence range and parity-twist C=2 counterexample; 240 extension controls pass; 7 draft entries / 9 relations submitted; peer mesh locked, audit pending."
(root / "PROGRESS_READY.json").write_text(json.dumps(progress, indent=2) + "\n", encoding="utf-8")

(root / "STATUS.md").write_text("STATE: NEEDS_REVIEW\nNEXT: w509 independently check L4-L6 sign counts, exact influence range and parity-twist counterexample; return KEEP/FIX/DROP before coordinator integration.\n\n" + stamp + ": Completed P0162 independent extension. Canonical overlap with w505 identified and labeled reproduction. Proved author-side L4-L6 for arbitrary bent bases and flipped vertices; global good-coordinate/aggregate-charge gap remains open. Final verification: 278 Boolean functions, 1,100 ledger checks, 256 initial phase/vertex controls plus 240 extension-only cases; local draft validation passed. Seven draft entries / nine relations submitted in two files; review, ingestion and retrievability remain false. Named-peer packet sent=" + str(sent).lower() + ". Hook and progress event staged locally under folder-only write limits.\n", encoding="utf-8")
print(json.dumps({"state": "NEEDS_REVIEW", "entries": count_entries, "relations": count_relations,
                  "claims": len(claim_rows), "peer_packet_sent": sent, "extension_cases": 240}))
