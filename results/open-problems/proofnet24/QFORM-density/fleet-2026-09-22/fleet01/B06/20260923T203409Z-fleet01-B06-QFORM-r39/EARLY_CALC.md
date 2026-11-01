SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T20:34:09Z.
attacking: the diagonal shared-index packet left by r38; retain the rank-one hub parabola and aggregate a transverse original-coordinate star before paying the outer physical square.

# Early calculation — transverse-star curved-fiber receiver

Let `X,Y` be independent cap-one variables and let `(U,V)=O(X,Y)` for a deterministic `O in O(2)`. For

`T=lambda U^2+alpha U+beta V+gamma`, `beta!=0`,

solve the level equation for `V`:

`v_t(u)=(t-gamma-lambda u^2-alpha u)/beta`.

Then

`p_T(t)=|beta|^(-1) int f_X(x(u)) f_Y(y(u)) du`,

where `(x(u),y(u))=O^T(u,v_t(u))`. Since

`x'(u)^2+y'(u)^2=1+v_t'(u)^2`,

partition the real line into `E_x={|x'|>=|y'|}` and `E_y=E_x^c`. On `E_x`, `|x'|>=1/sqrt(2)`. The map `u->x(u)` is a polynomial of degree at most two, so its multiplicity is at most two. The one-dimensional area formula gives

`int_(E_x) f_X(x(u))f_Y(y(u))du <=2sqrt(2)`.

The same bound holds on `E_y`. Therefore

`||p_T||inf <=4sqrt(2)/|beta|`.

This estimate is uniform in `lambda,alpha,gamma`; it uses the original product density directly and never treats `U,V` as independent.

Now suppose `Z` is an independent background product vector and

`S=lambda U^2+A(Z)U+2(n.Z+nu)V+R(Z)`, `n!=0`,

with arbitrary measurable `A,R`. Conditioning on `Z=z` and applying the preceding estimate gives

`||p_(S|Z=z)||inf <=2sqrt(2)/|n.z+nu|`.

Any probability density bounded by `M` has half-Riesz potential at most `4sqrt(M)`, hence

`H_(1/2)(S|Z=z) <=2^(11/4)|n.z+nu|^(-1/2)`.

Apply the completed fleet02/B06 product-projection theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` to `n.Z/||n||`: its density is at most `sqrt(e)`. Therefore `N=n.Z+nu` has density at most `sqrt(e)/||n||`, and the fractional bathtub inequality gives

`E|N|^(-1/2) <=2sqrt(2)e^(1/4)||n||^(-1/2)`.

Thus

`H_(1/2)(S) <=2^(17/4)e^(1/4)||n||^(-1/2)`.

If an additional original physical pivot gives

`Q=c(X_0+Psi)^2+S`, `c!=0`,

then the exact one-sided square kernel yields

`||p_Q||inf <=2^(17/4)e^(1/4)|c|^(-1/2)||n||^(-1/2)`.

This is scale-correct and independent of dimension, all support geometry, `lambda`, the longitudinal coefficient `A(Z)`, and the background remainder `R(Z)`.
