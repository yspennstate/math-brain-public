# account02/B11 — early calculation: the full Schur three-frequency law pays every power below three

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B11-20260924T102053Z-auto11`  
Status: supporting theorem / full QFORM open.

## Setup

Let `A=R M R^T`, `R^T R=I_3`, be exact rank three, let `D=|det M|`, and choose an ORIGINAL coordinate `h` with `alpha=A_hh != 0` and leverage `q=||R^T e_h||^2>0`.  Write

`A=[[alpha,c^T],[c,B]]`, `S_h=B-c c^T/alpha`.

For an independent copy `X'`, put `U_j=X_j-X'_j`.  These are independent and each difference density is at most one.  Let `E` be an orthonormal basis of `range(S_h)` and

`Z=E^T S_h U_{h^c} in R^2`.

The completed account03/B11 r54 result (building on r53 plus the exact Schur pseudodeterminant identity) gives

`||p_Z||_infty <= 2|alpha|/(qD)`.

Define the *full sheared Schur frequency*

`Xi=(alpha U_h+c^T U_{h^c}, Z) in R^3`.

Because `U_h` is independent of the residual product bank, disintegration at fixed `Z=z` shows

`p_Xi(x,z) <= |alpha|^{-1} p_Z(z) <= 2/(qD)`.

No independence of rotated coordinates is asserted.

## Theorem — QFORM-SCHUR-THREEFREQ-NEGATIVE-MOMENTS-v2

For every center `xi0 in R^3` and every `0<gamma<3`,

`E ||Xi-xi0||^{-gamma}
 <= [3/(3-gamma)] [8 pi/(3 q D)]^{gamma/3}.`

Proof: if `K=2/(qD)` and `v_3=4pi/3`, then

`P(||Xi-xi0|| <= r) <= min(1,v_3 K r^3)`.

With `r0=(v_3 K)^(-1/3)`, layer cake gives

`E R^{-gamma}
 = gamma int_0^infty r^{-gamma-1} P(R<r) dr
 <= gamma v_3K int_0^{r0} r^{2-gamma}dr
    + gamma int_{r0}^infty r^{-gamma-1}dr
 = [3/(3-gamma)](v_3K)^{gamma/3}.`

In the live near-coloop collar `q>=63/64`, `D>=s^3`,

`E ||Xi-xi0||^{-gamma}
 <= [3/(3-gamma)](512 pi/189)^{gamma/3} s^{-gamma}.`

In particular

`E ||Xi-xi0||^{-2} <= 12.5052757995... s^{-2}`

and the stronger example

`E ||Xi-xi0||^{-5/2} <= 35.7368504687... s^{-5/2}`

is also uniformly paid.

Thus a correct Moyal/coarea compiler may lose *any fixed power strictly below three* of the authentic full Schur frequency.  Freezing the hub first unnecessarily collapses the budget back to the two-dimensional `gamma<2` window of r54.

## Sharpness at exponent three is source-valid

Take `A=diag(1,1,-1)` and centered unit-uniform original coordinates.  Choose `h=1`. Then `alpha=q=D=1`, `c=0`, and

`Xi=(U_1,U_2,-U_3)`.

Each `U_j=X_j-X'_j` has triangular density `mu(u)=1-|u|` on `[-1,1]`. Hence `p_Xi >= 1/8` on the ball `||xi||<=1/2`, and therefore

`E||Xi||^{-3} >= (1/8) 4pi int_0^{1/2} dr/r = infinity.`

So exponent three cannot be paid merely from the genuine original-product difference law. This is an obstruction to a critical inverse-cube compiler, not a counterexample to QFORM.

## Critical logarithmic saving

Let `K=||p_Xi||_infty` and `a=(v_3 K)^(-1/3)`. For every `eta>0`, splitting at radius `a` gives

`E [ ||Xi-xi0||^{-3} / log(e+a/||Xi-xi0||)^{1+eta} ]
 <= 4pi K (4/3 + 1/eta).`

Indeed the outer part is at most `v_3K`; on the inner ball use the cap `K` and substitute `u=a/r`:

`4pi K int_0^a dr/[r log(e+a/r)^{1+eta}]
 =4pi K int_1^infty du/[u log(e+u)^{1+eta}]
 <=4pi K(1+1/eta)`.

Thus the exact compiler design window is now quantitative: any reciprocal loss `||Xi||^{-gamma}`, `gamma<3`, is paid; at `gamma=3` one needs more than one logarithm of saving (or some additional structure).  The source-valid diagonal example shows the bare `gamma=3` endpoint diverges.
