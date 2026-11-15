ACCEPT

The grandparent-graph theorem is correct as stated: for every integer b≥2 and every fixed p∈[0,1], almost surely every pair of distinct Bernoulli bond clusters on GP_b has a finite touching set. I found no fatal error or unresolved mathematical gap in steps (i)–(v). In particular, the infinite branch reduction, the direction of the modular ratio, the closed-boundary estimate, and the sprinkling coupling survive independent checking. This accepts the special-case proof, not a solution of C0159 or a certification of novelty. The submitted report expressly makes no novelty claim.

The scalar equation and finite-border decomposition have printed antecedents. I did not find an exact theorem asserting all-parameter two-point continuity or finite-cardinality touching on GP_b in the primary papers checked. That search result does not establish that the class theorem is new.

Errors and gaps requiring correction: none. The numbered findings below give locations, conclusions, and any useful clarification. Line numbers refer to claim_files/REPORT.md; I did not edit that file or use its code.

1. Lines 74–83, step (i): correct. Both common-neighbour counts, recovery of the parent map, stabilizer indices, degree, and modular ratio check out. No fix required.
2. Lines 87–103, step (ii): correct, including identification of the true infinite-network reliability. No fix required. To make the absence of a minimal/maximal fixed-point ambiguity more explicit, one may append the finite-depth iteration r_0=p and r_{d+1}=1−(1−p)(1−p r_d)^b; its increasing limit is the genuine free-network reliability and is the unique fixed point.
3. Lines 107–117, step (iii): correct. Each omitted cone has at most the two listed attachments, and its effective edge has probability pr, not r. Parallel original edges must remain separate, as the submitted proof says. No fix required.
4. Lines 121–137, step (iv): correct. B(x) is the complete edge boundary, the spacing-three boundaries are disjoint, and closing any selected boundary confines the cluster inside the largest cone. The error estimate is uniform on compact intervals below 1. No fix required.
5. Lines 141–148, step (v): correct. Sprinkling uses right-continuity from above. Countability is used over vertex pairs at a fixed p; there is no unjustified intersection over uncountably many p. No fix required.
6. Lines 159–203, computational evidence: the submitted contact-count simulations are not a direct test of the two-point reliability formula. This is a limitation of the evidence, not a gap in the proof, and the report does not use those simulations as a proof. I supplied independent exact enumeration and direct two-point simulations below.
7. Lines 210–237, literature and value: no incorrect claimed novelty needs retracting. The existing equation in Ménard–Sénizergues and the decomposition in Špakulová should continue to be credited. If this is presented as a new theorem elsewhere, establish priority separately; the present bounded search cannot do that. General nonunimodular finite-cardinality repulsion remains unresolved by this argument.

Here is the mathematical verification in detail.

For a tree edge {x,P(x)}, the common neighbours in GP_b are P²(x) and the b children of x. There are exactly b+1. For a long edge {x,P²(x)}, the only common neighbour is P(x). No other vertex can qualify: edges join only comparable vertices at tree distances one or two. These unequal counts recover the original tree from the unmarked graph. On the recovered tree-neighbour set of x, long-edge adjacency is precisely the star joining P(x) to each child of x. Its centre is unique for b≥2. Thus every graph automorphism preserves P, and conversely every tree automorphism fixing the distinguished end preserves GP_b. That group acts transitively.

Write Γ=Aut(GP_b). Since Γ_x fixes P(x), Γ_x⊂Γ_{P(x)}, and the latter stabilizer permutes its b children transitively. Hence [Γ_{P(x)}:Γ_x]=b and, for left Haar measure,

\[
\Delta(x,P(x)):=\frac{m(\Gamma_{P(x)})}{m(\Gamma_x)}=b,
\qquad
\Delta(x,y)=b^{h(y)-h(x)}.
\]

Here h increases toward the distinguished end. This is the convention used by the submitted report; reversing it would be an error. As a second check, transport one unit to the parent: outgoing mass is 1, incoming mass is b, and each incoming source has relative weight 1/b. The tilted incoming mass is therefore 1. The neighbours of x are its parent, grandparent, b children, and b² grandchildren, giving degree b²+b+2.

For step (ii), remove the direct terminal edge {x,P(x)} from H_x. A child y of x contributes exactly H_y together with the long edge {y,P(x)}. Inside H_y, descendants of y can connect to x through several edges; all those edges are included in its reliability r. The only edge from D(y) to P(x) is {y,P(x)}. For distinct children these branch edge sets are disjoint; their common terminal vertices do not create dependence in bond percolation. There are no edges between incomparable descendant cones. Thus H_x is exactly a direct Bernoulli(p) edge in parallel with b independent series branches having success probability pr. This proves equation (3), including for the infinite graph, because connectivity always has a finite witnessing path. Nothing is connected through an ideal point at infinity.

There is also a direct construction of the physical fixed point. Truncate D(x) at descendant depth d, retaining P(x), with free boundary. Its terminal reliability satisfies

\[
r_0=p,\qquad r_{d+1}=F_p(r_d),\qquad
F_p(t)=1-(1-p)(1-pt)^b.
\]

The finite graphs increase, so r_d increases to the actual r. Every finite path lies in one truncation. The limit solves r=F_p(r). Iteration from 0 gives the same sequence with an initial delay. Iteration from 1 is decreasing and gives the maximal fixed point. For 0<p<1 there is only one fixed point: g(t)=F_p(t)−t is concave, g(0)=p>0 and g(1)=−(1−p)^{b+1}<0. If it had roots 0<r<s, concavity would require the negative slope on [0,r] to be at least the zero slope on [r,s], which is impossible. The free and maximal solutions therefore coincide. At p=0 and p=1 the reliabilities are respectively 0 and 1. The compactness/subsequence argument in the submission proves continuity of r on (0,1).

For step (iii), the finite tree hull S of a,u,v is connected and ancestor-closed relative to a. Each component of T[D(a)]\S is a full descendant cone D(z), where t=P(z) belongs to S. A vertex of D(z) can connect outside that cone only as follows: z to t by a tree edge, z to P(t) by a long edge, or a child of z to t by a long edge. Consequently its only possible external vertices in D(a) are t and s=P(t). If s is not in S then t=a and s is outside D(a); it is not an unlisted terminal inside another omitted cone.

When both terminals belong to S, deleting core-internal edges leaves H_z plus the single edge {z,s}. The latter is independent of H_z, so the two-terminal indicator has probability pr. Distinct omitted cones use disjoint edges, even when their terminals coincide. A one-terminal cone can be discarded because it cannot join different core vertices. Contracting excursions of any finite path gives a walk in the reduced multigraph. Conversely, every open reduced walk expands to finitely many finite paths. This establishes exact preservation of core connectivity and the finite reliability polynomial in p and pr(p). Infinite open components within an omitted cone do not change this argument.

For step (iv), enumerate crossing edges by their deeper endpoint. The vertex x has the crossing edges to P(x) and P²(x). A child y of x has its long edge to P(x). Every deeper vertex has both ancestors inside D(x). This gives exactly

\[
B(x)=\{\{x,P(x)\},\{x,P^2(x)\}\}
\cup\{\{y,P(x)\}:P(y)=x\},\qquad |B(x)|=b+2.
\]

Assign every edge to its deeper endpoint. Edges in B(a_k) have deeper endpoints at heights h(w)+k or h(w)+k−1. The corresponding endpoint-height sets for k and k+3 are disjoint. Hence B(a_0),B(a_3),… are edge-disjoint, proving independence of their all-closed events. There is no exploration-conditioned independence assumption.

Both u and v lie in D(w)⊂D(a_k). If B(a_k) is closed, every path from u remains inside D(a_k), an assertion about the full cluster, not merely a chosen path. On that event connectivity of u,v in the full graph and in D(a_n) agrees whenever k≤n. Thus

\[
0\le \tau_p(u,v)-f_{u,v,a_n}(p)
\le \left[1-(1-p)^{b+2}\right]^{\lfloor n/3\rfloor+1}.
\]

For p∈[α,β]⊂(0,1), replace p on the right by β. The base is strictly below one. The approximation is uniform there, so the continuous finite-core functions converge to a continuous full two-point function. No assertion of a uniform rate up to p=1 is needed.

For step (v), fix u,v and let A_{u,v} be the event that their p-clusters are distinct and have infinitely many edges between them. Conditional on the complete p-configuration, all these edges are closed. To obtain q-percolation, independently open each closed edge with probability (q−p)/(1−p). Conditional on A_{u,v}, at least one of the infinitely many intercluster edges opens with probability one. Monotonicity gives

\[
\tau_q(u,v)-\tau_p(u,v)\ge \mathbb P_p(A_{u,v})\quad(p<q<1).
\]

Right-continuity forces this last probability to be zero. One may take a countable sequence q↓p; a simultaneous assertion for every q is unnecessary. The graph has countably many vertices, so a countable union excludes all infinitely touching pairs at the fixed p. Finite touching-vertex cardinality is equivalent to finitely many intercluster edges by bounded degree. A finite cluster already has only finitely many incident edges. At p=0 all clusters are singletons, and at p=1 there is one cluster. This proves precisely the submitted quantifiers.

Independent computation is recorded in code/independent_checks.py and code/full_graph_checks.py, with outputs in data/exact_checks.json, data/monte_carlo.json, and data/full_graph_checks.json. Neither program imports, executes, or copies claim_files/code. Both use only the Python standard library. Exact enumeration builds the unweighted finite graph directly from parent relations, visits every edge configuration, and tests connectivity by breadth-first search. Its comparison solver updates distributions on connectivity partitions and eliminates vertices after their last incident edge. It is a different procedure from full configuration enumeration.

Fifteen rational tests checked (3): b=2 with descendant depths 0,1,2, and b=3,4 with depth 1, at p=1/4,1/2,3/4. The largest network has 13 edges and 8192 configurations. Nine more rational tests checked the core reduction on a binary depth-two cone, using a root/grandchild pair, two children, and two cousins at the same three p values. All 24 equalities hold exactly. For example:

| Finite network, p=1/2 | Exhaustive reliability | Reduction reliability |
|---|---:|---:|
| H_x, b=2, depth 1 | 23/32 | 23/32 |
| H_x, b=2, depth 2 | 6511/8192 | 6511/8192 |
| D(a), depth 2, root/grandchild | 21/32 | 21/32 |
| D(a), depth 2, two children | 529/1024 | 529/1024 |
| D(a), depth 2, two cousins | 441/1024 | 441/1024 |

Buffered structural enumeration for b=2,3,4 independently scanned edges to verify degrees, both common-neighbour counts, all attachments of an off-core cone, five successive cone boundaries, and disjointness of the boundaries three levels apart. Boundary vertices were kept away from the artificial top and bottom.

The first Monte Carlo experiment used full binary descendant cones of depth 10: 2047 vertices, 4090 edges, 5000 independent configurations for each p=.28,.55,.76. It checked three fixed pairs at each p against both the finite-depth formula and the infinite-cone formula. All nine deviations from the finite-depth prediction are within 2.40 binomial standard errors. The maximum difference between the finite-depth and infinite-cone formulas is 1.41×10^−5. The data record every pair, seed, prediction, observation, and standard error.

The second experiment checks the full-graph two-point function rather than only in-cone connectivity. Take u,v to be the two tree children of w, retain the ancestor core up to a_180=P^180(w), and attach explicit off-core cones extending six generations below each off-core child. This is a finite subgraph of GP_2, with 23,424 vertices and 46,845 edges. It has free boundaries. For each p, simulate 2000 independent configurations. Evaluate the same finite core twice: first with exact finite-depth branch reliabilities, then with infinite-branch r(p). The difference is the bottom truncation bias. Equation (5) bounds the remaining difference to full GP_2.

| p | Infinite-branch core formula | Explicit finite-branch formula | Monte Carlo | Standard error | Ancestor error bound |
|---:|---:|---:|---:|---:|---:|
| .22 | .172176809 | .172152340 | .1780 | .00844 | 5.67×10^−13 |
| .32 | .403385228 | .403212177 | .4085 | .01097 | 4.24×10^−7 |
| .42 | .658140719 | .657947742 | .6500 | .01061 | 6.59×10^−4 |

The three Monte Carlo deviations are within .75 standard errors. Bottom biases are respectively 2.45×10^−5, 1.74×10^−4, and 1.93×10^−4. These computations test the formula directly; they do not identify finite components with infinite clusters. Displayed formula values use floating arithmetic; the theoretical ancestor bounds are analytic bounds, not claims of interval-certified rounding of every displayed decimal.

Reproduction commands, run from this directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/independent_checks.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/full_graph_checks.py
```

Both calculation processes verified inherited nice 10 and used one thread. The final exact/in-cone run took 9.87 s and peaked at 45,170,688 bytes RSS; the full-graph run took 63.13 s and peaked at 70,565,888 bytes. Seeds and source-code hashes are saved with the outputs. No language-model workers or subagents were started.

The literature result follows. Sixteen paper texts were downloaded independently into sources/. The download helper sends PDF bytes directly to pdftotext over pipes, saving only UTF-8 text. Source headers and sources/INDEX.txt record URLs and hashes; form feeds separate PDF pages. sources/LITERATURE_SEARCH.txt records the search scope and its limits.

BCRTT v2, Question 1.1, p. 3, asks exactly:

> Does a quasi-transitive graph necessarily exhibit cluster repulsion for any value of p ∈ [0, 1]?

The same wording occurs in v1 on p. 2. Its preceding definition requires a finite set of vertices of one cluster within unit distance of the other. Thus the question concerns cardinality, not modular weight. [BCRTT v2](https://arxiv.org/html/2509.10631v2)

HPS, Question 3, author manuscript p. 28, asks exactly:

> Does a quasi-transitive graph necessarily exhibit cluster repulsion for any p ∈ [0, 1]?

The published locator is p. 87 in Progress in Probability 44 (1999), 69–90. The continuity observation is the following paragraph of the same question. The robust-property result is Theorem 1.8 in this manuscript, cited as Theorem 4.1.6 in the published version. [HPS author manuscript](https://www.math.ucla.edu/~rhs/papers/hps.pdf)

The Häggström–Jonasson survey has an unnumbered discussion, rather than a separately numbered question, at the end of Section 5, printed pp. 308–309. It states the conjecture for all transitive graphs, notes Timár's unimodular result, and ends: “The nonunimodular case remains open.” [Survey](https://arxiv.org/abs/math/0612812)

| Primary reference and exact locator | What it establishes and its bearing on this audit |
|---|---|
| Timár, *Neighboring clusters in Bernoulli percolation*, Ann. Probab. 34 (2006), 2332–2343, Theorem 1.1; saved reprint p. 1 | Finite-cardinality touching for quasi-transitive unimodular graphs. GP_b has nonunimodular full automorphism group, so this theorem does not directly apply. [Paper](https://arxiv.org/abs/math/0702873) |
| Bell–Chu–Rodgers–Terlov–Tserunyan, arXiv:2509.10631v1, 12 September 2025, Theorem 1.2, p. 3; v2, 4 November 2026, Theorem 1.2, p. 3 | v1 states finite modular weight for touching of heavy clusters; v2 states it for distinct infinite clusters. The latter still permits infinite light touching sets. Neither theorem supplies the claimed GP cardinality conclusion. v2 Lemma 3.5, pp. 12–13, is exactly the sprinkling implication used here. [Versions](https://arxiv.org/abs/2509.10631) |
| HPS, manuscript Section 6, pp. 18–19; Section 9, p. 27; Question 3, p. 28 | Discusses GP, the distinguished uppermost vertex of a cluster, and p_c<p_h=p_u=1. States the general continuity criterion. No GP all-p continuity or finite-touching theorem was found there. [Manuscript](https://www.math.ucla.edu/~rhs/papers/hps.pdf) |
| Peres–Pete–Scolnicov, *Critical percolation on certain non-unimodular graphs*, arXiv:math/0501532v3, Section 2, Theorem 2.3 and Note 2.4, p. 5 | Decorated-tree results: no critical infinite clusters and exponential spatial decay of two-point connectivity for each p<1. This is decay in vertex distance, not a stated continuity theorem in p or finite-cardinality repulsion theorem. [Paper](https://arxiv.org/abs/math/0501532) |
| Tang, *Heavy Bernoulli-percolation clusters are indistinguishable*, Ann. Probab. 47 (2019), 4077–4115; Theorems 1.1, 1.3 and 2.9, saved pp. 2,3,9 | Heavy-cluster indistinguishability, the connectivity-decay characterization of p_u, and HPS robust properties. Does not state the target GP conclusion. The consequence excluding coexistence of infinite light and heavy clusters is explicit on p. 9. [Paper](https://arxiv.org/abs/1809.01284) |
| Hutchcroft, *Percolation on hyperbolic graphs*, GAFA 29 (2019), 766–810; Theorems 1.3,1.4,2.1, saved pp. 2,3,7 | Nonuniqueness, triangle condition, and the stronger operator-threshold inequality. GP_b is quasi-isometric to its underlying tree and is hyperbolic, but these theorems do not assert the desired all-p continuity or touching result. [Paper](https://arxiv.org/abs/1804.10191) |
| Hutchcroft, *Nonuniqueness and mean-field criticality for percolation on nonunimodular transitive graphs*, JAMS 33 (2020), 1101–1165; Theorems 1.2 and 1.5, saved pp. 4,6 | Nonempty light-cluster/nonuniqueness phase and critical estimates. These are not a finite-cardinality touching theorem. [Paper](https://arxiv.org/abs/1711.02590) |
| Timár, *Percolation on nonunimodular transitive graphs*, Ann. Probab. 34 (2006), 2344–2364; Section 3.1 and Sections 4–5 | Grandmother/GP examples, critical percolation, and heavy/light phases; no target repulsion theorem found. [Paper](https://arxiv.org/abs/math/0702875) |
| Terlov–Timár, *Weighted-amenability and percolation*, arXiv:2502.02560v2, Theorem 1.8, p. 6; Example 2.8, p. 9 | The heaviness transition is continuous under weighted nonamenability. GP is explicitly weighted amenable, so this is neither a GP application nor a theorem about two-point continuity. [Paper](https://arxiv.org/abs/2502.02560v2) |
| Hutchcroft–Pan, *Dimension jump at the uniqueness threshold for percolation in ∞+d dimensions*, arXiv:2412.15895, introduction pp. 1–7; *Percolation at the uniqueness threshold via subgroup relativization*, arXiv:2409.12283, introduction pp. 1–9 and Theorem 1.1, p. 3 | These study dimension, operator thresholds, and nonuniqueness for products and lamplighter groups. No GP touching or all-p two-point continuity theorem was found. [Dimension paper](https://arxiv.org/abs/2412.15895), [Subgroup paper](https://arxiv.org/abs/2409.12283) |
| Hermon–Hutchcroft, *Supercritical percolation on nonamenable graphs: isoperimetry, analyticity, and exponential decay of the cluster size distribution*, Section 5.1, saved p. 28 | Explicitly explains right jumps of the untruncated two-point function at p_u when infinitely many infinite clusters occur there. Thus the continuity input proved here is substantive and cannot be assumed on general transitive graphs. [Paper](https://arxiv.org/abs/1904.10448) |
| Špakulová, *Critical percolation of virtually free groups and other tree-like graphs*, Ann. Probab. 37 (2009), 2262–2296, Section 5.3, saved pp. 23–24 | Already decomposes the binary GP graph into finite pieces with border sets of size two to compute p_c. This is a clear antecedent of the proof technique, but not a stated finite-touching theorem. [Paper](https://arxiv.org/abs/0801.4153) |
| Ménard–Sénizergues, *Percolation on grandparent graphs of Bienaymé trees*, arXiv:2611.09762v1, 6 November 2026, equation (7) and Theorem 10, p. 9 | Equation (7) is x=1−p+p(1−p)ϕ(x). For deterministic b offspring, ϕ(x)=x^b and x=1−pr transforms it exactly into (3). Thus that scalar equation and its uniqueness are already in print. Theorem 10 concerns p_c, not the touching conclusion. [Paper](https://arxiv.org/abs/2611.09762v1) |

The class theorem is a valid, relatively elementary special-case result built from a two-terminal reduction and bounded independent upward cutsets. The exact scalar equation is not new, and the finite-border method is not new. I found no exact published theorem in the checked literature to cite as already proving its final GP_b conclusion, and I cannot certify that conclusion as new. The submission's explicit restraint about novelty is appropriate.

The remaining question is finite cardinality of touching sets on arbitrary nonunimodular transitive, or more generally quasi-transitive, graphs. Finite weight does not settle it: a sequence of vertices with weights b^−n may be infinite with finite total weight. On GP_b, p_h=p_u=1 makes the nontrivial phase a light-cluster phase, so the special-case proof does address an obstruction left by weighted repulsion. General light–light and heavy–heavy cardinality questions remain; no mixed heavy/infinite-light phase is required in the fixed-parameter Bernoulli setting. The two-terminal recursion and the bounded independent upward boundaries used here have not been supplied for those general graphs.

Task: “Break it if it is wrong.” — received 13 November 2026, approximately 08:37 Asia/Tbilisi; independent referee audit of C0159.
