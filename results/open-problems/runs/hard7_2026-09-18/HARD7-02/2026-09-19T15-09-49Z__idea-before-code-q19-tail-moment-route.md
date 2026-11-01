Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run is **not** GPT-6 at verified maximum reasoning. The exposed scheduler/runtime surface still has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration.

# HARD7-02 idea checkpoint before code — Q1.9 reciprocal-edge tail order parameter and subcritical-moment route

Status entering this run: **Campbell–O'Rourke (2022), Question 1.9, ADMITTED_ACTIVE / source OPEN by bounded current-status search.** Frozen metric `T_corr=0` from the admission report. This file records the mathematical ideas before any checker is written.

## Continuity and exact frozen slice

Resume the canonical claim `operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`, not the released Question 1.8 predecessor. Freeze `alpha=1` and

`eta_x = Law(sqrt(x)e^{i phi}, sqrt(1-x)e^{-i phi})`,
`vartheta_x = (eta_x + tau#eta_x)/2`,

at `x=1/4`. The source asks how the tail behavior of `mu_{alpha,theta_d}` varies with `theta_d`; `T_corr` counts only a complete rigorous tail exponent/class for a genuinely correlated non-Hermitian family.

The three new-method moves for this first Q1.9 run are **B2 / B24 / B30**.

## B2 — attack a smooth-interpolation negation first

For one reciprocal marked edge, write

`B(r,w) = [[0, r w_1], [r w_2, 0]]`.

Its eigenvalues satisfy `lambda^2 = r^2 w_1 w_2`, so their common modulus is

`r |w_1 w_2|^(1/2)`.

For `vartheta_x`, `|w_1 w_2|=sqrt(x(1-x))` deterministically. Hence every off-axis `x in (0,1/2]` retains the input Pareto radial exponent on the exact two-cycle object, while the iid axis support has `w_1w_2=0` and this mechanism vanishes. At `x=1/4`, the reciprocal-edge scale is

`kappa = (x(1-x))^(1/4) = (3/16)^(1/4) = 3^(1/4)/2`.

This is deliberately only a counterexample-oriented mechanism. It does **not** infer the limiting ESD tail from a finite `2 x 2` block.

## B24 — extremal angular product / Poisson exceedance intensity

For general angular measure `theta`, define

`K_alpha(theta) = int |w_1 w_2|^(alpha/2) theta(dw)`.

For a Poisson radial mark with intensity `alpha r^(-1-alpha) dr theta(dw)`, the exact mean number of reciprocal-edge block radii exceeding `R` is

`R^(-alpha) K_alpha(theta)`.

Thus `K_alpha` is an exact local tail-order parameter for reciprocal edges. For the frozen slice,

`K_1(vartheta_{1/4})=(3/16)^(1/4)>0`,

whereas it is zero on axis-supported iid dependence. The unresolved global step is to turn a positive density of large reciprocal edges into a lower bound on the planar ESD tail despite nonnormal coupling to the remainder; ordinary eigenvalue perturbation is not stable enough.

## B30 — localize one radial scale by proving all subcritical moments of the limiting ESD

Use the fact that `mu_{alpha,theta}` depends only on `(alpha,theta)` to choose an especially transparent representative of the frozen source class:

- `R` Pareto-1: `P(R>r)=r^(-1)` for `r>=1`;
- `W~vartheta_{1/4}`, independent of `R`;
- `(xi_1,xi_2)=R W`;
- diagonal atom `zeta=0`;
- normalization `a_n=n`.

This representative satisfies C2 and has exactly the required `theta_d=vartheta_{1/4}`. The coordinate marginals are identical. If `Z=|xi_1|^2`, then for `y>=1`, exactly

`P(Z>y)=m y^(-1/2)`,  where  `m=(1+sqrt(3))/4`.

For one normalized row let

`S_n = n^(-2) sum_{j=1}^{n-1} Z_j`.

For `t>=1`, split at `Z_j/n^2=t/2`. The large-jump union bound and a truncated first-moment Markov bound give

`P(S_n>t) <= C_* t^(-1/2)`

uniformly in `n>=2`, with the explicit valid constant

`C_* = 1 + 3 sqrt(2) m = 1 + (3/4)(sqrt(2)+sqrt(6))`.

Indeed the big-jump part is at most `sqrt(2)m t^(-1/2)`, while

`E[Z 1_{Z<=T}] <= 1+2m sqrt(T)`

for `T>=1`, which makes the truncated-sum part at most `t^(-1)+2sqrt(2)m t^(-1/2)`.

Therefore, for every `0<p<1`, with `q=p/2<1/2`, tail integration yields

`E S_n^(p/2) <= B_p := 1 + p C_*/(1-p)`.

Weyl majorization plus the Schatten row bound then gives

`E int |z|^p mu_{A_n}(dz) <= B_p`.

Since `mu_{A_n} => mu_{1,vartheta_{1/4}}` in probability and the limit is deterministic, bounded truncation followed by monotone convergence gives

`int |z|^p mu_{1,vartheta_{1/4}}(dz) <= B_p`  for every `p<1`.

Consequently

`mu_{1,vartheta_{1/4}}({|z|>R}) <= B_p R^(-p)`

for every `p<1`, hence

`liminf_{R->infinity} [-log mu(|z|>R)]/log R >= 1`.

This is a source-relevant theorem if the details survive verification. It does **not** yet determine the tail class, because stretched-exponential decay also satisfies the bound. Thus it is not `T_corr=1` by itself. The remaining direction is a matching lower tail bound, plausibly of order `R^-1`, for which B24 isolates the exact reciprocal-edge mechanism and the nonnormal stability obstruction.
