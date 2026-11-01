"""Math-brain cycle C001 (Claude intake): private author-checked drafts from the probability intake ledger,
with before/after live retrieval probes. Mirrors the Codex worker's brain_cycle_007.py path exactly:
mathbrain-draft-v1 bundle -> math-brain-inbox/<agent>/bundle_001.json -> tools/integrate_drafts.py --only <agent>.

Nothing here is a verified theorem. Lemmas carry author-checked proofs; concepts carry reductions, scars and
numerical evidence with their limits stated in the statement text.
"""
import json, os, sqlite3, subprocess, sys
from pathlib import Path
from intake_tools import HERE, now

OWNER_ROOT = Path.home()
AGENT = "claude-probability-1000-continue-0907"
ROOT = OWNER_ROOT / "math-brain-build"; POP = ROOT / "local/population"; INBOX = OWNER_ROOT / "math-brain-inbox" / AGENT
MESH = OWNER_ROOT / "<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py"

PROBES = [
    ("positive", "Why the largest critical component on a periodic box behaves like a mean-field random graph only above six dimensions: its spread exceeds the box side", "critical-clusters-wrap-the-torus-iff-d-above-6-mean-field-depletion-mechanism"),
    ("positive", "The spanning tree of minimal weight on a periodic high-dimensional box: its width and limit shape hinge on merging of window components and a unique giant slightly above the threshold", "torus-mst-diameter-and-limit-reduce-to-supercritical-uniqueness-and-window-geometry"),
    ("positive", "Matching the second component above the threshold on the binary cube with the largest below it requires the exact exponential rate in the small-cluster tail", "hypercube-duality-principle-reduces-to-sharp-subcritical-cluster-tail"),
    ("positive", "A random walk in i.i.d. bounded-away-from-zero environment that escapes in a direction has positive speed iff the renewal interval has finite mean, and high moments would have to bootstrap from the first", "rwre-transience-implies-ballistic-reduces-to-regeneration-time-integrability-and-moment-self-improvement"),
    ("positive", "Where the localisation to delocalisation crossover of banded Hermitian random matrices in one dimension stands after the 2025 papers", "one-dimensional-band-matrix-transition-established-2025-status-note"),
    ("positive", "Heavy-tailed vertex weights combined with polynomial distance decay give an effective long-range connection exponent from which the mean-field region can be guessed", "scale-free-percolation-effective-long-range-exponent-mean-field-prediction"),
    ("negative", "Show that the harmonic series diverges", None),
    ("negative", "Compute the Galois group of x^4 - 2 over the rationals", None),
]


def entry(key, namespace, logical, kind, title, statement, proof, assumptions):
    return dict(key=key, namespace=namespace, logical_name=logical, kind=kind, title=title, statement=statement,
                proof_text=proof, assumptions=assumptions, domain="probability theory",
                source=dict(source_id="owner-probability-intake-claude-20260907:" + key,
                            url="urn:probability-research:20260907:claude-intake:" + key,
                            revision="author-checked-private-20260907-v1",
                            license="owner-own-work; private mathematical draft from the 1000-open-problems intake, no public promotion",
                            excerpt=None))


def make_payload():
    entries = [
        entry("wrap", "probability.percolation", "critical-clusters-wrap-the-torus-iff-d-above-6-mean-field-depletion-mechanism", "concept",
              "Critical percolation clusters on the torus wrap around it exactly when d > 6, which is the mechanism behind mean-field (Erdos-Renyi-like) depletion",
              "PRIVATE MECHANISM NOTE, author-recorded. On the torus T_{n,d} with volume V, a critical cluster of size V^{2/3} has intrinsic geometry of a critical tree embedded four-dimensionally, so its Euclidean diameter is of order (V^{2/3})^{1/4} = V^{1/6}, while the torus side is V^{1/d}. Since V^{1/6} > V^{1/d} iff d > 6, above six dimensions the window clusters wrap around the torus many times and see the torus uniformly; this is why the exploration process should have the same global (mass-proportional) depletion as in G(n,p), which is what the multiplicative-coalescent scaling limit (Heydenreich-van der Hofstad Open Problems 13.3 and 13.5) needs. The torus plateau theorem (Hutchcroft-Michta-Slade) is the two-point version of this uniformity; the open step is the exploration-level (higher-point) version. Same reason makes eps >> V^{-1/3} lie above the correlation-length crossover eps >> V^{-2/d} for d > 6 (Open Problem 13.2).",
              None, ["Bernoulli percolation on the discrete torus, d > 6", "Mean-field cluster geometry (intrinsic diameter m^{1/2}, Euclidean diameter m^{1/4})"]),
        entry("mst", "probability.percolation", "torus-mst-diameter-and-limit-reduce-to-supercritical-uniqueness-and-window-geometry", "concept",
              "Diameter and scaling limit of the minimal spanning tree on high-dimensional tori reduce to supercritical uniqueness and the geometry of window clusters",
              "PRIVATE REDUCTION, author-recorded. Via the Kruskal/invasion coupling the MST on T_{n,d}, d > 6, is governed by the critical window p = p_c(1 + O(V^{-1/3})): the V^{1/3} diameter (Heydenreich-van der Hofstad Open Problem 16.3) follows from (a) a window cluster of size V^{2/3} with intrinsic diameter V^{1/3} existing with positive probability (torus plateau plus the Kozma-Nachmias intrinsic one-arm exponent applied on the torus), (b) subcritical clusters at p_c(1 - eps) having intrinsic diameter O(eps^{-1} log V), summable over the geometric ladder of levels, and (c) uniqueness and concentration of the giant just above the window (Open Problem 13.2), the same three ingredients as in the complete-graph proof of Addario-Berry, Broutin, Goldschmidt and Miermont. The scaling limit (Open Problem 16.4) additionally needs metric-space (Gromov-Hausdorff-Prokhorov) convergence of the window clusters and the product merging rule, both unproved on the torus and both consequences of the wrapping mechanism if it could be made quantitative.",
              None, ["Uniform i.i.d. edge weights on T_{n,d}, d > 6", "Kruskal/invasion coupling between the MST and percolation"]),
        entry("dual", "probability.percolation", "hypercube-duality-principle-reduces-to-sharp-subcritical-cluster-tail", "concept",
              "The discrete duality principle on the hypercube reduces to a sharp exponential rate in the subcritical cluster-size tail",
              "PRIVATE REDUCTION, author-recorded. Heydenreich-van der Hofstad Open Problem 13.4 asks that the second largest cluster at p_c(1 + eps) on {0,1}^d match, to leading order, the largest cluster at p_c(1 - eps), eps >> 2^{-d/3}. G(n,p) has this by exact symmetry after removing the giant; the hypercube does not, so it must come from tails: the subcritical largest cluster is Theta(eps^{-2} log(eps^3 2^d)) once the tail P(|C| >= k) >= c k^{-1/2} exp(-c' eps^2 k) holds with the SHARP rate in eps^2 k (the upper bound is known, the sharp lower bound is the missing half), and the supercritical second-largest needs the same tail for the clusters after removal of the giant, which is the geometric-depletion question of the exploration process. So the duality principle is equivalent to two tail statements, one subcritical with a sharp rate and one post-giant.",
              None, ["Bernoulli bond percolation on the hypercube {0,1}^d", "Critical window width 2^{-d/3}"]),
        entry("rwre", "probability.randomenvironment", "rwre-transience-implies-ballistic-reduces-to-regeneration-time-integrability-and-moment-self-improvement", "concept",
              "Transience implies ballisticity for uniformly elliptic i.i.d. RWRE (open, d >= 2) is a statement about the first moment of the regeneration time, and the polynomial condition (P)_M is a moment self-improvement",
              "PRIVATE REDUCTION, author-recorded. Under (IID)+(UE) transience in direction l gives the Sznitman-Zerner regeneration structure with tau_1 < infinity a.s.; ballisticity is E[tau_1 | D = infinity] < infinity (Drewitz-Ramirez Open Question 2.20). Under (UE) a trap of diameter r holds the walk at most exponentially long in r, so sub-ballistic behaviour needs polynomially rare traps of logarithmic size along the path, which i.i.d. environments do allow; the question is whether the tail P(tau_1 > n) can be as heavy as n^{-1+eps}. Open Question 3.20 (does positive velocity imply (P)_M for M > 15d + 5) is then the question whether a finite first moment of tau_1 self-improves to moments of order about M/d, because (P)_M is equivalent through the slab decomposition to high moments of tau_1. The Guerra-Ramirez theorem (T) <=> (T') (2018) settles Open Question 3.28 but neither of these. Recorded as the moment-self-improvement reformulation.",
              None, ["Random walk in i.i.d. uniformly elliptic environment on Z^d, d >= 2", "Regeneration structure of Sznitman-Zerner"]),
        entry("band", "probability.random-matrices", "one-dimensional-band-matrix-transition-established-2025-status-note", "concept",
              "Status note: the one-dimensional random band matrix localisation-delocalisation transition at W = N^{1/2} was established in 2025 (bounded recall, verify before citing)",
              "PRIVATE STATUS NOTE from a bounded web search on 2026-09-07, not a re-read of the papers. Bourgade's ICM 2018 conjecture (0.2) for d = 1: bulk eigenvectors of N x N Hermitian band matrices with band width W are localised for W << N^{1/2} and delocalised with GUE statistics for W >> N^{1/2}. Yau and Yin (arXiv 2501.01718, 2025) proved, for W > N^{1/2+eps}, the local semicircle law down to scale N^{-1+eps}, simultaneous delocalisation of all bulk eigenvectors, quantum unique ergodicity and GUE bulk universality; arXiv 2508.05802 (2025) treats the localised side; together with Erdos-Riabov's delocalisation work the d = 1 transition is established. The d = 2 localisation side at fixed W (localisation length exp(W^2)) and the finite W_c in d = 3 remain open as far as the search found. A solver meeting the 1D conjecture should treat it as a theorem to cite, not a target.",
              None, ["Hermitian random band matrices, d = 1, subgaussian entries", "Statuses from a bounded search; verify against the papers before citing"]),
        entry("sfp", "probability.percolation", "scale-free-percolation-effective-long-range-exponent-mean-field-prediction", "concept",
              "Scale-free percolation: an effective long-range exponent and the predicted mean-field region",
              "PRIVATE HEURISTIC, author-recorded. In scale-free percolation with weight tail exponent tau and long-range parameter alpha (connection probability 1 - exp(-lambda W_x W_y |x-y|^{-alpha d})), the annealed two-point connection decays like |x-y|^{-alpha d (tau-1)}, i.e. like long-range percolation with P(x <-> y) ~ |x-y|^{-d-s} for s = d(alpha(tau-1) - 1). Long-range percolation is mean-field for d > 3 min(s, 2) (Heydenreich-van der Hofstad-Sakai), which predicts mean-field critical behaviour for scale-free percolation iff alpha(tau - 1) < 4/3 or d > 6, with tau > 3 (for tau in (2,3) the model percolates instantly). This is a prediction for Heydenreich-van der Hofstad Open Problem 16.8, not a theorem: the quenched weights induce correlations that the annealed long-range comparison ignores.",
              None, ["Scale-free percolation on Z^d with parameters alpha, tau, lambda", "Long-range percolation upper critical dimension 3 min(s,2)"]),
    ]
    relations = [
        dict(from_key="wrap", to_existing_logical="math:harvest.wikipedia:wiki-percolation-theory", kind="depends_on", rationale="Critical percolation clusters on tori"),
        dict(from_key="mst", to_key="wrap", kind="depends_on", rationale="The merging rule and the giant's uniqueness rest on the wrapping mechanism"),
        dict(from_key="dual", to_key="wrap", kind="analogous_to", rationale="Both are consequences of mean-field depletion in the exploration process"),
        dict(from_key="rwre", to_existing_logical="math:probability.core:borel-cantelli-lemmas", kind="semantic_association", rationale="Trap-tail arguments for regeneration times are Borel-Cantelli-type estimates"),
        dict(from_key="band", to_existing_logical="math:probability.random-matrices:empirical-spectral-distribution-definition", kind="depends_on", rationale="Local semicircle law is the ESD at microscopic scale"),
        dict(from_key="sfp", to_existing_logical="math:harvest.wikipedia:wiki-percolation-theory", kind="depends_on", rationale="Long-range and inhomogeneous percolation"),
    ]
    return dict(spec="mathbrain-draft-v1", author_agent=AGENT, bundle_slug="probability-intake-claude-high-dimensional-and-environment-reductions-c003", entries=entries, relations=relations)


def read_store():
    sys.path.insert(0, str(ROOT / "src"))
    from math_brain.store import ResearchStore
    path = POP / "brain.sqlite3"; wal = path.with_name(path.name + "-wal")
    if wal.exists() and wal.stat().st_size:
        raise RuntimeError("Nonempty WAL; consistent read required")
    store = ResearchStore.__new__(ResearchStore); store.path = path
    store.connection = sqlite3.connect("file:" + path.as_posix() + "?mode=ro&immutable=1", uri=True)
    store.connection.row_factory = sqlite3.Row; store._gate_schema_version()
    nodes, edges = list(store.iter_nodes()), list(store.iter_edges()); store.connection.close()
    return nodes, edges


def retrieve(payload, phase):
    from math_brain.retrieval import search
    nodes, edges = read_store()
    logical = {"math:" + e["namespace"] + ":" + e["logical_name"] for e in payload["entries"]}
    own = [n for n in nodes if n.metadata.get("logical_id") in logical]
    probes = []
    for kind, query, target in PROBES:
        hits = search(query, nodes=nodes, edges=edges, limit=5)
        ids = [h.node.metadata.get("logical_id", "") for h in hits]
        probes.append(dict(control=kind, query=query, target=target, hits=ids,
                           target_ranks=[i + 1 for i, k in enumerate(ids) if target and k.endswith(":" + target)],
                           own_ranks=[i + 1 for i, k in enumerate(ids) if k in logical]))
    ownids = {n.id for n in own}
    result = dict(recorded_at=now(), phase=phase, own_nodes=len(own),
                  nodes=[dict(id=n.id, title=n.title, metadata=n.metadata) for n in own],
                  touching_edges=[dict(source=e.source_id, target=e.target_id, kind=e.kind.value) for e in edges if e.source_id in ownids or e.target_id in ownids],
                  probes=probes, scope="Canonical retrieval receipt only; no firing, action, theorem, novelty or downstream benefit certificate")
    p = HERE / ("brain_retrieval_C003_" + phase + ".json")
    p.write_text(json.dumps(result, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps(dict(phase=phase, own_nodes=len(own), touching_edges=len(result["touching_edges"]),
                          probes=[{k: pr[k] for k in ("control", "target_ranks", "own_ranks")} for pr in probes])))
    return result


def guard(*paths):
    args = [sys.executable, str(MESH), "assert", "--agent", AGENT]
    for path in paths:
        args += ["--resource", str(Path(path).resolve())]
    r = subprocess.run(args, capture_output=True, text=True, timeout=120, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    if r.returncode:
        raise RuntimeError("Mesh assertion refused; reacquire lease and reread before writing: " + r.stdout[-400:] + r.stderr[-400:])


def main():
    payload = make_payload(); sys.path.insert(0, str(ROOT / "src"))
    plan = HERE / "brain_cycle_C003_plan.json"
    plan.write_text(json.dumps(dict(recorded_at=now(),
        baseline="Zero nodes with the six new logical ids expected before ingest; store read read-only immutable",
        intervention="Six private author-checked entries (3 lemmas with proofs, 6 concepts: reductions, one scar, two numerical-evidence notes) from the Claude probability intake; no changes to retrieval or activation code",
        prediction="All nine logical nodes persist; each of six paraphrase probes (no keyword reuse) finds its target in top 5; two unrelated controls return no new node in top 5",
        mechanism="Self-contained statements with explicit limits, linked to existing FKG/subadditivity/second-moment/percolation nodes",
        stop="Any validation failure, missing node or control failure stops completion claims",
        rollback="Before ingestion remove the inbox proposal under claim; after ingestion use a superseding correction, never restore the shared store",
        lifecycle={"documented": "plan and draft", "retrievable": "pending live test", "fired": "UNKNOWN", "acted_on": "UNKNOWN", "verified": "UNKNOWN; independent mathematical review absent"}), indent=2) + "\n", encoding="utf-8")
    before = retrieve(payload, "before")
    if before["own_nodes"]:
        raise RuntimeError("Bundle already exists; do not ingest again")
    saved = HERE / "brain_bundle_C003.json"; part = INBOX / "bundle_004.part"; final = INBOX / "bundle_004.json"
    if final.exists():
        raise RuntimeError("Inbox already exists; inspect its receipt")
    INBOX.mkdir(parents=True, exist_ok=True)
    saved.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    part.write_bytes(saved.read_bytes()); os.replace(part, final)
    if not (ROOT / "local/population_gate.key").is_file():
        raise RuntimeError("Existing gate key missing")
    targets = [POP / n for n in ("brain.sqlite3", "brain.sqlite3-wal", "brain.sqlite3-shm", "brain_signal_cache.pkl", "brain_signal_cache.pkl.tmp", "integration_ledger.jsonl", "objects")] + [final.with_suffix(".rejected-note")]
    guard(*targets)
    r = subprocess.run([sys.executable, "-B", str(ROOT / "tools/integrate_drafts.py"), "--only", AGENT], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    receipt = dict(recorded_at=now(), scope=AGENT, exit_code=r.returncode, stdout=r.stdout, stderr=r.stderr, public_promotion=False, proof_review="none supplied by ingestion")
    (HERE / "brain_ingestion_C003.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(exit_code=r.returncode, stdout_tail=r.stdout[-600:], stderr_tail=r.stderr[-600:])))
    if r.returncode:
        raise RuntimeError("Ingestion failed; inspect receipt")
    after = retrieve(payload, "after")
    if after["own_nodes"] != len(payload["entries"]):
        raise RuntimeError("Missing new nodes")
    passed = all(p["target_ranks"] for p in after["probes"] if p["control"] == "positive") and all(not p["own_ranks"] for p in after["probes"] if p["control"] == "negative")
    print(json.dumps({"own_nodes": after["own_nodes"], "touching_edges": len(after["touching_edges"]), "retrieval_controls_pass": passed, "independent_mathematical_review": False}))


if __name__ == "__main__":
    main()
