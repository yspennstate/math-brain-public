# fleet02/B04 r11 addendum — aggregate adaptive E2 square, optimized e5 volume weights, and ridge comparison

Programme `QFORM-DENSITY-3EIG-20260922`. Full QFORM remains **OPEN**. This addendum preserves the immutable main report and applies the newest completed designated-partner result at an actual inequality.

## 1. First unpaid implication after this addendum

The main report paid a disjoint delocalized rank-one square plus an arbitrary two-sided-curvature residual through unconditional pair-volume half-Riesz smoothing. The calculation below shows that a support-rich near-coloop in the same geometry can instead be repaired extremely efficiently by **entropy reweighting of physical three-minors**. Thus the remaining structural debt can be narrowed to

`QFORM-SUPPORT-DEFICIENT-ENTANGLED-COLOOP-OR-AGGREGATE-SQUARE-v1`:

> in a full-target survivor where the third large spectral direction is entangled with the physical coordinates carrying the residual rank-two packet, either find a target-scale physical volume support admitting a bounded-cost fractional matching, or prove that genuine support deficiency / quantitative coloop concentration forces a disjoint aggregate-square, mixed-hub, ridge, pair-Schur, or grouped-coordinate endpoint before any vanishing local minor is inverted.

The point is structural. The product-space analytic endpoints below are already paid.

## 2. New designated-partner result actually applied

Newest completed partner source consumed:

`yspennstate/math-open-problems@df4567713c815300e94c25a594206b76ea00a04f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260923T075009Z-r28/REPORT.md`.

Its sharp half-Riesz rearrangement is

`sup_t int |x-t|^(-1/2) p(x) dx <= C_H ||p||_3^(3/4)`,

`C_H=2 sqrt(2 pi)/3^(1/4)=3.809251227455829...`.

For a quadratic-affine residual `R` with an original-coordinate cross block `M`, `E=e_2(M^T M)>0`, and selected natural squared-`2 x 2`-minor marginal maximum `mu<3/4`, r28 proves

`||p_R||_3 <= F(theta_*)^(2/3) E^(-1/6)`,

where

`F(theta)=e [3 theta/(3 theta-2)] K_theta^(-1/(4 theta))`,
`K_theta=theta^(-theta)(1-theta)^(-(1-theta))`,
`theta_*=min(theta_0,1/(2mu))`,

and consequently its physical-scalar square theorem has coefficient

`C_ad(mu)=C_H sqrt(F(theta_*))`.

I now apply this to a genuinely **delocalized** independent original-coordinate square bank.

### Theorem `QFORM-DELOCALIZED-SQUARE-ADAPTIVE-E2-v1`

Let `K,I,J,W` be pairwise disjoint original-coordinate banks. Let `Z=(Z_k)_(k in K)` be independent of all residual variables, `c!=0`, `a!=0`, and let

`Q=a[c^T Z+m]^2+R`,

where `m` is an arbitrary measurable function of the residual variables and `R` is an arbitrary quadratic polynomial in them. Suppose a disjoint physical residual cross block `M=R[I,J]` has `E=e_2(M^T M)>0`, and after choosing the better row/column orientation its natural squared-pair-volume marginal maximum is `mu<3/4`. Then

`||p_Q||_infinity <= sqrt(2) C_ad(mu)
 (|a| ||c||_2^2)^(-1/2) E^(-1/8).`                              (2.1)

Proof. Put `S=c^T Z`. The product-projection density bound gives

`||p_S||_infinity <= sqrt(2)/||c||_2`.

For fixed residual variables, translation by `m` preserves that cap, and the density of `a(S+m)^2` is bounded by

`[sqrt(2)/||c||_2] |a|^(-1/2)|u|^(-1/2)`

on the appropriate half-line. Averaging over the residual variables and invoking the r28 sharp `L^3 -> H_(1/2)` estimate gives

`||p_Q||_infinity <= [sqrt(2)/||c||] |a|^(-1/2)
 C_H ||p_R||_3^(3/4)`

`<=sqrt(2) C_H sqrt(F(theta_*))
 (|a| ||c||^2)^(-1/2)E^(-1/8)`.

This is (2.1). No rotation of the independent inputs occurs; the only projection is the scalar linear form on the disjoint original-coordinate product bank. QED.

Together with the unconditional theorem in the main report, for `mu<3/4` one may take the smaller of `C_E2` and `C_ad(mu)` before the common factor `sqrt(2)(|a|||c||^2)^(-1/2)E^(-1/8)`.

## 3. One target-valid rotated family

Fix `r=7/10`, an even integer `m>=4`,

`c_m=m^(-1/2)(1,...,1)`, `delta=1/m`,
`c0=cos(pi/8)`, `s0=sin(pi/8)`.

Let the `4 x 2` matrix `U_r` have rows

`sqrt(r)(c0,-s0)`,
`sqrt(1-r)(c0,-s0)`,
`sqrt(r)(s0,c0)`,
`sqrt(1-r)(s0,c0)`.

Then `U_r^T U_r=I_2` and every entry is nonzero. Set `M_r=2U_r`, so its two nonzero singular values are both exactly `2` and

`E_2(M_r^T M_r)=16`.

For mutually independent original-coordinate banks `Z in R^m`, `X in R^4`, `Y in R^2`, define

`Q_(m,r)=(c_m^T Z)^2 + delta ||X||_2^2 - delta ||Y||_2^2
          +2 X^T M_r Y`.                                       (3.1)

Both residual banks have nonzero self curvature. The residual cross block is genuinely rotated and has no zero entry.

Because `M_r^T M_r=4I_2`, the residual block

`[[delta I_4,M_r],[M_r^T,-delta I_2]]`

has active eigenvalues `+-sqrt(4+delta^2)`, each twice, plus `delta` twice from the left nullspace. Including the rank-one `Z` square, the full spectrum is

`{1, +-sqrt(4+delta^2) [each multiplicity 2], delta [multiplicity 2], 0^(m-1)}`.   (3.2)

Hence for every `m>=4` the form is indefinite and has five eigenvalues of modulus at least one. It is therefore inside the exact target.

The natural squared `2 x 2` minor law of `M_r` chooses one row from each repeated-direction pair, with row marginals

`(r,1-r,r,1-r)`.

Thus `mu=r=7/10` and `theta_*=1/(2r)=5/7`. The partner constants are

`K_(5/7)=1.818968511653173...`,
`F(5/7)=33.07096956390116...`,
`C_ad(7/10)=21.905999830112865...`.

Since `16^(-1/8)=1/sqrt(2)`, theorem (2.1) gives the actual all-product-law inequality

`boxed: ||p_(Q_(m,7/10))||_infinity <=21.90599983011287.`        (3.3)

The unconditional aggregate-square theorem from the main report gives the weaker but gate-free

`||p_Q||_infinity <=26.33404618075974`.                         (3.4)

If one instead chooses a single physical `Z_i` as the outer square and applies the partner r28 physical-scalar theorem, the same matrix gives

`||p_Q||_infinity <=15.48988102854417 sqrt(m)`,                 (3.5)

so the aggregate independent square removes the dimension loss.

## 4. Globally optimal q=1 e5 volume weight on the same matrix

Now split the flat square bank into equal halves `Z_L,Z_R` and take the physical cut

`I=Z_L union X`, `J=Z_R union Y`.

The cross block is the direct sum

`B=(c_L c_R^T) direct_sum M_r`.

Its nonzero singular values are exactly `1/2,2,2`, hence

`E_3(B^T B)=4`.                                                  (4.1)

A nonzero physical `3 x 3` minor chooses one `Z_L` row, one `Z_R` column, one row from each of the two repeated-direction pairs of `X`, and both `Y` columns. If the two selected `X` rows have pair weights `w_i,w_j in {r,1-r}`, then

`det(B[S,T])^2 = 16 w_i w_j / m^2`.                             (4.2)

The natural squared-minor law is therefore

`Unif(Z_L row) x Unif(Z_R column) x Bernoulli(r) x Bernoulli(r)`.

Its largest constrained-side marginal is `r=0.7`, so the original e5 Theorem D gate `alpha_i<=1/2` fails. The e5 D' natural-weight extension is admissible because `r<3/4`, but it gives only

`6 sqrt(e)(2r)^(-1/2)(3-4r)^(-1) 4^(-1/6)
 =33.17883601301569...`.                                        (4.3)

Now optimize **all** weights supported on the nonzero minors subject to the original e5 `q=1` marginal gate. In each repeated-direction pair exactly one row is selected, so its two row marginals sum to one. The constraints `alpha_i<=1/2` force both marginals to be exactly `1/2`. At those fixed marginals, the expected log determinant in (4.2) is fixed, while entropy is maximized by independent fair choices in the two pairs; the two flat-bank indices are independently uniform. Thus this is the global optimizer, not a symmetric ansatz.

Equivalently its KL cost relative to the natural volume law is

`KL_min=2 D_Ber(1/2 || r)=-log(4r(1-r))
       =0.17435338714477766...`.                                (4.4)

The arbitrary-weight determinant currency in e5 Theorem D is therefore

`G_3,opt=E_3 exp(-KL_min)=16 r(1-r)=3.36`.                       (4.5)

Applying the completed e5 theorem to this actual optimized weight gives a continuous density and

`boxed: ||p_(Q_(m,7/10))||_infinity
 <=6 sqrt(e) (3.36)^(-1/6)
 =8.083050245273677... .`                                       (4.6)

So on this same target matrix, support-rich near-coloop concentration is much cheaper to repair by entropy-balanced physical volume weights than by the raw natural D' exponent or by the pair-volume square route.

## 5. Direct ridge certificate on the same physical cut

Use the completed one-scale ridge theorem

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

Let `g=gamma^2`,

`k=4/(g+4)`, `h=1/(4g+1)`.

The two singular-2 directions contribute ridge factor `k`; the flat singular-1/2 direction contributes `h`. Hence on the constrained `I` side

`L_gamma=max{kr, 2h/m}`,                                       (5.1)
`theta_gamma=2k+h`,                                             (5.2)
`D_gamma=(1+4/g)^2(1+1/(4g))`.                                 (5.3)

Take the explicit scale `gamma=10^(-3)` (`g=10^(-6)`) and exponent `q=7/5`. For every `m>=4`,

`L_gamma <=0.6999998250000437 < q/2=0.7`,
`theta_gamma=2.999995500016125 >2q=2.8`.

Thus the ridge theorem applies. Its exact expression

`e/[sqrt(2q) gamma] * theta/(theta-2q) * D^(-1/(2theta))`

evaluates here to

`boxed: ||p_(Q_(m,7/10))||_infinity
 <=19.34049287249918... .`                                      (5.4)

As `gamma` tends to zero with `q=2r`, this certificate tends to

`3e/[2^(4/3) sqrt(r)(3-4r)]
 =19.34030832653649...`,                                        (5.5)

but (5.4), not the limiting statement, is the concrete applied inequality.

## 6. Same-matrix hierarchy and proof-map consequence

For every even `m>=4`, on exactly the target-valid form (3.1):

- globally optimized **e5 q=1 physical three-volume weight**: `8.0830502453`;
- explicit **direct ridge** certificate at `gamma=10^-3,q=7/5`: `19.3404928725`;
- newest-partner **aggregate adaptive E2 square**: `21.9059998301`;
- gate-free **aggregate E2 half-Riesz square**: `26.3340461808`;
- newest-partner **single physical square**: `15.4898810285 sqrt(m)`;
- raw natural-weight e5 D' certificate: `33.1788360130`.

This changes the structural diagnosis. A large natural volume marginal below one is not itself a hard obstruction: if the nonzero-minor support admits a fractional matching, entropy reweighting can be decisively better than ridge and square smoothing. The difficult survivor should therefore be described by **support deficiency / quantitative coloop structure**, not merely by a large natural marginal.

No law-uniform pointwise phase decay, arbitrary-joint coarea estimate, conditional projection-cap moment, post-rotation independence, moment/support/log-concavity assumption, or small-random-perturbation argument is used. Continuity is supplied by the e5 Fourier certificate (4.6); the aggregate-square theorem alone claims only absolute continuity plus essential boundedness.

Independent review status: the partner r28 theorem is a completed peer result; the new aggregate extension and same-matrix optimization in this addendum have not yet received an independent review. Full QFORM remains OPEN.
