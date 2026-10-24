Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **No movement at entry: `T_corr=4 -> 4`. Methods selected: B10/B13/B21, different from the preceding B5/B11/B30 triple.**

# HARD7-02 idea checkpoint before code — Q1.9 Pareto envelope from row-rank truncation

The latest Q1.9 report left as its main obstruction quantitative control of the near-critical moments `M_p(theta)` as `p up alpha`. Re-reading the earlier positive-off-axis proof shows that this control was already present but not exploited quantitatively: with `beta=alpha/2` and

`C_beta = 2 + 2^beta + 2^beta/(1-beta)`,

the finite-matrix row argument proved, uniformly in `n` and in the C2 angular law after probability normalization,

`int |z|^p mu_{alpha,theta}(dz) <= 1 + p C_beta/(alpha-p)`, `0<p<alpha`.

Rather than run the previous Tauberian annulus argument with a scale-dependent `p`, the new route attacks the loss at its source. The moment estimate came from a stronger row-norm tail bound

`P(||Row_i(A_n)||_2 > t) <= C_beta t^(-alpha)`, `t>=1`.

A deterministic rank/Frobenius truncation should transfer this weak-`L^alpha` row envelope directly to the singular-value counting function, avoiding the logarithm introduced by optimizing Markov over `p`:

1. For threshold `t`, split `A=B+C`, where `B` retains exactly the rows with norm `>t` and `C` the remaining rows. Then `rank(B)` is the number of large rows.
2. Rank perturbation gives `N_s(A,t) <= rank(B)+N_s(C,t)`.
3. Frobenius gives `N_s(C,t) <= ||C||_F^2/t^2`.
4. Taking expectations and using the row-tail bound plus truncated-tail integration should yield

`sup_n E[N_s(A_n,t)/n] <= D_alpha t^(-alpha)`, `t>=1`,

for an explicit `D_alpha<infinity`.
5. Weyl logarithmic majorization gives

`V_n(u):=n^(-1)sum_j log^+(|lambda_j|/u) <= n^(-1)sum_j log^+(s_j/u)`
`= int_u^infinity [N_s(A_n,t)/n] dt/t`.

Hence the limiting radial logarithmic potential should satisfy a **matching upper power envelope**

`V_theta(u) <= (D_alpha/alpha)u^(-alpha)`.

The earlier isolated-reciprocal-edge argument already gives, whenever `rho_off(theta)>0`, a matching lower envelope

`V_theta(r) >= A_theta r^(-alpha)`

for all sufficiently large `r`, with an explicit sector-dependent `A_theta>0`. Now choose a fixed multiplicative dilation `K>1` so that the upper bound at `Kr` is at most half the lower signal at `r`. Since

`V(r) <= F(r) log K + V(Kr)`,

this would give

`F_theta(r) >= c_theta r^(-alpha)`.

The potential upper bound also gives directly

`F_theta(r) <= V_theta(r/e) <= C_alpha r^(-alpha)`.

Thus the intended theorem is the two-sided **Pareto envelope**

`c_theta r^(-alpha) <= mu_{alpha,theta}({|z|>r}) <= C_alpha r^(-alpha)`

for every C2 angular law with positive off-axis mass. This is strictly stronger than the previous logarithmic exponent and `r^alpha log r F(r)->infinity`; it still does not assert existence of a regular-variation constant.

Two further consequences would become immediate and source-relevant:

- critical truncated moment `Q_alpha(R)=Theta(log R)`;
- near-critical moment blow-up `int |z|^p dmu = Theta((alpha-p)^(-1))` as `p up alpha` (with explicit liminf/limsup constants), closing the exact obstruction named in the previous report.

### Section-B route

- **B10 DERANDOMIZE.** Replace the arbitrary positive-mass sector `{|w_1w_2|>=delta}` by the deterministic angular functional `J_alpha(theta)=sup_delta delta^(alpha/2) theta(|w_1w_2|>=delta)` when recording an explicit lower constant.
- **B13 FIND WHAT ONLY INCREASES.** Use monotonicity of the radial tail/potential under moving the threshold and the monotone singular-value counting function to transfer a fixed-dilation potential gap to a pointwise tail gap without a logarithmic annulus loss.
- **B21 ASK WHO ELSE HAS THIS SHAPE.** Recast the row estimate as a weak-`L^alpha` / weak-Schatten counting problem. The rank-plus-truncated-Frobenius decomposition is the finite-dimensional mechanism that preserves the power exponent at the singular-value level.

### Counterexample-first stress test

The latest theorem still allowed `F(r)=r^(-alpha)/sqrt(log log r)`. The proposed singular-value upper estimate does not rule that out from above, but the fixed-dilation transfer rules out every `o(r^(-alpha))` tail from below. Therefore, if the derivation succeeds, all positive-off-axis laws have the same radial power **class up to multiplicative constants**, even though exact constants and directional tails can still vary with `theta`.

No checker has been written yet. The next step is to prove every deterministic inequality on-page, then use a small exact symbolic self-check only for the constant algebra if warranted.