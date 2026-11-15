PARTIAL

# F0083: deterministic nonuniqueness of stable allocations

For every locally finite set of centres in **dimension 1 or 2**, and every common appetite \(0<\alpha<\infty\), there is a Lebesgue-a.e. unique stable allocation. No growth bound on the original centre set is needed for this statement. A proof is given below, using the extremal-allocation inequalities of Hoffman–Holroyd–Peres (HHP), followed by a packing and flow argument.

There is also a sufficient condition in every dimension. Put

\[
N(r)=\#(\Xi\cap B(0,r)).
\]

If

\[
\sum_{k=1}^{\infty}\frac{4^k}{1+N(2^k)}=\infty, \tag{A}
\]

then the stable allocation is a.e. unique. In particular, this holds if

\[
N(r)=O\bigl(r^2\log r\log\log r\bigr)\quad(r\to\infty). \tag{B}
\]

These are partial answers to the question asking for a counterexample in *some* dimension. The existence or impossibility of such a counterexample in dimensions \(d\ge3\), without a growth assumption, is not settled here. No printed resolution of that full question was found in the literature search described below. No priority claim is made for the partial results.

## 1. Literature first: what the source actually states

The source is C. Hoffman, A. E. Holroyd and Y. Peres, *A stable marriage of Poisson and Lebesgue*, Ann. Probab. **34** (2006), 1241–1272, [DOI](https://doi.org/10.1214/009117906000000098), [arXiv v4](https://arxiv.org/abs/math/0505668v4). Its complete extracted text is [sources/hhp2006.txt](sources/hhp2006.txt).

**Pagination convention:** the downloaded v4 is the IMS electronic reprint. It expressly warns that its pagination differs from the original journal. Every page number for HHP 2006 below is a **reprint page**, not an inferred journal page. Form-feed characters in the text preserve page boundaries. An attempt to obtain the original journal PDF from Project Euclid returned an access-challenge page; it was not saved as a paper.

The following are exact mathematical restatements; the source file preserves the original wording.

- **Open problem (i), reprint p. 31:** “Does there exist a discrete set of centers in \(\mathbb R^d\) which admits two stable allocations (differing on a nonnull set)?” The following sentence rules out configurations of at most quadratic growth and configurations arising from a translation-invariant point process, referring to Theorems 2 and 3.
- **Theorem 2, reprint p. 3:** for a discrete \(\Xi\subseteq\mathbb R^d\), make \(G_b\) by joining every pair of centres at distance at most \(b\). If, for **every** \(b>0\), simple symmetric random walk on \(G_b\) is recurrent, then for each \(\alpha\in(0,\infty)\) a stable allocation exists and is Lebesgue-a.e. unique. For a disconnected graph, recurrence is understood component by component.
- **Theorem 3, reprint p. 5:** a translation-invariant simple point process on \(\mathbb R^d\) of finite intensity has, almost surely, a Lebesgue-a.e. unique stable allocation for each fixed \(\alpha\in(0,\infty)\). The allocation can be selected as a measurable factor commuting with isometries. The surrounding setup uses intensity \(\lambda\in(0,\infty)\); the zero-intensity case is the empty configuration. Ergodicity is **not** a hypothesis in the final theorem. The conclusion is almost sure, not a prohibition on individual null-event realizations.

### The precise growth condition is an edge count

Remark (vi), **reprint p. 7**, gives this sufficient condition for Theorem 2:

\[
\boxed{\quad
\text{for every finite }b>0,\qquad
E_b(r):=\#\bigl\{\{\xi,\xi'\}\subseteq\Xi\cap B(0,r):
|\xi-\xi'|<b\bigr\}=O(r^2\log r)
\quad(r\to\infty).\quad} \tag{1}
\]

Pairs here are unordered pairs of distinct centres. Constants may depend on \(b\) and the configuration. The theorem itself uses edges of length \(\le b\); using a slightly larger \(b\) in (1) removes that endpoint distinction.

The paragraph says the condition is natural for \(d\le2\), and cites Corollary (3.52) of Woess, *Random Walks on Infinite Graphs and Groups*. The condition and Theorem 2 make sense, and are sufficient, in **every ambient dimension**. The exponent is 2, not \(d\). It is not stated as a bound on \(N(r)\). If the number of neighbours within each fixed distance is uniformly bounded, then \(E_b(r)\le C_bN(r)\), so a centre-count bound implies (1). Arbitrarily dense clusters do not permit that deduction. The open-problem paragraph does not separately define “growth” as a centre count; (1) is the explicit quantitative condition supplied in the paper.

A concrete reason to distinguish these notions: let

\[
C_n=\{n+j/(10n):0\le j<n\},\qquad \Xi_0=\bigcup_{n\ge1}C_n\subset\mathbb R.
\]

Then \(N(r)\sim r^2/2\), but \(G_2\) is transient. Every vertex of \(C_n\) is joined to every vertex of \(C_{n+1}\). Send flow \(1/[n(n+1)]\) on each such edge, directed to the next layer, and zero on the other edges. The sole vertex of \(C_1\) sends one unit; each vertex in \(C_n\), \(n\ge2\), receives and sends \(1/n\). Its electrical energy is

\[
\sum_{n\ge1}n(n+1)\left(\frac1{n(n+1)}\right)^2
=\sum_{n\ge1}\frac1{n(n+1)}=1.
\]

The finite-energy unit-flow criterion gives transience. Also, the within-layer edges alone give \(E_2(r)=\Omega(r^3)\). Thus Theorem 2's hypothesis cannot simply be replaced, on the strength of the quoted remark, by \(N(r)=O(r^2)\). The new argument in Section 3 does establish a centre-count criterion, by bounding the density of a *disagreement subgraph* rather than the original graph.

### Later work and the scope of the search

The forward-citation query through 2026-11-13 returned **68 OpenAlex records dated 2006–2026**, including duplicates and some non-paper records. All titles were screened, and all **49 returned abstracts** were saved and screened. This is an index-based search, not exhaustive full-text coverage of every citing work. The complete query, raw metadata and bibliography are in [data/openalex_citing.json](data/openalex_citing.json), [sources/forward_citations.txt](sources/forward_citations.txt) and [sources/citing_abstracts.txt](sources/citing_abstracts.txt). Targeted web searches covered the named authors and the terms nonuniqueness, deterministic configurations, locally finite sets, stable allocations and quadratic growth. Relevant full texts were then inspected.

| Work inspected | Exact result/location checked | Relevance to (i) |
|---|---|---|
| HHP, *Tail bounds for the stable marriage of Poisson and Lebesgue*, Canad. J. Math. 61 (2009), 1279–1299, [text](sources/hhp_tail2009_published.txt), [DOI](https://doi.org/10.4153/CJM-2009-060-7) | Theorems **1.2, 1.3**, p. **1281**; definition of benign, pp. **1282–1283**; Theorem **1.6**, p. **1283** | Tail and continuity results. “Benign” already includes a.e. uniqueness. The continuity theorem therefore does not prove deterministic uniqueness for arbitrary limits. |
| Holroyd–Pemantle–Peres–Schramm, *Poisson matching*, AIHP 45 (2009), 266–287, [text](sources/hpps2009_published.txt), [DOI](https://doi.org/10.1214/08-AIHP170) | Proposition **9**, p. **273**; Theorem **6(ii)**, p. **269**, allocation extension p. **270**; Theorem **19**, p. **283**, allocation adaptation p. **286** | Proposition 9 is a point-to-point matching result with non-equidistance/no-descending-chain and probabilistic hypotheses. The allocation extension resolves a tail-bound question, not (i). |
| Deijfen–Holroyd–Peres, *Stable Poisson graphs in one dimension*, EJP 16 (2011), 1238–1253, [text](sources/deijfen_holroyd_peres2011.txt), [arXiv](https://arxiv.org/abs/1101.3716) | Proposition **1.1**, preprint p. **4**; Theorems **1.2, 1.3**, preprint p. **5**; stable multimatching discussion p. **3** | Discrete Poisson graphs, stubs and infinite components; not Lebesgue allocations for arbitrary deterministic centres. |
| Chatterjee–Peled–Peres–Romik, *Gravitational allocation to Poisson points*, Ann. Math. 172 (2010), 617–671, [text](sources/cppr2010_published.txt), [DOI](https://doi.org/10.4007/annals.2010.172.617) | Theorem **2**, p. **622**, fairness and efficiency; also preprint p. **8**, [preprint text](sources/cppr2010.txt) | Constructs a different, gravitational allocation. A second fair allocation is not a second stable allocation. |
| Markó–Timár, *A Poisson allocation of optimal tail*, Ann. Probab. 44 (2016), 1285–1307, [text](sources/marko_timar2016.txt), [arXiv](https://arxiv.org/abs/1103.5259) | Theorem **1.1**, reprint p. **1** | Another allocation rule with optimal diameter tail in \(d\ge3\); not a second Euclidean-stable allocation. |
| Holroyd, *Geometric properties of Poisson matchings* (2011), [text](sources/holroyd_geometry2011.txt), [arXiv](https://arxiv.org/abs/0909.0575) | Theorems **1–3**, preprint pp. **2–3** | Planarity, minimality and local finiteness for point-to-point matchings, a different model. |
| Haji-Mirsadeghi–Khezeli, *Stable transports between stationary random measures*, ECP 21 (2016), paper 51, [text](sources/haji_khezeli2016.txt), [arXiv](https://arxiv.org/abs/1504.02965) | Assumption **4.16**, p. **10/25**; Corollary **4.22**, p. **11/25**; Proposition **4.23** and Theorem **4.24**, p. **12/25**; Proposition **4.37**, p. **14/25** | Generalizes stable transport. The uniqueness theorem explicitly requires stationary random measures. Discussion on p. 10 points back to HHP's general-measure counterexample; it is not a Lebesgue counterexample. |
| Last–Penrose, *Lectures on the Poisson Process* (2017), [text](sources/last_penrose2017.txt), [author PDF](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf) | Theorem **11.9**, printed p. **107** | The uniqueness section begins by assuming a stationary simple point process of finite positive intensity. |
| Last–Thorisson, *Transportation of diffuse random measures on \(\mathbb R^d\)*, ALEA 20 (2023), 577–592, [text](sources/last_thorisson2023.txt), [DOI](https://doi.org/10.30757/ALEA.v20-21) | Proposition **4.3** and Remark **4.4**, p. **587** | Stable balancing allocation for jointly stationary ergodic measures with locally finite discrete destination. The following section explicitly changes to an allocation that need not be stable. |
| Khezeli–Mellick, *On the existence of balancing allocations and factor point processes*, [text](sources/khezeli_mellick2025.txt), [arXiv](https://arxiv.org/abs/2303.05137) | Theorems **1.1–1.2**, downloaded v2 pp. **2–3** | Existence of factors and balancing allocations under stationary-measure assumptions, not arbitrary deterministic uniqueness. Bibliographic year differs among indexes; the saved preprint is dated April 2024. |
| Eppstein–Goodrich–Mamano, *Algorithms for stable matching and clustering in a grid* (2017), [text](sources/grid2017.txt), [arXiv](https://arxiv.org/abs/1704.02303); Barequet–Eppstein–Goodrich–Mamano, *Stable-matching Voronoi diagrams* (2020), [text](sources/voronoi2020.txt), [DOI](https://doi.org/10.20382/jocg.v11i1a2) | Grid paper introduction; Voronoi paper introduction, preprint p. **2**, explicitly restricts to finite centre sets | Algorithmic finite problems, not an infinite deterministic nonuniqueness theorem. |
| Elboim–Spinka–Yakir, *Optimal matchings of randomly perturbed lattices*, indexed in 2026, [text](sources/perturbed_lattices2026.txt), [arXiv](https://arxiv.org/abs/2506.16873) | Theorem **1.1**, downloaded v1 p. **3** | Tail-optimal invariant point matchings; no claim resolving (i). Saved version is dated June 2025. |

## 2. How the original construction and uniqueness proofs work

All null sets mentioned here can be combined, since the centre set is countable. In particular, sites equidistant from two centres form a Lebesgue-null union of bisector hyperplanes. As in HHP, an allocation may be undefined on a null set.

In the **site-proposing** construction (Section 2, reprint pp. 8–9), every site applies to its closest centre that has not rejected it. At each stage a centre keeps its closest applicants up to volume \(\alpha\). Its rejection radius is

\[
r_n(\xi)=\inf\{r:\mathcal L(A_n(\xi)\cap B(\xi,r))\ge\alpha\}.
\]

The centre rejects applicants outside that radius. A site is eventually retained by one centre or is rejected by every centre and remains unclaimed. Local finiteness makes the distance-ordered alternatives well-defined. Fatou's lemma bounds limiting territories by \(\alpha\). A site that desires a centre must have been rejected by it, whereas a centre coveting a site could not have rejected it. This proves existence and stability (Theorem 1).

In the **centre-proposing** construction (Section 4, reprint p. 15), a centre applies to its nearest available sites, up to volume \(\alpha\), excluding sites that have rejected it:

\[
a_n(\xi)=\inf\{a:\mathcal L(B(\xi,a)\setminus R_n(\xi))\ge\alpha\}.
\]

Sites retain their closest applying centre and reject the others. A retained centre can only improve from the site's perspective; local finiteness gives an eventual choice. Lemma 14 proves this limit is stable.

Write these two limits as \(s\) and \(c\). Lemma **15**, reprint p. **16**, proves extremality. With

\[
g_x(\psi,r)=\mathbf1\{|x-\psi(x)|<r\},\qquad
\gamma_\xi(\psi,r)=\mathcal L(\psi^{-1}(\xi)\cap B(\xi,r)),
\]

and unclaimed distance \(\infty\), every stable \(\psi\) satisfies

\[
g_x(s,r)\ge g_x(\psi,r)\ge g_x(c,r)\quad\text{a.e. }x,
\]
\[
\gamma_\xi(c,r)\ge\gamma_\xi(\psi,r)\ge\gamma_\xi(s,r)\quad\text{every }\xi. \tag{2}
\]

These deterministic inequalities do not assume a point process or recurrence. They come from the fact that a stable partner cannot reject its site/centre in the respective algorithm (Lemmas 18–19, reprint p. 19). Equality of \(s\) and \(c\) therefore implies uniqueness of every stable allocation, not just uniqueness within equivariant allocations.

There are two different original uniqueness arguments:

1. **Theorem 2:** Section 3, reprint pp. 9–15, starts with *any* two differing stable allocations. It defines disputed sites \(D(\xi)\), the near disputed sites \(N(\xi)\), and the disputed sites preferring a centre \(M(\xi)\). Edges carry capacities \(\mathcal L(N(\xi)\cap M(\xi'))\). Lemmas **8–10** exclude cycles and order distances. Lemma **11** makes total outgoing capacity at least total incoming capacity. Lemma **12** gives a reachable graph with bounded edge lengths and summable capacities along every directed path. Proposition **13**, reprint pp. **13–15**, then produces a finite-energy unit flow, hence a transient graph. **The recurrence hypothesis is used only in the final paragraph proving Theorem 2, reprint p. 14:** this graph is a subgraph of some recurrent \(G_b\), which is impossible. The quantitative edge-growth estimate (1) is a separate sufficient route to recurrence; it is not used in existence, optimality, or the capacity lemmas.
2. **Theorem 3:** Lemma **16**, reprint p. **17**, gives the mass-transport identity
   \[
   \mathbb E g_0(\Psi,r)=\lambda\mathbb E^*\gamma_0(\Psi^*,r).
   \]
   Sites favour \(s\), centres favour \(c\), but this identity equates their averaged radial statistics. Thus the inequalities in (2) must be equalities. Taking countably many rational radii, applying Fubini, and excluding bisectors gives \(s=c\) a.e. The sandwich (2) gives uniqueness of all stable allocations. This proof uses stationarity and finite intensity, not quadratic growth.

## 3. Proof of the partial results

Only the existence of \(s,c\) and inequalities (2) are imported allocation results: HHP Theorem 1 and Lemmas 14–15. Everything after those facts is proved here. The proof also explains why dense clusters cannot produce a counterexample in dimensions 1 or 2.

### 3.1 A directed disagreement graph

Work off a single null set where the allocations or the site inequalities are undefined, or a site is equidistant from two centres. Denote territories by \(S_v=s^{-1}(v)\) and \(C_v=c^{-1}(v)\), and set

\[
A_v=S_v\setminus C_v,\qquad B_v=C_v\setminus S_v.
\]

Here and below these sets omit the common null set. From the centre inequality (2) at \(r=\infty\),

\[
\mathcal L(B_v)\ge\mathcal L(A_v). \tag{3}
\]

Every site of \(B_u\) is assigned under \(s\) to some centre other than \(u\), since a site claimed under \(c\) cannot be unclaimed under the better allocation \(s\). It strictly prefers that new centre. Put

\[
Q(u,v)=C_u\cap S_v\quad(u\ne v),\qquad q(u,v)=\mathcal L(Q(u,v)),
\]

and include the directed edge \(u\to v\) precisely when \(q(u,v)>0\). Then

\[
\sum_v q(u,v)=\mathcal L(B_u),\qquad
\sum_w q(w,u)\le\mathcal L(A_u),
\]

so

\[
\sum_wq(w,u)\le\sum_vq(u,v). \tag{4}
\]

The inequality, rather than equality, allows sites unclaimed under \(c\) but claimed under \(s\).

If \(s,c\) differ on positive measure, this graph has an edge. Indeed, a positive-measure set claimed differently under \(c\) already gives an edge, by countability. If all differences instead consist of \(c\)-unclaimed sites becoming claimed under \(s\), some \(A_v\) has positive measure. Equation (3) then gives a positive-measure \(B_v\), again producing an edge.

### 3.2 Receiving centres are sated and their radii decrease

Define

\[
T_v=\mathop{\rm ess\,sup}_{y\in C_v}|y-v|\in[0,\infty],
\]

taking \(T_v=0\) for a null territory. Suppose \(q(u,v)>0\). For a.e. \(x\in Q(u,v)\), the site \(x\) strictly prefers \(v\) to \(u\), its centre under \(c\). Stability of \(c\) therefore says that \(v\) does **not** covet \(x\). This has both consequences:

- \(v\) is sated under \(c\);
- no site in \(C_v\) is farther from \(v\) than \(x\).

Consequently

\[
T_v\le |x-v|<|x-u|\le T_u \quad\text{for a.e. }x\in Q(u,v). \tag{5}
\]

In particular \(T_v<\infty\) and \(T_v<T_u\). This also proves there are no directed cycles: every vertex on a cycle would have finite radius and these radii would strictly decrease around the cycle.

When \(T_u<\infty\), (5) places \(Q(u,v)\), up to null sets, in a spherical shell about \(u\). If \(\omega_d\) is the unit-ball volume, then

\[
q(u,v)\le\omega_d(T_u^d-T_v^d). \tag{6}
\]

Spheres have Lebesgue measure zero, so open versus closed shell boundaries do not affect this bound. Territory outliers on null sets do not invalidate (5), which uses essential radii.

Choose one edge \(\rho\to v_0\), put \(m=q(\rho,v_0)>0\), and keep only this edge together with all vertices and edges reachable from \(v_0\). Call the resulting graph \(H\). Acyclicity prevents a return to \(\rho\). At every nonroot vertex (4) still holds: all its outgoing edges remain, while some incoming edges may have been removed.

Let \(R=T_{v_0}<\infty\). Every nonroot vertex of \(H\) is sated and has

\[
T_v\le R.
\]

Every nonroot edge has length less than \(2R\), by (5) and the triangle inequality. The initial edge has finite length too. Thus all edges have length at most some finite \(b>0\). The root radius itself can be infinite; it is never used in (6).

### 3.3 Disjoint territories bound the local density of \(H\)

For a bounded set \(K\), each nonroot vertex \(v\in H\cap K\) has \(\alpha\) units of its \(c\)-territory in the radius-\(R\) enlargement \(K^{+R}\), up to null sets. These territories are disjoint. Therefore

\[
\alpha\,\#((V(H)\setminus\{\rho\})\cap K)
\le\mathcal L(K^{+R}). \tag{7}
\]

This bound concerns vertices participating in the reachable disagreement, not all centres in \(\Xi\). In particular,

\[
N_H(r):=\#(V(H)\cap B(0,r))
\le 1+\frac{\omega_d(r+R)^d}{\alpha}. \tag{8}
\]

There is a uniform finite degree bound \(D\) for the undirected graph \(H\). All nonroot neighbours of any vertex lie within distance \(b\); their disjoint, sated territories are contained in a ball of radius \(b+R\) about that vertex. Hence their number is at most \(\omega_d(b+R)^d/\alpha\). Adding the possible root neighbour changes this bound by at most one. Local finiteness also ensures that all sums in the flow construction below are finite at a vertex.

### 3.4 The capacities generate a finite-energy unit flow

Start a random directed path at \(\rho\), take its unique retained edge to \(v_0\), and thereafter choose an outgoing edge from \(u\) with probability

\[
p(u,v)=\frac{q(u,v)}{Q_u},\qquad Q_u=\sum_wq(u,w).
\]

A visited nonroot vertex has positive incoming capacity, so (4) ensures \(Q_u>0\); the path cannot terminate. Acyclicity prevents repeated vertices. Thus it is an infinite simple path.

Let \(a_n(u)\) be the probability of reaching \(u\) by time \(n\), and define \(f_n(u,v)=a_n(u)p(u,v)\). Then

\[
f_n(u,v)\le q(u,v)/m \quad\text{for all }n. \tag{9}
\]

Here is a direct induction, avoiding an assumption about a topological ordering of an infinite graph. The root sends one unit along its edge, equal to its capacity divided by \(m\). At a nonroot \(u\), the possible incoming last edges are disjoint path events, because no vertex is revisited. If the previous-stage edge bounds hold, then

\[
a_n(u)=\sum_w f_{n-1}(w,u)
\le m^{-1}\sum_wq(w,u)
\le Q_u/m.
\]

Multiplication by \(p(u,v)\) proves the next bound. The initial stage is immediate.

Taking increasing limits gives edge-traversal probabilities \(f(e)\le q(e)/m\). The path law and finite degrees give conservation of this flow at every nonroot vertex. There is unit outflow and no inflow at the root. It is therefore a unit flow to infinity on the undirected version of \(H\), with the displayed orientations.

For each sampled path, (6) telescopes after its first edge:

\[
\sum_{e\text{ on path}}q(e)
\le m+\omega_dR^d. \tag{10}
\]

Tonelli's theorem and (9) now give its electrical energy:

\[
\begin{aligned}
\sum_e f(e)^2
&=\mathbb E\!\left[\sum_{e\text{ on path}}f(e)\right]\\
&\le m^{-1}\mathbb E\!\left[\sum_{e\text{ on path}}q(e)\right]
\le 1+\frac{\omega_dR^d}{m}<\infty. \tag{11}
\end{aligned}
\]

This is the transience mechanism in HHP Proposition 13, here proved directly for the extremal disagreement graph.

### 3.5 A growth obstruction to finite-energy flows

We need this elementary graph fact. Let a locally finite graph have vertices in \(\mathbb R^d\), edge lengths at most \(b\), and degree at most \(D<\infty\). A unit flow to infinity of finite energy implies

\[
\sum_{k\ge1}\frac{4^k}{1+N_H(2^k)}<\infty. \tag{12}
\]

To prove it, take spherical cuts at radii \(r_j=(b+1)j\), ignoring the finitely many cuts not enclosing the root. Each cut is finite. Summing flow divergence over the vertices inside a cut shows that its net outward flow is one. Cauchy–Schwarz therefore makes the energy on that cut at least \(1/M_j\), where \(M_j\) is its number of crossing edges. If a cut has no crossing edge, a unit flow is already impossible.

An edge cannot cross two of these cuts, because its length is less than the separation of the radii. Thus all cut edge sets are disjoint. For cuts with radii in \([2^k,2^{k+1})\), their number is at least \(c_b2^k\) for sufficiently large \(k\). Every crossing edge has endpoints inside radius \(2^{k+1}+b\le2^{k+2}\). Hence

\[
\sum_{j:\,2^k\le r_j<2^{k+1}}M_j
\le D N_H(2^{k+2}).
\]

A second application of Cauchy–Schwarz bounds the energy on the cuts in that block below by

\[
\sum_j\frac1{M_j}
\ge\frac{(\#j)^2}{\sum_j M_j}
\ge c_{b,D}\frac{4^k}{1+N_H(2^{k+2})}. \tag{13}
\]

Summing over disjoint blocks and shifting the index by two proves (12). This argument allows edges crossing a cut in either direction; it uses net signed flux, not an assumption that the flow is spatially outward.

### 3.6 Conclusions and cases

If (A) holds for \(\Xi\), then \(N_H(r)\le N(r)\) makes the series in (12) diverge, contradicting (11). This proves the sufficient condition (A), in every dimension. Under (B), its terms are bounded below by a constant times \(1/(k\log k)\), so (A) holds.

For \(d\le2\), the local packing bound (8) gives \(N_H(2^k)=O(2^{dk})\). The series in (12) then diverges without any bound on \(N(r)\). Thus \(s=c\) a.e. for every locally finite \(\Xi\subset\mathbb R^d\), \(d=1,2\). Applying the sandwich (2), using rational radii and excluding bisectors, shows that every stable allocation agrees with them a.e.

This covers unsated centres and unclaimed sites through (3)–(5); no assumption that all centres are sated globally was made. It also covers disconnected centre graphs: the argument starts in one reachable component. A finite disagreement graph is impossible already at the infinite-path construction. Empty and finite centre sets cause no exception. The results were stated for \(0<\alpha<\infty\). At \(\alpha=0\), countability forces all sites to be unclaimed a.e.; at \(\alpha=\infty\), a centre always covets a finite-distance site in \(\mathbb R^d\), since a bounded ball has finite volume, so stability forces the nearest-centre allocation a.e. These endpoint cases do not enter the proof above.

### Independent check against the original disagreement construction

The key packing step can be recovered without using the extremal inequalities. In HHP Section 3, let

\[
U_v=\psi_1^{-1}(v)\cup\psi_2^{-1}(v),\quad
r_v=\sup\{r:\mathcal L(U_v\cap B(v,r))<\alpha\},\quad
N_v=D_v\cap B(v,r_v).
\]

HHP Lemma 8 makes \(M_v\cap N_v\) null. An incoming edge \(u\to v\) has a.e. disputed site \(x\in M_v\setminus N_v\), so

\[
r_v\le|x-v|<|x-u|.
\]

In particular \(r_v\) is finite. Outgoing edge sites from \(v\) lie within \(r_v\). Thus the radii are uniformly bounded on the descendants of a fixed edge. Continuity of \(r\mapsto\mathcal L(U_v\cap B(v,r))\) implies

\[
\mathcal L(U_v\cap B(v,r_v))=\alpha
\]

when \(r_v<\infty\). Across all centres, these union territories have multiplicity at most two. Their bounded-radius pieces therefore give (7) with an additional factor two. HHP Lemma 12 and Proposition 13 supply a finite-energy unit flow, and the cut argument above gives the same contradiction in \(d\le2\), or under (A). This second derivation checks the crucial local-density assertion separately from the extremal-flow derivation. Further case notes are in [data/proof_audit.md](data/proof_audit.md).

## 4. What remains of the counterexample route

Increasingly dense clusters on the line cannot give the requested example: the dimension-1 result above covers them even if their bounded-edge graphs are transient. The explicit quadratic-count example \(\Xi_0\) in Section 1 shows that the recurrence hypothesis is genuinely stronger than necessary.

For \(d\ge3\), (8) only gives \(N_H(r)=O(r^d)\). The series used in the contradiction can then converge. The argument therefore does not eliminate a bounded-density, transient disagreement graph in those dimensions. No compatible pair of stable Lebesgue allocations realizing such a graph was constructed here.

The original paper already gives a different-measure example immediately after Theorem 3, reprint p. 5: alternating odd and even harmonic-sum positions carry centres and unit point masses, and left-versus-right assignments are both stable. Atomic site mass is essential to that displayed example. It is not a counterexample for Lebesgue measure. Allowing infinitely many centres in a bounded region also leaves the present locally finite setting. Neither alteration is counted as an answer to F0083.

## 5. Finite-grid computation: evidence and its limits

The implementation is [code/grid_allocations.py](code/grid_allocations.py). It contains independent site-proposing and centre-proposing deferred-acceptance algorithms, followed by exhaustive capacity and blocking-pair checks. Forty additional finite instances with random strict shared costs, different quotas and unequal supply were checked first.

The deterministic candidate is

\[
\Xi=\delta+\bigcup_{n\ge1}\{\pm(n+j/(10n^2)):0\le j<n^2\},
\qquad \delta=\sqrt2/1000.
\]

It is locally finite and \(N(r)\sim(2/3)r^3\). Its complete bipartite links between successive same-sign clusters also permit a finite-energy flow, so it is not protected by HHP Theorem 2's recurrence assumption. The dimension-1 proof above does protect it.

For truncation index \(n\), centres from layers 1 through \(n\) were kept, and site cell midpoints covered \([-n-2,n+2]\) at spacing \(h\in\{1/32,1/64,1/128\}\). Appetite was \(\alpha=1\), hence integer quota \(1/h\). Each cell is indivisible in these experiments: this is a finite discrete approximation, not exact integration of the continuum territories. The irrational translation prevents receiver distance ties on the rational grid; strictness was checked numerically for every preference list. The smallest observed adjacent preference gap was positive and is recorded per run.

Both algorithms terminated with **zero differing cells in every run**, including the fixed observation interval \([-2,2]\). At each fixed mesh, assignments in that interval also remained unchanged as \(n\) increased through 4, 8, 12 and 16. Every terminal allocation passed an exhaustive blocking-pair check. Raw site coordinates and both allocations are in `data/grid_n*_r*.csv`; the nested centre coordinates are in `data/centres_n*.csv`. Summaries are in [data/grid_results.csv](data/grid_results.csv), [data/grid_results.json](data/grid_results.json) and [data/grid_run.log](data/grid_run.log).

Finite agreement has a structural explanation. With strict preferences induced by a shared pair cost, the globally cheapest remaining site–centre pair with residual capacity must be matched: otherwise both sides would prefer it to their assignments, or the centre would have spare capacity. Remove that site, reduce that centre's quota by one, and repeat. Induction gives a unique finite stable matching. A common total ordering resolves any irrelevant global ties consistently. Thus **even an infinite-volume counterexample would not require a disagreement in any finite terminal experiment**. These computations cannot distinguish two infinite stable boundary conditions. No convergence theorem to a distinct pair of infinite limits is claimed.

| Layers | Grid spacing | Centres | Grid cells | Differing cells | Blocking pairs, each allocation | Core changes from prior window |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 1/32 | 60 | 384 | 0 | 0 | — |
| 8 | 1/32 | 408 | 640 | 0 | 0 | 0 |
| 12 | 1/32 | 1300 | 896 | 0 | 0 | 0 |
| 16 | 1/32 | 2992 | 1152 | 0 | 0 | 0 |
| 4 | 1/64 | 60 | 768 | 0 | 0 | — |
| 8 | 1/64 | 408 | 1280 | 0 | 0 | 0 |
| 12 | 1/64 | 1300 | 1792 | 0 | 0 | 0 |
| 16 | 1/64 | 2992 | 2304 | 0 | 0 | 0 |
| 4 | 1/128 | 60 | 1536 | 0 | 0 | — |
| 8 | 1/128 | 408 | 2560 | 0 | 0 | 0 |
| 12 | 1/128 | 1300 | 3584 | 0 | 0 | 0 |
| 16 | 1/128 | 2992 | 4608 | 0 | 0 | 0 |

The run used one thread at inherited nice 10. Its measured peak resident set was **1,038,286,848 bytes** (about 1.04 GB), below the 4 GB limit. The sum of measured run times was about **25.15 seconds**. All allocations and coordinates are saved as plain numerical CSV. No PDFs, paper images or scans were written to this directory.

To reproduce from this directory, in a shell already running at nice 10:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B code/grid_allocations.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B code/audit_outputs.py
```

The solver sets the other common numerical-library thread limits to one before importing NumPy and checks its inherited priority. The fetch script, `code/fetch_text.py`, downloads PDF bytes into memory and pipes them directly through `pdftotext`; only text and source hashes are retained. `code/citation_search.py` reproduces the forward-citation query.

## 6. Audit and deliverables

A second program, [code/audit_outputs.py](code/audit_outputs.py), reloaded every saved CSV without calling either solver, recomputed capacities and every possible blocking pair, checked both outputs agree, and rechecked the changes in the observation interval. It passed all 12 runs; results are in [data/audit_results.json](data/audit_results.json). Centre counts were checked independently against

\[
2\sum_{j=1}^n j^2=\frac{n(n+1)(2n+1)}3,
\]

and site counts against \(2(n+2)/h\). The saved JSON and console-log records agree exactly. The proof's local-density step was independently re-derived from the original disputed-union construction, as detailed above. The proof does not use the numerical agreement.

[LOG.md](LOG.md) records the work as it proceeded. [data/source_manifest.jsonl](data/source_manifest.jsonl) records URLs, download times and hashes. Sources are retained only as plain text in `sources/`; code is in `code/`, numerical outputs and audit notes in `data/`. No publication, external writes, pushes or subagents were used.

Task: “Open problem F0083” — 2026-11-13 11:59 +04 (Asia/Tbilisi).
