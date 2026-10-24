# account01/B13 checkpoint — anchored third-volume exact identities

Programme: QFORM-DENSITY-3EIG-20260922. Full QFORM remains OPEN.

Fresh partner input actually used: account02/B13 r30, `math-open-problems@f6ad7b994c1ba509af30fceaf45e8b464db86af8`, which gives for any physical cross block `B` and slab ratio `rho` the alternative: either `s3(B)<=C3/rho`, `C3=9 sqrt(3e)`, or there are a physical row `i` and physical column `j` whose squared-third-minor marginals exceed `2/3`; hence their joint anchored third-volume is more than `Z/3`, where `Z=e3(B^T B)`.

New exact calculation. Reorder the chosen row/column to the first positions and write

`B = [[b, r^T],[c,D]]`.

Let

`Z_ij = sum_{|R|=|T|=2} det B[{i} union R,{j} union T]^2`.

If `b!=0`, set `S=D-c r^T/b`. Row/column elimination gives, term by term,

`det B[{i} union R,{j} union T] = b det S[R,T]`,

so by Cauchy-Binet

`Z_ij = b^2 e2(S^T S)`.

If `b=0`, let `P_r` and `P_c` be orthogonal projections onto `r^perp` and `c^perp`. Orthogonal changes of basis in the residual row/column spaces preserve the anchored squared-minor sum. Rotate `r=||r||e1`, `c=||c||f1`. The only nonzero anchored minors use residual row 1 and residual column 1, and their determinants are `-||r||||c|| D_ab` for `a,b>1`. Hence

`Z_ij = ||r||^2 ||c||^2 ||P_c D P_r||_F^2`.

This identity was numerically checked on 100 random `5x6` matrices: maximal relative errors were `3.97e-15` (`b!=0`) and `1.27e-15` (`b=0`). The numerical check is diagnostic only; the displayed algebra is the proof.

In the partner bi-hub branch, `s3(B)>C3/rho`, so `Z>=s3(B)^6>C3^6/rho^6`, while `Z_ij>Z/3`. Therefore

- if `b!=0`: `|b| sqrt(e2(S^T S)) > 2187 e^(3/2)/rho^3`;
- if `b=0`: `||r||||c||||P_c D P_r||_F > 2187 e^(3/2)/rho^3`.

The full report will combine this with the no-attainment finite-mixture product-law compiler and state the remaining closure obligation. No rotated random coordinates or perturbative deletion is used.
