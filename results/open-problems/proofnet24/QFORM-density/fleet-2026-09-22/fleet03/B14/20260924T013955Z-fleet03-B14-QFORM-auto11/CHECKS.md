# Checks for QFORM-DISJOINT-BANK-SCHUR-LOCALIZATION-v1

Run: `20260924T013955Z-fleet03-B14-QFORM-auto11`.

## 1. Scaling check

If `Y_r` has density cap `M_r`, then `Z_r=M_r Y_r` has density cap at most one because

`p_Z(z)=M_r^{-1} p_Y(z/M_r) <= 1`.

For the Ball--Rogozin choice `M_r=sqrt(2)/rho_r`, with `R=diag(rho_r)`,

`Z=sqrt(2) R^{-1}Y`, hence `Y=(1/sqrt(2))RZ`.

Therefore

`Y^T B Y = Z^T[(1/2)RBR]Z`,

and the partner theorem pays

`6sqrt(pi) / sigma_min((1/2)RBR) = 12sqrt(pi)/sigma_min(RBR)`.

## 2. Conditioning check

With

`A=[[UBU^T, UC],[C^TU^T,D]]`

and `Y=U^T X_I`, conditioning on the outside original coordinates `X_J=x` gives exactly

`Q = Y^TBY + 2Y^TCx + x^TDx`.

No coordinate inside any active bank is conditioned on. Therefore the three projected variables `Y_r`, each depending on a disjoint original source bank, remain independent.

## 3. Translation and affine-scope check

Replacing `X` by `X+s` produces active-bank linear coefficient

`2(As)_I = 2U(BU^T s_I + C s_J)`,

which lies in `col(U)`. Thus translation changes only the affine term in the compressed three variables and leaves `(1/2)RBR` unchanged.

A separately added affine perturbation `b^T X` is covered by the same proof when `b_I in col(U)`; `b_J` may be arbitrary because it becomes a scalar after conditioning on `X_J`. No claim is made for a generic active-bank affine component orthogonal to `col(U)`.

## 4. Diffuse control family

Let `u_r=m^{-1/2}1_{I_r}` on three disjoint blocks of size `m`, and

`B_*=I_3-(2/3)11^T`.

The rank-one matrix `11^T` has eigenvalues `3,0,0`, so `B_*` has eigenvalues `-1,1,1`. Also

`B_*^2 = I - (4/3)11^T + (4/9)(11^T)^2 = I - (4/3)11^T + (4/3)11^T = I`.

Thus `sigma_min(B_*)=1`.

Because the `u_r` are orthonormal, `A_m=UB_*U^T` has nonzero spectrum exactly `{-1,1,1}`.

For a selected physical triple, form the `3x3` membership matrix `P_S` whose row is the standard basis vector of the selected coordinate's bank. Then

`(A_m)_{S,S}=m^{-1}P_SB_*P_S^T`.

- If two rows of `P_S` coincide, the physical block is singular.
- If all three rows are distinct, `P_S` is a permutation matrix and the physical block spectrum is `{-1/m,1/m,1/m}`.

Hence every physical triple has `sigma_min<=1/m`, while the bank-localized theorem gives the uniform constant

`12sqrt(pi)=21.269446210866192...`.

The designated fleet04/B14 physical-triple theorem applied directly would give only `6sqrt(pi)m` in the one-per-bank triple, so bank aggregation removes exactly the dimension-dependent inverse-minor loss in this chamber.

## 5. Scope check

The theorem requires the factorization `A_II=UBU^T` and `A_IJ=UC`. It does not claim that arbitrary matrices with `s_3(A)>=1` possess such a factorization with a universal lower bound on `sigma_min(RBR)`.

Continuity is not claimed because the partner theorem used here establishes essential boundedness only.
