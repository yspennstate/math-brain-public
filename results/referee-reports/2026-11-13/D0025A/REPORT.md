PROVED

# D0025: a plateau for site-disordered finite-capacity exclusion

The literature resolves the site-disordered **K=1** question: Sly's Theorem 1 applies to every nonconstant i.i.d. rate law bounded away from zero. The proof below extends the comparison to the finite-K growth graph and establishes a positive-width plateau for every finite K in the source model. The derivation uses the established growth/hydrodynamic framework and Sly's comparison. No claim of novelty is made.

## Statement and exact scope

[Seppäläinen's source](https://arxiv.org/abs/math/9906194), Section 4, PDF/printed p. 9, asks Problem 4. The exact text is preserved in [sources/problem4_exact.txt](sources/problem4_exact.txt), including the opening invitation to rigorous results and the comparison with the zero-range transition. Its specific flux question is:

> Does the flux function f_K(ρ) have a flat segment on an interval around ρ = K/2?

The model is fixed by Section 3, equation (3.1), p. 8:

\[
 L^\alpha F(\eta)=\sum_{i\in\mathbb Z}\alpha_i
 1\{\eta_i>0,\eta_{i+1}<K\}[F(\eta^{i,i+1})-F(\eta)].
\]

Here **K is any fixed positive integer**, the rates are i.i.d., and their common law is supported on [r,1], with essential infimum r>0; see the standing convention on p. 4 and Theorem 3, pp. 8–9. The rate is per departure site, independent of the number of particles there once it is positive. It is not α_i η_i(K−η_{i+1}) or a per-particle total rate. Section 1, p. 2, expressly says particle disorder is not explicitly considered, except for the ordinary exclusion/gap correspondence.

Let H_K be the homogeneous rate-one flux of this same process and let

\[
 M_K=\max_{0\le\rho\le K} H_K(\rho)=H_K(K/2),\qquad
 J_K=rM_K,\qquad \mu=\frac1r-\mathbb E\frac1{\alpha_0}.
\]

**Theorem A (proved below).** For every finite K and every nonconstant i.i.d. law on [r,1],

\[
 \boxed{\quad f_K(\rho)=J_K\quad\text{whenever}\quad
 |\rho-K/2|\le\mu J_K.\quad} \tag{A}
\]

In particular μ>0 and M_K>0, so this is a nondegenerate flat interval containing K/2 in its interior. Moreover max f_K=J_K. No atom, density, gap in the support, dilution, or power-tail assumption is required. The interval in (A) is a guaranteed subinterval; its endpoints need not be the actual critical densities. For K=1, M_1=1/4, so (A) is exactly Sly's stated interval. For K>1 no explicit formula for M_K is asserted.

Constant rate laws are excluded from this assertion about a positive width: μ=0 for those laws. For instance homogeneous K=1 has the strictly concave flux rρ(1−ρ). Essential infimum zero and dependent environments are outside Theorem A.

## Literature first: what the printed results cover

The search and source retrieval were performed on 13 November 2026. Full text was inspected where listed below; inaccessible references are identified rather than assigned guessed theorem numbers. All retained source documents are plain text. Page breaks in the extracted texts preserve PDF page numbering, and sources/manifest.jsonl records URLs, retrieval times, and hashes.

| Reference | Exact result/location checked | Consequence and limitation |
|---|---|---|
| [Seppäläinen, arXiv:math/9906194v1](https://arxiv.org/abs/math/9906194) | Eq. (3.1), PDF p. 8; Theorem 3, pp. 8–9; Problem 4, p. 9; Theorem 2, p. 8 and eqs. (2.15)–(2.16), p. 7 | Defines site-disordered finite K and proves hydrodynamics with a concave, initially unidentified flux. Theorem 2 gives the constant-rate ZRP hydrodynamics, including its supercritical constant-flux part. |
| [Sly, *Note on the flux for TASEP with general disorder*, arXiv:1609.06589v1](https://arxiv.org/abs/1609.06589) | **Theorem 1, PDF p. 1**, proof pp. 2–4 | K=1, nonconstant i.i.d. positive rates with positive essential infimum r. Flux r/4 on [1/2−μr/4,1/2+μr/4]. Covers atoms at r, a gap above such an atom, and continuous laws with arbitrary endpoint tails. This is a publicly available theorem/preprint; no journal publication of this note was verified. |
| [Bahadoran–Bodineau, *Quantitative estimates for the flux of TASEP with dilute site disorder*, EJP 23 (2018), paper 44; arXiv:1602.06718v4](https://arxiv.org/abs/1602.06718) | **Proposition 2.1, PDF p. 6; Lemma 2.3 and Theorems 2.4, 2.6, p. 7; assumption (H), p. 9; Remark 2.5, p. 7** | K=1, law (1−ε)δ_1+εQ, inf supp Q=r∈(0,1). Under (H), plateau for sufficiently small ε; critical endpoints tend to (1±√(1−r))/2 and f_ε tends uniformly to min{ρ(1−ρ),r/4}. Lemma 2.3 makes Q([r,r+u))=O(u^κ), κ>1, sufficient for (H). Their (H) was not proved for Q=δ_r; Sly removes that obstacle for plateau existence. Their endpoint/dilute-limit results contain information absent from Sly's width bound. |
| [Krug–Ferrari, J. Phys. A 29 (1996), L465–L471](https://doi.org/10.1088/0305-4470/29/18/004) | Publisher and author's abstract checked; full-paper download unavailable | Particle disorder, K=1: phase transition under an endpoint integrability condition. Do not apply this statement to site disorder. The formula and rigorous hydrodynamic statement are also available in Seppäläinen's survey, pp. 7–8. No unverified theorem number is supplied. |
| [Evans, EPL 36 (1996), 13–18; arXiv:cond-mat/9606036](https://arxiv.org/abs/cond-mat/9606036) | Eq. (6), PDF p. 4 (printed manuscript p. 3), exact weights; forward-only reduction on same page; condensation discussion pp. 5–6 | Particle disorder, K=1. Exact finite-ring stationary weights and Bose condensation analogy; the low-density particle current is linear rρ, not a horizontal current plateau. This paper does not number its conclusions as theorems. |
| Seppäläinen–Krug, *Hydrodynamics and platoon formation for a totally asymmetric exclusion model with particlewise disorder*, J. Stat. Phys. 95 (1999), 525–567 | Bibliography confirmed against Krug's author publication list and the other source texts; full article not obtained | Rigorous K=1 particle-disorder hydrodynamics. For an actually inspected theorem use the author's survey **Theorem 2, PDF p. 8**, not a guessed theorem/page from this article. |
| [Krug, *Phase separation in disordered exclusion models*, Braz. J. Phys. 30 (2000), 97–104; arXiv:cond-mat/9912411](https://arxiv.org/abs/cond-mat/9912411) | Sec. 2.1, PDF pp. 3–4, eqs. (2)–(5); Sec. 3.2, pp. 6–8, eqs. (11)–(16) | Explains the particle-gap mapping, tail criterion, slow-stretch ceiling and conjectured phase separation. The sorting-all-slow-sites-into-one-block step behind eq. (14) is expressly described as unproved. It cannot be used as a rigorous lower bound. |
| [Tripathy–Barma, PRL 78 (1997), 3039–3042; arXiv:cond-mat/9704218](https://arxiv.org/abs/cond-mat/9704218) | Full four-page preprint, including exclusion discussion and phase-separated profile | Heuristics and numerical evidence for site-disordered exclusion. Their exact stationary solution concerns drop-push dynamics, a different model; it is not an exact stationary solution of disordered TASEP. |
| [Harris–Stinchcombe, PRE 70 (2004), 016108; arXiv:cond-mat/0403062](https://arxiv.org/abs/cond-mat/0403062) | Full text, abstract and mean-field closure | Mean-field and continuum analysis of a flat regime. These approximations are not a proof for the interacting exclusion process. |
| [Basu–Sidoravicius–Sly, arXiv:1408.3464v2 (2014)](https://arxiv.org/abs/1408.3464) | **Theorem 2, PDF p. 3** | Any single bond slowdown produces diagonal exponential-LPP time constant >4, hence maximal current <1/4. This is not an i.i.d. environment, and its current is not r/4. A defect does not change the homogeneous bulk flux ρ(1−ρ); it imposes a capacity constraint. |
| [Bahadoran, *Blockage hydrodynamics of one-dimensional driven conservative systems*, Ann. Probab. 32 (2004), 805–854](https://doi.org/10.1214/aop/1079021465) | Published abstract/bibliography checked; full-text endpoint returned HTML rather than the paper | A local blockage's hydrodynamics is described through a maximal-current parameter, under shape/coupling hypotheses. This does not by itself compute that parameter or prove an i.i.d. finite-K plateau. No unverified theorem number is claimed. |
| [Seppäläinen, *Existence of hydrodynamics for the totally asymmetric simple K-exclusion process*, Ann. Probab. 27 (1999), 361–415](https://doi.org/10.1214/aop/1022677266) | Primary article's bibliographic record and author survey Theorem 3 checked. Euclid's PDF endpoint was inaccessible. Independently inspected the author's [exclusion notes](https://people.math.wisc.edu/~tseppalainen/excl-book/ajo.pdf): **Theorems 9.3–9.5, printed/PDF pp. 140–141; Lemma 9.11, pp. 148–149; eqs. (9.40)–(9.44), pp. 148–150** | The homogeneous shape, symmetry, duality, and the actual finite-K growth graph used below. These notes, rather than an invented original theorem number, support the detailed graph construction. The site's disordered shape/hydrodynamic framework is the result summarized in the 1999 survey. |
| [Bahadoran–Guiol–Ravishankar–Saada, AIHP 50 (2014), 403–424; arXiv:1201.2160v2](https://arxiv.org/abs/1201.2160) | **Theorem 2.1, preprint PDF p. 6** | Quenched Euler hydrodynamics for bounded attractive systems in ergodic environments. Existence of a flux is not a theorem that it has a plateau. Guiol, not Mountford, is an author of this particular hydrodynamics paper. |
| [Bahadoran–Mountford–Ravishankar–Saada, Ann. Probab. 48 (2020), 404–444; arXiv:1801.01654v3](https://arxiv.org/abs/1801.01654) | **Theorem 2.1, preprint PDF p. 10**; flux definitions in Sec. 2 | ZRP hydrodynamics including condensation under averaging/defect hypotheses. It does not identify a site-disordered finite-capacity exclusion flux. Their 2014 preprint arXiv:1411.4305 is about supercritical ZRP convergence, not a general-K exclusion plateau. |
| [Emrah–Janjigian–Seppäläinen, EJP 26 (2021), paper 33; arXiv:1908.09319](https://arxiv.org/abs/1908.09319) | Sec. 2.4, preprint PDF pp. 13–14; **Theorem 3.10, p. 21** | Explicit shape/current asymptotics for integrable rates attached to particle/hole labels. Fixed spatial bond disorder does not have their separable row/column rate structure. Their later [2024/2025 anomalous-geodesics work](https://arxiv.org/abs/2408.13382) concerns the same type of inhomogeneous corner growth, not this missing finite-K flux calculation. |
| [Jeff Calder, *Directed last passage percolation with discontinuous weights*, arXiv:1402.3381v2](https://arxiv.org/abs/1402.3381) | **Theorem 1, PDF p. 6** and abstract | Deterministic macroscopic inhomogeneity, not stationary microscopic i.i.d. site disorder. No relevant “Calder–Mannion” joint result was located despite searches for both names with exclusion, hydrodynamics and TASEP; that bibliographic item remains unidentified. |

Searches also included “site disorder TASEP flat flux,” “K-exclusion plateau,” “K-exclusion flat segment,” and 2014–2026 variants. A 2026 space-time-discontinuity hydrodynamics preprint, arXiv:2605.13512, concerns macroscopic speed functions rather than the i.i.d. finite-K question. Search coverage is not a proof that no other theorem exists. In the inspected literature the theorem resolving the general i.i.d. **K=1** plateau is Sly's. Thus RESOLVED_IN_LITERATURE would overstate what was verified for arbitrary K; the additional finite-K argument is supplied below.

## What the phase transition means

Bahadoran–Bodineau's additional input (H) is specifically a finite-box current estimate: there must be constants b∈(0,2), a,c,β>0 such that, for sufficiently small ε and every N,

\[
 \mathbb P_\varepsilon\{j_{\infty,[0,N]}\le r/4+aN^{-b/2}\}\le cN^{-\beta}.
\]

Here j_∞ is the stationary current in a maximally driven open box, including its entrance and exit rates. This says that atypically low finite-box capacities are sufficiently rare. It is not just the existence of a minimal-rate atom or of long slow stretches. Their dilute limit is taken after the infinite-volume flux is defined; at ε=0 itself the homogeneous flux is ρ(1−ρ), so that limit does not commute with removing all defects first.

| Case | Plateau/transition decision |
|---|---|
| Particle disorder, K=1 | Condensation iff R_*<∞, as specified below. Physical flux is rρ in that phase; it is not a horizontal plateau about half filling. |
| Particle disorder, K>1 | Not specified by the source; no gap-to-ZRP theorem for such unspecified dynamics is claimed. |
| Site disorder, K=1 | General nonconstant i.i.d. law bounded away from zero: Sly Theorem 1. Dilute quantitative endpoints: Bahadoran–Bodineau under (H). |
| Site disorder, any finite K>1 | Same general nonconstant i.i.d. law: Theorem A proved here. No endpoint atom, support gap or dilution is needed. |

For **particle disorder with K=1**, write X_i for the ordered particle positions and g_i=X_{i+1}−X_i−1. When particle i jumps at its own rate a_i, g_i decreases by one and g_{i−1} increases by one, provided g_i>0. These gaps are precisely a constant-rate ZRP with site rates a_i, running toward decreasing labels. Its current is the common particle speed v. Particle flux per physical bond is **ρv**, not v.

For an i.i.d. particle-rate law Q with infimum r, set

\[
 R(v)=\mathbb E\frac{v}{a_0-v},\quad 0\le v<r,\qquad
 R_* =\mathbb E\frac{r}{a_0-r}\in(0,\infty].
\]

The relation is (1−ρ)/ρ=R(v) in the fluid regime. When R_*<∞, the low-density phase 0<ρ≤ρ_p:=1/(1+R_*) has v=r and physical flux rρ: holes condense in front of exceptionally slow particles and faster particles form platoons behind them. The ZRP flux has a horizontal piece at high gap density; the particle flux has a **linear** low-density piece. Neither is a site-disorder plateau symmetric about 1/2. If R_*=∞ there is no finite critical gap density and no positive ρ_p.

In fact this standard particlewise current–density relation has no horizontal interval anywhere in (0,1). In the fluid regime, R'(v)=E[a_0/(a_0−v)^2]>0 and R''(v)=E[2a_0/(a_0−v)^3]>0 for v<r; differentiation is justified by the positive distance from v to r. If ρv were a positive constant J on a fluid density interval, then ρ=J/v and the density relation would force R(v)=v/J−1 on the corresponding velocity interval, contradicting R''>0. In the condensed regime rρ is strictly increasing. Any nonempty putative plateau interval contains a subinterval of one of these two regimes, so it is impossible. This conclusion is for the usual K=1 particlewise model with its physical-bond current normalization.

An endpoint density proportional to (a−r)^β has R_*<∞ exactly when β>0. An atom at r makes R_*=∞. Consequently a two-point i.i.d. law with a positive fraction of slow particles has no such condensation transition, whereas the same two-point **site** law has the plateau in Theorem A. A gap just above the minimum, with an atom at the minimum, does not cure the particle integral. A single distinguished slower particle separated from the fast bulk is another model, not an i.i.d. law with a positive density of minimum-rate particles.

There is **no defined particlewise K>1 model in Problem 4**. Several choices of label order, service discipline and per-particle versus per-site clocks are possible and have different generators. With coincident particles the ordinary gaps X_{i+1}−X_i−1 can even be negative; arrival-capacity constraints couple the gaps. The preceding ZRP correspondence is therefore not a proof for unspecified particlewise K>1 dynamics. Theorem A resolves the finite-K site model actually defined in the source, not those additional models.

For **site disorder**, long stretches of nearly minimal rates impose the maximal current J_K of a homogeneous rate-r system. Added mass near half filling can be stored by changing the fractions of low- and high-density regions while this bottleneck current stays fixed. Tripathy–Barma and Krug's arguments describe this mechanism, but the existence of long stretches alone gives only the upper capacity bound. A lower bound at densities on both sides of half filling is essential. Bahadoran–Bodineau obtain this by multiscale estimates for dilute disorder under (H); Sly obtains it for K=1 by adding independent exponential delays. The next proof adapts that comparison to finite K.

A flux plateau is the macroscopic signature requested in Problem 4. It is not, by itself, a theorem about a unique finite-ring condensate, its location, interface fluctuations, or equilibration time. Such stronger microscopic assertions are not claimed here.

## Proof of Theorem A

### 1. The growth representation and the imported shape theorem

We use the existing hydrodynamic/growth-shape theorem for the source model. Here are the precise shape properties needed, so that the imported result is separated from the new comparison.

Let

\[
 C_K=\{(x,y): y\ge0,\ y+Kx\ge0\}.
\]

Take lattice paths with steps

\[
 (0,1),\qquad (1,0),\qquad (-1,K). \tag{1}
\]

Given α, put independent exponential weights Y_{i,j} of rate α_i on vertices. Let T_α(i,j) be the maximal weight from (0,0) to (i,j), omitting the starting weight. The graph is acyclic: the function 2j+Ki strictly increases on each step. All predecessor sets between fixed endpoints are finite.

The shape theorem gives the deterministic, finite, continuous, concave, degree-one homogeneous limit

\[
 \tau_\alpha(x,y)=\lim_{n\to\infty} n^{-1}T_\alpha(\lfloor nx\rfloor,\lfloor ny\rfloor)
 \quad\text{in probability in the interior of }C_K. \tag{2}
\]

Lattice approximations are taken inside the cone. Inverse passage times give the wedge-current shape k_α, and duality gives

\[
 k_\alpha(v)=\inf\{y\ge\max(0,-Kv):\tau_\alpha(v,y)>1\},\qquad
 f_K(\rho)=\inf_{v\in\mathbb R}\{k_\alpha(v)+v\rho\}. \tag{3}
\]

The inverse is understood by continuity at boundaries. In particular,

\[
 \max_\rho f_K(\rho)=k_\alpha(0)=1/\tau_\alpha(0,1). \tag{4}
\]

These are the growth-shape and duality framework of Seppäläinen's site-disordered K-exclusion hydrodynamics, summarized by Theorem 3 and the paragraph after (3.2), survey pp. 8–9. The homogeneous versions, including positivity of H_K and its reflection symmetry, are explicitly given in the author's notes, Theorems 9.3–9.5, pp. 140–141. Passage times and the graph are Lemma 9.11 and (9.40)–(9.44), pp. 148–150. The proof below uses this established framework; it does not claim a new proof of the underlying hydrodynamic theorem.

The current version of the framework can also be recovered directly from the survey's density theorem, so it does not require assigning an unverified theorem number to the inaccessible original article. Start with the wedge η_i(0)=K1{i≤0} and choose h_i(0)=K min(i,0). The rightmost occupied site increases by one at a rate at most one, so its position by time nt is stochastically bounded by a Poisson(nt) variable. For a fixed L>t, with probability tending to one h_{nt}(⌊nL⌋)=0. The identity h_{nt}(⌊nx⌋)=−∑_{i=⌊nx⌋+1}^{⌊nL⌋}η_i(nt), followed by Theorem 3, determines the height limit, including its additive constant. The wedge specialization of the survey's Hopf–Lax formula (3.2) is t f_K^*(x/t), giving (3). For fixed x, the limiting growth G_x(t)=t k_α(x/t) is a nondecreasing convex function of t (the perspective of the convex function k_α). It starts at max(0,−Kx), tends to infinity, and is strictly increasing once above that starting value: any positive secant slope of a convex nondecreasing function bounds its subsequent secant slopes below. Growth to infinity follows from comparison with the homogeneous rate-r process, whose central current is positive. Thus every y>max(0,−Kx) has a unique inverse time, and bracketing at times on either side proves the passage-time limit (2) in probability. The path tail bound below then gives convergence in expectation. Homogeneous passage-shape concavity also follows directly by concatenating paths, taking expectation limits and using homogeneity. These are the usual height/passage formulations of the same established hydrodynamic theorem.

To check that the graph is the right graph, let h_i−h_{i−1}=η_i, with a permitted jump reducing h_i by one. Before h_i can reach level h, it must previously have reached h+1, h_{i−1} must be at most h, and h_{i+1} at most h+K. Therefore the completion-time recurrence is

\[
 T(i,h)=\max\{T(i,h+1),T(i-1,h),T(i+1,h+K)\}+Y_{i,h}. \tag{5}
\]

The exponential waiting times are independent conditional on α: once a cell becomes eligible it remains eligible until its own clock rings, and fresh Poisson increments are independent of the predecessors. The usual inductive ordering by predecessors proves this as in Lemma 9.11; the same argument holds for fixed unequal rates. Replace h by −j to obtain (1). The wedge source is shifted by one vertical unit to place it at (0,0); this changes no macroscopic limit. For K>1 the vertical edge in (1) must be retained.

The convergence in (2) also holds in expectation. Indeed, for endpoint (i,j), if a,b,c count the three steps, then j=a+Kc and i=b−c. Hence the number of steps is bounded by |i|+2j. The number of paths is at most 3^{|i|+2j+1}; along any one path the independent weights are stochastically dominated by rate-r exponentials. A Chernoff bound followed by a union bound gives an exponentially decaying tail beyond a constant multiple of |i|+j. This proves uniform integrability of T/n on each fixed ray. Starting-point conventions add only a single integrable weight.

Write τ_1 for the homogeneous rate-one shape and A=τ_1(0,1)/r. By (4) for the homogeneous model, τ_1(0,1)=1/M_K and hence

\[
 A=1/(rM_K)=1/J_K. \tag{6}
\]

### 2. Homogeneous symmetry supplies a supporting plane

The transformation

\[
 S(x,y)=(-x,y+Kx)
\]

permutes the east and northwest steps in (1), fixes the vertical step and preserves the cone. The i.i.d. homogeneous weights have the same law after this transformation. Thus

\[
 \tau_1(x,y)=\tau_1(-x,y+Kx).
\]

Concavity and homogeneity now imply

\[
 \tau_1(x,y)
 \le \tau_1(0,y+Kx/2)
 =(y+Kx/2)\tau_1(0,1). \tag{7}
\]

This argument uses no differentiability and no formula for H_K. After scaling all rates to r, (7) becomes τ_r(x,y)≤A(y+Kx/2).

### 3. Sly's exponential addition works on the finite-K graph

Conditional on α, independently of all Y, take

\[
 U_{i,j}=B_{i,j}E_{i,j},\qquad
 B_{i,j}\sim\operatorname{Bernoulli}(1-r/\alpha_i),\quad E_{i,j}\sim\operatorname{Exp}(r).
\]

All these auxiliary variables are conditionally independent. Set Z=Y+U. For s≥0,

\[
 \mathbb E[e^{-sZ_{i,j}}\mid\alpha]
 =\frac{\alpha_i}{\alpha_i+s}
 \left[\frac r{\alpha_i}+
 (1-\frac r{\alpha_i})\frac r{r+s}\right]
 =\frac r{r+s}. \tag{8}
\]

Consequently the whole Z field, conditional on α, is i.i.d. Exp(r) with a law that does not depend on α. Also

\[
 \mathbb E[U_{i,j}\mid\alpha,Y]=d_i:=1/r-1/\alpha_i\ge0,
 \qquad \mathbb E d_i=\mu. \tag{9}
\]

Choose a maximizing Y-path γ by a deterministic tie rule. It is measurable with respect to (α,Y), and

\[
 T_Y=\sum_\gamma Z-\sum_\gamma U\le T_Z-\sum_\gamma U.
\]

Every path from column 0 to column i visits each intervening column: its horizontal increments belong to {−1,0,1}. Conditional expectation using (9) therefore yields

\[
 \mathbb E\sum_\gamma U\ge |i|\mu,
 \qquad \mathbb E T_Y(i,j)\le\mathbb E T_Z(i,j)-|i|\mu. \tag{10}
\]

For i>0 use columns 1,…,i; for i<0 use i,…,−1, so omitting the starting vertex causes no loss. Taking the expectation limits justified above, and then using (7), proves

\[
 \boxed{\quad\tau_\alpha(x,y)\le\tau_r(x,y)-\mu|x|
 \le A(y+Kx/2)-\mu|x|.\quad} \tag{11}
\]

It is essential that U is independent of Y **conditional on α**. One cannot subtract an unconditional mean along a path that was selected using those same auxiliary delays.

### 4. Long slow stretches fix the height of the plateau

First, couple weights as Y_{i,j}=E_{i,j}/α_i with E i.i.d. Exp(1). Since α_i≥r, comparison gives

\[
 \tau_\alpha(0,1)\le \tau_1(0,1)/r=A. \tag{12}
\]

Here is the reverse bound, including the step that is sometimes hidden behind an appeal to long stretches. Fix an integer m and ε>0. The event α_i≤r+ε has positive probability by the definition of essential infimum. For any fixed length ℓ, disjoint ℓ-site blocks are independent and have positive probability of being entirely slow. The probability none of the first N blocks is slow is (1−p_ε^ℓ)^N→0. Thus arbitrarily many slow blocks of each fixed length occur almost surely. Intersect these events over integer lengths and positive rational ε.

Every directed path from (a,b) to (a,b+m) lies in columns [a−m,a+m]. Choose an almost surely existing slow block containing this interval. Inside this block, Y≥E/(r+ε). Let V_m be the homogeneous rate-one last-passage value from (0,0) to (0,m), omitting its start. Concatenate optimal copies of this diamond in the selected strip, moving vertically by m at a time. Their vertex sets are disjoint after removal of their starting points: two successive diamonds can meet only in the endpoint/startpoint, because their vertical ranges are successive and, on the shared row, the first has columns ≤a while the second has columns ≥a. The corresponding homogeneous block values are therefore i.i.d. copies of V_m.

There is a finite admissible path from the origin to a sufficiently high starting point (a,b). After q diamonds there is a finite connector back to column zero, requiring only a bounded extra height. All connector weights are nonnegative. Conditional on the chosen environment, the strong law applied to the independent E blocks gives, as the final vertical height tends to infinity,

\[
 \tau_\alpha(0,1)\ge\frac{\mathbb E V_m}{m(r+\varepsilon)}. \tag{13}
\]

One can choose q=floor((n−C)/m), with C depending only on the fixed strip position and connectors; then qm/n→1. Selection of the strip depends only on α and hence does not bias the independent E variables. This deals with rare strips being very far away: their distance is fixed before n→∞.

The homogeneous shape theorem and uniform integrability give E V_m/m→τ_1(0,1). Take m→∞ in (13), then ε↓0. Together with (12),

\[
 \tau_\alpha(0,1)=A,\qquad \max f_K=1/A=J_K. \tag{14}
\]

This proof needs slow intervals of every fixed length, not a macroscopic all-slow interval in a finite ring. It applies equally to an atom at r and to every positive-probability interval [r,r+ε].

### 5. The lower bound produces an interval, not just one maximizer

Take |ρ−K/2|≤μ/A=μJ_K. For every admissible point on the line y=J_K−ρx, inequality (11) gives

\[
 \tau_\alpha(x,J_K-\rho x)
 \le 1+A(K/2-\rho)x-\mu|x|\le1. \tag{15}
\]

To see explicitly why this is the required flux inequality, fix v. If y_0=J_K−ρv lies at or below the cone boundary max(0,−Kv), the trivial bound k_α(v)≥max(0,−Kv) implies k_α(v)+ρv≥J_K. Otherwise (15), monotonicity in y and the inverse definition (3) imply k_α(v)≥y_0, giving the same inequality. Taking the infimum over v in (3), f_K(ρ)≥J_K. Equation (14) gives f_K(ρ)≤J_K. This proves (A).

Finally, μ>0 since α_0≥r and P(α_0>r)>0, and M_K>0 by the homogeneous shape theorem. The interval lies in [0,K]: for K≥2, μJ_K=(1−rE[1/α_0])M_K≤1≤K/2; for K=1 use M_1=1/4. This completes the proof.

## A direct proof of the K=1 particle-gap formulas

For completeness, here is the stationary calculation underlying the different particle-disorder transition. On a ring of m labels, gaps z_i≥0 with total H move i→i−1 at rate a_i 1{z_i>0}. The probability

\[
 \pi_H(z)=Z_{m,H}^{-1}\prod_{i=1}^m a_i^{-z_i},\qquad \sum z_i=H, \tag{16}
\]

is stationary. Indeed, an incoming move at label i comes from z+e_i−e_{i−1}, possible iff z_{i−1}>0. Its weighted rate is

\[
 a_i\,\pi_H(z+e_i-e_{i-1})=a_{i-1}\,\pi_H(z).
\]

Summing over i gives π_H(z) times the total outgoing rate, after a cyclic reindexing. The finite chain is irreducible for positive rates, so this is its unique invariant law. Summing (16) over all H with fugacity v gives independent geometrical gaps with P(z_i=k)=(1−v/a_i)(v/a_i)^k for v<r. Their means are v/(a_i−v), while a_i P(z_i>0)=v. Averaging over i.i.d. rates gives R(v), and converting labels to physical length gives ρ=1/(1+R(v)) and physical current ρv.

The function R is continuous and strictly increasing on [0,r), with limit R_* by monotone convergence. Therefore a normalizable fluid product law exists at gap density h precisely for 0≤h<R_*, with v=R^{-1}(h); the critical product at v=r exists when the endpoint integral is finite. The extension of the dynamical ZRP flux to v=r for h≥R_* is the inspected literature theorem, Seppäläinen survey Theorem 2, pp. 7–8, not a consequence of product stationarity alone. This distinguishes the elementary calculation proved here from the imported condensation-regime hydrodynamics. Formula (16) alone also does not prove localization at one slow site in the thermodynamic limit.

## Computation and verification

The files contain **94 simulation records** on rings of n=2,000, 10,000, and 100,000 sites, for K=1 and K=2. The disordered law was 0.2δ_0.3+0.8δ_1. Two environment seeds were used at n=2,000; the larger sizes use one environment seed. Each environment is reused across densities and capacities. At n=100,000 that sampled environment has a longest all-slow run of only 7 sites. The homogeneous controls use rate one.

The implementation in [code/ring_sim.cpp](code/ring_sim.cpp) uses exact fixed-time Poisson uniformization: in a time window T it draws a Poisson(nT) number of candidate events, chooses a site uniformly for each event, and accepts with probability α_i when η_i>0 and η_{i+1}<K. Thus the generator is the source's generator, with no discretization of physical time. M=round(nρ) is conserved exactly and occupation bounds are checked. The estimator is total accepted jumps/(nT); currents for every individual bond and eight consecutive time blocks are also recorded. A block standard deviation describes time variation; it is **not** an independent-sample confidence interval or an estimate of disorder uncertainty.

The initial grid used burn/measurement times (10,000,10,000), (2,000,4,000), and (1,000,1,000), respectively, for the three sizes. After the initial-state comparison revealed large-ring transients, the follow-up used (10,000,10,000) on the large rings and (100,000,200,000) for three central densities on n=2,000. Data from the earlier windows were retained. Random, compact packed, and two-region initial configurations are distinguished in the CSV. The two-region profile uses local means 0.15K and 0.85K and is aligned with a longest slow run; it is an initialization diagnostic, not an assumed stationary measure.

The long n=2,000 runs, environment seed 125, give:

| K | density | current | block SD | range of individual-bond currents |
|---|---|---|---|---|
| 1 | 0.35 | 0.10089899 | 0.000573 | 0.100795–0.100965 |
| 1 | 0.50 | 0.10093241 | 0.000973 | 0.100765–0.101420 |
| 1 | 0.65 | 0.10119109 | 0.000764 | 0.101110–0.101270 |
| 2 | 0.70 | 0.15635124 | 0.001129 | 0.156060–0.156975 |
| 2 | 1.00 | 0.15578284 | 0.001236 | 0.155405–0.156980 |
| 2 | 1.30 | 0.15575077 | 0.001249 | 0.155515–0.156095 |

These support a broad central nearly flat region on the sampled finite rings. They do not identify the infinite-volume plateau height: the exact K=1 height is 0.075, substantially below these finite-size measurements. A ring's longest slow stretch grows only logarithmically with n for binary disorder, so the infinite slow-stretch ceiling is approached slowly. Finite observation time creates a separate bias.

The dependence on initial state on n=100,000 remains substantial at half filling:

| K | burn | measurement | initial state | center current |
|---|---|---|---|---|
| 1 | 1,000 | 1,000 | random | 0.11160214 |
| 1 | 1,000 | 2,000 | compact packed | 0.00194879 |
| 1 | 10,000 | 10,000 | random | 0.10256196 |
| 1 | 10,000 | 10,000 | two-region | 0.08132142 |
| 2 | 1,000 | 1,000 | random | 0.17239300 |
| 2 | 1,000 | 2,000 | compact packed | 0.00274989 |
| 2 | 10,000 | 10,000 | random | 0.16034437 |
| 2 | 10,000 | 10,000 | two-region | 0.13723497 |

**Stationarity at n=100,000 is not established.** It would be incorrect to report those large-ring points as a measured stationary flux curve with only Monte Carlo error. They are finite-time current curves. At n=2,000, extending the run reduced the across-bond mismatch and gave mutually close central currents, but a finite numerical check still is not a proof of a flat thermodynamic flux. Neither numerical observation enters Theorem A.

The homogeneous K=2 center control was 0.418840916667 on n=2,000; this is only a finite-ring estimate of M_2. In particular, no unjustified formula such as H_K(ρ)=ρ(K−ρ) was used. For the simulated rate law μ=28/15. For K=1, the proven interval from Theorem A is [0.36,0.64]; for K=2 it is |ρ−1|≤(14/25)M_2, with M_2 deliberately left symbolic.

An independent exact finite-state calculation enumerated all configurations at fixed mass, built the continuous-time generator, and solved πQ=0. [data/validation.json](data/validation.json) records the following checks:

| ring/model | exact stationary current | simulated current | difference |
|---|---|---|---|
| n=6, K=1, M=3, homogeneous | 0.300000000000 | 0.299990333333 | −0.000009666667 |
| n=6, K=1, M=3, one rate-0.3 site | 0.193332570950 | 0.193205666667 | −0.000126904283 |
| n=5, K=2, M=5, two rate-0.3 sites | 0.197132437139 | 0.197380600000 | +0.000248162861 |

Stationarity residuals were below 8×10^−17. The homogeneous K=1 result was separately checked against M(n−M)/(n(n−1)). These checks validate rates and current normalization in two capacities; they do not validate the thermodynamic phase transition by simulation.

The proof was audited a second way at its load-bearing steps: the finite-K predecessor recurrence was checked against the source notes; reflection was checked by its action on each edge; the exponential coupling was checked by its full conditional Laplace transform; the selected-path subtraction was conditioned before averaging; slow-strip diamonds were checked to share only their connecting endpoint; and the strip is chosen before taking the macroscopic limit. [code/audit_growth_graph.py](code/audit_growth_graph.py) additionally checked the finite cones and reflections for K=1,…,5 and endpoint heights through 12, with results in data/growth_graph_audit.json. This finite check supplements the general arguments, which do not depend on enumerating K.

Everything ran with one simulation worker and one thread per numerical library. The simulator reports nice=10 on all 94 records. Its three main arrays occupy about 20n bytes (approximately 2 MB at n=100,000), and it rejects inputs exceeding a fixed small allocation budget. macOS rejected the attempted address-space limit; that call had initially been unchecked and was removed. The final executable records its own peak resident memory. The n=100,000, K=2 reproduction used **3,407,872 bytes (3.25 MiB)** of peak resident memory, recorded in data/resource_usage.json, and reproduced its existing CSV row exactly. No enforced address-space cap is claimed. No external publication, push, trading process, or additional language-model worker was used.

Artifacts and reproduction:

- [data/current_density.svg](data/current_density.svg): standalone current–density plot. At a repeated density it uses the longest recorded random-initial run; all measurement windows remain in the CSV. The K=2 dotted line is a homogeneous-ring estimate times r, not an exact value.
- [data/ring_currents.csv](data/ring_currents.csv), [data/summary.json](data/summary.json), and [data/summary_tables.md](data/summary_tables.md): raw records and derived summaries.
- Build with `clang++ -O3 -std=c++17 code/ring_sim.cpp -o code/ring_sim`.
- Run `python3 code/run_simulations.py`, then `python3 code/run_longer.py`; they append records and save progress. Run the longer script only once per intended batch, since it deliberately appends a new batch.
- Run `python3 code/validate_simulation.py`, `python3 code/audit_growth_graph.py`, then `python3 code/analyze_results.py` for the checks and plot. The analyzer expects the completed 94-record batch.
- [LOG.md](LOG.md) records the progression, access limitations and the audit. [sources/manifest.jsonl](sources/manifest.jsonl) records provenance. PDF bytes were only held in memory for text extraction; no paper images, scans or PDFs were retained.

The conclusion concerns exactly the source's nonconstant i.i.d. site-disorder model, for every fixed finite K. Its plateau existence is proved in Theorem A; the exact whole flux, optimal plateau endpoints for general disorder, microscopic phase-separated invariant measures, and an unspecified particlewise K>1 model are not solved here.

Task: “Open problem D0025.” Request logged 2026-11-13 11:11 +04; work started 11:12 +04 (Asia/Tbilisi).
