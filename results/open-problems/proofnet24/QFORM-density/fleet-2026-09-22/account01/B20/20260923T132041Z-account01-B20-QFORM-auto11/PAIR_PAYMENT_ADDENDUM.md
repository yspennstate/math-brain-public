# Addendum — the account03/B20 r32 indefinite physical-pair packet is already paid

The current account03/B20 r32 compiler leaves, among its four structural packets, an ORIGINAL-coordinate indefinite principal pair `B` satisfying

`D:=|det B| > 53/3276800`,

`kappa:=sigma_min(B) > 53/428800`,

while the ambient matrix has `s_3(A)>=1`.

The completed full-matrix physical indefinite-pair theorem is recorded at

`yspennstate/math-open-problems@1a70497363989dfea9fa4ce9e515fa279677df69`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260922T184724Z-account03-B20-QFORM-r15/REPORT.md`, Section 2.3. It states, for arbitrary remaining spectrum and affine terms,

`||p_Q||_infinity <= 3*400^(1/3) (D^2 kappa s_3(A))^(-1/6)`.

Substitution of the **actual r32 constants** gives

`||p_Q||_infinity
 < 3*400^(1/3)
   [ (53/3276800)^2 (53/428800) ]^(-1/6)`

`=3916.178013122167... <3916.179`.

Hence the r32 indefinite-pair packet is a completed arbitrary-extra-spectrum density branch. No rank-three restriction, spectral-coordinate independence, or pointwise quadratic oscillatory estimate is used.

Combining this with the main report of the present run, the currently unpaid r32 descendants are now only:

1. the moderate-diagonal descendants produced by `QFORM-N3-MODERATE-PIVOT-SCHUR-COMPOUND-COMPILER-v1`: anchored `O1`, or fixed-mass `O2/O3` third-compound packets;
2. the star / rank-two-dominated cross packet;
3. the star / two-sided ridge-localized physical-anchor packet.

Thus the first remaining closure obligation sharpens to

`QFORM-N3-O1/O2/O3-OR-RANK2/TWOANCHOR-PAYMENT-v1`.

Full QFORM remains OPEN. This addendum does not claim full-target continuity.
