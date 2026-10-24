SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-23T07:30:06Z.
attacking: the pair-conditional-diffuse anchored-third-volume survivor by retaining the fixed anchor row/column through the decoupled integral, rather than discarding their product provenance.

# Early substantive checkpoint

Full QFORM remains OPEN. This checkpoint records a new analytic calculation before the final proof is expanded.

Let R be an arbitrary quadratic-plus-affine polynomial in independent original coordinates with cap-one densities. After conditioning outside two disjoint physical banks, write its cross block as

M = [[a, r^T],[c,N]],  a != 0,

with fixed physical row h and column k. Put S=N-c r^T/a. Define the anchored third-volume

W = sum_{|P|=|T|=2} det M[{h} U P,{k} U T]^2 = a^2 E2(S).

Let the natural squared-2-minor law of S have row inclusion marginals gamma_i. If max gamma_i <= 1/2, then the following calculation gives a dimension-free half-Riesz estimate despite arbitrary same-bank quadratic curvature.

After Weyl differencing across the column bank,

|phi_R(t)|^2 <= I(t) := int prod_i |psi_i(2t(Mz)_i)| prod_j g_j(z_j) dz,

where g_j=f_j*tilde f_j are independent probability densities with cap <=1. Change the anchor-column variable to

y = a z_k + r.z_0.

Then

I(t)=|a|^{-1} int |psi_h(2ty)| H_t(y) dy,

where the residual row arguments are S z_0 +(c/a)y and the anchor-difference density remains inside H_t. Two bounds are immediate and compatible:

(1) ||H_t||_1 <= |a|, retaining the anchor difference density rather than dropping it.

(2) ||H_t||_infty <= 4 e pi^2 |t|^{-2} E2(S)^{-1/2}
    = 4 e pi^2 |a| |t|^{-2} W^{-1/2}.

For (2), fix y, drop only the cap-one anchor density, and apply the order-two determinant-weight Brascamp-Lieb estimate to S. The shifts (c_i/a)y do not affect the BL constant. The row gate gamma_i<=1/2 is exactly the Fourier L^p endpoint needed here; no post-rotation independence is used.

Interpolation gives

||H_t||_2 <= 2 sqrt(e) pi |a| |t|^{-1} W^{-1/4}.

Plancherel for the actual original anchor coordinate gives

||psi_h(2t .)||_2 <= sqrt(pi/|t|).

Therefore the anchor edge cancels exactly:

|phi_R(t)|^2 <= 2 sqrt(e) pi^(3/2) |t|^{-3/2} W^{-1/4},

hence

|phi_R(t)| <= sqrt(2) e^(1/4) pi^(3/4) |t|^{-3/4} W^{-1/8}.      (CP.1)

This is the key new mechanism: a fixed row/column anchor whose ordinary third-volume marginal would be 1 is paid by L2 in the anchor variable, while the conditionally diffuse residual pair bank pays the other two determinant directions. The nonzero anchor-edge magnitude disappears from (CP.1).

The next step in this run is to turn (CP.1) into a translation-uniform half-Riesz bound and then, after one genuine original-coordinate scalar square, an L-infinity density bound. I will also compile it with the designated account02/B13 two-hub packet and with the account02/B07 incident-E2 anchor lift.

Sources actually used so far:
- account02/B13 completed r23 exterior/Schur compiler: math-open-problems@892bfe36756e09cbaff3f05070f7a3e20fea0fd1.
- account02/B07 incident-E2 anchor lift, current report path proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T043951Z-account02-B07-4c9e7a/REPORT.md.
- newest required volume-stability package: proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md (full QFORM still open).

Status: SUPPORTING CALCULATION, not a full theorem yet. Independent review not performed. WITHOUT_VERIFIED_BRAIN.
