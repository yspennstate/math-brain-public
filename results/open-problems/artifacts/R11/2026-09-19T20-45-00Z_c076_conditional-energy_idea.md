# R11 / I0054 — idea before code: conditional-energy derandomization

Methods for this run: **#10 DERANDOMIZE, #21 ASK WHO ELSE HAS THIS SHAPE, #24 FIND THE EXTREMAL OBJECT**.  This note is intentionally written before any new checker.

Starting point is U054/C075: equal-weight sparse translation support can be chosen by a probabilistic existence argument, but the canonical construction uses lexicographic exhaustive search and the simultaneous union bound sees `D_K ~ 3^K/2` generator coordinates.

## New route

For a cutoff `K`, let `g_t` be the vector of all specified unordered split contributions of translation `t` on every visible subset of `[K]`, with the same `p/[2u(p-u)]` threshold rescaling as U054.  Let `mu=(1/p) sum_t g_t` and `z_t=g_t-mu`.

The key observation is that the **total l2 energy of this entire vector is only order `K 2^K`, not `3^K`**.  For a visible subset `V` of size `m`, sort its threshold ranks as `x_1<...<x_m` and put `y_r=L_p(x_r)`, where `L_p(x)=H_x-H_{p-1-x}`.  Exactly the `m-1` consecutive-rank cuts can be produced by this translation, and their contributions are `(y_{r+1}-y_r)/2`.  Hence

`sum_{cuts of V} g_t(c)^2 = (1/4) sum_{r=1}^{m-1}(y_{r+1}-y_r)^2 <= sum_{v in V} L_p(phi(t+v))^2`.

Averaging in `t` and using U054's `M_p=(1/p) sum_x L_p(x)^2 < 8` gives

`(1/p) sum_t ||g_t||_2^2 < 8 sum_{m=2}^K m binom(K,m) = 8K(2^{K-1}-1)`.

Therefore the centered energy obeys the same bound.

Now choose an equal-weight `L`-subset **deterministically by conditional expectation**, not exhaustive search.  For a partial selected set `A` of size `r`, let `R` be the remaining translations, `n=|R|`, `s=L-r`, `S_A=sum_{t in A} z_t`, and `Q_R=sum_{t in R} ||z_t||^2`.  If the completion is a uniform `s`-subset of `R`, the exact conditional expected final squared error is

`F(A)=((n-s)(n-s-1)/(n(n-1))) ||S_A||^2 + (s(n-s)/(n(n-1))) Q_R`

(with the obvious terminal conventions).  At each step choose the least translation minimizing `F(A union {t})`.  By the tower property, `F` never increases.  At termination,

`||(1/L) sum_{t in S} g_t - mu||_2^2 <= ((p-L)/(L(p-1))) * (1/p)sum_t ||z_t||^2 < 8K(2^{K-1}-1)/L`.

Thus every coordinate has error at most

`sqrt(8K(2^{K-1}-1)/L)`.

This is an explicit polynomial-time equal-weight sampler (polynomial in `p`, `L` and the number of represented coordinates), and improves the previous `3^K` union-bound energy scale to `K 2^K`.

## Extremal lower bound to compare

A single translation can give positive rate to at most `K-1` of the `2^{K-1}-1` nontrivial unordered splits of the full visible set `[K]`.  Therefore any support that makes **every** full-`K` CTCS split positive must satisfy

`L >= ceil((2^{K-1}-1)/(K-1))`.

Equivalently, for uniform additive error smaller than the minimum CTCS full-`K` split rate

`b_K = 1/((K-1) max_j binom(K-2,j))`,

the same lower bound is necessary.  So the constructive upper scale `O(K 2^K / eps^2)` and the positivity lower scale `Omega(2^K/K)` both have exponential base 2; the old base-3 coordinate count is not intrinsic.

## Candidate C076

Use the same growing-power ambient model as C072 and an equal-weight budget `B_N -> infinity`, but select the support by the conditional-energy algorithm above.  A concrete choice can keep `B_N=max(3,ceil(log_2 log_2(N+4)))`.  Choose `K_N` so that `8K_N(2^{K_N-1}-1) <= B_N^{1/2}` (and at least `K_N=2` at finitely many small N by convention).  Then the generator error is `O(B_N^{-1/4})` on every represented coordinate and `K_N -> infinity`, so each fixed restriction should converge in path total variation by the existing finite-state uniformization argument.

At `N=4`, `p=5,d=3,L=3`, exact conditional expectation should be checked.  Preliminary hand calculation suggests the selected set may differ from C075's `{0,1}`; the exact rate array will be used only after a checker confirms it.

No novelty is claimed for method of conditional expectations, approximate Caratheodory, or deterministic convex approximation.  The candidate new content is the CTCS split-vector energy collapse from `~3^K` coordinates to `O(K2^K)` and its use for an explicit equal-weight CTCS compiler.