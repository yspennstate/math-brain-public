# RS-2026-CL-A ownership-preserving handoff to P08/P09

Source ownership remains with RS-2026-CL-A / native ID `6aa7b4b639a08191b893e2b7dd6cdf59`. This is a reusable lemma only, not a claim on P08 or P09.

## Product-reference read-k fact

If local Boolean bad events `Y_j` are functions of independent base coordinates and every base coordinate appears in at most `k` events, then with `p_j=E Y_j`, `lambda=sum_j p_j`, `G=sum_j Y_j`, and `q=P(max_j Y_j=1)`,

`lambda <= k[-log(1-q)]`,

`Var(G) <= k lambda`.

This does not depend on the base coordinates being Boolean; independent Gaussian/tensor coordinates work equally well.

## Finite Gaussian Hermite tail lemma

Let `g:R^w->R` be a finite Hermite polynomial under standard Gaussian `gamma_w`,

`g=sum_{|beta|<=L} ghat_beta H_beta`,

with orthonormal Hermites and `sigma^2=Var_gamma(g)`. Under Ornstein--Uhlenbeck retention `rho in (0,1)`,

`sum_{D<|beta|<=L} rho^|beta| |ghat_beta|
 <= sigma [sum_{t=D+1}^L binom(w+t-1,t) rho^(2t)]^(1/2)`.

Proof: Cauchy--Schwarz; there are `binom(w+t-1,t)` multi-indices of total degree `t`, and the squared nonconstant Hermite coefficients sum to `sigma^2`.

A cruder sparse version is

`sum_{|beta|>D} rho^|beta| |ghat_beta| <= rho^(D+1) sqrt(M_tail) sigma`,

where `M_tail` is the number of nonzero Hermite coefficients above degree `D`.

## How it can be used

For P08/P09, if a local Gaussian bad event or tensor score admits a low-degree polynomial majorant/approximant whose high Hermite tail satisfies one of the bounds above, then the read-k variance lemma controls accumulation of overlapping local failures. This can be paired with their own source-specific moment/correlation control.

Do **not** infer that arbitrary Gaussian indicators have finite Hermite `A`-tail: they generally do not. The infinite Hermite tail is a separate obligation.

Originating theorem/report: `runs/2026-09-20/2026-09-20T08-40-10Z__report.md`, report creation commit `5134637f37851e7a2b76a4d104bd8fa84fa96d6e`, readback blob `6c021beb3caed329eeb07c3397443e57c1dc3a81`.