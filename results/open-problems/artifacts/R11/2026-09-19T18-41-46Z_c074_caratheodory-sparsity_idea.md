# R11 idea-before-code: sharp translation-support compression for I0054

Date: 2026-09-19 UTC.

Continue from U052/C073. Use the prescribed nonrepeating methods **#5, #20, #30**.

## #5 ADD A PARAMETER AND DIFFERENTIATE IN IT

Parameterize the number `L_N` of active translation families rather than fixing `L_N=p_N^(3/4)`. The equal-weight interval proof of C073 needs `L_N >> sqrt(p_N)` only because incomplete exponential-sum completion costs `sqrt(p_N)`. Ask for the true support threshold when the surviving translations are allowed unequal positive clock weights.

## #20 FIND WHY THE ALGORITHM FAILS

A single translation family induces a total order of a visible `k`-block. Sweeping the threshold can realize only the `k-1` cuts between consecutive ranks. With `L` active translations, at most `L(k-1)` of the `2^(k-1)-1` unordered specified root splits can have positive rate. Hence bounded `L` cannot converge to CTCS on every fixed restriction: choose fixed `k` with `2^(k-1)-1 > L(k-1)`.

This identifies the real obstruction: support must diverge. It does **not** suggest any positive-power threshold.

## #30 ONE SCALE / ONE DIRECTION AT A TIME

For a finite visible cutoff `K`, collect into one vector all split rates for every non-singleton subset of `[K]`. The number of coordinates is

`D_K = sum_{m=2}^K binom(K,m)(2^(m-1)-1) = (3^K-2^(K+1)+1)/2`.

For the full-translation C072 model, this generator vector is the uniform average of the `p_N` per-translation generator vectors. By finite-dimensional Caratheodory, the same vector is an **exact** convex combination of at most `D_K+1` translation vectors. Because all entries are rational, a rational basic feasible representation exists.

Therefore, given any prescribed integer budget `L_N -> infinity`, let `K_N` be the largest integer with `K_N <= min(N,d_N-1)` and `D_{K_N}+1 <= L_N`. Then `K_N -> infinity`, and one can choose at most `L_N` translations with positive rational weights whose complete `[K_N]` generator is **exactly** the C072 generator. For each fixed `k`, eventually `k <= K_N`, so the entire `[k]` path law equals C072's and hence converges to CTCS(infinity).

This would prove a sharp support statement inside the threshold-translation architecture:

- any `L_N -> infinity`, however slowly, is sufficient;
- bounded `L_N` is impossible.

Thus the `alpha=1/2` barrier from interval completion is an equal-weight interval artifact; the true support-growth threshold is simply divergence.

Concrete candidate C074: take `L_N=max(7,ceil(log log(N+e^e)))`, choose the lexicographically first rational basic feasible Caratheodory representation on `[K_N]`, and use clock rate `p_N lambda_t/[2u(p_N-u)]` for active translation `t` and threshold `u`. At `N=4`, use the explicit exact representation on `p=5,d=3,K=3` with translations `(0,1,3,4)` and weights `(4/15,1/3,4/15,2/15)`; this matches the full-orbit generator on every subset of the first three labels but has a visibly anisotropic four-label root generator, giving a finite non-equivalence witness without affecting the limit.
