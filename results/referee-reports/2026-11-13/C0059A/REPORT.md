PARTIAL

# C0059: random walk on the dual of an infinite Boltzmann map

The requested transience statement is **not proved or disproved here**. No published resolution was located in the literature search. The partial result is an explicit sufficient criterion, with proof, reducing transience to an energy functional of the conditioned perimeter walk and elementary uniform cyclic updates. Its required bound remains unproved throughout the requested range. No new subrange is settled.

The report also gives the dense-phase argument, the obstruction at and above $a=2$, a rigorous layer-cutset inequality, and reproducible simulations. Numerical observations are evidence about the sampled finite explorations, not a proof of an infinite-volume assertion.

## 1. Sources, versions, and the precise question

Two different versions of Curien's notes were recovered and saved in full as plain text:

- [Saint-Flour draft](sources/curien_saintflour.txt), 252 PDF pages, downloaded from an older [direct author-linked Dropbox URL](https://dl.dropboxusercontent.com/s/bfjbuxiv4ms1gdl/StFlour.pdf). The relevant chapter is Chapter 15, “Simple random walks,” pp. 206–215. Its **Open Question 15.10, p. 213**, asks whether the dual is transient for type $a\in[2,5/2)$.
- [Earlier Peccot draft](sources/curien_peccot.txt), 104 PDF pages, from [Curien's author site](https://www.imo.universite-paris-saclay.fr/~nicolas.curien/cours/peccot.pdf). Chapter VIII, printed pp. 86–90, contains the same question on **PDF page 93, printed page 89**. This is the source matching the page in the request. Its question reads: “Let $q$ be of type $a\in[2;5/2)$, it is the case that $\mathfrak m^\dagger$ is transient under $\mathbb P^{(1)}_\infty$?” It describes the 2016 Geneva/Peccot courses; it is not the 2023 book.

The 2023 book is N. Curien, *Peeling Random Planar Maps: École d'Été de Probabilités de Saint-Flour XLIX—2019*, Lecture Notes in Mathematics 2335, Springer, [DOI 10.1007/978-3-031-36854-7](https://doi.org/10.1007/978-3-031-36854-7). Page and theorem citations to the notes below refer to the downloaded drafts, not to that edition. The current Dropbox link on the author's teaching page was broken; the older direct link worked.

### Model and conventions

Maps are rooted bipartite planar multigraphs. Loops and parallel edges retain their electrical multiplicities. A face of degree $2k$ receives weight $q_k\ge0$; for a map with a prescribed external boundary, that external face is excluded from the weight product. Write $W^{(\ell)}$ for the partition function with boundary perimeter $2\ell$.

In the Saint-Flour draft, Proposition 5.10, p. 81, characterizes non-generic type $a\in(3/2,5/2)$ by

\[
 W^{(\ell)}\sim \frac{p_q}{2}c_q^{\ell+1}\ell^{-a},\qquad \ell\to\infty,
\]

with $p_q,c_q>0$. Such sequences are critical. The endpoint $a=5/2$ is the generic critical finite-variance class, Proposition 5.9, pp. 80–81. The endpoint $a=3/2$ denotes the subcritical class in these notes and is outside this question.

Theorem 7.1, p. 98, constructs $\mathbb P^{(\ell)}_\infty$ by the local limit of finite Boltzmann maps with perimeter $2\ell$ conditioned to have a large number of vertices. It is supported on locally finite infinite maps of the plane with the prescribed finite boundary. For $\ell=1$, closing the external digon gives the usual infinite Boltzmann map $M_\infty$. We keep the digon when running peeling and call its dual vertex $o$. Closing it only changes a finite neighborhood, so it cannot change recurrence or transience.

The question is whether, almost surely under $\mathbb P^{(1)}_\infty$, the unit-conductance dual graph $G=M_\infty^\dagger$ satisfies

\[
 R_{\rm eff}^{G}(o\leftrightarrow\infty)<\infty
 \qquad\text{for every critical type }a\in[2,5/2).
 \tag{1}
\]

The phases are dense for $3/2<a<2$, dilute for $2<a<5/2$, with the Cauchy case $a=2$ at the boundary. Beware two other index conventions: the perimeter stable index is (a-1); the stable-map/mobile index in Le Gall–Miermont is $\alpha=a-1/2$.

There is also a genuine version difference at $a=2$: the Peccot draft, printed p. 53, restricts “type 2” to its explicit gamma-function example. Saint-Flour Proposition 5.10 and the Cauchy paper cover a broader class. The experiments use the explicit family only; the conditional criterion below is not restricted to that family.

## 2. Literature search and what is actually known

Search performed on 13 November 2026. It combined the named papers, current author publication pages, and queries about “Boltzmann maps”/“stable maps” with “dual,” “transience,” “recurrence,” “effective resistance,” and “resistance growth,” including searches restricted to 2024–2026. Search-result crawl dates were not treated as publication dates. In particular, Budd's mini-course notes are dated **14 May 2017 in the document**, despite recent search metadata.

No answer to (1) was found. This is a search result, not a proof that no answer exists. The strongest explicit status checks found were the Cauchy paper's open question and Curien–Marzouk's 2021 statement that dilute dual transience remains open. The recent papers checked do not supply a resistance/flow theorem resolving it.

| Reference | Exact location inspected | Consequence and scope |
|---|---|---|
| Curien, Saint-Flour draft | Proposition 5.10 p. 81; Theorem 7.1 p. 98; Theorem 10.13 pp. 137–138; Theorem 13.3 pp. 179–182; Theorem 15.1 p. 207; Corollary 15.8 p. 211; Proposition 15.9 p. 212; Open Question 15.10 p. 213 | Defines the setting, proves primal recurrence and dense dual transience, leaves (1) open. |
| T. Budd and N. Curien, *Geometry of infinite planar maps with high degrees*, Electron. J. Probab. **22** (2017), paper 35, [DOI](https://doi.org/10.1214/17-EJP55), [arXiv:1602.01328v2](https://arxiv.org/abs/1602.01328v2) | Lemma 3.1 pp. 15–16; Theorem 4.2 pp. 21–23; Proposition 5.1 and Corollary 5.2 pp. 24–25; open question p. 5; Lemma 6.1 p. 35. These page numbers are in the saved 37-page preprint. | Finite expected FPP distance to infinity and dual transience for $a<2$; dilute metric growth; no dilute transience conclusion. |
| T. Budd, N. Curien, C. Marzouk, *Infinite random planar maps related to Cauchy processes*, J. Éc. polytech. Math. **5** (2018), 749–791, [DOI](https://doi.org/10.5802/jep.82), [arXiv:1704.05297](https://arxiv.org/abs/1704.05297) | Open Question 1 p. 754; Proposition 3 pp. 766–767; Theorem 3 and Proposition 4 p. 771. In the saved journal PDF these are PDF pp. 7, 19–20, 24. | The case $a=2$ is explicitly left open; proves logarithmic FPP clock growth and stretched-exponential graph-ball growth. |
| O. Gurel-Gurevich and A. Nachmias, *Recurrence of planar graph limits*, Ann. Math. **177** (2013), 761–781, [DOI](https://doi.org/10.4007/annals.2013.177.2.10) | Theorem 1.1 p. 761 | Recurrence of distributional planar limits with exponential root-degree tails. It does not cover the heavy-tailed dual degrees. |
| J. E. Björnberg and S. Ö. Stefánsson, *Recurrence of bipartite planar maps*, Electron. J. Probab. **19** (2014), paper 31, [DOI](https://doi.org/10.1214/EJP.v19-3102), [arXiv:1311.0178](https://arxiv.org/abs/1311.0178) | Theorem 1.2, p. 5 of the saved 47-page author manuscript | Recurrence of the primal local limit. The manuscript's page numbering differs from the 40-page journal version. |
| N. Curien and C. Marzouk, *Markovian explorations of random planar maps are roundish*, Bull. Soc. Math. France **148** (2020), 709–732, [arXiv:1902.10624](https://arxiv.org/abs/1902.10624) | Theorem 1.1 and Corollary 1.3, PDF pp. 5–6 of the saved author copy | Compares explorations and primal/dual distances; controls pioneer-point exploration. Metric control does not bound electrical energy. |
| N. Curien and C. Marzouk, *Infinite stable Boltzmann planar maps are subdiffusive*, Probab. Math. Phys. **2** (2021), 1–26, [DOI](https://doi.org/10.2140/pmp.2021.2.1), [arXiv:1910.09623](https://arxiv.org/abs/1910.09623) | Theorem 1 p. 2; Theorem 2 p. 3; explicit open-status discussion p. 5 (PDF pp. 4, 5, 7) | Subdiffusivity on the primal and slow dual displacement in the dense phase. The p. 5 discussion still calls dilute dual transience open. |
| T. Budzinski and T. Lehéricy, *Recurrence of the Uniform Infinite Half-Plane Map via duality of resistances*, Ann. Probab. **50** (2022), 1725–1754, [DOI](https://doi.org/10.1214/21-AOP1539), [arXiv:1912.08790](https://arxiv.org/abs/1912.08790) | Theorem 1, p. 2 of the saved preprint | Logarithmic resistance lower bound for a different, self-dual half-plane model. Its self-duality does not transfer to heavy-tailed plane Boltzmann duals. |
| E. Kammerer, *On large (3/2)-stable maps*, Ann. Inst. H. Poincaré Probab. Statist. **61** (2025), 1566–1602, [arXiv:2304.01167](https://arxiv.org/abs/2304.01167) | Theorems 1.1–1.2, p. 4 of the saved 46-page preprint | Distances and diameters of finite Cauchy maps, not dual random-walk transience. |
| E. Kammerer, *Scaling limit of first-passage percolation geodesics on planar maps*, J. London Math. Soc. **112** (2025), e70312, [DOI](https://doi.org/10.1112/jlms.70312), [arXiv:2412.02666v3](https://arxiv.org/abs/2412.02666v3) | Theorem 1.1 pp. 6–7; Corollary 1.2 p. 7; Proposition 2.1 p. 14 and equation (2.5) p. 15 | Detailed one-geodesic and coalescing-flow information. It does not establish a finite-energy electrical flow. |
| E. Kammerer, *Distances on the CLE4, critical Liouville quantum gravity and (3/2)-stable maps*, Probab. Math. Phys. **6** (2025), 1111–1180, [arXiv:2311.08571](https://arxiv.org/abs/2311.08571) | Theorem 1.4, p. 5 of the saved preprint | Scaling limits of boundary-to-large-face distances. |
| E. Kammerer, *Gaskets of O(2) loop-decorated random planar maps*, Math. Phys. Anal. Geom. **29** (2026), article 1, [arXiv:2411.05541](https://arxiv.org/abs/2411.05541) | Theorem 1.1 p. 4 of the saved preprint; publication checked against author's current research page | Identifies the critical Cauchy/gasket class, without answering the walk question. |
| J.-F. Le Gall and G. Miermont, *Scaling limits of random planar maps with large faces*, Ann. Probab. **39** (2011), 1–69, [arXiv:0907.3262](https://arxiv.org/abs/0907.3262) | Theorems 4 and 5, pp. 52 and 59 of the saved 73-page preprint | Foundational primal stable-map scaling limits. |
| N. Curien, G. Miermont, A. Riera, *The scaling limit of planar maps with large faces*, [arXiv:2501.18566v2](https://arxiv.org/abs/2501.18566v2) (2025) | Theorem 1.1 p. 4; discussion p. 14 | Metric scaling-limit construction, not a theorem on (1). Its resistance metric on a coding looptree is not the dual-map effective resistance in (1). |

Budd's peeling paper [arXiv:1506.01590](https://arxiv.org/abs/1506.01590) and his [2017 mini-course](https://hef.ru.nl/~tbudd/docs/mappeeling.pdf) were also checked for the perimeter description. Budzinski's and Curien's publication lists were checked for related work; causal-map and hyperbolic-map results concern different laws. No claim about those models is being used to settle (1).

## 3. The dichotomy and the dense proof

### 3.1 Primal recurrence does not imply dual recurrence

Saint-Flour Theorem 15.1 proves recurrence of the primal for every critical weight sequence. The root degree has an exponential tail, Lemma 15.6, pp. 209–210. The proof peels around the root until an event with probability uniformly bounded away from zero hides it; the number of such steps has a geometric tail. The graph is a local limit of finite uniformly edge-rooted maps, so the exponential-degree extension of the circle-packing recurrence theorem applies, after the usual vertex/edge-rooting change of measure.

A dual vertex has the degree of a primal face. For a first face discovered from a digon, its half-degree distribution is

\[
 \mathbb P(K=k)=\frac{h^\uparrow(k)}{h^\uparrow(1)}\nu(k-1),
 \qquad h^\uparrow(p)=2p\,4^{-p}{2p\choose p}\asymp\sqrt p.
 \tag{2}
\]

After closing the digon this gives the rooted-face degree law. For the canonical family, the mass in (2) is of order $k^{1/2-a}$, and the tail is of order $k^{3/2-a}$. In the general type class the corresponding tail statement follows from the regularly varying positive tail of 
$\nu$. There is no exponential tail. The degree-two external face before closing the digon must not be confused with this stationary rooted-face degree.

For comparison, when a critical weight sequence has finite support, the dual has bounded degrees and is recurrent. More generally the same planar-limit argument applies when its rooted degree has an exponential tail, as for regular critical weights. These are generic type-5/2 examples; the type-5/2 condition alone need not give an exponential tail. The Peccot draft records the bounded-face conclusion as Corollary 39, printed p. 90.

Consequently the primal recurrence theorem cannot just be applied to the dual. Nor does the intersection/Liouville property proved for the dual, Proposition 15.9, imply recurrence without degree control. The dense examples already demonstrate that failure.

### 3.2 Perimeter and Eden clock

For every filled peeling algorithm, the half-perimeter $P_n$, started at $P_0=1$, has transition law

\[
 \mathbb P(P_{n+1}=p+k\mid P_n=p)
 =\nu(k)\frac{h^\uparrow(p+k)}{h^\uparrow(p)},\qquad p+k>0.
 \tag{3}
\]

The underlying walk $S$ has i.i.d. increments with law

\[
 \nu(k)=q_{k+1}c_q^k\quad(k\ge0),\qquad
 \nu(-j)=2W^{(j-1)}c_q^{-j}\quad(j\ge1).
\]

For $3/2<a<5/2$, its negative mass satisfies $\nu(-j)\sim p_qj^{-a}$ and its positive tail satisfies
$\nu([j,\infty))\sim p_q\cos(\pi a)j^{1-a}/(a-1)$.
It has finite mean zero for $a>2$, and no absolute first moment for $a\le2$. The scaling limit has stable index (a-1). Pointwise positive-tail mass asymptotics require additional regularity; the canonical family has them.

Uniform peeling is the Eden exploration for independent Exp(1) lengths on dual edges. Its jump clock is

\[
 T_n=\sum_{i=0}^{n-1}\frac{E_i}{2P_i},
 \qquad E_i\text{ independent Exp(1), independent of }(P_i).
 \tag{4}
\]

The exact identity from Saint-Flour Lemma 13.5, or Budd–Curien Lemma 3.1, is

\[
 \mathbb E\!\left[\frac1{P_n}\right]
 =2\sum_{k=n+1}^\infty\frac{\mathbb P_1(S_k=0)}k,
 \qquad
 \mathbb E[T_\infty]
 =\sum_{k\ge1}\mathbb P_1(S_k=0).
 \tag{5}
\]

The local limit exponent is $\mathbb P_1(S_k=0)\asymp k^{-1/(a-1)}$. Thus the last series is finite in the dense phase and diverges at and above 2.

### 3.3 Complete finite-energy argument for the known dense result

For $a<2$, (5) gives a finite annealed expected FPP distance to infinity. On almost every fixed map, choose a measurable simple infinite FPP geodesic ray $\Gamma$ of finite expected length. Existence follows by taking finite geodesics escaping to infinity and a diagonal subsequence in the locally finite graph. Uniqueness is unnecessary.

For either orientation of an edge set

\[
 \theta(\vec e)=\mathbb P_{\rm fpp}(\vec e\in\Gamma)
 -\mathbb P_{\rm fpp}(\overleftarrow e\in\Gamma).
\]

This is an antisymmetric unit flow from $o$ to infinity: each ray has divergence 1 at $o$, zero elsewhere, and local finiteness allows expectations in those finite sums.

The needed dependence-sensitive bound has a short proof. If $X\sim\operatorname{Exp}(1)$, $A$ is any event, and $\delta=\mathbb P(A)$, then

\[
 \mathbb E[X1_A]
 =\int_0^\infty\mathbb P(A\cap\{X>t\})\,dt
 \ge\int_0^\delta(\delta-t)\,dt=\delta^2/2,
\]

because $\mathbb P(X\le t)\le t$. No independence of $A$ and $X$ is assumed. In particular, choosing one orientation per unoriented edge,

\[
 \mathcal E(\theta)=\sum_e\theta(e)^2
 \le\sum_e\mathbb P_{\rm fpp}(e\in\Gamma)^2
 \le2\mathbb E_{\rm fpp}\!\left[\sum_{e\in\Gamma}X_e\right]<\infty.
\]

Thomson's principle proves transience. This is the random-path proof of Budd–Curien Corollary 5.2 and Saint-Flour Corollary 15.8. It even gives the annealed bound $\mathbb E[R_{\rm eff}(o,\infty)]\le2\mathbb E[T_\infty]$ in the digon convention.

### 3.4 What breaks at $a\ge2$

At $a=2$, Budd–Curien–Marzouk Proposition 3 proves

\[
 T_n/\log n\longrightarrow 1/(\pi^2p_q)\quad\text{in }L^1.
\]

For $a>2$, the FPP clock grows on the scale $n^{(a-2)/(a-1)}$, with a strictly positive scaling limit. Monotonicity then implies $T_\infty=\infty$ almost surely: convergence at a growing scale to a positive variable forces $\mathbb P(T_n\le M)\to0$ for every fixed $M$. The Cauchy convergence gives the same conclusion at $a=2$.

The finite-expected-length ray used above is therefore unavailable. A divergent upper estimate on a proposed energy is not a proof that every flow has infinite energy. FPP nonexplosion is compatible with transience; for example, the infinite binary tree is transient and has no exploding Exp(1) ray. This example can be checked by bounding the probability of a length-$n$ path of total weight at most a fixed $t$ by $2^nt^n/n!\to0$.

## 4. Peeling layers and a valid Nash–Williams bound

Let $\theta_r$ be the first time the minimum dual height of an active boundary face is $r$. The boundary half-perimeter is $P_{\theta_r}$. Let $C_r$ be the set of actual dual edges leaving the filled vertex hull of the radius-$r$ dual ball.

These are finite cutsets separating $o$ from infinity. An edge in $C_r$ joins distance $r$ to distance (r+1): filling a finite component cannot introduce a boundary edge from that component to the infinite complementary component. Hence $C_r$ and $C_s$ are edge-disjoint for $r\ne s$.

Each crossing edge has an active boundary occurrence, so $|C_r|\le2P_{\theta_r}$. Equality need not hold. Lazy peeling can leave two boundary occurrences which will later be glued to an edge whose two dual endpoints are already inside. Such occurrences do not represent a crossing edge.

For any unit flow, Cauchy–Schwarz on $C_r$ gives

\[
 \sum_{e\in C_r}\theta(e)^2\ge |C_r|^{-1}.
\]

Summing the disjoint edge sets and taking the infimum proves

\[
 R_{\rm eff}(o,\infty)
 \ge\sum_{r\ge0}\frac1{|C_r|}
 \ge\sum_{r\ge0}\frac1{2P_{\theta_r}}.
 \tag{6}
\]

Thus divergence of the last series would prove recurrence. It is a rigorous sufficient criterion about the peeling-layer perimeter process.

The known typical scales explain why the direct attempt is weak. For $a>2$, Theorem 4.2 of Budd–Curien gives the layer-perimeter scale $P_{\theta_r}\sim r^{1/(a-2)}$ in the scaling-limit sense, and volume exponent $(a-1/2)/(a-2)$. The corresponding reciprocal-perimeter scale is summable throughout the dilute range. At $a=2$, their Cauchy-paper Theorem 3 gives

\[
 \frac{\log(2P_{\theta_r})}{\sqrt r}\longrightarrow\pi\sqrt2
 \quad\text{in probability}.
\]

Again the typical reciprocal scale is summable. These distributional assertions are **not** pathwise bounds proving convergence of the series in (6). More importantly, convergence of this lower bound would not prove transience. Rare small actual cutsets, or poor access to a large frontier, could still produce infinite resistance.

This also explains why a high-degree separating vertex in the dense phase is not a small-conductance edge cutset: its incident edge count can be enormous. The notes discuss exactly this pitfall before Corollary 15.8, pp. 210–211.

## 5. Partial result: an explicit sufficient perimeter criterion

This section proves a conditional reduction. It does not assert that the condition holds for any previously open value of $a$, or claim a new general electrical principle.

### 5.1 A tree extracted from uniform peeling

Run uniform filled peeling and retain only dual edges created when a new face is discovered. Delete gluing edges and every finite pocket filling. Each new face has one parent, the already discovered face across the peeled edge. These edges form a rooted tree $\mathcal T$ embedded as a subgraph of $G$.

The entire tree/frontier process can be generated without sampling a map or a pocket filling. Conditional on the perimeter path (3), maintain a cyclic word $L_n$ of $2P_n$ active half-edges, each labeled by its incident discovered face. Start with two entries labeled $o$. At a transition $P_{n+1}=P_n+k$:

1. For $k\ge0$, choose a uniform entry, labeled $v$, replace it by $2k+1$ entries labeled by a new vertex $w$, and add the tree edge $vw$.
2. For $k=-j<0$, remove a uniformly positioned cyclic block of $2j$ entries. No tree edge is added.

For negative jumps the two possible sides of a gluing have equal probability. Both give the same tree-word law as deletion of a uniform block. In the actual map the two extreme entries are paired; the other $2j-2$ entries border the finite pocket which has been omitted. For positive jumps the new face has degree $2k+2$, one edge joining its parent and $2k+1$ new active occurrences.

The spatial Markov property and uniform choice of the peeling edge prove the stated conditional construction by induction. The conditional position kernels depend only on the perimeter path; future perimeter transitions do not depend on these positions. Kammerer's reversed uniform exploration, Proposition 2.1, gives another description of the same uniform cyclic mechanism.

### 5.2 An explicit energy functional

For a new tree vertex $v_i$ born at step $i$, let $D_{i,N}$ be the number of entries of $L_N$ whose labels descend from $v_i$, including entries labeled $v_i$ itself. Define

\[
 U_N=\sum_{\substack{0\le i<N\\\Delta P_i\ge0}}
       \left(\frac{D_{i,N}}{2P_N}\right)^2
       +\frac1{4P_N}.
 \tag{7}
\]

Everything in (7) is generated by (3) and the explicit cyclic rules. Define the deterministic finite-path functional

\[
 F_N(p_0,\ldots,p_N)
 :=\mathbb E_{\rm positions}[U_N\mid P_0=p_0,\ldots,P_N=p_N].
 \tag{8}
\]

It can be computed by finite enumeration of the uniform positions, by their associated finite transition operators, or by Monte Carlo conditional on the path. It contains no unknown Boltzmann partition functions or unseen pocket geometries once $\nu$ is specified.

A useful two-mark form is

\[
 F_N=\sum_{\Delta p_i\ge0}
 \mathbb P_{\rm positions,marks}
 \{\text{both independent uniform terminal marks descend from }v_i\}
 +\frac1{4p_N}.
 \tag{9}
\]

This follows because, conditional on the cyclic construction, that probability is $(D_{i,N}/(2p_N))^2$. Thus it is a two-path overlap quantity, rather than the one-point clock $\sum1/P_i$.

### Proposition: sufficient condition for dual transience

For a critical type $a\in(3/2,5/2]$, either of the following conditions suffices for almost-sure transience of the dual:

\[
 \liminf_{N\to\infty}F_N(P_0,\ldots,P_N)<\infty
 \quad\text{almost surely};
 \tag{10}
\]

or the stronger annealed condition

\[
 \liminf_{N\to\infty}\mathbb E[F_N(P_0,\ldots,P_N)]<\infty.
 \tag{11}
\]

**Proof.** Give each tree edge resistance 1. At time $N$, attach each active half-edge to a common terminal with resistance $1/2$. Send mass $1/(2P_N)$ to each such terminal occurrence along the unique root-to-occurrence tree path.

This is a unit flow: every non-root tree vertex passes its incoming mass to its descendant branches and its own active half-edges. The current on the parent edge of $v_i$ is exactly $D_{i,N}/(2P_N)$. The terminal half-edges contribute

\[
 2P_N\cdot\frac12\left(\frac1{2P_N}\right)^2=\frac1{4P_N}.
\]

Thus the flow's energy is exactly $U_N$.

Filled peeling exhausts the map almost surely, Saint-Flour Theorem 10.13. In particular, every active half-edge incident to any fixed discovered face is eventually processed or swallowed. Each face has finite degree. It follows that terminal occurrences eventually avoid every finite set of tree vertices. The tree is locally finite because it is a subgraph of the locally finite dual.

If $\liminf_N U_N<\infty$, choose a sample-dependent subsequence on which these energies are bounded. On each fixed tree edge the currents lie in $[0,1]$, oriented away from the root. A diagonal subsequence converges on every edge. Because each vertex has finite degree and terminal occurrences escape, Kirchhoff's law passes to the limit, with divergence 1 at $o$ and zero elsewhere. Fatou's lemma gives finite energy to the limiting unit flow. Hence $\mathcal T$, and therefore its supergraph $G$, is transient.

Under (10), conditional Fatou yields

\[
 \mathbb E[\liminf_N U_N\mid(P_n)_{n\ge0}]
 \le\liminf_N\mathbb E[U_N\mid(P_n)_{n\ge0}]
 =\liminf_NF_N(P_0,\ldots,P_N)<\infty.
\]

Therefore $\liminf_N U_N<\infty$ almost surely. Under (11), the same argument uses ordinary Fatou. This proves both sufficient conditions. $\square$

The remaining mathematical task in this approach is exactly the bound (10) or (11) for the explicitly defined functional. It is unproved here. The criterion is stronger than transience of the full dual, since it discards many useful edges; its failure would not establish recurrence. The simulations below do not demonstrate the needed bound, even for the canonical weights.

## 6. Modest computations

All computations ran in this directory, with one numerical thread, inherited **nice 15** (lower priority than nice 10), and small memory use. No full paper PDF or page image was written to disk. Fetches were converted in memory to text. No publication, git push, or background service was performed.

### 6.1 Canonical family and an exact tail sampler

Use Budd–Curien Lemma 6.1, equations (57)–(58):

\[
 q_k=c\kappa^{k-1}\frac{\Gamma(k+1/2-a)}{\Gamma(k+1/2)}1_{k\ge2},
 \quad \kappa=\frac1{4a-2},\quad
 c=-\frac{\sqrt\pi}{2\Gamma(3/2-a)}.
\]

For $k\ne0$, $\nu(k)=c\Gamma(k+3/2-a)/\Gamma(k+3/2)$, interpreted by reflection at negative integers; $\nu(0)=0$. For $j\ge1$, the numerically convenient positive expression is

\[
 \nu(-j)=\frac{\Gamma(a-1/2)}{2\sqrt\pi}
          \frac{\Gamma(j-1/2)}{\Gamma(j+a-1/2)}.
\]

Here is why the rejection sampler used for (3) has no tail truncation. Let $\operatorname{BG}(\alpha,\beta)$ mean: sample $B\sim\operatorname{Beta}(\alpha,\beta)$, then a geometric variable on $1,2,\ldots$ with success probability $B$. Its probability mass is

\[
 g_{\alpha,\beta}(k)=\frac{\mathrm B(\alpha+1,\beta+k-1)}{\mathrm B(\alpha,\beta)}.
\]

The gamma formulas give exactly

\[
 g_{a-3/2,\,5/2-a}(k)=\nu(k)h^\uparrow(k+1),\qquad
 \nu(-j)=b\,g_{a-1,\,1/2}(j),\quad b=\frac1{2(a-1)}.
\]

At perimeter $p$, propose a positive $k$ from the first distribution with probability $1/(1+b)$, accepting with probability
$h^\uparrow(p+k)/(h^\uparrow(p)h^\uparrow(k+1))$.
Otherwise propose $-j$ from the second distribution, rejecting if $j\ge p$, and accepting with probability $h^\uparrow(p-j)/h^\uparrow(p)$.

The positive ratio is at most 1 since
$h^\uparrow(n+1)/h^\uparrow(n)=1+1/(2n)$ decreases with $n$; the negative ratio is also at most 1. The accepted mass before normalization is exactly (3) divided by $1+b$. Harmonicity makes its total mass $1/(1+b)$, proving the sampler. Computation uses logarithms and gamma-ratio asymptotics at large arguments; “exact” refers to its untruncated probability law, not arbitrary-precision random arithmetic.

### 6.2 Layer experiment

[code/peeling_layers.py](code/peeling_layers.py) simulates the exact $(P,D,H)$ kernel in Budd–Curien equation (34), where $D$ is the number of boundary occurrences at the lower of the two active heights. It records

\[
 A_N=\sum_{r:\theta_r\le N}\frac1{2P_{\theta_r}},\qquad
 B_N=\sum_{n=0}^{N-1}\frac1{2P_n}.
\]

$A_N$ is the finite Nash–Williams lower bound in (6), including $r=0$. $B_N$ is the conditional mean Eden clock, **not** effective resistance.

There were 32 independent runs per parameter, each to 20,000 steps: 2,560,000 steps total. The table gives medians; the raw files include empirical quartiles.

| $a$ | steps | median dual layers $H_N$ | median $B_N$ | median $A_N$ |
|---:|---:|---:|---:|---:|
| 1.8 | 1,000 | 3 | 1.1495 | 0.5267 |
| 1.8 | 20,000 | 5 | 1.3828 | 0.5268 |
| 2.0 | 1,000 | 6.5 | 3.2629 | 0.7718 |
| 2.0 | 20,000 | 10 | 4.3867 | 0.7720 |
| 2.2 | 1,000 | 9 | 5.1919 | 0.8449 |
| 2.2 | 20,000 | 20.5 | 11.0259 | 0.8467 |
| 2.4 | 1,000 | 16.5 | 10.8915 | 1.3391 |
| 2.4 | 20,000 | 47.5 | 30.0569 | 1.4327 |

The usual layer lower bound appears to accumulate slowly after its initial layers, while the clock grows more substantially as $a$ increases. For the Cauchy member $p_q=1/4$, the limiting mean-clock coefficient is $4/\pi^2\approx0.4053$; the observed finite-time clock scale is compatible with logarithmic growth. No fitted exponent or statistical claim of convergence is made.

Data: [all checkpoints](data/peeling_runs.csv), [summary](data/peeling_summary.csv), [individual layers for three runs per parameter](data/peeling_layers.csv), [metadata](data/simulation_metadata.json).

### 6.3 Electrical experiment on the peeled skeleton

[code/peeling_skeleton.py](code/peeling_skeleton.py) represents the cyclic boundary by runs of labels, so very large faces do not require enormous arrays. It retains the discovered face-tree edges and gluing edges, omits all finite pocket fillings, and wires each unfinished half-edge through a resistor of resistance $1/2$. It solves the resulting grounded sparse Laplacian.

These are finite electrical approximations to a **subgraph** of the dual, not fully sampled finite Boltzmann maps. Their resistances $R_N^{\rm skel}$ increase with exploration to the skeleton's resistance to infinity, which is at least the full dual's resistance. A finite value of $R_N^{\rm skel}$ does not upper-bound the full infinite resistance. A uniform bound along the entire exploration would prove transience; a few increasing finite values cannot.

Twelve runs per parameter were taken to 2,000 steps. The reported medians are:

| $a$ | $R_{100}^{\rm skel}$ | $R_{500}^{\rm skel}$ | $R_{2000}^{\rm skel}$ | tree resistance at 2,000 | uniform tree-flow energy $U_{2000}$ |
|---:|---:|---:|---:|---:|---:|
| 1.8 | 0.7288 | 1.8883 | 2.3387 | 3.2292 | 7.9355 |
| 2.0 | 1.7103 | 2.0411 | 2.4847 | 5.6913 | 8.2991 |
| 2.2 | 1.9828 | 3.3563 | 3.9586 | 8.5941 | 14.9990 |
| 2.4 | 1.5660 | 2.2422 | 3.1753 | 10.0550 | 13.6290 |

The extra gluing edges materially reduce resistance relative to the tree, and the uniform tree-flow construction is less efficient than the optimal tree flow. These observations explain why merely dividing current equally over a frontier can be too expensive. Sample-to-sample variability is substantial; the nonmonotone ordering across $a$ should not be interpreted as a phase diagram.

Data: [electrical runs](data/skeleton_runs.csv), [metadata](data/skeleton_metadata.json).

### 6.4 What was checked

[code/audit.py](code/audit.py) independently checks:

- 5,920 small layer states against direct cyclic lists of boundary heights, including both sides of gluing and all low-height counts.
- Beta-geometric probabilities against beta-mixture numerical integrals and the gamma formula; maximum absolute discrepancy $6.03\times10^{-10}$.
- The analytic rejection acceptance probability $1/(1+b)$ against all simulated proposals; the largest standardized discrepancy was 1.53.
- The grounded-Laplacian resistance against the dissipated energy $\sum_{uv}(V_u-V_v)^2+\sum_v2\ell_vV_v^2$; maximum scaled discrepancy $3.17\times10^{-14}$.
- The inequalities $R_N^{\rm skel}\le R_N^{\rm tree}\le U_N$, monotonicity of the sampled skeleton resistances, and analytic series/parallel examples $R=1/4$ and $R=9/4$.
- Every retained file in `sources/` has the `.txt` extension.

Results: [data/audit_results.json](data/audit_results.json). Reproduction, from this directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/peeling_layers.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/peeling_skeleton.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/audit.py
```

The scripts inherit nice 15 in this session. They must be run at nice 10 or lower priority if reproduced elsewhere. Quartiles measure empirical dispersion, not confidence intervals. The modest horizons, omitted pockets in the electrical experiment, and lack of a tail bound on the energy prevent an infinite-volume conclusion.

## 7. Unresolved point

A proof of (10), or another finite-energy flow using gluing edges and pocket connections, would establish transience. A divergent sequence of genuine disjoint cutset reciprocals would establish recurrence. This work obtains neither for $a\in[2,5/2)$.

The most concrete open estimate left by the partial reduction is the two-mark overlap functional (9). Existing one-geodesic length and perimeter growth results do not by themselves control it. No citation found in this search fills that gap.

Task: “Open problem C0059” — received 2026-11-13 06:59 +04 (session launch time).
