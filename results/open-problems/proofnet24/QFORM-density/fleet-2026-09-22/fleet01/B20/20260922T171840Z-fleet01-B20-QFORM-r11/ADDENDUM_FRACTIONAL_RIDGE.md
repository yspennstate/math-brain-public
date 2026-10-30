# Addendum — diffuse rank-two exterior mass is already a paid half-Riesz packet

This addendum continues the same B20 run after `QFORM-O0-FIVEBANK-LAPLACE-CASCADE-v1` and sharpens the analytic interface on the four-bank block `C=C_{pr}`.

## Source used

The completed fractional-ridge theorem is fleet01/B03 run `fleet01-B03-20260922T164925Z-r12`, canonical mathematics

`yspennstate/math-open-problems@c301be6b21f382934962aeb4c019b713377eac2f`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/fleet01-B03-20260922T164925Z-r12/REPORT.md`.

For an original-coordinate cross block `C`, with

`K_gamma=CC^T(gamma^2 I+CC^T)^(-1)`,
`theta_gamma=tr K_gamma`,
`D_gamma=det(I+CC^T/gamma^2)`,

its `q=1`, half-Riesz specialization states that if `max_i (K_gamma)_ii<=1/2` and `theta_gamma>1`, then for the full quadratic form `R` retaining arbitrary same-side terms and outside couplings,

`sup_z E|z-R|^(-1/2)`
` <= 2^(5/4) sqrt(e) gamma^(-1/2)`
`    * [theta_gamma/(theta_gamma-1)]`
`    * D_gamma^(-1/(4 theta_gamma)).`                              (A.1)

## New theorem `QFORM-E2-DIFFUSE-HALF-RIESZ-v1`

Let `C` be any original-coordinate cross block of a quadratic form in independent cap-one coordinates, and suppose

`E_2:=e_2(CC^T)>0`.                                                  (A.2)

Let `gamma>0` be the unique scale for which

`theta_gamma=3/2`.                                                   (A.3)

(The scale exists because (A.2) implies `rank C>=2`, so `theta_gamma` decreases continuously from at least two to zero.) If

`max_i (K_gamma)_ii<=1/2`,                                          (A.4)

then

`boxed(
 sup_z E|z-R|^(-1/2)
 <= 3*2^(31/24)*sqrt(e) * E_2^(-1/8)
 < 12.109 E_2^(-1/8).
)`                                                                    (A.5)

### Proof

Write the positive eigenvalues of `CC^T/gamma^2` as `ell_j` and

`k_j=ell_j/(1+ell_j)`.

Then `sum_j k_j=3/2`. Since `0<=k_j<1`,

`e_2(k)=((sum k_j)^2-sum k_j^2)/2 >=1/2`.                          (A.6)

Indeed, subject to `0<=k_j<=1` and total mass `3/2`, the convex quantity `sum k_j^2` is maximized at the extreme profile `(1,1/2,0,...)`, where it equals `5/4`; hence (A.6). Since `ell_j=k_j/(1-k_j)>=k_j`,

`e_2(ell)>=e_2(k)>=1/2`.                                            (A.7)

Scaling gives

`E_2=gamma^4 e_2(ell)`,

so

`gamma^4<=2E_2`.                                                     (A.8)

Also

`D_gamma=prod_j(1+ell_j)>=e_2(ell)=E_2/gamma^4`.                   (A.9)

Apply (A.1) with `theta_gamma=3/2`. The ratio is `theta/(theta-1)=3` and the determinant exponent is `1/(4theta)=1/6`, so

`H:=sup_z E|z-R|^(-1/2)`
` <= 3*2^(5/4)sqrt(e) gamma^(-1/2) D_gamma^(-1/6)`
` <= 3*2^(5/4)sqrt(e) gamma^(1/6) E_2^(-1/6)`.                    (A.10)

By (A.8),

`gamma^(1/6)<=2^(1/24)E_2^(1/24)`.

Substitution into (A.10) gives exactly (A.5). QED.

## Application to the fleet02/B20 heavy packet

The main B20 report proves that the completed fleet02/B20 packet supplies disjoint physical banks with

`s E_2 > 1/995328`,                                                  (A.11)

where

`s=||B[i,R_q]||_2^2`

is the singleton-to-bank cross energy and `E_2=e_2(C_{pr}C_{pr}^T)` is the rank-two exterior mass on four other banks.

Therefore, whenever `C_{pr}` is ridge-diffuse at its `theta=3/2` scale,

`sup_z E|z-R|^(-1/2)`
` < 3*2^(31/24)sqrt(e) * 995328^(1/8) * s^(1/8)`
` < 68.053 s^(1/8).`                                                 (A.12)

Thus the four-bank rank-two side of the O0-heavy cascade is **already analytically paid in the diffuse branch** at the exact half-Riesz level that a square-pivot transducer would need. What remains is not another time-integral estimate. It is a product-provenance transducer for the disjoint singleton-to-`R_q` bank when no usable physical square is available, or else the complementary branch in which `C_{pr}` itself has ridge leverage `>1/2` at `theta=3/2` and can be recursively localized.

This does not prove the full QFORM target and does not claim continuity. It narrows the O0-heavy debt to a bank-level hyperbolic/localization problem while retaining arbitrary self blocks and outside couplings in the fractional-ridge theorem's stated scope.
