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
    ("positive", "Adding conductors to a random medium can only raise the effective conductivity, which is the cluster density times the walk's diffusion constant", "effective-conductivity-theta-times-sigma-squared-is-nondecreasing-in-p"),
    ("positive", "Recursive majority of three: a query strategy that reads a leaf with probability five sixths per level, and an influence bound that caps how small any strategy's revealment can be", "iterated-three-majority-revealment-exponent-between-0166-and-0369"),
    ("positive", "Counting points of the deep level set below the field's top equals the extremal measure only if the cluster sizes at large depth are uniformly integrable", "deep-extremal-level-set-conjecture-equivalent-to-cluster-size-limit-given-uniform-integrability"),
    ("positive", "A peeling exploration swallows every boundary vertex eventually exactly when the sum of per-step swallowing chances along the perimeter walk diverges", "filled-in-peeling-exhausts-the-map-iff-swallowing-series-diverges"),
    ("positive", "Convergence of all correlation functions of a random measure to those of a limit determined by its moments forces convergence in law of the measure", "moment-determinate-limit-turns-r-point-convergence-into-measure-convergence"),
    ("positive", "Homogenization of the walk on the vacant set throughout the supercritical regime follows by combining the decoupling framework with the equality of the critical parameters", "vacant-set-quenched-invariance-principle-all-u-from-prs-plus-sharpness"),
    ("negative", "Prove that every bounded monotone sequence of reals converges", None),
    ("negative", "Classify finite simple groups of order less than 100", None),
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
        entry("cond", "probability.percolation", "effective-conductivity-theta-times-sigma-squared-is-nondecreasing-in-p", "lemma",
              "theta(p) sigma^2(p) is nondecreasing in p for random walk on the supercritical percolation cluster",
              "PRIVATE AUTHOR-CHECKED DRAFT, no independent review. For supercritical Bernoulli bond percolation on Z^d let theta(p) be the density of the infinite cluster and sigma^2(p) the diffusion constant of simple random walk on it (quenched invariance principle). Then p -> theta(p) sigma^2(p) is nondecreasing on (p_c, 1]. Monotonicity of sigma^2(p) itself, asked as Open Problem 14.1 in Heydenreich-van der Hofstad's lecture notes, is NOT implied: the lemma only controls the product.",
              "Couple all p at once by i.i.d. uniform edge labels U_e and declare e open at level p iff U_e <= p; increasing p only adds edges. The homogenised conductivity of the random conductance model with conductance 1 on open edges and 0 on closed edges equals a fixed normalising constant times theta(p) sigma^2(p): the effective conductivity per unit volume is the density of the conducting phase times the diffusion constant of the walk on it, closed-edge sites contributing nothing. The homogenised conductivity is the infimum over correctors of the expected Dirichlet energy per unit volume, and adding conductors increases every Dirichlet energy (Rayleigh's monotonicity principle), hence increases the infimum. The normalising constant does not depend on p. Therefore theta(p) sigma^2(p) is nondecreasing. The same argument gives nothing for sigma^2 alone because theta(p) is itself increasing; near p_c the product bound only yields sigma^2(p) >= theta(p') sigma^2(p')/theta(p) for p > p'.",
              ["Supercritical Bernoulli bond percolation on Z^d, d >= 2", "Quenched invariance principle on the infinite cluster (so sigma^2 is defined)", "Homogenised conductivity identity for the conductance model on the cluster"]),
        entry("maj", "probability.boolean", "iterated-three-majority-revealment-exponent-between-0166-and-0369", "lemma",
              "The optimal revealment of iterated 3-majority on 3^k bits decays like n^{-sigma} with sigma in [log(6/5)/log 3, 1 - log 2/log 3]",
              "PRIVATE AUTHOR-CHECKED DRAFT, no independent review. Let f_k be the iterated majority-of-three function on n = 3^k bits. The greedy recursive algorithm (evaluate two random children, the third only if they disagree) has revealment (5/6)^k = n^{-log(6/5)/log 3} = n^{-0.1660}, so the optimal revealment delta(f_k) is at most that. Every leaf has influence 2^{-k} = n^{-log 2/log 3}, and the inequality delta(f) >= Var(f)/(n max_i I_i) (Garban-Steif notes, Theorem VIII.7) gives delta(f_k) >= (2/3)^k = n^{-(1 - log 2/log 3)} = n^{-0.3691}. So the exponent sigma asked for in Exercise VIII.5 of the Garban-Steif notes lies in [0.1660, 0.3691]; the exact value is open.",
              "Greedy revealment: at each level a given child is one of the two evaluated first with probability 2/3, or is the third child with probability 1/3 and is then evaluated only if the first two disagree, which for independent uniform bits happens with probability 1/2; so the probability that a fixed leaf is read is (2/3 + 1/6)^k = (5/6)^k. Influence: flipping a leaf flips the output iff at every level above it the two sibling subtrees disagree, each with probability 1/2 independently across levels, giving 2^{-k}. Theorem VIII.7 of the source for the {-1,1}-valued balanced function (Var f = 1) with n max_i I_i = 3^k 2^{-k} gives delta >= (2/3)^k. Exponents follow from n = 3^k.",
              ["Independent uniform bits", "Revealment is the maximum over leaves of the probability the algorithm reads that leaf", "Garban-Steif Theorem VIII.7"]),
        entry("deep", "probability.gaussian", "deep-extremal-level-set-conjecture-equivalent-to-cluster-size-limit-given-uniform-integrability", "concept",
              "Biskup's Conjecture 16.5 (size of deep extremal level sets of the 2D DGFF) is equivalent to his Conjecture 16.6 given uniform integrability of deep cluster sizes",
              "PRIVATE REDUCTION, author-recorded. By the cluster-process structure of the DGFF extremal process (Biskup-Louidor), the number of points of the level set at depth t inside A is a Poisson sum over extremal local maxima in A of i.i.d. cluster sizes at the corresponding depths, so its conditional expectation given the extremal measure Z^D equals Z^D(A) times the integral over depth of e^{alpha s} E[cluster size at depth s] ds. Conjecture 16.5 (the count normalised by (1/t) e^{-alpha t} converges to c Z^D(A)) therefore reduces to the existence of lim e^{-alpha h} E_nu(f_h) (Conjecture 16.6) plus (i) uniform integrability of cluster sizes at depth t uniformly in N, to exchange the N and t limits, and (ii) a variance bound making the Poisson sum concentrate, which follows from the same uniform integrability. Conversely 16.5 implies the limit in 16.6 by taking expectations. The open content is thus 16.6 together with the uniform-in-N control of deep clusters, which the concentric decomposition delivers only at bounded depth.",
              None, ["2D DGFF in admissible domains; extremal process with Poisson-cluster structure (Biskup-Louidor)", "Exchange of limits requires uniform integrability not currently available"]),
        entry("peel", "probability.planarmaps", "filled-in-peeling-exhausts-the-map-iff-swallowing-series-diverges", "concept",
              "Curien's question (peeling notes, after Corollary 27) is equivalent to a divergence criterion for the perimeter walk of a general critical weight sequence",
              "PRIVATE REDUCTION, author-recorded. For a filled-in peeling exploration of the infinite Boltzmann map with critical weight sequence q, every boundary vertex is eventually swallowed almost surely iff sum_n q_{S_n} = infinity a.s., where S_n is the half-perimeter process (an h-transform of the step walk with law nu) and q_l is the probability that a peeling step at perimeter l swallows at least half of the boundary on a given side. For type a in [3/2, 5/2] the source proves divergence from q_l asymp l^{1-a} and the scaling limit S_n asymp n^{1/(a-1)}. Without a type, the criterion is a recurrence-type statement for the positive test function q along the h-transformed walk; it holds whenever liminf n q_{S_n} is bounded below in probability, so the question reduces to the growth of the h-transformed perimeter walk for non-regularly-varying critical nu. The reduction is rigorous (conditional Borel-Cantelli); the growth control is the open part.",
              None, ["Critical weight sequence q (any type or none)", "Filled-in peeling with any fixed algorithm"]),
        entry("ise", "probability.branching", "moment-determinate-limit-turns-r-point-convergence-into-measure-convergence", "concept",
              "For a moment-determinate limit such as ISE, convergence of all r-point functions of a random probability measure gives convergence in distribution of the measure",
              "PRIVATE OBSERVATION, author-recorded, used to reduce Heydenreich-van der Hofstad Open Problem 15.1. If random probability measures mu_n on R^d have r-point (moment) measures converging weakly to those of a random probability measure mu whose moment measures satisfy a Carleman-type determinacy condition (total masses of order r! K^r), then mu_n converges in distribution to mu: the law of a random probability measure is determined by its moment measures under such a condition, and tightness is automatic on the compact scaling window. Integrated super-Brownian excursion satisfies the condition. Consequently, for spread-out critical percolation in d > 6, Hara-Slade's convergence of the r-point functions conditioned on cluster size n (with the n^{-1/4} spatial scaling at fixed Fourier variable) implies the conditional-measure convergence to ISE asked in Open Problem 15.1, provided the r-point convergence gives weak convergence of the r-point measures (characteristic-function convergence at every bounded Fourier variable suffices). The nearest-neighbour case is not covered (no r-point expansion in d >= 11).",
              None, ["Random probability measures on R^d", "Carleman-type moment determinacy of the limit (holds for ISE)", "Hara-Slade r-point convergence, not re-verified here"]),
        entry("qip", "probability.percolation", "vacant-set-quenched-invariance-principle-all-u-from-prs-plus-sharpness", "concept",
              "Quenched invariance principle on the vacant set of random interlacements for every u < u* as a corollary of Procaccia-Rosenthal-Sapozhnikov plus the 2023 sharpness theorem (conditional)",
              "PRIVATE CONDITIONAL RESOLUTION, author-recorded, sources not re-fetched. Procaccia, Rosenthal and Sapozhnikov (PTRF 2016) prove a quenched invariance principle for random walk on the infinite cluster of correlated percolation models satisfying a polynomial decoupling condition, local uniqueness and a density condition; for the vacant set these were known for u < u** at the time. Duminil-Copin, Goswami, Rodriguez, Severo and Teixeira (2023) prove u* = u** = bar u, so the inputs hold for every u < u*, and the conclusion of PRS should extend to the whole supercritical phase, answering Open Problem 16.7 of Heydenreich-van der Hofstad for the vacant set (the interlacement set itself was already covered for all u > 0). Verification owed: that the decoupling inequalities of the sharpness paper have exactly the PRS form and that constants may depend on u.",
              None, ["Random interlacements on Z^d, d >= 3", "PRS 2016 hypotheses; DGRST 2023 equality of thresholds"]),
    ]
    relations = [
        dict(from_key="cond", to_existing_logical="math:harvest.wikipedia:wiki-percolation-theory", kind="depends_on", rationale="Supercritical cluster and its density"),
        dict(from_key="maj", to_existing_logical="math:combinatorics.correlation:fkg-inequality", kind="semantic_association", rationale="Boolean-function influence and revealment live in the same discrete-Fourier toolbox as correlation inequalities; no logical dependence"),
        dict(from_key="deep", to_existing_logical="math:probability.concentration:borell-tis-inequality", kind="analogous_to", rationale="Extremes of Gaussian fields; the DGFF cluster structure refines the maximum"),
        dict(from_key="ise", to_existing_logical="math:probability.concentration:second-moment-method-and-what-it-does-not-give", kind="analogous_to", rationale="Moment measures as the identifying data of a random object"),
        dict(from_key="qip", to_existing_logical="math:harvest.wikipedia:wiki-percolation-theory", kind="depends_on", rationale="Supercritical vacant set is a correlated percolation cluster"),
        dict(from_key="peel", to_existing_logical="math:probability.core:borel-cantelli-lemmas", kind="depends_on", rationale="The divergence criterion is a conditional Borel-Cantelli statement"),
        dict(from_key="cond", to_key="qip", kind="analogous_to", rationale="Both concern random walk on percolation clusters and the quenched invariance principle"),
    ]
    return dict(spec="mathbrain-draft-v1", author_agent=AGENT, bundle_slug="probability-intake-claude-reductions-and-two-lemmas-c002", entries=entries, relations=relations)


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
    p = HERE / ("brain_retrieval_C002_" + phase + ".json")
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
    plan = HERE / "brain_cycle_C002_plan.json"
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
    saved = HERE / "brain_bundle_C002.json"; part = INBOX / "bundle_003.part"; final = INBOX / "bundle_003.json"
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
    (HERE / "brain_ingestion_C002.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
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
