SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-23T11:28:21Z.
attacking: a distribution-domain L^p-L^q replacement for pointwise Fresnel decay: one diffuse rank-one bilinear bank plus one source-disjoint grouped square, with exact signed-Fejer transfer.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

This run changes mechanism after the preceding rank-two-cross sequence. The proposed packet is

\[
Q_c=F_c(X_I)+(2\gamma U b+d(c))^T X_J+\lambda Z^2+r(c),
\quad U=a^TX_I+h(c),\quad Z=z^TX_D+k(c),
\]

on disjoint original-coordinate banks `I,J,D,C`, conditioned on `X_C=c`. Put
\[
\kappa=|\gamma|\|a\|_2\|b\|_2,\qquad
\rho=|\lambda|\|z\|_2^2.
\]
No J-side quadratic self-curvature is included in this packet; that is an explicit boundary.

For `0<beta<1`, a probability density bounded by `m` satisfies, uniformly in the translation `s`,
\[
\mathbb E|Y-s|^{-\beta}\le { (2m)^\beta\over 1-\beta}.
\]
The proof is layer cake with `P(|Y-s|<r)<=min(1,2mr)`.

For `p>1`, `beta=(p-1)/p`, conditioning on `X_I` and using the product-projection density cap on the untouched original J-bank gives
\[
\|p_{F_c(X_I)+(2\gamma Ub+d)^TX_J}\|_p
\le p\,2^\beta\,\kappa^{-\beta}.
\]
Indeed `||2 gamma U b+d|| >= 2|gamma|||b|| |U-u_0|`, while `U` has density cap at most `sqrt(2)/||a||`.

For `p>2`, `q=p/(p-1)`, if `Z` has density cap `m`, then
\[
\|p_{\lambda(Z+s)^2}\|_q
\le 2^{1/p}\left({p-1\over p-2}\right)^{(p-1)/p}
 m^{2/p}|\lambda|^{-1/p}.
\]
With the product-projection cap `m<=sqrt(2)/||z||`, this becomes
\[
\|p_{\lambda Z^2}\|_q
\le 2^{2/p}\left({p-1\over p-2}\right)^{(p-1)/p}\rho^{-1/p}.
\]

Young's inequality therefore gives the conditional and unconditional density bound
\[
\|p_Q\|_\infty\le K_p\kappa^{-(p-1)/p}\rho^{-1/p},
\]
where
\[
K_p=p\,2^{1+1/p}\left({p-1\over p-2}\right)^{(p-1)/p}.
\]
The clean specialization `p=3` is exact:
\[
\boxed{\|p_Q\|_\infty\le 12\,\kappa^{-2/3}\rho^{-1/3}.}
\]
Because the two factors lie in conjugate finite `L^p,L^q`, their convolution belongs to `C_0`; dominated convergence over `c` preserves a continuous `C_0` representative.

For the pure grouped form
\[
Q=2\gamma(a^TX_I)(b^TX_J)+\lambda(z^TX_D)^2,
\]
the nonzero spectrum is exactly `{-kappa,+kappa,lambda||z||^2}`. Thus `kappa>=1,rho>=1` is a genuine target-valid rank-three class. With normalized all-ones vectors on three growing blocks and `gamma=lambda=1`, its spectrum is `{-1,1,1}`, every diagonal is at most `1/m`, and every physical 2x2 principal determinant is at most `1/m^2`: it lies in the no-pivot N3 regime for every fixed threshold once `m` is large, while the proposed bound stays `12`.

Remaining tasks before finalization: write the full proof with density-existence details, preserve the phase-aligned scalar counterexample, apply account04/B01's completed exact signed-Fejer identity to this inequality, run deterministic algebra/spectrum checks, refresh controls/corrections, and read back the final commits.
