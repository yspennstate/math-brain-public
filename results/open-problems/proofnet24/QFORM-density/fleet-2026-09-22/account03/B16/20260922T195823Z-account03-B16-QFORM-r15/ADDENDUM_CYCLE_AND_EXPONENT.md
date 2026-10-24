# Addendum — asymmetric cycle determinant and the exponent deficit after one decoupling

Let `C=(c_jk)` be an arbitrary real `3x3` matrix and consider `L_j^t(u)=(u_j,t(Cu)_j)` on `R^3`. Kernel directions are

`n_1=t(0,-c13,c12)`, `n_2=t(c23,0,-c21)`, `n_3=t(-c32,c31,0)`,

so

`det[n_1 n_2 n_3]=t^3 Delta(C)`,

with

`Delta(C)=c12 c23 c31-c13 c21 c32`.                                  (A.1)

For symmetric `C`, `Delta(C)=0`, recovering the exact obstruction in `REPORT.md`.

If `Delta(C)!=0`, the codimension-one geometric Loomis–Whitney/Brascamp–Lieb inequality gives

`integral_(R^3) product_j F_j(L_j^t u)^(1/2)du
 <= |t|^(-3/2)|Delta(C)|^(-1/2) product_j ||F_j||_1^(1/2)`.             (A.2)

Applying this with `F_j=|K_j|^2` and the proved ambiguity-kernel budget `||K_j||_2^2<=pi` yields

`integral product_j |K_j(u_j,t(Cu)_j+c_j)|du
 <= pi^(3/2)|t|^(-3/2)|Delta(C)|^(-1/2)`.                              (A.3)

The affine shifts do not alter the datum.

## Critical exponent check

Even (A.3) does **not** close QFORM after one quadratic decoupling, because the exact decoupling identity controls `|phi_A(t)|^2`. Taking the square root of an ideal `|t|^(-3/2)` estimate yields only `|phi_A(t)|=O(|t|^(-3/4))`, which is not integrable.

Thus breaking the symmetric three-cycle degeneracy is necessary but not sufficient. After one decoupling, the absolute product integral must gain essentially `|t|^(-3)` in order for its square root to have the integrable `|t|^(-3/2)` decay. Pure `L^2` counting points to six effective ambiguity factors, or an equivalent stronger mixed-norm/cancellation mechanism, in the delocalized regime. Localized cases can continue to use the existing physical-pivot/product-curvature arguments.

This exact exponent accounting prevents promoting a heuristic “three factors after decoupling” without paying the square-root loss.
