# Post-publication splice: latest designated partner r24

A newer designated-partner artifact appeared during this run and is consumed here before handoff:

`yspennstate/math-open-problems@41b0325c7328a76eaa36b832b21c5cfbf720625d`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T044100Z-fleet03-B07-qform-r24/PREPUBLICATION_ADDENDUM.md`.

Its corrected high-tail compiler says: if the determinant-weighted row and column disjointness probabilities are both `<eta`, then for a physical anchor decomposition

`M=[[b,r^T],[c,N]]`

one has, with `F=||M||_F`, `Z=E3(M)>=(theta^2/6)F^6`,

`max{ b^2 E2(N), ||c||^2||r||^2 F_perp^2 } >= rho F^6`,

`rho=((1-2eta)theta^2)/216`,

where `F_perp=||P_(c^perp) N P_(r^perp)||_F`.

The r24 E-branch already gives `E2(N)>=rho F^4`. The T-branch gives the transverse norm

`Y := ||L_c N iota_r||_HS = ||c||||r||F_perp >= sqrt(rho)F^3`.

Now use the exact anchored third-minor tensor from partner r21,

`H = b C_2(N) - L_c N iota_r`,

whose Hilbert--Schmidt norm squared is the complete squared mass `W_ia` of physical `3x3` minors through the same row/column anchors. Put

`X=||b C_2(N)||_HS=|b| sqrt(E2(N))`.

Then the r24 T-branch has a cancellation-safe dichotomy:

- if `X>=Y/2`, then because `b^2<=F^2`,
  `E2(N)>=X^2/F^2>=rho F^4/4`;
- if `X<Y/2`, reverse triangle gives
  `sqrt(W_ia)=||H||_HS>=Y-X>Y/2`, hence
  `W_ia>rho F^6/4`.

Combining this with the r24 E-branch proves

## `QFORM-R24-E2-OR-ANCHORED-E3-v1`

Every r24 high-tail, small-disjointness state has either

`boxed: E2(N) >= (rho/4) F^4`,

or an **actual physical anchored third-minor bank**

`boxed: W_ia >= (rho/4) F^6`.

No individual minor is selected and no reciprocal pivot is taken.

The second branch feeds directly into the two-level conditional concentration tree proved in `REPORT.md`. If neither conditional-diffuse stop occurs, one physical `3x3` minor has

`|det C|^2 > W_ia/9 >= rho F^6/36`.

In `N3(tau)` the preceding physical-core theorem therefore gives

`||p_Q||_inf
 < 648 sqrt(pi)(tau+tau^2) rho^(-1/2) F^(-3)`.

If the outer large-star branch failed, `F>kappa/Lambda`, so this is universal.

At the r24 concrete collar

`theta=1/16`, `eta=1/64`, `rho=31/1769472`,
`tau=1/128`, `kappa=1/(256sqrt(3))`, `Lambda=1`,

the terminal concentrated anchored branch has the explicit unoptimized bound

`||p_Q||_inf < 1.88349e11`.

Thus the latest r24 high-tail branch is sharpened to two genuine lower-order debts:

1. residual aggregate `E2(N)>=rho F^4/4` (with r24's disjoint matching-bank structure available);
2. an anchored third-volume packet of mass `>=rho F^6/4`, whose fully concentrated portion is now paid and whose only remaining portion is pair- or singleton-conditional determinant diffusion with arbitrary same-bank curvature.

If r24's determinant-disjointness gate is large, its already-completed balanced-crossminor Fourier branch applies instead. The low-tail rank-one tube remains separate.

Full QFORM remains OPEN. This addendum supersedes the partner-version description in the first report for the final handoff, while leaving the sharp standalone theorem `W_ia >= T_2 Z_ia/2` intact.
