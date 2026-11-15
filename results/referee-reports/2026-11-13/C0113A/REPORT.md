PARTIAL

# C0113: connectivity of the Poisson Euclidean minimal spanning forest

Task: “Open problem C0113”, received 13 November 2026 at approximately 10:27 +04 (Asia/Tbilisi). Literature checked on 13 November 2026. No unconditional resolution for a Poisson process in any fixed dimension d ≥ 3 was found. This report does not claim one.

The results proved here are (i) precise free/wired and invasion reductions, including a direct Poisson free=wired proof using fixed-parameter uniqueness and the Mecke formula; (ii) a conditional theorem: square summability of the **revealed-cell probabilities** of a specified Poisson invasion exploration implies infinitely many trees; and (iii) an exact finite-box path-confinement criterion, with finite wired certificates. The additional decay hypothesis in (ii) is not established by the continuum lace expansion. These are reductions/conditional results, not a solution of the open problem and not claims of novelty.

## 1. What the source asks

The saved public author preprint is `sources/aldous_steele_objective_2004.txt`, from https://www.stat.berkeley.edu/~aldous/Papers/me101.pdf. Its page numbers 63–64 are the preprint's printed page numbers; the relevant passage is in Section 6.3, headed “A Second Percolation Connection – Forest vs. Tree”. It reports Alexander's planar result, says d ≥ 3 remains open, and expresses the suspicion of disconnection in sufficiently high dimension. **It does not specify a cutoff such as 6, 8, or 19 for the Poisson model.** Its mention of dimension >19 concerns a then-known Bernoulli-percolation theorem used as indirect evidence, not a Poisson MSF disconnection theorem.

Definition 4.2, preprint p.33, keeps e={x,y} of length s exactly when the strict sublevel components C_s(x), C_s(y) are distinct and at least one is finite. This is the **wired** minimal spanning forest. The free definition imposes only distinctness. For the homogeneous Poisson Euclidean model the two agree almost surely, as proved in Section 4 below. Thus the distinction matters for interpreting the definition, but does not give two separate connectivity questions in this model.

Throughout, Π is a homogeneous intensity-one Poisson process on R^d. The graph G_s has vertices Π and edges of Euclidean length strictly less than s. Its critical connection distance is r_c; the Boolean occupied set at this parameter is the union of balls of radius r_c/2. Varying intensity at fixed ball radius and varying connection distance at intensity one are equivalent by dilation. All edge lengths are distinct almost surely. A path in a graph always means a finite path unless explicitly called a ray.

## 2. Literature findings and the gap

### 2.1 Planar proof and the higher-dimensional obstruction

Alexander (1995), Theorem 2.6, p.93, and Example 2.8, pp.93–94, prove connectivity in the Poisson plane. The proof uses the planar Delaunay graph (called the Voronoi graph there), its Voronoi dual, and absence of a critical vacant infinite component. It also uses critical occupied nonpercolation and simultaneous uniqueness to conclude that the resulting tree has one end, through Theorem 2.5(ii), pp.92–93.

Here is the deterministic connectivity argument, with the percolation input separated. Almost surely the Delaunay graph is a proper plane graph with finite degrees and bounded faces. It has the same MSF and the same strict sublevel connectivity as the complete Euclidean graph. To see the latter bottleneck property, traverse a line segment between two sites through the Voronoi tessellation. The successive nearest sites give a Delaunay path whose edge lengths are at most the original segment length: at a switching point at distance t along a segment of length s, both nearest sites are within min(t,s−t), and hence their mutual distance is at most 2 min(t,s−t) ≤ s. Degeneracies can be avoided almost surely (or by an arbitrarily small perturbation). In particular every edge of length <r has a Delaunay replacement using edges <r. Also every MSF edge has an empty relative-neighborhood lune, hence an empty diametral ball, and is a Delaunay edge.

Suppose the forest F has several trees, and let T be one of them. If a Delaunay edge e across T's vertex boundary had length s<r_c, its endpoints would lie in the same finite G_s component (otherwise e itself is in F). The MST of that finite component is contained in F, connecting the endpoints, a contradiction. Thus every edge across the boundary has length at least r_c. Since r_c is deterministic and Poisson pair distances have continuous distributions, almost surely no edge has length exactly r_c, so these lengths are actually greater than r_c. The duals of these boundary edges form a nonempty subgraph with even degrees. It cannot have a finite component: a finite even component has a dual cycle, enclosing primal vertices, and no F edge crosses this cycle. Some infinite F component would then be trapped in a bounded region containing only finitely many sites. Therefore there is an infinite dual boundary component made of edges dual to primal lengths ≥r_c. The corresponding Voronoi edges are at distance at least r_c/2 from every Poisson site, so give an unbounded critical vacant component. Planar critical vacant nonpercolation rules this out. All F components are infinite by the finite-cut argument in Section 4.

The topological fact used here is the usual proper-plane cut/dual-cycle separation: the dual may be embedded through the shared primal edge, and a dual cycle separates primal vertices on its two sides. Infinite components of a proper locally finite embedded graph have unbounded geometric realization. The proper plane graph hypotheses are those of Alexander's Theorem 2.6. This proof is for connectivity; the one-ended conclusion additionally follows from his Theorem 2.5 and critical occupied nonpercolation. In d ≥ 3 the boundary does not supply such a planar vacant dual path, and there is no corresponding contradiction. Uniqueness of the supercritical occupied cluster alone does not make invasion trees meet.

### 2.2 What critical nonpercolation does, and does not, imply

Alexander's Theorem 2.5(ii) says that, under his stationarity/ambiguity/finite-density/simultaneous-uniqueness hypotheses, a two-ended MSF tree would contain the critical infinite cluster. In particular θ(r_c)=0 implies every MSF component is one-ended. Lyons–Peres–Schramm (2006), Theorem 3.12, proves an analogous implication for unimodular quasi-transitive graphs with independent edge labels. It does **not** assert connectivity.

There is no established equivalence here between Poisson MSF connectivity and absence of an infinite critical Boolean cluster. Such an equivalence was not found in the cited sources. The free=wired equivalence in Lyons–Peres–Schramm Proposition 3.6 is instead about almost-everywhere **uniqueness**, not critical nonpercolation. Their Conjecture 6.9 (with p_c<1 added by the 9 September 2024 erratum) concerns p_u and quasi-transitive **nonamenable** graphs; it is not a theorem about Poisson space or Z^d.

A small counterexample to the *general* implication “critical nonpercolation implies wired connectivity” is worth making explicit. Give the 3-regular tree iid uniform edge labels. At p_c=1/2, every outward branch is a critical Binomial(2,1/2) Galton–Watson process and dies out: its extinction equation q=((1+q)/2)^2 has only the solution q=1 in [0,1]. Thus critical percolation has no infinite cluster, including after a countable union over starting vertices. For a fixed edge e with label s>1/2, its two strict-sublevel endpoint branches are independent supercritical Binomial(2,s) processes, each surviving with probability 1−((1−s)/s)^2>0. Therefore e is deleted from the WMSF with probability at least ∫_{1/2}^1[1−((1−s)/s)^2]^2 ds>0. Its endpoints then cannot be connected, since the underlying graph is a tree. This proves that the WMSF is not almost surely connected despite critical nonpercolation. This example concerns an abstract regular tree, not the Poisson problem.

On Z^d with iid continuous nearest-neighbor edge weights, free and wired MSFs coincide by amenability (Lyons–Peres–Schramm Proposition 3.5(c)). Their Question 6.8, p.1689, asks which dimensions give a single tree; Question 6.10 on the same page separately asks whether the number of components must be 1 or infinity. The corrected Lyons–Peres book, version 8 November 2020, Question 11.35, printed p.406, still states the lattice connectivity question and records the competing thresholds 8 and 6. Question 11.19, printed p.400, asks the component-number question. These questions must not be answered by importing results for a different forest.

The Poisson component count is an almost-sure constant in {1,2,…,∞}, by translation ergodicity: the count is a translation-invariant measurable function of Π. This alone does not exclude a finite constant greater than one. The conditional result below proves **infinity**, rather than merely positive probability of two trees. We do not claim the unconditional 1-or-infinity dichotomy for this model from these references.

### 2.3 Newman–Stein and Jackson–Read

Newman–Stein, “Ground State Structure in a Highly Disordered Spin Glass Model” (1996; public preprint adap-org/9505005), has an **unnumbered theorem in Section 5**, preprint pp.9–11: for lattice invasion membership G(z)=P(z is invaded from 0), the condition Σ_z G(z)^2<∞ forces infinitely many disjoint invasion trees. Its proof compares two explorations in the same iid edge environment with two independent environments before their incident edge sets meet, and bounds the independent contact probability by shifted convolutions of G. This is a genuine conditional theorem, not a proof of the required decay of G.

The proposed invasion estimate G(z)≈|z|^{4−d}, motivated by an incipient-cluster dimension of four, makes ΣG² finite when d>8: the radial sum has exponent d−1+2(4−d)=7−d. At d=8 it is logarithmically divergent under this power law. This is the origin of the old threshold, and of the analogy with intersecting random walks. The critical percolation two-point function τ(z)≈|z|^{2−d} is a different function; it cannot simply replace G in this argument.

Jackson–Read (2010), Part I, Section II (especially preprint pp.7–8), explains that close invasion trees have correlated boundary labels that suppress mergers. Their exact mean-field calculation on the wired Bethe lattice gives component dimension six (Section III; conclusion in Section IV, preprint p.17), and their Euclidean scaling prediction is a threshold of six. Part II develops a perturbation expansion at criticality. Neither part proves a finite-dimensional Poisson or Z^d disconnection theorem. Part I contains language describing the earlier d≤8 upper bound as rigorous after assuming invasion dimension four; the original Newman–Stein proof shows explicitly that the quantitative membership/square-summability input is still needed. We use the original theorem's actual hypothesis.

### 2.4 What continuum lace expansion supplies

Heydenreich–van der Hofstad–Last–Matzke, arXiv:1908.11356v4 (2023 revision; published in Ann. Inst. H. Poincaré Probab. Statist. 62 (2026), 1–67), Proposition 1.1(a), preprint pp.4–5, verifies their high-dimensional finite-variance assumptions for the deterministic-ball Boolean connection function. Theorem 1.2, preprint p.5, gives the triangle condition and a Fourier infrared bound in sufficiently large dimension. Theorem 1.3, also p.5, gives γ=1 and θ(λ_c)=0. The Boolean model is included in the sufficiently-large-d branch. Its fixed-range deterministic-ball case is **not** the same as the weak, spread-out connection function L^{−d}h(x/L), for which d>6 and sufficiently large L are assumed.

By Alexander's theorem these results imply one-ended Poisson MSF components in sufficiently high dimension. They do not count those components. A Fourier infrared bound is not by itself a pointwise spatial invasion bound. Even a critical spatial estimate τ(x)≤C(1+|x|)^{2−d} would still require a separate transfer estimate controlling invasion, and in the cell-oracle proof below controlling all revealed cells. None of these cited theorems supplies that transfer.

Chatterjee–Sen, Theorem 2.1 (preprint p.3), proves quantitative normal approximation for finite Poisson MST length, and Lemma 5.1 (preprint p.9) gives a uniform continuum two-arm estimate on compact ranges of the connection radius, decaying logarithmically in the outer scale for d≥3. This is a finite-cluster uniqueness/stabilization estimate, not the invasion occupation decay required here. Duminil-Copin–Ioffe–Velenik (2016), Theorem 2.1, public reprint p.5, develops quantitative Burton–Keane estimates under strong FKG; Duminil-Copin–Raoufi–Tassion (2020), Theorem 1, public preprint p.3, proves subcritical sharpness for Boolean percolation. Subcritical exponential decay and uniqueness do not settle the all-scale merger question at issue.

### 2.5 Other named and recent work

Aldous–Steele (1992), Lemma 1 and Proposition 9, constructs the Poisson forest/local MST limit and proves the needed local convergence. It does not prove that the limit is connected. Hirsch–Neuhäuser–Schmidt (2013), introduction and abstract, explicitly says the Poisson question is open for d>2 and constructs connected finite-order graph approximations whose decreasing intersection is the MSF. Connectivity need not survive a decreasing graph limit.

Garban–Pete–Schramm (2018), Theorem 1.1 (public preprint p.6), proves a unique planar triangular-lattice MST scaling limit. It is not a higher-dimensional Poisson connectivity theorem. Benjamini–Lyons–Peres–Schramm (2001), Theorems 9.2 and 9.4, printed pp.32–33 of the public author version, gives a random-walk intersection criterion and component count for the **uniform** spanning forest. On Z^d the uniform forest is connected for d≤4 and has infinitely many components for d≥5 (Pemantle's result, discussed there). These are analogies, not implications for MSF; d>4 must not be reported as the Poisson MSF threshold.

The search also inspected the 2025 hierarchical-clustering preprint arXiv:2503.18555; its one-ended limiting forest/subforest of the Poisson MSF does not establish MSF connectivity. Nachmias–Tang's PWIT work (2024 publication; arXiv:2207.09305), Angel–Sénizergues (2026 publication; arXiv:2312.14640), and Makowiec's August 2026 preprint arXiv:2608.10654 concern PWIT/complete-graph local or scaling limits, not fixed-dimensional Poisson geometry. Asselah–Schapira–Sousi, arXiv:2509.21253 (September 2026 revision), concerns high-dimensional critical lattice percolation capacities. It does not supply a Poisson invasion theorem.

Searches were made for the named authors, Poisson/Euclidean MSF connectivity and disconnection, high-dimensional invasion two-point functions, and 2024–2026 papers. No published d≥3 Poisson decision was located. This is a literature-search conclusion, not a proof that no paper exists. Recent online claims about critical *lattice* percolation, even if validated, would not themselves prove Poisson MSF connectivity or the invasion estimate below.

## 3. A conditional theorem with an explicit unproved hypothesis

### Theorem A (Poisson exploration cells)

Partition R^d into half-open unit cells Q_z=z+[−1/2,1/2)^d, z∈Z^d. Let v_k be the Poisson site nearest k∈Z^d. Run Prim invasion from v_k using the deterministic cell-oracle algorithm specified below, revealing the entire restriction Π∩Q_z whenever a cell is queried. Let S_k⊂Z^d be the set of all cells ever queried. Define q(z)=P(z∈S_0).

If

    Σ_{z∈Z^d} q(z)^2 < ∞,                                      (H)

then the wired Euclidean MSF, and hence the common Poisson free/wired MSF, has infinitely many trees almost surely. More quantitatively, for deterministic k,l,

    P(v_k and v_l are in the same WMSF tree)
        ≤ h(l−k),     h(a)=Σ_z q(z)q(z−a).                     (3.1)

The bound may exceed one at short distances. Hypothesis (H) is not asserted to be known in any fixed dimension for this exploration.

**Cell-oracle algorithm.** Locate v_k by querying cells in increasing distance from k until the closest revealed site is closer than the distance from k to every unqueried cell. Break cell ties by the lexicographic order of z−k. To add an invasion edge, let A be the finite set of invaded sites and m the shortest edge from A to a revealed site outside A. If no such site is known, query an unqueried cell minimizing distance to A. Otherwise query an unqueried cell with distance to A at most m, if any exists, choosing one of minimum distance, then the same deterministic tie break. Recompute m after each query. When all unqueried cells have distance greater than m, add the unique shortest known outgoing edge. Repeat. Store cell contents for reuse. This algorithm uses only previously revealed cells to choose the next cell.

Every finite invasion step needs finitely many queries almost surely. For finite A there is an actual nearest outside site at a finite distance, and there are finitely many cells within any bounded distance of A. After the relevant finite collection is exposed, the minimum is certified. The initial root search has the same property. Every invaded site belongs to a queried cell. Integer translation of Π and the seed translates the entire algorithm, so P(z∈S_k)=q(z−k).

**Proof of Theorem A.** Couple two separate copies of the exploration, seeded at k and l in independent Poisson cell environments. Interleave their operations fairly, for example alternating one primitive operation from each. A collision is the first time an exploration requests a cell already queried by the other; detect it *before* exposing the requested contents. Until this first collision all new responses are independent cell variables, with exactly the laws of a single common Poisson environment. Thus one may assign each response to a common environment on first query, fill all other cells independently, and continue both common-environment explorations after a collision. The common and independent histories agree up to the first collision; the event that no collision ever occurs is the same in this coupling. Formally one first constructs this coupling for any finite number of primitive queries and then takes the decreasing limit of the no-collision events; the fair interleaving executes every finite query at finite time. This assertion uses adaptive revelation of independent cells, not a claim of independence conditional on two final random sets being disjoint.

If the independent final queried sets intersect, they contain a common cell z. By independence of the two entire environments and the union bound,

    P(S_k^ind ∩ S_l^ind ≠ ∅)
        ≤ Σ_z P(z∈S_k^ind)P(z∈S_l^ind)
        = Σ_z q(z−k)q(z−l) = h(l−k).

Consequently, with probability at least 1−h(l−k), the two common-environment invasion trees lie in disjoint queried cells, so have disjoint vertex sets. Section 4 proves that invasion trees from vertices in the same WMSF component intersect. This proves (3.1).

For completeness, h(a)→0 as |a|→∞ whenever q∈ℓ². Choose a finitely supported f with ||q−f||₂<ε. By Cauchy–Schwarz, uniformly in a,

    |Σ_z q(z)q(z−a) − Σ_z f(z)f(z−a)|
        ≤ ε(||q||₂+||f||₂).

The second sum is zero when a separates the finite supports. Let ε tend to zero. No pointwise decay or Fourier theorem is needed.

Fix an integer K≥2 and ε>0. Choose deterministic k_1,…,k_K with all pairwise separations so large that h(k_i−k_j)<ε/binom(K,2). By (3.1) and a union bound, with probability at least 1−ε these roots belong to K different WMSF trees. Therefore P(number of trees ≥K)≥1−ε for every ε, and is one. Intersect these probability-one events over K to obtain infinitely many trees. This last step does not require ergodicity or an unproved 1-or-infinity theorem. ∎

### Corollary A.1 (a quantitative sufficient estimate)

For d>8 it suffices to prove, for this algorithm and some finite C,

    q(z) ≤ C(1+||z||)^{4−d}  for every z∈Z^d.                 (H4)

Indeed a shell of radius n has O(n^{d−1}) sites, so the squared sum is bounded by a constant times 1+Σ_{n≥1} n^{7−d}, which converges exactly for d>8. This is a sufficient threshold for this criterion, not a prediction of the true threshold.

For a completely specified critical-percolation route, define τ_c(x)=P(0 and x are connected in G_{r_c}(Π∪{0,x})) and a(z)=1_{z=0}+∫_{Q_z}τ_c(x) dx. It would suffice to prove both (a) a(z)≤C(1+||z||)^{2−d} for every z∈Z^d and (b) q(z)≤C Σ_u a(u)a(z−u) for every z∈Z^d. The second bound is a separate exploration-transfer hypothesis for the exact algorithm above. Neither is being silently assumed to follow from the other. Under these two precise bounds, (H4) follows for d>4: split the convolution into |u|≤|z|/2, |z−u|≤|z|/2, and their complement. In the first region the sum is at most C|z|^{2−d}Σ_{|u|≤|z|/2}(1+|u|)^{2−d}≤C'|z|^{4−d}; the second is symmetric. In the remaining region with |u|≤2|z|, both factors are O(|z|^{2−d}) and there are O(|z|^d) sites. For |u|>2|z|, the dyadic shell bound is CΣ_{j≥1}(2^j|z|)^{4−d}≤C'|z|^{4−d}. Bounded z are handled by finiteness of the convolution for d>4. This proves the stated implication, including all summability conditions.

Theorem A avoids a continuum pitfall in directly copying Newman–Stein: disjoint sets of *invaded points* need not reveal disjoint Poisson information. Empty search balls and neighboring candidate points have also been inspected. The hypothesis therefore concerns S_k, not merely the occupied vertices. Proving a useful bound on S_k remains the central missing step. The continuum results in Section 2 prove independent cell structure, critical nonpercolation and triangle/infrared estimates; they do not prove (H), (H4), or the transfer inequality.

## 4. Deterministic reductions and their Poisson application

### Lemma B (finite cuts and invasion)

Let X be an infinite locally finite subset of R^d with all pair distances distinct. Every finite nonempty A⊂X has a unique shortest outgoing edge, because a bounded neighborhood of a finite set contains finitely many sites. Let F_w consist of edges whose endpoints are in different strict sublevel components, at least one finite. Then:

1. e∈F_w iff e is the shortest edge across some finite nonempty cut A,X\A.
2. F_w is the union of Prim invasion trees from all vertices; it is acyclic, spans X, and all its components are infinite.
3. Two vertices are in the same F_w component iff their invasion trees intersect.

**Proof.** If e={x,y} of length s is in F_w and the component C_s(x) is finite, e is the unique shortest edge leaving that component. Conversely, if e minimizes a finite cut A, the strict sublevel component of its endpoint in A stays in A and cannot contain the other endpoint. This proves 1.

Every invaded edge is the shortest edge across the currently invaded finite set, and hence is in F_w. Conversely, starting from a vertex in a finite C_s(x), Prim fills that component before using any edge of length ≥s: any unfinished part has an internal crossing edge <s. It then takes e, the unique shortest outgoing edge. Thus every F_w edge is invaded from some vertex, proving the union assertion. A cycle cannot occur because its longest edge has a strictly shorter alternative path and fails the defining test. Every vertex has an outgoing minimum and is therefore spanned. If a component had a finite vertex set A, its shortest outgoing edge would belong to F_w by 1, a contradiction. Each invasion is infinite because every finite invaded set has a next outgoing edge.

For 3, intersection implies common F_w component because all invaded edges lie in F_w. For the reverse, it suffices to treat an F_w edge e={x,y} of length s. Its strict sublevel components C_x,C_y are distinct and at least one, say C_x, is finite. If both are finite, invasion from either endpoint fills its own component, takes e, fills the other, and reaches the same finite set C_x∪C_y before continuing identically. If C_y is infinite, invasion from x fills C_x, takes e, and then follows invasion from y: every finite stage in C_y has an outgoing edge <s, while every other edge leaving C_x has length >s. Thus the two invasion vertex sets have finite symmetric difference. Along any finite path of F_w edges the symmetric difference remains finite by the triangle inequality for set differences. Since each invasion set is infinite, two such sets intersect. ∎

This proof explicitly covers the infinite-degree complete Euclidean graph; a theorem restricted to locally finite abstract graphs is not applied without this check.

### Proposition C (Poisson free equals wired)

Assume the standard fixed-distance uniqueness theorem for the Poisson Boolean model: for each deterministic s>0, the strict graph G_s(Π) has at most one infinite component almost surely. Then F_f(Π)=F_w(Π) almost surely.

**Proof.** Fix deterministic distinct x,y∈R^d and s=|x−y|. Inserting x and y into Π cannot create new disjoint infinite components of G_s: each inserted vertex has only finitely many neighbors, and the union of finitely many finite old components and these inserted vertices is finite. Thus the augmented strict graph still has at most one infinite component almost surely. This argument also covers the case where there was no infinite component. In particular x and y cannot belong to distinct infinite strict s-components in Π∪{x,y}.

The two-fold Mecke formula now says that for each bounded box B, the expected number of ordered distinct Poisson pairs x,y∈B lying in distinct infinite strict |x−y|-components is

    ∫_B ∫_B P(x,y lie in distinct infinite strict |x−y|-components
                  of Π∪{x,y}) dx dy = 0.

The diagonal has Lebesgue measure zero. Taking a countable exhaustion of space proves that no exceptional Poisson edge exists. The free and wired edge rules can differ only at such an edge. ∎

This supplies the random-edge-threshold justification directly; it does not interchange a countable or uncountable family of fixed-parameter probability-one events without an argument. Alexander's stronger simultaneous uniqueness result also gives the equality.

### Proposition D (finite-box confinement is equivalent to connectivity)

Let X satisfy Lemma B and let Q_L=[−L/2,L/2]^d exhaust space. Let T_L be the ordinary Euclidean MST on X∩Q_L. Fix x,y∈X. For all sufficiently large L these sites are present. Write P_L(x,y) for their unique T_L path and M_L=max{|v|_∞:v∈P_L(x,y)}. Then

    x ↔ y in F_f  iff  liminf_{L→∞} M_L < ∞.                (4.1)

If they are connected, P_L is eventually the same finite F_f path, so in fact sup over sufficiently large L of M_L is finite. If disconnected, M_L→∞. Along any nested exhaustion, for every fixed inner cube Q_R, the event P_L⊂Q_R decreases eventually to {x ↔ y in F_f restricted to Q_R}. Consequently

    P(x ↔ y in F_f)
       = lim_{R→∞} lim_{L→∞} P(P_L(x,y)⊂Q_R),              (4.2)

for fixed random roots that are eventually present (with the harmless absence convention at small L). For Poisson, F_f=F_w, so this is a criterion for the forest in the question.

**Proof.** For a fixed edge e, once both endpoints are present, membership in T_L decreases as L increases. The edge is excluded exactly when there is a finite alternative path with every edge shorter than e. Such a witness, if it exists globally, lies in some finite cube. If none exists, e is in every T_L containing its endpoints. Hence the edgewise decreasing limit is precisely F_f.

If x,y are connected by a finite F_f path, all its edges occur in every sufficiently large T_L, and uniqueness of paths in a tree forces P_L to be that path. Conversely, a bounded liminf supplies arbitrarily large L for which P_L lies among the finitely many vertices of a fixed cube. There are finitely many possible simple paths on those vertices. One occurs for an unbounded sequence of L; all its edges must survive the decreasing limit, giving an F_f path. For a fixed Q_R, the restrictions T_L|Q_R are decreasing finite forests once L≥R, and stabilize to F_f|Q_R. This proves the event assertion, then (4.2) by bounded/monotone convergence. ∎

**Why the order of limits matters.** Testing whether T_L connects x,y gives 1 identically. Testing confinement inside a window proportional to L while also letting |x−y| grow probes a different finite-size question and cannot establish (4.2). The computations below record this distinction.

### Proposition E (computable lower certificates)

On X∩Q_L, adjoin a vertex ∂ and edges {x,∂} of weight δ_L(x)=distance(x,R^d\Q_L). Keep the ordinary internal Euclidean edges. Let W_L be its MST after deleting ∂ and all its incident edges. Assume generic distinct weights, as holds almost surely for Poisson boxes at any fixed countable sequence of L. Then

    W_L ⊂ F_w(X),     W_L ↑ F_w(X) edgewise as L ↑ ∞.       (4.3)

For Poisson and fixed inner Q_R this gives computable eventual brackets

    {x ↔ y in W_L|Q_R}
        ⊂ {x ↔ y in F|Q_R}
        ⊂ {x ↔ y in T_L|Q_R},                             (4.4)

and both brackets converge to the middle event as L→∞.

**Proof.** An internal MST edge e of length s is kept exactly when its endpoints are disconnected in the strict augmented sublevel graph. At least one endpoint's sublevel component A does not contain ∂, so A is finite, has no shorter internal outgoing edge, and δ_L(a)≥s for each a∈A. Every actual edge from a to a site outside Q_L has length at least δ_L(a)≥s. Thus e is the minimum edge of a finite cut in the infinite configuration, and is in F_w by Lemma B.

Equivalently, an edge is in W_L when its two internal strict components are distinct and at least one stays at distance ≥s from the exterior. Such a finite component remains exactly the same strict component in every larger box: it has no edge <s to any outside site. Hence that certificate persists and W_L is increasing on fixed edges. For e∈F_w, choose a finite endpoint strict component C_s(x). Once the box contains this finite set with a margin greater than s, the same component avoids ∂ and certifies e∈W_L. This proves (4.3). Finite restrictions stabilize, and (4.4) follows from F_w=F_f. ∎

The distance-to-exterior wire is an optimistic external shortcut, not a claim that actual exterior Poisson vertices sit at those positions. This is why retained internal edges are valid lower certificates.

## 5. Computation (evidence only)

The final run used 16 independent nested Poisson realizations per dimension, with expected sample sizes 1,024, 4,096, 16,384 and 65,536. This is 48 independent realizations and 384 finite MSTs, because the four sizes are nested and the two boundary conditions are paired. The actual maximum sample count was 66226. Points have intensity one; the side lengths at the largest scale are 40.3175, 16 and 9.1896 for d=3,4,5. Thus “65,536 points” in d=5 still gives a spatially modest box.

**Exact finite MST calculation.** Candidate edges are all pairs within a radius, found by cKDTree. Kruskal's algorithm (SciPy sparse MST) is run on this graph; the radius is enlarged if the graph is disconnected. Every accepted tree has n−1 edges and maximum edge length strictly below the candidate radius. Every omitted complete-metric edge is at least that radius, so it cannot improve the tree, by the cycle/cut property. This certifies the *complete* Euclidean MST for free boundaries and the complete minimum-image torus MST for periodic boundaries; it is not an uncertified k-nearest-neighbor approximation. The distance-to-exterior wired forest of Proposition E is also computed for each free box.

**Observables.** The whole finite MST connects every pair, and this tautological check passed in all 384 cases. The nontrivial primary statistic selects 64 distinct random pairs in the central cube of side L/2, each with Euclidean separation at least L/3, and tests connection after restricting the MST to that cube. The same pairs are used for free and periodic boundaries. These are deliberately far-apart *moving* pairs. Their separation and window both grow with L, so these statistics do not estimate the iterated fixed-root limit (4.2).

Separately, in each smallest box a maximally separated pair among its central-cube points is chosen once and held fixed across the four nested boxes. Its connection is recorded within the fixed inner cube of side 0.75 L_min, as well as in the wired certificate using the whole growing box. The root coordinates are recorded, and this selection from the smallest sample is dependent on that sample. No Palm or unbiased-pair interpretation is attached to it.

The following entries are mean fractions of far pairs connected in the central cube. The bounds are approximate 95% Student-t intervals calculated over the 16 **replicate fractions**. They are descriptive intervals, not rigorous confidence bounds or intervals based on treating the 1,024 pairs as independent.

| d | Expected n | Free interior connection fraction (interval) | Periodic interior connection fraction (interval) |
|---|---:|---:|---:|
| 3 | 1,024 | 0.0918 (0.0240–0.1596) | 0.0576 (0.0267–0.0886) |
| 3 | 4,096 | 0.0566 (0.0295–0.0838) | 0.0400 (0.0199–0.0602) |
| 3 | 16,384 | 0.0615 (0.0358–0.0872) | 0.0381 (0.0104–0.0658) |
| 3 | 65,536 | 0.0459 (0.0207–0.0711) | 0.0342 (0.0100–0.0584) |
| 4 | 1,024 | 0.0381 (0.0128–0.0633) | 0.0352 (0.0094–0.0609) |
| 4 | 4,096 | 0.0264 (0.0021–0.0506) | 0.0205 (0.0000–0.0436) |
| 4 | 16,384 | 0.0166 (0.0039–0.0293) | 0.0137 (0.0008–0.0265) |
| 4 | 65,536 | 0.0156 (0.0065–0.0247) | 0.0117 (0.0023–0.0211) |
| 5 | 1,024 | 0.0420 (0.0233–0.0607) | 0.0273 (0.0126–0.0421) |
| 5 | 4,096 | 0.0156 (0.0055–0.0257) | 0.0117 (0.0029–0.0206) |
| 5 | 16,384 | 0.0098 (0.0000–0.0207) | 0.0068 (0.0000–0.0154) |
| 5 | 65,536 | 0.0059 (0.0007–0.0110) | 0.0039 (0.0002–0.0076) |

At the largest scale, the wired whole-box certificate connected the fixed pair in the following numbers of realizations. A success proves connection in the corresponding infinite Poisson forest under the exact-arithmetic model; a failure does not prove disconnection. Floating-point arithmetic is used in the actual numerical implementation.

| d | Fixed-pair wired successes, as expected n grows 1,024 → 4,096 → 16,384 → 65,536 | Final far-pair fraction connected in whole-box wired certificate |
|---|---|---:|
| 3 | 0/16 → 0/16 → 4/16 → 6/16 | 0.0801 |
| 4 | 0/16 → 0/16 → 1/16 → 3/16 | 0.0479 |
| 5 | 0/16 → 0/16 → 0/16 → 0/16 | 0.0127 |

The fixed-inner-window brackets converge to 0/16, 0/16 and 0–1/16 (wired lower/free upper) in dimensions 3,4,5 respectively at the final scale. This concerns only that small fixed window: the d=3 whole-box wired successes above show directly why a zero in a small observation window must not be read as global disconnection. The interior connected-pair fractions generally fall as separation increases, especially in d=4,5. The limited scales, dependence, and path escape permit no conclusion that the infinite forest is disconnected, no estimate of its number of trees, and no fitted critical dimension.

**Checks and reproducibility.** `code/poisson_msf.py --validate-only` compares the sparse Kruskal trees against an independently implemented dense Prim algorithm on 120 points in each dimension with both metrics; all edges agree. It also compares the augmented wired MST with full Prim and checks the strict-sublevel finite-cut witness for every retained wired edge. During the final run the code checks that wired certificates are retained by both finite boundary conditions, periodic interior edges are a subset of free interior edges, the fixed-window free events decrease, and the wired events increase. All checks passed.

`code/audit_results.py` independently aggregates the 24,576 saved pair records, reconstructs all fractions, recalculates the t intervals using a tabulated critical value, checks the root geometry and nested monotonicity, and verifies the MST radius certificates from the saved records. It passed: `data/audit.json`. This audits the finite calculations, not infinite-volume connectivity.

Run commands, from this directory:

    python3 code/poisson_msf.py --replicates 16
    python3 code/audit_results.py

The task launcher supplied nice 10; the simulation verifies it. There was one simulation process, with numerical thread environment variables set to one. NumPy 2.2.3 and SciPy 1.15.2 were used. Peak recorded resident memory was 1,112,948,736 bytes (1.113 decimal GB), below 4 GB, and elapsed time was 137.77 seconds. A candidate-edge cap guards the array sizes. The attempt to set a 3.2 GB data-segment limit was rejected by macOS; it was not an active hard limit. The reported memory bound is the measured peak RSS. No subagents or other model workers were started.

Raw data: `data/observations.jsonl` (384 graph records, seeds, sample hashes, root coordinates, graph certificates); `data/pair_observations.csv` (24,576 pair records); `data/summary.csv`; `data/run_metadata.json`; `data/simulation_run.log`; `data/audit.json`. The earlier smaller pilot is preserved separately under `data/pilot_16384/` and is not pooled with the final results. The sample hashes permit deterministic regeneration with the recorded NumPy version and seeds; the full coordinate arrays are not stored. Source PDFs and paper images were never saved.

## 6. Source record and audit

Source acquisition and version details are in `sources/`; every text records its URL, retrieval timestamp and response SHA256. PDF responses were converted in memory and never saved as PDF files or images. The current author/book versions are distinguished from journal pagination. A failed publisher download is retained as an explicitly named access-failure text, not treated as a paper.

The proof audit checks: strict versus non-strict thresholds; fixed versus random thresholds; infinite-degree complete graph versus locally finite abstract graphs; invaded vertices versus revealed information; connectivity versus ends; finite component counts versus infinitely many; and the two different orders of spatial limits. No simulation or critical percolation theorem is used to assert the missing hypothesis (H).

### Selected exact source locations

The page references marked “preprint” or “author version” refer to the saved text's printed pages, not an inferred offset in another edition. No published resolution is asserted.

| Source | Exact result/location used | Scope |
|---|---|---|
| [Aldous–Steele, objective-method author preprint](https://www.stat.berkeley.edu/~aldous/Papers/me101.pdf) | Definition 4.2, p.33; Section 6.3, pp.63–64 | Wired definition; Poisson question, planar result, unspecified high-d conjecture |
| [Alexander, Ann. Probab. 23 (1995), 87–104](https://www.stat.berkeley.edu/~aldous/206-SNET/Papers/alexander.pdf) | Proposition 2.2, p.91, with Poisson application p.92; Theorem 2.5(ii), pp.92–93; Theorem 2.6 and Example 2.8, pp.93–94; Theorem 4.2, p.99; Lemma 3.7, p.97 | Simultaneous uniqueness, ends, planar connectivity, invasion |
| [Lyons–Peres–Schramm, Ann. Probab. 34 (2006), 1665–1692](https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf) | Propositions 3.3–3.4, p.1672; Proposition 3.5(c), pp.1672–1673; Proposition 3.6, p.1673; Proposition 3.10, p.1674; Theorem 3.12, p.1675; Questions 6.8 and 6.10, p.1689 | General iid edge-weighted graph results and open questions |
| [LPS erratum, 9 September 2024](https://rdlyons.pages.iu.edu/errata/msf.pdf) | Single page; adds p_c(G)<1 to Conjecture 6.9 | Checked; no effect on the reductions proved here |
| [Newman–Stein, J. Stat. Phys. 82 (1996), 1113–1132, public preprint](https://arxiv.org/abs/adap-org/9505005) | Unnumbered theorem in Section 5, preprint pp.9–11; equation (6), p.9; equations (8)–(15), pp.10–11 | Conditional square-summability theorem; invasion-dimension heuristic |
| [Jackson–Read I, Phys. Rev. E 81 (2010), 021130](https://arxiv.org/abs/0902.3651) | Section II, preprint pp.7–8; Section III, including III.G on PWIT; Section IV, p.17 | Exact tree mean field, predicted d_c=6 for Euclidean geometry |
| [Jackson–Read II, Phys. Rev. E 81 (2010), 021131](https://arxiv.org/abs/0909.5343) | Abstract and renormalization discussion; companion perturbation expansion | No finite-dimensional connectivity theorem |
| [Heydenreich–van der Hofstad–Last–Matzke, 2023 public revision](https://arxiv.org/abs/1908.11356v4) | Proposition 1.1(a), preprint pp.4–5; Theorems 1.2 and 1.3, p.5 | Boolean high-d triangle/infrared, γ=1, θ(λ_c)=0; published AIHP 62 (2026), 1–67, DOI 10.1214/24-AIHP1490 |
| [Chatterjee–Sen, Minimal spanning trees and Stein's method](https://arxiv.org/abs/1307.1661) | Theorem 2.1, preprint p.3; Lemma 5.1, p.9 | Finite Poisson MST CLT and logarithmic continuum two-arm bound |
| [Duminil-Copin–Ioffe–Velenik, Ann. Probab. 44 (2016), 3335–3356](https://arxiv.org/abs/1409.5199) | Theorem 1.1, public reprint p.2; Theorem 2.1, p.5 | Reverse Poincaré and two-arm estimates |
| [Duminil-Copin–Raoufi–Tassion, Ann. H. Lebesgue 3 (2020), 677–700](https://arxiv.org/abs/1805.00695) | Theorem 1, public preprint p.3 | Sharpness under radius moment assumptions, satisfied by deterministic balls |
| [Aldous–Steele, PTRF 92 (1992), 247–258](https://www.stat.berkeley.edu/~aldous/Papers/me57.pdf) | Lemma 1, p.248; Proposition 9, pp.253–254 | Construction and local convergence, not connectivity |
| [Hirsch–Neuhäuser–Schmidt, Adv. Appl. Probab. 45 (2013), 20–36](https://www.mathematik.uni-ulm.de/stochastik/personal/schmidt/publications/connectivity.pdf) | Author preprint abstract/introduction, p.1 | Connected finite-order approximations; Poisson d>2 explicitly open |
| [Garban–Pete–Schramm, Ann. Probab. 46 (2018), 3501–3557](https://arxiv.org/abs/1309.0269) | Theorem 1.1, public preprint p.6 | Planar triangular-lattice scaling limit |
| [Benjamini–Lyons–Peres–Schramm, Uniform spanning forests](https://rdlyons.pages.iu.edu/pdf/usf.pdf) | Theorems 9.2, 9.4, author-version pp.32–33 | Uniform-forest random-walk criterion, not minimal-forest theorem |
| [Lyons–Peres, Probability on Trees and Networks, corrected 8 November 2020](https://rdlyons.pages.iu.edu/prbtree/book_corr.pdf) | Proposition 11.7, pp.395–396; Question 11.19, p.400; Question 11.35, p.406 | Free/wired equivalence, component count and competing connectivity conjectures |
| [Fitzner–van der Hofstad, EJP 22 (2017), paper 43, extended public version](https://arxiv.org/abs/1506.07977) | Abstract and Section 1 main results | Modern d≥11 lattice mean-field regime; no Poisson invasion transfer |

The newer sources listed in Section 2.5 are also saved in full extracted text. A source filename ending in 2025 identifies the original submission year, not a guarantee that the response was the first version; the retrieved header and text determine the actual version.

### Status of the conditional theorem's inputs

| Input | Poisson status supported by the checked sources |
|---|---|
| Independent cell restrictions and finite queries for every finite invasion prefix | Proved directly in the construction above |
| Fixed-radius uniqueness / free=wired | Known in all dimensions; Proposition C gives the needed random-edge step |
| No occupied infinite cluster at criticality | Known in the plane and sufficiently high d in the sources checked; high-d reference is HVHLM Theorem 1.3 |
| Critical triangle condition and Fourier infrared bound | Proved for deterministic balls in sufficiently high d by HVHLM |
| Spatial critical bound on a(z) used in the optional transfer route | Not claimed as a consequence of the cited Fourier bound |
| The inequality q≤C(a*a), or directly (H4) | Additional unproved hypothesis |
| Square summability (H) for this Poisson invasion exploration | Additional unproved hypothesis; no fixed-d instance established here |

The remaining obstruction is quantitative control of invasion exploration/coalescence across scales. The proofs above make that obstruction explicit and give a way to certify and measure finite connections, but do not remove it.

Task: “Open problem C0113” — 13 November 2026, approximately 10:27 +04 (Asia/Tbilisi).
