SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B01, 2026-09-24T06:35:52Z.
attacking: the rank-one two-hub arrowhead left by finite-leak routing; aggregate all weak leaf edges before inversion and spend the aggregate through half-Riesz.

# fleet02/B01 — grouped rank-one arrowhead half-Riesz receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T063552Z-fleet02-B01-qform-auto11-r46`  
Role: Oscillatory replacement / complementary constructions and source-valid counterexamples  
Status: **NEW HALF-RIESZ RECEIVER FOR EVERY NON-SINGLE-LEAF RANK-ONE TWO-HUB ARROWHEAD / FULL QFORM OPEN**

## 1. Scope and corrections retained

All scalar random coordinates below are original independent coordinates with probability densities bounded by one. No moment, compact-support, connected-support, Gaussian, iid, log-concavity, or post-rotation independence assumption is used. Continuity is not claimed.

The phase-aligned-density obstruction is retained: no positive law-uniform pointwise power decay for a scalar quadratic phase is used or asserted. The live corrections forbidding arbitrary-joint coarea, rotated independence, near-zero-half-Riesz perturbation, and absorption of arbitrary same-bank curvature by a single heavy edge are also retained.

The full owner target remains OPEN.

## 2. Required pinned source actually spent

Required source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I use three proved items from `RESULTS.md` / `FOURIER_ROUTE_REPORT.md` at explicit equations below:

1. for every cap-one density `f` and every complex `g` with `|g|<=f`,

   `integral |g_hat(u)|^p du <= 4 pi / sqrt(p)`, `p>=2`;                 (2.1)

2. at `alpha=1/2`, the fractional-potential interface

   `H_(1/2)(Z):=sup_s E|Z-s|^(-1/2)`
   ` <= (2pi)^(-1/2) integral |t|^(-1/2)|phi_Z(t)| dt`;                 (2.2)

3. the scalar-square peel: if an exact literal completion gives

   `Q=a(X_0+h)^2+R`, `a!=0`, then

   `||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R)`.                         (2.3)

The same pinned source's D/D'/D5 volume bounds are applied to a concrete obstruction in Section 7.

## 3. Setup: rank-one two-hub arrowhead with diagonal leaves

Let `H=(H_1,H_2)` be two independent original cap-one coordinates and let `Y=(Y_1,...,Y_m)` be a source-disjoint product bank. Let `w in R^2\{0}`, `c in R^m\{0}`. Put

`W=||w||_2`, `C=||c||_2`, `s=WC`.                                      (3.1)

Consider

`R = F(H) + 2 (w dot H)(c dot Y)`
`    + sum_i (d_i Y_i^2 + ell_i Y_i) + const`,                          (3.2)

where `F` is an arbitrary measurable real hub phase and the leaf coefficients `d_i,ell_i` are arbitrary real numbers.

For each frequency `t`, push the complex hub measure

`exp(itF(h)) f_(H1)(h_1) f_(H2)(h_2) dh`

under `S=w dot H`. It has a complex density `g_t` satisfying

`|g_t(u)| <= p_S(u) <= K:=1/||w||_infinity <= sqrt(2)/W`.               (3.3)

Indeed, condition on the hub coordinate whose coefficient has maximal modulus; scaling its cap-one density gives the first inequality. This is only an algebraic pushforward bound, not a claim that a rotated coordinate is independent of anything.

Writing

`q_i(y)=exp(it(d_i y^2+ell_i y)) f_i(y)`,                               (3.4)

the characteristic function obeys

`|phi_R(t)| <= integral |g_t(u)| prod_i |q_i_hat(2t c_i u)| du`.        (3.5)

This is the point at which all weak physical leaf edges are aggregated before any reciprocal edge coefficient is paid.

## 4. Spread leaves: a shape-free aggregate half-potential

Assume

`max_i c_i^2/C^2 <= 1/2`.                                               (4.1)

Set `alpha_i=c_i^2/C^2`. Hölder with exponents `1/alpha_i`, the substitution `v=2|t|Cu`, and (2.1) give

`integral prod_i |q_i_hat(2t c_i u)| du`
` <= (2|t|C)^(-1) prod_i`
`    [ |c_i/C|^(-1) integral |q_i_hat(v)|^(1/alpha_i) dv ]^(alpha_i)`
` <= (2|t|C)^(-1) prod_i (4pi)^(alpha_i)`
` = 2pi/(|t|C)`.                                                        (4.2)

Thus, by (3.3),

`|phi_R(t)| <= min(1, 2pi K/(C|t|))`.                                  (4.3)

For every `A>0`,

`integral_R |t|^(-1/2) min(1,A/|t|) dt = 8 sqrt(A)`.                   (4.4)

Spending the required fractional-potential estimate (2.2) at (4.3) yields

`H_(1/2)(R) <= 8 sqrt(K/C)`
`             <= 2^(13/4) (WC)^(-1/2)`.                                (4.5)

Therefore

`boxed: H_(1/2)(R) <= 2^(13/4) s^(-1/2)`                               (4.6)

in the spread branch. Numerically `2^(13/4)=9.513656920021768...`.

## 5. One heavy leaf plus any nonzero tail

Suppose instead that there is a unique heavy leaf `h` with

`c_h^2>C^2/2`,                                                         (5.1)

and assume the remaining tail is nonzero. Set

`T=(C^2-c_h^2)^(1/2)>0`,
`theta=|c_h| T/C^2 in (0,1/2)`.                                        (5.2)

Factor the integrand in (3.5) as the heavy factor

`F_t(u)=q_h_hat(2t c_h u)`                                              (5.3)

and the tail product

`G_t(u)=prod_(i!=h) q_i_hat(2t c_i u)`.                                (5.4)

Plancherel and `|q_h|<=f_h<=1`, `integral f_h=1`, give

`||F_t||_2^2 <= pi/(|t c_h|)`.                                         (5.5)

For the tail put `beta_i=c_i^2/T^2`. Hölder, now with exponents `1/beta_i`, and (2.1) at `p_i=2/beta_i>=2` give

`||G_t||_2^2`
` <= (2|t|T)^(-1) prod_(i!=h)`
`    [ |c_i/T|^(-1) integral |q_i_hat(v)|^(2/beta_i) dv ]^(beta_i)`
` <= sqrt(2) pi/(|t|T)`.                                               (5.6)

Cauchy-Schwarz in the pushed-forward hub variable, together with (3.3), therefore gives

`|phi_R(t)|`
` <= min(1, K pi 2^(1/4) (|c_h|T)^(-1/2) |t|^(-1)).                   (5.7)

Using (2.2) and (4.4) once more,

`H_(1/2)(R)`
` <= 2^(21/8) K^(1/2) (|c_h|T)^(-1/4)`
` <= 2^(23/8) W^(-1/2)(|c_h|T)^(-1/4)`
` = 2^(23/8) s^(-1/2) theta^(-1/4)`.                                  (5.8)

Hence

`boxed: H_(1/2)(R) <= 2^(23/8) s^(-1/2) theta^(-1/4)`                  (5.9)

whenever a heavy leaf has any nonzero independent tail. The numerical prefactor is `2^(23/8)=7.33603234563737...`.

No leverage condition is imposed on the tail. Arbitrary diagonal leaf quadratic twists survive because they enter only through the complex factors `q_i` to which (2.1) applies.

## 6. Density compiler after one literal square

Combining Sections 4-5 with the pinned square peel (2.3) gives the main result.

### Theorem — `QFORM-RANK1-TWOHUB-ARROWHEAD-HALFRIESZ-v1`

If an exact original-coordinate completion gives

`Q=a(X_0+h)^2+R`, `a!=0`,                                              (6.1)

with `R` of the rank-one two-hub arrowhead form (3.2), then:

- under (4.1),

  `boxed: ||p_Q||_infinity <= 2^(13/4)|a|^(-1/2)s^(-1/2)`;             (6.2)

- if one leaf is heavy and the remaining tail is nonzero,

  `boxed: ||p_Q||_infinity <= 2^(23/8)|a|^(-1/2)s^(-1/2)theta^(-1/4)`. (6.3)

Thus every rank-one two-hub arrowhead with at least two nonzero leaf slopes is paid. The only degeneration in this receiver is the quantitative approach to one literal leaf, `theta->0`.

Essential boundedness is proved in this scope; continuity is not asserted.

## 7. Full-target stress family invisible to D/D'/D5

Take five original coordinates `(X_0,H_1,H_2,Y_1,Y_2)`, let

`w=c=2^(-1/2)(1,1)`,

and consider

`Q_* = X_0^2 + 2(w dot H)(c dot Y)`.                                  (7.1)

The coefficient matrix is the direct sum of `[1]` and the symmetric bipartite block with cross matrix `w c^T`. Since that cross matrix has singular values `{1,0}`, the spectrum of the full matrix is

`{1,1,-1,0,0}`.                                                        (7.2)

Hence this is an exact owner-target family with three eigenvalues of absolute value at least one.

Here `s=1` and the two leaf leverages are exactly `1/2`, so (6.2) gives

`boxed: ||p_(Q_*)||_infinity <= 2^(13/4)=9.513656920021768...`.        (7.3)

This also applies the pinned source to a concrete obstruction: every original-coordinate cross block of this matrix has rank at most two (the isolated `X_0^2` never contributes to a disjoint cross block, and the remaining off-diagonal matrix has rank two). Consequently

`e_3(M^T M)=e_5(M^T M)=0`                                             (7.4)

for every physical cut. Therefore the pinned D, D', and D5 volume currencies are identically zero on this full-target family, while the grouped half-Riesz receiver above gives (7.3).

## 8. Newest designated-partner result applied at an actual inequality

Newest compatible partner result read before publication:

`fleet03/B01`, run `20260924T063007Z-fleet03-B01-qform-auto11-r46`, theorem `QFORM-INDEFINITE-PAIR-THIRDCURVATURE-v1`.

For an invertible indefinite physical pair `P`, with `D=|det P|`, `kappa=sigma_min(P)` and `lambda=s_3(A)>0`, it proves

`||p_Q||_infinity <= 14.180833 D^(-3/10)(kappa lambda)^(-1/5)`.        (8.1)

On the concrete target (7.1), every nonzero physical edge has coefficient `1/2`, so choosing the pair `(H_1,Y_1)` gives

`P=[[0,1/2],[1/2,0]]`, `D=1/4`, `kappa=1/2`, `lambda=1`.               (8.2)

The partner theorem therefore gives the valid full-target estimate

`||p_(Q_*)||_infinity <= 14.180833 (1/2)^(-4/5)`
`                       < 24.691`.                                    (8.3)

The grouped-arrowhead theorem improves this to `9.514` by aggregating all four weak hub/leaf edges before inversion. In particular, the partner has now removed the analytic post-pair cross-collapse singularity; the remaining reason not to rely on one pair is purely structural/quantitative: in diffuse families every individual `|A_ij|` may tend to zero even when the aggregate rank-one slope `s=||w|| ||c||` stays order one.

This exactly matches the partner's new unpaid implication `QFORM-AGGREGATE-PAIR-CURRENCY-BEFORE-INVERSION-v1` on the rank-one two-hub arrowhead subclass.

## 9. Exact obstruction at the single-leaf boundary

The degeneration `theta->0` cannot simply be removed from the half-potential statement. Let `H_1,H_2,Y` be independent centered unit-interval variables, put

`S=(H_1+H_2)/sqrt(2)`,
`R=(S+Y)^2=S^2+2SY+Y^2`.                                              (9.1)

The density of `S+Y` is continuous and strictly positive near zero. Hence

`H_(1/2)(R) >= E|R|^(-1/2)=E|S+Y|^(-1)=infinity`.                     (9.2)

So a shape-free half-Riesz bound depending only on the aggregate rank-one slope is false when the leaf support collapses to one coordinate. This is not a QFORM counterexample: the coefficient matrix of (9.1) has rank one, and even after adjoining one independent unit square it supplies only two large eigenvalue directions.

The next step must therefore use the owner's third large eigenvalue structurally at the exact/almost-single-leaf boundary, rather than pretending the present half-potential survives there.

## 10. First unpaid implication

`QFORM-ALMOST-SINGLELEAF-THIRD-CURVATURE-ROUTING-v1`:

> In the finite-leak rank-one arrowhead state, when `theta=|c_h| ||c_tail||/||c||^2` is tiny or zero, force from `s_3(A)>=1` a product-preserving third resource outside the nearly rank-one square: a literal independent square/pair, a grouped-square packet, a second aggregate slope, or a projected crossing. Combine that resource with the generic physical-edge quarter-potential or the newest partner third-curvature pair receiver without paying a reciprocal coefficient that is allowed to vanish.

The phase-aligned-density counterexample remains preserved; the new estimates are integrated-frequency/rearrangement estimates only.

Full QFORM: OPEN.
