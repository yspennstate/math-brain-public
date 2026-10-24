"""Save the P0104 review packet and an atomic, unintegrated draft bundle."""
import json
from pathlib import Path
from datetime import datetime, timezone
import os

BASE = Path(__file__).resolve().parent
if (BASE / "BUNDLE_RECEIPT.json").exists():
    raise SystemExit("A submission receipt already exists. Review the saved packet; do not repeat the one-shot submission.")
def write_json(name, data):
    (BASE / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

problem = json.loads((BASE / "original_problem.json").read_text(encoding="utf-8"))
prior = json.loads((BASE / "original_attempts.json").read_text(encoding="utf-8"))
hash_check = json.loads((BASE / "SOURCE_HASH_RECEIPT.json").read_text(encoding="utf-8"))
test = json.loads((BASE / "REFEREE_RECEIPT.json").read_text(encoding="utf-8"))
assert test["all_checks_pass"] and hash_check["raw_matches"] and hash_check["text_matches"]
write_json("SOURCE_STATUS.json", {
    "problem_id": "P0104", "checked_on": "2026-10-10",
    "exact_intake": {"path": "~/Downloads/Probability_1000_20h_20260906/problems.jsonl", "line": 175, "record": problem},
    "original_attempt": {"path": "~/Downloads/Probability_1000_20h_20260906/attempts.jsonl", "line": 106, "record": prior[0]},
    "primary_source": {
        "title": "50 years of first passage percolation", "authors": ["Antonio Auffinger", "Michael Damron", "Jack Hanson"],
        "url": "https://arxiv.org/pdf/1511.03262v2", "arxiv_revision_date": "2016-09-23", "intake_source_statement_date": "2016-09-26",
        "source_id": "fpp_survey_2015", "verified_questions": [13, 15],
        "verified_locator": "Questions 13 and 15: one-based PDF page 37, section 3.1; variance convention equation (3.1): PDF pages 34-35",
        "saved_text_locations": {"question_13": [1772, 1773], "question_15": [1777]},
        "short_source_quotes": ["under suitable conditions on F", "If d = 2, show that χ = 1/3.", "For suitable d, show that χ > 0."],
        "complete_scope_in_own_words": "For nondegenerate iid nonnegative edge weights on nearest-neighbor Z^d, find suitable distributional conditions and a precise fluctuation-exponent definition under which chi<1/2 for d>=2; establish chi=1/3 in d=2; establish chi>0 in a suitable dimension. The original source does not give a complete universal hypothesis package and discusses multiple meanings of variance scaling.",
        "locator_correction": {"old": problem["locator"], "new": "Questions 13/15 are together on PDF page 37 in the checked 160-page v2, not identified by the intake's page 34/40 pointer."},
        "hash_receipt": "SOURCE_HASH_RECEIPT.json", "hash_check_is_mathematical_proof": False
    },
    "restricted_attempt": {"law": "iid Uniform[1,2]", "graph": "undirected nearest-neighbor Z^2", "endpoints": ["(0,0)", "(n,0)"], "n": "positive integer", "goal": "Var(T_n)=n^(2/3+o(1))", "exponent_definition": "lim log Var(T_n)/(2 log n)", "full_parent_generality": False},
    "recent_primary_literature": {"url": "https://arxiv.org/html/2604.01214v1", "date": "2026-04-01", "locator": "Theorem 1; sections 1.1 and 1.3", "scope_checked": "Bounded positive smooth isotropic Riemannian field built from a nonnegative compactly supported radial kernel and Gaussian white noise or a Poisson process, with a monotone smooth transform; the published polynomial variance bound is for this specified continuum model.", "lattice_transfer": "Not proved by this paper; its section 1.3 discusses a possible extension with an additional uniform-curvature assumption.", "paper_proof_independently_audited": False},
    "owner_solved_retired_check": {"original_attempt_full_problem_solved": False, "ranking_status": "attempted_un on 2026-09-07", "H_I_and_lean_ID_probe": "No P0104 proof row found in the named H/I attempt paths or lean directory; ranking annotation is historical only.", "prior_FPP_store_evidence": ["claim_f2576eacbf43455993d206cbe36d536a", "claim_925a5f66e641446fa12df62c9b4b5b34", "claim_8155eb9223844b2b91e0bc3b4ae43a49"], "interpretation": "Checked campaign cards separate the proved abstract resampling engine from an unproved variance-ratio wall and explicitly leave chi=1/3 unmoved. This is a targeted check, not an exhaustive proof of current openness or retirement status."},
    "current_openness": "UNKNOWN", "parent_solved": False,
    "novelty_claim": False,
    "next": "Audit the actual quantitative coupled-threshold estimate; source verification and the exact identity are finished, and the geometric crossover remains unproved."
})

claims = [json.loads(line) for line in (BASE / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
claims[0]["prior_work"] = "P0104-A001 already states this correction; reproduced here, not a new result."
claims += [
 {"claim_id": "w362-C002", "problem_id": "P0104", "statement": "For finite independent coordinates and f in L2, H_f(t)=sum_{S nonempty}|S|exp(-|S|t)||f_S||_2^2 is nonnegative and decreasing, and Var(f)=integral H_f. For the bounded lattice target H_n(0)<=2n. If for every epsilon in (0,1/3), H_n(n^(-1/3-epsilon))>=c_epsilon n and Cov(T_n(W),T_n(W^{n^(-1/3+epsilon)}))<=C_epsilon n^(2/3+epsilon) for all sufficiently large n, then Var(T_n)=n^(2/3+o(1)).", "assumptions": ["independent finite product coordinates", "coordinate refresh at rate one", "f in L2", "for the lattice conclusion, iid Uniform[1,2] on undirected Z^2 and integer n>=1", "both stated crossover estimates, with constants uniform in n"], "source": {"source_id": "owner-own-work:w362:p0104-conditional-calibration", "path": "PRODUCT_RESAMPLING.md"}, "proof_or_counterexample": "Commuting coordinate-average projections give orthogonal f_S and refresh eigenvalues exp(-|S|t). Integrate the resulting energy. The one-edge exchangeability and old-geodesic comparison bound H_n(0) by 2n. Monotonicity supplies the lower interval n^(-1/3-epsilon); split the upper integral at n^(-1/3+epsilon). Bounds are c_epsilon n^(2/3-epsilon) and (2+C_epsilon)n^(2/3+epsilon). Let epsilon tend to zero.", "independent_reviewer": {"agent": "w365", "state": "requested locally; pending", "packet": "REVIEW_REQUEST_w365.md"}, "remaining_gap": "Neither crossover estimate is proved. This is a conditional implication, not a solution or a new unconditional FPP result.", "status": "proved special case", "novelty_claim": False},
 {"claim_id": "w362-C003", "problem_id": "P0104", "statement": "For a finite connected graph with independent Uniform[1,2] edges and simple terminal paths, define p_e=clip(B_e-A_e-1,0,1), where A_e is the cheapest through path excluding e's own cost and B_e is the cheapest avoiding path. For 0<=a<=b<=1, the shared-coordinate capped-uniform covariance is K(a,b)=a^2 b/2-a^2 b^2/4-a^3/6>=a^2 b/12. The resampling energy is exp(-t) sum_e E[K(p_e,p_e^t)].", "assumptions": ["finite connected graph and distinct connected terminals", "positive edges with iid Uniform[1,2] law", "paths are simple", "irrelevant through-path class contributes zero; absent avoiding class uses cap one", "off-edge coupled refresh is independent of the edge retention flag and edge uniforms"], "source": {"source_id": "owner-own-work:w362:independent-w361-kernel-reproduction", "path": "INDEPENDENT_KERNEL_AUDIT.md", "peer_source": "peer_snapshots/w361/ATTEMPT.md"}, "proof_or_counterexample": "Split the shared uniform integral at a and b and subtract (a-a^2/2)(b-b^2/2). Centered coordinate products vanish after independent edge replacement and contribute K after retention, whose probability is exp(-t). Thresholds are not assumed independent.", "independent_reviewer": {"agent": "w365", "state": "requested locally; pending", "packet": "REVIEW_REQUEST_w365.md"}, "remaining_gap": "The same algebra independently checks w361's matching kernel; it supplies no n-dependent decorrelation scale. Use as w362's own proof remains pending w365.", "status": "proved special case", "novelty_claim": False},
 {"claim_id": "w362-C004", "problem_id": "P0104", "statement": "For iid Uniform[1,2] planar nearest-neighbor undirected FPP, the energy H_n of rate-one independent edge refresh satisfies, for every epsilon in (0,1/3) and all large n, H_n(n^(-1/3-epsilon))>=c_epsilon n and C_n(n^(-1/3+epsilon))<=C_epsilon n^(2/3+epsilon), with positive constants independent of n.", "assumptions": ["the explicitly chosen bounded planar FPP model", "H_n and C_n are defined in PRODUCT_RESAMPLING.md"], "source": {"source_id": "owner-own-work:w362:p0104-unproved-crossover", "path": "PRODUCT_RESAMPLING.md section 4"}, "proof_or_counterexample": "Attempted from product algebra and linear path length. Those prove only H_n(0)<=2n and H_n(t)<=2n exp(-t). A fixed iid Uniform[1,2] path has H_n(t)=(n/12)exp(-t), showing these algebraic facts do not force the needed crossover. The planar optimization input is still missing.", "independent_reviewer": {"agent": "w365", "state": "pending"}, "remaining_gap": "Both upper covariance decay and lower energy persistence at the chosen n^(-1/3) scale remain unproved; no evidence is offered for this conjecture.", "status": "conjecture", "novelty_claim": False}
]
(BASE / "CLAIMS.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in claims), encoding="utf-8")

reviews = [json.loads(line) for line in (BASE / "PEER_REVIEWS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
reviews[0]["checks"] = "Independent exact enumeration: 16 of 16 assignments and 5 of 5 coupled covariance checks pass; see REFEREE_RECEIPT.json."
reviews += [
 {"review_id": "w362-R003", "reviewer": "w362", "author": "w361", "claim_id": "ATTEMPT.md replacement-threshold kernel and normalization", "verdict": "KEEP", "scope": "Finite-product kernel and variance identity only", "source_path": "peer_snapshots/w361/ATTEMPT.md", "reproduction": "INDEPENDENT_KERNEL_AUDIT.md independently obtains K(a,b)=a^2[b(2-b)/4-a/6], with w361's avoiding/through labels swapped to my notation. PRODUCT_RESAMPLING.md independently proves the orthogonal identity. Conditioning on the off-edge pair contributes exp(-t)K on retention and zero on replacement. Empty classes and simple-path restriction are necessary and treated in the peer statement. A one-edge control gives integral exp(-t)/12=1/12.", "remaining_gap": "The two-sided integrated threshold estimate is unproved. No lattice exponent follows from this KEEP.", "status": "independently checked proof"},
 {"review_id": "w362-R004", "reviewer": "w362", "author": "w361", "claim_id": "ATTEMPT.md sufficient stronger decay/persistence route", "verdict": "KEEP", "scope": "Conditional implication only", "source_path": "peer_snapshots/w361/ATTEMPT.md", "reproduction": "If the peer's unweighted kernel sum is <=C n F(n^(1/3)t), with nonnegative integrable F, its exp(-t)-weighted integral is <=C n^(2/3) integral F. Persistence >=c n until c' n^(-1/3) gives lower bound c c' exp(-c') n^(2/3). The constants must be uniform in n. The peer correctly labels both inputs unproved and the integrated target as equivalent to the variance question.", "remaining_gap": "No proof of the decay envelope or persistence interval; parent remains unresolved.", "status": "independently checked proof"}
]
(BASE / "PEER_REVIEWS.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in reviews), encoding="utf-8")

namespace = "probability.first-passage-percolation"
probe = json.loads((BASE / "STORE_PROBE_RECEIPT.json").read_text(encoding="utf-8"))
assert namespace in probe["namespaces"]
def source(agent, path, label):
    return {"source_id": "owner-own-work:" + agent + ":p0104:" + label, "url": "file:///~/brain_workers/" + agent + "/" + path, "revision": "as-checked-2026-10-10", "license": "owner-own-work", "excerpt": None}
entries = [
 {"key": "square-selection", "namespace": namespace, "logical_name": "square-fpp-minimum-path-selection-dependent-edge-costs", "kind": "lemma", "title": "Minimum-path selection makes iid square-edge costs dependent", "statement": "On a square with opposite terminals and four independent edge costs uniform on {1,2}, select the two-edge upper path when its total cost is no larger than the lower path. Given upper selection, the covariance of its successive edge costs is -5/121. Without conditioning, the covariance of the two selected edge costs is -9/256. Their total has variance 23/64, whereas the sum of their individual variances is 55/128. This finite example refutes independence inferred solely from the iid input edges after global minimizing-path selection; it gives no lattice fluctuation exponent.", "proof_text": "The upper pairs (1,1),(1,2),(2,1),(2,2) have respectively 4,3,3,1 compatible lower pairs among 16 equally likely configurations, giving 11 upper-selection cases. Conditional means are 15/11 and product mean 20/11, so covariance is -5/121. Including strict lower wins gives selected-pair counts 7,4,4,1. The individual mean is 21/16 and product mean 27/16, so covariance is -9/256. Direct total-cost moments give variance 23/64; each selected cost has variance 55/256. Independently recounted by w362 and exactly reproduced on all 16 configurations.", "assumptions": ["finite square graph with opposite terminals", "four iid Uniform{1,2} edge costs", "upper path selected on ties"], "domain": "probability, first-passage percolation, proof auditing", "source": source("w361", "INDEPENDENT_OBSTRUCTION.md", "square-selection")},
 {"key": "finite-box", "namespace": namespace, "logical_name": "one-two-bounded-lattice-fpp-exact-finite-box-reduction", "kind": "lemma", "title": "Exact finite-box reduction for lattice costs in [1,2]", "statement": "For every configuration of edge costs in [1,2] on the undirected nearest-neighbor lattice Z^2 and integer n>=1, the passage time from (0,0) to (n,0) equals the minimum over simple paths in the induced finite graph on [-2n,2n]^2 intersect Z^2. It lies between n and 2n. No iid or continuity hypothesis is needed. The reduction gives no fluctuation exponent.", "proof_text": "The horizontal n-edge path costs at most 2n, and any terminal path has at least n edges and costs at least n. A path leaving the box takes at least 2n+1 edges before its first outside vertex, so costs more than 2n. Positive-cost loops can be removed. The finite graph has finitely many simple paths, hence its minimum exists and equals the full-lattice infimum. Independently checked by w362 against w360-C1.", "assumptions": ["undirected nearest-neighbor Z^2", "all edge costs in [1,2]", "integer n>=1"], "domain": "probability, first-passage percolation", "source": source("w360", "ATTEMPT.md", "finite-reduction")},
 {"key": "conditional-crossover", "namespace": namespace, "logical_name": "planar-fpp-noise-crossover-conditional-exponent-calibration-draft", "kind": "concept", "title": "DRAFT: sufficient noise crossover for the planar variance exponent", "statement": "Unproved-input proof route for iid Uniform[1,2] undirected nearest-neighbor Z^2 FPP, T_n=T(0,n e1). Refresh every edge independently at rate one. Let C_n(t)=Cov(T_n(W),T_n(W^t)) and H_n(t)=-C_n'(t). Finite-product orthogonality proves H_n>=0, H_n decreasing, Var(T_n)=integral_0^infinity H_n(t)dt and H_n(0)<=2n. If, for every epsilon in (0,1/3) and all large n, H_n(n^(-1/3-epsilon))>=c_epsilon n and C_n(n^(-1/3+epsilon))<=C_epsilon n^(2/3+epsilon), with positive constants independent of n, then c_epsilon n^(2/3-epsilon)<=Var(T_n)<=(2+C_epsilon)n^(2/3+epsilon), yielding variance exponent 1/3. BOTH crossover bounds remain unproved. The conditional implication awaits independent w365 review. Product structure and a linear geodesic-length bound alone only give order n; no parent solution or novelty is claimed.", "proof_text": None, "assumptions": ["explicit bounded planar FPP model", "independent rate-one coordinate refresh", "both crossover estimates are unproved inputs"], "domain": "probability, first-passage percolation, draft proof route", "source": source("w362", "PRODUCT_RESAMPLING.md", "conditional-calibration")},
 {"key": "source-scope", "namespace": namespace, "logical_name": "p0104-grouped-exponent-target-primary-source-scope-audit", "kind": "concept", "title": "P0104 source scope and unresolved proof boundary", "statement": "The campaign's P0104 record groups Questions 13 and 15 of Auffinger--Damron--Hanson's 50 years of first passage percolation (arXiv:1511.03262v2, PDF page 37): strict exponent below 1/2 in dimensions at least two under suitable edge-law conditions; exponent 1/3 in the plane; and a positive exponent in a suitable dimension. The source leaves suitable hypotheses and the exact variance-scaling convention to be specified. A bounded Uniform[1,2] planar variance-exponent attempt covers a restricted slice. The April 2026 arXiv:2604.01214v1 polynomial improvement is for its specified isotropic Riemannian continuum model and supplies no proved iid square-lattice transfer. October 2026 current openness is UNKNOWN under this targeted check, and no P0104 solution is claimed. Verified source hashes establish provenance, not mathematical proof.", "proof_text": None, "assumptions": ["statement about the cited source record and the checked paper hypotheses", "no assertion that the long published proofs were independently checked"], "domain": "probability, first-passage percolation, source audit", "source": source("w362", "SOURCE_STATUS.json", "source-scope")}
]
relations = [
 {"from_key": "conditional-crossover", "to_key": "finite-box", "kind": "depends_on", "rationale": "The route uses 'Finite-product orthogonality' for this bounded lattice model; the finite-box endpoint supplies an 'induced finite graph' exactly, so no infinite-volume cutoff extrapolation is needed."},
 {"from_key": "square-selection", "to_key": "conditional-crossover", "kind": "semantic_association", "rationale": "The square endpoint refutes 'independence inferred solely from the iid input edges after global minimizing-path selection'; the route instead uses 'Refresh every edge independently at rate one' and an actual product-space covariance identity. The counterexample does not refute that valid identity."},
 {"from_key": "conditional-crossover", "to_key": "source-scope", "kind": "semantic_association", "rationale": "The route leaves 'BOTH crossover bounds remain unproved'; the source endpoint identifies a 'restricted slice' of the grouped P0104 targets. This records the relation without claiming the conditional route proves the parent problem."}
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w362", "bundle_slug": "p0104-referee-calibration-20261010", "entries": entries, "relations": relations}
write_json("bundle_local.json", bundle)
with (BASE / "RELATION_EVIDENCE.jsonl").open("w", encoding="utf-8") as handle:
    for rel in relations:
        handle.write(json.dumps({**rel, "from_statement": next(x["statement"] for x in entries if x["key"] == rel["from_key"]), "to_statement": next(x["statement"] for x in entries if x["key"] == rel["to_key"]), "status": "draft for coordinator audit"}, ensure_ascii=False) + "\n")

# Structural checks only; this does not invoke or emulate store ingestion.
required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
keys = {x["key"] for x in entries}
assert len(keys) == len(entries) and len(entries) <= 200
for entry in entries:
    assert required <= set(entry)
    assert entry["namespace"] in probe["namespaces"]
    assert entry["kind"] in {"definition", "lemma", "theorem", "concept"}
    assert (bool(entry["proof_text"]) if entry["kind"] in {"lemma", "theorem"} else entry["proof_text"] is None)
    assert entry["source"]["license"].startswith("owner-own-work")
for rel in relations:
    assert rel["from_key"] in keys and rel["to_key"] in keys
    assert rel["kind"] in {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
assert [r for r in relations if r["kind"] == "depends_on"] == [relations[0]]

# The task expressly names this agent's draft inbox as an output location.
inbox = Path("~/math-brain-inbox/w362").resolve()
inbox.mkdir(parents=True, exist_ok=True)
number = 1
while (inbox / f"bundle_{number:03}.json").exists() or (inbox / f"bundle_{number:03}.json.part").exists():
    number += 1
destination = inbox / f"bundle_{number:03}.json"
part = inbox / f"bundle_{number:03}.json.part"
assert part.parent.resolve() == inbox and destination.parent.resolve() == inbox
with part.open("x", encoding="utf-8") as handle:
    handle.write(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n")
    handle.flush()
    os.fsync(handle.fileno())
part.rename(destination)
assert json.loads(destination.read_text(encoding="utf-8")) == bundle

write_json("BUNDLE_RECEIPT.json", {"path": str(destination), "entries": len(entries), "relations": len(relations), "submitted": True, "submission_time_utc": datetime.now(timezone.utc).isoformat(), "reviewed": {"w360_finite_reduction": "KEEP by w362", "w361_square_and_kernel": "KEEP by w362", "w362_conditional_calibration_and_kernel": "w365 pending", "second_login_gate": "not claimed"}, "ingested": "NOT_VERIFIED; validating coordinator only", "retrievable": "NOT_VERIFIED", "structural_checks_pass": True, "live_store_writes": 0, "source_hashes_match": 2, "proof_receipt": "REFEREE_RECEIPT.json"})
hooks = [
 {"id": "p0104-w362-01", "area": "math", "event": "stage-start", "cue": "(?i)(selected|geodesic).{0,100}(independent|factor|multiply)", "fire_when": "A proof factors costs along a globally selected minimizing path solely because input edges are iid.", "silent_when": "The proof computes a covariance under an explicitly constructed independent coordinate-refresh coupling.", "text": "Iid input edges need not stay independent after path selection. The square example gives covariance -5/121 after conditioning. Prove the actual factorization or use a covariance/martingale identity.", "evidence": "w362/PEER_REVIEWS.jsonl:w362-R001; REFEREE_RECEIPT.json, 16 exact assignments", "proposer": "w362"},
 {"id": "p0104-w362-02", "area": "math", "event": "stage-start", "cue": "(?i)(resampling|refresh).{0,100}(variance|integral|covariance)", "fire_when": "A rate-one refresh variance identity integrates the shared-coordinate kernel with no retained-coordinate factor.", "silent_when": "The identity includes exp(-t), or uses p=1-exp(-t) with the factor absorbed into dp.", "text": "Check refresh normalization. A one-edge Uniform[1,2] example requires integral exp(-t)/12=1/12; omitting retention makes it infinite. An exact identity still needs the quantitative crossover estimate.", "evidence": "w362/PEER_REVIEWS.jsonl:w362-R003; INDEPENDENT_KERNEL_AUDIT.md; w361 ATTEMPT.md one-edge control", "proposer": "w362"}
]
(BASE / "HOOK_PROPOSALS.jsonl").write_text("".join(json.dumps(h, ensure_ascii=False) + "\n" for h in hooks), encoding="utf-8")
write_json("PROGRESS_EVENT.json", {"agent": "w362", "row": "S1.P0104", "event": "P0104 referee: exact source recovered, 4 narrow KEEP verdicts, 16/16 counterexample checks, 4-entry draft submitted; noise crossover unproved.", "evidence": str(BASE / "REPORT.md"), "publication": "staged locally; worker forbids global progress writes and mesh sends"})

print(json.dumps({"draft": str(destination), "entries": len(entries), "relations": len(relations), "claims": len(claims), "peer_keep_verdicts": len(reviews), "local_schema_checks": "PASS", "parent_solved": False}, indent=2))
