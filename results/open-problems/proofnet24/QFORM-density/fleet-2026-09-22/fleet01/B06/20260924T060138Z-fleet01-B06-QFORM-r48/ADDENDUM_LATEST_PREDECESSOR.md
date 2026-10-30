# Addendum — reconciliation with the actual latest B06 predecessor

After the initial r48 report was drafted, the worker-owned `LATEST.json` showed a newer completed B06 run than the older r47 handoff first consumed. The actual latest predecessor is:

- fleet01/B06 run `20260924T053508Z-fleet01-B06-QFORM-r48`;
- `yspennstate/math-open-problems@0f6cfec7bda71e411d2296267eb7ff1ab016d46f`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260924T053508Z-fleet01-B06-QFORM-r48/REPORT.md`.

That predecessor proves the exact two-hub normal-direction Schur collapse when both hub twists vanish and leaves `QFORM-TWOHUB-ONE-TWIST-OR-SMALLPAIR-RECEIVER-v1`: remove one zero-twist assumption, or route a small/singular physical pair and the concentrated-normal third-hub certificate through a product-preserving receiver.

The present run directly pays a genuine part of that debt:

1. `QFORM-RANK1-PHYSICAL-PAIR-TRANSVERSE-SLOPE-v1` applies to an **exact rank-one physical pair with arbitrary same-bank tail quadratic curvature and with no zero-twist assumption**. If `w` spans the pair nullspace and `n=A_{T,H}w`, then

   `||p_Q||_infinity <=2^(13/4)e^(1/4)(|theta| ||n||)^(-1/2)`.

2. `QFORM-ZERO-PAIR-RANK2-CROSS-v1` applies when the literal pair block vanishes and the full literal cross block has rank two:

   `||p_Q||_infinity <=sqrt(2 pi e)(sigma_1 sigma_2)^(-1/2)`.

3. In the rank-three carrier notation of the predecessor, for `H={h,j}`, `T=H^c`, `eta=||r_h wedge r_j||`, `tau_res=1-sigma_1(R_H)^2`, and `s=sigma_min(Lambda)`, the exact cross block satisfies

   `sigma_1(A_{H,T})sigma_2(A_{H,T}) >= s^2 tau_res eta`,

   and every unit pair direction `w` satisfies

   `||A_{T,H}w|| >= s sqrt(tau_res) eta`.

Therefore, on the predecessor's two-hub plane branch `eta^2>7/64`, exact rank-zero and exact rank-one physical-pair degeneracy are no longer obstructions whenever the residual carrier gap `tau_res` and, in the rank-one case, the surviving pair eigenvalue are quantitative.

This does **not** solve the predecessor's full debt. Still open are: near-coloop `tau_res ->0`; small surviving rank-one eigenvalue; and near-singular but nonzero indefinite pairs, whose logarithmic critical singularity can interact with arbitrary same-bank curvature. The latest predecessor is thus compatible with and strictly sharpened by the present endpoint receivers.
