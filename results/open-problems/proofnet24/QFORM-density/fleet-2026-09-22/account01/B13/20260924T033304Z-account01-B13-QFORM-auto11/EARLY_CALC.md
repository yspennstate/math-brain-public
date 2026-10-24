# account01/B13 early calculation — transverse diagonal rigidity inside the two-strip chamber

Run: `20260924T033304Z-account01-B13-QFORM-auto11`

Full QFORM status: OPEN. This note records the first substantive calculation only.

Fresh compatible input is account03/B13 r41 as consumed by account02/B13 r40. In the hard exact-rank-two chamber write

\[
A=D+U\Lambda U^\top,\qquad U^\top U=I_2,
\]

choose the r41 pivot `k` with `|d_k|>=1`, rotate only the deterministic latent two-frame so

\[
u_k=(\sqrt c,0),\qquad u_i=(x_i,y_i),\quad s_i=y_i^2,
\quad t_i=x_i/y_i\ (s_i>0).
\]

For every low-leverage transverse pair (`c_i,c_j<=1/4`, `s_i s_j>0`) r41 proves

\[
|\tau_{ij}|<C_*\rho^{-1},\qquad
C_*={2278125\over256e^2}=1204.338641107064\ldots,
\]

where

\[
\tau_{ij}=d_kq_{ij}+d_iq_{kj}+d_jq_{ki}.
\]

Put

\[
G_{ij}={\tau_{ij}\over s_is_j}
=d_k(t_i-t_j)^2+a_i+a_j,
\qquad a_i={c d_i\over s_i}.
\]

At the r41 transverse threshold `s_i>=alpha=rho^{-1/3}`, every pair obeys

\[
|G_{ij}|<\epsilon:=C_*\rho^{-1/3}.
\]

The exact four-point identity is

\[
G_{ij}+G_{\ell m}-G_{i\ell}-G_{jm}
=-2d_k(t_i-t_m)(t_j-t_\ell).
\]

Ordering `M>=4` transverse slopes and taking `(i,m,j,ell)=(1,M-1,M,2)` yields

\[
(t_{M-1}-t_1)(t_M-t_2)
\le {2\epsilon\over |d_k|}.
\]

Hence after deleting at most one transverse outlier there is a slope interval of length

\[
w_k=\sqrt{{2C_*\over |d_k|}}\rho^{-1/6}
=49.07827709093\,|d_k|^{-1/2}\rho^{-1/6}.
\]

For every surviving pair,

\[
|a_i+a_j|
\le |G_{ij}|+|d_k||t_i-t_j|^2
\le 3C_*\rho^{-1/3}.
\]

If at least three transverse rows survive, then

\[
2a_i=(a_i+a_j)+(a_i+a_\ell)-(a_j+a_\ell),
\]

so

\[
|a_i|\le {9\over2}C_*\rho^{-1/3}.
\]

Therefore the actual diagonal coefficients on the transverse bank satisfy the aggregate identity/inequality

\[
|c d_i|\le {9\over2}C_*s_i\rho^{-1/3},
\qquad
c\sum_{i\in B_1}|d_i|
\le {9\over2}C_*\rho^{-1/3}
=5419.523884982\,\rho^{-1/3},
\]

because `sum_i s_i<=1`. Thus, after finitely many physical centers, arbitrary distributed diagonal curvature can persist freely only in the near-pivot strip; on the transverse strip its coefficient trace mass is quantitatively forced small after multiplication by the pivot leverage `c`. The small diagonal tail is retained exactly; it is not treated as a small random perturbation.

The same calculation sharpens the transverse projective tube to

\[
\operatorname{dist}(u_i,\ell_1)
\le {1\over2}w_k
=24.53913854547\,|d_k|^{-1/2}\rho^{-1/6}.
\]

If fewer than four transverse rows exist, they are a finite-center endpoint and may be included in the center set before applying the account02/B13 finite-center conditioning theorem.

Next: combine this with the exact center-induced affine alignment
`b_B=2U_B Lambda U_E^T y` and the optimizer-free finite-mixture product-indicator reduction; then write the complete source-pinned theorem and remaining receiver.
