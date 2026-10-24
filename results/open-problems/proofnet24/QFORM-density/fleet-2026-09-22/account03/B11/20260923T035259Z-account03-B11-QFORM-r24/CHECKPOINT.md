SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T03:52:59Z.
attacking: minority-sign physical scalar completion: turn the third coordinate into an elliptic discriminant trace, then splice with the partner sign-frustrated triangle branch.

# Early substantive checkpoint — minority scalar discriminant

Let `X` be a real variable with density at most one, independent of a two-dimensional random vector `Y` with joint density `g` satisfying `||g||_infinity<=M`. Let

`H=[[a,b^T],[b,C]]`

be an invertible symmetric `3x3` matrix of inertia `(2,1)` or `(1,2)`. Assume the scalar pivot `a` carries the minority inertia sign. Equivalently, `a det(H)>0`. Allow arbitrary affine terms:

`Q=aX^2+2X(b^T Y+r)+Y^T C Y+2d^T Y+c`.

For fixed `Y=y`, the quadratic equation `Q=t` has discriminant

`D_t(y)=(b^T y+r)^2-a(y^T C y+2d^T y+c-t)`.

Because `f_X<=1`, summing the two scalar roots gives the pointwise conditional-density envelope

`p_{Q|Y=y}(t)<=1_{D_t(y)>0}/sqrt(D_t(y))`.

Set `K=bb^T-aC`. Schur inertia gives

`K>0`,

because with `S=C-bb^T/a`, the minority-pivot hypothesis makes `S` definite with the majority sign and `K=-aS`. Also

`det K=a det H>0`.

After completing the square in `y`, every superlevel set of the kernel is an elliptical shell:

`|{y: 0<D_t(y)<s^{-2}}| <= pi s^{-2}/sqrt(det K)`.

Using both `g<=M` and `int g=1`, layer cake gives

`p_Q(t) <= int_0^infinity min(1, M*pi*det(K)^(-1/2)*s^(-2)) ds`
`       = 2 sqrt(pi M) det(K)^(-1/4)`
`       = 2 sqrt(pi M) [a det H]^(-1/4)`.

Thus the candidate theorem is

`||p_Q||_infinity <= 2 sqrt(pi M) [a det H]^(-1/4)`.

For an ORIGINAL-coordinate physical triple inside the full ambient QFORM problem, conditioning every outside original coordinate leaves the three input coordinates independent; choosing the minority-sign physical coordinate as `X` gives `M=1`, so the same bound is uniform in all outside couplings/affine terms.

This is correction-safe: no post-rotation independence, arbitrary-joint coarea theorem, conditional-density surrogate, moment/support hypothesis, or pointwise stationary-phase bound is used.

Still to check before finalization: exact determinant/inertia algebra, the affine shell measure, an explicit rotated target example, and splice with the completed designated account04/B11 sign-frustrated theorem at an actual inequality. Full QFORM remains open; continuity is not yet claimed.
