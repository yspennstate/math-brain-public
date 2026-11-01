# PROB10-05 idea checkpoint — replace the saturated degree-18 quasimode by a degree-22 Ritz trial

Runtime request: GPT-6 / maximum. The actual execution environment identifies **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**, so this is not claimed to be GPT-6 maximum.

## Frozen source target and incoming metric

Keep the exact source process and event unchanged:

- centered standard fractional Brownian motion `B_{1/4}`;
- `I(t)=int_0^t B_{1/4}(u) du`;
- continuous one-sided persistence `P{sup_{0<=t<=T} I(t)<=1}=T^{-theta_{2,1/4}+o(1)}`;
- canonical parent claim `operations/claims/MOLCHAN-2025-THETA2H.md`, owner `HARD7-05`.

The strongest current-master complementary checkpoint found before this write is

`proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T0343Z__sharp-probit-1654865.md`,

which gives the repository candidate

`330973/2000000 < theta_{2,1/4} <= 1/4`, width `169027/2000000 = 0.0845135`,

using the already certified comparator `r=7/8`, `s=24861/25000`, cyclic fourth-trace cap `<1.081798`, and the inherited degree-18 quasimode. This supersedes this worker's own earlier `0.165483512` checkpoint and is the incoming baseline.

## Primary new route: higher-degree Ritz residual, not another orthant micro-improvement

The existing Temple proof has three numerical ingredients at the fixed comparator:

1. a Perron-root threshold `x<r^(4 theta_*)`;
2. a fourth-trace cap controlling the non-Perron spectrum;
3. a normalized trial vector with Rayleigh quotient `mu` and residual `eps^2`.

Recent runs concentrated on item 2, shaving the four-cycle trace while keeping the same degree-18 trial. The new route attacks item 3 directly. The degree-18 residual is about `4.7004494e-4`; a materially smaller residual would move the exponent by orders of magnitude more than another `1e-5` trace improvement.

Exploratory Hermite-Galerkin diagonalization of the *same* compact self-adjoint killed transfer operator `K_{7/8,24861/25000}` suggests that degree 22 already supports a polynomial trial with

- Rayleigh quotient about `0.9119014796`,
- residual squared about `2.8549217e-4`,

versus the inherited degree-18 values `mu about 0.9116948312`, `eps^2 about 4.7004494e-4`.

No floating value will enter a theorem. The planned promotion is an integer-coefficient degree-22 polynomial, checked by the same exact Gaussian-moment / outward-rational interval engine already used for the degree-18 certificate. The exact checker must independently verify the norm, `<f,Kf>`, `<Kf,Kf>`, and hence `eps^2`, then perform the spectral-tail/Temple contradiction using only rational inequalities.

Candidate source target to test after exact certification:

`theta_* = 8399/50000 = 0.16798`.

If certified with the already inherited trace cap `<1.081798`, this would give

`8399/50000 < theta_{2,1/4} <= 1/4`, width `4101/50000 = 0.08202`,

a source-metric gain of `0.0024935` over the incoming `0.1654865` candidate.

## Negation test required before promotion

The obvious failure modes are:

- Hermite-to-monomial rounding destroys the numerical residual advantage;
- the degree-22 residual interval is too wide to certify the target;
- the fourth-trace tail forces `beta` so close to `mu` that Temple still fails.

The exact checker must test all three. If any fails, do **not** promote the `0.16798` value.

## Three materially different attacks compared this run

### A. Degree-22 Ritz/Galerkin quasimode — primary

Change the spectral certificate rather than the covariance comparison or four-cycle integral. This is the only route in this run expected to move the source metric substantially.

### B. Equicorrelation coalescence integral — secondary analytic route

For the equicorrelated four-variable endpoint `P_eq(rho)`, Plackett differentiation from `rho` to the coalescent endpoint `1` gives, after `t=cos u`,

`P_eq(rho)=1/2 - 3 alpha/(4 pi) - 3/(2 pi^2) int_0^alpha asin(cos u/(1+2 cos u)) du`,

where `alpha=acos rho`. Differentiation shows the integrand is concave on this short interval, so the trapezoid rule gives a rigorous lower bound on the integral and hence an improved upper bound on `P_eq`. This is analytically distinct from the preceding Mills/probit endpoint route. It is useful as reserve slack but should not displace the Ritz route unless needed.

### C. Reverse continuous interpolation for a new exponent upper bound — obstruction test

A source upper bound on `theta` would require converting sampled negativity back to continuous negativity at only subexponential loss. The current deterministic inclusion works only in the lower-bound direction. At zero barrier the sampled values may lie arbitrarily close to zero, so a uniform bridge survival factor per mesh interval would cost exponentially unless one first proves a repulsion/overshoot estimate under long survival. No such estimate follows from the existing covariance domination. Therefore this route is recorded as a genuine unresolved obstruction, not silently replaced by a discrete persistence claim.

## Promotion criterion

Only after the degree-22 polynomial is certified by exact arithmetic should a substantive report claim any source movement. The current source remains OPEN/PARTIAL; the exact value at `H=1/4` is not determined by this route.