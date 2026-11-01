"""Prepare review artifacts and a concept-only draft; never ingest a store."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
NOW = datetime.now(timezone.utc).isoformat()
def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

measure = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
peer_measure = json.loads((ROOT / "PEER_AUDIT_MEASUREMENTS.json").read_text(encoding="utf-8"))
assert measure["result"] == peer_measure["result"] == "PASS"
peer_path = Path("~/brain_workers/w450/ATTEMPT.md")
peer_text = peer_path.read_text(encoding="utf-8-sig")
assert "d_ell(p)>=0" in peer_text
(ROOT / "PEER_PROOF_READ.md").write_text(peer_text, encoding="utf-8")
scope_url = "https://raw.githubusercontent.com/openai/math/main/lean/docs/220.md"
paper_url = "https://github.com/openai/math/blob/main/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf"
comparator_url = "https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/DirectionalBallisticity.lean"
primary_url = "https://arxiv.org/pdf/1309.2589"
source = {
    "candidate_id": "C0041", "worker": "w451", "checked_at": NOW,
    "current_openness": "UNKNOWN", "novelty_claim": False,
    "exact_statement": "For every d>=2, every iid law of nearest-neighbor site kernels on Z^d with some deterministic kappa>0 bounding all transitions below, and every fixed real unit vector ell: if P0(X_n.ell -> +infinity)=1, is P0(liminf X_n.ell/n>0)=1? Under the directional law of large numbers this is equivalent to a deterministic positive limiting projection.",
    "primary_source": {"url": primary_url, "locator": "Open question 2.20, PDF page 24; Definitions 2.13-2.14, PDF page 20", "read": True, "transience_quantifier": "annealed probability one", "ballisticity_quantifier": "annealed almost sure positive liminf of the same directional projection"},
    "historical_ranking": {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv", "line": 540, "tier": 5, "status": "attempted_un"},
    "prior_attempt": {"id": "C0041-A001", "path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl", "line": 32, "retained_gap": "Finite regeneration duration almost surely does not give finite conditional expectation."},
    "bounded_owner_checks": {"attempts_H_I": "Targeted C0041 searches found no additional matching proof record", "lean_campaign": "Historical ranked-list nomination only", "team_O": "No C0041 row in the targeted board search", "population_export": "Dated unverified open-problem concept and prior attempt; no target resolution certificate read", "canonical_math_research_store": "No direct query performed; not certified exhaustive"},
    "recent_claim": {"claimed_date": "2026-09-23", "scope_url": scope_url, "paper_url": paper_url, "scope_matches_target": True, "pdf_downloaded": True, "pdf_bytes": (ROOT / "PUBLIC_C0041_PAPER.pdf").stat().st_size, "pdf_pages": 58, "read_scope": "Theorem 1.1, proof strategy, and targeted quantitative crossing reduction; not the entire 58-page proof", "critical_unchecked_step": "For some fixed 0<beta<1, the environment probability P(a_N<N^(-beta)), a_N=P_{0,omega}(T_N<T_{-1}), decays faster than every power of N. The paper's later two-copy and profile/entropy arguments for this estimate remain unaudited here.", "verdict": "CLAIM_FOUND_UNVERIFIED; do not infer current openness from the old ranking, or validity from a scope note"},
    "formal_receipt": {"checked_source": comparator_url, "theorem": "OAI.DirectionalTransience.directional_transience_implies_ballisticity", "statement": "MainStatement", "assumptions": ["d>=2", "nu is a probability row measure", "iid product site environment", "uniform ellipticity", "dot ell ell=1", "annealed almost-sure directional transience"], "source_lines": [81, 82, 83, 84, 86, 87], "body": "by sorry", "lean_build_run": False, "trusted_axioms_receipt": None, "accepted_as_proof": False, "scope_limit": "An admitted comparator is not a proof receipt; it does not refute a separate manuscript or formalization."},
    "recall": {"result": "TIMEOUT_60S", "fallback_slug": "perceptron_proof_open_gaps_fleet_2026_07_12", "rule_applied": "Verify the hardest mathematical piece rather than equating source hashes, statements, or a completed pipeline with proof."},
    "independent_derivation_saved_before_paired_read": True,
    "served_model_evidence": {"author": None, "referee": None, "note": "No response-side identity receipt available. Requested settings are not evidence."},
    "independent_reviewer": {"id": "w452", "request_delivered": True, "message_id": "msg-b4476721b0", "receipt_received": False},
}
write_json(ROOT / "SOURCE_STATUS.json", source)

audit_row = {"id": "w451-C0041-audit-w450", "kind": "proof_audit", "statement": "KEEP w450 L0-L3 as their stated restricted finite-domain/martingale lemmas and L4 as the signed occupation-drift counterexample. L2 needs nonnegative local directional drift; L3 is sharp only for relaxed exit vectors; none proves C0041.", "assumptions": ["Finite connected killed domain", "Site iid and UE for L1-L3", "Nonnegative local drift for L2", "No assumption of directional transience for L4"], "source": {"path": str(peer_path), "frozen_copy": str(ROOT / "PEER_PROOF_READ.md"), "quote": "d_ell(p)>=0 pi-a.s., with m=E_pi[d_ell(p)]>0"}, "proof_or_counterexample": "Independent Green visit decomposition and denominator inequalities in PEER_AUDIT.md; exact two-site I-Q inversion in PEER_AUDIT_MEASUREMENTS.json.", "independent_reviewer": "w451 auditing w450; response-side served identity unavailable", "remaining_gap": "Signed-drift C0041 regeneration integrability and the public manuscript's decisive crossing estimate have not been checked.", "status": "independently checked proof", "scope": "Restricted L0-L4 only; different-model promotion gate unverified"}
with (ROOT / "CLAIMS.jsonl").open("a", encoding="utf-8") as f:
    f.write(json.dumps(audit_row, ensure_ascii=False) + "\n")

draft_entries = []
def entry(key, logical, title, statement):
    draft_entries.append({"key": key, "namespace": "probability.randomenvironment", "logical_name": logical, "kind": "concept", "title": title, "statement": "DRAFT audit material; independent review pending. " + statement, "proof_text": None, "assumptions": ["Author derivation at w451/INDEPENDENT_BOUNDARY.md", "Not a proof or refutation of C0041", "Different-model promotion gate not verified"], "domain": "probability theory", "source": {"source_id": "owner-own-work:w451:C0041-boundary:" + key, "url": "file:///~/brain_workers/w451/INDEPENDENT_BOUNDARY.md", "revision": "campaign-2026-10-10-v1", "license": "owner-own-work", "excerpt": None}})
entry("homogeneous", "rwre-fixed-ellipticity-no-uniform-speed-bound", "Fixed ellipticity permits arbitrarily small positive speeds", "Fix d>=2, b=1/(2d), kappa=1/(4d), and 0<epsilon<=kappa. At every site take probabilities b+epsilon for +e1, b-epsilon for -e1 and b in every other direction. This deterministic product environment is site iid and UE with the fixed bound kappa. Its walk has velocity 2epsilon e1 and E T_1=1/(2epsilon), where T_1 is first arrival at projected height one. Thus a law-independent positive speed lower bound or finite crossing-mean upper bound depending only on d,kappa is impossible.")
entry("uniform-bridge", "rwre-law-independent-speed-bridge-is-false", "Invalid uniform speed bridge", "The auxiliary assertion that there exists c(d,kappa)>0 such that every directionally transient site-iid UE nearest-neighbor law on Z^d has directional speed at least c(d,kappa) is false. The homogeneous epsilon family at fixed kappa=1/(4d) has speed 2epsilon decreasing to zero. The qualitative C0041 implication for each individual law is a distinct assertion.")
entry("critical", "rwre-critical-two-point-infinite-crossing-mean", "Critical two-point crossing mean", "In dimension one let site right-jump probabilities be iid, equal to 3/4 with probability 3/4 and 1/4 otherwise. The walk is UE, transient to the right, and has zero speed. For rho=(1-p)/p, E log rho=-(log3)/2 and E rho=1. The first crossing expectation has lower bound E T_1>=2L+1 for every integer L>=1, hence is infinite. A geometric-excursion recursion yields the bound; a stationary ergodic argument with truncated, generally dependent crossing durations gives zero speed. Dimension one is outside C0041.")
entry("layered", "rwre-layered-zero-speed-counterexample-needs-site-iid", "Layered lift loses site independence", "For d>=2 let p_i be the critical iid sequence from the preceding construction and define omega(x,+e1)=p_x1/2, omega(x,-e1)=(1-p_x1)/2, and omega(x,+/-ej)=1/[4(d-1)] for j>=2. This nearest-neighbor environment is stationary and ergodic under the full translation group and UE with lower bound min(1/8,1/[4(d-1)]). The walk is directionally transient in e1 and has zero vector speed despite raw mean local e1 drift 1/8. It is not site iid: two different sites sharing x1 have favorable-type indicator covariance 3/16. An independent Bernoulli axial clock reduces the first coordinate to the one-dimensional example.")
entry("ergodic-bridge", "rwre-ergodic-transience-ballisticity-bridge-is-false", "Stationary ergodicity does not replace site iid", "The stronger auxiliary statement that UE and stationary ergodicity under the full translation group suffice to turn directional transience into positive speed in d>=2 is false. The critical layered law above is transient with zero speed. Shared layer variables violate site independence, so this is not a counterexample to C0041's iid-site statement.")
entry("gap", "rwre-directional-regeneration-integrability-audit-gap", "Directional regeneration integrability audit boundary", "A directional-transience proof must distinguish finite regeneration times almost surely from finite conditional mean duration E0[tau_1|D=infinity], where D is first backtracking below the starting height. The classical renewal formula gives positive directional speed when that mean is finite. C0041's precise site-iid UE d>=2 implication has a September-23-2026 public resolution claim, not independently validated in this packet; its decisive small-quenched-crossing-probability estimate is the next mathematical proof gate. Source status is UNKNOWN, not certified open.")
existing = "math:probability.randomenvironment:open-problem-c0041-transience-in-a-direction-implies-ballisticity-for-uniformly-elliptic"
relations = [
    {"from_key": "homogeneous", "to_key": "uniform-bridge", "kind": "refutes", "rationale": "The explicit product point-mass laws keep d,kappa fixed while their speed tends to zero."},
    {"from_key": "layered", "to_key": "critical", "kind": "depends_on", "rationale": "The axial coordinate at Bernoulli clock times is the critical one-dimensional walk."},
    {"from_key": "layered", "to_key": "ergodic-bridge", "kind": "refutes", "rationale": "The full-group ergodic UE construction escapes directionally with zero speed and has covariance 3/16 across same-layer sites."},
    {"from_key": "homogeneous", "to_existing_logical": existing, "kind": "semantic_association", "rationale": "The family satisfies the target's exact hypotheses and restricts any attempted quantitative speed constant."},
    {"from_key": "layered", "to_existing_logical": existing, "kind": "analogous_to", "rationale": "The target conclusion fails after site iid is replaced by full-group stationary ergodicity; the missing premise is explicit."},
    {"from_key": "gap", "to_existing_logical": existing, "kind": "semantic_association", "rationale": "The original target and the new public claim share the regeneration-duration proof gate."},
]
draft = {"spec": "mathbrain-draft-v1", "author_agent": "w451", "bundle_slug": "rwre-c0041-sharp-boundary-audit-20261010", "entries": draft_entries, "relations": relations}
keys = {e["key"] for e in draft_entries}
assert len(keys) == len(draft_entries) <= 200
for e in draft_entries:
    assert e["kind"] == "concept" and e["proof_text"] is None
    assert e["source"]["license"].startswith("owner-own-work")
for edge in relations:
    assert edge["from_key"] in keys
    assert edge["kind"] in {"depends_on", "refutes", "semantic_association", "analogous_to"}
    assert edge.get("to_key", "critical") in keys
assert [(r["from_key"], r["to_key"]) for r in relations if r["kind"] == "depends_on"] == [("layered", "critical")]
write_json(ROOT / "DRAFT_BUNDLE.json", draft)
inbox = Path("~/math-brain-inbox/w451")
inbox.mkdir(parents=True, exist_ok=True)
number = next(i for i in range(1, 1000) if not (inbox / f"bundle_{i:03d}.json").exists() and not (inbox / f"bundle_{i:03d}.part").exists())
part = inbox / f"bundle_{number:03d}.part"
destination = inbox / f"bundle_{number:03d}.json"
write_json(part, draft)
part.replace(destination)

hook = {"id": "rwre-boundary-w451-01", "area": "math", "event": "stage-start", "cue": r"(?is)\b(C0041|directional transience)\b.*\b(proof|proving|ballistic|regeneration|layered)\b", "fire_when": "C0041 proof infers integrable regeneration from almost-sure escape or treats layered variables as iid sites", "silent_when": "Homogeneous biased walk with an explicit law-dependent finite crossing mean", "text": "For RWRE, preserve d>=2 and iid across sites. Finite regeneration almost surely does not give finite mean. A layered lift shares site variables; fixed ellipticity alone gives no uniform positive speed. Name the extra premise or quantitative tail estimate.", "evidence": "~/brain_workers/w451/MEASUREMENTS.json: 504 exact finite environments, critical lower bound 2L+1, same-layer covariance 3/16; perceptron_proof_open_gaps_fleet_2026_07_12", "proposer": "w451"}
assert len(hook["text"]) <= 300
assert re.search(hook["cue"], hook["fire_when"])
assert not re.search(hook["cue"], hook["silent_when"])
line = json.dumps(hook, ensure_ascii=False)
(ROOT / "HOOK_PROPOSAL.jsonl").write_text(line + "\n", encoding="utf-8")
(ROOT / "patches").mkdir(exist_ok=True)
live_path = "~/primary_directive/hooks1000/proposals/math-C0041-w451.jsonl"
(ROOT / "patches/01_regeneration_boundary_hook.diff").write_text(f"--- a/{live_path}\n+++ b/{live_path}\n@@ -0,0 +1 @@\n+{line}\n", encoding="utf-8")
write_json(ROOT / "DRAFT_VALIDATION.json", {"result": "PASS", "entries": len(draft_entries), "relations": len(relations), "concepts_only": True, "owner_source_tag": True, "internal_endpoints_checked": True, "depends_on_acyclic": True, "cross_bundle_target": existing, "cross_bundle_resolved_by_integrator": False, "hook_fire": True, "hook_silent": True, "not_store_validation": True})
states = {"prepared": {"at": NOW, "value": True}, "submitted": {"at": NOW, "value": True, "path": str(destination)}, "reviewed": {"value": False, "required": "w452 independent mathematics and different-model evidence"}, "ingested": {"value": False}, "retrievable": {"value": False}, "hook_submitted": False, "hook_reviewable_patch": str(ROOT / "patches/01_regeneration_boundary_hook.diff")}
write_json(ROOT / "BRAIN_STATES.json", states)

report = f"""Prepared an independent C0041 boundary packet before reading w450's proof. The fixed-ellipticity homogeneous family rules out law-independent speed constants; the critical layered example identifies site independence as the exact missing hypothesis. These do not solve or refute C0041. The new public manuscript claims a full resolution; current openness remains UNKNOWN because its decisive crossing estimate is not independently audited here.

The independent audit keeps w450 L0-L3 within their stated scope and L4 as a signed occupation-drift counterexample. L2's nonnegative local drift is stronger than the target assumptions; a ballisticity corollary still needs the Kalikow implication.

Measured by `python -X utf8 ~/brain_workers/w451/verify_boundary.py`: 504 finite environments, 24 matrix/formula comparisons, PASS in {measure['elapsed_seconds']:.3f} seconds. Critical lower crossing bounds grow from 13 at L=6 to 201 at L=100. Same-layer covariance is 3/16; raw mean layered drift is 1/8. By `python -X utf8 ~/brain_workers/w451/audit_exact_bridge.py`: raw mean drift 1/125 but finite-domain Kalikow drift {peer_measure['Kalikow_drift']} ({peer_measure['Kalikow_drift_decimal']:.8f}), PASS. Finite exact diagnostics do not certify the probabilistic proof.

Brain handoff: {destination.as_posix()}, six concept/draft entries and six scoped relations, all with owner-own-work source tags. DRAFT_VALIDATION.json checks shape, endpoints and acyclicity. BRAIN_STATES.json separates submitted, reviewed, ingested and retrievable. Independent mathematical and served-model review receipts remain pending; no theorem promotion or measured recall gain is claimed.

Apply: the validating coordinator reviews this packet and ingests the concept draft after the required gates; append HOOK_PROPOSAL.jsonl to the destination named in patches/01_regeneration_boundary_hook.diff only after hook auditors KEEP it. The hook is a local reviewable patch because this worker's write boundary excludes live hook files.

Risk: a layer-iid law must not be recalled as site iid; the first crossing lower bound must not be promoted to a parent-target counterexample; an admitted Lean comparator is not a formal certificate. New public proof status must stay separate from this packet's restricted audit.

NEXT: w452 checks B1-B3, and the integrator retains the exact restricted scope and validates the public manuscript's small-crossing-probability estimate before any solved-status update.
"""
(ROOT / "REPORT.md").write_text(report, encoding="utf-8")
(ROOT / "ATTEMPT.md").write_text("C0041 / w451 adversarial packet, 2026-10-10\n\nIndependent proof: INDEPENDENT_BOUNDARY.md, saved before paired-proof reading. B1 is an in-class quantitative bridge counterexample. B2 is the critical one-dimensional infinite-mean boundary. B3 is its d>=2 layered lift and explicit failure of site iid.\n\nPaired-proof audit: PEER_AUDIT.md independently checks w450's Green/occupation route, retaining nonnegative local drift and finite-domain scope. PEER_AUDIT_MEASUREMENTS.json records the exact signed-drift obstruction.\n\nSource status: SOURCE_STATUS.json. The historical conjecture is recovered exactly, but a September-23-2026 public manuscript claims resolution. Its quantitative crossing estimate, not source availability or the comparator's admitted theorem, is the hardest unchecked target step.\n\nProof statuses and assumptions: CLAIMS.jsonl. Exact finite diagnostics: MEASUREMENTS.json. These are not formal theorem certificates.\n\nNEXT: w452 independently checks B1-B3; the public paper's decisive crossing estimate needs a separate mathematical audit.\n", encoding="utf-8")
artifacts = ["INDEPENDENT_BOUNDARY.md", "PEER_AUDIT.md", "PEER_PROOF_READ.md", "CLAIMS.jsonl", "SOURCE_STATUS.json", "MEASUREMENTS.json", "PEER_AUDIT_MEASUREMENTS.json", "REPORT.md"]
packet = {"worker": "w451", "candidate": "C0041", "created_at": NOW, "referee": "w452", "integration_contact": "codex-01a12190", "scope": "Three independent boundary results plus first restricted audit of w450 L0-L4", "verdict": "REVIEW_READY; no parent solved verdict", "artifacts": [{"path": (ROOT / name).as_posix(), "sha256": hashlib.sha256((ROOT / name).read_bytes()).hexdigest()} for name in artifacts], "hash_receipt_is_mathematical_proof": False, "draft_path": destination.as_posix(), "draft_entry_count": len(draft_entries), "claims_count": sum(1 for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()), "served_model_evidence": source["served_model_evidence"], "independent_referee_received": False, "remaining_gap": source["recent_claim"]["critical_unchecked_step"], "next": "w452 checks B1-B3; integrator preserves concept-only draft status until the independent proof and model gates pass."}
write_json(ROOT / "REVIEW_PACKET.json", packet)
print(json.dumps({"result": "REVIEW_READY", "draft": destination.as_posix(), "entries": len(draft_entries), "claims": packet["claims_count"], "hook_controls": "PASS"}))
