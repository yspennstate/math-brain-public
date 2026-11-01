# QFORM B17 — rotated infinitesimal-frame Gaussian-floor theorem

Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`.

Classification: **AUXILIARY_ONLY / ROTATED_INFINITESIMAL_LIMIT_NO_ESCAPE**. The full arbitrary-product finite-dimensional QFORM conjecture remains **OPEN / NOT PROVED**. Continuity for the full conjecture also remains open.

## Source pins actually used

1. Designated partner `fleet02/B17`, theorem `GENERAL_INFINITESIMAL_BANK_LIMIT_NO_ESCAPE`, canonical mathematics `yspennstate/math-open-problems@9ef2d4cbf56e1aa3368eeaa322d09ba4d91f31cf`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260922T154450Z-fleet02-B17-QFORM-r11b/REPORT.md`. The scalar input needed below is: for every convergent infinitesimal scalar triangular array
   
   `Z_mk = a_mk X_mk - c_mk`, `sum_k a_mk^2 = 1`, `max_k |a_mk| -> 0`,
   
   with independent inputs of density at most one, the Levy--Khintchine Gaussian variance of every weak limit is at least `1/12`.
2. `QFORM-GAUSSIAN-FULL-NONCENTRAL-C3SQRT2-v1`, source `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/20260922T120821Z-fleet01-B17-qform-sharp-constant-v1/ADDENDUM_NONCENTRAL_GAUSSIAN.md`: if `G~N(m,Sigma)`, `Sigma >= sigma^2 I`, and the symmetric quadratic matrix has at least three eigenvalues of magnitude at least one, then the quadratic-form density is bounded and continuous with norm at most `1/(2 sqrt(2) sigma^2)`.
3. Live correction inbox through control snapshot `math-research-brain@fc1ce39df9220d4c90d43d68cf668e7f3f28f4f5` was checked. No pointwise oscillatory-decay, post-rotation independence, single-minor, conditional-cap, fixed-fragment-count, fiberwise-trace, or phase-Wiener premise is used.

## Theorem: multivariate rotated infinitesimal frames inherit the `1/12` Gaussian floor

Fix a finite dimension `d >= 3`. For each row `m`, let `r_mk in R^d`, `1 <= k <= n_m`, satisfy the exact tight-frame identity

`sum_k r_mk r_mk^T = I_d`

and the infinitesimal leverage condition

`max_k ||r_mk||_2 -> 0`.

Let `X_mk` be independent real random variables, each possessing a probability density bounded by one. Let `c_mk in R^d` be deterministic, and suppose the vector triangular array

`Z_mk = r_mk X_mk - c_mk`

is infinitesimal and its row sums converge in law,

`sum_k Z_mk => Y in R^d`.

Write `Gamma` for the Gaussian covariance matrix in the Levy--Khintchine decomposition of the infinitely divisible limit `Y`. Then

`Gamma >= (1/12) I_d`.

### Proof

Fix an arbitrary unit vector `u in R^d`. Project the whole triangular array onto `u`:

`u^T Z_mk = a_mk X_mk - d_mk`,

where `a_mk = u^T r_mk` and `d_mk = u^T c_mk`.

The tight-frame identity gives exactly

`sum_k a_mk^2 = u^T (sum_k r_mk r_mk^T) u = 1`.

Moreover

`max_k |a_mk| <= max_k ||r_mk||_2 -> 0`.

Vector infinitesimality implies scalar infinitesimality after applying the continuous linear map `z -> u^T z`, and the continuous mapping theorem gives

`sum_k (u^T Z_mk) => u^T Y`.

Therefore the completed designated-partner scalar theorem applies **verbatim** to this projected array. It says that the Levy--Khintchine Gaussian variance of `u^T Y` is at least `1/12`.

If `Gamma` is the Gaussian covariance matrix of `Y`, the Gaussian variance of the scalar projection `u^T Y` is exactly `u^T Gamma u`. Hence

`u^T Gamma u >= 1/12`

for every unit vector `u`. By the quadratic-form characterization of Loewner order,

`Gamma >= (1/12) I_d`.

This proves the theorem. QED.

## Quadratic-form consequence: arbitrary rotated infinitesimal limits cannot beat `3 sqrt(2)`

Let `B` be any fixed real symmetric `d x d` matrix with at least three eigenvalues of magnitude at least one. Every infinitely divisible `Y` above has a Levy--Khintchine decomposition

`Y = b + G + R`,

where `G~N(0,Gamma)`, `Gamma >= I_d/12`, and `G` is independent of the pure-jump residual `R`.

Condition on `R=r`. Then `b+G+r` is Gaussian with arbitrary mean `b+r` and covariance `Gamma >= I_d/12`. Applying `QFORM-GAUSSIAN-FULL-NONCENTRAL-C3SQRT2-v1` with `sigma^2=1/12` gives

`|| p_{(b+G+r)^T B (b+G+r)} ||_infinity <= 3 sqrt(2)`

for every `r`.

The unconditional density is the mixture of these conditional densities, so

`p_Q(y) = E[p_{Q|R}(y)]`

and therefore

`||p_Q||_infinity <= E ||p_{Q|R}||_infinity <= 3 sqrt(2)`.

Each conditional density has a continuous representative and is bounded by the same integrable constant `3 sqrt(2)`; dominated convergence in `r` shows the mixture also has a bounded continuous representative. Thus

**`||p_{Y^T B Y}||_infinity <= 3 sqrt(2)`**, with continuity for this limiting class.

## Exact target-admissible rotated-frame corollary

Let `R_m` be the `n_m x d` matrix whose rows are `r_mk^T`, so `R_m^T R_m=I_d`. For a fixed symmetric `B`, define the physical matrix

`A_m = R_m B R_m^T`.

The nonzero eigenvalues of `A_m` are exactly the eigenvalues of `B`: indeed `R_m` is an isometry from `R^d` into `R^{n_m}`, and `A_m` restricted to `range(R_m)` is unitarily equivalent to `B`. In particular, if `B=diag(1,1,-1)` then every finite `A_m` has nonzero spectrum exactly `{1,1,-1}` and is an exact instance of the owner's three-large-eigenvalue hypothesis.

For independent cap-one physical inputs `X_m=(X_m1,...,X_mn_m)`, the physical quadratic form is exactly

`X_m^T A_m X_m = (R_m^T X_m)^T B (R_m^T X_m)`.

Hence any convergent **infinitesimal** rotated tight-frame projection limit falls under the theorem above and has limiting quadratic density at most `3 sqrt(2)`.

This closes a mechanism left explicitly open by the designated partner: shared-coordinate loading across several active spectral directions is not an escape if the physical row leverage is infinitesimal and a weak limit exists. The scalar disjoint-bank theorem is recovered by taking the frame rows axis-aligned.

## Concrete genuinely rotated rare-fragment family

Take `d=3`, `B=J=diag(1,1,-1)`, and the orthonormal rotated directions

`v1=(1,0,1)/sqrt(2)`, `v2=(0,1,0)`, `v3=(1,0,-1)/sqrt(2)`.

Repeat each `vj` in a bank of `m` physical rows as `vj/sqrt(m)`. Then the resulting `R_m` satisfies `R_m^T R_m=I_3`, so `A_m=R_m J R_m^T` has exact nonzero spectrum `{1,1,-1}` for every `m`.

Give a physical coordinate in the first bank a density-one support consisting of a central interval of length `1-alpha/m` and rare intervals of total length `alpha/m` centered at locations `b_r sqrt(m)`, while the other banks use the centered unit interval. The first-bank characteristic exponent in a test direction `xi` has the standard expansion

`m log psi_m(xi) -> -(xi.v1)^2/24 + sum_r alpha_r (exp(i b_r xi.v1)-1)`.

The other two banks contribute `-(xi.v2)^2/24` and `-(xi.v3)^2/24`. Since `sum_j vj vj^T=I_3`, the full projected limit is

`Y = G + W`, `G~N(0,I_3/12)`,

where `W` is a compound-Poisson shift along the **cross-sign rotated direction** `v1`; `G` and `W` are independent. Therefore

`||p_{Y^T J Y}||_infinity <= 3 sqrt(2)`.

No axis alignment, coordinatewise independence after rotation, or diagonalization of the physical product law is being assumed.

More generally, the same conditional inequality shows that **any** independent residual shift `W` added to a Gaussian floor `G~N(0,Gamma)`, `Gamma>=I/12`, satisfies the same `3 sqrt(2)` ceiling. Thus a growing fragment alphabet, an infinite-activity jump limit, or an arbitrary rotated jump law cannot raise the limiting peak as long as an independent isotropic Gaussian floor survives.

## Direct application to the designated partner result

The designated partner proves that each of three disjoint infinitesimal banks has a limiting decomposition

`Y_j = G_j + R_j`, `G_j iid N(0,1/12)`.

Taking `d=3`, `Gamma=I_3/12`, `B=diag(1,1,-1)` in the mixture inequality above gives immediately

`||p_{Y_1^2+Y_2^2-Y_3^2}||_infinity <= 3 sqrt(2)`.

The present argument is strictly more structural: instead of three axis-aligned scalar banks it applies the partner theorem to **every one-dimensional projection** of an arbitrary tight-frame array and reconstructs the matrix inequality `Gamma>=I/12`.

## What remains unpaid

This is a limiting theorem, not a finite-row local limit theorem. Weak convergence alone does not exclude narrow finite-`m` density spikes. It also does not cover non-infinitesimal/mixed-leverage rows. Therefore a witness above `3 sqrt(2)`, if one exists, must now exploit at least one of:

- a non-infinitesimal or mixed-leverage physical row that survives in the limit;
- finite-row local-density spikes invisible to weak convergence;
- failure of a useful convergent projected limit.

In particular, **shared-coordinate rotation by itself is no longer an escape mechanism in the infinitesimal regime**.

This does not prove the full QFORM conjecture and does not establish that the sharp universal constant equals `3 sqrt(2)`.
