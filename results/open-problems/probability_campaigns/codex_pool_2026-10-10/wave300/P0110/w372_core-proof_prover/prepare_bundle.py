"""Prepare only a draft packet; no store ingestion or cryptographic ceremony."""
from __future__ import annotations
import datetime
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
INBOX = pathlib.Path("~/math-brain-inbox/w372")
SOURCE = {"source_id": "owner-own-work:w372:p0110-cylinder-reduction:2026-10-10",
          "url": "urn:owner-own-work:w372:p0110-cylinder-reduction:2026-10-10",
          "revision": "draft-2026-10-10-v1-pending-w374",
          "license": "owner-own-work; campaign derivation, no novelty claim, independent review pending",
          "excerpt": None}


def entry(key, name, kind, title, statement, assumptions, proof=None):
    return {"key": key, "namespace": "probability.first_passage", "logical_name": name,
            "kind": kind, "title": title, "statement": statement, "proof_text": proof,
            "assumptions": assumptions, "domain": "probability theory", "source": dict(SOURCE),
            "review_status": "pending-w374", "parent_problem_solved": False}


entries = [
    entry("setup", "uniform-one-two-undirected-lattice-fpp-cylinder-setup", "definition",
          "Bounded iid lattice FPP and deterministic cylinder restriction",
          "On undirected nearest-neighbor Z^d, d>=2, assign iid Uniform[1,2] weights. T(x,y) is the minimum total weight over paths from x to y. For an induced finite box C containing a straight n-edge route from x to x+n e_1, T_C is the analogous constrained minimum. The unique unrestricted geodesic exists almost surely. Its deviation D(x,y) is the maximum Euclidean distance from the segment [x,y]. Along these axis endpoints n<=T<=T_C<=2n, and T_C-T vanishes whenever the geodesic is contained in C.",
          ["d>=2", "undirected nearest-neighbor graph", "iid Uniform[1,2] weights"]),
    entry("floor", "uniform-bounded-fpp-origin-edge-variance-floor", "lemma",
          "A uniform variance floor from the origin edges",
          "For iid Uniform[1,2] undirected nearest-neighbor FPP on Z^d, d>=2, Var T(0,v)>=4^{-(4d+1)} for every nonzero lattice v. A minimizing path exists, is unique almost surely, and has at most 2||v||_1 edges. This only certifies the nonnegative lower fluctuation threshold; it does not prove a positive exponent or exponent equality.",
          ["d>=2", "iid Uniform[1,2] weights", "unrestricted undirected FPP"],
          "A coordinate path costs <=2||v||_1; positivity confines all possible minimizing paths to a finite ball and bounds their lengths. Continuous independent weights rule out distinct-path ties. Condition on the exterior of the 2d origin edges. T=min_i(U_i+A_i), where A_i are exterior-measurable route costs avoiding the origin. When all U_i<=5/4, T<=min A_i+5/4; when all U_i>=7/4, T>=min A_i+7/4. Each event has conditional probability 4^{-2d}. Two independent conditional copies and Var X=(1/2)E(X-X')^2 give conditional variance >=4^{-4d}/4. Total variance proves the bound."),
    entry("transfer", "nonnegative-coupling-cylinder-variance-transfer", "lemma",
          "Variance transfer through nonnegative coupling errors",
          "Let F_1,F_2 be identically distributed square-integrable variables with standard deviation s, and G_1,G_2 iid square-integrable variables on the same probability space. Suppose Delta_i=G_i-F_i>=0 have equal means and ||Delta_i||_2<=delta. Then 2(s-2delta)_+^2<=Var(F_1-F_2)<=2(s+2delta)^2. Independence is required only for G_1,G_2, and is not assumed for localization events, errors, or F_1,F_2.",
          ["square integrability", "unconditional independence of G_1,G_2", "identical F marginals and identical G marginals", "nonnegative errors with equal means and the stated L2 bound"],
          "Centering contracts L2, so |sd G_i-s|<=delta. Positivity gives E(Delta_1-Delta_2)^2<=E Delta_1^2+E Delta_2^2<=2delta^2. Both passage-time differences have mean zero; independence gives ||G_1-G_2||_2=sqrt(2)sd G_1. Apply the forward and reverse L2 triangle inequalities, then square."),
    entry("budget", "bounded-fpp-polynomial-localization-variance-budget", "lemma",
          "A sufficient polynomial confinement budget for variance decoupling",
          "Consider two translated axis passage times F_i=T(x_i,x_i+n e_1) in iid Uniform[1,2] undirected FPP, restricted times G_i in translated induced boxes with disjoint deterministic edge sets and containing the straight n-edge routes. If sd F_i>=c n^b and the probability that F_i differs from G_i is <=C n^{-q}, for all sufficiently large n, then q>2(1-b) implies Var(F_1-F_2)/(2Var F_1)->1. Departure of the unique geodesic is a sufficient exceptional event. This is conditional and does not establish confinement.",
          ["iid Uniform[1,2] weights", "translated boxes with disjoint edge sets", "straight axis route contained in each box", "c>0, C<infinity and the two stated bounds for all large n", "q>2(1-b)"],
          "The constrained times are iid because they depend on disjoint deterministic coordinates. For Delta_i=G_i-F_i, 0<=Delta_i<=n and Delta_i=0 off the exceptional event, so ||Delta_i||_2<=n sqrt(p_n). Divide the nonnegative-coupling variance inequalities by 2s_n^2. Their error ratio is at most (sqrt(C)/c)n^{1-q/2-b}, which tends to zero."),
    entry("mean-gap", "fpp-mean-gap-to-cylinder-departure-union-bound", "lemma",
          "Positive mean gaps give a dependence-safe departure bound",
          "For iid Uniform[1,2] undirected FPP on Z^d, let m(x)=ET(0,x), v=n e_1, and C=([-w,n+w] x [-w,w]^{d-1}) intersect Z^d, with n,w positive integers. Assume a>=0, alpha>0, M<infinity and E exp(alpha|T(0,x)-m(x)|/|x|^a)<=M for every nonzero lattice x. If m(z)+m(v-z)-m(v)>=H_n>0 for every z in the l1 ball of radius 2n outside C, then P(the 0-to-v geodesic leaves C)<=3M(4n+1)^d exp(-alpha H_n/[3(3n)^a]). No independence among the three passage times is needed. The positive mean-gap assumption is not proved for this law here.",
          ["the stated iid bounded FPP model", "uniform exponential moment bound", "positive deterministic mean-gap bound on the stated finite vertex set"],
          "A departing geodesic visits one of at most (4n+1)^d deterministic candidate vertices z. At that vertex T(0,v)=T(0,z)+T(z,v). Subtract means: at least one of the three absolute centered fluctuations is >=H_n/3. Their endpoint distances are <=3n. Exponential Markov, translation invariance and a union bound over three events and the deterministic vertex set give the displayed bound."),
    entry("short-endpoints", "uniform-bounded-fpp-zero-wandering-at-short-axis-endpoints", "lemma",
          "Short endpoints obstruct a literal all-endpoint wandering lower bound",
          "For iid Uniform[1,2] undirected FPP on Z^d, d>=2, D(0,e_1)=0 for every environment and D(0,2e_1)=0 almost surely. Therefore inf_{v!=0} ED(0,v)/|v|^b=0 for every real b. A lower wandering exponent definition must allow a large-distance cutoff for this candidate. Chatterjee's original (A4) allows that cutoff; an all-nonzero-endpoint version cannot be applied literally to this law.",
          ["iid Uniform[1,2] undirected nearest-neighbor FPP", "d>=2", "D measured from the endpoint segment"],
          "For e_1 the direct edge costs <=2 and alternatives have at least three edges, costing >=3. For 2e_1 the straight two-edge route costs <4 almost surely and every alternative has at least four edges, costing >=4. In both cases the geodesic follows the segment, so its deviation is zero."),
    entry("counterexample", "rare-common-shock-obstructs-localization-only-decoupling", "lemma",
          "Vanishing exceptional probability alone does not certify variance decoupling",
          "For fixed 0<=b<1 and n>=2, take Z_n Bernoulli with p_n=n^{-2(1-b)}, F_1=F_2=n(2-Z_n), G_1=G_2=2n. The G_i are independent constants, n<=F_i<=G_i<=2n, the errors are nonnegative and <=n, and F_i=G_i except on probability p_n->0. Nevertheless Var F_i=n^{2b}(1-p_n) and Var(F_1-F_2)=0. This refutes the abstract inference from vanishing departure probability to decoupling; it is not an iid FPP construction or a KPZ counterexample.",
          ["abstract random variables", "0<=b<1", "n>=2"],
          "Both F_i are the same Bernoulli function, so their difference is identically zero. Constant G_i are independent, and G_i-F_i=n Z_n. Direct Bernoulli moments yield Var F_i=n^2 p_n(1-p_n)=n^{2b}(1-p_n)."),
    entry("global-gap", "iid-fpp-kpz-global-exponent-coincidence-gap", "concept",
          "P0110: unproved global exponent coincidence and local mean-gap input",
          "P0110 asks for one nondegenerate iid undirected lattice FPP law for which the KPZ relation chi=2xi-1 is proved with suitable exponents. For the Uniform[1,2] candidate, the parent input remains UNPROVED: chi_a=chi_b and xi_a=xi_b in Chatterjee's original definitions. Upper thresholds use uniform exponential moments of |T-ET|/|v|^a and D/|v|^a over all nonzero lattice endpoints; lower thresholds use uniform lower powers for Var T and ED over all sufficiently distant lattice endpoints. The local cylinder route additionally lacks a positive mean-gap bound m(z)+m(ne_1-z)-m(ne_1)>=c w^2/n at some sublinear width w. The verified coupling and union-bound reductions prove neither input. Current openness as of the bounded 2026-10-10 source check is UNKNOWN; independent review of this packet is pending.",
          ["one actual iid undirected law", "global endpoint quantifiers", "original sufficiently-large-distance lower cutoffs", "draft gap material only"]),
]

relations = [
    {"from_key": "floor", "to_key": "setup", "kind": "depends_on", "rationale": "The variance floor uses the iid Uniform[1,2] origin edges and unrestricted passage time defined in setup."},
    {"from_key": "budget", "to_key": "transfer", "kind": "depends_on", "rationale": "The budget substitutes delta=n sqrt(p_n) and s_n>=c n^b into the displayed variance-transfer inequalities."},
    {"from_key": "budget", "to_key": "setup", "kind": "depends_on", "rationale": "The axis-route bound n<=T<=T_C<=2n supplies the n-sized nonnegative error."},
    {"from_key": "mean-gap", "to_key": "setup", "kind": "depends_on", "rationale": "Positive weights confine the unrestricted minimizing path to the deterministic l1 ball and identify a departing vertex."},
    {"from_key": "short-endpoints", "to_key": "setup", "kind": "depends_on", "rationale": "Weights between one and two force the short axis geodesics to be straight."},
    {"from_key": "counterexample", "to_key": "budget", "kind": "semantic_association", "rationale": "At q=2(1-b) the counterexample has individual variance of order n^{2b} and zero difference variance, showing why the budget cannot be replaced by p_n->0 for arbitrary couplings."},
    {"from_key": "global-gap", "to_key": "mean-gap", "kind": "semantic_association", "rationale": "The gap card explicitly names the unproved positive mean-gap assumption of this conditional departure lemma and distinguishes it from global exponent equality."},
]

bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w372",
          "bundle_slug": "p0110-dependence-safe-cylinder-reduction-001",
          "entries": entries, "relations": relations}


def validate():
    required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
    keys = {e["key"] for e in entries}
    assert len(keys) == len(entries) <= 200
    for e in entries:
        assert required <= e.keys()
        assert e["source"]["license"].startswith("owner-own-work")
        assert e["review_status"] == "pending-w374"
        assert isinstance(e["statement"], str) and e["statement"]
        if e["kind"] in {"lemma", "theorem"}:
            assert e["proof_text"]
        else:
            assert e["proof_text"] is None
    adjacency = {key: [] for key in keys}
    for relation in relations:
        assert relation["from_key"] in keys and relation["to_key"] in keys
        assert relation["kind"] in {"depends_on", "semantic_association"}
        if relation["kind"] == "depends_on":
            adjacency[relation["from_key"]].append(relation["to_key"])
    def visit(key, active):
        assert key not in active
        for target in adjacency[key]:
            visit(target, active | {key})
    for key in keys:
        visit(key, set())


def main():
    validate()
    text = json.dumps(bundle, indent=2, ensure_ascii=False)+"\n"
    (ROOT / "bundle_001.json").write_text(text, encoding="utf-8")
    INBOX.mkdir(parents=True, exist_ok=True)
    destination = INBOX / "bundle_001.json"
    temporary = INBOX / "bundle_001.json.part"
    if destination.exists() or temporary.exists():
        raise SystemExit("existing inbox file preserved; do not overwrite a submitted draft")
    with temporary.open("x", encoding="utf-8") as f:
        f.write(text)
    temporary.rename(destination)
    state = {"submitted": {"status": "draft-file-present", "path": str(destination),
                            "at": datetime.datetime.now(datetime.timezone.utc).isoformat()},
             "reviewed": {"status": "pending", "reviewer": "w374"},
             "ingested": {"status": "not-requested-by-worker"},
             "retrievable": {"status": "not-verified"},
             "structural_validation": {"entries": len(entries), "relations": len(relations), "passed": True,
                                       "mathematical_audit": False},
             "live_store_modified_by_worker": False, "parent_problem_solved": False}
    (ROOT / "BUNDLE_STATE.json").write_text(json.dumps(state, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(state, indent=2))


if __name__ == "__main__":
    main()
