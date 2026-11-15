RESOLVED_IN_LITERATURE

# C0151: independent-set densities on random regular graphs and FIID on trees

The general conjecture is false, including its version with closures. Gamarnik–Sudan proved a gap for all sufficiently large degrees; Rahman–Virág proved asymptotic half-optimality. Gerencsér–Harangi, **Theorem 12.1, p. 39**, arXiv:2510.12600v3, 12 March 2026, makes the gap explicit for **every integer d ≥ 403**. This last source is a preprint; the general refutation was already published. Degrees **3 and 4 remain open in the literature located here**. No claim is made that 403 is the smallest degree with a gap.

A separate certificate below gives the concrete example

\[
f_{1000}\le0.0106<0.0107<\alpha^*_{1000},
\]

where \(f_d\) is the supremum of measurable FIID independent-set densities on the tree and \(\alpha_d^*\) is the limiting maximum independence ratio of uniform simple random d-regular graphs. This applies existing theorems, with rational interval verification of the numerical inequalities. It is not a new resolution.

## 1. Statement and conventions

The [current linked notes](https://math.bme.hu/~gabor/PGG.pdf), retrieved 13 November 2026, are dated **3 April 2024**, 243 pages. The text is saved in [sources/pete_current.txt](sources/pete_current.txt), with URL, retrieval time, hash and page markers. The older course webpage's date does not describe its current linked file.

Conjecture 14.16 remains on **printed p. 214**, also PDF page 214. It asserts equality between possible independent-set densities in random d-regular graphs and those obtainable as IID factors on d-regular trees. The preceding paragraph explicitly discusses “all possible limit densities.” The conjecture's sentence itself specifies **no closure, convergence mode, or separate degree quantifier**. The immediately preceding Theorem 14.15, p. 213, treats d ≥ 3, the nontrivial range considered here. This location in the notes does not acknowledge the refutation.

Here is a precise interpretation. Fix d ≥ 3, take n tending to infinity with nd even, and let \(G_{n,d}\) be uniform over labeled simple d-regular graphs. A density p is achievable if one can select independent sets \(I_n\), using the whole graph and optional additional randomness, with \(|I_n|/n\to p\) in probability. “Possible” does not mean occurring only on rare graphs, or averaging graph instances whose densities differ macroscopically.

For the tree side put independent uniform [0,1] labels \(U_v\) at vertices of \(T_d\). An FIID independent set is a measurable map

\[
\Phi:[0,1]^{V(T_d)}\to\{0,1\}^{V(T_d)},\qquad
\Phi(gU)=g\Phi(U)\quad(g\in\operatorname{Aut}(T_d)),
\]

whose occupied vertices are independent almost surely. Its density is \(\mathbb P(\Phi(U)_o=1)\). This requires full automorphism equivariance of the map, not just an invariant output law. Its coding radius need not be bounded or almost surely finite. Independent sequences of auxiliary marks at each vertex can be encoded in one uniform label. See Lyons, §2, pp. 3–4 in the saved author version.

Let \(\mathcal F_d\) be the set of FIID densities and \(f_d=\sup\mathcal F_d\). Independent thinning makes this set downward closed, so \(\overline{\mathcal F_d}=[0,f_d]\). We do not assume that its supremum is attained. Bayati–Gamarnik–Tetali's limit theorem and heredity of independent sets give the random-graph density set \([0,\alpha_d^*]\); proofs of these elementary consequences appear below. Equality after closure asks whether \(f_d=\alpha_d^*\). Exact equality additionally requires an FIID at the endpoint. The positive gap refutes both readings.

The degree qualification matters: if d = 2 is included literally without closure, density 1/2 is another endpoint obstruction. It is achievable asymptotically on random unions of cycles but is not an FIID independent-set density on the two-sided path. Stationarity and density 1/2 force the spins across every edge to be opposite almost surely. The root spin is then invariant under translation by two, contradicting ergodicity of the IID shift by two and of its factors. This observation is separate from the d ≥ 3 problem. Degree 1 consists of disjoint edges and poses no such problem.

## 2. Literature decision and exact source locations

Page numbers below refer to the **specific saved source versions**, not inferred journal pagination. The available Rahman–Virág and long Gamarnik–Sudan texts are author/preprint versions of published results. Publisher downloads were blocked; their journal theorem-page locations were not independently verified. The exact locations in accessible texts are given instead.

| Source | Exact location read | Result |
|---|---|---|
| Hatami–Lovász–Szegedy, [arXiv:1205.4356v1](https://arxiv.org/abs/1205.4356v1), 2012 | **Conjecture 7.13, p. 16**, `hls_v1.txt` | Random regular graphs conjecturally form a Bernoulli sequence in the local-global sense. This concerns approximation of all finite colored-neighborhood statistics. |
| HLS, [v2](https://arxiv.org/abs/1205.4356v2), 2013; GF&A 24 (2014), 269–296 | **§7, p. 15**, `hls.txt` | Already states that Gamarnik–Sudan disproved the Bernoulli-sequence conjecture. The remaining Conjecture 7.12 asks a weaker convergence question. Numbering changed. |
| Gamarnik–Sudan, [arXiv:1304.1831](https://arxiv.org/abs/1304.1831) | **Theorem 2.5, p. 7**; also Theorem 2.5, PDF p. 4 in the saved ITCS extended abstract | For every ε > 0 and all sufficiently large d, \(f_d/\alpha_d^*\le1/2+1/(2\sqrt2)+\varepsilon\). ITCS 2014; expanded publication: Ann. Probab. **45 (2017), 2353–2376**, DOI 10.1214/16-AOP1114. |
| Rahman–Virág, [arXiv:1402.0485v2](https://arxiv.org/abs/1402.0485v2), 2015 | **Theorem 2.1, p. 5**; definitions and measurable-to-local approximation, pp. 3–4 | \(\limsup_{d\to\infty}d f_d/\log d\le1\). Published as *Local algorithms for independent sets are half-optimal*, Ann. Probab. **45 (2017), 1543–1577**, DOI 10.1214/16-AOP1094. |
| Bayati–Gamarnik–Tetali, [arXiv:0912.2444v3](https://arxiv.org/abs/0912.2444v3) | **Theorem 3, p. 10**, electronic reprint | Existence of \(\alpha_d^*\) for every fixed d. *Combinatorial approach to the interpolation method and scaling limits in sparse random graphs*, Ann. Probab. 41 (2013), 4080–4115. |
| Ding–Sly–Sun, [arXiv:1310.4787](https://arxiv.org/abs/1310.4787) | **Theorem 1, p. 1**, saved author text | For d above an unspecified constant, identifies the maximum and constant-order fluctuations around \(n\alpha_d^*-c_d\log n\). Acta Math. 217 (2016), 263–340. It supplies no usable small-degree threshold. |
| Gerencsér–Harangi, [arXiv:2510.12600v3](https://arxiv.org/abs/2510.12600v3), March 2026 | **Theorem 12.1 and Lemma 12.2, p. 39; Corollary 12.3 and discussion, p. 40** | Separation for **all d ≥ 403**, even from weak limits of FIID processes. **Theorem 1.3, p. 4**, gives an explicit lower bound for every d. The introduction, p. 2, still identifies Csóka's constructions as best for d = 3,4. |

The asymptotic reason is

\[
f_d=(1+o(1))\frac{\log d}{d},\qquad
\alpha_d^*=(2+o(1))\frac{\log d}{d}.
\]

Greedy FIIDs give the first lower bound; Frieze–Łuczak gives the second asymptotic, with Ding–Sly–Sun much sharper subsequently. Eventually the quantities are, for example, at most \(1.25\log d/d\) and at least \(1.75\log d/d\), respectively. This proves failure for all sufficiently large **fixed** d. It does not justify substituting d = 1000 into an unspecified error term; §4.3 supplies a finite-degree proof.

Other requested literature was checked. Backhausz–Szegedy–Virág, *Ramanujan graphings and correlation decay in local algorithms*, **Theorem 2.2, p. 4, and Theorem 3.1, p. 7**, in [arXiv:1305.6784](https://arxiv.org/abs/1305.6784), restricts correlations, but does not determine independent-set optima. Csóka–Gerencsér–Harangi–Virág (CGHV), *Invariant Gaussian processes and independent sets on regular graphs of large girth*, **Theorem 1, p. 2**, gives the certified cubic density 0.4361; it uses FIID approximations to Gaussian waves, rather than assuming the wave itself is an FIID. Lauer–Wormald, **Theorems 1–2, pp. 2–3**, in the saved author text, gives the greedy density \([1-(d-1)^{-2/(d-2)}]/2\). Lyons' survey explains measurable factors and their various closures.

For 2014–2026 developments, Harangi's 2022 replica bounds sharpen small-degree upper bounds; Marino–Kirkpatrick's 2020/2023 work supplies algorithmic experiments, not equality; Wein's low-degree hardness work extends large-degree obstructions beyond local rules for sparse Erdős–Rényi graphs, rather than deciding small-degree regular graphs. Backhausz–Szegedy's entropy inequalities and Csóka–Harangi–Virág's *Entropy and expansion* provide further necessary constraints. The 2026 Gerencsér–Harangi update supplies the explicit threshold above. Targeted searches through 13 November 2026 found no proof or refutation for d = 3 or 4. This is a search conclusion, not a theorem that no such paper exists. Search terms, source versions and provenance are saved under `sources/`.

## 3. Small degrees and the obstruction

The strongest located construction figures are Csóka's [*Independent sets and cuts in large-girth regular graphs*](https://arxiv.org/abs/1602.02747), **§2, p. 4**, which has no numbered main theorem. It explains finite-round local implementations and reports approximately **0.445327** for d = 3 and **0.404073** for d = 4. The abstract rounds to 0.44533 and 0.40407; rounding upward must not become a strict inequality.

| d | Best located FIID construction figure | Same lower construction for random regular graphs | Best located upper bound for \(\alpha_d^*\), hence also \(f_d\) |
|---|---:|---:|---:|
| 3 | approximately 0.445327 | approximately 0.445327 | 0.45078521 (5-RSB) |
| 4 | approximately 0.404073 | approximately 0.404073 | 0.41109414 (4-RSB) |

The upper entries are Harangi, *Improved replica bounds for the independence ratio of random regular graphs*, **Table 1, p. 2**; the underlying inequalities are **Theorem 2.2, p. 6, and Corollary 2.3, p. 8**, in [the saved author version](https://users.renyi.hu/~harangi/papers/rsb_bounds.pdf). These inequalities bound every allowed substitution; numerical minimization finds good substitutions and need not establish global optimality. The table reports rounded values. Safely relaxed upper inequalities are \(\alpha_3^*<0.4507853\) and \(\alpha_4^*<0.4110942\). The paper's conjecture that its cubic bound is close to sharp does not determine \(\alpha_3^*\).

There is a numerical-proof qualification on the lower entries. **Csóka, p. 2, footnote 2**, distinguishes CGHV's proved numerical integration error bound for 0.4361 from ODE calculations without a proved numerical error bound, and says his own result uses the latter type of calculation. Thus these are the strongest reported local-construction figures, not interval-certified constants established by this audit. A certified statement is \(0.4361\le f_3\le\alpha_3^*\). An elementary rigorous baseline for d = 4 is \(1/3\le f_4\), from random greedy; this is not claimed to be the strongest rigorous baseline. The sharper Csóka figures are the standard literature comparison, with his qualification retained.

The gaps between the reported construction figures and upper bounds are approximately 0.00546 and 0.00702. Neither proves a difference between FIID and random-graph optima: the same lower construction applies to both sides, and the random-graph upper bound also applies to both. Separation needs a stronger FIID upper obstruction and an independently larger achievable random-graph density. The large-degree overlap argument supplies these, but its estimates do not establish them at d = 3,4. Conversely, finite simulations cannot prove equality for arbitrary measurable factors or endpoint attainment.

## 4. Proofs

### 4.1 Transfer of every measurable FIID density

**Local tree lemma.** For fixed d and R, the fraction of vertices of \(G_{n,d}\) whose R-ball is not a tree tends to zero in probability.

**Proof.** In the configuration model, expose a vertex's R-ball by successively pairing its half-edges. Only a constant \(M=M(d,R)\) half-edges and vertices need be exposed. Each partner is uniform among remaining half-edges. The chance of a collision with an exposed vertex at any step is at most \(dM/(nd-2M)\). A union bound gives \(O_{d,R}(1/n)\). Thus the expected bad-vertex fraction is \(O(1/n)\), and Markov's inequality gives convergence in probability.

Conditioning on simplicity preserves this conclusion. Here are the needed details of its positive limiting probability. There are \(n\binom d2\) loop patterns, each with probability \(1/(nd-1)\), and \(2\binom n2\binom d2^2\) double-edge patterns, each with probability \(1/((nd-1)(nd-3))\). Their expected counts tend to \((d-1)/2\) and \((d-1)^2/4\). For each fixed k, the k-th factorial moment of their total count tends to the k-th power of the sum of these means. Disjoint patterns give the product limit; compatible overlapping distinct patterns have at least one more prescribed edge than free vertex and contribute \(O(1/n)\); incompatible patterns contribute zero. Bonferroni bounds for having no patterns, followed by k tending to infinity, give probability \(\exp(-(d^2-1)/4)>0\). Absence of both pattern types is exactly simplicity. Every labeled simple graph has the same \((d!)^n\) configuration realizations, so conditioning gives the uniform simple model. Dividing a probability tending to zero by a probability bounded below proves the claim. □

**Transfer theorem.** Every density p of a measurable Aut(\(T_d\))-equivariant FIID independent set is achievable on random d-regular graphs. The same holds for every p in \(\overline{\mathcal F_d}\).

**Proof.** Let \(X=\Phi(U)\). For the sigma-field \(\mathcal A_r\) of labels in \(B_r(o)\), set

\[
q_r=\mathbb E[X_o\mid\mathcal A_r],\qquad
Y^{(r)}_o=\mathbf1\{q_r>1/2\}.
\]

Conditional integration over labels outside the ball gives a root-isomorphism-invariant version of \(q_r\). Applying that rule at every vertex defines an equivariant block process. Martingale convergence gives \(q_r\to X_o\) almost surely and in L1, since these sigma-fields generate all labels. Thus \(e_r=\mathbb P(Y^{(r)}_o\ne X_o)\to0\).

Thresholding need not preserve independence. Repair it by

\[
Z^{(r)}_v=Y^{(r)}_v\prod_{w\sim v}(1-Y^{(r)}_w).
\]

Adjacent vertices cannot both survive. If every Y-value in the root's closed star agrees with X, the repaired root equals X as well, because X is independent. Hence

\[
\mathbb P(Z^{(r)}_o\ne X_o)\le(d+1)e_r,
\qquad p_r:=\mathbb E Z^{(r)}_o\longrightarrow p.
\]

The repaired rule has radius R = r+1. On a finite d-regular graph, evaluate the raw Y-rule at vertices with tree r-ball and assign raw value zero elsewhere, then apply the same deletion formula. This always yields an independent set. At a vertex with tree R-ball the output distribution is its tree distribution.

Condition on the finite graph. Let \(S=\sum_v Z_v\), and let b be its fraction of non-tree R-balls. Then

\[
\left|\mathbb E[S/n\mid G]-p_r\right|\le b.
\]

Outputs at distance greater than 2R depend on disjoint label sets and are independent. If \(C_{d,R}\) bounds the number of vertices within distance 2R of a vertex, summing covariances gives

\[
\operatorname{Var}(S/n\mid G)\le C_{d,R}/n.
\]

The lemma and Chebyshev's inequality imply \(S/n\to p_r\) in probability for every fixed r. Choose radii \(r_j\) with \(|p_{r_j}-p|<1/(2j)\). Next choose increasing \(N_j\) such that for every admissible n ≥ \(N_j\), that fixed-radius algorithm's density is within \(1/(2j)\) of \(p_{r_j}\) with failure probability at most \(1/j\). For \(N_j\le n<N_{j+1}\), use radius \(r_j\). This diagonal sequence has density tending to p in probability. The radius is allowed to increase slowly in this achievement statement; each approximation is a fixed local rule.

If p is only a limit of FIID densities, use their repaired block approximations in the same diagonal argument. Therefore \(\overline{\mathcal F_d}\subseteq[0,\alpha_d^*]\), in particular \(f_d\le\alpha_d^*\). □

For the random-graph set's converse characterization, BGT gives \(\alpha(G_{n,d})/n\to\alpha_d^*\). For \(p\le\alpha_d^*\), take a maximum independent set and retain \(\min(\lfloor pn\rfloor,\alpha(G_{n,d}))\) vertices. Its density tends to p. No larger limit density is possible. Thus the set is \([0,\alpha_d^*]\).

Finally, independent thinning means replacing \(X_v\) by \(X_v\mathbf1\{V_v\le t\}\) with fresh independent uniform marks. This is an FIID independent set of density tp. It proves \(\overline{\mathcal F_d}=[0,f_d]\) without asserting endpoint attainment.

### 4.2 Overlap obstruction, including measurable factors

Here is a proof of the necessary condition behind Gerencsér–Harangi **Lemma 12.2, p. 39**.

Every finite-alphabet FIID has ordered-edge and vertex distributions π and p satisfying the edge–vertex entropy inequality

\[
\frac d2H(\pi)-(d-1)H(p)\ge0,\qquad H(p)=-\sum_i p_i\log p_i.\tag{1}
\]

To prove it, approximate the factor by finite-radius finite-alphabet rules, choosing a most probable label conditional on the ball. The root error tends to zero, so their vertex and edge distributions tend to p and π. On random regular graphs, empirical vertex and edge distributions of each fixed rule converge in probability to their tree distributions. This follows from the local tree lemma and the bounded-dependence variance argument above, also applied to edge indicators. Thus these graphs admit labelings arbitrarily close to p and π with probability tending to one.

But in the configuration model, for counts \(n_i=np_i\) and ordered-edge counts \(nd\pi_{ij}\), the expected number of such labelings is

\[
\frac{n!}{\prod_i n_i!}
\frac{\prod_i(dn_i)!}
{(nd-1)!!\;\prod_{i<j}(nd\pi_{ij})!\;
\prod_i2^{nd\pi_{ii}/2}(nd\pi_{ii}/2)!}.
\]

Allocate half-edges to types, match cross-type groups, and pair within-type groups to obtain this formula. Infeasible integral counts contribute zero. Stirling's formula makes its logarithm

\[
n\left(\frac d2H(\pi)-(d-1)H(p)\right)+O(\log n).
\]

There are polynomially many possible count vectors for a fixed alphabet. If (1) were negative, continuity of entropy gives a neighborhood with negative exponent. The first moment would exclude all labelings in that neighborhood with probability tending to one, also after conditioning on simplicity. This contradicts transfer of the approximations. Passing their error to zero proves (1).

Suppose now that an FIID independent set has density a. Couple two IID label fields by retaining each original vertex label with probability t and resampling otherwise. Applying the same factor gives independent sets A and B of density a, jointly an FIID on an enlarged IID input. Put \(b(t)=\mathbb P(o\in A\cap B)\). Then \(b(0)=a^2\), \(b(1)=a\), and b is continuous even for a measurable factor. Indeed approximate its root indicator in L1 by a finite-radius indicator with error e. The corresponding overlap is a polynomial in t, conditioning on which finitely many labels are retained, and differs from b uniformly by at most 2e. Thus b is a uniform limit of continuous functions. Every \(b\in[a^2,a]\) is attained.

Use vertex states 11, 10, 01, 00 for membership in A and B. Their probabilities are

\[
(b,a-b,a-b,1-2a+b).
\]

The independent-set constraints determine all allowed ordered-edge probabilities except \(c=\pi_{10,01}=\pi_{01,10}\). The nonzero entries have probabilities b twice, c twice, \(a-b-c\) four times, and \(1-4a+2b+2c\) once. Writing \(h(x)=-x\log x\), \(h(0)=0\), the left side of (1) is therefore at most

\[
\begin{split}
F_{d,a}(b)={}&\frac d2\{2h(b)+2h(c)+4h(a-b-c)+h(1-4a+2b+2c)\}\\
&-(d-1)\{h(b)+2h(a-b)+h(1-2a+b)\},\tag{2}
\end{split}
\]

where c maximizes edge entropy. For the parameters below its feasible interval has an interior maximum. Differentiating gives

\[
(a-b-c)^2=c(1-4a+2b+2c),\qquad
c=-(1/2-a)+\sqrt{(1/2-a)^2+(a-b)^2}.
\]

Entropy is concave in these affine probabilities, so this is the global maximum. Thus every FIID density a obeys

\[
F_{d,a}(b)\ge0\quad\text{for every }b\in[a^2,a].\tag{3}
\]

This is Gerencsér–Harangi equation (8), p. 6, and Lemma 12.2. It explains the obstruction: noise-coupled copies of a factor must traverse every intermediate overlap, while random graphs can forbid some of those overlaps. Merely having an invariant independent-set law does not give the coupling argument.

### 4.3 Explicit counterexample at d = 1000

The external existence input here is **Gerencsér–Harangi Theorem 1.3, p. 4**, with equation (7), p. 6. Set

\[
\phi_d(x)=h(x)+\frac d2h(1-2x)-(d-1)h(1-x),
\]

and let \(\alpha_d^{FM}\) be its unique root in (0,1/2). Their theorem gives

\[
\alpha_d^*\ge\alpha_d^{FM}-\varepsilon_d,
\qquad \varepsilon_d=\frac{4\sqrt2}{e}\frac{\sqrt{\log d}}{d^{3/2}}.\tag{4}
\]

We use that theorem, rather than claiming to reprove its lengthy second-moment estimates. At d = 1000, exact rational intervals from [code/certify_gap.py](code/certify_gap.py) give

\[
\phi_{1000}(0.0109)>0.0000365302322698893>0,
\qquad\varepsilon_{1000}<0.000174.
\]

The sign and unique-root characterization imply \(\alpha_{1000}^{FM}>0.0109\). Hence

\[
\alpha_{1000}^*>0.0109-0.000174=0.010726>0.0107.
\]

For the FIID upper bound choose exact rationals \(a=0.0106=53/5000\) and \(b=0.005=1/200\). They satisfy \(a^2<b<a\), and (2) gives

\[
-0.000532031524072000<F_{1000,a}(b)
<-0.000532031524071998<0.
\]

This violates (3). Any FIID density larger than a could be independently thinned to a, so all densities at least a are excluded, giving \(f_{1000}\le0.0106\). Consequently **p = 0.0107** is an achievable random-regular density by the maximum-subset argument, and is outside even the closure of FIID densities. □

The certificate uses rational interval arithmetic. Square roots are enclosed by integer square roots at scale \(10^{35}\). For logarithms it rescales to [1,2], puts \(z=(x-1)/(x+1)\), and uses

\[
\log x=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}+R_N,
\quad0\le R_N\le\frac{2z^{2N+1}}{(2N+1)(1-z^2)},\quad N=65.
\]

The same series certifies log 2 for rescaling. A finite positive series for e gives a sufficient lower bound for (4). All assertions use `Fraction`; floating point was used only for an earlier exploratory check. Outward-rounded interval endpoints are saved in [data/gap_certificate.json](data/gap_certificate.json). The explicit example does not rely on substituting into an unspecified asymptotic error or trusting a rounded table entry.

## 5. Cubic computation: evidence only

The final experiment is [code/experiment.py](code/experiment.py), with results under [data/final/](data/final/). It samples a uniform pairing of 3n half-edges and rejects the whole pairing if a loop or parallel edge occurs. Conditioning samples **uniform simple labeled cubic graphs**, without repairing a configuration. The master seed is 15120261113. Graph seeds, edge lists, rejection counts and independent-set witnesses are retained in `samples.jsonl`.

Three local constructions were compared:

1. Sixteen parallel greedy rounds: fresh IID priorities among surviving vertices, select local minima, delete their closed neighborhoods.
2. A finite Gaussian factor followed by local maxima. Coefficients come from the lowest eigenvector of radial tree adjacency with off-diagonals √3, √2, √2, … . Nonbacktracking-walk recurrences compute sphere sums on the tree and define local polynomials on every cubic graph. The extra local polynomial A−3I suppresses the constant eigenvector.
3. The Gaussian rule followed by a fixed number of parallel 1-to-2 improvements and local filling. A selected center proposes two unselected neighbors with no other selected neighbor. Proposals whose additions overlap or are adjacent conflict. Fresh IID keys retain compatible proposals. Pair choices use IID vertex keys so the construction respects isomorphisms.

Parameters were selected on **six separate training graphs of order 2000**, with three labelings each: radii {9,17,25}, improvement-round counts {0,2,5}. The best mean was **radius 25 and two improvement rounds**. Those parameters were then fixed for testing. Each test graph has 12 independent labelings. The local column averages them, rather than choosing the best labeling separately for each graph. Every rule has a bounded radius independent of n, expressed using per-vertex IID mark sequences. For very small graphs the radius can encompass the graph; their finite-size behavior is not a tree-limit estimate.

A separate global heuristic uses 24 minimum-residual-degree starts, improvements, and four annealing runs of 100n moves. Best-of-run selection occurs only in this comparator. It supplies lower bounds on sample maxima, not exact maxima or FIID densities.

For every sample at n = 20,40,60, an exact include/exclude recursion with leaf reductions and component splitting computes the optimum. For three graphs at each size, an independent binary MILP also certifies the same optimum at zero reported MIP gap: **30 exact cases and nine MILP cross-checks**.

| n | Graphs | Parallel greedy | Gaussian only | Chosen local mean ± graph SE | Exact maximum mean | Global heuristic mean |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 10 | 0.36208 | 0.39292 | 0.41125 ± 0.00566 | 0.42000 | 0.42000 |
| 40 | 10 | 0.37396 | 0.41792 | 0.42667 ± 0.00470 | 0.44000 | 0.44000 |
| 60 | 10 | 0.37000 | 0.40125 | 0.41819 ± 0.00260 | 0.43500 | 0.43500 |
| 200 | 8 | 0.37219 | 0.42344 | 0.43380 ± 0.00149 | — | 0.44375 |
| 500 | 8 | 0.37369 | 0.42552 | 0.43490 ± 0.00063 | — | 0.44550 |
| 2000 | 6 | 0.37185 | 0.42640 | 0.43613 ± 0.00027 | — | 0.44683 |

Each SE is the sample standard deviation of the independent **graph means**, divided by √(number of graphs). Labelings within one graph are not treated as independent graph samples. These are one-standard-error summaries, not rigorous confidence bounds on limiting densities. At n = 2000 heuristic outputs ranged from 0.44600 to 0.44850. This difference concerns the tested implementations; it does not establish a degree-3 FIID gap. The best reported local construction in §3 is stronger than the simple family tested here.

## 6. Verification, reproduction and scope

[code/audit.py](code/audit.py) independently rereads the data, verifies all graphs are simple and cubic, checks **706 independent-set witnesses across 52 graphs**, verifies all nine exact/MILP agreements, and recomputes summary means and standard errors. Results are in `data/final/audit.json`. The exact recursion uses \(\alpha(G)=\max(1+\alpha(G-N[v]),\alpha(G-v))\); a leaf can be included in some maximum set by exchanging its sole neighbor, and component optima add. These justify its reductions.

The d = 1000 floating-point exploration was replaced by the independent rational certificate. The literature audit checked HLS numbering changes, Pete's actual date, the ODE error qualification, and the distinction between Gaussian waves and their FIID approximations. Pilot computations remain in `data/`, with original code in `code/experiment_pilot.py`; only `data/final/` supplies the reported table.

Reproduce the certificate and audit with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/certify_gap.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/audit.py
```

To repeat the full experiment, copy the script and choose a fresh output directory: it refuses to overwrite samples. Python 3.13.2 and NumPy 2.2.3 were used; SciPy's single-thread HiGHS supplied the MILP checks. Environment details are saved with the data.

The final simulation used **one process, one numerical thread, inherited nice 10**, 34.8 seconds of wall time and peak RSS **89,931,776 bytes**, below 4 GB. Source acquisition used at most three concurrent lightweight fetch/conversion processes. No subagents were started. All task writes stayed in this directory; PDF responses were converted in memory. Only source text is retained, with no PDFs, scans or paper page images. No publication or push was performed.

The remaining mathematical questions are small-degree equality and exact FIID endpoint attainment. The general conjecture is already decided. This report stops at that literature resolution and the requested supporting proofs and evidence.

Task: “Open problem C0151.” Received 13 November 2026, 09:52 +04 (Asia/Tbilisi; first recorded task clock).
