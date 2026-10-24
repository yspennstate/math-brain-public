SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T19:56:12Z.
attacking: stabilize a diffuse strong rank-three carrier against a weak fourth carrier by aggregate physical three-volume smoothing, or force strong original-coordinate localization without deleting the weak mode.

# Early substantive checkpoint

Let

A = D + R K R^T + mu w w^T,

where D is diagonal in the original source coordinates, R has three orthonormal columns, w is a unit vector orthogonal to range(R), K=K^T is 3x3 with s_3(K)>=gamma>0, and mu is arbitrary. Put a_i=||R(i,:)||_2^2.

Set delta=1/192, H={i:a_i>delta}, L=H^c. Then |H|<=576. If lambda_min(R_L^T R_L)<1/4, some unit u in R^3 satisfies

||(Ru)_H||_2^2>3/4,

so a genuinely strong carrier direction is physically localized.

Otherwise R_L^T R_L>=I_3/4. Split the light coordinates randomly into J and L\J, putting H on the other side I. Since

E||R_J^T R_J-(1/2)R_L^T R_L||_F^2
 =(1/4) sum_{j in L} a_j^2
 <=(delta/4) sum_j a_j
 <=1/256,

there exists a literal original-coordinate cut with

R_J^T R_J>=I_3/16,
R_I^T R_I>=7I_3/16.

For the strong cross block B0=R_J K R_I^T,

s_3(B0)>=sqrt(7) gamma/16=:c gamma,

and every size-three row-volume marginal is at most

alpha_j(B0)=R(j,:)(R_J^T R_J)^(-1)R(j,:)^T<=16/192=1/12.

Now add the weak-mode cross perturbation E=mu w_J w_I^T. It has rank one and ||E||op<=|mu|/2. If the singular values of B0 are sigma_1>=sigma_2>=sigma_3, the exterior-cube map has the exact rank-one-update expansion

wedge^3(B0+E)=wedge^3(B0)+T,

with no terms containing E twice, and in singular coordinates

||T||HS <= ||E||op (sigma_1 sigma_2+sigma_1 sigma_3+sigma_2 sigma_3)
           <=3 ||E||op sigma_1 sigma_2.

Hence, writing Z0=||wedge^3 B0||HS^2 and theta=||T||HS/sqrt(Z0),

theta<=3|mu|/(2c gamma).

If

|mu| <= c gamma/12 = sqrt(7) gamma/192,

then theta<=1/8. Therefore

sqrt(Z_3(B0+E)) >= (7/8)sqrt(Z0)
                 >=(7/8)(c gamma)^3.

For a physical row j in J, project the exterior cube onto row triples containing j. Triangle inequality gives

alpha_j(B0+E)
 <=[(sqrt(1/12)+1/8)/(7/8)]^2
 <0.224<1/2.

Thus the completed account03/B09 aggregate physical-cross theorem applies to the FULL cross block B=B0+E, while D and all same-side curvature stay in the phase:

||p_(X^T A X)||_infinity
 <=6 sqrt(2e) Z_3(B)^(-1/6)
 <=[96 sqrt(2e)/(sqrt(7))] (8/7)^(1/3) gamma^(-1)
 <88.454 gamma^(-1).

The same coefficient gives P{X^TAX in I0}<=88.454 gamma^(-1)|I0|, and the density is continuous. This is a uniform weak-fourth-mode stability statement: as mu->0 there is no reciprocal |mu| loss. If the paid branch fails while |mu| is below this universal fraction of gamma, a strong top-three carrier direction, not merely the weak fourth mode, is >3/4 localized on at most 576 original coordinates.

This checkpoint is only a supporting theorem; full QFORM remains open.
