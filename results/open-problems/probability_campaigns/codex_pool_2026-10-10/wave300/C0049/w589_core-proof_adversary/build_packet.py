"""Freeze scoped evidence and prepare a draft packet; never mutate a live store."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone, timedelta
import hashlib
import json
import time
import urllib.request

BASE = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w589")

def save(name, data):
    p = BASE / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def append_claim(row):
    p = BASE / "CLAIMS.jsonl"
    ids = {json.loads(line)["id"] for line in p.read_text(encoding="utf-8").splitlines() if line.strip()}
    if row["id"] not in ids:
        with p.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

# Snapshot the exact peer bytes reviewed; a later peer edit requires a fresh verdict.
peer_path = Path("~/brain_workers/w588/ATTEMPT.md")
peer_bytes = peer_path.read_bytes()
peer_sha = sha(peer_bytes)
snap = BASE / "review_snapshot" / "w588_ATTEMPT.md"
snap.parent.mkdir(exist_ok=True)
snap.write_bytes(peer_bytes)
save("REVIEW_SNAPSHOT.json", {"live_path": str(peer_path), "snapshot": str(snap), "sha256": peer_sha,
     "scope": "L1, L2, L3 as present in frozen bytes; full target not proved", "frozen_at_utc": datetime.now(timezone.utc).isoformat()})

# Primary-source bytes, not an integrator digest/manifest ceremony.
cached = Path("~/Downloads/Probability_1000_intake_claude_20260907/sources/duminil_copin_ising_potts_2017/source.pdf")
primary = [{"source_id": "arxiv:1707.00520", "path": str(cached), "sha256": sha(cached.read_bytes()),
            "locator": "Conjectures 3-4, printed pp.93-94", "statement_checked": True, "proof_checked": False}]
q4_url = "https://arxiv.org/pdf/2610.08507v1"
q4_path = BASE / "sources" / "arxiv_2610.08507v1.pdf"
q4_path.parent.mkdir(exist_ok=True)
try:
    if not q4_path.exists():
        with urllib.request.urlopen(q4_url, timeout=20) as response:
            q4_bytes = response.read(3_000_001)
        if not q4_bytes.startswith(b"%PDF") or len(q4_bytes) > 3_000_000:
            raise ValueError("unexpected PDF signature or size")
        q4_path.write_bytes(q4_bytes)
    primary.append({"source_id": "arxiv:2610.08507v1", "url": q4_url, "path": str(q4_path),
                    "sha256": sha(q4_path.read_bytes()), "locator": "Theorem 1.2",
                    "statement_checked": True, "proof_checked": False,
                    "scope": "q=4 p=2/3 free-boundary macroscopic loops -> nested CLE(4), not a stated Dobrushin chordal theorem"})
except Exception as error:
    primary.append({"source_id": "arxiv:2610.08507v1", "url": q4_url, "path": None, "sha256": None,
                    "download_error": type(error).__name__ + ": " + str(error),
                    "statement_checked_in_primary_html": True, "proof_checked": False})
save("SOURCE_HASHES.json", primary)

# A fresh, bounded gate for exact scalar sanity checks, no simulations or model/GPU work.
start = datetime.now(timezone.utc)
gate = {"worker": "w589", "scope": "exact scalar coefficient and explicit counterexample sanity checks",
        "permitted": True, "authorization": "assigned C0049 proof/adversary task",
        "activated_at_utc": start.isoformat(), "expires_at_utc": (start+timedelta(seconds=20)).isoformat(),
        "max_wall_seconds": 20, "max_memory_mib": 16, "max_cases": 64,
        "network": False, "gpu": False, "children": False, "model_calls": False, "writes": str(BASE)}
save("COMPUTE_GATE.json", gate)
timer = time.perf_counter()
checks = 0
for sigma in [Q(1,10), Q(1,3), Q(1,2), Q(2,3), Q(1), Q(3,2)]:
    for w in [Q(-2), Q(0), Q(3)]:
        for t in [Q(0), Q(1,2)]:
            # Multiply separate binomial expansions of (g')^sigma and (Z/z)^(-sigma).
            numerator_second = -2*sigma*t
            denominator_second = -2*sigma*t + sigma*(sigma+1)*w*w/2
            combined = numerator_second + denominator_second
            assert combined == sigma*(sigma+1)*w*w/2 - 4*sigma*t
            checks += 1
for x in [-3,-2,-1,1,2,3]:
    for eps in [Q(1,2), Q(2)]:
        assert 1+eps/Q(x*x) > 0
        checks += 1
for residual in [1+1j*1j, 1j*(-1j)-1, -(-1)-1j*(-1j), -1-1j*1j]:
    assert residual == 0
    checks += 1
for sigma, expected in [(Q(1,3), Q(6)), (Q(1,2), Q(16,3)), (Q(1), Q(4))]:
    assert 8/(1+sigma) == expected
    checks += 1
elapsed = time.perf_counter()-timer
assert checks <= gate["max_cases"] and elapsed < gate["max_wall_seconds"]
save("EXACT_CHECKS.json", {"command": "python -X utf8 ~/brain_workers/w589/build_packet.py",
     "passed": checks, "failed": 0, "elapsed_seconds": elapsed,
     "scope": "36 coefficient constants, 12 positive boundary factors, 4 plaquette residuals, 3 kappa special values",
     "limitations": "Sanity checks are not an independent mathematical proof, FK experiment, or recall-quality measurement."})

verdicts = []
for lemma, why, limit in [
    ("L1", "KEEP: deterministic localization bounds the local martingales; both coefficient limits have uniform deterministic remainders; the second coefficient is sigma(sigma+1)U^2/2-4sigma*theta. W is made a local martingale before invoking bracket or Levy. Independently supported by w589's inverse-observable derivation.", "Conditional identification only; G and FK compactness are inputs."),
    ("L2", "KEEP: all four interior residuals vanish exactly; the explicitly defined bilinear average remains nonzero at a fixed point but vanishes off a shrinking neighborhood. No locally uniform continuous limit exists.", "Abstract weak-equation field, not an FK observable or a refutation of FK convergence."),
    ("L3", "KEEP: joint convergence and fixed-time uniform integrability permit bounded cylinder tests; continuity gives the natural-filtration monotone class and right-continuous augmentation. Common stopped-history convergence is explicit.", "The actual FK stopped integrability and joint convergence are not proved.")]:
    verdicts.append({"claim_id": "w588-C0049-"+lemma, "verdict": "KEEP", "scope": limit, "why": why,
                     "source_path": str(peer_path), "snapshot_path": str(snap), "source_sha256": peer_sha,
                     "auditor": "w589", "served_model_evidence": None,
                     "promotion_gate": "No different-model/account certification; referee w590 and served-identity gates remain separate."})
(BASE/"AUDIT_w588.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False)+"\n" for x in verdicts), encoding="utf-8")

status = json.loads((BASE/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
status.update({"checked_at": "2026-10-10", "current_openness": "UNKNOWN",
  "exact_primary_statement": "Critical square-lattice FK Dobrushin explorations in approximating simply connected domains converge weakly to chordal SLE(kappa), kappa=4*pi/(pi-arccos(sqrt(q)/2)); q in (0,4], q!=2 for this lane. Boundary approximation and critical tuning must be specified; q<1 self-dual criticality is not imported.",
  "primary": primary, "prior_owner_work_checked": "Scoped targeted searches completed; exhaustive retirement clearance unavailable.",
  "paired_prover_opened": True, "independent_checkpoint_before_prover_read": ["ATTEMPT.md", "CONDITIONAL_IDENTIFICATION.md", "MARTINGALE_LIMIT_OBSTRUCTION.md"],
  "q4_update": "October 6 preprint Theorem 1.2 asserts free-boundary CLE(4) loop convergence. No automatic Dobrushin retirement.",
  "hardest_gap": "Renormalized FK vertex-observable convergence in random slit domains, with localization, joint stopped-history convergence, and uniform integrability."})
save("SOURCE_STATUS.json", status)

append_claim({"id": "w589.C0049.004", "statement": "The historical C0049 attempt does not establish that an additional discrete relation is necessary for every proof; it describes one sufficient observable route. The full route also needs random-slit observable convergence and martingale transfer.",
  "assumptions": "Interpret the source node as a dated, author-checked attempt, not a theorem-equivalence proof.",
  "source": {"type": "owner-own-work", "artifact": "SOURCES.md", "existing_node": "claim_3908da7919a7318bc7b220dc189ceb958a0b62e279555dd907896a7f04d7bf77", "source_quote": "So the conjecture is reduced, for q in [1,4], exactly to finding an additional discrete relation for the parafermionic observable"},
  "proof_or_counterexample": "The primary source gives a sufficient observable-convergence route, not a necessity theorem about extra finite-mesh relations. L1/L3 in the paired proof explicitly isolate the random-domain and uniform-integrability inputs.",
  "independent_reviewer": "w590 (pending)", "remaining_gap": "Live-store revision needs coordinator review; this row is a draft source/scope correction.", "status": "sketch", "parent_problem_solved": False})

own_source = {"source_id": "owner-probability-campaign-w589-C0049-20261010", "url": "urn:owner:probability-campaign:w589:C0049:20261010",
              "revision": "independent-adversary-draft-v1", "license": "owner-own-work", "excerpt": None}
def entry(key, logical, title, statement, assumptions, source=None):
    return {"key": key, "namespace": "probability.statmech", "logical_name": logical, "kind": "concept",
            "title": title, "statement": statement, "proof_text": None, "assumptions": assumptions,
            "domain": "probability and complex analysis", "source": source or own_source}
entries = [
 entry("endpoint", "parafermionic-boundary-phase-endpoint-control", "DRAFT: endpoint control in parafermionic identification",
       "DRAFT; independent referee pending. On the upper half-plane with the upper logarithm, for 0<sigma<=1 and epsilon>0, z^(-sigma)(1+epsilon/z^2) has the same positive boundary rays as z^(-sigma) and the same z^sigma F->1 normalization at infinity, but differs. Even the nonvanishing function z^(-sigma)exp(epsilon/z^2) has those data. Boundary phases and infinity normalization alone do not prove uniqueness. A uniform bound on z^sigma F near zero, real continuous boundary values away from zero, and uniform infinity normalization do imply F=z^(-sigma) by reflection, removability, and Liouville.",
       ["Analytic in H; upper logarithm; continuous boundary values away from marked endpoint 0", "No FK endpoint estimate is proved here"]),
 entry("ui", "uniform-path-limit-martingale-integrability-obstruction", "DRAFT: uniform path convergence does not preserve martingales",
       "DRAFT; independent referee pending. For a unit-rate Poisson process N, M^n_t=1-t+nN_{t/n}, 0<=t<=1, is a nonnegative true martingale in its own natural filtration. Its paths eventually equal 1-t on the entire interval almost surely, because the first Poisson jump time is positive. Thus it converges uniformly almost surely to a continuous deterministic non-martingale. Uniform integrability is absent: E[M^n_t]=1 but E[1-t]=1-t. Joint path convergence alone cannot pass a renormalized observable's conditional martingale identity to the limit.",
       ["Each prelimit uses the time-changed Poisson natural filtration", "This is an abstract inference counterexample, not an FK counterexample"]),
 entry("driver", "conditional-complex-parafermionic-driver-identification", "DRAFT: complex observable identifies the Loewner driver",
       "DRAFT; independent referee pending. Let sigma>0 and W_0=0 be a real continuous adapted chordal Loewner driver, with dg_t=2/(g_t-W_t)dt. If exp(sigma(Log g'_t(z)-Log(g_t(z)-W_t))) is a full complex continuous local martingale in the same usual filtration for every z=im, m a positive integer, before swallowing, then W has bracket 8t/(1+sigma), zero drift, and W/sqrt(8/(1+sigma)) is Brownian motion. Recover the semimartingale premise from a local inverse of the nonzero observable; Ito's imaginary finite-variation equation removes signed drift. This conditional route does not establish discrete observable convergence.",
       ["Consistent continuous logarithms", "Both real and imaginary parts are local martingales", "No random time-dependent normalization"]),
 entry("gap", "c0049-random-slit-observable-convergence-gap", "DRAFT: precise remaining C0049 observable gap",
       "DRAFT. For the square-lattice FK-to-SLE observable route, the unresolved input is convergence of the correctly normalized vertex observable (2delta)^(-sigma)f_delta in actual explored slit domains to a fixed deterministic multiple of (g'_t/(g_t-W_t))^sigma, together with common localization, joint convergence of stopped histories, and stopped uniform integrability. Static-domain convergence or weak contour equations alone do not provide this input. The historical C0049 attempt's additional-discrete-relation strategy is sufficient if completed, not a proved necessary characterization of every solution route. Full target openness is UNKNOWN here; q<1 critical tuning and tightness also require verification.",
       ["Source target is Dobrushin square-lattice bond FK; triangular site percolation is different", "No C0049 solved or retired claim"]),
 entry("q4", "c0049-q4-free-loop-source-status-october-2026", "Source status: October 2026 q=4 free-loop convergence",
       "As checked on 2026-10-10, Averous, Duminil-Copin, He, Lammers and Manolescu, arXiv:2610.08507v1 (6 October 2026), Theorem 1.2 states that critical square-lattice random-cluster loop ensembles with q=4 and p=2/3, free boundary conditions, and Caratheodory domain approximation converge weakly to nested CLE(4) in the Camia-Newman topology. This is a checked primary theorem statement; its proof is not independently audited here. The stated theorem does not itself assert Dobrushin chordal-interface convergence. It qualifies older blanket open-status records but does not automatically retire the exact C0049 target.",
       ["Free boundary loop ensembles; square lattice; q=4 p=2/3", "Primary-source statement check is separate from proof review"],
       {"source_id": "arxiv:2610.08507v1", "url": "https://arxiv.org/html/2610.08507v1#S1.SS3", "revision": "v1-as-read-2026-10-10", "license": "arxiv-nonexclusive (facts paraphrased; no reproduced proof)", "excerpt": "with free boundary conditions"})]
existing = "math:probability.statmech:open-problem-c0049-convergence-of-random-cluster-interfaces-to-sle-kappa-for-q-in-0-4-q-n"
relations = [
 {"from_key": "gap", "to_key": "ui", "kind": "cites", "rationale": "The route requires 'stopped uniform integrability'; the Poisson counterexample establishes why 'joint path convergence alone' is insufficient."},
 {"from_key": "gap", "to_key": "driver", "kind": "cites", "rationale": "The gap names the limiting full complex martingale; the conditional identification entry derives the driver only after that input."},
 {"from_key": "gap", "to_key": "endpoint", "kind": "cites", "rationale": "The gap requires identification of the analytic limit; the endpoint example prevents replacing that identification by boundary phases alone."},
 {"from_key": "gap", "to_existing_logical": existing, "kind": "semantic_association", "rationale": "Existing target is 'critical random-cluster ... Dobrushin domains'; this entry isolates the random-slit observable route to that target."},
 {"from_key": "q4", "to_existing_logical": existing, "kind": "semantic_association", "rationale": "Existing target includes q in (0,4]; Theorem 1.2 now gives q=4 free-loop CLE4 convergence, with a different stated boundary observable."}]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w589", "bundle_slug": "c0049-adversary-endpoint-martingale-20261010", "entries": entries, "relations": relations}
save("bundle_001.json", bundle)
INBOX.mkdir(parents=True, exist_ok=True)
destination = INBOX / "bundle_001.json"
if destination.exists():
    if json.loads(destination.read_text(encoding="utf-8")) != bundle:
        raise RuntimeError("Existing inbox draft differs: use a new numbered bundle, do not overwrite shared artifacts")
else:
    part = INBOX / "bundle_001.json.part"
    part.write_text(json.dumps(bundle, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    part.rename(destination)
save("DELIVERY_STATE.json", {"prepared": True, "submitted": True, "reviewed": False, "ingested": False, "retrievable": False,
     "submission_path": str(destination), "entries": len(entries), "relations": len(relations),
     "reason": "DRAFT concepts only; independent referee and served-identity evidence pending. Coordinator integrates; no live-store write."})
print(json.dumps({"exact_checks": checks, "elapsed_seconds": elapsed, "audit_rows": len(verdicts), "peer_sha256": peer_sha,
                  "draft_entries": len(entries), "draft_relations": len(relations), "submitted": str(destination), "primary_sources": len(primary)}))
