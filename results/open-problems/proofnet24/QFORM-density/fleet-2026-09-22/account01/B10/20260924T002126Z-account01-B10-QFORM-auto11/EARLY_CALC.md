SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-24T00:21:26Z.
attacking: QFORM-SHARED-HUB-ONE-PLUS-TWO-BANK-GLUING-v1 via exact triangular source-bank conditioning and null-hub Gram identities.

# Early calculation — triangular same-source leakage can be absorbed exactly

Work in the exact-rank-three null-hub normal form. Let `U^T U=I_3`, choose a physical row `u_0=sqrt(h) r` with `r^T M r=0`, and choose the orthonormal spectral basis `(r,v,q)` with `v=Mr/||Mr||`. Then

`M=[[0,s,0],[s,b,c],[0,c,d]]`, with `s!=0`, `d!=0`, and `D:=|det M|=s^2|d|`.

Write every leaf row as `u_i=t_i r+y_i v+z_i q`. Let the leaves be split into disjoint ORIGINAL-coordinate banks `L union R`. Suppose the unrestricted bank satisfies the exact triangular source condition

`t_R = alpha y_R + beta z_R`

for some real `alpha,beta`, and suppose the transverse Gram

`G_R=[[||y_R||^2,<y_R,z_R>],[<y_R,z_R>,||z_R||^2]]`

is positive definite.

Condition on all ORIGINAL variables in `L`. If `T_L,Y_L,Z_L` denote their now-fixed linear aggregates, then, with

`Y=Y_L+Y_R`, `Z=Z_L+Z_R`,

`T_L+T_R = alpha Y+beta Z+gamma_L`,
`gamma_L=T_L-alpha Y_L-beta Z_L`.

Hence the full quadratic form becomes, conditionally,

`Q=2s sqrt(h) X_0 Y +(b+2s alpha)Y^2+2(c+s beta)YZ+dZ^2+2s gamma_L Y`.

Thus the same-source longitudinal leakage on `R` has disappeared into the transverse quadratic/affine coefficients; it does NOT need to be independent of `(Y,Z)`. The only independent split now used is the genuine original-coordinate split `{0}` versus `R`, after conditioning `L`.

The vector `(Y_R,Z_R)` has density cap at most

`K_2 <= 2 / sqrt(det G_R)`

by normalizing with `G_R^{-1/2}` and applying the sharp two-dimensional product-projection density theorem. The scaled hub `sqrt(h)X_0` has density cap `K_H<=h^{-1/2}`.

The preceding account01/B10 two-bank hyperbolic-square receiver extends verbatim to arbitrary affine terms in `(Y,Z)` and gives

`||p_{Q | X_L}||_infinity <= 6 (K_H K_2)^(2/3) (s^2|d|)^(-1/3)`

and therefore

`||p_{Q | X_L}||_infinity <= 6*2^(2/3) h^(-1/3) D^(-1/3) (det G_R)^(-1/3)`.

The right side is independent of the conditioned values. Averaging the conditional densities therefore gives the same essential bound for the unconditional law. Continuity of this conditional mixture is not asserted.

## Exact obstruction identity

Let

`delta_R^2 := dist(t_R,span{y_R,z_R})^2`.

Since `G_R>0`, Schur's determinant identity gives

`det Gram(t_R,y_R,z_R)=det(G_R) delta_R^2`.

Cauchy--Binet gives the exact physical-row formula

`det Gram(t_R,y_R,z_R)
 = sum_{i<j<k in R} det(u_i,u_j,u_k)^2`.

Hence

`boxed: delta_R^2 det(G_R)=sum_{i<j<k in R} det(u_i,u_j,u_k)^2.`

So the triangular bank criterion is equivalent to vanishing of every hub-free rank-three minor inside `R`. In the full near-coloop leaf set, Parseval gives `G=I_2`, `t perp y,z`, hence the right side is exactly `||t||^2=1-h`. This identifies the generic residual as a small but nonzero hub-free triple-volume, not a failure of the two-bank analytic receiver.

Next: formalize the affine receiver, prove the conditional-mixture theorem, apply it to the completed account02/B10 near-coloop family and to a row-mixed contaminated-leakage variant, and then quantify why the projected-crossing route still loses the residual triple-volume scale.
