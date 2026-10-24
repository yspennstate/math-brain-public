"""Prepare local review artifacts and a draft; never ingest or change live store state."""
from __future__ import annotations
import difflib
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXISTING = "math:probability.core:open-problem-p0017-dimension-free-log-concave-poincare-or-cheeger-constant"


def save(name, data):
    path = ROOT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def entry(key, logical, kind, title, statement, proof, assumptions, artifact):
    return {"key": key, "namespace": "probability.logconcave", "logical_name": logical,
            "kind": kind, "title": title, "statement": statement, "proof_text": proof,
            "assumptions": assumptions, "domain": "probability theory; Euclidean functional inequalities",
            "source": {"source_id": "owner-probability-campaign-w356-20261010:" + key,
                       "url": (ROOT / artifact).as_uri(), "revision": "author-draft-20261010-review-pending",
                       "license": "owner-own-work (campaign derivation and attributed audit; no novelty claim)",
                       "excerpt": None}}


def main():
    measurement = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
    assert measurement["result"] == "PASS" and len(measurement["weighted_energy_checks"]) == 3
    status = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
    status["statement_status"] = "verified against the original problem source and a current primary theorem statement"
    status["original_source"] = {
        "title": "Randomstrasse101: Open Problems of 2025", "version": "2603.29571v1",
        "url": "https://arxiv.org/html/2603.29571v1", "location": "Entry 13, Conjecture 30; equations immediately following",
        "primary_blog": "https://randomstrasse101.math.ethz.ch/posts/KLSConjecture/",
        "formulation": "A universal lower bound on Euclidean Cheeger constant divided by the best half-space cut ratio; equivalently h(mu)>=c/sqrt(||Cov(mu)||_op), uniformly over dimensions and log-concave probabilities.",
        "source_typo_handling": "The arXiv HTML half-space formula binds H but prints S in the ratio. The primary blog uses H consistently. The covariance-normalized formulation is unambiguous in both. The audit uses that formulation and notes the correction explicitly."}
    status["primary_theorem_statement"] = {"url": "https://arxiv.org/html/2610.05474v1", "location": "Theorem 1.1; equations (5)-(6)",
        "assumptions": "Every n>=1 and every isotropic log-concave probability measure on R^n; C_P uses all locally Lipschitz L2 test functions and Euclidean gradient.",
        "mathematical_validity_checked": "Statement only; full proof unaudited"}
    status["primary_proof_claims"][1].update({"url": "https://arxiv.org/abs/2610.07728v2", "revised": "2026-10-08", "claimed_bound": "C_P<=25", "checked": "v2 primary abstract; proof not independently audited"})
    status["primary_proof_claims"][2].update({"url": "https://arxiv.org/abs/2610.01447v2", "revised": "2026-10-04", "claimed_bound": "universal O(1) bound", "checked": "v2 primary abstract; v1 log-star bound is superseded in this source"})
    status["local_solved_retired_check"] = {
        "scanned": "Named September ranking, annotated Lean ranking, intake dedup index, H/I attempts (exact ID and KLS/title searches), Team O board, targeted population export and read-only population store query.",
        "found": "The existing P0017 attempt card contains a standard-Gaussian Hermite-expansion special case and explicitly says it does not prove general KLS and has no independent review.",
        "certifies_no_other_solution": False,
        "limitations": "No whole-corpus or retired-machine search; canonical alternate-store location was not established in this packet. Current openness remains UNKNOWN with primary full-resolution claims recorded."}
    status["brain_states"] = {"prepared": True, "submitted": False, "reviewed": False, "ingested": False, "retrievable": False}
    save("SOURCE_STATUS.json", status)

    entries = [
      entry("constants", "euclidean-poincare-and-cheeger-constant-conventions", "definition", "Poincare and Cheeger constants: Euclidean conventions",
        "For a probability measure nu, C_P(nu) is the least coefficient in Var_nu(f)<=C_P(nu) integral |grad f|^2 dnu for locally Lipschitz L2 functions; infinite energy makes the inequality automatic. h(nu) is inf nu^+(B)/min(nu(B),1-nu(B)) over Borel sets with 0<nu(B)<1, where nu^+(B)=liminf_{epsilon down to 0}(nu(B+epsilon EuclideanBall)-nu(B))/epsilon. On a line the gradient uses Euclidean arclength. Isotropic means barycenter zero and covariance identity.",
        None, ["Euclidean metric", "Borel probability measure"], "SOURCE_STATUS.json"),
      entry("parent", "p0017-normalized-kls-source-status-20261010", "concept", "P0017: normalized KLS target and October proof-claim status",
        "The P0017 target asks for a finite universal C with C_P(mu)<=C for every dimension n>=1 and every isotropic log-concave probability on R^n; equivalently a universal positive Euclidean Cheeger lower bound. Original source: Randomstrasse101: Open Problems of 2025, 2603.29571v1, Entry 13, Conjecture 30. On 2026-10-10 primary preprints 2610.05474v1, 2610.01447v2 and 2610.07728v2 claim full proofs; the last claims C_P<=25. This draft verifies their statement/version metadata, not their proofs. The September attempted_unsolved label cannot certify current openness. Openness UNKNOWN in this audit; no new solution or novelty claim. A partial slice lemma does not settle the parent.",
        None, ["Full-dimensional log-concave probability", "Covariance normalization", "Status observation dated 2026-10-10"], "SOURCE_STATUS.json"),
      entry("pointwise-bridge", "refuted-ambient-isotropy-uniform-line-fiber-bridge", "concept", "Refuted bridge: ambient isotropy bounds every line fiber",
        "FALSE auxiliary claim: one finite universal B bounds C_P(mu(.|P_{u-perp}X=z)) for every dimension, every isotropic log-concave mu, every unit u, and projected-almost-every z, without restandardizing the conditional law. The isotropic-simplex edge-fiber family forces essential supremum 2(n+1)(n+2)/pi^2. This stronger bridge's failure does not refute normalized KLS.",
        None, ["Inherited Euclidean metric", "Regular conditional laws", "Essential supremum against projected law"], "SIMPLEX_FIBERS.md"),
      entry("simplex", "isotropic-simplex-edge-fiber-poincare-extremes", "lemma", "Isotropic simplex: exact extremes and average of edge-fiber constants",
        "Author-proved special case; independent review pending. For each n>=2 an isotropic uniform regular-simplex probability mu_n and an edge-parallel unit u have orthogonal-projection fibers whose inherited-arclength constants satisfy ess sup C_P=2(n+1)(n+2)/pi^2, E C_P=12/pi^2, ess sup Var=(n+1)(n+2)/6 and E Var=1. The ess sup uses the projected law and every near-extremal range has positive mass. Each fiber itself satisfies C_P=(12/pi^2)Var, so it is the conditional covariance control that fails.",
        "For X uniform on {x_i>=0,sum x_i<=1}, m=EX and Sigma=Cov X, let a=(n+1)(n+2), A=Sigma^{-1/2}, Y=A(X-m), u=Ae_1/sqrt(2a). Direct simplex integration gives Sigma^{-1}=a(I+J), so Y is isotropic and |Ae_1|^2=2a. The projected base fixes x_2,...,x_n; conditionally x_1 is uniform on [0,T], T=1-sum_{i>=2}x_i. Thus <u,Y> is uniform on a centered interval of length sqrt(2a)T. T has Beta(2,n-1) law, ET^2=6/a and P(T>1-epsilon)>0. Interval variance L^2/12 and sharp Poincare coefficient L^2/pi^2 give all claims. Independently represented in w355's barycentric H-space derivation and checked by w356; w356's own contribution still awaits its designated reviewer w359.",
        ["n>=2", "Uniform regular simplex whitened to covariance I", "Orthogonal projection along an edge", "No individual fiber rescaling"], "SIMPLEX_FIBERS.md"),
      entry("averaging-bridge", "refuted-unweighted-average-fiber-energy-bridge", "concept", "Refuted bridge: separate the average constant from fiber energy",
        "FALSE auxiliary inference: E C_P(fiber)=B implies E Var(f|Z)<=B E |partial_u f|^2 for all Lipschitz f. The valid conditional inequality is E Var(f|Z)<=E[C_P(fiber) E(|partial_u f|^2|Z)]. Removing this covariance between fiber size and energy is unjustified. The isotropic-simplex cosine test family has a quotient 50.5 times B at n=100,k=10, although B=12/pi^2.",
        None, ["Orthogonal projection Z onto u-perp", "Directional energy only", "Finite integrals"], "SIMPLEX_FIBERS.md"),
      entry("weighted", "isotropic-simplex-cosine-weighted-directional-energy-counterexample", "lemma", "Simplex cosine family: exact failure of unweighted fiber-energy averaging",
        "Author-proved special case; independent review pending. In the preceding simplex let a=(n+1)(n+2), T=1-sum_{i>=2}X_i and f_k(Y)=T^k cos(pi X_1/T), extended by zero at T=0, for integer k>=1. It is Lipschitz and E[f_k|Z]=0. Its conditional-variance/directional-energy quotient is R(n,k)=(2a/pi^2)(2k)(2k+1)/((n+2k-1)(n+2k)). For k>1 it exceeds 12/pi^2; for n=100,k=10 its ratio to that mean fiber constant is exactly 50.5. As k grows, R tends to 2a/pi^2. No assertion uses this directional energy in place of the full gradient in KLS.",
        "Since 0<=X_1<=T, partial derivatives of T^k cos(pi X_1/T) are bounded by constants times T^(k-1); it extends continuously and is Lipschitz on the simplex. Along u, A^{-1}u=e_1/sqrt(2a) and T is fixed. Conditional cosine mean is zero, variance is T^(2k)/2 and directional energy is pi^2 T^(2k-2)/(4a). For T~Beta(2,n-1), ET^r=(r+1)!n!/(n+r)!. Dividing the two moments proves R. At n=100,k=10, (a/6)*420/(119*120)=101/2. The transverse part of the gradient remains outside this directional calculation.",
        ["The simplex and direction from the preceding lemma", "Integer k>=1", "Lipschitz extension, no C1 claim at T=0"], "SIMPLEX_FIBERS.md"),
      entry("interval", "uniform-interval-sharp-poincare-cheeger-scale-boundary", "lemma", "Uniform interval: exact Poincare, Cheeger and scale boundary",
        "Independently rederived by w356 from w354's claim. Uniform probability on a Euclidean interval of length L>0 has variance L^2/12, C_P=L^2/pi^2 and h=2/L. At variance one these are C_P=12/pi^2 and h=1/sqrt(3). Arbitrary dilation therefore forbids an unnormalized universal C_P upper bound or h lower bound, without contradicting the normalized KLS target.",
        "Integrating x and x^2 gives variance L^2/12. Even reflection of a mean-zero H1 function gives a 2L-periodic function; Parseval and the first nonzero frequency pi/L imply C_P<=L^2/pi^2. Cos(pi x/L) attains equality. A half interval has outer Minkowski perimeter 1/L and min mass 1/2. Any nontrivial Borel set either has positive closure-minus-set mass and infinite outer perimeter, or a nonempty open complement component with an interior endpoint supplies an epsilon expansion strip of length epsilon. Thus perimeter>=1/L and h>=2/L. The half interval attains the lower bound.",
        ["L>0", "Uniform probability", "Euclidean gradient and outer Minkowski perimeter", "Min-mass Cheeger convention"], "PEER_REVIEWS.jsonl")
    ]
    entries.append(entry("triangle-polynomial", "isotropic-triangle-polynomial-full-gradient-accounting", "lemma", "Isotropic triangle: a smooth polynomial separates directional and full energy",
        "Independently rederived by w356 from w354's polynomial claim. On the whitened uniform standard triangle, use the edge direction u from the simplex construction, T=<u,Y>, S=X_2 and f(Y)=T(1-S)^2. Then E[f|Z]=0, E Var(f|Z)=1/2, E|partial_u f|^2=1/3 and E|grad f|^2=13/27. Replacing the mean fiber constant 12/pi^2 in the directional conditional inequality would require 1/2<=4/pi^2, which is false. The full-gradient Rayleigh quotient is 27/26; this calculation does not refute KLS.",
        "With t=1-X_2, its density is 2t and conditional Var(T|Z)=2t^2. The affine base gradient b=grad_Y S is perpendicular to u and has |b|^2=1/18. Therefore f has variance 2Et^6=1/2 and directional energy Et^4=1/3. Its full gradient is u*t^2-2*T*t*b, with zero cross term; its energy is Et^4+4|b|^2E[T^2t^2]=13/27. Independently integrating the raw polynomial f/sqrt(24)=X_1t^2-t^3/2 and its two derivatives against exact triangle monomial moments gives the same variance and full energy. Since pi>3, 4/pi^2<4/9<1/2.",
        ["Whitened uniform triangle in dimension two", "Euclidean full gradient and the specified edge direction", "The polynomial is smooth"], "PEER_REVIEWS.jsonl"))
    relations = [
      {"from_key": "simplex", "to_key": "constants", "kind": "depends_on", "rationale": "The exact simplex constants use the declared inherited-arclength and isotropy conventions."},
      {"from_key": "simplex", "to_key": "pointwise-bridge", "kind": "refutes", "rationale": "The positive-mass essential supremum grows quadratically with n under the bridge's ambient-isotropy assumptions."},
      {"from_key": "weighted", "to_key": "simplex", "kind": "depends_on", "rationale": "The cosine test uses precisely that simplex, direction and beta-distributed fiber length."},
      {"from_key": "weighted", "to_key": "averaging-bridge", "kind": "refutes", "rationale": "Its n=100,k=10 conditional-variance/energy ratio is exactly 50.5 times the proposed average coefficient."},
      {"from_key": "interval", "to_key": "constants", "kind": "depends_on", "rationale": "The sharp interval formulas use the same Poincare and Cheeger conventions."},
      {"from_key": "simplex", "to_key": "interval", "kind": "depends_on", "rationale": "After explicit disintegration each edge fiber is a uniform interval; its sharp interval coefficient is applied at its actual length."},
      {"from_key": "parent", "to_existing_logical": EXISTING, "kind": "semantic_association", "rationale": "Updates the audit context of the dated P0017 problem card without refuting its explicitly historical status or declaring a proof independently checked."},
      {"from_key": "triangle-polynomial", "to_key": "simplex", "kind": "depends_on", "rationale": "The exact smooth witness uses dimension two of that whitened simplex and the same edge projection."},
      {"from_key": "triangle-polynomial", "to_key": "averaging-bridge", "kind": "refutes", "rationale": "Exact monomial integration gives 1/2 conditional variance and 1/3 directional energy, contradicting the proposed mean coefficient 12/pi^2, with the full energy separately accounted for."}
    ]
    bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w356",
              "bundle_slug": "p0017-simplex-fiber-referee-20261010-001", "entries": entries, "relations": relations}
    keys = {e["key"] for e in entries}
    allowed_kinds = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
    for e in entries:
        assert e["source"]["license"].startswith("owner-own-work")
        assert (bool(e["proof_text"]) if e["kind"] in ("lemma", "theorem") else e["proof_text"] is None)
    for relation in relations:
        assert relation["from_key"] in keys and relation["kind"] in allowed_kinds
        assert relation.get("to_key") in keys if "to_key" in relation else relation["to_existing_logical"] == EXISTING
    graph = {k: [] for k in keys}
    for r in relations:
        if r["kind"] == "depends_on":
            graph[r["from_key"]].append(r["to_key"])
    def walk(key, chain):
        assert key not in chain, "cycle in depends_on"
        for other in graph[key]:
            walk(other, chain | {key})
    for key in keys:
        walk(key, set())
    save("drafts/bundle_001.json", bundle)
    proof_sources = {e["key"]: {"artifact": ("SOURCE_STATUS.json" if e["key"] in ("constants", "parent") else "PEER_REVIEWS.jsonl" if e["key"] in ("interval", "triangle-polynomial") else "SIMPLEX_FIBERS.md"),
                                 "reviewed": e["key"] in ("interval", "triangle-polynomial"), "independent_reviewer": "w356" if e["key"] in ("interval", "triangle-polynomial") else "w359 (pending)"}
                     for e in entries}
    save("review_packet/ENTRY_REVIEW_STATES.json", proof_sources)
    by_key = {e["key"]: e for e in entries}
    historical_statement = "Is there a universal positive lower bound for the Euclidean Cheeger constant of every isotropic log-concave probability measure, in every dimension?"
    with (ROOT / "review_packet/RELATION_EVIDENCE.jsonl").open("w", encoding="utf-8") as stream:
        for r in relations:
            stream.write(json.dumps({"relation": r, "from_statement_quoted": by_key[r["from_key"]]["statement"],
                "to_statement_quoted": by_key[r["to_key"]]["statement"] if "to_key" in r else historical_statement,
                "evidence": proof_sources[r["from_key"]]["artifact"], "state": "prepared; not ingested"}, ensure_ascii=False) + "\n")
    text = (ROOT / "drafts/bundle_001.json").read_text(encoding="utf-8")
    live = "~/math-brain-inbox/w356/bundle_001.json"
    patch = "".join(difflib.unified_diff([], text.splitlines(keepends=True), fromfile="a/" + live, tofile="b/" + live))
    (ROOT / "patches").mkdir(exist_ok=True)
    (ROOT / "patches/01_p0017_draft.diff").write_text(patch, encoding="utf-8")
    receipts = []
    for worker in ("w354", "w355"):
        for name in (("CLAIMS.jsonl", "ATTEMPT.md", "SIMPLEX_PROOF.md") if worker == "w354" else ("CLAIMS.jsonl", "ATTEMPT.md")):
            path = Path("~/brain_workers") / worker / name
            raw = path.read_bytes()
            receipts.append({"path": str(path), "sha256": hashlib.sha256(raw).hexdigest(),
                             "scope": "reviewed peer artifact only; not a bundle digest or proof receipt"})
    save("review_packet/PEER_ARTIFACT_RECEIPTS.json", receipts)
    save("DRAFT_VALIDATION.json", {"result": "PASS", "entries": len(entries), "relations": len(relations),
        "keys_resolve": True, "depends_on_acyclic": True, "proof_text_conventions": True,
        "license_prefixes": True, "measurement_receipt": "MEASUREMENTS.json",
        "is_mathematical_proof": False, "integrator_run": False})
    save("SUBMISSION_STATE.json", {"prepared": True, "submitted": False, "reviewed": False, "ingested": False,
        "retrievable": False, "local_draft": str(ROOT / "drafts/bundle_001.json"), "destination": live,
        "own_result_reviewer": "w359", "review_request_sent": False})
    print(json.dumps({"result": "PASS", "entries": len(entries), "relations": len(relations), "draft": "drafts/bundle_001.json"}))


if __name__ == "__main__":
    main()
