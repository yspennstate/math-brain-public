# Rigor addendum — slice representatives and rough-law passage

This addendum records two measure-theoretic details used in `REPORT.md` and does not change the theorem or constants.

## 1. Hyperplane slice Fourier identity

Fix a smooth cap-one product density `F=prod f_j`, an external slice value `l`, and `t!=0`. On the hyperplane `v·x=l`, write

`H_(l,t)(x)=exp(i 2 a t l xi·x) F(x)`.

For the regularised square phase `exp(i t gamma Z^2-epsilon Z^2)`, the one-dimensional Fresnel identity gives an integral in the dual square variable `q`. For every fixed `q`, the hyperplane Fourier-slice formula gives

`I_l(q)=(2 pi)^(-1) int_R exp(-isl) prod_j fhat_j(s v_j+q z_j+2atl xi_j) ds`.

The translated two-dimensional Brascamp--Lieb estimate of REPORT (5.7) proves

`int_R int_R prod_j |fhat_j(sv_j+qz_j+2atl xi_j)| ds dq <=(4 pi)^2`.

Consequently the right side is absolutely integrable in `(s,q)`. Fubini is legitimate, and the Fresnel damping can be removed by dominated convergence because the regularised Fresnel kernel has modulus at most its limiting constant times an extra Gaussian factor `<=1`. Thus the hyperplane slice has the representative used in REPORT (5.3)-(5.4), and

`|muhat_l(t)|<=4 sqrt(pi)|gamma t|^(-1/2)`.

The same absolute-integrability statement gives a continuous representative in `l` for the smoothed inputs, so the slice estimate can be taken for every `l` in that approximation rather than merely almost every `l`.

## 2. Passage from smooth inputs to arbitrary cap-one densities

Let `phi_epsilon` be a smooth probability approximate identity and set

`f_(j,epsilon)=f_j*phi_epsilon`.

Then `0<=f_(j,epsilon)<=1`, each has mass one, and

`||f_(j,epsilon)-f_j||_1 ->0`.

For fixed finite dimension, the product laws converge in total variation because

`||prod f_(j,epsilon)-prod f_j||_1 <= sum_j ||f_(j,epsilon)-f_j||_1`.

Apply the proved slice theorem and the fleet03/B05 r24 hub receiver to the smoothed product laws. The resulting **full output** interval estimate has the same universal constant for every `epsilon`. A deterministic pushforward contracts total variation, so the laws of the corresponding quadratic forms converge in total variation to the original output law. Therefore the interval estimate passes to every fixed interval without any pointwise convergence of conditional densities or slice representatives. Lebesgue differentiation then yields the stated essential `L^infinity` density bound for the original rough product law.

Thus no hidden output-continuity or conditional-density assumption is used in the rough-law passage.
