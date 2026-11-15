PARTIAL

# E0030: variance of the optimal Euclidean TSP

The original conjecture is not proved here. No applicable printed proof of variance convergence was found in the search, including work from 2017 through 13 November 2026. The mathematical results below are elementary subsequential conclusions, an exactly solvable block surrogate, and conditional convergence criteria. The numerical experiment concerns heuristic tours on the torus.

## Exact source and question

Sourav Chatterjee, *A general method for lower bounds on fluctuations of random variables*, **Annals of Probability 47**(4) (2019), 2140–2171, [DOI 10.1214/18-AOP1304](https://doi.org/10.1214/18-AOP1304). The checked manuscript is [arXiv:1706.04290v3](https://arxiv.org/abs/1706.04290v3), dated 26 July 2018. Its complete, page-labelled text is `sources/chatterjee_2018_v3.txt`.

Section 3, item (2), manuscript/PDF p. **27**, asks to

> prove that the variance of the length of the optimal tour converges to a constant as the number of points tends to infinity

and, if possible, identify the constant. It specifies uniform points in **[0,1]^2** and attributes the conjecture to Mike Steele in a personal communication. In the independent sampling setting of Section 2.1 and Theorem 2.3, this is

\[
X_1,\ldots,X_n\stackrel{\mathrm{iid}}\sim\operatorname{Unif}([0,1]^2),\qquad
T_n=\min_{\pi\in S_n}\sum_{i=1}^n\|X_{\pi(i)}-X_{\pi(i+1)}\|_2,
\quad\pi(n+1)=\pi(1),
\]

and the question is whether \(\operatorname{Var}(T_n)\to\sigma_B^2\). This is **binomial input, fixed n, ordinary Euclidean distance, a square with boundary, dimension two**. Theorem 2.3, manuscript p. **12**, separately establishes a fluctuation lower bound of order \(n^{(d-2)/(2d)}\) for independent uniform cube points, every d>=2. Item (2) itself does not state a general-dimensional, Poisson or torus conjecture. [Chatterjee, pp. 12, 27](https://arxiv.org/pdf/1706.04290).

The known lower bound implies \(\liminf_n\operatorname{Var}(T_n)>0\); a uniform upper bound is independently proved below. Rhee's 1991 result is the earlier planar fluctuation lower bound.

For normalization comparisons, the tour length H_n on n points in a cube of volume n satisfies

\[
H_n\overset d=n^{1/d}T_n,\qquad
\operatorname{Var}(H_n)/n=n^{2/d-1}\operatorname{Var}(T_n).
\]

The same identity holds for Poisson input with mean n. If unit-cube length is first divided by \(n^{1-1/d}\), multiply its variance by n to obtain the quantity on the right. In dimension two, the unscaled unit-cube variance is already the order-one quantity.

## Literature audit

Searches used both spellings of traveling/travelling, the requested variance-asymptotics and CLT phrases, and all requested author leads. Raw searches are in `data/literature_search_01.json` through `09.json`, with additional primary-page and 2026 localization records. This is a documented negative search, not a proof that no unindexed result exists.

| Work | Exact result/location checked | Scope and consequence |
|---|---|---|
| Chatterjee (2019), above | Theorem 2.3, manuscript p. 12; problem (2), p. 27 | Fixed-n cube lower bound, not a variance limit. |
| Sky Cao, *Central limit theorems for combinatorial optimization problems on sparse Erdős–Rényi graphs*, Ann. Appl. Probab. 31(4) (2021), 1687–1723, DOI 10.1214/20-AAP1630 | [arXiv:1905.08366v4](https://arxiv.org/abs/1905.08366v4), Theorems 2.1–2.2, p. 5; 2.3, p. 6; general Theorem 2.4, pp. 10–11 | Matchings and edge cover on independently weighted sparse/mean-field graphs. No geometric optimal tours. No paper with the suggested Cao TSP-CLT title was located. A CLT normalized by its own finite-n variance would not alone prove variance convergence. |
| S. Chatterjee and S. Sen, *Minimal spanning trees and Stein's method*, Ann. Appl. Probab. 27(3) (2017), 1588–1645, DOI 10.1214/16-AAP1239 | [arXiv:1307.1661v4](https://arxiv.org/abs/1307.1661v4), Theorem 2.1, p. 3; introduction pp. 1–2 | Quantitative MST CLT on rate-one Poisson points in expanding cubes, d>=2. Not Hamiltonian tours. |
| H. Kesten and S. Lee, *The central limit theorem for weighted minimal spanning trees on random points*, Ann. Appl. Probab. 6(2) (1996), 495–527 | [DOI 10.1214/aoap/1034968141](https://doi.org/10.1214/aoap/1034968141); abstract p. 495 checked in the indexed original article | Fixed-n uniform cube points, d>=2, power-weighted MST. Full text was not successfully acquired locally; no unverified theorem number is assigned. Not a TSP result. |
| M. Penrose and J. Yukich, *Central limit theorems for some graphs in computational geometry*, Ann. Appl. Probab. 11(4) (2001), 1005–1041 | [DOI 10.1214/aoap/1015345393](https://doi.org/10.1214/aoap/1015345393); model scope checked; exact general hypotheses checked in the following published exposition | Poisson/binomial stabilization framework. Original journal download returned a challenge response. Its hypotheses cannot be assumed for TSP. |
| J. Yukich, *Limit theorems in discrete stochastic geometry*, Chapter 8, LNM 2068 (2013), 239–275 | [Published-layout author text](https://www.lehigh.edu/~jey0/SpringerLNMsurvey-JY.pdf): **Theorem 8.5, printed p. 258 / PDF p. 20** (Poisson); **Theorem 8.6, printed p. 266 / PDF p. 28** (binomial); de-Poissonization pp. 266–267 | Variance asymptotics and CLTs under score stabilization and moments; the displayed versions include exponential stabilization and additional binomial conditions. Variance constants differ by a squared add-one correction. TSP is treated in the subadditivity/LLN discussion, not as a verified fluctuation application. |
| J. M. Steele, *Probability Theory and Combinatorial Optimization*, SIAM, CBMS-NSF 69 (1997); J. Yukich, *Probability Theory of Classical Euclidean Optimization Problems*, LNM 1675 (1998) | [Steele publisher record](https://epubs.siam.org/doi/book/10.1137/1.9781611970029); [Yukich publisher contents](https://link.springer.com/book/10.1007/BFb0093472): uniform case pp. 32–52, concentration pp. 64–77, umbrella theorems pp. 78–96 | Background on laws of large numbers and concentration. Complete books were not acquired; no claim of checking every theorem in them. The upper bound needed here is proved independently. |
| M. Hessler and J. Wästlund, *Edge cover and polymatroid flow problems*, Electron. J. Probab. 15 (2010), 2200–2219 | [Author manuscript](https://www.math.chalmers.se/~wastlund/HesslerWastlund.pdf), Theorem 1.1, manuscript p. 3 | Independent exponential edges in a complete bipartite graph; convergence of minimum edge-cover cost in mean/probability. Neither geometric TSP nor its variance. |
| G. Ganesan, *Euclidean Travelling Salesman Problem with Location-Dependent and Power-Weighted Edges*, J. Theor. Probab. 35 (2022), 819–862 | [arXiv:2011.10716v1](https://arxiv.org/abs/2011.10716), **Theorem 3, p. 16** (variance upper bound); **Theorem 5, p. 21** (lower bound) | Bounds for generalized weights, not a variance limit. The lower-bound theorem as stated uses exponent alpha<1. |
| Z. Dong and J. Cao, *New Bounds for the Euclidean TSP Constant* (2026) | [arXiv:2610.02809v1](https://arxiv.org/abs/2610.02809), Theorem 2, p. 1 | Bounds on the BHH mean-length constant beta, not variance. Junyu Cao is distinct from Sky Cao. |
| J. Gaudio and C. Guan, *An Improved Upper Bound for the Euclidean TSP Constant Using Band Crossovers* (2026) | [arXiv:2602.11250](https://arxiv.org/abs/2602.11250), Theorem 1.1, p. 1; Section 3 | Mean-length constant and constructed tours, not optimal-tour variance convergence. |
| B. Błaszczyszyn, D. Yogeshwaran and J. Yukich, *Limit theory for Lipschitz-localized statistics in random geometric models*, 26 May 2026 | [Author preprint](https://www.lehigh.edu/~jey0/CLTMarkingMay2026.pdf), Proposition 5.3 and Theorem 5.4, pp. 38–40; applications | Weaker localization framework with variance asymptotics under hypotheses. No TSP application located. Full 194-page text saved and searched. |
| T. Trauthwein and J. Yukich, *Second-order Poincaré inequalities and localization on the Poisson space* (2026) | [Author preprint](https://www.lehigh.edu/~jey0/TYMay2026.pdf), Theorem 2.1, p. 5; Theorem 2.7, p. 10; full text searched | Normal approximation bounds and localization hypotheses, not a TSP locality verification. Cong–Xia–Yukich's 2026 dependent-marked-process CLT preprint was also checked for scope/TSP mentions. |

Gold, Wade and Barbosa were searched explicitly with Euclidean, TSP, variance and CLT terms. No applicable result was identified from those surname leads. Hits about all feasible tours, heuristics, posterior sampling, or independent random edge weights do not establish the assertion about a geometric optimum. The 2024 feasible-tour CLT and 2026 posterior-concentration hits were screened on this basis.

In particular, exact Gaussianity after standardization by the actual variance would still allow a length-scale sequence proportional to a normal variable to have an oscillating variance. A deterministic normalization plus suitable uniform integrability would be needed to infer a second-moment limit from a CLT.

No located theorem proves the required variance convergence for the binomial square or the Poisson square/torus. Thus `RESOLVED_IN_LITERATURE` is not warranted. Page numbers above are manuscript/PDF pages unless explicitly called printed pages; draft and journal pagination have not been conflated.

## Unconditional partial results

All statements in this section concern true optima. Set T(empty)=T(singleton)=0 and T({x,y})=2d(x,y).

**Proposition 1.** With \(v_n=\operatorname{Var}(T_n)\), the square has \(0\le v_n\le8\), and the flat unit two-torus has \(0\le v_n\le2\). For K=8 or K=2, respectively,

\[
|\sqrt{v_{n+1}}-\sqrt{v_n}|\le\sqrt{K/(n+1)},\qquad
|v_{n+1}-v_n|\le2K/\sqrt{n+1}. \tag{1}
\]

The cluster set of either variance sequence is the closed interval between its liminf and limsup. In the square, the lower endpoint is positive by the known fluctuation lower bound. This does not prove that the interval is a singleton.

*Proof.* Shortcutting and insertion next to a nearest point give, for nonempty finite A,

\[
0\le T(A\cup\{x\})-T(A)\le2d(x,A). \tag{2}
\]

Let R be the nearest Euclidean distance from an independent uniform point to m uniform points, and S its nearest infinity distance. In the square, the intersection of an infinity ball of radius r with the square has side lengths at least r for 0<=r<=1. Hence, conditioning on the inserted point,

\[
\Pr(S>r)\le(1-r^2)^m,\quad
ER^2\le2ES^2\le2\int_0^1(1-u)^mdu=2/(m+1).
\]

On the torus the infinity ball has exactly area 4r^2, 0<=r<=1/2. Thus \(ES^2=1/[4(m+1)]\) and \(ER^2\le1/[2(m+1)]\).

Delete point i and condition on the remaining set A. The original and replacement insertion costs delta, delta' are conditionally iid. Therefore

\[
E(\delta-\delta')^2=2E\operatorname{Var}(\delta\mid A)
\le2E\delta^2\le8ER^2.
\]

Efron–Stein, including its factor 1/2, gives \(v_n\le4nER^2\), proving the bounds. Under the nested coupling, (2) gives \(E(T_{n+1}-T_n)^2\le K/(n+1)\). The reverse triangle inequality on centered L2 norms proves the first inequality of (1); multiplying by \(\sqrt{v_{n+1}}+\sqrt{v_n}\le2\sqrt K\) proves the second.

Boundedness gives convergent subsequences attaining the two endpoints. Every intermediate value is crossed arbitrarily late. At a crossing its distance from a term of the sequence is at most one consecutive step, tending to zero by (1). Thus every intermediate value is a subsequential limit as well.

These facts do not prove convergence: \(a+b\sin(\log n)\), a>b>0, has positive bounded values and smaller consecutive increments but no limit.

## Conditional convergence through block costs

Let \(Q_L=[0,L]^d\), d>=2, with rate-one Poisson input. Let H_L be the global tour cost, using either the cube metric or side-L periodic distance. For a fixed integer r>=1, partition Q_L into side-r cubes and rectangular remainder cells. Let B_{L,r} be the **sum of independent Euclidean TSP costs inside the separate cells**, a disconnected surrogate. Write \(D_xF=F(\mathcal P\cup\{x\})-F(\mathcal P)\).

**Proposition 2.** Assume the following unproved locality estimate for the true TSP:

\[
e_r^2:=\limsup_{L\to\infty}L^{-d}\int_{Q_L}
E|D_xH_L-D_xB_{L,r}|^2dx\longrightarrow0\quad(r\to\infty). \tag{L}
\]

Then the finite limit

\[
\lim_{L\to\infty}\operatorname{Var}(H_L)/L^d
=\lim_{r\to\infty}\operatorname{Var}(T(\mathcal P\cap[0,r]^d))/r^d \tag{3}
\]

exists. Positivity is not asserted by this argument. If (L) holds for both boundary conditions, their Poisson limits coincide.
For the cube, positivity would follow separately from the known binomial lower bound: conditional on its count, unit-cube Poisson input is iid uniform, and total variance is at least the average conditional variance. Counts between n/2 and 2n then give a positive lower bound after multiplication by n^(2/d-1). No analogous unconditional torus lower-bound proof is supplied here.

*Proof.* Poisson restrictions to different cells are independent. If L=kr,

\[
\operatorname{Var}(B_{kr,r})/(kr)^d
=a_r:=\operatorname{Var}(T(\mathcal P\cap[0,r]^d))/r^d. \tag{4}
\]

This is an unconditional, exact variance identity for the surrogate. For arbitrary L, remainder cells have total volume O_d(rL^{d-1}) and diameter at most sqrt(d)r. A cell of volume v<=r^d has cost at most sqrt(d)rN, with N~Poisson(v), so its variance is at most \(dr^2(v^2+v)\le dr^2(r^d+1)v\). Their total variance is o(L^d) for fixed r. Thus (4) holds in the limit along all L.

Poisson Poincaré gives

\[
\operatorname{Var}(H_L-B_{L,r})\le
\int_{Q_L}E|D_xH_L-D_xB_{L,r}|^2dx.
\]

There is no regularity gap in applying it here. At fixed L,r the add-one costs are deterministically bounded by (2). Divide the bounded domain into m independent Poisson cells and apply Efron–Stein replacement. Events with one point in either the old or new restriction give the displayed integral in the mesh limit: their two contributions cancel the factor 1/2. The aggregate contribution of events with at least two old/new points is O(1/m), using bounded increments and Poisson second moments. Coupling removal of a shrinking cell justifies the limit of the bounded integrands. This proves the inequality for the functionals used here.

Consequently the reverse triangle inequality yields

\[
\limsup_L|\sqrt{\operatorname{Var}(H_L)/L^d}-\sqrt{a_r}|\le e_r.
\]

Comparing r,s through the same L gives \(|\sqrt{a_r}-\sqrt{a_s}|\le e_r+e_s\). Thus sqrt(a_r) is Cauchy, and its finite limit proves (3).

Here is a precise sufficient stabilization assumption for (L) in the cube. Suppose a whole-space rate-one Poisson process has an almost surely finite radius R such that the add-one cost at the origin is identical for **every finite completion outside that ball**, after its interior Poisson points are fixed. Translate the condition to x. Global and cell add-one costs then agree whenever x is at distance at least s from the cell boundary and R_x<=s.

The higher moments needed for this implication are available without stabilization. In a side-r cube, assign infinity nearest distance S=r on the empty configuration. For t<r, the ball intersection has volume at least t^d, so

\[
\Pr(S>t)\le e^{-t^d},\qquad
E|D_xT|^p\le(2\sqrt d)^p\Gamma(1+p/d),\quad p>0,
\]

uniformly in r,x. The torus has an analogous bound. Hölder, for p>2, bounds the averaged squared gradient error by

\[
C_{d,p}\{s/r+\Pr(R>s)^{1-2/p}\},
\]

apart from a remainder vanishing with L. The boundary fraction is at most 2ds/r. Choose s=sqrt(r) to obtain (L), without needing an exponential tail. For the periodic global functional one must additionally prove compatibility with the same local add-one cost under periodic completion; Euclidean stabilization is not silently substituted for this boundary-condition assertion.

Since H_L has law L times the unit-domain length at Poisson intensity n=L^d, (3) is convergence of \(n^{2/d-1}\operatorname{Var}(T(\mathcal P_n))\). It is a **conditional Poisson** result, not the fixed-n conjecture.

**Proposition 3: conditional de-Poissonization in the plane.** Let N_n~Poisson(n) be independent of an iid point sequence, and couple T_{N_n} and T_n using it. Suppose \(\operatorname{Var}(T_{N_n})\to\sigma_P^2\) and for a fixed a the centered version of

\[
R_n=T_{N_n}-T_n-a(N_n-n)/\sqrt n
\]

has L2 norm tending to zero. Then \(\operatorname{Var}(T_n)\to\sigma_P^2-a^2\).

*Proof.* Center the identity defining R_n. T_n and N_n are independent, so the variance of the two main terms is v_n+a^2. The error variance and covariances vanish by Cauchy–Schwarz and Proposition 1's bound. Take limits. No required remainder estimate or value of a is established here for TSP.

## Why stabilization does not yet finish the problem

A finite optimal tour can be decomposed into vertex scores equal to half the incident edge lengths. This algebra does not construct an infinite-volume local score or prove independence from distant changes. A nearest-neighbor insertion bound controls the **size** of the cost change, but not its determination by local data. Even short incident edges do not rule out distant changes affecting which local connections the global Hamiltonian cycle selects.

No adequate stabilization radius or substitute L2 estimate for true TSP was located or proved here. This is a missing theorem, not a claim that such a radius cannot exist. The newer localization frameworks also require verifying an actual locality/mixing hypothesis.

Subadditive boundary patching controls errors on the mean scale. In a planar side-L domain, a block patching bound can be O(L^2/r) for fixed r while fluctuations have scale L. It supplies no centered L2 error o(L). Using a boundary functional or torus distance does not establish that estimate. Likewise relative tour error small against sqrt(n) need not be small against constant fluctuations. Poisson count fluctuations also contribute on that scale, so concentration of N_n/n around one is insufficient for de-Poissonization.

## Numerical experiment and validation

The model computed is fixed-n independent uniform points on the flat unit two-torus, with distance

\[
d_{\mathbb T}(x,y)=\left[\sum_{j=1}^2\min\{|x_j-y_j|,1-|x_j-y_j|\}^2\right]^{1/2}.
\]

There is no winding constraint. This variant removes the square's boundary and supplies evidence about a related model; it is not the source's exact setting.

`code/torus_tsp.cpp` implements nearest-neighbor initialization, candidate 2-opt, Or-opt chains of lengths 1–3, and short double-bridge iterated local search. Candidate lists contain 32 periodic nearest neighbors, with 16 used for Or-opt. Each reported length is the better of two independently seeded starts. The main budget is 80 epochs per start, each with max(1,n/50) individually repaired perturbations; 20-epoch checkpoints are recorded. Full local-search sweeps finalize the tours. The stronger calibration uses 320 epochs on matched points. All local moves decrease the current objective; the code makes no global optimality claim.

The predeclared main sample counts are 400, 400, 300, 200, 120 at n=100,300,1000,3000,10000. Points use NumPy PCG64 with seed 300013+1000000*n+index. Solver seeds and frozen code/binary hashes are in `data/run_manifest.json`. `data/torus_samples.csv` contains every main observation; `data/calibration.csv` contains 122 matched comparisons (40,30,24,16,12). Pilot files are retained but excluded from the estimates.

The complete main run contains **1,420 point sets**, including 120 at n=10000. Variances use the unbiased sample variance. Standard errors and percentile intervals below come from 5,000 nonparametric bootstrap resamples of instances; they concern the heuristic distribution only.

| n | samples | mean U/sqrt(n) | sample Var(U) | bootstrap SE | bootstrap 95% interval |
|---:|---:|---:|---:|---:|---:|
| 100 | 400 | 0.716423 | 0.039979 | 0.002773 | [0.034679, 0.045557] |
| 300 | 400 | 0.719173 | 0.040004 | 0.003229 | [0.033954, 0.046495] |
| 1000 | 300 | 0.722513 | 0.034590 | 0.002638 | [0.029438, 0.039821] |
| 3000 | 200 | 0.723330 | 0.033992 | 0.003593 | [0.027144, 0.041083] |
| 10000 | 120 | 0.723463 | 0.034554 | 0.004308 | [0.026297, 0.043058] |

A descriptive constant fit over these five sizes is 0.03693 with sampling SE 0.00141; chi-square 3.87 on 4 degrees of freedom (approximate p=0.42). The slope against log10(n) is -0.00372 with SE 0.00217. Thus the finite-size heuristic data are compatible with a roughly constant variance; they do not identify an asymptotic limit. The normalized mean rises with n, so a size-dependent solver bias remains a practical concern.

The 20-epoch variance checkpoints were 0.04140, 0.04282, 0.03601, 0.03361, 0.04059 in the same size order. Their difference from the 80-epoch values shows that search effort can affect the measured variance.

Matched calibration compares the 80-epoch result with the better of that result and the 320-epoch result. The two columns of variances below use only the smaller matched subsets, not all main samples. Intervals use 10,000 paired bootstrap resamples.

| n | pairs | mean length improvement | SD of improvement | Var at 80 | Var after stronger search | 95% interval for variance change |
|---:|---:|---:|---:|---:|---:|---:|
| 100 | 40 | 0.02222 | 0.02890 | 0.03914 | 0.03938 | [-0.00282, 0.00318] |
| 300 | 30 | 0.04547 | 0.03596 | 0.02546 | 0.02483 | [-0.00504, 0.00392] |
| 1000 | 24 | 0.10102 | 0.05519 | 0.03508 | 0.03638 | [-0.00544, 0.00831] |
| 3000 | 16 | 0.15187 | 0.05859 | 0.03013 | 0.02495 | [-0.01432, 0.00358] |
| 10000 | 12 | 0.35498 | 0.07525 | 0.04988 | 0.04754 | [-0.01541, 0.01144] |

At n=10000 the stronger search still improves lengths by about 0.355 on average (roughly 0.49%). Its mean improvement is several times the point-to-point SD of that improvement. The calibration cannot rule out variance changes of several thousandths. The observed improvement is a lower bound on the baseline's optimization error; the error remaining after the stronger search is unknown.

For the three dual-bound instances at each size, these are the worst relative-gap upper bounds U/lower_bound-1. They bound individual length error, not variance bias:

| n | worst bound at 80 epochs | worst bound after stronger search |
|---:|---:|---:|
| 100 | 1.72% | 1.33% |
| 300 | 3.20% | 2.34% |
| 1000 | 2.29% | 1.65% |
| 3000 | 2.83% | 2.54% |
| 10000 | 3.10% | 2.66% |

The observed n=10000 variance, about 0.0346, is evidence for order-one fluctuations of these near-optimal torus tours. It is not a numerical determination of the square conjecture or of the exact torus variance limit.

Machine-readable results: `data/analysis.json`, `data/variance_summary.csv`, `data/analysis_complete.txt`. Original numerical plot: [variance trend](data/variance_trend.svg). Bootstrap seeds are fixed in `code/analyze.py`. Every main variance was re-derived independently with Python statistics.variance; paired variance differences were checked using their covariance identity.

Heuristic error is assessed in three separate ways. Each reported best tour is independently checked in Python for a permutation of all vertices and a fresh periodic-length sum. An independent exact Held–Karp dynamic program checked 48 small instances: the initial 32 all matched within 9e-16; one of the additional 16 edge cases had a heuristic gap of 0.00711194 (about 0.28%), while the other 15 matched within rounding. The additional edge cases also ran under undefined-behavior sanitization and audited every accepted move. Four n=100 runs audited moves as well. These checks establish implementation consistency, not large-n optimality.

The separate `code/held_karp_bound.cpp` uses complete-graph minimum 1-trees with integer distances rounded downward at scale 10^8, with an extra one-unit downward margin. For any penalties p_i,

\[
\min_{\text{1-trees }G}\sum_{ij\in G}(w_{ij}+p_i+p_j)-2\sum_i p_i
\]

is a lower bound on the rounded TSP optimum: every Hamiltonian cycle is a 1-tree and has degree two at every vertex. Rounded edge costs are below Euclidean costs, so this also bounds the true-metric optimum. The integer dual was checked below all 32 exact test optima. Three 200-iteration bounds per main size provide reported finite-instance gap bounds. Floating distances used for rounding were evaluated in long double with a 10^-8 safety margin; these are numerical lower-bound checks, not interval-arithmetic optimality certificates.

There is also a two-nearest-edge lower bound on every instance. It is usually loose. Search improvements, restart disagreements, and agreement with the empirical BHH constant are diagnostics, not rigorous estimates of the remaining error.

For a heuristic length U=T+E, E>=0,

\[
\operatorname{Var}(U)=\operatorname{Var}(T)+\operatorname{Var}(E)+2\operatorname{Cov}(T,E).
\]

Consequently a small mean relative gap neither bounds the variance bias tightly nor determines its sign. Matched search comparisons use the same point sets and bootstrap pairs; their confidence intervals account for sampling of instances, not unmeasured error relative to true optima. Half the mean squared difference between starts is reported only as a solver-variability diagnostic; it is not subtracted from the measured variance.

## Reproduction, resources and remaining gap

The session launcher and direct getpriority checks give nice 10. Both numerical jobs used one thread each; BLAS, OpenMP and Accelerate thread counts were fixed to one. The main Python peak RSS was 136,855,552 bytes and its solver peak was 5,636,096 bytes. The largest additional array was the 400,000,000-byte complete lower-bound matrix. The design stays well below the 4 GB budget. The main run took 967 seconds of wall time, with 874 seconds summed solver time; calibration ran as a second single-threaded job. There were no search-cap hits and no final feasibility or length-recomputation failures. No subagents, publication, git pushes or external messages were used.

From this directory, in a shell running at nice 10:

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
clang++ -O3 -std=c++17 -Wall -Wextra code/torus_tsp.cpp -o code/torus_tsp
clang++ -O3 -std=c++17 -Wall -Wextra code/held_karp_bound.cpp -o code/held_karp_bound
python3 code/validate.py
python3 code/experiment.py
python3 code/calibrate.py
python3 code/analyze.py
```

The experiment resumes existing main rows; use a different --output name for a fresh sample file. Calibration overwrites its deterministic comparison file. `code/validate_edges.py` reproduces the additional small-instance audit after compiling the sanitizer binary with the command in `LOG.md`. NumPy, SciPy, a C++17 compiler and pdftotext were already installed; no solver package or dependency installation was needed. Source downloads are reproducible with `code/acquire_source.py URL name`; only text is retained.

To turn the conditional route into a solution, one still needs to prove the locality estimate (L) for the true global optimizer and the appropriate fixed-count transfer, or replace them with a direct binomial variance argument. None of the computations supplies those missing estimates.

The source collection contains only plain text. PDF bytes were converted on stdin and never retained as files. Acquisition failures and access limitations are recorded in `LOG.md`. Full proof development, including a second remainder-bound check, is retained in `data/proof_notes.txt`.

Task: “Open problem E0030” — 13 November 2026, approximately 13:01 Asia/Tbilisi (workspace launch clock; exact prompt receipt time unavailable).
