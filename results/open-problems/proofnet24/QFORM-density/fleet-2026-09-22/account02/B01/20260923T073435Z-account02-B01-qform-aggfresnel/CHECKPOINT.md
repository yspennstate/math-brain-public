# QFORM B01 checkpoint — grouped rank-two coefficient plus receiver Fresnel packet

Run: `20260923T073435Z-account02-B01-qform-aggfresnel`.


## Substantive checkpoint

Let original independent coordinates split into disjoint banks `I,J` (all other coordinates may be conditioned). Assume the exact cross matrix `K=A_{IJ}` has rank two, with nonzero singular values `kappa1,kappa2` and `Delta=kappa1*kappa2`. Let `V` be an orthonormal basis of `range(K^T)`. Suppose the `J`-self block is

`D + R Lambda R^T`,

where `D` is diagonal, `R` has `r` orthonormal columns, `Lambda` is invertible diagonal, and `[V R]` has full column rank. Put

`Omega^2 = det(R^T (I - V V^T) R)`

(with `Omega=1` for `r=0`), `S=span(V,R)`, and assume every physical-coordinate leverage of `S` is at most `1/2`.

For a quadratic form of the shape

`Q = H(X_I) + 2 X_I^T K X_J + X_J^T(D+R Lambda R^T)X_J + b^T X_J + c`,

with completely arbitrary measurable real `H` and arbitrary affine `b,c`, the source Fresnel identity plus a two-dimensional product-projection density cap and geometric Brascamp--Lieb give the candidate bound

`|phi_Q(t)| <= min(1, B_r |t|^{-(2+r/2)})`,

`B_r = (4*pi)^(2+r/2) / [2 Delta Omega sqrt(|det Lambda|)]`.

Indeed, `A=K^T X_I` has planar density cap `2/Delta`. After Fresnel-linearising the `r` receiver squares, average `|F_t(A)|` over this density, change variables `s=2tA`, and use the volume map `(s,u)->s+Ru`, whose Jacobian is `Omega`. The remaining integral is over the `(2+r)`-dimensional subspace `S` of a product of twisted one-dimensional Fourier transforms. With row leverage `ell_j<=1/2`, geometric BL and the source lemma `int |g_hat|^p <=4*pi/sqrt(p)` yield exactly `(4*pi)^(2+r)` for that subspace integral.

Integrating the displayed characteristic-function envelope gives

`||p_Q||_infinity <= 4(r+4)/(r+2) * [2 Delta Omega sqrt(|det Lambda|)]^(-2/(r+4)).`

For `r=1` this is

`||p_Q||_infinity <= [20/(3*2^(2/5))] (Delta Omega sqrt(|lambda|))^(-2/5) < 5.053 (Delta Omega sqrt(|lambda|))^(-2/5).`

This is a joint averaged-frequency statement. It never asserts law-uniform pointwise decay for a scalar quadratic phase, so the phase-aligned-density refutation remains intact.

## Endpoint partner application

When `r=0`, the same setup is exactly a one-sided-affine rank-two cross packet. The completed account03/B01 determinant-area theorem gives the sharper, leverage-free actual inequality

`||p_Q||_infinity <= 2*sqrt(pi) Delta^(-1/2)`.

The present Fourier calculation would only give `4*sqrt(2) Delta^(-1/2)` under the leverage gate. Thus the new calculation is complementary: it spends one or more genuinely transverse receiver Fresnel directions; the designated partner pays the zero-Fresnel endpoint.

Remaining work before final report: audit constants/signs and the affine-translation invariance carefully; build an exact strict-N3 target family with dense arbitrary curvature on the conditioned bank and one transverse receiver square; refresh live corrections/partner state before publication.
