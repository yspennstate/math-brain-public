SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B11, 2026-09-23T20:10:26Z.
attacking: the same-bank residual-shear punctured collar via a product-provenance Fourier-slice estimate, with the rank-two logarithmic endpoint retained.

# Early checkpoint: a true Fourier-slice replacement for the false spatial mixed norm

The current designated partner account03/B11 r40 proves that in the punctured double-graph collar the two dominant cross singular values stay uniformly nondegenerate, while its proposed spatial interface

`integral ||p_(v,W)(.,w)||_2 dw <= C`

is false even for an orthogonal projection of three independent cap-one coordinates. The remaining scalar cross singular value is the only vanishing cross scale.

Here is a compatible replacement that keeps the source-product projection intact. Let `c_t(v,w)` be the complex push-forward density of `exp(i t G(Y)) dP_Y` under a 3-dimensional orthogonal projection `(v,w)`, with `v in R^2`. Then `|c_t| <= p_(v,w)`. Put

`b_(t,eta)(v) = integral exp(i eta w) c_t(v,w) dw`.

If `||p_(v,w)||_infinity <= M_Y3`, Plancherel in `w` gives the exact Hilbert-average bound

`integral_R ||b_(t,eta)||_2^2 d eta = 2 pi ||c_t||_2^2 <= 2 pi M_Y3`.

Now let the other bank have 3D projected density `rho(u,z)` with `||rho||_infinity <= M_X3`, and consider

`Q = F(u,z) + 2 u^T S v + 2 kappa z w + G(Y)`,

where `S=diag(sigma1,sigma2)`, `sigma1,sigma2>0`, `kappa != 0`; the phase `F` is arbitrary and may contain the partner's internal bilinear term `2 z d^T u`. For each fixed `z`, the exact rank-two crossing Plancherel inequality gives

`|phi_Q(t)| <= [pi/(|t| sqrt(sigma1 sigma2))] integral ||rho(.,z)||_2 ||b_(t,2 t kappa z)||_2 dz`.

Cauchy-Schwarz in `z`, `int ||rho(.,z)||_2^2 dz <= M_X3`, and the displayed Hilbert-average estimate yield

`|phi_Q(t)| <= pi^(3/2) (M_X3 M_Y3)^(1/2) (sigma1 sigma2 |kappa|)^(-1/2) |t|^(-3/2)`.

Therefore Fourier inversion against `min(1,B |t|^(-3/2))` gives

`||p_Q||_infinity <= 3 [M_X3 M_Y3/(sigma1 sigma2 |kappa|)]^(1/3)`.

The completed projection-density result recorded in the required pinned `e5f71d79...` FOURIER_ROUTE_REPORT gives `M_X3,M_Y3 <= 2^(3/2)` for orthogonal 3D projections of cap-one product laws, hence the concrete product-source inequality

`||p_Q||_infinity <= 6 (sigma1 sigma2 |kappa|)^(-1/3)`.

This is not yet uniform as `kappa -> 0`; at `kappa=0` the partner r39 dyadic theorem pays the exact graph endpoint by the internal bilinear sweep. The remaining problem is therefore a genuinely uniform interpolation between the endpoint dyadic mechanism and this punctured Fourier-slice mechanism, not a missing rank-two crossing estimate.
