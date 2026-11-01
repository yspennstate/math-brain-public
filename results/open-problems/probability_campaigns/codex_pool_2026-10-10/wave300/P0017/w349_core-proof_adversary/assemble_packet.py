"""Prepare review artifacts and the explicitly authorized DRAFT inbox bundle."""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()


def write_json(name, obj):
    (ROOT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


new_claims = [
    {
        "id": "w349-C006",
        "statement": "For X=Exp(1)-1, s>0, independent Z~N(0,1), Y_s=sX+sqrt(s)Z, A=Var(X|Y_s), and the fixed function f(x)=x, E|Cov(f(X),X|Y_s)|^2 = E A^2 > (E A)^2 = (E||Cov(X|Y_s)||_op)(E Var(f(X)|Y_s)). Thus the unweighted expectation-factorization shortcut fails within isotropic log-concave Gaussian observation posteriors.",
        "assumptions": ["s>0", "X=Exp(1)-1", "Z independent standard Gaussian", "f(x)=x is fixed"],
        "source": "WEIGHTED_GAP.md, independently derived before paired proof access",
        "proof": "Bayes gives a N((y-1)/s,1/s) density truncated below -1. Its variance A(y) is continuous, tends to 0 and 1/s at the two infinities, and satisfies 0<A<=1/s. Y_s has an everywhere-positive density. Hence A is nonconstant, square integrable, and E A^2-(E A)^2=Var(A)>0. All three conditional quantities in the statement equal A or A^2 for f=x.",
        "remaining_gap": "Does not refute the variance-weighted estimate (W) or KLS.",
        "status": "proved special case"
    },
    {
        "id": "w349-C007",
        "statement": "For compactly supported full-dimensional isotropic log-concave mu, let mu_t=Law(X|Y_r,0<=r<=t), Y_t=tX+B_t, and v_t(f)=Cov_mu_t(f,X). If for every smooth f and a.e. t in (0,T), E|v_t(f)|^2<=K E Var_mu_t(f), and the strong-convexity posterior bound C_P(mu_T)<=1/T is available, then C_P(mu)<=exp(KT)/T. Uniform constants extend to arbitrary isotropic log-concave laws by truncation, recentering, whitening, and passage on compact smooth tests.",
        "assumptions": ["T>0 and K<infinity", "standard Brownian observation with independent X", "the weighted estimate holds for every smooth f", "posterior strong-convexity Poincare inequality", "uniform constants in the approximation step"],
        "source": "WEIGHTED_GAP.md conditional reduction; primary analytic background in BKL 2610.05474v1 Section 2",
        "proof": "Innovation filtering gives d(mu_t f)=v_t(f) dW_t. Total variance and Ito isometry give V_f'(t)=-E|v_t(f)|^2. Gronwall yields V_f(T)>=exp(-KT)Var_mu f. Posterior strong log-concavity gives V_f(T)<=mu|grad f|^2/T. Combine. The input estimate is not derived here.",
        "remaining_gap": "Independent referee check of filtering, convex-support strong-convexity approximation and extension; the universal weighted estimate remains unproved.",
        "status": "sketch",
        "conditional_reduction": True
    },
    {
        "id": "w349-C008",
        "statement": "Unproved sufficient input (W): universal T>0 and K<infinity exist such that for every compactly supported full-dimensional isotropic log-concave mu, every smooth f, and a.e. 0<t<T in the Brownian observation model, E|Cov_mu_t(f,X)|^2 <= K E Var_mu_t(f).",
        "assumptions": ["all dimensions", "all such measures", "all smooth test functions", "one common pair T,K"],
        "source": "WEIGHTED_GAP.md, selected exact missing input",
        "proof": None,
        "remaining_gap": "Entire universal inequality; unweighted expectation decay does not establish it.",
        "status": "conjecture"
    },
    {
        "id": "w349-C009",
        "statement": "For every 1<=p<=q and dim H>=2, a nonzero tensor symmetric in its first p and last q positions attains ||T||/||P_qT||=binom(q,p): in an orthonormal binary basis its coefficients are (-1)^a/binom(q,p-a) when the total number of ones is p, and zero otherwise. Tensoring with any nonzero vector in W preserves equality.",
        "assumptions": ["ordered-index Hilbert tensor norm", "P_q averages permutations of the first q positions", "dim H>=2", "W nonzero for the extended statement"],
        "source": "PEER_L1_INDEPENDENT.md, derived from statement before reading w348 proof",
        "proof": "Arrangement counting and the c-th finite difference of binom(q-p+z,c) give P_qT=(-1)^p block_swap(T)/binom(q,p). Block swap is an isometry.",
        "remaining_gap": "w350 independent check; this equality witness alone is not the universal upper-bound proof. w348's upper bound is separately audited KEEP.",
        "status": "proved special case"
    },
    {
        "id": "w349-C010",
        "statement": "Finite fourth moments and isotropy do not suffice to define exponential tilt averages near zero: if R has density 5r^(-6) on r>=1, S is an independent fair sign, and X=sqrt(3/5)SR, then E X=0, E X^2=1, E X^4=9/5, but E exp(zX)=infinity for every real z!=0.",
        "assumptions": ["R is Pareto with shape 5 and minimum 1", "S independent fair sign"],
        "source": "PEER_AUDIT.md L4 scope counterexample",
        "proof": "For k<5, E R^k=5/(5-k), giving the stated moments. On the sign matching z, exponential growth dominates the polynomial r^-6 tail, so the integral diverges.",
        "remaining_gap": "This is not log-concave and is only a counterexample to the general finite-fourth-moment derivative domain. The algebraic quadratic norm identity remains correct.",
        "status": "proved special case"
    }
]
existing = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
ids = {row["id"] for row in existing}
with (ROOT / "CLAIMS.jsonl").open("a", encoding="utf-8") as out:
    for claim in new_claims:
        if claim["id"] not in ids:
            claim.update(independent_reviewer="w350 (pending receipt)", created_utc=now)
            out.write(json.dumps(claim, ensure_ascii=False) + "\n")

audits = [
    {"id": "w349-A001", "subject": "w348 L1", "verdict": "KEEP", "why": "Exact incidence coefficients agree by Vandermonde; nonnegative s=p term gives the full upper bound. Independently derived sharpness witness agrees.", "scope": "Finite-dimensional Hilbert tensors, both block symmetries, 1<=p<=q", "source": "~/brain_workers/w348/ATTEMPT.md L1", "evidence": "PEER_AUDIT.md; PEER_L1_INDEPENDENT.md; PEER_MEASUREMENTS.json", "remaining_gap": "Universal analytic input for KLS remains open in this packet"},
    {"id": "w349-A002", "subject": "w348 L2", "verdict": "KEEP", "why": "The original disjoint block projections commute; no P_q/Q commutation is used. The b+1 stability coefficient accounts for both errors.", "source": "~/brain_workers/w348/ATTEMPT.md L2", "evidence": "PEER_AUDIT.md", "remaining_gap": "No optimal stability coefficient claimed"},
    {"id": "w349-A003", "subject": "w348 L3", "verdict": "KEEP", "why": "Normalized kernel, factorial multiplicity and support orthogonality are correct. Positive frame trace bounds each support; the direct sum adds no support count. Single-coordinate witness attains the claimed norm.", "scope": "Independent centered Exp(1) coordinates; all finite n,d; ordered HS tensor norm", "source": "~/brain_workers/w348/ATTEMPT.md L3", "evidence": "PEER_AUDIT.md; PEER_MEASUREMENTS.json", "remaining_gap": "Special case only; no general log-concave estimate follows"},
    {"id": "w349-A004", "subject": "w348 L4 derivative domain", "verdict": "FIX", "why": "Finite fourth moments do not ensure finite Laplace transform near zero; the exact Pareto-tail counterexample has variance 1 and fourth moment 9/5.", "fixed_text": "For a centered isotropic law with finite fourth moments, define the algebraic map T_2 f=(1/2)E[f(XX^T-I)]. It equals (1/2)D^2F_f(0) when the Laplace transform is finite in a neighborhood of zero. The quadratic-form operator-norm identity holds for the algebraic map under finite fourth moments alone.", "source": "~/brain_workers/w348/ATTEMPT.md L4", "evidence": "PEER_AUDIT.md; w349-C010", "remaining_gap": "Peer's textual repair and referee check"},
    {"id": "w349-A005", "subject": "September P0017 attempted_un ranking", "verdict": "FIX", "why": "The dated label is historical. Accessible October primary preprints claim full proofs; current independent validity is not certified.", "fixed_text": "Current openness UNKNOWN; reported complete proof claims YES; full-target novelty NO.", "source": "SOURCE_STATUS.json", "evidence": "Primary BKL Theorem 1.1 and Balasubramanian-Kasiviswanathan v2 abstract", "remaining_gap": "Complete independent primary proof audit"}
]
(ROOT / "AUDITS.jsonl").write_text("".join(json.dumps(dict(row, auditor="w349", created_utc=now), ensure_ascii=False) + "\n" for row in audits), encoding="utf-8")

source = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["last_updated_utc"] = now
source["reported_complete_resolution"] = True
source["original_cheeger_statement"] = "A universal c>0 satisfies h(mu)>=c/sqrt(||Cov(mu)||_op) for every full-dimensional log-concave probability law, where h is the Euclidean outer-Minkowski boundary ratio infimum over sets of mass strictly between 0 and 1. In isotropic position the bound is h(mu)>=c."
source["sources"].insert(0, {
    "id": "randomstrasse-2603.29571v1", "title": "Randomstrasse101: Open Problems of 2025",
    "url": "https://arxiv.org/html/2603.29571v1", "locator": "Entry 13, Conjecture 30, covariance formulation",
    "license_as_displayed": "CC-BY-4.0", "inspection": "Primary conjecture, covariance normalization and Poincare formulation inspected. Source's half-space display mixes H and S notation; the covariance formulation is unambiguous. For arbitrary sets this packet uses the standard liminf boundary convention rather than presuming existence of the source's displayed limit."
})
for item in source["sources"]:
    if item["id"] == "balasubramanian-kasiviswanathan-2610.07728":
        item.update(version="v2", revised="2026-10-08", url="https://arxiv.org/abs/2610.07728v2", inspection="Primary current v2 abstract inspected: claims C_P<=25 using a deterministic variational argument. Full proof not audited here; initial search summary described v1 and is superseded.")
source["prior_work_check"]["canonical_population_store"] = {
    "path": "~/math-brain-build/local/population/brain.sqlite3", "mode": "read-only plus PRAGMA query_only=ON",
    "targeted_record_count": 2, "records": ["Historical Cheeger open-problem card", "Author-checked Gaussian Hermite special-case attempt"],
    "evidence": "LIVE_STORE_P0017.json and TARGETED_STATUS_STORE.json"
}
source["prior_work_check"]["original_ledger_path"] = "The old worktree path cited by the intake README is absent. Exact primary statement was recovered directly and original relevant store cards were read; no whole ledger export was read."
source["prior_work_check"]["owner_solved_retired"] = "No solved/retired P0017 card appeared in the two targeted store hits. This is a bounded query result, not a certification of all private owner work. Reported public proof claims are recorded separately."
write_json("SOURCE_STATUS.json", source)

measure = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
peer = json.loads((ROOT / "PEER_MEASUREMENTS.json").read_text(encoding="utf-8"))
assert measure["within_compute_gate"] and peer["within_compute_gate"]

(ROOT / "ATTEMPT.md").write_text("""# P0017 adversarial attempt

The exact full target is the universal upper bound C_P(mu)<=C for isotropic
log-concave laws in every dimension, with the variance/Dirichlet normalization.
The original Randomstrasse Entry 13, Conjecture 30 asks equivalently for a
universal Cheeger lower bound in isotropic position. SOURCE_STATUS.json records
the primary statement and the October proof claims. Current openness UNKNOWN;
no full-target novelty or complete independent proof certification is claimed.

The prior live-store attempt proves the Gaussian Hermite special case and
explicitly leaves the general input open. The named H/I targeted searches did
not locate a P0017 proof. The original ledger worktree path is absent. The
source recovery and store read were bounded; private owner work is not certified
exhaustively.

The selected hard input for the independent localization route is (W): universal
T,K control E|Cov_mu_t(f,X)|^2 by K E Var_mu_t(f) for every test function and
every isotropic log-concave law up to time T. WEIGHTED_GAP.md derives the
conditional exp(KT)/T Poincare bound and leaves (W) explicitly unproved.
The reduction uses an actual observation filtration, innovation Brownian
motion, total variance, and Ito isometry; it multiplies no unrelated conditional
expectations. Convex-support strong-convexity and the final approximation are
explicit referee obligations. Smooth strong-convexity itself follows from the
integrated Bochner identity in BKL Section 2: an eigenfunction gives
lambda^2||f||^2>=T||grad f||^2=T lambda||f||^2, hence lambda>=T.

The attempted shortcut to (W) fails even in dimension one for an isotropic
centered exponential law. For f=x and Y_s=sX+sqrt(s)Z, every conditional
variance/covariance factor is the same nonconstant scalar A. The proposed
factorization becomes E A^2<=(E A)^2 and is strictly false. This is w349-C006,
not a counterexample to KLS. The remaining uniform weighted bound is the exact
unfinished mathematical step.

INDEPENDENT.md was saved before paired-prover proof access. It also gives
normalization, raw-moment/cumulant, tilted-covariance and matrix-norm controls.
After reading only w348's challenge, PEER_L1_INDEPENDENT.md supplied an
independent equality witness for the binomial tensor constant and a safe
symmetry-error bound. Then PEER_AUDIT.md checked the actual proof: KEEP L1,
KEEP L2, KEEP L3, FIX only the general finite-fourth-moment Taylor terminology
in L4. The Pareto-tail counterexample and exact minimal repair are recorded
there. The algebraic quadratic-form norm identity remains correct.

For w348's full-target route the unproved universal all-degree Taylor estimate
is the selected hard analytic input. The tensor lemma and centered-exponential
product family do not supply it. No raw moments replace cumulants, no source
hash counts as a proof, and no successful finite computation certifies KLS.

Reproduction:
    python -X utf8 verify_obstructions.py
    python -X utf8 verify_peer.py
Both small runs passed their predeclared gates. The first provides an ordinary
quadrature diagnostic backed by the exact strict-variance argument, and the
second checks exact finite identities. Mathematical evidence and finite checks
are kept separate in CLAIMS.jsonl and the measurement files.

Review: w350 is the independent referee for w349's new results. All such results
remain DRAFT concepts in the inbox until review; account separation and
ingestion are not inferred. w353 independently checks the referee's own results.

NEXT: w350 check C006, the conditional C007 reduction, C009 equality witness and
C010 domain counterexample; then decide whether the universal input (W) or
the published analytic input can be audited without promoting it prematurely.
""", encoding="utf-8")

hook = {
    "id": "weighted-localization-w349-01", "area": "math", "event": "stage-start",
    "cue": "A localization proof replaces E[covariance norm times conditional variance] by the product of its two expectations without a dependence bound",
    "fire_when": "The claimed replacement is used to obtain a dimension-free variance-retention or Poincare bound",
    "silent_when": "The proof keeps the joint expectation, proves independence, or explicitly proves the variance-weighted bound",
    "text": "Keep covariance and conditional variance inside the same expectation. A fixed linear test under an isotropic exponential posterior gives E[A^2]>(E[A])^2. Prove the weighted bound before Gronwall.",
    "evidence": "w349-C006; WEIGHTED_GAP.md; MEASUREMENTS.json s=1 exact-argument diagnostic ratio 1.3930872433467762; proof_steps_need_derived_joint_structure_2026_09_09",
    "proposer": "w349"
}
(ROOT / "HOOK_PROPOSAL.jsonl").write_text(json.dumps(hook) + "\n", encoding="utf-8")

entries = []


def entry(key, logical, title, statement, assumptions, file):
    return {
        "key": key, "namespace": "probability.stochastic_localization", "logical_name": logical,
        "kind": "concept", "title": title, "statement": statement, "proof_text": None,
        "assumptions": assumptions, "domain": "probability and functional inequalities",
        "source": {"source_id": "owner-probability-campaign-w349-20261010:" + key,
                   "url": (ROOT / file).as_uri(), "revision": "author-checked-20261010-v1",
                   "license": "owner-own-work (campaign draft; independent review pending)", "excerpt": None}
    }

entries.append(entry("weighted-counterexample", "exponential-posterior-expectation-factorization-counterexample", "DRAFT: dependent covariance and variance in a log-concave posterior", "DRAFT independent audit, pending w350 check. Let X=Exp(1)-1, s>0 and Z an independent N(0,1), Y=sX+sqrt(s)Z, A=Var(X|Y), and f(x)=x. Then X is isotropic log-concave in dimension one, E|Cov(f(X),X|Y)|^2=E A^2, and (E||Cov(X|Y)||_op)(E Var(f(X)|Y))=(E A)^2. Bayes' posterior is N((Y-1)/s,1/s) truncated below -1. Its variance is bounded, continuous and nonconstant, so E A^2>(E A)^2. Consequently the unweighted expectation-factorization shortcut is false in this class. This does not refute the variance-weighted bound or KLS.", ["s>0", "fixed f=x", "independent standard Gaussian observation noise"], "WEIGHTED_GAP.md"))
entries.append(entry("weighted-input", "unproved-uniform-localization-variance-weighted-input", "UNPROVED: uniform variance-weighted localization input", "UNPROVED SUFFICIENT INPUT, not a theorem. There would exist universal T>0,K<infinity such that for every compactly supported full-dimensional isotropic log-concave mu in every R^n, X~mu independent of Brownian B, mu_t=Law(X|Y_r:0<=r<=t), Y_t=tX+B_t, every smooth fixed f, and a.e. 0<t<T, E|Cov_mu_t(f,X)|^2 <= K E Var_mu_t(f). The same constants must work for all dimensions, measures and functions. Unweighted covariance expectation bounds do not establish this input.", ["compact support and full dimension", "isotropic log-concave law", "Brownian observation filtration", "universal quantifiers over f and mu"], "WEIGHTED_GAP.md"))
entries.append(entry("conditional-route", "conditional-variance-weighted-localization-poincare-reduction", "DRAFT: Poincare reduction conditional on a weighted input", "DRAFT conditional reduction, pending referee check. For compactly supported isotropic log-concave mu and Brownian observation mu_t, assume E|Cov_mu_t(f,X)|^2<=K E Var_mu_t(f) for every smooth f and a.e. 0<t<T. Also use the T-strong-convexity posterior inequality C_P(mu_T)<=1/T. Innovation Ito isometry gives V_f'(t)=-E|Cov_mu_t(f,X)|^2, where V_f(t)=E Var_mu_t(f). Gronwall and E mu_T|grad f|^2=mu|grad f|^2 then give C_P(mu)<=exp(KT)/T. The universal weighted hypothesis is unproved here; this is not a KLS proof.", ["T>0, finite K", "the uniform variance-weighted estimate is assumed", "posterior strong-convexity Poincare inequality", "bounded compact-support filtering justification"], "WEIGHTED_GAP.md"))
entries.append(entry("tilt-domain", "finite-fourth-moments-insufficient-for-exponential-tilts", "DRAFT: fourth moments do not guarantee exponential tilt derivatives", "DRAFT scope correction, pending independent check. Let R have density 5r^(-6) on r>=1, S an independent fair sign, and X=sqrt(3/5)SR. Then E X=0, E X^2=1 and E X^4=9/5, but E exp(zX)=infinity for every real z!=0. Thus isotropy and finite fourth moments alone do not define an exponential tilt average near zero. Require finite Laplace transform on a neighborhood, or define f -> (1/2)E[f(XX^T-I)] algebraically and identify it with a tilt derivative only when tilts exist. This counterexample is not log-concave and does not refute the log-concave target.", ["Pareto shape 5", "independent fair sign", "scope is general probability laws with finite fourth moments"], "PEER_AUDIT.md"))
entries.append(entry("tensor-witness", "sharp-block-symmetry-binomial-tensor-equality-witness", "DRAFT: equality witness for partial tensor symmetrization", "DRAFT independently derived equality witness, pending w350 check. Let 1<=p<=q, dim H>=2, P_q average permutations of the first q positions in H^(tensor(p+q)), and choose orthonormal binary basis e0,e1. For each coordinate let a be the number of ones in its first p positions. Set T=(-1)^a/binom(q,p-a) if the total number of ones is p, and 0 otherwise. T is separately symmetric in its first p and last q positions. A finite-difference identity gives P_qT=(-1)^p block_swap(T)/binom(q,p), so ||T||/||P_qT||=binom(q,p). Tensoring with a nonzero vector in any auxiliary Hilbert space preserves equality. This witness alone is not an upper-bound proof or a KLS proof.", ["ordered-index Hilbert norm", "1<=p<=q", "dim H>=2", "nonzero auxiliary vector when used"], "PEER_L1_INDEPENDENT.md"))

target = "math:probability.core:open-problem-p0017-dimension-free-log-concave-poincare-or-cheeger-constant"
bundle = {
    "spec": "mathbrain-draft-v1", "author_agent": "w349", "bundle_slug": "p0017-weighted-covariance-adversary-001",
    "entries": entries,
    "relations": [
        {"from_key": "conditional-route", "to_key": "weighted-input", "kind": "depends_on", "rationale": "The reduction assumes this universal weighted estimate and does not derive it."},
        {"from_key": "weighted-counterexample", "to_key": "weighted-input", "kind": "semantic_association", "rationale": "The counterexample explains why the weighted input cannot be replaced by a product of unweighted expectations."},
        {"from_key": "weighted-counterexample", "to_existing_logical": target, "kind": "semantic_association", "rationale": "The exact counterexample rules out a shortcut in a localization route to the same isotropic log-concave Poincare/Cheeger problem."},
        {"from_key": "conditional-route", "to_existing_logical": target, "kind": "semantic_association", "rationale": "If its universal input is proved, this conditional variance-retention reduction yields the target Poincare bound."},
        {"from_key": "tensor-witness", "to_existing_logical": target, "kind": "semantic_association", "rationale": "The witness checks sharpness of the deterministic tensor-recovery component in the tilt-derivative route; no universal analytic input is supplied."}
    ]
}
write_json("bundle_001.json", bundle)

allowed_rel = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
keys = {row["key"] for row in entries}
assert len(keys) == len(entries) and len(entries) <= 200
for row in entries:
    assert row["kind"] == "concept" and row["proof_text"] is None
    assert row["source"]["license"].startswith("owner-own-work")
    assert row["statement"] and row["assumptions"]
for rel in bundle["relations"]:
    assert rel["from_key"] in keys and rel["kind"] in allowed_rel
    assert ("to_key" in rel) != ("to_existing_logical" in rel)
    if "to_key" in rel:
        assert rel["to_key"] in keys
write_json("BUNDLE_VALIDATION.json", {"shape_valid": True, "entries": len(entries), "relations": len(bundle["relations"]), "all_concept_drafts": True, "dependency_graph": "one edge, acyclic", "formal_math_proof_check": False, "live_integrator_run": False})

inbox = Path(r"~\math-brain-inbox\w349")
dest = inbox / "bundle_001.json"
inbox.mkdir(parents=True, exist_ok=True)
if dest.exists():
    prior = json.loads(dest.read_text(encoding="utf-8"))
    if prior != bundle:
        raise RuntimeError("Existing inbox bundle differs; preserve it and stop submission")
else:
    part = inbox / "bundle_001.part"
    with part.open("x", encoding="utf-8") as out:
        out.write(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n")
    part.rename(dest)

write_json("BRAIN_STATE.json", {
    "prepared": True, "submitted": True, "submitted_path": str(dest), "submitted_utc": now,
    "narrow_claim_receipt": "clm-bd5cffb79c", "reviewed": False, "review_receipts": [],
    "ingested": False, "retrievable": False, "status": "DRAFT concepts only",
    "coordinator_integration_required": True
})

live = json.loads((ROOT / "LIVE_STORE_P0017.json").read_text(encoding="utf-8"))
target_rows = [row for row in live if "Open problem:" in row["title"]]
assert len(target_rows) == 1
edge = {
    "from_key": "weighted-counterexample", "to_existing_logical": target, "kind": "semantic_association",
    "from_quote": "E|Cov(f(X),X|Y_s)|^2 = E A^2 > (E A)^2",
    "to_quote": "Is there a universal positive lower bound for the Euclidean Cheeger constant of every isotropic log-concave probability measure, in every dimension?",
    "to_card_id": target_rows[0]["id"], "support": "WEIGHTED_GAP.md and LIVE_STORE_P0017.json",
    "rationale": "This refutes a localization shortcut for the same target class, not the target statement.",
    "review_status": "pending w350; exact supporting ends quoted locally"
}
(ROOT / "RELATIONS_EVIDENCE.jsonl").write_text(json.dumps(edge) + "\n", encoding="utf-8")
write_json("PROGRESS_EVENT.json", {"agent": "w349", "row": "S1.P0017.C006", "event": "P0017 adversary: exact log-concave posterior factorization counterexample; peer L1-L3 KEEP and L4 domain FIX; five concept drafts submitted for referee review", "evidence": str(ROOT / "WEIGHTED_GAP.md"), "global_progress_posted": False, "reason": "Prepared locally under worker-only output restriction; DRAFT inbox and named-peer mesh are the explicit external-output scope."})

review = ROOT / "review_packet"
review.mkdir(exist_ok=True)
(review / "INDEX.md").write_text("""# w349 P0017 review packet

First check ../WEIGHTED_GAP.md: the exact in-class posterior counterexample
and the conditional reduction with its unproved input visible.

Then ../PEER_AUDIT.md and ../PEER_L1_INDEPENDENT.md: KEEP L1-L3 and the
minimal L4 derivative-domain repair. ../CLAIMS.jsonl records each exact
statement, assumptions, proof, status, reviewer and remaining gap.

Reproduction scripts: ../verify_obstructions.py and ../verify_peer.py.
Evidence: ../MEASUREMENTS.json, ../PEER_MEASUREMENTS.json,
../SOURCE_STATUS.json, ../LIVE_STORE_P0017.json, ../AUDITS.jsonl.

Submission: ../bundle_001.json matches
~/math-brain-inbox/w349/bundle_001.json.
All entries are concepts and explicitly DRAFT/UNPROVED. ../BRAIN_STATE.json
distinguishes submitted, reviewed, ingested and retrievable.

No live integration, recall change, theorem promotion, blind material,
background job or other worker file modification was performed.

NEXT: w350 independently check C006/C007/C009/C010 and attach receipts;
validating coordinator decides integration only after the required review.
""", encoding="utf-8")
write_json("review_packet/REQUEST.json", {
    "reviewer": "w350", "new_claims": ["w349-C006", "w349-C007", "w349-C009", "w349-C010"],
    "unproved_input": "w349-C008", "requested_checks": ["Nonconstant posterior variance and strict Jensen argument", "Innovation identity, Gronwall, strong convexity and approximation", "Binomial equality witness", "Finite-fourth-moment tilt-domain counterexample"],
    "account_separation": "not certified by worker", "formal_receipt": None, "full_target_claim": False
})

(ROOT / "REPORT.md").write_text(
    "P0017 review deliverables are complete. The main result is an exact counterexample to multiplying an expected covariance norm by an expected conditional variance in log-concave localization. A fixed linear test under a centered exponential posterior makes the claimed inequality E[A^2]<=(E[A])^2, which is strictly false. The sufficient weighted input and a conditional Poincare reduction are written separately; the input remains unproved.\n\n"
    "The paired proof audit keeps w348 L1-L3 and requests one narrow L4 repair: finite fourth moments alone do not guarantee exponential tilt derivatives. A Pareto-tail law supplies the exact counterexample; adding local Laplace finiteness or defining the quadratic map algebraically repairs the scope.\n\n"
    f"Measurements: python -X utf8 verify_obstructions.py passed in {measure['elapsed_seconds']:.6f}s; at s=1, E[A^2]~0.236220603 versus (E[A])^2~0.169566267, ratio~1.393087243. This ordinary quadrature is a diagnostic; strict failure is proved by nonconstant posterior variance. python -X utf8 verify_peer.py passed in {peer['elapsed_seconds']:.6f}s: {peer['incidence_ordered_pair_checks']} exact incidence pairs, 10 sharpness tensors, 64 Gram checks and 36 support traces through degree 8.\n\n"
    "Five concept drafts and five supported relations were submitted atomically to the explicitly named w349 inbox after exclusive claim clm-bd5cffb79c. BRAIN_STATE.json records submitted=true, reviewed=false, ingested=false, retrievable=false. No measured live recall improvement or theorem promotion is claimed. New results still need the independent referee, and source abstracts do not certify full KLS proofs.\n\n"
    "Apply: the validating coordinator independently reviews the packet and then runs its approved draft integrator only for ~/math-brain-inbox/w349; no live-code patch is needed.\n\n"
    "STUCK: the two guessed integrator script paths were absent; switched to a pure local schema check. The live integrator was not run because integration belongs to the validating coordinator. The hook and progress event are prepared locally for the reviewer under the worker output restriction.\n\n"
    "NEXT: w350 check C006/C007/C009/C010, attach exact review receipts, and retain C008 as unproved until its universal inequality is established.\n", encoding="utf-8"
)
(ROOT / "STATUS.md").write_text("STATE: WORKING\nNEXT: Collect the named referee receipts and peer L4 response, verify the saved draft submission, then set NEEDS_REVIEW.\n\n" + now + " Saved complete claim/audit rows, conditional route, exact in-class counterexample, measured controls, review packet and five DRAFT inbox concepts. Submitted only; integration and retrieval not claimed.\n", encoding="utf-8")
print(json.dumps({"claims_total": len(existing) + sum(c["id"] not in ids for c in new_claims), "audit_rows": len(audits), "bundle_entries": len(entries), "bundle_relations": len(bundle["relations"]), "submitted": str(dest), "reviewed": False, "ingested": False}, indent=2))
