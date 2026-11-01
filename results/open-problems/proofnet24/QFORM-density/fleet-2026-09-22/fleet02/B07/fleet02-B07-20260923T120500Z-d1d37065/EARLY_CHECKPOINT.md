# fleet02/B07 early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN.
Run: fleet02-B07-20260923T120500Z-d1d37065.

First unpaid implication attacked: `QFORM-COMMON-BANK-R1-AND-NONZERO-ANCHOR-RECEIVER-v1` from designated partner fleet03/B07 20260923T110409Z. The partner supplies an aggregate two-star packet `Z_2 >= H^4/4096` (or the stronger transverse `H^4/64`) but its density theorem required an exactly zero physical two-anchor quadratic block. The goal here is to keep an arbitrary genuinely nonzero 2x2 anchor block and arbitrary within-bank curvature.

## New calculation: fixed-anchor Plancherel receiver

Let `H` be `k` ORIGINAL physical anchor coordinates, `J` a disjoint coordinate bank, and after conditioning all other ORIGINAL coordinates write

`Q(x,z)=x^T B x + 2 x^T G z + a^T x + R(z)`

with `x in R^k`, `G` a full-row-rank `k x |J|` physical coefficient matrix, and `R` an entirely arbitrary quadratic polynomial in `z`. Put `Z_k=det(G G^T)=sum_{|T|=k} det(G_T)^2`.

Let `U=GZ+a/2`. By the LPP product-projection theorem recorded and checked in the required pinned e5 Fourier source,

`||p_U||_infinity <= 2^(k/2) Z_k^(-1/2)`.

For fixed `t`, set

`g_t(x)=prod_{h in H} f_h(x_h) exp(i t x^T B x)`.

The complex pushforward measure

`nu_t(du)=E[ exp(i t R(Z)) ; U in du ]`

has a density satisfying `|nu_t(u)|<=p_U(u)`. Hence

`||nu_t||_2 <= ||p_U||_infinity^(1/2) <= 2^(k/4) Z_k^(-1/4)`.

Moreover

`phi_Q(t)=integral hat(g_t)(2 t u) nu_t(u) du`.

Cauchy-Schwarz plus Plancherel and `prod f_h <=1`, `int prod f_h=1`, give

`||hat(g_t)(2t .)||_2 <= pi^(k/2) |t|^(-k/2)`.

Therefore

`boxed: |phi_Q(t)| <= 2^(k/4) pi^(k/2) Z_k^(-1/4) |t|^(-k/2).`

This is uniform in the anchor block `B`, all same-bank curvature in `R`, affine terms and conditioned outside couplings. It uses the aggregate determinant packet `Z_k`, not one selected minor.

For `k>=3`, Fourier inversion of `min(1,K|t|^(-k/2))` gives

`boxed: ||p_Q||_infinity <= sqrt(2) k/(k-2) Z_k^(-1/(2k)).`

In particular for three fixed physical anchors,

`boxed: ||p_Q||_infinity <= 3 sqrt(2) Z_3^(-1/6).`

For `k=2`, the required e5 fractional-potential Lemma 4.1 at alpha=1/2 gives

`boxed: H_(1/2)(Q) <= 2^(11/4) Z_2^(-1/8).`

Thus the designated partner's nonzero-anchor aggregate-E2 branch is already curvature-safe at the half-Riesz level:

common-bank packet: `H_(1/2)(Q) <= 2^(17/4) H^(-1/2)`;
transverse packet: `H_(1/2)(Q) <= 2^(7/2) H^(-1/2)`.

This does NOT yet give a density bound from two-anchor E2 alone; the next step must spend a third spectral currency. Indeed the rank-two family `Q=2(eps X1+eps^(-1)Z1)(eps X2+eps^(-1)Z2)` has a genuinely nonzero anchor block, `Z_2=1`, and logarithmically unbounded density for independent centered unit-interval inputs. This is an obstruction only to a local E2-to-density theorem, not to QFORM, because the matrix has rank two.

Required pinned source actually used: yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, Section 2.4 (LPP projection density) and Lemma 4.1 (fractional potentials).

Designated partner actually used: yspennstate/math-open-problems@7ad9327f11c39bd465780bd1539d52de9feaacdd, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T110409Z-fleet03-B07-qform-r29/REPORT.md`.
