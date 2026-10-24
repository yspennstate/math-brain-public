SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T03:01:25Z.
attacking: scalar-pivot plus aggregate Schur-cross-volume gluing, with arbitrary rough product laws retained.

# Early substantive checkpoint

Let `k` be an ORIGINAL coordinate with `a=A_kk != 0`. After conditioning/completing only that original scalar,

`Q = a (X_k + ell(Z)/a)^2 + R(Z)`,

where `Z=(X_i)_{i!=k}` remains a product source and the quadratic matrix of `R` is the Schur complement

`S=A_{\bar k,\bar k}-a^{-1}A_{\bar k,k}A_{k,\bar k}`.

Suppose some disjoint ORIGINAL-coordinate cross block `M=S[I,J]` has

`Z3=e_3(M^T M)>0`.

The completed account03/B13 r21 theorem gives

`||p_R||_3 < 6.787 Z3^(-1/9)`

with all other Schur terms and affine leakage arbitrary. For fixed outside coordinates, the cap-one law of the shifted original scalar gives

`p_{a(X_k+s)^2}(u) <= |a|^(-1/2)|u|^(-1/2)`.

Therefore

`p_Q(t) <= |a|^(-1/2) E |t-R|^(-1/2)`.

New fractional-potential calculation: if `p>=0`, `int p=1`, `||p||_3<=L`, then

`sup_t int |t-s|^(-1/2)p(s) ds <= C_* L^(3/4)`,

where

`C_* = 4 sqrt(pi/(2 sqrt(3))) = 3.809251227455829...`.

Proof: for lambda>0,

`|u|^(-1/2) <= lambda + (|u|^(-1/2)-lambda)_+`,

and

`int_R (|u|^(-1/2)-lambda)_+^(3/2) du = (3pi/2) lambda^(-1/2)`.

Holder followed by optimization in lambda gives the displayed constant.

Hence the target-level branch

`||p_Q||_infinity < 16.018 |a|^(-1/2) Z3^(-1/12)`.

This is homogeneous of degree `-1` in the quadratic scale. It uses no support/moment/connectedness condition and no independence after rotation. The remaining structural gap is to force a universally positive currency `|a|^6 Z3` in an unpaid no-pivot branch, or route its failure into an already-paid diffuse/null/tube/hub mechanism.

Designated partner use: account04/B13 at math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1 proves the no-attainment product purification; after proving the slab inequality for bounded finite-union unit product sets, its Corollary 2.2 transfers it to every arbitrary cap-one product law with zero constant loss.

Status: supporting theorem candidate with full derivation to follow; full QFORM and full continuity remain OPEN.
