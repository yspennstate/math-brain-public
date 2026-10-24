Model actually running: **GPT-5.6 Sol. Reasoning/effort level: UNVERIFIED** — the model family is authenticated by the runtime, but no separate authenticated maximum-effort metadata is exposed.

# P26 / LIVE20 T08 — Cartesian multifront Green transfer and a non-Gaussian spectral-expander cutoff class

**Parent status before:** `PARTIAL / OPEN` for Salez Problem 2.3.

**Parent status after:** `PARTIAL / OPEN` for Salez Problem 2.3. The parent conjecture is not claimed solved. The proved restricted scope is strictly enlarged by a new fixed-Cartesian-power transfer theorem and a degree-12 vertex-transitive spectral-but-not-long-range class with an explicit non-Gaussian TV profile.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A--C and the concrete Cartesian-square application below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. A bounded fresh search did not identify a matching theorem phrased as a shell-Green multifront criterion with the explicit order-statistic TV profile below. Cartesian products and product-chain mixing are classical, so no priority claim is made.

Repository/branch: `yspennstate/math-open-problems` / `master`.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`.

Run root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff, preserved failures, and companion split

The latest own substantive report read was

`2026-09-20_16-56-12__hermitian-nbrw-berry-green-transfer.md`.

It proved a quantitative Berry--Green transfer theorem for a single radial front and applied it to degree-32 Hermitianized two-step NBRW edge graphs. It left the general T08 obstruction in the **positive exceptional NBRW sector**. The earlier Ihara/first-repeated-directed-edge tangle route remains incomplete, and the global point-source heat-kernel `L^2` route remains too strong. Those failures are preserved; none is relabeled as solved here.

This run takes a materially different mechanism from the proposed anticommutator-filter attack. Instead of forcing every relevant shell sector to become Green-small at one common radius, it proves that a bounded number of independent entropy fronts may survive simultaneously and that TV is then governed by their **order statistic**. The application is not framework-only: it yields an explicit degree-12 Cayley spectral-expander sequence, proves cutoff with a quantitative window, and proves that its limiting profile is not Gaussian.

The newest relevant historical-C28 successor report read was NM13-01

`2026-09-20T14-15-00Z__schreier-hecke-fiber-cutoff.md`.

NM13-01 now owns the homogeneous-space / Schreier--Hecke / stochastic-fiber route: arbitrary doubly stochastic orbital kicks, exact stabilizer lifts, and pathwise fiber `L^2` contraction. P26 remains complementary: covering-tree shell Green functions, radial fronts, and the present multifront/order-statistic transfer. No NM13-01 fiber theorem is used below.

The root `POSTED.md` exclusion registry was read. In particular, the posted Salez Problem 2.4 Abelian Cayley product-condition manuscript is not reopened.

## 1. Exact source convention and current exact boundary

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), inserts independent mean-one exponential waiting times between transitions. If `P` is the discrete transition matrix, the exact convention is

\[
H_t=e^{t(P-I)}
=e^{-t}\sum_{j\ge0}\frac{t^jP^j}{j!}.
\tag{1.1}
\]

His expander sequences have diverging size, uniformly bounded degree and one-sided spectral gap bounded away from zero, and Problem 2.3 is exactly

> Prove that all vertex-transitive expanders exhibit cutoff.

Fresh source screening on 20 September 2026 leaves that target open.

Dylan J. Altschuler, `arXiv:2609.14945v1` (14 September 2026), proves cutoff with an explicit Gaussian profile for every fixed-degree **long-range expander** sequence. His definition, for `q=d-1`, requires

\[
|B(S,r)|\ge \min\{3n/4,\;c|S|q^r\}
\tag{1.2}
\]

uniformly in sets and radii, and he proves the strict hierarchy

\[
\text{Ramanujan}\Longrightarrow\text{long-range}\Longrightarrow\text{spectral},
\]

with neither converse. Long-range expansion is therefore not synonymous with the hypothesis of Salez Problem 2.3.

Francesco Pedrotti--Justin Salez, `arXiv:2607.05345` (6 July 2026), prove a window theorem using a non-equilibrium Poincare quantity `gamma_*`; the checked statement does not derive the needed bound from vertex transitivity plus an ordinary fixed spectral gap.

The new class below is deliberately outside Altschuler's output hypothesis and, unlike the LRE theorem, has a non-Gaussian limiting profile.

## 2. Parent before/after versus mechanism-level movement

### Parent before

Salez Problem 2.3 was open. P26 could transfer a single Green-small radial shell front, quantitatively, to a Gaussian TV profile.

### Parent after

Salez Problem 2.3 remains open. The strict new restricted scope is:

> For every fixed `k`, a fixed Cartesian power of a transitive shell-Green cutoff sequence has a quantitative **multifront** cutoff. Its limiting TV profile is the survival function of the minimum of `k` independent radial fronts. Applied to Cartesian powers of a nonbipartite degree-six LPS Ramanujan Cayley sequence, this produces bounded-degree vertex-transitive spectral expanders that fail long-range expansion. For `k>=2`, their limiting profile is genuinely non-Gaussian.

For the concrete square `k=2`, the outputs are degree `12`, Cayley, have gap at least

\[
\boxed{\frac{3-\sqrt5}{6}=0.12732200375\ldots,}
\tag{2.1}
\]

fail every fixed positive long-range-expansion constant, and satisfy

\[
\boxed{
d_{\rm TV}\!\left(
\frac32\log_5 N+z\sqrt{\log_5N}
\right)
\longrightarrow
1-\Phi\!\left(\frac{2z}{3\sqrt3}\right)^2.
}
\tag{2.2}
\]

The profile at the entropic center is `3/4`, not `1/2`, and its two Gaussian-tail exponents differ by a factor two. Thus it is not an affine Gaussian survival profile.

### Mechanism-level movement

The reusable advance is that **Green-smallness is only required when every coordinate front has crossed its entropic radius**. The bad event is the union of early fronts. Consequently, the TV profile becomes an order statistic rather than a single Gaussian front. This gives a quantitative theorem and a proved application; it is not an auxiliary constant or receipt.

## 3. Theorem A — exact continuous-time Cartesian factorization

Let `X` be a finite `d`-regular graph with discrete SRW kernel `P`. For fixed `k>=1`, let

\[
Y=X^{\square k}
\]

be the Cartesian power. It is `kd`-regular, and its discrete SRW kernel is

\[
P_Y=\frac1k\sum_{i=1}^k P^{(i)},
\tag{3.1}
\]

where `P^{(i)}` acts as `P` on coordinate `i` and as the identity elsewhere. Therefore

\[
P_Y-I=\frac1k\sum_{i=1}^k(P^{(i)}-I).
\tag{3.2}
\]

The summands commute, so under Salez's exact convention,

\[
\boxed{
H_t^Y
=\bigotimes_{i=1}^k H^X_{t/k}.
}
\tag{3.3}
\]

Thus, from a point start, the `k` coordinates are independent copies of the base continuous-time walk, each run for time `t/k`. This is an exact identity, not a de-Poissonization approximation.

If `X=Cay(Gamma,S)`, then `Y` is the Cayley graph of `Gamma^k` with generators acting in one coordinate, hence is vertex-transitive.

## 4. Theorem B — multifront Green squeeze

Let `(X_n)` be finite transitive regular graphs with uniform stationary laws `pi_n`. Suppose the base exact continuous-time walk admits a shell decomposition

\[
\delta_xH_s
=\sum_{r\ge0}p_{n,s}(r)\nu^x_{n,r}.
\tag{4.1}
\]

Let `R_s` have law `p_{n,s}`. Assume there is an entropic radius `ell_n -> infinity` and error functions `G_n,L_n` such that

\[
\sup_x\sup_{r\ge\ell_n+h}
\chi^2(\nu^x_{n,r}\Vert\pi_n)
\le G_n(h),
\tag{4.2}
\]

and the union of all shell supports up to radius `ell_n-h`, from any fixed start `x`, is contained in a set `A_{n,x}(ell_n-h)` with

\[
\sup_x\pi_n(A_{n,x}(\ell_n-h))\le L_n(h).
\tag{4.3}
\]

Fix `k`. Let `Y_n=X_n^{\square k}` and write `d_{n,k}(t)` for its worst-start TV distance. Put `s=t/k`. Then, for every `h>=0`,

\[
\boxed{
1-\Pr(R_s>\ell_n-h)^k-kL_n(h)
\le d_{n,k}(t)
}
\tag{4.4}
\]

and

\[
\boxed{
d_{n,k}(t)
\le
1-\Pr(R_s\ge\ell_n+h)^k
+\frac12\sqrt{(1+G_n(h))^k-1}.
}
\tag{4.5}
\]

### Proof of the lower bound

Under (3.3), conditional on radial coordinates `(r_1,...,r_k)`, the endpoint shell law is

\[
\nu_{n,r_1}^{x_1}\otimes\cdots\otimes\nu_{n,r_k}^{x_k}.
\tag{4.6}
\]

Let

\[
\mathcal A=
\bigcup_{i=1}^k
\{y:\ y_i\in A_{n,x_i}(\ell_n-h)\}.
\tag{4.7}
\]

If `min_i r_i <= ell_n-h`, the endpoint lies in `mathcal A`. Independence of the radial coordinates gives

\[
\Pr(\min_iR_s^{(i)}\le\ell_n-h)
=1-\Pr(R_s>\ell_n-h)^k.
\tag{4.8}
\]

By the union bound under product stationarity,

\[
\pi_n^{\otimes k}(\mathcal A)\le kL_n(h).
\tag{4.9}
\]

Testing TV on `mathcal A` proves (4.4).

### Proof of the upper bound

For product measures,

\[
\boxed{
1+\chi^2\!\left(\bigotimes_i\mu_i\middle\|\bigotimes_i\pi_i\right)
=\prod_i(1+\chi^2(\mu_i\Vert\pi_i)).
}
\tag{4.10}
\]

Hence, whenever every `r_i>=ell_n+h`, (4.2) gives

\[
\chi^2(\nu_{r_1}\otimes\cdots\otimes\nu_{r_k}\Vert\pi_n^{\otimes k})
\le(1+G_n(h))^k-1.
\tag{4.11}
\]

Using `TV <= (1/2)sqrt(chi^2)` on this good event and the trivial TV bound one on its complement, then averaging the shell mixture, yields

\[
d_{n,k}(t)
\le
\Pr(\min_iR_s^{(i)}<\ell_n+h)
+\frac12\sqrt{(1+G_n(h))^k-1},
\]

which is (4.5). `QED`

The theorem is useful precisely when no single scalar front describes the whole product: the output stays far from equilibrium until the **last** coordinate has crossed the base entropic radius.

## 5. Theorem C — quantitative order-statistic profile

Assume, in addition, that for fixed constants `A,a,b>0`, uniformly for `0<=h<=ell_n/2`,

\[
L_n(h)\le Ae^{-ah},
\qquad
G_n(h)\le A(\ell_n+h+2)^b e^{-ah}.
\tag{5.1}
\]

Suppose the radial front has a quantitative CLT: for every fixed `Z`, uniformly for `|z|<=Z` and `|u|<=C\log\ell_n`, at

\[
s_n(z)=\frac{\ell_n}{v}+z\sqrt{\ell_n},
\tag{5.2}
\]

we have

\[
\Pr(R_{s_n(z)}\ge \ell_n+u)
=
\Phi\!\left(\frac z\tau\right)
+O_Z\!\left(\frac{\log\ell_n}{\sqrt{\ell_n}}\right),
\qquad
\tau^2=\frac{\sigma^2}{v^3}.
\tag{5.3}
\]

Then for fixed `k` and fixed `Z`, at

\[
t_{n,k}(z)
=
\frac{k\ell_n}{v}+kz\sqrt{\ell_n},
\tag{5.4}
\]

we have

\[
\boxed{
\sup_{|z|\le Z}
\left|
d_{n,k}(t_{n,k}(z))
-\left[1-\Phi\!\left(\frac z\tau\right)^k\right]
\right|
\le
C_{Z,k}\frac{\log\ell_n}{\sqrt{\ell_n}}.
}
\tag{5.5}
\]

Consequently, for fixed `epsilon in (0,1)`,

\[
\boxed{
t_{\rm mix}^{(n,k)}(\varepsilon)
=
\frac{k\ell_n}{v}
+k\tau\Phi^{-1}((1-\varepsilon)^{1/k})\sqrt{\ell_n}
+O_{k,\varepsilon}(\log\ell_n).
}
\tag{5.6}
\]

### Proof

Choose `h_n=c_0 log ell_n` with `c_0` large enough that

\[
kL_n(h_n)+\sqrt{(1+G_n(h_n))^k-1}=O(\ell_n^{-2}).
\tag{5.7}
\]

At output time (5.4), each coordinate is at base time `s_n(z)`. Formula (5.3) at thresholds `ell_n +/- h_n` gives

\[
\Pr(R_{s_n(z)}>\ell_n-h_n)
=
\Phi(z/\tau)+O_Z(\log\ell_n/\sqrt{\ell_n})
\tag{5.8}
\]

and the same estimate with `>=ell_n+h_n`. Since `u -> u^k` is `k`-Lipschitz on `[0,1]`, insert (5.8) into the two sides of Theorem B and use (5.7). This proves (5.5). The limiting profile is strictly decreasing, with positive derivative at every fixed quantile, so inversion gives (5.6). `QED`

For `k>=2`, this profile is not an affine Gaussian survival function. Indeed, as `z -> +infinity`,

\[
1-\Phi(z/\tau)^k\sim k(1-\Phi(z/\tau)),
\]

so its logarithmic quadratic right-tail rate is `1/(2 tau^2)`. As `z -> -infinity`,

\[
1-\{1-\Phi(z/\tau)^k\}=\Phi(z/\tau)^k,
\]

whose logarithmic quadratic left-tail rate is `k/(2 tau^2)`. An affine Gaussian survival profile has the same quadratic rate on both tails. The rates differ as soon as `k>1`.

## 6. Base input — degree-six nonbipartite LPS Ramanujan Cayley graphs

Take a suitable nonbipartite degree-six LPS Ramanujan Cayley sequence `(G_n)`; write `n=|V(G_n)|`. Put `q=5` and

\[
\ell_n=\lceil\log_5 n\rceil.
\tag{6.1}
\]

The universal cover is `T_6`. Conditional on lifted radius `r`, the lifted endpoint is uniform on the tree sphere, and projection to `G_n` is exactly the length-`r` NBRW endpoint kernel `K_r`.

Let `p_r` be the normalized NBRW polynomial, so `K_r=p_r(P)`. On the Ramanujan interval

\[
|\lambda|\le \frac{2\sqrt5}{6}=\frac{\sqrt5}{3},
\]

the standard Chebyshev representation gives

\[
|p_r(\lambda)|\le C(r+1)5^{-r/2}.
\tag{6.2}
\]

Vertex transitivity and spectral decomposition yield

\[
\chi^2(K_r(x,\cdot)\Vert\pi)
=\sum_{i=2}^n p_r(\lambda_i)^2
\le Cn(r+1)^2 5^{-r}.
\tag{6.3}
\]

Therefore, for `r>=ell_n+h`,

\[
\boxed{
G_n(h)\le C(\ell_n+h+1)^2 5^{-h}.
}
\tag{6.4}
\]

For early shells, every endpoint lies in the ordinary graph ball of radius `r`, and degree counting gives `|B(x,r)|<=C5^r`. Hence

\[
\boxed{
L_n(h)\le C5^{-h}.
}
\tag{6.5}
\]

The lifted radial chain on `T_6`, away from the root, has one-jump increment

\[
\xi=
\begin{cases}
+1,&5/6,\\
-1,&1/6.
\end{cases}
\tag{6.6}
\]

Thus, under the exact rate-one Poisson clock,

\[
v=\mathbb E\xi=\frac23,
\qquad
\sigma^2=\mathbb E\xi^2=1.
\tag{6.7}
\]

The second identity is the continuous-time variance rate: Poissonization adds the jump-count fluctuation, so it is `E xi^2`, not `Var xi`. The positive drift makes the total root-boundary correction exponentially integrable. The Berry--Esseen argument from the previous P26 quantitative theorem therefore gives (5.3) with

\[
\boxed{\tau^2=\frac{1}{(2/3)^3}=\frac{27}{8}.}
\tag{6.8}
\]

This establishes every hypothesis of Theorem C without invoking long-range expansion for the output graph.

## 7. New application — Cartesian squares of degree-six LPS graphs

Define

\[
\boxed{Y_n=G_n\square G_n.}
\tag{7.1}
\]

Let

\[
N=|V(Y_n)|=n^2.
\tag{7.2}
\]

### 7.1 Vertex transitivity and spectral expansion

Each `Y_n` is a degree-12 Cayley graph on the product group. If `lambda_i` are the normalized eigenvalues of the degree-six base, then the normalized output eigenvalues are

\[
\frac{\lambda_i+\lambda_j}{2}.
\tag{7.3}
\]

Since every nontrivial base eigenvalue is at most `sqrt(5)/3`, the output second eigenvalue obeys

\[
\lambda_2(Y_n)
\le\frac{1+\sqrt5/3}{2}.
\]

Therefore

\[
\boxed{
\operatorname{gap}(Y_n)
\ge
\frac{1-\sqrt5/3}{2}
=
\frac{3-\sqrt5}{6}
>0.1273.
}
\tag{7.4}
\]

Thus `(Y_n)` is a bounded-degree vertex-transitive spectral-expander sequence in the exact sense relevant to Salez Problem 2.3.

### 7.2 Quantitative cutoff and non-Gaussian profile

For `k=2`, Theorem C gives the center

\[
\frac{2\ell_n}{v}=3\log_5 n+O(1)
=\frac32\log_5 N+O(1).
\tag{7.5}
\]

Write the output window in the natural `sqrt(log_5 N)` scale. Since `log_5N=2ell_n+O(1)`, (5.5) becomes

\[
\boxed{
d_{Y_n}\!\left(
\frac32\log_5 N+z\sqrt{\log_5N}
\right)
=
1-\Phi\!\left(\frac{2z}{3\sqrt3}\right)^2
+O_Z\!\left(
\frac{\log\log N}{\sqrt{\log N}}
\right).
}
\tag{7.6}
\]

At the entropic center `z=0`, the limiting TV distance is

\[
1-(1/2)^2=\frac34.
\tag{7.7}
\]

The fixed-accuracy mixing expansion is

\[
\boxed{
t_{\rm mix}^{Y_n}(\varepsilon)
=
\frac32\log_5N
+
\frac{3\sqrt3}{2}
\Phi^{-1}(\sqrt{1-\varepsilon})
\sqrt{\log_5N}
+O_\varepsilon(\log\log N).
}
\tag{7.8}
\]

The profile in (7.6) is genuinely non-Gaussian by the unequal left/right quadratic tail rates proved after Theorem C. This matters conceptually: Altschuler's long-range-expander theorem has the Ramanujan Gaussian profile, whereas ordinary transitive spectral expanders can already exhibit a different limiting shape while still having cutoff.

### 7.3 Direct proof that the outputs are not long-range expanders

Graph distance in a Cartesian product is additive:

\[
\operatorname{dist}_{Y_n}((x_1,x_2),(y_1,y_2))
=
\operatorname{dist}_{G_n}(x_1,y_1)
+
\operatorname{dist}_{G_n}(x_2,y_2).
\tag{7.9}
\]

Degree counting on the degree-six base gives `|B_{G_n}(x,r)|<=C5^r`, so

\[
|B_{Y_n}((x_1,x_2),r)|
\le C'(r+1)5^r.
\tag{7.10}
\]

A degree-12 long-range expander would require singleton growth at the tree branching rate `11^r` until macroscopic saturation. Set

\[
r_N=\left\lfloor\frac12\log_{11}N\right\rfloor.
\tag{7.11}
\]

For any fixed proposed LRE constant `c>0`, the branch `c11^{r_N}` is below `3N/4` for all large `N`, while

\[
\frac{|B_{Y_n}(x,r_N)|}{11^{r_N}}
\le C'(r_N+1)\left(\frac5{11}\right)^{r_N}
\longrightarrow0.
\tag{7.12}
\]

Hence no fixed positive `c` can satisfy the LRE condition. The output class is genuinely **spectral but not long-range**.

This direct growth proof is independent of the non-Gaussian-profile argument and prevents any circular use of Altschuler's theorem.

## 8. Exact checker and sanity checks

The essential checker executed in this run and was archived as

`2026-09-20_17-59-36__cartesian-multifront-green-check.py`

at creation commit

`05b0616234b4376f995ee34ba010ab5e15a91bb6`.

Its executed output was archived as

`2026-09-20_17-59-36__cartesian-multifront-green-check.out`

at creation commit

`d3e3aa33aaecf993518b19adf511c88ed805db3b`.

The checker verifies:

* `v=2/3`, base `tau^2=27/8` and square natural-scale `tau^2=27/4`;
* the exact output gap lower bound `(3-sqrt(5))/6`;
* the tensor chi-square identity (4.10) on an exact rational test;
* the exact continuous-time semigroup tensor factorization numerically on `C_3 square C_3`, with maximum matrix error `3.886e-16`;
* the center value `D_2(0)=3/4`;
* the natural-window scale `3sqrt(3)/2`;
* the strict branching mismatch `5<11`.

The terminal marker is

`P26_T08_CARTESIAN_MULTIFRONT_GREEN_EXACT_PASS`.

These checks are sanity evidence, not an independent audit.

## 9. C28 coordination and what this changes about the obstruction

The latest NM13-01 theorem proves stochastic-fiber cutoff transfer for nonnormal Schreier/Hecke fibers, allowing singular zero-gap cross kernels and strong noncommutation, and gives a canonical lossless stabilizer lift for arbitrary transitive graphs. That route attacks **hidden homogeneous-space coordinates**.

The present P26 theorem attacks a different issue: **several macroscopic Green fronts can coexist without destroying cutoff**. It shows that forcing a single shell Green front is unnecessarily restrictive. The correct limiting object may be the last of finitely many fronts, producing a non-Gaussian order-statistic profile.

This observation feeds directly back into the preserved positive-exceptional-mode obstruction. A bounded positive exceptional sector need not be killed if its components can instead be promoted to finitely many trackable fronts.

## 10. Residual obstruction and next attack

The parent obstruction remains: arbitrary vertex transitivity plus a fixed ordinary spectral gap does not currently supply either a Ramanujan shell Green estimate or a controlled finite collection of positive exceptional fronts.

The next P26 attack is therefore **finite positive-exceptional-front transfer**, not another attempt to annihilate those modes. The target statement is: if the late shell likelihood ratio decomposes into a Green-small residual plus a fixed-rank positive exceptional spectral subspace whose coefficients each have a quantitative one-dimensional crossing law, then total variation is governed by a finite-dimensional front event, with window `O(sqrt(log n))` whenever all crossings occur on that scale. The Cartesian theorem supplies the exact model case and shows why this can succeed even though a single-front criterion fails.

This remains distinct from NM13-01's Hecke-fiber program: P26 will work with shell likelihood ratios and exceptional spectral projectors rather than homogeneous-space stochastic kicks.

## 11. ledger_delta

```json
{
  "owner_track": "P26",
  "parent": "T08 / Salez arXiv:2508.21055 Problem 2.3",
  "parent_before": "PARTIAL / OPEN",
  "parent_after": "PARTIAL / OPEN",
  "source_convention": "H_t = exp(t(P-I)), rate-one Poissonization",
  "mechanism_advance": "fixed-k Cartesian multifront Green squeeze with quantitative order-statistic profile",
  "new_application": "Cartesian squares of nonbipartite degree-6 LPS Ramanujan Cayley graphs",
  "output_degree": 12,
  "output_gap_lower_bound": "(3-sqrt(5))/6",
  "output_size": "N=n^2",
  "cutoff_center": "(3/2) log_5 N + O(1)",
  "profile": "1 - Phi(2z/(3sqrt(3)))^2 on the sqrt(log_5 N) scale",
  "profile_error": "O_Z(log log N / sqrt(log N))",
  "mixing_second_order": "(3sqrt(3)/2) Phi^{-1}(sqrt(1-epsilon)) sqrt(log_5 N)",
  "not_long_range": "ball growth <= C(r+1)5^r versus degree-12 LRE benchmark 11^r",
  "new_dynamic_feature": "non-Gaussian TV profile for a transitive spectral-but-not-LRE expander sequence",
  "failed_routes_preserved": [
    "positive exceptional NBRW modes not generally controlled",
    "Ihara/first-repeat tangle route incomplete",
    "global point-source heat-kernel L2 too strong"
  ],
  "companion_split": "NM13-01 owns Schreier-Hecke stochastic fibers; P26 owns shell Green/radial multifront transfer",
  "checker_commit": "05b0616234b4376f995ee34ba010ab5e15a91bb6",
  "checker_output_commit": "d3e3aa33aaecf993518b19adf511c88ed805db3b",
  "checker_terminal": "P26_T08_CARTESIAN_MULTIFRONT_GREEN_EXACT_PASS",
  "restricted_status": "CANDIDATE_FULL pending later independent review",
  "publication_novelty": "UNVERIFIED",
  "next_attack": "finite positive-exceptional-front spectral-projector transfer"
}
```

End of complete P26 substantive T08 report.
