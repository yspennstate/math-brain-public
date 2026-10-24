SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-24T05:28:09Z.
attacking: QFORM-PUNCTURED-MAJORITY-ROOT-NUMERATOR-v1 by keeping the untouched physical hub density inside the exact root numerator and recovering the order-one star before any positive-discriminant majorant.

# Early calculation: star-preserving Fresnel-Plancherel

Programme `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

Let `H` be an original-coordinate source, independent of a product bank `X`, all scalar densities at most one. Let `a != 0`, `b != 0`, and let `S` be any real symmetric matrix on the `X` bank. Consider

`Q = a ( H + b^T X/a )^2 + X^T S X`.

Put `c=b/a`. Fresnel linearisation of the displayed completed square gives, for `t != 0`,

`|phi_Q(t)| <= (4*pi*|t*a|)^(-1/2) int |psi_H(xi)| |F_t(xi)| dxi`,

where

`F_t(xi)=E_X exp(i*t*X^T*S*X + i*xi*c^T*X)`.

By Plancherel, `||psi_H||_2^2 = 2*pi*||f_H||_2^2 <= 2*pi`. The function `F_t` is the Fourier transform of the complex pushforward measure of `exp(i*t*X^T*S*X) prod_j f_j(X_j)dX` under `c^T X`; its density `h_t` obeys pointwise `|h_t| <= p_{c^T X}`. The one-dimensional product-projection density theorem gives

`||p_{c^T X}||_infinity <= sqrt(2)/||c||_2`.

Hence

`||F_t||_2^2 = 2*pi ||h_t||_2^2 <= 2*pi*sqrt(2)/||c||_2`.

Cauchy-Schwarz therefore yields the exact uniform-in-`S` estimate

`|phi_Q(t)| <= 2^(1/4)*sqrt(pi) * ||b||_2^(-1/2) * |t|^(-1/2).`

The small physical pivot `a` cancels completely. This is the source information erased by replacing the exact hub-root numerator by the cap `1`.

For the newest account03/B16 r41 collar, `||b||>=rho>=s*sqrt(62/63)`, so

`|phi_Q(t)| <= 2^(1/4)*sqrt(pi)*(63/62)^(1/4) s^(-1/2)|t|^(-1/2) < 2.117 s^(-1/2)|t|^(-1/2).`

This is not an `L^1_t` bound and therefore does not close the density. It does, however, remove the puncture singularity at `a=0` while retaining the literal source density. Combining it with the pinned fractional-potential lemma gives a uniform quarter-potential bound; the remaining debt is to extract one further phase-sensitive half/quarter power from the indefinite Schur plane without replacing the projected pair by independent coordinates.
