# account02/B01 r36 substantive checkpoint

Run: `20260923T040531Z-account02-B01-qform-r36`

Status: supporting analytic step / explicit obstruction. Full QFORM remains OPEN.

## Two-bank rank-two half-Riesz endpoint

Let the original independent coordinates be split into disjoint banks `I,J,K`. After conditioning `K`, write

\[
R=F(X_I)+2X_I^T M X_J+G(X_J)+c,
\]

where `F,G` are arbitrary real measurable phases (in QFORM they contain all same-bank quadratic curvature and all affine leakage), and suppose the physical cross block `M` has exact rank two with nonzero singular values \(\sigma_1,\sigma_2\).

Take an SVD \(M=U\Sigma V^T\), with \(\Sigma=\operatorname{diag}(\sigma_1,\sigma_2)\), and put \(Y=U^TX_I, Z=V^TX_J\). The two-dimensional product-projection theorem gives density caps \(\|p_Y\|_\infty,\|p_Z\|_\infty\le2\). The complex pushforwards of \(e^{itF}d\mu_I\) and \(e^{itG}d\mu_J\) to `Y,Z` therefore have densities `h_t,k_t` satisfying \(|h_t|\le p_Y, |k_t|\le p_Z\), hence \(\|h_t\|_2,\|k_t\|_2\le\sqrt2\).

With Fourier convention \(\widehat k(\xi)=\int e^{i\xi\cdot z}k(z)dz\),

\[
\phi_R(t)=\iint h_t(y)k_t(z)e^{i2t y^T\Sigma z}\,dy\,dz.
\]

Cauchy--Schwarz and two-dimensional Plancherel give

\[
|\phi_R(t)|\le {\pi\over |t|\sqrt{\sigma_1\sigma_2}}\|h_t\|_2\|k_t\|_2
\le {2\pi\over |t|\sqrt{\sigma_1\sigma_2}}.
\]

Thus the false scalar law-uniform Fresnel envelope is not used; the decay comes from a joint two-bank bilinear receiver. Combining with `|phi|<=1` and the source fractional-potential identity

\[
|x|^{-1/2}=\sqrt{2/\pi}\int_0^\infty t^{-1/2}\cos(tx)dt
\]

yields

\[
\boxed{\sup_s\mathbb E|R-s|^{-1/2}\le8(\sigma_1\sigma_2)^{-1/4}.}
\]

The integral is exact at the envelope level: if \(K=2\pi(\sigma_1\sigma_2)^{-1/2}\), then
\(\int_0^\infty t^{-1/2}\min(1,K/t)dt=4\sqrt K\).

This is an averaged/weighted-frequency endpoint. It tolerates arbitrary self-curvature on BOTH active grouped banks.

## Why this cannot be upgraded to a density bound using only rank-two cross currency

Let independent \(x_1,x_2,y_1,y_2\sim\operatorname{Unif}[-1/2,1/2]\) and

\[
R=(x_1+y_1)^2-(x_2-y_2)^2.
\]

The `I-J` cross block is exactly \(I_2\), so \(\sigma_1=\sigma_2=1\). But \(Z=x_1+y_1\) has density \(1-|z|\) on `[-1,1]`, and \(Z^2\) has density \(h(w)=w^{-1/2}-1\) on `(0,1)`. Hence

\[
p_R(0)=\int_0^1 h(w)^2dw=\infty.
\]

So arbitrary self-curvature on both banks genuinely destroys any direct bounded-density theorem based only on a rank-two cross block. This is NOT a QFORM counterexample: the coefficient matrix has only two large eigenvalues, \(2,-2\). The half-Riesz endpoint above is therefore the correct currency to spend against a third curvature packet.

## Strict-N3 full-target stress family repaired by a third grouped square

Take five disjoint banks of size `m` and normalized bank sums `A,B,C,D,W`. Define

\[
Q_m=(A+C)^2-(B-D)^2+W^2.
\]

Its nonzero spectrum is exactly \(\{2,-2,1\}\); every physical diagonal has absolute value `1/m`, and every physical `2x2` principal determinant has absolute value at most `1/m^2`. Thus for every fixed no-pivot threshold this family lies in strict N3 for large `m`.

The bicore \(R_m=(A+C)^2-(B-D)^2\) has a rank-two `I-J` cross block with singular values `1,1`, hence \(H_{1/2}(R_m)\le8\). The independent normalized grouped sum `W` has one-dimensional product-projection density cap at most \(\sqrt2\), so `W^2` has density at most \(\sqrt2\,u^{-1/2}`. Therefore

\[
\boxed{\|p_{Q_m}\|_\infty\le8\sqrt2<11.314}
\]

uniformly in `m` and in all cap-one input laws.

Remaining debt: extract, from arbitrary N3, either a product-preserving rank-two bicore with quantitative singular product plus a third curvature packet to spend this half-Riesz bound, or route to an already-paid volume/hub/pair/physical-block branch.
