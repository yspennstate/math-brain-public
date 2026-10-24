"""Build and validate the local P0043 DRAFT packet; never ingest a store."""
from datetime import datetime, timezone
from pathlib import Path
import difflib
import json

ROOT = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()
def save(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

source_status = {
    "worker": "w435", "target": "P0043", "checked_at": now,
    "exact_statement_file": "STATEMENT.md",
    "model": "iid Bernoulli bond percolation on an infinite connected locally finite quasi-transitive graph with p_c<1",
    "target_conclusion": "No infinite open cluster exists almost surely at p=p_c",
    "current_openness": "UNKNOWN", "full_target_proved_by_this_packet": False,
    "novelty_claim": False,
    "historical_primary_sources": [
        {"url": "https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/978/978-3321-1-PB.pdf",
         "title": "Benjamini and Schramm, Percolation Beyond Z^d (1996)",
         "locator": "Conjecture 4, printed page 75, PDF page 5",
         "quote": "Critical percolation dies in every almost transitive graph (assuming pc < 1).",
         "status": "opened exact historical statement", "model_note": "Original paper uses site percolation; precise bond version below."},
        {"url": "https://arxiv.org/html/1605.05301v1", "title": "Hutchcroft (2016), Critical Percolation on Any Quasi-Transitive Graph of Exponential Growth",
         "locator": "Introduction, unnumbered Benjamini--Schramm conjecture; Theorem 1; Theorem 6",
         "status": "opened exact bond model and hypotheses",
         "exact_hypotheses": ["connected", "locally finite", "quasi-transitive", "p_c<1"],
         "proved_scope": "quasi-transitive graphs of exponential growth", "full_target_certificate": False},
        {"url": "https://arxiv.org/pdf/math/9701227", "title": "Benjamini, Pemantle and Peres, Unpredictable Paths and Percolation",
         "locator": "Section 2, equations (5)--(7), PDF pages 5--6",
         "status": "opened common-edge second-moment method; L2 is a classical rederivation"}
    ],
    "local_records": [
        {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv", "line": 549, "id": "P0043", "status": "dated title only"},
        {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl", "line": 84, "id": "C0084", "source": "heydenreich_hofstad_highd_2017, Open Problem 15.11", "status": "matching exact statement, dated and unreviewed"},
        {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl", "line": 72, "id": "C0084-A001", "method": "growth-class split", "status": "incomplete, critical-susceptibility inference corrected by L5"},
        {"path": "~/brain_workers/teams/W0300_O/TEAM_BOARD.md", "line": 21, "holder": "w344", "target_alias": "C0084"}
    ],
    "recent_primary_claim": {
        "scope_url": "https://github.com/openai/math/blob/main/lean/docs/213.md",
        "paper_url": "https://github.com/openai/math/blob/main/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf",
        "status": "full-solution claim encountered; paper and actual formal solution not verified",
        "comparator_url": "https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/CriticalPercolation.lean",
        "theorem": "OAI.CriticalPercolation.BondGraph.no_percolation_at_criticality",
        "comparator_locator": "lines 47--53", "observed_proof_body": "by sorry",
        "scope_note": "A comparator specifies the target. Its placeholder is not evidence that the repository has no separate solution.",
        "actual_solution_module": None, "formal_check_receipt": None, "trusted_axioms": None,
        "novelty_or_current_openness_certified": False
    },
    "owner_work_check": {
        "paths_searched": ["~/Big Open problem in probability theory/notes", "~/Big Open problem in probability theory/paper"],
        "status": "targeted hits concern nonamenable p_c<p_u and L2-gap work; no complete P0043 solution certified",
        "completeness": "bounded search only"
    },
    "proof_scar": "perceptron_proof_open_gaps_fleet_2026_07_12",
    "independent_reviewer": "w437", "independent_review_status": "pending"
}
save("SOURCE_STATUS.json", source_status)

def source(key):
    return {"source_id": "owner-own-work:w435:P0043:"+key,
            "url": "file:///~/brain_workers/w435/ATTEMPT.md",
            "revision": "2026-10-10-author-proof-awaiting-w437",
            "license": "owner-own-work (campaign rederivation; no novelty claim)", "excerpt": None}

def entry(key, logical, title, statement, assumptions, kind="concept"):
    return {"key": key, "namespace": "probability.percolation", "logical_name": logical,
            "kind": kind, "title": title, "statement": statement, "proof_text": None,
            "assumptions": assumptions, "domain": "probability", "source": source(key)}

entries = [
    entry("target", "critical-quasi-transitive-bond-percolation-target-p0043",
          "DRAFT target: no infinite critical cluster on quasi-transitive graphs",
          "Historical conjectural target P0043: if G is an infinite connected locally finite quasi-transitive graph with bond threshold p_c(G)<1, then iid Bernoulli bond percolation on G at p_c has no infinite component almost surely. Current openness is UNKNOWN in this packet; a recent public solution claim has not been verified. This entry is a target, not a proof.",
          ["G infinite, connected, locally finite, quasi-transitive", "iid Bernoulli bond percolation", "p_c(G)<1"]),
    entry("energy", "simple-ray-common-edge-energy",
          "Common-edge energy of a measure on simple rays",
          "For a Borel probability measure mu on infinite simple rays starting at o in a locally finite graph H, let K(gamma,gamma') be the number of shared undirected edges of two independent rays sampled from mu. For 0<r<1 define I_r(mu)=E[r^{-K}], with r^{-infinity}=infinity. Edge labels, rather than shared vertices, determine K for bond percolation.",
          ["Borel probability mu on infinite simple rays from o", "H locally finite", "0<r<1"], "definition"),
    entry("fragility", "quenched-threshold-one-for-critical-bond-components",
          "DRAFT auxiliary: critical components have quenched threshold one",
          "Author-derived auxiliary statement, awaiting independent review: on any countable connected locally finite graph G with p_c(G)>0, almost surely every infinite component C of iid Bernoulli(p_c(G)) bond percolation satisfies p_c(C)=1 for independent bond thinning on the fixed graph C. This is consistent with an infinite critical component and does not by itself prove critical extinction.",
          ["G countable, connected, locally finite", "iid Bernoulli bond states", "p_c(G)>0"]),
    entry("criterion", "finite-common-edge-energy-implies-bond-survival",
          "DRAFT auxiliary: finite ray energy gives percolation survival",
          "Classical second-moment criterion, rederived by the author and awaiting independent review: let H be connected and locally finite, mu a Borel probability on infinite simple rays from o, and 0<r<1. If I_r(mu)<infinity, then iid Bernoulli(r) bond percolation on H satisfies P_r(o connects to infinity)>=1/I_r(mu)>0. The normalized open-prefix second moment uses the number of shared edges, because two length-n prefixes have 2n-K_n distinct edges in their union.",
          ["H connected, locally finite", "mu Borel probability on infinite simple rays from o", "0<r<1", "I_r(mu)<infinity"]),
    entry("cutset", "ray-common-edge-energy-cutset-obstruction",
          "DRAFT auxiliary: cutsets obstruct finite ray energy",
          "Author-derived auxiliary statement, awaiting independent review: for a ray measure mu with finite I_r, the averaged signed ray traversals form a unit flow f from o to infinity with sum_e f(e)^2 <= (I_r-1)/(r^{-1}-1). For pairwise edge-disjoint boundaries D_j of finite vertex sets containing o, I_r >= 1+(r^{-1}-1)sum_j 1/|D_j|. Therefore no subgraph of the nearest-neighbor square lattice supports such a measure with I_r finite for r<1, since square boundaries have 8j+4 edges and the reciprocal sum diverges.",
          ["mu Borel probability on infinite simple rays from o in a locally finite graph", "0<r<1", "D_j pairwise edge-disjoint finite edge boundaries surrounding o"]),
    entry("tree", "square-generation-tree-positive-critical-bond-survival",
          "DRAFT control: critical survival without quasi-transitivity",
          "Author-derived explicit counterexample, awaiting independent review: in the rooted tree T whose depth-(n-1) vertices have four children when n is a positive perfect square and two children otherwise, maximum degree is five, p_c(T)=1/2, and P_{1/2}(o connects to infinity)>=2/7. The uniform-ray common-edge energy at r=1/2 is 7/2. The unique degree-four root fixes infinitely many distance orbits, so T is not quasi-transitive. This refutes removing quasi-transitivity from P0043 and does not refute P0043.",
          ["Rooted spherically symmetric tree with b_n=4 at positive square n, b_n=2 otherwise", "iid Bernoulli bond percolation"]),
    entry("susceptibility", "regular-tree-critical-susceptibility-diverges-with-extinction",
          "DRAFT correction: critical extinction does not make susceptibility finite",
          "Classical regular-tree computation, rederived by the author and awaiting independent review: for the infinite d-regular tree, d>=3, p_c=1/(d-1), all critical bond clusters are finite almost surely but chi_o(p_c)=E|C_o|=infinity. The expected critical open count within graph distance N of o equals 1+Nd/(d-1). Thus subcritical finite susceptibility cannot be extended to p=p_c without another argument; Hutchcroft's exponential-growth proof uses finiteness for p<p_c.",
          ["Infinite d-regular tree, d>=3", "iid Bernoulli bond percolation", "p=1/(d-1)"]),
    entry("gap", "critical-cluster-ray-energy-construction-gap-p0043",
          "DRAFT unresolved gap: constructing a robust critical-cluster ray measure",
          "Unproved route requirement: for a graph class where finite ray energy is possible, deduce from quasi-transitivity and a hypothetical infinite critical component that the component supports some ray measure mu with I_r(mu)<infinity for r<1. Critical thinning fragility would then give a contradiction. The required construction is missing. It cannot be a universal recurrent-graph construction, and a good measure on the host graph does not automatically transfer to a critical component. P0043 is not proved by this route.",
          ["P0043 hypotheses", "Hypothetical infinite critical component", "A graph class where recurrence does not preclude finite ray energy"])
]
relations = [
    {"from_key": "criterion", "to_key": "energy", "kind": "depends_on", "rationale": "The criterion assumes 'I_r(mu)<infinity'; the definition specifies 'I_r(mu)=E[r^{-K}]' with K counting shared edges."},
    {"from_key": "cutset", "to_key": "energy", "kind": "depends_on", "rationale": "The cutset bound concerns 'a ray measure mu with finite I_r'; the definition supplies the exact common-edge energy."},
    {"from_key": "tree", "to_key": "criterion", "kind": "depends_on", "rationale": "The tree has 'energy at r=1/2 is 7/2'; the criterion yields survival '>=1/I_r(mu)', giving 2/7."},
    {"from_key": "gap", "to_key": "fragility", "kind": "depends_on", "rationale": "The gap says 'Critical thinning fragility would then give a contradiction'; fragility says each critical component has 'p_c(C)=1'."},
    {"from_key": "gap", "to_key": "criterion", "kind": "depends_on", "rationale": "The gap requires 'I_r(mu)<infinity for r<1'; the criterion then gives positive r-thinning survival on that component."},
    {"from_key": "fragility", "to_key": "target", "kind": "semantic_association", "rationale": "Fragility is a necessary property of hypothetical critical components; the target asks whether those components are absent. No equivalence is asserted."},
    {"from_key": "susceptibility", "to_key": "target", "kind": "semantic_association", "rationale": "The regular-tree computation has 'all critical bond clusters are finite' and 'chi_o(p_c)=infinity'; it blocks a finite-susceptibility inference in an earlier attempt at the target."}
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w435",
          "bundle_slug": "p0043-thinning-ray-energy-route-001", "entries": entries, "relations": relations}
save("draft_bundle_001.json", bundle)

# Static offline schema, licensing, references and dependency-cycle checks.
required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
keys = {e["key"] for e in entries}
assert len(keys) == len(entries) <= 200
for e in entries:
    assert required <= e.keys()
    assert e["kind"] in ("concept", "definition") and e["proof_text"] is None
    assert e["source"]["license"].startswith("owner-own-work")
    assert all(e[k] for k in ("key", "namespace", "logical_name", "title", "statement"))
adj = {k: [] for k in keys}
for rel in relations:
    assert rel["from_key"] in keys and rel["to_key"] in keys
    assert rel["kind"] in {"depends_on", "semantic_association"}
    assert rel["rationale"]
    if rel["kind"] == "depends_on":
        adj[rel["from_key"]].append(rel["to_key"])
def visit(k, stack):
    assert k not in stack
    for child in adj[k]:
        visit(child, stack | {k})
for k in keys:
    visit(k, set())
claims = [json.loads(s) for s in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
for c in claims:
    assert {"statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"} <= c.keys()
assert not any(c["status"] == "independently checked proof" for c in claims)
metrics = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
assert metrics["status"] == "PASS"
save("VALIDATION.json", {"status": "PASS", "checked_at": now,
    "entries": len(entries), "relations": len(relations), "claim_rows": len(claims),
    "lemma_or_theorem_entries": 0, "dependency_cycle": False,
    "local_schema_checks_only": True, "live_integrator_run": False,
    "mathematical_audit_complete": False, "numerical_checks": metrics["checks_passed"]})

patchdir = ROOT / "patches"
patchdir.mkdir(exist_ok=True)
text = (ROOT / "draft_bundle_001.json").read_text(encoding="utf-8")
diff = "".join(difflib.unified_diff([], text.splitlines(keepends=True),
       fromfile="a/math-brain-inbox/w435/bundle_001.json", tofile="b/math-brain-inbox/w435/bundle_001.json"))
(patchdir / "01_p0043_draft_bundle.diff").write_text(diff, encoding="utf-8")
if not (ROOT / "SUBMISSION.json").exists():
    save("SUBMISSION.json", {"prepared": {"state": True, "at": now},
        "submitted": {"state": False}, "reviewed": {"state": False, "reviewer": "w437"},
        "ingested": {"state": False}, "retrievable": {"state": False},
        "claim_id": "clm-ea8e60bfc9", "claim_expires_at": "2026-10-10T06:16:02Z"})
print(json.dumps({"status": "PASS", "draft_entries": len(entries), "relations": len(relations),
                  "claim_rows": len(claims), "numerical_checks": metrics["checks_passed"]}))
