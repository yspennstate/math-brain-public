# account01/B06 r25 early substantive checkpoint

Run `20260923T053749Z-account01-B06-QFORM-r25`. Full QFORM remains open. Execution label: `WITHOUT_VERIFIED_BRAIN`.

## Heavy-right-plane hub: exact physical completion

Continue from account01/B06 r24, in the exact-rank-three zero-Schur-diagonal survivor

`kappa<1/3, x^2<1/6, y^2>1/2`,

with right-bank orthonormal pair `(q,v)`, `h_R=beta v + m q`, `m=rho y`, and a physical right coordinate `r` of plane leverage

`ell_r=q_r^2+v_r^2>1/2`.

Write `T=R\{r}`, `H=h_T.X_T`, `V=v_T.X_T`, and let `xi` denote the left/outside square centre. If `h_r!=0`, the exact identity

`(1/a)(h_r X_r+H+xi)^2 + 2 sigma U(v_r X_r+V)`

`= (h_r^2/a)(X_r+S)^2 + 2 sigma U Z + F(Omega)`

holds with

`S=(H+xi)/h_r + a sigma v_r U/h_r^2`,

`Z=[v_T-(v_r/h_r)h_T].X_T`,

`F(Omega)=-2 sigma(v_r/h_r)U xi-a sigma^2(v_r^2/h_r^2)U^2`.

Thus all residual right-bank dependence stays only in the arbitrary square centre `S` and in the single scalar projection `Z`; the remainder `F` is independent of the right bank.

The exact exterior identity is

`|h_r| ||v_T-(v_r/h_r)h_T|| = m sqrt(ell_r)`.

Indeed `h=beta v+m q` gives, for `k!=r`,

`h_r v_k-v_r h_k=m(q_r v_k-v_r q_k)`,

and orthonormality of `(q,v)` gives

`sum_{k!=r}(q_r v_k-v_r q_k)^2=q_r^2+v_r^2=ell_r`.

## Product-weighted curved kernel to prove

The required scalar/dependent-centre extension is:

If a cap-one scalar `X` is independent of two independent original-coordinate product banks `Omega,Y`, `U=U(Omega)` has density cap `L`, `Z=Z(Y)` has density cap `K`, while `S(Omega,Y)` and `F(Omega)` are arbitrary, then

`T=A(X+S)^2+2d U Z+F`

should satisfy

`||p_T||_infinity <= 4 sqrt(LK)/sqrt(|A d|)`.

The intended proof keeps the one-sided square kernel, integrates `Z` with its true marginal density cap, then averages the surviving `|U|^{-1/2}` singularity against the true `U` density. No spectral-fiber supremum is taken.

Applying account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` to the unit projections `U` and `Z/||Z_coeff||` gives the actual caps `L,K<=sqrt(e)`. Combined with the exact completion above this would yield

`||p_Q||_infinity <= 4 sqrt(e) [ |a|/(|sigma| m |h_r| sqrt(ell_r)) ]^(1/2)`.

With `tau=|h_r|/rho`, `m=rho y`, and the earlier exact spectral inequality `(rho^2/|a|)|sigma|>=s_3(A)^2`, this becomes

`||p_Q||_infinity <= 4 sqrt(e)/[s_3(A) sqrt(y tau sqrt(ell_r))]`.

Since the live survivor has `y^2>1/2` and `ell_r>1/2`, the subbranch `tau>=1/8` would be paid by

`||p_Q||_infinity < 16 sqrt(e)/s_3(A) < 26.38/s_3(A)`.

The remaining branch would therefore have a heavy right-plane hub with the additional near-null condition `|h_r|<rho/8`.

This checkpoint records the first substantive implication before the full proof and source refresh. It is not yet the final theorem claim.
