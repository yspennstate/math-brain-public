# Rigor check — fleet03/B15 affine fixed-instance regularity

Run: `20260924T092642Z-fleet03-B15-qform-auto11`.

## 1. Affine critical set

For `q(x)=x^T A x+b^Tx+c`, `grad q=2Ax+b`. If the equation `2Ax=-b` has no solution, the critical set is empty. If it has a solution `x0`, the full solution set is `x0+ker A`. When `A!=0`, this is a proper affine subspace and is Lebesgue-null. When `A=0,b!=0`, the gradient is constant nonzero. Thus every nonconstant affine quadratic has a null critical set. The coarea null-set proof of absolute continuity is therefore valid.

## 2. Coordinate scaling

For `T_m=diag(1,...,m,...,1)` and `X=T_mY`,

`X^TAX=Y^T(T_mAT_m)Y`,

`b^TX=(T_mb)^TY` because `T_m` is symmetric. Hence the scaled affine vector is exactly `T_mb`; there is no reciprocal factor.

If a coordinate subdensity `g` has mass `m` and `h=g/m`, while `X_j~h`, then `Y_j=X_j/m` has density

`m h(my)=g(my)<=1`

and total mass one. Therefore the normalized affine output is exactly a cap-one product instance of `(A_m,T_mb,c)`.

## 3. Square-root submass and signed difference

The affine-uniform scaled certificate is

`P(q_m(Y) in I)<=K(A,j)m^(-1/2)|I|`.

Multiplication by the original submass gives height

`m*K*m^(-1/2)=K sqrt(m)`.

For probability densities `f,g`, let `delta=||f-g||_1`. Since `int(f-g)=0`,

`int(f-g)_+ = int(g-f)_+ = delta/2`.

Also `(f-g)_+<=f<=1` and `(g-f)_+<=g<=1`. Thus the two signed subpushforwards each have height at most `K sqrt(delta/2)`, so

`||p_f-p_g||_infinity <=2K sqrt(delta/2)=sqrt(2)K sqrt(delta)`.

Because `delta<=2`, the required submass condition `m<=1` always holds.

## 4. Smooth affine C0 anchor

Write `b=b_R+b_K` with `b_R in Range(A)`, `b_K in ker A`, and `h=(1/2)A^dagger b_R`. Since `Ah=b_R/2`, substituting `x=y-h` cancels the range-affine term and leaves

`q(y-h)=y^TAy+b_K^Ty+constant`.

If `b_K=0`, the already proved smooth fixed-rank quadratic `C_0` theorem applies.

If `b_K!=0`, choose orthogonal coordinates with `z_1` parallel to `b_K` inside `ker A`. Then

`q(y,z)=y^TLambda y+beta z_1+constant`, `beta=|b_K|>0`.

For smooth compact amplitude `F_tilde`, integrating the delta constraint in `z_1` gives

`p(t)=|beta|^{-1} int F_tilde(y,z',(t-c-y^TLambda y)/beta) dy dz'`.

The projected `(y,z')` integration domain can be restricted to the compact projection of `supp F_tilde`; the integrand is uniformly bounded and continuous in `t`. Dominated convergence proves continuity. The image of a compact support under `q` is compact, so the density has compact support. Thus `p in C_c subset C_0`.

No independence is used after this orthogonal coordinate change.

## 5. Uniform-limit identification

For cap-preserving smooth compact marginal approximants `f_{j,k}`, the multi-marginal estimate gives

`||p_k-p_l||_infinity <= sqrt(2) sum_j K(A,j)||f_{j,k}-f_{j,l}||_1^(1/2) ->0`.

So `p_k` converges uniformly to some `p in C_0`, since `C_0(R)` is closed in the sup norm.

The product laws converge in total variation, hence their deterministic pushforwards converge in total variation. On every bounded interval `I`, uniform convergence implies `int_I p_k -> int_I p`, while total variation gives `mu_k(I)->mu(I)`. Therefore `mu(I)=int_I p`. A monotone-class argument extends equality from bounded intervals to all Borel sets. Thus `p` is the target density.

## 6. Partner family algebra

For

`H=[[aI_2,R],[R^T,-aI_m]]`,

direct multiplication gives

`H^2=diag(a^2I_2+RR^T, a^2I_m+R^TR)`

because the off-diagonal blocks are `aR-aR=0`. Hence every singular value/eigenvalue modulus of symmetric `H` is at least `a`, so `H` is invertible and `rank H=m+2>=3`.

For `h=(1/2)H^{-1}b`,

`(X+h)^T H(X+h)+c-h^THh = X^THX + 2h^THX+c = X^THX+b^TX+c`.

The partner interval constant `2pi/a` therefore survives every affine perturbation by coordinate translation of the input laws.

Finally, with Fourier convention `phi(t)=int e^{itx}p(x)dx`, Plancherel gives

`int |phi(t)|^2 dt =2pi int p(x)^2 dx <=2pi ||p||_infinity ||p||_1 <=4pi^2/a`.

All constants and signs in the report agree with these identities.

## 7. Scope audit

The report does not claim a target-uniform `K(A,j)`, a uniform continuity modulus, pointwise oscillatory decay, bounded support diameter, finite fragment count, moments, log-concavity, Gaussianity, or independence after spectral rotation. It leaves the universal QFORM height theorem open.
