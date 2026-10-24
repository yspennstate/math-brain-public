# account03/B10 r32 early calculation — transverse curvature cannot collapse

Programme: `QFORM-DENSITY-3EIG-20260922`. Exact-rank-three near-coloop state only. Full QFORM remains open.

Let the spectral core in the deterministic adapted basis `(e,v,q)` be

`M=[[alpha,s,0],[s,b,k],[0,k,d]]`,

with `M=M^T`, `sigma_min(M)>=1`, and `|alpha|<1`. (In the live B10 collar `|alpha|<1/16`.) Since every eigenvalue of `M` has modulus at least one,

`M^2-I >= 0`.

Set

`delta:=alpha^2+s^2-1 >=0`.

The principal `{e,q}` block of `M^2-I` is

`[[delta, s k],[s k, k^2+d^2-1]]`.

Its determinant is nonnegative, hence

`delta(k^2+d^2-1) >= s^2 k^2`.

Using `s^2-delta=1-alpha^2`, this rearranges exactly to

`boxed: delta(d^2-1) >= (1-alpha^2) k^2`. 

If `delta>0`, the right side is nonnegative and therefore `d^2>=1`. If `delta=0`, the same inequality forces `k=0`, while the `(q,q)` diagonal of `M^2-I` gives `d^2-1>=0`. Thus in all cases

`boxed: |d|>=1`.

More generally, if `sigma_min(M)>=sigma` and `|alpha|<sigma`, the identical proof applied to `M^2-sigma^2 I` gives

`(alpha^2+s^2-sigma^2)(d^2-sigma^2) >= (sigma^2-alpha^2)k^2`,

so `|d|>=sigma`.

This is an exact deterministic consequence of the three-large-eigenvalue hypothesis; it uses no probabilistic rotation. In the B10 canonical form from r28, `d` is precisely the coefficient of the orthogonal transverse square `(y.X_L)^2`. Therefore the third curvature coefficient itself is endpoint-stable even when both the physical-coloop leakage `rho` and the hub Rayleigh coefficient `alpha` tend to zero.

The next step in this run is to combine this floor with the designated account04/B10 three-bank theorem, which already gives disjoint original-coordinate banks with `||A_{0,U}||^2>1/206` and `||y_V||^2>=1/162`, and then identify the exact remaining source-provenance obstruction to applying the independent-third-square receiver.
