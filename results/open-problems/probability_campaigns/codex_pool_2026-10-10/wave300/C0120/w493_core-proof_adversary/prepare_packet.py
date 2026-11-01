import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
now = datetime.datetime.now(datetime.timezone.utc).isoformat()

def write(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

scope = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
scope["primary_source"].update({"body_verified": True, "revision": "0810.4221v2, 2008-12-16",
    "exact_model": "Independent unit Gaussian weights on Z_+^2; n-vertex up/right paths from origin with free endpoint; M_n=max path sum, negative of ground-state energy.",
    "historical_question_quote": "Improve the fluctuation exponent in directed polymers.",
    "source_bound": "Var(M_n)<=C n/log n; Theorem 8.1",
    "scope_correction": "log Z_n and general-dimension variants require distinct primary sources."})
scope["precise_session_target"] = "Exist delta in (0,1), finite C, and n0 such that Var(M_n)<=C n^(1-delta) for all n>=n0 in the exact source model."
scope["paired_proof_read_after_independent_save"] = True
scope["independent_save_sha256_before_peer_read"] = "fb468e88e4a45cc46a3e69f81e7cdd7dd43061d9b73d806b716ee5c56874f2f1"
scope["served_identity"] = {"author": "UNVERIFIED", "referee": "UNVERIFIED",
    "reason": "No response-side served-model receipt available; requested settings and identifiers do not establish it."}
scope["primary_literature_checks"] = [
    {"url": "https://arxiv.org/abs/0909.1352", "scope": "Higher-dimensional last-passage sublinear variance; not a verified resolution of the precise power target."},
    {"url": "https://arxiv.org/abs/1204.1819", "scope": "Finite-temperature nearly-gamma concentration at square-root(n/log n) scale; different cited model."},
    {"url": "https://arxiv.org/abs/2509.21453", "scope": "Moment-matching intermediate-disorder universality; not fixed-model Gaussian ground-state power variance."},
    {"url": "https://arxiv.org/abs/2603.06574", "scope": "Continuous Gaussian polymers, spatial covariance, and high-temperature diffusion; distinct model."}]
scope["openness_limit"] = "Targeted owner prior-work and primary literature checks did not provide a solved/retired certificate; absence of a match is not proof of present openness."
scope["store_targets"] = [
    {"id": "claim_2b6b7c1da300a8ed1c28367cabd584f2c02769a03a64ed519cf081b1af04693d", "logical": "math:probability.gaussian:open-problem-c0120-fluctuation-exponent-of-directed-polymers-beyond-the-logarithmic-impro", "finding": "Unsupported log-Z/general-dimension scope in source card."},
    {"id": "claim_7891e285a213a1ead9b1e54b02b29177a06d86c6f3df76b6447ca94dbe6add7f", "logical": "math:probability.gaussian:attempt-c0120-fluctuation-exponent-of-directed-polymers-beyond-the-logarithmic-impro", "finding": "Attempt record inherits broader scope and ambiguous noise-size parameter."}]
scope["shared_source_correction"] = "~/brain_workers/w492/patches/01_c0120_source_scope.diff; w493 independent scoped KEEP; Claude/source-correction review pending."
scope["checked_at_utc"] = now
write("SOURCE_STATUS.json", scope)

source = {"source_id": "owner-own-work:w493:C0120:layer-mean-audit:2026-10-10",
    "url": "file:///~/brain_workers/w493/ATTEMPT.md",
    "revision": "independent-derivation-2026-10-10-before-paired-proof",
    "license": "owner-own-work", "excerpt": None}
assumptions = ["Independent N(0,1) vertex weights on Z_+^2",
    "n vertices including origin; each step right or up; endpoint unrestricted",
    "All identities refer to finite n; no claim of parent solution or novelty",
    "Author-derived special cases pending w494 independent check; stored as concept/DRAFT"]
entries = [
    {"key": "layer-mean-floor", "namespace": "probability.gaussian",
     "logical_name": "gaussian-quadrant-polymer-layer-mean-variance-floor",
     "kind": "concept", "title": "Gaussian polymer layer means: exact finite-n variance floor (draft)",
     "statement": "AUTHOR-DERIVED, UNREVIEWED finite-n identities. Let M_n=max_p sum_{v in p}g_v for n-vertex up/right paths from the origin in Z_+^2 with free endpoint and independent N(0,1) vertex weights. Define A_i as the mean of the i+1 weights on x+y=i, r_v=g_v-A_i on that layer, and H_n=sum_{j=1}^n 1/j. The layer means are Gaussian-independent of r, and M_n(g)=sum_{i=0}^{n-1}A_i+M_n(r), so Var(M_n)=H_n+Var(M_n(r)). For F_{n,beta}=log sum_p exp(beta sum_{v in p}g_v) at fixed beta>0, Var(F_{n,beta})=beta^2 H_n+Var(F_{n,beta}(r)). Under OU coupling g_t=e^(-t)g+sqrt(1-e^(-2t))g', maximizing-path overlap R_n(t) has floor sum_v P(v in P_n)^2>=H_n at every t>=0. These identities do not establish a power variance upper bound.",
     "proof_text": None, "assumptions": assumptions, "domain": "probability theory", "source": source},
    {"key": "n2-overlap-witness", "namespace": "probability.gaussian",
     "logical_name": "gaussian-quadrant-polymer-two-vertex-noise-overlap-witness",
     "kind": "concept", "title": "Two-vertex Gaussian polymer: full noise overlap stays positive (draft)",
     "statement": "AUTHOR-DERIVED, UNREVIEWED exact finite witness. In the independent standard-Gaussian quadrant polymer with two vertices per path, the two paths share the origin and choose either (1,0) or (0,1). M_2=g_0+max(g_1,g_2). With OU time t>=0 and g_t=e^(-t)g+sqrt(1-e^(-2t))g' for independent g', the expected number of shared maximizing-path vertices is R_2(t)=3/2+arcsin(e^(-t))/pi, and Var(M_2)=2-1/pi. Thus R_2(t)>=3/2 and its independent-environment limit is 3/2. A bound R_2(t)<=C exp(-c t) for all t with finite C and c>0 is false. Centered-overlap estimates must also account for the first-chaos variance floor. This is a proof-step counterexample, not a disproof of polynomial variance improvement.",
     "proof_text": None, "assumptions": assumptions + ["n=2", "Noise parameter is OU time, not noise amplitude"],
     "domain": "probability theory", "source": source}]
relations = [{"from_key": "n2-overlap-witness", "to_key": "layer-mean-floor", "kind": "specializes",
    "rationale": "At n=2 the general layer-mean and independent-environment floor is H_2=3/2; the witness computes the remaining centered variance and entire OU overlap explicitly."}]
write("bundle_001.json", {"spec": "mathbrain-draft-v1", "author_agent": "w493",
    "bundle_slug": "c0120-layer-mean-and-n2-obstructions-w493", "entries": entries, "relations": relations})
(ROOT / "RELATION_EVIDENCE.jsonl").write_text(json.dumps({"relation": relations[0],
    "from_statement": entries[1]["statement"], "to_statement": entries[0]["statement"],
    "evidence": "ATTEMPT.md exact n=2 and layer-mean derivations; MEASUREMENTS.json 116 checks; independent review pending",
    "status": "draft", "allowed_relation_type": True})+"\n", encoding="utf-8")

hook = {"id": "polymer-overlap-floor-w493-01", "area": "math", "event": "stage-start",
    "cue": "A proof claims full maximizing-path overlap for the origin-start Gaussian quadrant polymer tends to zero, or is bounded by C_n exp(-c_n t) for all OU times t.",
    "fire_when": "R_n(t)<=C_n exp(-c_n t) for all t>=0 in the exact Gaussian quadrant/free-endpoint model, without subtracting the first-chaos floor.",
    "silent_when": "The estimate is for R_n(t)-sum_v P(v in P_n)^2, or is explicitly restricted to a finite noise-time range; the variance floor is retained and the remaining bound is left unproved.",
    "text": "Keep the first-chaos floor before claiming full polymer overlap decays to zero. For the Gaussian origin-start quadrant model, R_n(t)>=sum_v P(v in P_n)^2>=H_n. The n=2 independent-environment overlap is 3/2. Centered overlap needs a separate floor bound.",
    "evidence": "w493/ATTEMPT.md exact n=2 derivation; MEASUREMENTS.json R_2(1)=1.619916090212428 versus false 2e^-1=0.7357588823428847; proof_steps_need_derived_joint_structure_2026_09_09",
    "proposer": "w493"}
assert len(hook["text"]) <= 300
(ROOT / "HOOK_PROPOSAL.jsonl").write_text(json.dumps(hook)+"\n", encoding="utf-8")
write("HOOK_CONTROLS.json", {"fire": "full R_n(t)<=C_n exp(-c_n t), all t: refuted by R_2(infinity)=3/2",
    "silent": "centered R_n(t)-B_n estimate with B_n separately bounded: no contradiction",
    "proposal_only": True, "live_hook_installed": False,
    "placement_policy": "Local proposal only; worker's write-only boundary does not authorize mutating the global hook directory."})

# Source-fidelity rows are not mathematical proofs, regardless of verified PDF metadata.
claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
for claim in claims:
    if claim["claim_id"] == "w493-C0120-002":
        claim["status"] = "sketch"
        claim["mathematical_proof_claim"] = False
(ROOT / "CLAIMS.jsonl").write_text("".join(json.dumps(c)+"\n" for c in claims), encoding="utf-8")
print(json.dumps({"claims": len(claims), "bundle_entries": len(entries), "relations": len(relations),
    "hooks_proposed_locally": 1, "submission": "not submitted", "parent_solved": False}))
