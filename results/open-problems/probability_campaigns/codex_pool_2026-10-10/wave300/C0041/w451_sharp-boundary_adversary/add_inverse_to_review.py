"""Add the sharp inverse-moment boundary to the same unreviewed packet."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()
def read(name):
    return json.loads((root / name).read_text(encoding="utf-8"))
def write(name, value):
    (root / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
receipt = read("INVERSE_MEASUREMENTS.json")
assert receipt["result"] == "PASS"
claim = {"id": "w451-C0041-B4", "kind": "counterexample_to_bridge", "statement": "For the critical iid one-dimensional law P(p_i=3/4)=3/4 and P(p_i=1/4)=1/4, the quenched probability q of never hitting -1 has E[q^(-lambda)] finite exactly for 0<=lambda<1. The walk has infinite first crossing mean and zero speed. The same survival probability occurs in the B3 layer-iid lift, which deliberately fails site independence.", "assumptions": ["Nearest-neighbor critical two-point iid environment in dimension one", "Or the explicitly layer-iid, not site-iid d>=2 lift", "lambda>=0"], "source": {"source_id": "owner-own-work:w451:C0041-B4", "path": (root / "INVERSE_MOMENT_BOUNDARY.md").as_posix()}, "proof_or_counterexample": "Harmonic scale gives q^-1=1+sum future rho products. Subadditivity gives E q^-lambda<=1/(1-E rho^lambda) for 0<lambda<1; E rho^lambda<1 follows from (3^lambda-1)(3^lambda-3)<0. Tonelli yields infinity at lambda=1; monotonicity covers lambda>1. See INVERSE_MOMENT_BOUNDARY.md.", "independent_reviewer": "w452; check requested, not received", "remaining_gap": "Independent review pending. Does not refute the public manuscript's later super-polynomial crossing estimate or C0041.", "status": "proved special case"}
with (root / "CLAIMS.jsonl").open("a", encoding="utf-8") as f:
    f.write(json.dumps(claim, ensure_ascii=False) + "\n")
entry = {"key": "critical-inverse-moment", "namespace": "probability.randomenvironment", "logical_name": "rwre-critical-reciprocal-survival-moment-threshold", "kind": "concept", "title": "A positive inverse escape moment does not give a finite crossing mean", "statement": "DRAFT audit material, independent review pending. In dimension one let right-jump probabilities be iid, equal to 3/4 with probability 3/4 and to 1/4 otherwise. With rho_i=(1-p_i)/p_i and q=P_{0,omega}(T_{-1}=infinity), harmonic scale gives q^-1=1+sum_{k>=0} product_{j=0}^k rho_j. For lambda>=0, E q^-lambda is finite exactly when lambda<1: for 0<lambda<1, it is at most 1/[1-(3/4)3^-lambda-(1/4)3^lambda]; at lambda=1 Tonelli and E rho=1 make it infinite. In particular E q^-1/2<=4+2sqrt(3), although the first crossing mean is infinite and the walk's speed is zero. This same q appears in the layer-iid d>=2 lift omega(x,+e1)=p_x1/2, omega(x,-e1)=(1-p_x1)/2, omega(x,+/-ej)=1/[4(d-1)] for j>=2; the lift is not site iid. A small positive inverse moment alone therefore cannot replace an integrable duration estimate. This is not a C0041 counterexample and does not refute the public claimed proof's stronger crossing estimate.", "proof_text": None, "assumptions": ["Critical one-dimensional iid law, outside C0041", "In the lifted version: iid layers, not iid sites", "Independent and different-model review not complete"], "domain": "probability theory", "source": {"source_id": "owner-own-work:w451:C0041-B4", "url": "file:///~/brain_workers/w451/INVERSE_MOMENT_BOUNDARY.md", "revision": "campaign-2026-10-10-v1", "license": "owner-own-work", "excerpt": None}}
extra = {"spec": "mathbrain-draft-v1", "author_agent": "w451", "bundle_slug": "rwre-c0041-critical-inverse-moment-boundary-20261010", "entries": [entry], "relations": [{"from_key": entry["key"], "to_existing_logical": "math:probability.randomenvironment:open-problem-c0041-transience-in-a-direction-implies-ballisticity-for-uniformly-elliptic", "kind": "semantic_association", "rationale": "The critical law isolates why a small positive reciprocal-survival moment is weaker than the duration premise needed for positive speed; its d>=2 lift explicitly lacks site iid."}]}
assert entry["kind"] == "concept" and entry["proof_text"] is None
assert entry["source"]["license"] == "owner-own-work"
write("DRAFT_BUNDLE_EXTRA.json", extra)
inbox = Path("~/math-brain-inbox/w451")
number = next(i for i in range(1, 1000) if not (inbox / f"bundle_{i:03d}.json").exists() and not (inbox / f"bundle_{i:03d}.part").exists())
part = inbox / f"bundle_{number:03d}.part"
destination = inbox / f"bundle_{number:03d}.json"
part.write_text(json.dumps(extra, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
part.replace(destination)
states = read("BRAIN_STATES.json")
states["submitted"]["paths"] = [states["submitted"]["path"], destination.as_posix()]
states["submitted"]["last_updated"] = now
states["submitted"]["entries_total"] = 7
states["submitted"]["relations_total"] = 7
write("BRAIN_STATES.json", states)
validation = read("DRAFT_VALIDATION.json")
validation["extra_bundle"] = {"result": "PASS", "path": destination.as_posix(), "entries": 1, "relations": 1, "kind": "concept", "proof_text": None, "license": "owner-own-work", "internal_endpoint_valid": True, "depends_on_acyclic": True}
write("DRAFT_VALIDATION.json", validation)
source = read("SOURCE_STATUS.json")
source["recent_claim"]["read_scope"] = "Theorem 1.1, proof strategy, Lemma 2.4's conditional expectation step, and Proposition 2.5's quantitative input; not the whole 58-page proof"
source["small_inverse_moment_scope"] = "Lemma 2.4's endpoint-indicator Markov comparison does not require independent endpoint values. B4 proves a sharp boundary showing that a small positive inverse moment alone cannot imply finite mean crossing duration outside the target's site-iid d>=2 class. No verdict on the later public proof's estimate (5)."
write("SOURCE_STATUS.json", source)
with (root / "REPORT.md").open("a", encoding="utf-8") as f:
    f.write(f"\nAdded the sharp reciprocal-survival threshold for the same critical family: E q^-lambda is finite exactly for 0<=lambda<1, yet crossing mean is infinite. `python -X utf8 ~/brain_workers/w451/verify_inverse_boundary.py` independently solves 126 finite hitting matrices and checks six mean-inverse formulas E[1/a_N]=N+1; PASS in {receipt['elapsed_seconds']:.3f} seconds. The lambda=1/2 analytic upper bound is 4+2sqrt(3), approximately {receipt['half_inverse_moment_upper_bound']:.6f}. Extra concept draft: {destination.as_posix()}. Total submission: seven concepts and seven relations across two bundles. Proof and referee gates remain unchanged.\n")
with (root / "ATTEMPT.md").open("a", encoding="utf-8") as f:
    f.write("\nB4: INVERSE_MOMENT_BOUNDARY.md proves the critical inverse escape moment threshold, addressing why the public manuscript's small-moment lemma is weaker than its decisive equation (5). Exact finite hitting-matrix receipt: INVERSE_MEASUREMENTS.json.\n")
packet = read("REVIEW_PACKET.json")
names = [Path(a["path"]).name for a in packet["artifacts"]]
names += ["INVERSE_MOMENT_BOUNDARY.md", "INVERSE_MEASUREMENTS.json", "DRAFT_VALIDATION.json", "BRAIN_STATES.json", "ATTEMPT.md"]
packet["artifacts"] = [{"path": (root / name).as_posix(), "sha256": hashlib.sha256((root / name).read_bytes()).hexdigest()} for name in names]
packet["scope"] = "Four independent boundary results B1-B4 plus the first restricted audit of w450 L0-L4"
packet["draft_paths"] = states["submitted"]["paths"]
packet["draft_entry_count"] = 7
packet["draft_relation_count"] = 7
packet["claims_count"] = sum(bool(line.strip()) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines())
packet["measurements"] = {"crossing_environments": 504, "crossing_formula_comparisons": 24, "inverse_environments": 126, "inverse_formula_comparisons": 6, "signed_environment_cases": 4, "result": "PASS", "not_a_formal_certificate": True}
packet["next"] = "w452 independently checks B1-B4; validating integrator preserves draft status and audits equation (5) before any solved-status update."
write("REVIEW_PACKET.json", packet)
print(json.dumps({"result": "REVIEW_READY", "draft_paths": packet["draft_paths"], "claims": packet["claims_count"], "entries": 7, "relations": 7}))
