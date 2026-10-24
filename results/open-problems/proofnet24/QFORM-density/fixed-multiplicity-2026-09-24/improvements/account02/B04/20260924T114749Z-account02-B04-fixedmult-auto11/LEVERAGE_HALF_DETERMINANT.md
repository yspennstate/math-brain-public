# QFORM-LEVERAGE-HALF-DETERMINANT-v1

Status: proved supporting improvement; **not** an unconditional reduction of the 17-eigenvalue theorem.

Pinned baseline manuscript: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Let `X_I,X_J` be disjoint original-coordinate product banks with coordinate densities at most one, let `F,G` be arbitrary real measurable within-bank terms, and

`Z = F(X_I) + 2 X_I^T M X_J + G(X_J)`.

Write the rows of `M` as `m_i^T` and define physical row leverages

`ell_i = m_i^T (M^TM)^dagger m_i`,

with zero leverage on a zero row.

## Theorem

If `max_i ell_i <= 1/2`, then for every real `t`,

`|phi_Z(t)| <= det(I + t^2 M^TM/(2*pi^2*e^2))^(-1/4)`.

Consequently, if

`Z_3(M) = sum_{|S|=|T|=3} det(M_{S,T})^2 > 0`,

then `Z` has a bounded continuous density and

`||p_Z||_infinity <= 3*sqrt(2)*e*Z_3(M)^(-1/6)`.

## Proof

The baseline manuscript's second-power decoupling inequality gives

`|phi_Z(t)|^2 <= E_D prod_i |hat f_i(2t(MD)_i)|`,

where `D=X_J-X'_J` has independent coordinate densities at most one.

Put `a=2t`,

`alpha=(2*pi*e*sqrt(2))^2=8*pi^2*e^2`,

`H=alpha I + a^2 M^TM`,

and define the same geometric-frame weights as in the manuscript:

`c_j=alpha e_j^T H^{-1}e_j`,

`d_i=a^2 m_i^T H^{-1}m_i`.

The frame identity is unchanged and `theta=sum_i d_i=sum_j(1-c_j)`. Spectral calculus on the row space gives

`d_i <= m_i^T(M^TM)^dagger m_i = ell_i <=1/2`.

Apply the geometric rank-one Brascamp--Lieb theorem after `x=H^{-1/2}z`, but now use row functions `h_i(u)=|hat f_i(u)|`, not their squares. The coordinate difference-density factors give `L^{1/c_j}` norm at most one exactly as in the baseline proof. Since `p_i=1/d_i>=2`, the baseline scalar Fourier-power lemma yields

`||h_i||_{1/d_i}
 = (int |hat f_i(u)|^(1/d_i) du)^(d_i)
 <= (2*pi*sqrt(2e*d_i))^(d_i)`.

The row Jacobian contributes `d_i^(-d_i/2)`, so the `d_i` powers cancel. The coordinate entropy factor obeys

`prod_j c_j^(-c_j/2) <= e^(theta/2)`.

Therefore the total scalar factor is

`[(2*pi*sqrt(2e))*sqrt(e)/sqrt(alpha)]^theta
 = [2*pi*e*sqrt(2)/sqrt(alpha)]^theta
 =1`.

Thus the Brascamp--Lieb integral is at most

`det(I+a^2M^TM/alpha)^(-1/2)`.

Taking the square root required by second-power decoupling proves

`|phi_Z(t)| <= det(I+t^2M^TM/(2*pi^2*e^2))^(-1/4)`.

By Cauchy--Binet,

`det(I+zM^TM) >= z^3 Z_3(M)`.

Hence

`|phi_Z(t)| <= min(1,(u/|t|)^(3/2))`,

where

`u=sqrt(2)*pi*e*Z_3(M)^(-1/6)`.

The baseline power-envelope lemma with exponent `3/2` gives

`||p_Z||_infinity <= [u*(3/2)]/[pi*(1/2)] = 3u/pi
 = 3*sqrt(2)*e*Z_3(M)^(-1/6)`.

The envelope is integrable, so Fourier inversion also gives continuity for this branch.

## Scope and threshold consequence

This theorem upgrades the baseline determinant exponent from `-1/8` to `-1/4` on a literal physical crossing whose row leverage is at most one-half. It makes **order-three crossing volume directly density-integrable** rather than merely sufficient for a negative-half-potential estimate.

If a no-pivot `s_9>=1` matrix supplied a random-cut crossing satisfying both the baseline lower bound `Z_3>=4^{-3} kappa^3` and this leverage cap, the resulting density bound would be

`||p_Q||_infinity <= 480*sqrt(2)*e`.

But the baseline random-cut argument controls only `Z_3`, not row leverage. No-pivot alone does not rule out high-leverage/star-like physical rows. Therefore this result does **not** prove a nine-eigenvalue theorem. The next structural obligation is a dichotomy: either extract a target-scale order-three crossing with maximum row leverage at most one-half, or route the complementary high-leverage case through another product-preserving receiver.
