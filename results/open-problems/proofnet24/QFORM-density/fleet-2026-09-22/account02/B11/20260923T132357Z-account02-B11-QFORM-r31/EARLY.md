# account02/B11 r31 — early null-pivot reduction

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target OPEN.

First unpaid implication attacked: the genuinely indefinite exact-rank-three branch with a physical zero/near-zero pivot, where the rank-two opposite-sign logarithm must be smoothed by the third direction without post-rotation independence.

## Exact null-pivot normal form

Let `A=RMR^T`, `R^TR=I_3`, `M=M^T` invertible and indefinite. Fix an ORIGINAL coordinate `0` with spectral row `r`, leverage `c=||r||^2>0`, and physical pivot `A_00=r^TMr=0`.

Put `e1=r/sqrt(c)`. Since `e1^TMe1=0`, the vector `Me1` is Euclidean-orthogonal to `e1`. Choose an orthonormal spectral basis `(e1,e2,e3)` with `e2=Me1/||Me1||`; then

`M = [[0,kappa,0],[kappa,a,b],[0,b,d]]`,

where `kappa=||Me1|| >= s := sigma_min(M)` and

`det M = -kappa^2 d`.

Write the remaining spectral projections as

`U=sum_{j!=0}u_j X_j`, `V=sum v_j X_j`, `Z=sum z_j X_j`.

Parseval gives

`sum (u_j,v_j,z_j)(u_j,v_j,z_j)^T = diag(1-c,1,1)`.

Thus the exact quadratic form is

`Q = 2 kappa (sqrt(c)X_0+U)V + a V^2 + 2b VZ + d Z^2`.          (E1)

The three coefficient vectors of

`W:=sqrt(c)X_0+U`, `V`, `Z`

are orthonormal in the ORIGINAL coordinate space, but are not asserted independent. This is a product-provenance normal form, not a probabilistic rotation.

For signature `(+,+,-)`, `det M<0`, hence `d>0`; for `(+,-,-)`, `det M>0`, hence `d<0`. Therefore the isolated square `dZ^2` has the majority sign. Deleting it leaves the null/hyperbolic rank-two core `2kappa WV+aV^2+2bVZ`, which contains the logarithmic product endpoint.

## Immediate source application and partner obstruction

The pinned Claude ruled theorem pays the majority one-sheet side of every exact-rank-three indefinite form by `pi*sqrt(2)/s`; it does not pay the opposite two-sheet side.

The latest completed designated partner account03/B11 r32 gives a four-ray exact-rank-three family for which every raw physical triple volume is `O(k^{-3})`, so any proof demanding one fixed good raw triple loses scale. However every row in that family has full rank-three leverage at most `1/(2k)<=1/2`; therefore the pinned Claude Theorem F applies directly and yields

`||p_Q||_infinity <= 12 |det M|^{-1/3} <= 12/s`.

So the r32 obstruction is real for fixed-minor selection but is already paid by diffuse Fresnel--Brascamp--Lieb. The genuinely unpaid exact-rank-three branch must retain high localized leverage after the diffuse exit; the zero/near-null pivot is the relevant localized geometry.

Next: exploit (E1) with ORIGINAL-coordinate product provenance. In the source-disjoint Witt-split subcase, `W` is genuinely independent of the planar pair `(V,Z)` and the completed null-scalar receiver gives a determinant-homogeneous bound. Outside that subcase, identify the exact finite-spike obstruction rather than replacing `(V,Z)` by an arbitrary planar joint cap.
