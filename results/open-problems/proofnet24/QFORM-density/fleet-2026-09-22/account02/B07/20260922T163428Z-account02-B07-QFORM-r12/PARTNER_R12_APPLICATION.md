# Late same-run application of designated partner account03/B07 r12

After the initial REPORT.md was written, the designated partner account03/B07 completed a newer QFORM run. I read the complete immutable source:

`yspennstate/math-open-problems@685929d9daee92a164dbf6ba6f9305d2e6550826`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T163733Z-account03-B07-qform-r12/REPORT.md`.

Its theorem `QFORM-THIRD-COMPOUND-OVERLAP-REDUCTION-v1` is a full-matrix strengthening of the packet input used in the initial report. Since

`||wedge^3 A||_HS^2=sum_{i<j<k}lambda_i^2 lambda_j^2 lambda_k^2>=1`,

one of four overlap classes has mass at least `1/4`. In its O0 alternative, a random original-coordinate bipartition produces a cross block `B=A[L,R]` with

`E:=e_3(BB^T)>=1/256`.

The partner pays O0 when, at effective ridge dimension `theta=8/3`, every row ridge leverage is at most `1/2`, obtaining a continuous-density bound `<19.54`; otherwise it returns a ridge-DPP heavy row of inclusion marginal `>1/2`.

The new theorem of this B07 run, `QFORM-Q0-RIDGE-FOUR-HEAVY-DPP-v1`, applies directly to the partner's same O0 cross block and sharpens the residual. Normalize instead at effective dimension `theta=3` (or use the `gamma downarrow0` rank-three limit). If

`max_i K_ii<=3/5`,

the ridge theorem with `q=6/5` gives

`||p_Q||_infinity
 <= 5e sqrt(5/12) E^(-1/6)
 <= 5e sqrt(5/12) 256^(1/6)
 = 22.107121236243...`.

If this gate fails, define

`H={i:K_ii>3/5}`.

The determinant L-ensemble identity proved in REPORT.md gives `P(i in S)=K_ii` and `E|S|=tr K=3`. Hence

`(3/5)|H|<3`,

so

`|H|<=4`.

Thus the partner's full-target O0 alternative is now reduced as follows:

1. if its earlier `theta=8/3`, `1/2`-leverage gate fires, use the partner's `<19.54` bound;
2. otherwise move to effective dimension three; if all row marginals are at most `3/5`, use the new `<22.108` bound;
3. otherwise the entire unpaid O0 obstruction contains a dimension-free set of at most four original coordinates, each carrying more than `3/5` of the effective-dimension-three regularized determinant inclusion weight.

This is a strict application of the newest designated-partner result: it removes the partner's unstructured single-heavy-row O0 residual and replaces it by a bounded four-coordinate determinant core. The full QFORM theorem remains open because this four-heavy O0 core and the partner's O1/O2/O3 aggregate branches still require product-preserving analytic payment.

Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`. No full-proof claim.
