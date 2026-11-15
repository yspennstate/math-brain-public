ACCEPT

The stated partial theorem is correct for the sequential non-backtracking walk law in the question. I found no mathematical error in its routing construction, reversal argument, resampling congestion bound, constants, or expectation calculation. It proves the square-root birthday bound uniformly on graphs of bounded maximum-to-minimum degree ratio, including regular graphs whose degree grows with n. It does not settle unrestricted Conjecture 1.5. The construction is an extension of Dozier's proof, with weighted departures and conditional resampling doing the additional work. No printed result establishing this entire extension was located; priority beyond the searched literature remains unverified.

The following are the remaining limitations and presentation issues. None invalidates the partial theorem.

1. **The unrestricted conjecture remains open in this argument.** Location: claim_files/REPORT.md, lines 107–143 and 221–223. Packing, terminal returns, and reversal weights cost Q, Q, and Q respectively. For unbounded degree ratio these losses are not controlled uniformly. Fix required for a full solution: replace these estimates with bounds independent of Q, or supply another argument. The claim correctly discloses this limitation and labels itself PARTIAL.
2. **Some referenced artifacts are absent from the supplied review bundle.** Location: claim_files/REPORT.md, lines 24 and 53, and its literature/source discussion. There is no claim_files/PROOF.md or claim_files/sources/ here. The full proof is included in REPORT.md, so this is a reproducibility issue, not a missing mathematical argument. Fix: include the referenced files or revise the references. I independently retrieved the primary papers into this review's sources/ directory.
3. **The original numerical experiments do not test a nontrivial value of the proposed upper bound.** Location: claim_files/code/experiment.py, line 213, and claim_files/REPORT.md's computation discussion. Its large-graph checkpoints stop at 6 sqrt(n). Since Q>1, 256 Q(1+Q)n/k²>512/36>1 throughout those checkpoints. Small exact tests are also in the trivial regime. The report does not claim that simulation proves the bound, so this is an evidentiary limitation rather than a false statement. Fix: report the bound alongside the observations and explain this limitation. My independent data do this, including later checkpoints where the upper bound is below 1.
4. **Novelty is conditional on the literature search.** Location: claim_files/REPORT.md, opening paragraph and literature conclusion. I found no contrary priority evidence, but an empty citation index is not a proof of priority. Fix: retain the qualified novelty wording already used; do not describe this as a verified first result or a resolution of G0012.

The primary source and its conventions were checked against two independently extracted representations. The full Dozier text is in [sources/dozier_2608.26321v1.txt](sources/dozier_2608.26321v1.txt), with mathematical HTML alttext retained, and [sources/dozier_2608.26321v1_pages.txt](sources/dozier_2608.26321v1_pages.txt), with PDF page boundaries. PDF bytes were parsed in memory and never saved. Theorem 1.1 is on PDF p.1; Conjecture 1.5 is on PDF p.2. The following transcriptions preserve the statements, with mathematical notation typeset.

> Theorem 1.1. Fix d ≥ 3. For any ε > 0, there exists a C = C(d, ε) such that if Γ is a d-regular graph on n vertices, and k > C√n, then for any edge δ, the probability that a length k random non-backtracking walk starting with δ is simple is less than ε.

> Conjecture 1.5 (Alon-Peres). For any ε > 0, there exists a C = C(ε) such that if Γ is a graph on n vertices with all degrees at least 3, and k > C√n, then for any edge δ, the probability that a length k random non-backtracking walk starting with δ is simple is less than ε.

These are statements from [Dozier, arXiv:2608.26321v1](https://arxiv.org/html/2608.26321v1). His graphs are undirected, without loops or multiple edges; every edge mentioned has an orientation. “Simple” means no repeated vertex, including the starting vertex. Length k counts k edges, including the prescribed starting edge δ=(x₀,x₁), hence k+1 visited vertices. In particular p₁=p₂=1 and p_k=0 for k≥n. Connectedness is not assumed. The claim reads these conventions correctly.

Dozier does not separately give an irregular-graph transition formula. The standard sequential interpretation used here is

\[
 P((u,v),(v,w))=\frac{1}{d(v)-1}\quad(w\in N(v),\ w\ne u).
\]

It is explicitly the law defined by [Bencs et al., arXiv:2608.09729v1, Introduction, PDF p.1](https://arxiv.org/html/2608.09729v1). Their first step from a specified vertex is uniform over its neighbours; conditioning on that first directed edge gives the law audited here. Uniform sampling from all complete length-k non-backtracking paths is a different measure on irregular graphs. The proof does not establish the claimed inequality for that measure, and the claim explicitly makes this distinction.

I audited each substantive step of claim_files/REPORT.md as follows. References below are to its line numbers.

| Location | Independent check and conclusion |
|---|---|
| 73–81: product measure on plans | Each local neighbour permutation is a uniformly chosen derangement. Exactly R_d/(d−1) derangements send a specified neighbour to another specified neighbour: conjugation by permutations fixing the input acts transitively on the other outputs. A simple path imposes one constraint at each of k−1 distinct interior vertices, giving probability ∏ᵢ₌₁ᵏ⁻¹ 1/(d(xᵢ)−1), exactly the sequential NBW path probability. Summing over simple paths gives μ(S)=p_k. Equality of the full plan-walk law and NBW law after collisions is neither true nor needed. |
| 73: invertibility | At every vertex incoming directed edges map bijectively to outgoing directed edges. Together these local maps make a permutation of all directed edges, even when degrees differ. No equal-degree assumption occurs. |
| 85–95: departure weights | There are d(xᵢ)−2 alternative outgoing edges at index i. Giving each weight 1/(d(xᵢ)−1) makes the total at that index (d(xᵢ)−2)/(d(xᵢ)−1) lie in [1/2,1). Thus T≥(k−1)/2. The minimum-degree-three assumption is used exactly here. |
| 97–99: certificates | The excursion is followed only until its first return to the main path or its L-th edge. Until then its interior vertices lie outside the main path, so their routing is unchanged by any replacement at xᵢ. If the excursion repeats internally or hits the already visited prefix, collision has already occurred before routing at xᵢ could be used again. Thus every allowed replacement preserves a certified collision by time i+L. |
| 103–110: packing | For an uncertified excursion that avoids the path, its L directed edges are distinct. If two such excursions shared a directed edge, invertibility forces their backward histories to agree until a departure edge is reached. Unequal backward lengths force the longer history to have visited a main-path vertex before its supposed first return; equal lengths identify the same departure. Hence the edge sets are disjoint. There are ∑ᵥd(v)≤nM directed edges and each departure weighs at most 1/(m−1), giving U≤Qn/L. No unproved independence or mixing assumption appears. |
| 115–121: terminal returns | Given a final directed edge into x_k, inverse routing outside the path uniquely recovers the excursion back to its last departure from the path. Distinct departures therefore have distinct final edges. There are at most d(x_k)≤M such edges, giving total weight at most Q. The sharper regular-case d−1 count is unnecessary. Counting certified returns here as well merely overestimates the error term. |
| 125–129: reversal construction | For an interior first return at x_ℓ, invert each exterior local permutation once and leave every path permutation unchanged. The main path is preserved. If πᵥ(a)=b, its inverse sends b to a, so every excursion transition is reversed, including multiple transitions at the same exterior vertex. The reversed sequence has no main-path vertex before its endpoint. A returning excursion cannot repeat a directed edge before returning: deterministic routing would then trap it forever outside the path. Repeated vertices do not cause this problem. |
| 127: legality of reversed departure | For an excursion of two or more edges its last predecessor is outside the main path, so it cannot be either main-path neighbour of x_ℓ. For a one-edge excursion the edge is a chord of the simple path. Consecutive endpoints would make the original departure a backtrack or the original continuation, both excluded. Thus the reverse edge is an allowed departure in every case. |
| 129–139: involution and weights | Reversing again visits the same exterior vertex set and inverts the same local permutations, restoring the original plan and departure. If the excursion repeats a vertex then both directions are certified; otherwise the direction ending at the earlier path index is certified. All base plans have the same μ-mass, although their local degree counts differ by vertex. The two departure weights have ratio (d(x_ℓ)−1)/(d(xᵢ)−1), bounded between 1/Q and Q. Pairing triples, rather than asserting a pairing within each fixed plan, therefore gives total uncertified interior-return weight at most Q times certified interior-return weight. This averaging point is handled correctly. |
| 141–145: average bad weight | Partition departures into certified, uncertified non-returning, uncertified terminal-returning, and uncertified interior-returning ones. Initial returns are certified. Allowing the terminal estimate to include extra certified departures only enlarges the right side. Consequently (1+Q)B≥(k−1)/2−Qn/L−Q. |
| 149: truncation near the end | Retain indices i≤k−L. At most L−1 indices are actually discarded, each of total departure weight below 1. The weaker B₀≥B−L is valid, also when there are no retained indices. |
| 151–161: resampling mass | At degree d there are R′_d=R_d/(d−1) replacement derangements satisfying the chosen outgoing edge. Mass μ(ρ)/(d−1), split uniformly over them, contributes μ(ρ)/R_d to each replacement. This exact cancellation is the reason a factorial derangement factor does not enter the final bound. |
| 163–169: incoming congestion | For any output plan ψ with first collision at edge j, an admissible source changing routing at i has i<j≤i+L. Thus i is in the L-integer interval [j−L,j−1]. At a fixed i, ψ determines the departure vertex, incoming edge, and outgoing departure edge. Only that vertex's source derangement is unknown, with at most R_d possibilities. Every such source has μ(ρ)=μ(ψ), so its total incoming mass is at most μ(ψ) for this i, and at most Lμ(ψ) overall. There is no hidden multiplicity from other vertices or different outgoing edges. |
| 169–173: flow inequality | Summing outgoing mass over simple sources gives p_k B₀. All outputs are nonsimple, giving p_k B₀≤Lμ(Sᶜ)≤L. This is valid even though nonsimple plan trajectories need not have the ordinary NBW law. |

The stationarity issue in the question does not break the proof. The directed-edge transition matrix is doubly stochastic on irregular graphs too:

\[
 \sum_{u\in N(v)\setminus\{w\}}P((u,v),(v,w))
 =(d(v)-1)\frac1{d(v)-1}=1.
\]

The stationary law on directed edges is uniform; its vertex marginal is proportional to degree. This is [Kempton, arXiv:1603.05553v1, Lemma 1, PDF p.4](https://arxiv.org/abs/1603.05553). Uniformity on vertices would require regularity, but it is never used in this proof. Nor does the argument require irreducibility, aperiodicity, expansion, or fast mixing. A stationary distribution alone would not supply the asserted birthday bound.

The constants in lines 175–206 also check out. Write A=1+Q. Only the regime 1≤k<n and k²≥256QAn needs proof. Since n>k, that regime implies k>256QA, hence k≥16A, k≥4, and Q≤k/16. With

\[
 L=\lceil16Qn/k\rceil,
\]

one has

\[
 \frac{Qn}{L}\le\frac{k}{16},\qquad
 L\le\frac{k}{16A}+1\le\frac{k}{8A}<k.
\]

Thus the bad-weight inequality gives

\[
 B\ge\frac{(k-1)/2-k/16-k/16}{A}
 =\frac{3k/8-1/2}{A}\ge\frac{k}{4A},
 \qquad B_0\ge\frac{k}{8A}.
\]

The 8 in the next bound is therefore justified:

\[
 p_k\le\frac{8AL}{k}
 \le\frac{128AQn}{k^2}+\frac{8A}{k}
 \le\frac{136AQn}{k^2}
 \le\frac{256AQn}{k^2}.
\]

The penultimate step uses k<n≤Qn. For k≥n, p_k=0 by vertex counting; for k²<256QAn the asserted bound is simply 1. Thus no unjustified restriction to small k is concealed in the proof, and equality at the threshold causes no issue. The proof actually leaves slack between 136 and the advertised 256 within its nontrivial regime. A separate exact-rational check of 113 admissible parameter choices, including lengths adjacent to the nontrivial threshold and to n, verified these rounding and constant inequalities; its count is recorded in data/final_checks.json.

For M/m≤D, necessarily D≥1, and

\[
 Q=\frac{M}{m}\frac{m}{m-1}\le\frac32D,
 \qquad256Q(1+Q)\le960D^2<1024D^2.
\]

Hence k>32D√(n/ε) gives p_k<ε. This constant is independent of the absolute degrees. For M≤Δ and m≥3,

\[
 256Q(1+Q)\le256\frac\Delta2\left(1+\frac\Delta2\right)
 =64\Delta(\Delta+2),
\]

so the other stated constant, 8√(Δ(Δ+2)/ε), is correct. These cover 0<ε<1; using the ε=1/2 constant for ε≥1 is sufficient.

I separately checked the expectation calculation, lines 208–219. Let τ=min{t: X_t repeats an earlier vertex}, where the fixed edge is time 1. Then τ≤n and P(τ>k)=p_k, including p₀=1. Put H=256Q(1+Q)n and a=⌈√H⌉. The displayed sum is legitimate, albeit deliberately loose at its integer endpoint:

\[
 \begin{aligned}
 \mathbb E\tau
 &=\sum_{k=0}^\infty\Pr(\tau>k)\\
 &\le a+1+H\sum_{k=a+1}^\infty k^{-2}\\
 &\le a+1+H/a\\
 &\le2\sqrt H+2
 =32\sqrt{Q(1+Q)n}+2.
 \end{aligned}
\]

Here ∑_{k=a+1}∞k⁻²≤∫ₐ∞x⁻²dx=1/a, a≤√H+1, and H/a≤√H. This also works if a≥n, when the actual tail is zero. The factor 32 is exactly 2√256; there is no lost logarithm or collision-time indexing error. Averaging over a random first edge from a specified vertex preserves the bound.

The independent numerical work is in [code/independent_probabilities.py](code/independent_probabilities.py) and [code/independent_routing.py](code/independent_routing.py). These were written and run before I read the supplied implementation. Neither imports nor copies claim_files/code. The subsequent read of that implementation found the expected killed-walk DP and a uniform non-backtracking sampler; its sampling shortcut is valid because each allowed neighbour has exactly one preimage among the sampled indices.

The exact DP has state (visited subset, previous vertex, current vertex). With H₀=lcmᵥ(d(v)−1), all live masses at length k are integers divided by H₀^(k−1). For each unvisited neighbour it multiplies the numerator by H₀/(d(current)−1). Moves to visited vertices are killed, not renormalized. This independently computes the sequential NBW survival probabilities as exact fractions. A separate direct rational path recursion crosschecks tiny instances.

The exact suite covers all 173 Graph Atlas isomorphism classes on at most seven vertices with minimum degree at least three; two constructed irregular graphs at each order 8 through 14; Petersen, Heawood, K₃,₁₁; and a disconnected union of two K₄s. Every directed starting edge is evaluated, not just representatives. There are 191 cases, 5,522 starts, 41,324 exact positive-length probability values, 598,592 processed live states, and 318 direct-enumeration crosschecks. All probabilities are nonincreasing, all p_n vanish, and every stated probability and expectation inequality passes. Results, graph adjacencies, exact fractions, and exact expected times are in [data/exact_all_starts.json](data/exact_all_starts.json). These small cases are all in the trivial regime of the proposed tail bound.

Some independently recovered values are:

| Graph and directed start | Exact values |
|---|---|
| K₅ minus {0,1}, start (0,2) | p₃=7/9, p₄=8/27 |
| Same graph, start (2,0) | p₃=2/3, p₄=5/18 |
| Petersen, start (0,1) | p₉=1/32, Eτ=27/4 |
| Heawood, start (0,1) | p₁₃=3/512, Eτ=4299/512 |
| K₃,₁₁, start from the size-three side | p₄=1/2, p₅=9/20, p₆=0 |

The routing program exhaustively enumerates all 16 plans on K₄, 2,916 plans on K₅ minus an edge, and 64 plans on K₃,₃. It checks every directed starting edge, every k=2,…,n−1 and L=1,…,n+1. It verifies packing disjointness, terminal injection, reversed-departure legality, involution, weight ratio, the aggregate bad-weight inequality, every retained local replacement's certificate and first-collision index, and output congestion. Totals are 1,620,912 examined departures, 242,784 reversal checks, 204,000 replacement checks, 63,708 output-congestion checks, and 948 aggregate inequalities. A further random-plan audit on an irregular 12-vertex graph checks 38,089 interior reversals, including 6,499 excursions that repeat an exterior vertex. All pass. Details are in [data/routing_summary.json](data/routing_summary.json). This supports the delicate combinatorial steps; it is not a replacement for the argument above.

Monte Carlo uses a fresh choice at each step from the current neighbour list, rejecting exactly the preceding vertex. It runs each walk until its actual first collision, without censoring. Eleven graphs, 23 directed starts, and 5,000 trials per start give 115,000 walks. Families include random cubic graphs at n=4,096, 16,384 and 65,536; the same sizes with an added matching giving degrees three and four; cubic bases with three new hubs each joined to √n distinct base vertices; K₃,₄₀₉₃; and a ladder with an added hub. Both hub-edge orientations and an ordinary base edge are tested. The largest graph has 65,539 vertices. Every graph is checked for simplicity, symmetry and minimum degree three.

[data/monte_carlo.csv](data/monte_carlo.csv) gives 401 probability checkpoints with the claimed bound and pointwise 95% Wilson intervals. Fifty-six rows have k<n and claimed upper bound below 1. All comparisons pass; there are no observed survivors in those 56 rows. Zero observed survival is not zero probability: with 5,000 trials the Wilson upper endpoint is about 0.000768. Many of these bounds are still too loose for such a sample to discriminate sharply. [data/collision_times.jsonl](data/collision_times.jsonl) contains all collision times; [data/mc_metadata.json](data/mc_metadata.json) records starts, graph sizes, degrees and fingerprints. Fixed seeds and graph construction rules are in the code.

At the largest sizes, representative observations are:

| Graph / starting-edge type | p̂ at k≈√n | p̂ at k≈2√n | p̂ at k≈4√n | Mean τ / √n |
|---|---:|---:|---:|---:|
| Cubic | 0.8342 | 0.4992 | 0.0650 | 2.1305 |
| Degrees three and four | 0.7966 | 0.4100 | 0.0284 | 1.8711 |
| Three hubs, hub→base | 0.5560 | 0.1932 | 0.0084 | 1.2729 |
| Three hubs, base→hub | 0.5678 | 0.2068 | 0.0076 | 1.3072 |
| Three hubs, ordinary base edge | 0.7426 | 0.3174 | 0.0140 | 1.6663 |

The unequal-degree sanity check deserves a separate interpretation. For the last hub graph, m=3, M=256, Q=128, n=65,539, and H=256Q(1+Q)n=277,038,071,808. Even H/n²≈64.497>1, so the claimed upper bound is identically 1 for every potentially simple length. Its expectation bound is also larger than the deterministic τ≤n bound. Consequently this example cannot contradict the claim, independently of its simulation results. Its observed collision scale is compatible with √n, but does not prove the unrestricted conjecture.

An n-cycle has p_k=1 for k<n and does refute the minimum-degree-two version. This graph is excluded. Known square-root lower examples also do not contradict this theorem: [Bencs et al., Theorem 3](https://arxiv.org/html/2608.09729v1) supplies regular high-girth examples with Eτ≥√n/6, consistent with an upper bound of a constant times √n. The multigraph construction in the claim is correct: b_j=2^(j²+1) parallel edges give forward survival at least ∏_{j≥2}(1+2^{−(2j−1)})⁻¹≥e^(−1/6), while all degrees are at least four. It is outside the simple-graph assumptions. Subdividing the parallel edges creates forbidden degree-two vertices; replacing them by distinct neighbours changes the graph size and collision mechanism. Neither that construction nor the few-hub examples give an immediate simple-graph counterexample at unbounded ratio.

The verified literature comparison is as follows. The full texts of the two central 2026 papers were read, including Dozier's entire Section 2. Bencs et al., Theorem 1, PDF p.2, proves E T=O_Δ(√n log n) for connected graphs of minimum degree three and fixed maximum degree Δ. Theorem 2 removes the logarithm under regularity and a fixed spectral gap. Question 4, PDF p.3, asks for the unrestricted square-root expected-time bound and immediately explains the multigraph obstruction. These results are earlier than Dozier. They do not already imply the audited irregular-graph O_D(√n) bound. Their vertex-start convention does not obstruct comparison: conditioning on one of at most Δ first edges costs at most Δ in their bounded-degree result. [Bencs et al., primary text](https://arxiv.org/html/2608.09729v1).

Dozier's Theorem 1.1 supplies a constant allowed to depend on a fixed regular degree. Its statement does not give the bounded-ratio result for irregular graphs, nor a degree-uniform bound even for all regular degrees. His proof uses plans, disjoint departures and excursion reversal; those ideas are correctly credited in the claim. His deterministic replacement count retains an R_d factor in Lemma 2.3. The present proof's randomized replacement cancels that factor, and its departure weighting controls variable degrees. Thus the claim is a useful quantitative extension of an existing method, not a new proof architecture. No theorem located gives its entire conclusion immediately. A naive regularization is insufficient: adding edges changes the transition probabilities, and cloning/splitting vertices changes n and the simple-path event.

I also checked [Kim–Montenegro–Peres–Tetali, arXiv:0712.0220v2, Theorems 3.2 and 3.6](https://arxiv.org/abs/0712.0220). These birthday bounds for general Markov chains require mixing/transition-probability controls. Applied to the directed-edge chain, their state count is ∑ᵥd(v), and their hypotheses are not supplied by a bounded degree ratio alone. They therefore do not give an immediate alternative proof here. [Alon–Benjamini–Lubetzky–Sodin, math/0610550](https://arxiv.org/abs/math/0610550), addresses regular-expanders' mixing and load estimates, rather than this arbitrary-graph bound. Both primary texts are saved as plain text. The indexed Alon birthday draft at his old author URL has a polylogarithmic loss; direct retrieval returned 404, so I have not treated its full contents or date as verified.

The later-literature search on 13 November 2026 used exact arXiv IDs, the Dozier title, author and Alon–Peres searches, and irregular-graph non-backtracking collision/birthday queries. The arXiv metadata pages still list only v1 for each central paper. OpenAlex work W7204519595 reports zero indexed Dozier citers and the direct citing-works query returns zero; the work record was updated 7 November. Semantic Scholar returns HTTP 429. These are coverage limitations, not evidence that all possible citers were examined.

As an additional route, I followed all four indexed Bencs citers. One is Dozier. The other three, whose full HTML texts were retrieved and whose relevant statements/citation contexts were checked, are:

| Later paper | Result relevant to this search |
|---|---|
| [Pei, Critical and near-critical influence bounds for ferromagnetic Ising models, 2609.20866v1](https://arxiv.org/html/2609.20866v1), Introduction and Theorems 1.1–1.2 | Gives square-root Ising influence bounds by cavity/magnetization arguments. Removing a logarithm in this Ising consequence is not a non-backtracking collision theorem. |
| [Péron–Budzynski, Perfect sampling of Ising spin glasses with bounding chains, 2610.37300v1](https://arxiv.org/html/2610.37300v1), Introduction/results and Bencs citation | Concerns perfect-sampling coalescence and block updates; no general NBW collision resolution. |
| [Ju–Liu–Yin, Fine-Grained Complexity Across the Computational Phase Transition, 2611.02702v1](https://arxiv.org/html/2611.02702v1), §1.2, critical Ising discussion | Cites the earlier non-backtracking influence bound in a spin-system complexity discussion; no bounded-ratio or unrestricted NBW birthday theorem. |

The citation responses and later texts are in sources/. No printed resolution of Conjecture 1.5, or printed theorem covering the full bounded-ratio extension, was found. My novelty verdict is therefore: apparently additional to the verified statements in the literature, with the ideas and substantial proof structure inherited from Dozier; priority is not certified.

The exact statement accepted is: for every finite simple undirected n-vertex graph of minimum degree m≥3 and maximum degree M, every specified directed first edge, and every integer k≥1, the sequential NBW satisfies

\[
 \Pr(\tau>k)\le\min\left\{1,\frac{256\,[M/(m-1)]\,[1+M/(m-1)]\,n}{k^2}\right\},
 \qquad
 \mathbb E\tau\le32\sqrt{[M/(m-1)]\,[1+M/(m-1)]\,n}+2.
\]

This yields the claimed constants for bounded ratio and bounded maximum degree, uniformly over starting edges. The argument supplies neither an unrestricted ratio-independent constant nor a simple-graph counterexample.

To reproduce the independent checks, from this directory with inherited nice 10:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/independent_probabilities.py
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/independent_routing.py
```

The probability suite took 22.59 seconds and measured peak RSS 212,631,552 bytes, about 203 MiB. The routing audit took 4.33 seconds. Both verified nice 10 and used one process without worker threads; numerical-library thread limits were set to one. No dependency installation was needed. All new files are inside this directory. Source files are plain text; no PDFs, scans or paper-page images were saved. No publication, push, external message or global database update was made. LOG.md records the audit.

Task: “You are an independent referee. … Break it if it is wrong. … Write REPORT.md.” — received 13 November 2026, 10:02 Asia/Tbilisi.
