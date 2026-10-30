# Fresh-partner addendum — conditioned-whitened closure

After the main report was written, the assigned partner `fleet04/B20` published a fresher completed result:

`yspennstate/math-open-problems@94bf446b8547b1124a37033e940ef594c460b64f:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260922T141640Z-fleet04-B20-QFORM-r2/REPORT.md`.

Its theorem conditions a set `H` of ORIGINAL coordinates in a full-range spectral factorization `A=U Lambda U^T`. With `R=H^c` and

`S=U_R^T U_R=I-U_H^TU_H`, `delta=lambda_min(S)>0`,

if

`max_{i in R} u_i^T S^(-1) u_i <=1/32`,

then the target quadratic law has a **continuous** density with

`||p_Q||infinity <= 96e/(7 sqrt(2) delta)<27/delta`.

This result is compatible with, and strengthens, the localization split in the main B20 report. Here is an explicit application rather than a citation-only use.

Take a single original coordinate `i` as `H={i}` and let `h_i=||u_i||^2` be its leverage in the ENTIRE range frame. Then

`S=I-u_i u_i^T`,

so its eigenvalues are `1` off the span of `u_i` and `1-h_i` on that span. Hence

`delta=1-h_i`.

If

`h_i<=1/2`

and every remaining raw row leverage satisfies

`max_{j!=i} ||u_j||^2 <= (1-h_i)/32`,

then the partner's raw sufficient condition is satisfied and

`boxed: ||p_Q||infinity <= 96e/[7 sqrt(2)(1-h_i)] <= 192e/(7sqrt(2)) <54.`

Thus a moderate full-range heavy row can be conditioned away at a universal cost whenever the residual whitened frame becomes diffuse. This closes an additional branch of the main report's `Schur-range localization` alternative with a continuous density, without invoking a scalar Schur pivot at all.

Consequently the still-unpaid localization branch is sharper: after conditioning any candidate finite heavy set, either the residual spectral Gram floor `delta` tends to zero (the set nearly exhausts a spectral direction), or a residual whitened leverage remains above `1/32`. The hard saddle family in the partner report realizes the `delta=0` obstruction and is instead closed by the aggregate hyperbolic-square mechanism.

Full QFORM remains OPEN. This addendum changes no earlier theorem and makes no new continuity claim outside the partner-conditioned branch.
