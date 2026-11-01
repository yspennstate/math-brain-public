"""Prepare scoped draft outputs and review receipts; never integrate into a store."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REVIEW = ROOT / "review_packet"
REVIEW.mkdir(exist_ok=True)

referee_path = Path("~/brain_workers/w398/REVIEW_w397.md")
referee_text = referee_path.read_text(encoding="utf-8")
assert "VERDICT: KEEP" in referee_text and "Reviewer: w398" in referee_text
(REVIEW / "REVIEW_w397_by_w398.md").write_text(referee_text, encoding="utf-8")
measurements = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
assert measurements["all_passed"] and measurements["cases"] == 96
source_receipts = json.loads((ROOT / "sources/source_receipts.json").read_text(encoding="utf-8"))

status = {
    "worker": "w397", "target_id": "P0003", "date": "2026-10-10",
    "historical_title": "Hexagonal self-avoiding-walk scaling limit",
    "historical_ranking": {"date": "2026-09-07", "tier": 5, "status": "attempted_un"},
    "current_openness": "UNKNOWN",
    "current_openness_reason": "The cited primary papers formulate conjectures. Bounded public arXiv searches did not verify a resolution as of the task date; absence of search results is not proof of openness.",
    "exact_historical_question": "Does a uniformly distributed n-step SAW from the origin of H converge weakly, when suitably rescaled, to the Schramm–Loewner random curve SLE8/3?",
    "target_source": {"author": "Geoffrey R. Grimmett", "title": "Selected problems in probability theory", "arxiv": "2205.07318v1", "url": "https://arxiv.org/abs/2205.07318v1", "locator": "Question 2.2; printed/PDF page 3", "H": "hexagonal lattice", "scope_gap": "Source leaves rescaling, SLE geometry/stopping rule and curve topology unspecified; no silent chordal replacement is permitted."},
    "related_chordal_subproblem": {"source": "Duminil-Copin--Smirnov, arXiv:1007.0575v2, Conjecture 1, page 9", "ensemble": "Variable-length walks between two prescribed boundary points weighted by x_c^length", "x_c": "1/sqrt(2+sqrt(2))", "remaining_gap": "Equivalence or transfer to the uniform fixed-length origin-started question has not been proved."},
    "primary_identity": {"source": "arXiv:1007.0575v2, Definition 1 and Lemma 1, page 2", "statement": "At x=x_c and sigma=5/8, sum_(p adjacent v)(p-v)F(p)=0", "verified_against_pdf": True},
    "hardest_missing_input": "H_5/8: asymptotic conformal covariance of the positive chordal SAW partition ratios. Local identities and finite martingale estimates do not provide it.",
    "other_unproved_inputs": ["Curve tightness and simplicity", "Avoidance-event/collar stability", "Uniform fixed-length ensemble bridge", "For the observable route: uniform regularity suppressing interior circulation modes"],
    "sources": source_receipts,
    "additional_primary_sources_read": [
        {"url": "https://arxiv.org/abs/math/0204277v2", "title": "On the scaling limit of planar self-avoiding walk", "read_scope": "Abstract and fixed-endpoint ensemble context; web read only"},
        {"url": "https://arxiv.org/abs/math/0209343", "title": "Conformal restriction: the chordal case", "read_scope": "Introduction and simple-curve restriction identification; web read only"}
    ],
    "prior_work_checks": [
        {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv", "result": "P0003 row checked; historical label only"},
        {"path": "Named probability_1000_intake_* folders, attempts_H_20260912, attempts_I_20260914 and prob1000_lean_20260908", "method": "Bounded text/file searches for exact ID P0003; no corpus export or model load", "result": "Historical ranking and related C0095/C0096 context located; no complete P0003 proof verified. This is not an exhaustive solved/retired audit."},
        {"path": "~/math-brain-build/export/population/nodes.jsonl", "locator": "claim_1f7a2a12ab2a649bf165699aa2efee71c08bca2100b4609c325b8f2d99b4f0dd", "result": "Canonical served P0003 row matches the Grimmett question, and labels current status unverified."},
        {"path": "~/brain_workers/teams/W0300_O/TEAM_BOARD.md", "result": "Related observable lane C0095 belongs to w334. This worker's finite circulation counterexample and independent collar audit do not duplicate its exact computations."}
    ],
    "brain_scars": ["perceptron_proof_open_gaps_fleet_2026_07_12", "proof_steps_need_derived_joint_structure_2026_09_09"],
    "independence": {"saved_before_paired_proof": "INDEPENDENT.md", "paired_statement_read_after_saving": True, "paired_full_proof_audit": "pending separate receipt", "independent_finite_lemma_referee": "w398", "review_artifact": "review_packet/REVIEW_w397_by_w398.md"},
    "formal_check_receipt": None,
    "landing_states": {"prepared": True, "submitted": False, "reviewed": False, "ingested": False, "retrievable": False}
}
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

rows = [
    {"id": "w397.P0003.001.review", "target": "P0003", "statement": "The homogeneous honeycomb vertex relation, fixed boundary values and a uniform bound do not imply uniqueness or local uniform compactness.", "assumptions": ["Embedded regular honeycomb", "Interior hexagonal face", "Only the stated vertex identity and boundary values are imposed"], "source": {"kind": "owner-own-work", "artifact": "INDEPENDENT.md", "primary_context": "Duminil-Copin--Smirnov Lemma 1 and Section 4"}, "proof_or_counterexample": "Explicit H(p_j)=delta/(v_(j+1)-v_j), zero elsewhere; the two vertex contributions are exactly -delta/2,+delta/2, norm and adjacent jump are 1.", "independent_reviewer": "w398", "review": {"verdict": "KEEP", "artifact": "review_packet/REVIEW_w397_by_w398.md", "scope": "Finite counterexample to an inference only"}, "remaining_gap": "No estimate for the genuine walk-sum observable and no SAW convergence proof.", "status": "independently checked proof", "claim_type": "counterexample_to_inference", "landing_state": "draft"},
    {"id": "w397.P0003.002", "target": "P0003", "statement": "For positive weighted simple a-to-b paths on a finite graph and A subset B avoiding the endpoints, D_k=P(avoid A | F_k)-P(avoid B | F_k) satisfies P(max_k D_k>=lambda)<=D_0/lambda for every lambda>0.", "assumptions": ["Finite graph", "Positive inherited edge weights", "Z_G(a,b)>0", "Stopped prefix filtration, with the completed path retained", "A subset B disjoint from a,b", "Quotients only on positive-probability prefixes"], "source": {"kind": "owner-own-work", "originator": "w396 statement packet", "independent_derivation": "ATTEMPT.md"}, "proof_or_counterexample": "D_k=E[1_avoidA-1_avoidB | F_k] is nonnegative and bounded. Stop at its first lambda crossing, clipped at |V|-1; bounded optional sampling gives the inequality. Three paths of weights1,1,2 attain equality at lambda=1/2.", "independent_reviewer": "w397 independently derived w396's candidate; integration referee w398 pending", "remaining_gap": "Full paired proof audit and referee receipt; initial collar decay and H_5/8 remain unproved.", "status": "proved special case", "claim_type": "finite_reduction", "landing_state": "draft"},
    {"id": "w397.P0003.003", "target": "P0003", "statement": "Uniform convergence of simple chordal curves does not alone imply convergence of avoidance probabilities for a fixed closed obstacle.", "assumptions": ["D=(-3,3)x(0,3), endpoints(-2,0),(2,0)", "A is the closed disk centered(0,1), radius1/4"], "source": {"kind": "owner-own-work", "artifact": "ATTEMPT.md"}, "proof_or_counterexample": "Three-segment paths at horizontal height5/4+1/n avoid A and converge uniformly to a path tangent to A at(0,5/4), which does not avoid A.", "independent_reviewer": "w398 requested through review packet; pending", "remaining_gap": "Independent check; for a SAW limit one needs boundary-event probability zero or a vanishing inner/outer collar squeeze.", "status": "proved special case", "claim_type": "counterexample_to_limit_inference", "landing_state": "draft"},
    {"id": "w397.P0003.004", "target": "P0003", "statement": "The P0003 historical source asks about uniform n-step origin-started walks; a critical variable-length chordal convergence result requires an additional ensemble bridge to answer that question.", "assumptions": ["Exact historical source is Grimmett Question2.2", "The related chordal formulation is DCS Conjecture1"], "source": {"kind": "primary_source_check", "url": "https://arxiv.org/abs/2205.07318v1", "locator": "Question2.2, page3", "quote": status["exact_historical_question"]}, "proof_or_counterexample": "Compare the source's origin, fixed length and uniform weighting with the paired packet's two boundary endpoints, variable length and x_c weights.", "independent_reviewer": "w398 pending", "remaining_gap": "No asymptotic bridge proved; the source's full SLE geometry/rescaling also needs specification.", "status": "sketch", "claim_type": "source_scope_correction", "landing_state": "draft"}
]
with (ROOT / "CLAIMS.jsonl").open("a", encoding="utf-8") as handle:
    for row in rows:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")

def entry(key, logical, kind, title, statement, proof, assumptions, revision="2026-10-10-draft"):
    return {"key": key, "namespace": "probability.saw", "logical_name": logical,
            "kind": kind, "title": title, "statement": statement, "proof_text": proof,
            "assumptions": assumptions, "domain": "probability theory and discrete complex analysis",
            "source": {"source_id": "owner-probability-w397-p0003-20261010:" + key,
                       "url": None, "revision": revision, "license": "owner-own-work",
                       "excerpt": "Campaign derivation and source-status record in w397/ATTEMPT.md; review states are separate."}}

entries = [
    entry("vertex-equation", "honeycomb-homogeneous-vertex-equation", "definition", "Honeycomb homogeneous vertex equation", "For a honeycomb graph embedded in the complex plane with edge midpoints p, the homogeneous vertex equation for a complex field F is sum_(p adjacent v)(p-v)F(p)=0 at every interior vertex v. This equation alone does not define F as a self-avoiding-walk observable.", None, ["Honeycomb embedded in the complex plane"]),
    entry("face-obstruction", "honeycomb-face-circulation-compactness-obstruction", "lemma", "Interior face circulation obstructs identity-alone compactness", "Finite lemma independently checked by w398; P0003 remains unresolved. On an interior regular hexagon of side delta with ordered vertices v_j and midpoints p_j, H(p_j)=delta/(v_(j+1)-v_j), zero on all other midpoints, satisfies the homogeneous vertex equation with zero boundary values. Its norm is1, successive values differ by1 at distance sqrt(3)*delta/2. Thus the local equation plus fixed boundary data and a uniform bound imply neither uniqueness nor local uniform compactness. This field need not be a genuine SAW observable.", "At v_j the preceding edge contributes(-delta/2) and the following edge(+delta/2); elsewhere all values vanish. Adjacent directions differ by60 degrees, so unit-modulus reciprocal directions differ by1. Shrinking faces in a fixed interior neighborhood violate equicontinuity. Adding cH to any solution preserves its boundary values. Reviewer w398 independently rederived these steps in REVIEW_w397.md; finite exact arithmetic checked96 configurations.", ["Interior regular hexagonal face", "Only the homogeneous vertex equation and fixed boundary data are imposed"], "2026-10-10-w398-checked-finite-only"),
    entry("invalid-inference", "honeycomb-local-identity-alone-compactness-inference-refuted", "concept", "Refuted inference: vertex identity alone supplies compactness", "REFUTED INFERENCE, not a SAW convergence theorem: claiming that the honeycomb homogeneous vertex identity, fixed boundary values and uniform boundedness force a unique locally uniform continuous limit is false. An interior face circulation has zero boundary, bounded amplitude and mesh-scale jumps. A valid observable proof must supply an additional estimate for the genuine walk sums.", None, ["Inference uses only local linear equations, boundary values and a magnitude bound"]),
    entry("collar-reduction", "finite-saw-collar-martingale-reduction-draft", "concept", "Draft finite collar control isolates the static SAW gap", "DRAFT reduction: in a finite positive weighted simple-path ensemble, for forbidden vertex sets A subset B, D_k=P(avoid A|F_k)-P(avoid B|F_k) is a bounded nonnegative martingale and P(max_k D_k>=lambda)<=D_0/lambda. Its conditional probabilities use completion partition functions on the slit graph deleting previous vertices. This transfers a small initial collar difference to exploration control; it proves no initial collar decay or conformal exponent5/8. Independent derivation by w397; integration referee pending.", None, ["Finite graph and positive inherited weights", "Positive total endpoint partition function", "Stopped prefix filtration and retained terminal indicators", "A subset B disjoint from endpoints", "lambda>0"]),
    entry("target-scope", "hexagonal-saw-fixed-length-chordal-ensemble-scope", "concept", "P0003 fixed-length and chordal ensemble scope", "SOURCE STATUS RECORD; current openness UNKNOWN. Grimmett, arXiv:2205.07318v1 Question2.2 page3, asks about a uniformly selected n-step hexagonal-lattice SAW from the origin after suitable rescaling. Duminil-Copin--Smirnov, arXiv:1007.0575v2 Conjecture1 page9, separately state critical variable-length boundary-to-boundary convergence to chordal SLE(8/3). A proof of the second formulation is a related subproblem and needs an additional fixed-length/geometry bridge to answer the first. Neither conjecture is proved by this packet.", None, ["Historical P0003 citation is Grimmett Question2.2", "No equivalence between the two ensembles is assumed"]),
    entry("avoidance-stability", "curve-avoidance-event-stability-required-draft", "concept", "Draft warning: weak curve limits need avoidance-event stability", "DRAFT finite counterexample; independent check pending. In D=(-3,3)x(0,3), paths from(-2,0) vertically to height5/4+1/n, horizontally to x=2 and vertically to(2,0) all avoid the closed disk centered(0,1) of radius1/4. They converge uniformly to a path tangent to that disk, which does not avoid it. Passing closed-obstacle avoidance probabilities through a weak curve limit therefore requires a zero-probability boundary-event condition or a proved vanishing inner/outer collar squeeze.", None, ["Fixed closed disk obstacle", "Corresponding three-segment parametrizations"])
]
relations = [
    {"from_key": "face-obstruction", "to_key": "vertex-equation", "kind": "depends_on", "rationale": "The finite face field is a homogeneous solution of exactly the vertex equation defined in the target entry."},
    {"from_key": "face-obstruction", "to_key": "invalid-inference", "kind": "refutes", "rationale": "The source entry constructs zero-boundary fields of norm1 and adjacent jumps1 at shrinking distances, contradicting the target entry's identity-alone uniqueness/compactness implication."},
    {"from_key": "collar-reduction", "to_key": "target-scope", "kind": "semantic_association", "rationale": "The finite collar reduction belongs to the positive chordal route, whose ensemble distinction and unproved bridge are recorded in the target scope entry."},
    {"from_key": "avoidance-stability", "to_key": "collar-reduction", "kind": "semantic_association", "rationale": "The collar reduction controls a given static difference; the avoidance example explains why limiting that initial difference needs an additional stability input."}
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w397",
          "bundle_slug": "p0003-circulation-and-collar-audit-20261010", "entries": entries, "relations": relations}
allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
keys = {e["key"] for e in entries}
assert len(keys) == len(entries) and len(entries) <= 200
for e in entries:
    assert e["source"]["license"].startswith("owner-own-work")
    assert (e["proof_text"] is None) == (e["kind"] in {"concept", "definition"})
for r in relations:
    assert r["kind"] in allowed and r["from_key"] in keys and r["to_key"] in keys
assert len([r for r in relations if r["kind"] == "depends_on"]) == 1
local_bundle = ROOT / "DRAFT_BUNDLE_001.json"
data = json.dumps(bundle, ensure_ascii=False, indent=2) + "\n"
local_bundle.write_text(data, encoding="utf-8")
# The later task brief explicitly names this worker's draft inbox as an output exception.
inbox = Path("~/math-brain-inbox/w397")
inbox.mkdir(exist_ok=True)
target = inbox / "bundle_001.json"
assert not target.exists(), "Do not overwrite an existing submitted bundle"
part = inbox / "bundle_001.part"
assert not part.exists(), "Do not overwrite another pending part file"
part.write_text(data, encoding="utf-8")
part.rename(target)
submission = {"prepared": True, "submitted": True, "reviewed": False,
              "reviewed_parts": {"w397.P0003.001": "w398 KEEP finite inference counterexample only"},
              "ingested": False, "retrievable": False,
              "path": str(target), "entries": len(entries), "relations": len(relations),
              "validation": "Local shape, allowed relation endpoints and license tags checked; live integrator not run because store writes are prohibited."}
(ROOT / "SUBMISSION_RECEIPT.json").write_text(json.dumps(submission, indent=2) + "\n", encoding="utf-8")
status["landing_states"].update({k: submission[k] for k in ["prepared", "submitted", "reviewed", "ingested", "retrievable"]})
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

hook = {"id": "p0003-circulation-w397-01", "area": "math", "event": "stage-start",
        "cue": "SAW/honeycomb proof derives observable uniqueness or locally uniform compactness from only the vertex identity, boundary values and a magnitude bound",
        "fire_when": "A proof declares a convergent holomorphic observable limit from those three conditions without an additional regularity estimate.",
        "silent_when": "The proof derives a quantitative regularity estimate for the genuine walk sums, or explicitly retains compactness as an open input; a finite conditional martingale bound alone is not the cue.",
        "text": "The honeycomb vertex identity admits zero-boundary face circulations of norm1 and mesh-scale jumps1. It cannot supply compactness alone. Name the extra regularity estimate for the true SAW observable; keep an unproved estimate as a gap.",
        "evidence": "w397/INDEPENDENT.md; MEASUREMENTS.json:96 cases,576 exact vertex equations,96 broken controls; w398 KEEP in review_packet/REVIEW_w397_by_w398.md",
        "proposer": "w397"}
assert len(hook["text"]) <= 300
hooks = ROOT / "hook_proposals"
hooks.mkdir(exist_ok=True)
line = json.dumps(hook, ensure_ascii=False) + "\n"
(hooks / "math-w397.jsonl").write_text(line, encoding="utf-8")
patches = ROOT / "patches"
patches.mkdir(exist_ok=True)
patch = "--- a/primary_directive/hooks1000/proposals/math-w397.jsonl\n+++ b/primary_directive/hooks1000/proposals/math-w397.jsonl\n@@ -0,0 +1 @@\n+" + line
(patches / "01_p0003_circulation_hook.diff").write_text(patch, encoding="utf-8")
(ROOT / "PROGRESS_EVENT.txt").write_text("w397 S1.P0003: w398-kept finite honeycomb circulation obstruction,96 exact configurations/576 identities;6-entry draft submitted, H_5/8 and fixed-length bridge remain open. Evidence:~/brain_workers/w397/ATTEMPT.md\n", encoding="utf-8")
(REVIEW / "PACKET.json").write_text(json.dumps({"worker": "w397", "referee": "w398", "supervisor": "claude-4a88bc43",
    "artifacts": ["ATTEMPT.md", "INDEPENDENT.md", "CLAIMS.jsonl", "SOURCE_STATUS.json", "MEASUREMENTS.json", "verify_circulation.py", "REVIEW_w396_statement.md", "DRAFT_BUNDLE_001.json", "SUBMISSION_RECEIPT.json", "patches/01_p0003_circulation_hook.diff"],
    "check_needed": ["Finite collar lemma/proof scope", "Tangent-obstacle example", "Exact source scope correction", "Remaining draft bundle entries and relations"],
    "accepted_scope": "The finite face-circulation obstruction has a w398 KEEP. No genuine SAW regularity estimate, full scaling-limit proof, novelty certification, ingestion or retrievability is claimed."}, indent=2) + "\n", encoding="utf-8")
print(json.dumps(submission, indent=2))
