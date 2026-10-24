# Leverage-interpolated order-four endpoint

Source manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

For
\[
Z=F(X_I)+2X_I^TMX_J+G(X_J)
\]
with original independent cap-one coordinates, let
\[
\ell_i=m_i^T(M^TM)^\dagger m_i
\]
be the ordinary leverage of row `i` of `M`.

## Theorem

If `1<=q<2` and `max_i ell_i<=q/2`, then
\[
|\phi_Z(t)|\le
\det\!\left(I+\frac{q t^2}{2\pi^2e^2}M^TM\right)^{-1/(4q)}.
\]
The transposed statement holds under the analogous column-leverage hypothesis.

Indeed, raise the manuscript's unsquared decoupling bound to `q` and use Jensen. With
\[
\alpha=(2\pi e)^2\frac2q,
\quad H=\alpha I+(2t)^2M^TM,
\quad d_i=(2t)^2m_i^TH^{-1}m_i,
\]
SVD gives `d_i<=ell_i<=q/2`. Therefore the scalar Fourier-power lemma applies at exponent `q/d_i>=2`. The graph Brascamp--Lieb factors cancel exactly after this choice of `alpha`, leaving the determinant above.

Consequently, for crossing volume `Z_k(M)`,
\[
|\phi_Z(t)|\le
\min\left\{1,
\left(\frac{\pi e\sqrt{2/q}\,Z_k(M)^{-1/(2k)}}{|t|}\right)^{k/(2q)}
\right\}.
\]
For `k=4`,
\[
\|p_Z\|_\infty\le
\frac{2e\sqrt{2/q}}{2-q}Z_4(M)^{-1/8}.
\]

## Thirteen-eigenvalue corollary under a diffuse-leverage cut

In the normalized no-pivot `s_13(A)>=1` branch, the manuscript's spectral-to-volume proposition at `k=4` and random-cut lemma give a physical cut with
\[
Z_4(M)\ge4^{-4}\kappa^4,
\qquad Z_4(M)^{-1/8}\le160.
\]
If one volume-good cut has either row- or column-leverage maximum at most `3/4`, choose `q=3/2` to obtain
\[
|\phi_Q(t)|\le
\det\!\left(I+\frac{3t^2}{4\pi^2e^2}M^TM\right)^{-1/6}
\]
and
\[
\|p_Q\|_\infty\le\frac{8e}{\sqrt3}Z_4(M)^{-1/8}
\le\frac{1280e}{\sqrt3}<2009.
\]
All pivot branches of the manuscript already close under `s_13>=1`, with the scalar branch bounded by `6010`. Hence this explicit diffuse-leverage subclass satisfies
\[
\|p_Q\|_\infty\le6010K^2/s.
\]

The remaining order-four obstruction is therefore the physical two-sided near-coloop regime: every volume-good cut has both row and column maximum leverage tending to one. No rotated random variables are treated as independent and no coefficient tail is deleted.
