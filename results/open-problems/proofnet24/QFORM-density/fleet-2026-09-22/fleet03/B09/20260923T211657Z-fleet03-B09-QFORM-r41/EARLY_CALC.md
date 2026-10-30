SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T21:16:57Z.
attacking: aggregate a diffuse rank-two physical cross bank before reciprocal packet selection, then feed its two grouped bilinear directions into the full non-coordinate kernel-derivative receiver to obtain a linear interval bound.

# Early calculation — grouped rank-two cross bank

Let `L` be three ORIGINAL coordinates and `J` an arbitrary disjoint original-coordinate bank. Put

`P=A[L,L]`, `C=A[L,J]`, `rank(C)=2`.

Let `n` be a unit vector spanning `ker(C^T)`, `a=Pn`, and let

`Delta = sigma_1(C)sigma_2(C) = sqrt(pdet(CC^T)) >0`.

The key point is to aggregate the entire right bank before choosing any physical pair. Choose an orthonormal frame `E` for `n^perp` and write the left physical triple analytically as `Y=nx+Eu`. Then `B=E^T C` has rank two and the same nonzero singular values as `C`. Factor

`B=L0 R^T`,

where `L0=(BB^T)^(1/2)` and `R=B^T L0^(-1)` has orthonormal columns. Hence

`det L0 = Delta`, `R^T R=I_2`.

For the right original product bank `Z=X_J`, set `V=R^T Z`. The reviewed product-projection theorem gives

`||p_V||_infinity <= 2`.

For an arbitrary right-bank quadratic/affine phase `G(Z)`, push the complex measure `exp(itG(Z))dP_Z` to `V`; its density `b_t(v)` satisfies

`|b_t(v)|<=p_V(v)`, hence `||b_t||_2<=sqrt(2)`.

On the left, the only `x`-dependent phase is

`q_u(x)=d x^2+2 p^T u x+beta x`,

with `d=n^TPn`, `p=E^TPn`. Its derivative is the genuine original-product projection

`q_u'(x)=2(Pn)^T Y+beta = 2a^T Y+beta`.

Repeating the coarea/Hausdorff--Young calculation of fleet02/B09 `QFORM-3x2-KERNELDERIVATIVE-L1-v1`, but before the `u`-to-cross-slope change of variables, gives

`||A||_4 <= 2^(13/8) pi^(1/4) ||a||^(-1/4)`,

where `A(t)^2=int |F_u(t)|^2 du` is the squared left-fiber Fourier budget. There is no `Delta` loss in this step.

The cross term is exactly

`2Y^TCZ = 2u^T L0 V`.

Two-dimensional Plancherel therefore gives

`|phi_Q(t)| <= pi sqrt(2) Delta^(-1/2)|t|^(-1) A(t)`.

Together with `|phi_Q|<=1`, Holder on the tail and the same optimized split as the 3x2 kernel-derivative theorem yield

`||p_Q||_infinity <= C_grp Delta^(-2/5)||a||^(-1/5)`,

with

`C_grp = 2^(2/5) * [5*6^(3/5)*2^(-11/10)]
       = 5*6^(3/5)*2^(-7/10)
       = 9.018613132839626...`.

Thus the whole arbitrary-width rank-two cross bank is paid before reciprocal physical-pair selection.

For a fixed left triple, Cauchy--Binet gives an exact aggregate identity. If `c_r` are the physical columns and `w_rs=c_r x c_s`, then all `w_rs` are parallel to `n` and

`sum_(r<s)||w_rs||^2 = Delta^2`,

so

`V1_L := sum_(r<s)||P w_rs||^2 = Delta^2 ||Pn||^2`.

Hence the grouped receiver may be written

`||p_Q||_infinity <= C_grp [Delta sqrt(V1_L)]^(-1/5)`.

This directly closes the diffuse stress family from fleet02/B09 r14 where `Delta=1`, `V1_L=1`, while every individual packet currency is `4/m^2` and tends to zero.

Remaining scale debt: the theorem is not a pure `V1_L^(-1/6)` estimate; if both `Delta` and the grouped currency `Delta sqrt(V1_L)` are small, another spectral/curvature exit is still needed.
