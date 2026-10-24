SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T19:50:27Z.
attacking: a carrier-local approximation-number theorem for arbitrary signed spectral additions, replacing hard footprint rank by the best local low-rank approximation error.

# Early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target OPEN.

Fresh brain control resolved at `b3194faf6f2f82029363d57446443234a27d7079`; effective OWNER CONTROL revision `2026-09-22.15`. Current owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` consumed. Same-hour canonical login already existed for account01/B12 and was preserved rather than overwritten.

The first missing implication attacked is additional-eigenvalue stability without treating the induced quadratic remainder as an independent convolution. Let `P=P_H` be projection onto an ORIGINAL-coordinate carrier of size `m`, and let `A=A0+E` with `A0,E` symmetric. For every `k,r` with `k+r<=m`, the rectangular singular-value inequality gives

`boxed: sqrt(lambda_k((A^2)[H,H])) = s_k(AP) >= [s_(k+r)(A0 P)-s_(r+1)(E P)]_+.`

Equivalently,

`boxed: sqrt(lambda_k((A^2)[H,H])) >= [sqrt(lambda_(k+r)((A0^2)[H,H]))-s_(r+1)(E P_H)]_+.`

Proof route: take the rank-r truncated SVD `L_r` of the carrier action `E P`; write `E P=L_r+R_r` with `rank L_r<=r` and `||R_r||op=s_(r+1)(E P)` (Eckart-Young). Rank-r interlacing gives `s_k(A0P+L_r)>=s_(k+r)(A0P)`, then operator-norm Weyl pays `R_r`.

This strictly softens the previous hard local-footprint theorem: `rank(E P)<=r` makes the charge zero, but full-rank `E P` is still harmless when its `(r+1)`st singular value is small. The mechanism is purely deterministic in original coordinates and uses no independence after rotation.

Designated partner to be applied at an actual inequality: `account02/B12` report `yspennstate/math-open-problems@c635fcdce6aa206c68f1f14e061cf617d72376fb`, whose six-square-mode compiler turns `lambda_6((A^2)[H,H])>=g^2` on an ORIGINAL-coordinate carrier into `||p_Q||_infinity<=C_m/g` with explicit `C_m`.
