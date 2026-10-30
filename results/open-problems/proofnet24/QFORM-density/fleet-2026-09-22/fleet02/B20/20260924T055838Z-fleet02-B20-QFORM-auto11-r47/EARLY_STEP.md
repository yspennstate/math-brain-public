SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-24T05:58:38Z.
attacking: the newest fleet03/B20 r48 strong-edge punctured-rank-two survivor by applying the exact arbitrary-rank physical-pair theorem and Schur rank-two completion before any post-puncture minor extraction.

# Early substantive step

Let the literal original-coordinate pair in fleet03/B20 r48 be first and write

A = [[B,E],[E^T,C]],   S = C-E^T B^{-1}E.

Define

A0 = [[B,E],[E^T,E^T B^{-1}E]]
   = [I;E^T B^{-1}] B [I,B^{-1}E].

Hence rank(A0)=2 and A-A0=diag(0,S). By the best-rank-two characterization of the third singular value,

s3(A) <= ||A-A0||op = ||S||op.

Thus the full target hypothesis s3(A)>=1 forces ||S||op>=1 with no condition on E and without any rotation of the random source. The remaining variables are still the original independent coordinates after exact completion of the physical pair.

The source-pinned arbitrary-rank quarter-small-ball theorem then gives, for the exact Schur remainder R including all induced affine terms,

sup_w P(|R-w|<rho) <= min(1,5 rho^(1/4)).

Combining this with the completed logarithmic density envelope for an invertible indefinite physical pair B, D=|det B|, kappa=s_min(B), yields

||p_Q||infinity <= 3*400^(1/3) D^(-1/3) kappa^(-1/6).

For the newest designated partner fleet03/B20 r48, the exact physical-pair constants are

D >= D0 = 9.530157744638501e-7,
kappa >= kappa0 = 6.075614261408114e-5.

Therefore the entire r48 strong-edge leaf is paid, with no post-puncture s3 hypothesis:

||p_Q||infinity <= 3*400^(1/3) D0^(-1/3) kappa0^(-1/6)
                 = 11328.598626026012 < 11329.

This strictly removes the r48 `punctured-rank-two` survivor from that strong-edge leaf. Full unrestricted QFORM remains open because the transverse/aligned and global diffuse/hub-star branches need not contain such a quantitative physical pair.
