PARTIAL

C0159: cluster repulsion beyond unimodularity

The general conjecture remains unresolved by this work. No full resolution was found in the literature searched through 13 November 2026. Below is a complete proof for every regular grandparent graph at every fixed Bernoulli bond parameter. This includes a natural nonunimodular class whose infinite clusters are light below p=1. The proof uses elementary network reductions and sprinkling, independently of the weighted repulsion theorem. No claim of novelty is made for this class result.

Statement and conventions.

Let G=(V,E) be infinite, connected, locally finite, and transitive. Fix p and retain each edge independently with probability p. All distances are distances in G, including closed edges. For distinct open clusters C,D, define

\[
\tau(C,D)=\{x\in C:\exists y\in D,\ \{x,y\}\in E\}.
\]

The conjecture asks whether, almost surely, every pair of distinct infinite clusters has finite touching set. This means: for each fixed p, all pairs simultaneously. A single probability-one event for every real p is not asserted. Bounded degree makes finiteness of either touching set equivalent to finiteness of the set of edges between the clusters.

The survey passage is the last paragraph of Section 5, printed pp. 308–309, PDF pp. 20–21. Section 6, read as requested, concerns nonuniqueness for suitably generated Cayley graphs: Lemmas 6.1–6.2 and Theorem 6.3, printed pp. 309–311. The repulsion conjecture there is unnumbered. Timár's exact statement is Theorem 1.1, Annals of Probability 34 (2006), p. 2332, or p. 1 of the saved reprint; it covers quasi-transitive unimodular graphs. The proof here is for bond percolation.

The literature gap.

Fix a closed quasi-transitive group Gamma of automorphisms, a left Haar measure m, and a reference vertex o. Write

\[
w_o(x)=m(\Gamma_x)/m(\Gamma_o),\qquad
W_o(A)=\sum_{x\in A}w_o(x).
\]

Heavy means infinite W; light means finite W, including for infinite sets. Changing o multiplies all weights by a positive constant. The main BCRTT statement uses Gamma=Aut(G); subgroup variants require specifying the acting group separately.

Bell–Chu–Rodgers–Terlov–Tserunyan, arXiv:2509.10631v1 (12 September 2025), Theorem 1.2, p. 3, proves finite weight of touching sets for two heavy clusters on nonunimodular quasi-transitive graphs. Version 2 (4 November 2026), Theorem 1.2, p. 3, states the conclusion for all distinct infinite clusters on every quasi-transitive graph. Its Question 1.1 on that page still asks for finite cardinality. The formulations have the same substantive content: a subset of a light cluster is already light.

There is no heavy–infinite-light case at a fixed p in this Bernoulli model. HPS's robust-property theorem gives noncoexistence, explicitly recorded on author manuscript p. 27; Tang repeats it after Theorem 2.9, saved PDF p. 9. Heaviness is invariant and robust: removing one edge leaves at most two components, at least one of which has infinite total weight if the original did. Apply that literature theorem. Thus the remaining cardinality cases are heavy–heavy and light–light, not a mixed case. This application does not purport to reprove the robust-property theorem itself.

An elementary consequence of finite weight is

\[
|A\cap\{x:w_o(x)\geq\varepsilon\}|\leq W_o(A)/\varepsilon<\infty
\quad(\varepsilon>0).
\tag{1}
\]

Each summand on that subset is at least epsilon. An infinite touching set allowed by the weighted result would therefore escape every positive weight cutoff. The distinction is real: a downward ray in a b-ary oriented tree has weights 1,b^-1,b^-2,... and finite sum. This is a deterministic illustration of the gap, not a percolation counterexample. For a unimodular quasi-transitive action the weights take finitely many positive values, so finite weight implies finite cardinality.

Why ordinary mass transport fails.

For a transitive action set Delta(x,y)=m(Gamma_y)/m(Gamma_x). The tilted mass transport identity for a nonnegative equivariant random transport F is

\[
\mathbb E\sum_y F(o,y)
=\mathbb E\sum_x F(x,o)\Delta(o,x).
\tag{2}
\]

For a quasi-transitive action choose orbit representatives o_i and root probabilities a_i>0. Choose the root with those probabilities and use

\[
\Delta_a(x,y)=\frac{a(y)m(\Gamma_y)}{a(x)m(\Gamma_x)},
\]

where a(x) is the probability of x's orbit. This is Tang, Proposition 3.2, saved PDF p. 9. Hutchcroft's root-distribution formulation is Proposition 2.2, saved PDF p. 12. The ratio convention is explicit here to prevent reversing the tilt.

On a grandparent graph, send one unit from every vertex to its tree parent toward the distinguished end. Outgoing mass is 1, incoming mass is b. Each of the b incoming sources has relative weight 1/b, so the tilted incoming mass is 1, as (2) requires. The unweighted equality is false.

In Timár's bounded-outgoing-mass arguments, infinitely many unweighted contributors force a contradiction at a bottleneck. After tilting they can have summable weights. If each touching point sends an equal share to an assigned finite set F, its contribution at z in F is proportional to W_o(tau)/(w_o(z)|F|), rather than |tau|. Infinite cardinality alone no longer forces divergence. A forest with many ordinary ends also need not have weighted exponential growth. BCRTT develops further machinery for that growth obstruction; (2) alone does not prove its repulsion result.

The class theorem.

Let b>=2, let T be the (b+1)-regular tree, and fix an end xi. Let P(x) be the neighbor toward xi. Define GP_b by keeping the tree edges and adding the edge {x,P^2(x)} for every x.

Theorem. For every fixed p in [0,1], Bernoulli bond percolation on GP_b almost surely has finite touching sets between all distinct clusters.

Proof, step 1: this is a transitive nonunimodular graph.

End-preserving tree automorphisms act transitively and preserve all added edges. The orientation can also be recovered from the unmarked graph. A tree edge has b+1 common neighbors, while an added edge has exactly one. This recovers T. Among the tree neighbors of any vertex x, the added-edge adjacency relation is the star with center P(x) and b leaves, the children of x. Since b>=2 its center is unique, so every automorphism preserves P.

The stabilizer of x fixes P(x), whereas the stabilizer of P(x) permutes its b children transitively. Therefore

\[
|\Gamma_xP(x)|=1,\quad |\Gamma_{P(x)}x|=b,\quad
m(\Gamma_{P(x)})/m(\Gamma_x)=b.
\]

The graph is nonunimodular. If height h increases by one under P, with h(o)=0, its weights are b^h(x). Its degree is b^2+b+2.

Step 2: reliability of a descendant cone with one extra parent.

Let D(x) consist of x and all its tree descendants, and let H_x be the induced graph on D(x) union {P(x)}. Define

\[
r(p)=\mathbb P_p(x\leftrightarrow P(x)\text{ inside }H_x).
\]

There is a direct edge xP(x). If it is closed, each child y of x gives a route when y connects to x inside H_y and the grandparent edge yP(x) is open. These b events have probability pr(p), are mutually independent, and are independent of the direct edge. Their edge sets are disjoint; sharing the terminal x is harmless for bond percolation. No edges join different child cones. Hence

\[
r=1-(1-p)(1-pr)^b.\tag{3}
\]

The decomposition is exact for infinite cones: any connection has a finite witnessing path, which contracts to a path in this parallel network. Conversely any terminal connection in a branch supplies a finite witnessing path.

For 0<p<1 set g_p(t)=1-(1-p)(1-pt)^b-t on [0,1]. It is concave, g_p(0)=p>0, and g_p(1)=-(1-p)^(b+1)<0. It has exactly one zero. Indeed, if 0<r<s were two zeros, concavity would require the secant slope on [0,r], namely -p/r<0, to be at least the zero slope on [r,s], a contradiction. Existence follows from continuity. The actual reliability solves (3), so it is the unique zero.

This zero r(p) is continuous on (0,1). For p_n tending to p, every subsequential limit of the bounded sequence r(p_n) solves (3) at p. Uniqueness makes every such limit r(p), proving convergence.

Step 3: an exact finite network for fixed vertices in an infinite downward cone.

Fix u,v in D(a). Let S be the finite tree hull of u,v,a. Every component of T[D(a)] minus S is D(z), for an off-core child z of some t in S; there are finitely many such components. Its attachment vertices in the grandparent graph are t=P(z) and, if it lies in S, s=P(t). There are no other attachments.

If s is absent, the component has only one attachment and cannot affect connections between core vertices. If s is present, consider its two-terminal network with all edges internal to S excluded. Its only edge from the interior to s is zs. Its remaining z-to-t reliability is r(p). It therefore connects s to t with probability pr(p). Replace it by one auxiliary edge with that probability. A parallel original core edge, if present, is kept separately.

These networks use disjoint edge sets and are independent of the original edges within S. Replacing each by its connection indicator preserves core connectivity: contract a finite path to a core walk, or expand a finite core walk using finite terminal paths. Consequently

\[
f_{u,v,a}(p)=\mathbb P_p(u\leftrightarrow v\text{ in }GP_b[D(a)])
\]

is a finite multigraph reliability polynomial in the probabilities p and pr(p). It is continuous on (0,1). No downward branch has been truncated; each has been integrated out exactly.

Step 4: the missing ancestors have a uniformly small effect.

Let w be the nearest common tree ancestor of u and v, and a_n=P^n(w). The edge boundary of D(x) is exactly

\[
B(x)=\{\{x,P(x)\},\{x,P^2(x)\}\}
\cup\{\{y,P(x)\}:P(y)=x\}.
\tag{4}
\]

It has b+2 edges. The sets B(a_0),B(a_3),B(a_6),... are pairwise edge-disjoint, since an edge spans at most two tree levels toward xi. Each is all closed with probability (1-p)^(b+2), independently of the others. If a selected B(a_k) with k<=n is closed, the full-graph cluster of u stays in D(a_k), hence in D(a_n). Therefore

\[
0\leq\mathbb P_p(u\leftrightarrow v)-f_{u,v,a_n}(p)
\leq[1-(1-p)^{b+2}]^{\lfloor n/3\rfloor+1}.
\tag{5}
\]

These are predetermined disjoint edge sets; no independence conditional on a cluster exploration is being assumed. On a compact interval [alpha,beta] inside (0,1), the upper bound is at most [1-(1-beta)^(b+2)]^(floor(n/3)+1), which tends to zero. Thus the full two-point function is a uniform limit of continuous functions there. It is continuous at every p in (0,1), for every fixed u,v.

Step 5: sprinkling excludes infinite touching.

This implication is HPS's observation, also BCRTT v2 Lemma 3.5, pp. 12–13. For completeness, suppose the p-clusters of fixed u,v are distinct and have infinitely many edges between them on an event A of positive probability. In the monotone coupling with q>p, conditional on the entire p-configuration, each closed edge opens independently with probability (q-p)/(1-p)>0. On A, infinitely many independent opportunities join the two clusters, so u and v connect at q with conditional probability one. They were disconnected at p. Hence

\[
\mathbb P_q(u\leftrightarrow v)-\mathbb P_p(u\leftrightarrow v)
\geq\mathbb P_p(A).
\]

Right continuity as q decreases to p forces P_p(A)=0. The countable union over all vertex pairs excludes every infinitely touching cluster pair. At p=0 singleton clusters have finite degree; at p=1 there is only one cluster. This proves the theorem. QED.

The simulation parameters are genuinely in a nonuniqueness regime.

For 1/b<p<1 choose a downward tree ray and, at each ray vertex, a child z off the ray. The cones D(z) are an infinite antichain. For each, require all b+2 boundary edges in (4) to be closed and the internal open tree edges to contain an infinite path from z. The latter has positive probability: the offspring law is Binomial(b,p), with mean bp>1. More explicitly, its extinction generating function (1-p+pt)^b has a fixed point below 1 because its derivative at 1 is bp>1, and iteration from 0 gives the extinction probability.

These events have a common positive probability and use disjoint edge sets, so infinitely many occur almost surely. Each gives a separate infinite grandparent cluster isolated in its cone. Thus every p in (1/b,1) has infinitely many infinite clusters. For b=2 this proves the claim for .55,.65,.75 without estimating pc. HPS additionally records pc<ph=pu=1 for grandparent graphs, author PDF p. 27. Thus the nontrivial regime of the class theorem concerns light clusters.

Checks and computation.

The proof was audited by separately checking cone boundary edges, attachment vertices, disjoint edge sets, uniqueness of the fixed point, and uniformity in p of (5). These are mathematical deductions, not simulation conclusions.

`python3 code/check_proof.py` performs exact rational finite checks. Nine terminal-network checks compare complete configuration enumeration with (3), including a 13-edge network with 8192 configurations. Three separate core calculations check replacement by independent parallel edges. Probabilities are 1/5,11/20,4/5. Direct boundary enumeration checks (4) and disjointness for b=2,3,4. All 15 checks passed; details are in `data/proof_checks.json`.

`python3 code/audit_data.py` independently checks the 36 depth-10 configurations using breadth-first search instead of union-find. Component counts, large-pair counts, contact totals, and 396 per-level counts agree. It also verifies all 48 tracked-pair rows against their separate vertex-level files. Results are in `data/data_audit.json`.

`python3 code/simulate.py` simulates binary descendant cones with free boundary at depths 10,12,14, having 2047,8191,32767 vertices and 4090,16378,65530 edges. Large means at least 64 vertices. Twelve fixed seeds, three p values, and three depths give 108 samples. Nested depths and increasing p share independent uniform edge labels. Level is depth below the cone top, whose modular weight is normalized to 1; a level-ell vertex has weight 2^-ell.

The table gives means over 12 samples, except the last column, which is the maximum observed. A contact is an underlying edge between different large components.

| p | Depth | Large components | Adjacent large pairs | Contact edges | Maximum edges for one pair |
|---|---:|---:|---:|---:|---:|
| .55 | 10 | 3.00 | 2.17 | 7.92 | 6 |
| .55 | 12 | 7.25 | 6.92 | 25.17 | 8 |
| .55 | 14 | 23.67 | 24.75 | 94.75 | 14 |
| .65 | 10 | 1.75 | .75 | 3.00 | 4 |
| .65 | 12 | 3.08 | 2.25 | 8.75 | 8 |
| .65 | 14 | 10.58 | 10.08 | 40.17 | 12 |
| .75 | 10 | 1.08 | .08 | .33 | 4 |
| .75 | 12 | 1.33 | .33 | 1.50 | 6 |
| .75 | 14 | 3.00 | 2.00 | 7.92 | 6 |

`data/contacts_by_level.csv` counts contact edges at their deeper endpoint's level. `data/cluster_pairs.csv` records the two touching-vertex cardinalities and weights separately. For another view, select a pair with most contacts at depth 10, when one exists, and follow the same two vertex anchors through larger depths. Sixteen pairs were selected; all stayed distinct with unchanged contact counts across these windows. Their vertex-level touching counts and weights are in `data/anchored_levels.csv`.

At depth 14 the mean contact counts by level are:

| Deeper endpoint level | p=.55 | p=.65 | p=.75 |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | .08 | 0 | 0 |
| 2 | 1.00 | .33 | 0 |
| 3 | 2.08 | .83 | .17 |
| 4 | 3.25 | 1.17 | .17 |
| 5 | 5.25 | 1.83 | .33 |
| 6 | 10.33 | 3.17 | .50 |
| 7 | 19.25 | 8.00 | 1.08 |
| 8 | 30.42 | 14.58 | 3.17 |
| 9 | 19.42 | 9.58 | 2.50 |
| 10 | 1.75 | .33 | 0 |
| 11 | 1.25 | .17 | 0 |
| 12 | .50 | .17 | 0 |
| 13 | .17 | 0 | 0 |
| 14 | 0 | 0 | 0 |

The 64-vertex filter and the bottom boundary strongly affect these profiles; the absence of contacts at the last level is not an infinite-graph conclusion.

Finite components are not identified with infinite clusters. Paths outside the window can merge them, the top boundary is artificial, and most vertices are near the bottom. Aggregate contacts also grow because more pairs are sampled. The observations establish neither an infinite-graph bound nor an asymptotic law; they are consistent with the proved class result.

This run used one thread, inherited nice 10, 49,250,304 bytes peak RSS (about 47 MiB), and 1.419 seconds. Seeds and resource measurements are in `data/simulation_metadata.json`. Use `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` when reproducing; both programs use only the standard library and no worker processes.

Literature audit and exact locations.

All source papers below are saved as plain extracted text under `sources/`, with URLs, response hashes, and PDF page separators. Reprint PDF pagination is distinguished from journal pagination. `sources/SEARCH_LOG.txt` records searches and limitations. The source filenames identify the corresponding authors.

| Reference | Result and checked location | Bearing on C0159 |
|---|---|---|
| Häggström–Jonasson, Probability Surveys 3 (2006), 289–344; DOI [10.1214/154957806000000096](https://doi.org/10.1214/154957806000000096) | End of Section 5, printed 308–309 / PDF 20–21; Section 6, printed 309–311 / PDF 21–23 | Source statement and conventions. |
| Häggström–Peres–Schonmann, *Percolation on transitive graphs as a coalescent process: relentless merging followed by simultaneous uniqueness*, Progress in Probability 44 (1999), 69–90; [author manuscript](https://www.math.ucla.edu/~rhs/papers/hps.pdf) | Question 3, published p. 87 / author PDF p. 28. Robust-property Theorem 1.8, author PDF p. 7, cited subsequently as book Theorem 4.1.6. Noncoexistence and grandparent ph=pu=1: author PDF p. 27 | Conjecture, continuity criterion, and no mixed heavy/light phase. |
| Timár, *Neighboring clusters in Bernoulli percolation*, Ann. Probab. 34(6) (2006), 2332–2343; DOI [10.1214/009117906000000485](https://doi.org/10.1214/009117906000000485) | Theorem 1.1, published p. 2332 / saved PDF p. 1; transport scheme pp. 2–3; Lemmas 2.3–2.5 and proof pp. 5–11 | Unimodular resolution. Saved electronic reprint has 13 pages. |
| Bell–Chu–Rodgers–Terlov–Tserunyan, *Heavy repulsion of clusters in Bernoulli percolation*, [arXiv:2509.10631](https://arxiv.org/abs/2509.10631) | Both versions: Theorem 1.2, p. 3. Version 2: Question 1.1 p. 3; Theorem 2.1 p. 6; Lemma 3.5 pp. 12–13 | Finite weight. Cardinality conjecture still posed in the 4 November 2026 revision. |
| Hutchcroft, *Nonuniqueness and mean-field criticality for percolation on nonunimodular transitive graphs*, JAMS 33(4) (2020), 1101–1165; [arXiv:1711.02590](https://arxiv.org/abs/1711.02590) | Theorem 1.2, saved PDF p. 4; Theorem 1.5 p. 6; Proposition 2.2 p. 12 | pc<pu; pc<ph for the transitive action of Theorem 1.5; tilted transport. |
| Tang, *Heavy Bernoulli-percolation clusters are indistinguishable*, Ann. Probab. 47(6) (2019), 4077–4115; DOI [10.1214/19-AOP1354](https://doi.org/10.1214/19-AOP1354) | Theorem 1.1, saved arXiv PDF p. 2; Theorem 2.9 and Proposition 3.2 p. 9; Proposition 4.7 p. 17 | Indistinguishability, noncoexistence, TMTP, and behavior at ph; no cardinality theorem. |
| Lyons–Schramm, *Indistinguishability of percolation clusters*, Ann. Probab. 27(4) (1999), 1809–1836; [author publication](https://rdlyons.pages.iu.edu/pdf/indis-pub.pdf) | Theorem 1.1, printed p. 1809 / PDF p. 1; Theorem 3.3, printed p. 1815 / PDF p. 7 | Individual-cluster indistinguishability, used in Timár's proof. |
| Benjamini–Lyons–Peres–Schramm, *Group-invariant percolation on graphs*, GAFA 9 (1999), 29–66; [author manuscript](https://rdlyons.pages.iu.edu/pdf/invar.pdf) | Theorem 7.2, author PDF p. 30 | Ends, pc, and expected degree in invariant forests under unimodularity. |
| Timár, *Percolation on nonunimodular transitive graphs*, Ann. Probab. 34(6) (2006), 2344–2364; DOI [10.1214/009117906000000494](https://doi.org/10.1214/009117906000000494) | Introduction, saved PDF pp. 1–2; heavy/light and level framework | Nonunimodular phases, not a repulsion resolution. |
| Pete, *A note on percolation on Z^d: isoperimetric profile via exponential cluster repulsion*, ECP 13 (2008), 377–392; [arXiv:math/0702474](https://arxiv.org/abs/math/0702474) | Theorem 1.1 and discussion, saved PDF p. 2 | Quantitative finite-cluster versus infinite-cluster repulsion on Z^d, a different question. |
| Hutchcroft, *Transience and anchored isoperimetric dimension of supercritical percolation clusters*, [arXiv:2207.05226](https://arxiv.org/abs/2207.05226) | Propositions 2.1 and 2.4, saved PDF pp. 6 and 8 | Sprinkled/martingale finite-cluster bounds, not infinite–infinite cardinality. |
| Terlov–Timár, *Weighted-amenability and percolation*, [arXiv:2502.02560v2](https://arxiv.org/abs/2502.02560v2), 14 September 2025 | Theorem 1.8, p. 6 | No heavy cluster at ph under its weighted nonamenability and transitivity assumptions. |
| Hutchcroft–Pan, *Dimension jump at the uniqueness threshold for percolation in infinity+d dimensions*, [arXiv:2412.15895](https://arxiv.org/abs/2412.15895) | Introduction and nonunimodular framework, saved PDF pp. 1–7 | Dimension and thresholds for products with trees; no cardinality conclusion found. |
| Hutchcroft–Pan, *Percolation at the uniqueness threshold via subgroup relativization*, [arXiv:2409.12283](https://arxiv.org/abs/2409.12283) | Theorem 1.1, saved PDF p. 3; introduction pp. 1–9 | Nonuniqueness at pu for lamplighter groups and related results. |
| Tserunyan–Tucker-Drob, *The Radon–Nikodym topography of acyclic measured graphs*, [arXiv:2512.24741v2](https://arxiv.org/abs/2512.24741v2), 26 October 2026 | Section 1.E, p. 7 | Verified forward citation of BCRTT, describing its weighted conclusion and inputs. |
| Higgins–Spaas–Tenenbaum, *Spectral Theory for Borel PMP Graphs*, [arXiv:2602.05185](https://arxiv.org/abs/2602.05185), 2026 | Introduction pp. 1–6; reference BCR+25b, p. 42 | Verified forward citation; measured spectral/combinatorial results, not cardinality repulsion. |
| Špakulová, *Critical percolation of virtually free groups and other tree-like graphs*, Ann. Probab. 37 (2009), 2262–2296; [arXiv:0801.4153](https://arxiv.org/abs/0801.4153) | Section 5.3, saved PDF pp. 23–24 | Earlier finite-boundary decomposition of grandparent percolation for computing pc. Relevant prior technique. |
| Ménard–Sénizergues, *Percolation on grandparent graphs of Bienaymé trees*, [arXiv:2611.09762v1](https://arxiv.org/abs/2611.09762v1), 6 November 2026 | Equation (7) and Theorem 10, p. 9 | Threshold calculation. For deterministic b offspring, x=1-pr in (3) gives exactly its equation (7), independently checking the cone equation. |

Limits.

Finite cardinality is not proved here for arbitrary heavy–heavy or light–light pairs on a nonunimodular transitive graph. No counterexample was constructed. The grandparent proof depends on two special facts: off-core components have at most two attachment vertices with a unique continuous reliability law, and the route toward the distinguished end has independent bounded closed cutsets. Neither step has been established here for Diestel–Leader graphs or general products with nonunimodular factors. The literature search supports reporting an unresolved general problem, not a claim that no later unindexed result exists.

Continuity of the two-point function cannot simply be assumed on general transitive graphs. Hermon–Hutchcroft, *Supercritical percolation on nonamenable graphs: isoperimetry, analyticity, and exponential decay of the cluster size distribution*, Inventiones Mathematicae 224 (2021), 445–486, Section 5.1, saved PDF p. 28 ([arXiv:1904.10448](https://arxiv.org/abs/1904.10448), saved as `hermon_hutchcroft_2021.txt`), explains jumps at pu when infinitely many infinite clusters occur there. The proof above establishes its continuity input specifically for grandparent graphs. Also, a Cayley graph times a regular tree admits a transitive unimodular action and is already covered by Timár, even though it also admits a nonunimodular subgroup preserving a tree end.

Task: “Open problem C0159” — received 13 November 2026, approximately 08:07 Asia/Tbilisi.
