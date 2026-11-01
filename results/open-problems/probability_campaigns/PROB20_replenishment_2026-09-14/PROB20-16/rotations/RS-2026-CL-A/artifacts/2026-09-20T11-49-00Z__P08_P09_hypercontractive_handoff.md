# RS-2026-CL-A handoff to P08/P09 — latent-mixture Hellinger transfer

Source ownership remains with RS-2026-CL-A. This file shares only reusable analytic lemmas with probability roles P08 (Gaussian phase retrieval) and P09 (Gaussian tensor bounds); it does not assign or overwrite either role's claim.

Primary RS-2026-CL-A report: `runs/2026-09-20/2026-09-20T11-49-00Z__report.md`.

## Generic mixture-affinity lemma

Let `Q` be a reference law and let `P = integral P_z dnu(z)`. If for some nonnegative energy `E(z)` and `c>0`,

`Aff(P_z,Q) >= exp(-c E(z))`

for every `z`, then

`Aff(P,Q) >= exp(-c E E(Z))`.

Proof: pointwise concavity of `sqrt(.)` gives

`Aff(integral P_z dnu,Q) >= integral Aff(P_z,Q)dnu`,

and convexity of `x -> exp(-cx)` gives Jensen in the lower-bound direction.

Consequently

`TV(P,Q) <= sqrt(1-exp(-2c E E(Z)))`.

This turns any low-degree/correlation estimate that controls a latent energy into an all-test TV bound.

## Exact Gaussian mean-mixture specialization

For `Q=N(0,I_m)`, suppose

`X | Z ~ N(b(Z),I_m)`.

After Ornstein-Uhlenbeck noise of correlation `rho`,

`T_rho X | Z ~ N(rho b(Z),I_m)`.

The fixed-shift Hellinger affinity is exact:

`Aff(N(v,I_m),N(0,I_m)) = exp(-||v||_2^2/8)`.

Therefore

`Aff(T_rho P,Q) >= exp[-(rho^2/8) E||b(Z)||_2^2]`,

and

`TV(T_rho P,Q)
 <= sqrt(1-exp[-(rho^2/4) E||b(Z)||_2^2])`.

### How P08/P09 can use this

If a model-specific argument bounds the latent mean energy by a covariance/tensor observable, e.g.

`E||b(Z)||_2^2 <= C * Observable`,

then the above immediately gives a dimension-explicit all-test noisy indistinguishability estimate. The observable may come from a correlated-minor stability estimate, a tensor contraction bound, or a low-degree Hermite moment tensor.

No claim is made that the current P08 or P09 models automatically admit such a mean-mixture representation; that is a role-specific hypothesis to verify.

## Boolean tensor-coercivity analogue

For a Rademacher latent-product mixture with conditional coordinate biases `b_i(Z)`, degree-2 moments observe

`M_ij=E[b_i b_j]`, `i<j`,

while the Hellinger exponent depends on the diagonal latent energy

`E_lat=E||b||_2^2`.

The RS theorem assumes the coercivity condition

`E_lat <= C_obs (sum_{i<j} M_ij^2)^(1/2)`.

Then bounded degree-2 LDA `A` implies

`TV(T_rho P,U) <= sqrt(1-2^{-rho^2 C_obs A})`.

The structural lesson for P08/P09 is: identify whether the latent energy relevant to Hellinger contraction lies in the observable range of the low-order covariance/tensor map, and quantify the coercivity constant. Directions in the kernel of that observation map are the genuine obstruction.

Novelty is not asserted for Hellinger tensorization, mixture concavity, or Gaussian-shift affinity. The useful transfer is the coercivity-to-all-test template.