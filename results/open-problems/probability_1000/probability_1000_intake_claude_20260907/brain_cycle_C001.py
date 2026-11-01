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
    ("positive", "Every one-site conditional occupation probability of a translation-invariant repulsive point process on a finite group is at least a spectral average, so a Bernoulli product law sits below it", "harmonic-mean-product-domination-equivariant-determinantal-finite-group"),
    ("positive", "A stationary point process on the integers whose Fourier symbol only involves multiples of a fixed frequency splits into independent copies on residue classes", "determinantal-symbol-in-k-theta-splits-into-independent-sublattice-copies"),
    ("positive", "Two well separated maxima of a Gaussian field that are both stable under small resampling show that having several summits does not force sensitivity", "two-summit-gaussian-field-has-multiple-peaks-without-chaos"),
    ("positive", "Does the ratio of crossing-arm probabilities across nested annuli on the square grid depend only on the ratio of radii, and what does that buy for the existence of an exponent", "four-arm-exponent-existence-on-square-lattice-needs-scale-invariance"),
    ("positive", "Which partition of n has the most standard tableaux, and is it essentially unique for small n", "maximal-dimension-partition-unique-up-to-conjugation-for-n-at-most-40"),
    ("positive", "Splitting a random subset drawn from a projection kernel into two pieces with prescribed sub-kernel laws is a transportation problem that was feasible in every trial", "union-marginal-coupling-of-projection-determinantal-laws-lp-feasible-evidence"),
    ("positive", "To rule out an infinite critical cluster in the whole space from the half-space result one needs the half-space cluster of the origin to have infinite expected size plus a way to glue across the boundary hyperplane", "critical-percolation-full-space-from-half-space-needs-infinite-susceptibility-and-gluing"),
    ("positive", "Non-Gaussian scaling limit of the three-dimensional spin model reduces to two random current clusters meeting with probability bounded below", "ising-3d-nontriviality-reduces-to-current-intersection-lower-bound"),
    ("positive", "Whether the minimum spanning forest of a Poisson cloud in high dimension is connected follows from no percolation at the critical radius", "poisson-minimal-spanning-forest-high-dimension-single-tree-conditional"),
    ("negative", "Compute the fundamental group of the Klein bottle", None),
    ("negative", "Solve the heat equation on a bounded interval with Dirichlet boundary conditions by separation of variables", None),
    ("negative", "Find the number of primitive roots modulo a prime power", None),
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
        entry("hm", "probability.determinantal", "harmonic-mean-product-domination-equivariant-determinantal-finite-group", "lemma",
              "Harmonic-mean product-measure domination for equivariant determinantal processes on a finite group",
              "PRIVATE AUTHOR-CHECKED DRAFT, no independent review. Let Gamma be a finite group and Q a Gamma-equivariant positive contraction on l^2(Gamma) with 0 < Q < I, and let P_Q be the determinantal probability measure on subsets of Gamma with kernel Q. Let HM(Q) be the harmonic mean of the eigenvalues of Q. Then P_Q stochastically dominates the product Bernoulli measure of density HM(Q), and symmetrically P_Q is dominated by the product measure of density 1 - HM(I - Q). This is strictly weaker than Lyons's Conjecture 5.7 (ICM 2014), which asserts the same with the geometric mean (Fuglede-Kadison determinant) in place of the harmonic mean; the conjecture is the harmonic-to-geometric upgrade, and numerical monotone-coupling linear programs on Z/nZ, n <= 6 (102 random symmetric circulant contractions), satisfy the geometric-mean bound exactly, with density FK(Q) + 0.01 already failing on a tested instance.",
              "Write J = Q(I - Q)^{-1}, so that P_Q(X = A) = det(I - Q) det(J_A) for every A subset Gamma (standard formula for determinantal measures with a strict contraction kernel). For a site e and a configuration B on Gamma minus e, P_Q(e in X | X minus e = B) = P(B union e)/(P(B) + P(B union e)) = s_B/(1 + s_B), where s_B = det J_{B union e}/det J_B is the Schur complement of J_B in J_{B union e}, i.e. s_B = 1/((J_{B union e})^{-1})_{ee}. For positive definite M and S subset S' containing e, ((M_{S'})^{-1})_{ee} >= ((M_S)^{-1})_{ee} (the Schur complement of M_{S'} onto e is the minimum over a larger space of a quadratic form, hence smaller), so s_B is nonincreasing in B and its minimum over B is attained at B = Gamma minus e: s_min = 1/(J^{-1})_{ee} = 1/((I - Q)Q^{-1})_{ee} = 1/((Q^{-1})_{ee} - 1). Equivariance makes Q a convolution operator, diagonalised by the irreducible characters with the eigenvalues lambda_chi repeated with multiplicity dim(chi)^2, and (Q^{-1})_{ee} = (1/|Gamma|) trace(Q^{-1}) = the mean of 1/lambda over the spectrum = 1/HM(Q). Hence s_min = HM/(1 - HM) and the minimal conditional probability of presence is s_min/(1 + s_min) = HM(Q). Holley's inequality with a product measure as the smaller measure reduces to exactly this one-site condition (for nu = Bernoulli(p)^Gamma the Holley condition mu(eta^e) nu(xi_e) >= mu(eta_e) nu(xi^e) for eta >= xi becomes mu(eta^e)/mu(eta_e) >= p/(1-p), i.e. conditional presence probability at least p), so P_Q dominates Bernoulli(HM(Q))^Gamma. Applying the same to the complement process, whose kernel is I - Q and which is again equivariant, gives the upper domination by Bernoulli(1 - HM(I - Q))^Gamma. Numerical check (intake raw/C_lyons_conj57_fk_domination_check.json): on Z/nZ, n = 3..6, 102 random symmetric circulant contractions, the monotone-coupling linear program certifies both dominations with the GEOMETRIC mean with zero violation, and raising the product density above the geometric mean by 0.01 breaks feasibility; the harmonic-mean bound proved here is therefore not sharp, and the geometric mean is the conjectured sharp value.",
              ["Finite group Gamma", "Q Gamma-equivariant with 0 < Q < I (strict contraction, invertible); the boundary cases follow by limits", "Holley's inequality in its product-measure form"]),
        entry("sub", "probability.determinantal", "determinantal-symbol-in-k-theta-splits-into-independent-sublattice-copies", "lemma",
              "A stationary determinantal process whose symbol is a function of k theta is an interleaving of independent copies on the k residue classes",
              "PRIVATE AUTHOR-CHECKED DRAFT, no independent review. Let f : T -> [0,1] be a symbol of the form f(theta) = g(k theta) for an integer k >= 2 and a symbol g, and let P_f be the stationary determinantal process on Z with kernel K(x,y) = f-hat(x - y). Then the restrictions of P_f to the residue classes kZ + j, j = 0..k-1, are independent, and each is (after reindexing the class by Z) the stationary determinantal process P_g. Consequence for Lyons's Question 5.4 (ICM 2014): if g is a trigonometric polynomial of degree m/k and P_g is an (m/k + 1)-block factor of an i.i.d. process, then P_f is an (m+1)-block factor of an i.i.d. process on Z; in particular for m = 2, k = 2 the question has a positive answer because the m = 1 case is known.",
              "The Fourier coefficients of f(theta) = g(k theta) are f-hat(n) = g-hat(n/k) when k divides n and 0 otherwise. Hence K(x,y) = 0 unless x = y mod k, so after grouping Z into the residue classes the kernel is block diagonal. A determinantal measure with a block-diagonal kernel is the product of the determinantal measures of the blocks (every finite-dimensional minor det K_A factorises over the blocks, and the correlation functions determine the law). Within the class kZ + j the kernel is K(kx + j, ky + j) = g-hat(x - y), the kernel of P_g. For the block-factor consequence: if the value at x in class j is a function of the i.i.d. variables at the (m/k + 1) consecutive class positions x, x + k, ..., x + m, then interleaving the k independent constructions, with independent i.i.d. sequences placed on the classes, expresses P_f as a factor of one i.i.d. process on Z whose value at x depends on the variables in the window {x, ..., x + m} of length m + 1.",
              ["f = g(k .) with g a measurable symbol into [0,1]", "Block-diagonal kernels give product measures (correlation functions determine the law)"]),
        entry("peaks", "probability.gaussian", "two-summit-gaussian-field-has-multiple-peaks-without-chaos", "lemma",
              "A Gaussian field with two well-separated summits has multiple peaks but neither chaos nor superconcentration",
              "PRIVATE AUTHOR-CHECKED DRAFT, no independent review. Let n be even, Z_1, Z_2 independent standard Gaussians, (g_i) independent N(0, sigma^2) with sigma small, and X_i = Z_1 + g_i for i <= n/2, X_i = Z_2 + g_i for i > n/2. Then (a) with probability tending to one as sigma -> 0 there are two near-maximal indices with correlation R = 0 (multiple peaks in Chatterjee's sense with deficit |Z_1 - Z_2| of order one), (b) Var(max_i X_i) -> Var(max(Z_1, Z_2)) > 0, so the field is not superconcentrated relative to its variance scale, and (c) the argmax half is determined by sign(Z_1 - Z_2) and is unchanged under Ornstein-Uhlenbeck noise of size t unless t exceeds a level of order |Z_1 - Z_2|, so the field is not chaotic. Hence any multiple-peaks condition that admits two peaks cannot be equivalent to chaos or superconcentration; this refutes the two-peak reading of Chatterjee's open problem 6 in 'Chaos, concentration, and multiple valleys' and leaves the growing-number version open.",
              "(a) The maximisers of the two halves are near Z_1 + max g and Z_2 + max g respectively; the two indices lie in different halves and have covariance 0, so R = 0, while the smaller of the two half-maxima is within |Z_1 - Z_2| + O(sigma sqrt(log n)) of the global maximum. (b) max_i X_i = max(Z_1, Z_2) + O(sigma sqrt(log n)) uniformly, so the variance converges to that of max(Z_1, Z_2), which equals 1 - 1/pi > 0. (c) Under the OU flow X^t = e^{-t} X + sqrt(1 - e^{-2t}) X', the half containing the argmax flips only if the noised difference Z_1^t - Z_2^t changes sign, which requires the noise contribution sqrt(1 - e^{-2t}) (Z_1' - Z_2') to exceed e^{-t}|Z_1 - Z_2|; for fixed Z_1 - Z_2 not 0 this has probability tending to 0 as t -> 0, so the overlap between the maximisers at time 0 and time t tends to 1 as t -> 0 uniformly in n, which is the negation of chaos.",
              ["Gaussian field on n points as specified", "Chatterjee's definitions of multiple peaks, superconcentration and chaos"]),
        entry("arm", "probability.percolation", "four-arm-exponent-existence-on-square-lattice-needs-scale-invariance", "concept",
              "Existence of the four-arm exponent on the square lattice is not a consequence of quasi-multiplicativity alone (a corrected route)",
              "PRIVATE SCAR, author-recorded. A tempting argument: quasi-multiplicativity alpha_4(1,R) asymp alpha_4(1,rho) alpha_4(rho,R) makes f(R) = -log alpha_4(1,R) approximately subadditive in log R, so lim f(R)/log R exists by the de Bruijn-Erdos approximate-subadditivity lemma, giving the four-arm exponent on Z^2. The step is invalid as written: approximate subadditivity needs alpha_4(rho,R) asymp alpha_4(1,R/rho), i.e. dependence on the ratio of radii up to constants (scale invariance up to constants), which on Z^2 is exactly as unproved as the exponent; on the triangular lattice it comes from the SLE(6) computation. What quasi-multiplicativity rigorously gives is alpha_4(1,2^n) asymp prod_{k<n} alpha_4(2^k,2^{k+1}) with each factor bounded between constants by RSW; the exponent exists iff the logarithms of the dyadic factors are Cesaro convergent, which is open. So both the existence and the value (conjecturally 5/4) of the four-arm exponent on Z^2 are open, as the Garban-Steif notes state. Route refuted for the existence claim; do not reuse.",
              None, ["Bernoulli bond percolation on Z^2 at p = 1/2", "RSW crossing estimates and quasi-multiplicativity hold on Z^2"]),
        entry("young", "combinatorics.partitions", "maximal-dimension-partition-unique-up-to-conjugation-for-n-at-most-40", "lemma",
              "For every n <= 40 the partition of n maximising the number of standard Young tableaux is unique up to conjugation",
              "PRIVATE EXHAUSTIVE COMPUTATION, author-checked. For each n <= 40, among all p(n) partitions of n (p(40) = 37338) the maximum of the dimension n!/prod(hooks) is attained either by a single self-conjugate partition (n in {1,3,5,6,8,10,12,15,17,21,23,27,30,34,36,38}) or by exactly one pair of mutually conjugate partitions; no tie between non-conjugate shapes occurs. Since conjugation preserves the hook multiset, dim(lambda) = dim(lambda'), so Romik's question (The surprising mathematics of longest increasing subsequences, Section 1.18) whether the maximal-dimension shape is unique must be read up to conjugation; with that reading it holds for all n <= 40 and is open beyond.",
              "Exact integer enumeration: generate all partitions of n in decreasing-part form, compute the conjugate, the hook lengths h(i,j) = lambda_i - j + lambda'_j - i - 1 and the exact integer n!/prod h, take the maximum and list all maximisers; check that the maximiser set is either a singleton equal to its own conjugate or a conjugate pair. Script and results: intake raw/C_romik_maxdim_n_le_40.json (produced 2026-09-07 with Python integer arithmetic). The dimension identity for conjugates follows from the hook-length formula and the fact that conjugation maps the cell (i,j) to (j,i) with the same hook length.",
              ["Hook-length formula", "Exhaustive enumeration for n <= 40 only; no claim for larger n"]),
        entry("lp", "probability.determinantal", "union-marginal-coupling-of-projection-determinantal-laws-lp-feasible-evidence", "concept",
              "Lyons's union-marginal coupling question: transportation polytope feasible in every tested instance, naive conditional splitting fails",
              "PRIVATE NUMERICAL EVIDENCE, not a proof. Lyons (ICM 2014, Question 2.8) asks whether for H = H_1 (+) H_2 orthogonal in l^2(E) there is a coupling of the determinantal projection measures P_{H_1}, P_{H_2} whose union has law P_H. Since the cardinalities are dim H_1, dim H_2 and dim H almost surely, the union must be disjoint, and the question is the nonemptiness of the transportation polytope with the three marginals. Exact LP (HiGHS, minimum total violation) on 1360 random pairs of orthogonal subspaces with |E| in {3,...,6} over all dimension splits, on generic instances with |E| = 7 and 8, on Fourier-mode subspaces of cycles of length 5..8, and on star-space splits in the edge space of K_4 found a feasible coupling with zero violation every time (intake raw/C_lyons_q28_lp_check.json and _structured.json). A structural observation: the naive rule 'sample X_1 from P_{H_1} conditioned on X_1 subset C, set X_2 = C minus X_1' does NOT reproduce the P_{H_2} marginal in general (checked on |E| = 4), so the coupling, when it exists, is not the conditional splitting. Open: a general construction.",
              None, ["Finite E, orthogonal subspaces H_1, H_2", "Evidence is computational on |E| <= 8 only"]),
        entry("half", "probability.percolation", "critical-percolation-full-space-from-half-space-needs-infinite-susceptibility-and-gluing", "concept",
              "Bootstrapping theta(p_c) = 0 from the half-space result: the two missing inputs",
              "PRIVATE REDUCTION, author-recorded. Barsky-Grimmett-Newman: at p_c(Z^d) the half-space N x Z^{d-1} has no infinite cluster. To conclude theta(p_c) = 0 in Z^d (open for 3 <= d <= 10) one would show that a unique infinite cluster (Burton-Keane) cannot be made of infinitely many finite half-space clusters connected through the boundary hyperplane. In d = 2 this works because the half-plane susceptibility at p_c is infinite. The reduction: theta(p_c) = 0 in Z^d follows from (i) infinite half-space susceptibility at p_c(Z^d), and (ii) a gluing lemma showing that finite half-space clusters linked across the hyperplane force an infinite half-space cluster on one side at a slightly larger parameter. Both (i) and (ii) are open for 3 <= d <= 10; (i) is a natural intermediate target because it is a statement about a single half-space cluster rather than about the full-space cluster.",
              None, ["Bernoulli percolation on Z^d, 3 <= d <= 10", "Barsky-Grimmett-Newman half-space theorem; Burton-Keane uniqueness"]),
        entry("ising", "probability.statmech", "ising-3d-nontriviality-reduces-to-current-intersection-lower-bound", "concept",
              "Non-triviality of the 3D Ising scaling limit reduces to a uniform lower bound on the intersection probability of two random currents",
              "PRIVATE REDUCTION, author-recorded. By Aizenman's random-current identity the four-point Ursell function is expressed through the probability that the currents from x_1 to x_2 and from x_3 to x_4 share a cluster; non-triviality (nonvanishing renormalised coupling) is equivalent to inf over scales L of P(two independent random-current clusters at scale L intersect) > 0. The 4D case is now trivial (Aizenman-Duminil-Copin 2021); in 3D the heuristic is favourable because the current-cluster dimension (5 - eta)/2 = 2.48 exceeds 3/2, so independent fractals of that dimension would intersect with positive probability. A second-moment argument on the number of intersection points reduces the uniform lower bound to (a) a two-point function lower bound with exponent 2 - eps in d = 3 (Duminil-Copin's Conjecture 5, PIMS lectures) and (b) a variance bound on the intersection count, which involves six-point correlations beyond the Lebowitz inequality. Both inputs are open; (b) is the genuinely new obligation.",
              None, ["Nearest-neighbour Ising model on Z^3 at beta_c", "Random-current representation and switching lemma"]),
        entry("msf", "probability.percolation", "poisson-minimal-spanning-forest-high-dimension-single-tree-conditional", "concept",
              "The minimal spanning forest of a Poisson process in high dimension should be a single tree (conditional, opposite to the source's guess)",
              "PRIVATE CONDITIONAL RESOLUTION, author-recorded, sources not re-fetched. Aldous-Steele (2004) ask whether the minimal spanning forest of a homogeneous Poisson process in R^d is connected for d >= 3 and suspect it is not in high dimension. Lyons-Peres-Schramm's criterion (Ann. Probab. 2006) makes the free MSF a single tree when there is no percolation at criticality and the infinite cluster is unique above criticality; for the Poisson-Boolean (Gilbert) model uniqueness above criticality is classical and absence of percolation at the critical radius in high dimensions follows from the lace expansion for the random connection model (Heydenreich-van der Hofstad-Last-Matzke 2019). If the LPS criterion transfers verbatim to Poisson point processes, the MSF IS a single tree for d large, the reverse of the source's suspicion. Two verifications remain: the exact hypotheses of the LPS criterion in the continuum, and the exact statement of the high-dimensional continuum result. Treat as a lead with sign, not a theorem.",
              None, ["Homogeneous Poisson process in R^d, d large", "LPS tree criterion; continuum lace expansion (both to be verified against the papers)"]),
    ]
    relations = [
        dict(from_key="hm", to_existing_logical="math:combinatorics.correlation:fkg-inequality", kind="analogous_to", rationale="Holley's inequality in product-measure form is the domination tool; the FKG lattice form is its sibling"),
        dict(from_key="hm", to_key="lp", kind="analogous_to", rationale="Both concern stochastic comparison of determinantal measures on finite sets via linear programs"),
        dict(from_key="sub", to_key="hm", kind="analogous_to", rationale="Both exploit translation equivariance of the kernel (Fourier diagonalisation)"),
        dict(from_key="peaks", to_existing_logical="math:probability.concentration:borell-tis-inequality", kind="analogous_to", rationale="The variance of the maximum of a Gaussian field is the quantity whose smallness superconcentration asserts"),
        dict(from_key="arm", to_existing_logical="math:analysis.core:fekete-subadditive-lemma", kind="refutes", rationale="Records that the subadditivity route to the exponent fails on Z^2 for lack of scale invariance; the lemma itself is untouched"),
        dict(from_key="arm", to_existing_logical="math:harvest.wikipedia:wiki-percolation-theory", kind="depends_on", rationale="Arm events of critical planar percolation"),
        dict(from_key="half", to_existing_logical="math:harvest.wikipedia:wiki-percolation-theory", kind="depends_on", rationale="Half-space and full-space critical clusters"),
        dict(from_key="ising", to_existing_logical="math:probability.concentration:second-moment-method-and-what-it-does-not-give", kind="depends_on", rationale="The reduction is a second-moment argument on the intersection count and inherits that method's gap"),
        dict(from_key="msf", to_existing_logical="math:harvest.wikipedia:wiki-percolation-theory", kind="depends_on", rationale="Tree criterion is a statement about critical and supercritical percolation of the Gilbert graph"),
        dict(from_key="msf", to_key="half", kind="analogous_to", rationale="Both hinge on absence of percolation at criticality"),
        dict(from_key="young", to_key="lp", kind="analogous_to", rationale="Both are exact finite computations (enumeration, linear programs) offered as evidence for an open conjecture, with the range of the computation stated as the limit of the evidence"),
    ]
    return dict(spec="mathbrain-draft-v1", author_agent=AGENT, bundle_slug="probability-intake-claude-determinantal-percolation-chaos-c001", entries=entries, relations=relations)


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
    p = HERE / ("brain_retrieval_C001_" + phase + ".json")
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
    plan = HERE / "brain_cycle_C001_plan.json"
    plan.write_text(json.dumps(dict(recorded_at=now(),
        baseline="Zero nodes with the nine new logical ids expected before ingest; store read read-only immutable",
        intervention="Nine private author-checked entries (3 lemmas with proofs, 6 concepts: reductions, one scar, two numerical-evidence notes) from the Claude probability intake; no changes to retrieval or activation code",
        prediction="All nine logical nodes persist; each of nine paraphrase probes (no keyword reuse) finds its target in top 5; three unrelated controls return no new node in top 5",
        mechanism="Self-contained statements with explicit limits, linked to existing FKG/subadditivity/second-moment/percolation nodes",
        stop="Any validation failure, missing node or control failure stops completion claims",
        rollback="Before ingestion remove the inbox proposal under claim; after ingestion use a superseding correction, never restore the shared store",
        lifecycle={"documented": "plan and draft", "retrievable": "pending live test", "fired": "UNKNOWN", "acted_on": "UNKNOWN", "verified": "UNKNOWN; independent mathematical review absent"}), indent=2) + "\n", encoding="utf-8")
    before = retrieve(payload, "before")
    if before["own_nodes"]:
        raise RuntimeError("Bundle already exists; do not ingest again")
    saved = HERE / "brain_bundle_C001.json"; part = INBOX / "bundle_002.part"; final = INBOX / "bundle_002.json"
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
    (HERE / "brain_ingestion_C001.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
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
