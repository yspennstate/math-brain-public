# Addendum: isotropic Gaussian translation is an L-infinity contraction for every quadratic form

Run: `20260924T074031Z-fleet01-B17-QFORM-auto11`  
Status: general structural theorem strengthening the reflection result. **FULL QFORM remains OPEN.**

## Theorem T — Gaussian translation contraction

Let `A` be any real symmetric `n x n` matrix, let `G~N(0,s I_n)` with `s>0`, and let `M` be any independent random vector in `R^n` with no moment, density, or support assumptions. Suppose the centered quadratic form `G^T A G` has a bounded density. Then

`||p_{(G+M)^T A(G+M)}||_infinity <= ||p_{G^T A G}||_infinity`.

Thus **an arbitrary independent location mixture cannot increase the density norm of an isotropic Gaussian quadratic form**.

### Proof

Condition first on `M=m` and orthogonally diagonalize

`A=O^T diag(lambda_1,...,lambda_r,0,...,0) O`,

where `lambda_i!=0`. Isotropy of `G` means the rotated Gaussian coordinates remain independent `N(0,s)`. Write `m_i` for the rotated deterministic shift and `eps_i=sign(lambda_i)`.

For each active coordinate,

`|lambda_i|(G_i+m_i)^2`

is a scaled noncentral chi-square variable. The Poisson-mixture representation says that, with independent

`K_i~Poisson(m_i^2/(2s))`,

conditional on `K_i=k_i`,

`|lambda_i|(G_i+m_i)^2 ~ Gamma(1/2+k_i, 2s|lambda_i|)`.

Gamma shape additivity lets us realize this conditional law as

`Z_i + W_i`,

where, independently across `i` and between the two families,

`Z_i~Gamma(1/2,2s|lambda_i|)`,

`W_i~Gamma(k_i,2s|lambda_i|)`,

with `Gamma(0,theta)` interpreted as a point mass at zero. Therefore, conditional on the entire Poisson index vector `K`,

`(G+m)^T A(G+m)`

has the same law as

`Q_0 + R_K`,

where

`Q_0=sum_i eps_i Z_i`

has exactly the centered law `G^T A G`, and

`R_K=sum_i eps_i W_i`

is independent of `Q_0`.

Consequently

`p_{(G+m)^T A(G+m) | K} = p_{G^T A G} * mu_{R_K}`.

Convolution with a probability measure contracts `L^infinity`, hence

`||p_{(G+m)^T A(G+m) | K}||_infinity <= ||p_{G^T A G}||_infinity`.

Mixing over `K`, then over the arbitrary random location `M`, preserves the same bound. This proves Theorem T.

The underlying one-coordinate Poisson mixture can be checked directly from Laplace transforms:

`(1+2s|lambda|t)^(-1/2)`

`* exp[(m^2/(2s))((1+2s|lambda|t)^(-1)-1)]`

`=(1+2s|lambda|t)^(-1/2)`

`* exp[-m^2|lambda|t/(1+2s|lambda|t)]`,

which is the Laplace transform of `|lambda|(N(m,s))^2`.

## Reflection and spectral-slack corollaries

For a three-dimensional reflection `B` with spectrum `{1,1,-1}`, the centered law at variance `s` has exact global maximum

`1/(2sqrt(2)s)`.

Theorem T therefore immediately gives the arbitrary-location result proved separately in `ADDENDUM_GLOBAL_GAUSSIAN_LOCATION.md`. At `s=1/12`, every independent Gaussian location mixture has density norm at most `3sqrt(2)`.

More generally, whenever a centered Gaussian three-eigenvalue calculation supplies a bound for a fixed active spectrum, exactly the same bound automatically holds for **every independent random translation**, including arbitrary compound-Poisson limits. In particular, the earlier B17 centered spectral-slack estimates for signature `(2,1)` extend to noncentral/location-mixture limits without any new two-sheet analysis.

## Consequence for sharp-witness search

This removes a whole class of candidate overshoot mechanisms. If a diffuse/product triangular array converges to

`G+M`,

with `G` isotropic Gaussian and `M` independent of `G`, then the random location component by itself can never make the quadratic-form density sharper than the corresponding centered Gaussian quadratic form, regardless of the distribution, dimension, tails, or sign orientation of `M`.

Hence future B17 stress tests seeking a finite-dimensional or asymptotic overshoot above the centered Gaussian obstruction must change more than the location. Candidate mechanisms must alter covariance/shape, preserve non-Gaussian dependence inside active aggregate coordinates, introduce shared macroscopic rows that are not an independent additive location, or exploit additional active spectrum in a way not absorbed by convolution.

No finite-input independence after an orthogonal spectral rotation is asserted here: orthogonalization occurs only inside the isotropic Gaussian conditional law after conditioning on `M`.
