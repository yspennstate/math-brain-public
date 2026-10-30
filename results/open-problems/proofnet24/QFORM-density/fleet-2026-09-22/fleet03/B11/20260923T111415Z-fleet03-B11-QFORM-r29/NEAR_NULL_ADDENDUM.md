# r29 addendum — exact algebra at the near-null shared-line endpoint

This addendum sharpens, but does not close, the remaining `m_22 -> 0` endpoint of the main report.

In the exact two-plane geometry

`G_S=diag(1,rho,0)`, `G_T=diag(0,1-rho,1)`,

the spectral core of the physical cross block, after removing the positive row/column scale factors, is

`C=[[m_12,m_13],[m_22,m_23]].`

Thus exact physical cross rank at most one implies

`m_12 m_23 = m_13 m_22`.                                      (A.1)

For `m_22 !=0`, (A.1) says that after completing the shared square the off-diagonal entry of the outer Schur complement vanishes exactly:

`N_13=m_13-m_12 m_23/m_22=0`.

So the r29 receiver is actually paying a diagonal nondegenerate outer rank-two quadratic in this exact cross-collapse chamber. The half-Riesz theorem was kept in orientation-free form because no sign case split is needed.

At the exact null endpoint `m_22=0`, (A.1) becomes

`m_12 m_23=0`.                                                  (A.2)

Since `M` is invertible, the two factors cannot both vanish. There are exactly two algebraic alternatives.

### Alternative A

If `m_12=0`, then `m_23 !=0` and

`det M = -m_11 m_23^2`.                                       (A.3)

Moreover `||M e_2||=|m_23|`, so `sigma_min(M)>=s` implies

`|m_23|>=s`.                                                   (A.4)

The quadratic form is

`m_11 Y_1^2 + 2m_13 Y_1 Z_3 + m_33 Z_3^2
 +2m_23 (Y_2+Z_2)Z_3`.                                      (A.5)

### Alternative B

If `m_23=0`, then `m_12 !=0` and

`det M = -m_33 m_12^2`,                                      (A.6)

while `||M e_2||=|m_12|` gives

`|m_12|>=s`.                                                   (A.7)

This is the sign/reflection-dual configuration.

Equations (A.3)--(A.7) show that the remaining exact endpoint is not loss of all curvature: a null shared direction has a coupling of size at least `s` to exactly one outer direction, and invertibility supplies transverse quadratic curvature on the opposite outer direction. What fails is the **product partition required by the existing null-scalar theorem**: the null scalar is `Y_2+Z_2`, a sum of one component from each independent planar bank, while `Y_1` is correlated with `Y_2` inside bank `S` and `Z_3` is correlated with `Z_2` inside bank `T`.

Accordingly the exact next analytic statement is now:

`QFORM-TWOPLANAR-NULLSUM-RECEIVER-v1`:

> Let `(U,Z)` and `(V,W)` be independent planar random vectors with bounded joint densities. Prove a dimension-free density bound for the null-sum normal form
> `beta U^2 + 2 alpha V(Z+W) + 2 gamma UV + delta V^2 + affine`,
> uniformly under the determinant condition `alpha beta !=0`, with the sign-dual form allowed.

A proof of this statement with constants depending only on the planar density caps and `|alpha^2 beta|` would close the exact `m_22=0` rank-one cross endpoint after the r28 two-bank balance. It must keep the two planar product weights through the `1/|V|` null kernel; replacing either bank by a worst conditional scalar cap is forbidden by the live corrections.

This addendum is a structural reduction, not a bounded-density theorem for the null endpoint and not a solution of full QFORM.
