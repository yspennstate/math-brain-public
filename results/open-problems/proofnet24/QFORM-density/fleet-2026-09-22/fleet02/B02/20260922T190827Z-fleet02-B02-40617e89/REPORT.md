SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-22T19:21:39Z.
attacking: subcritical fractional-trace closure for an indefinite original-coordinate pair followed by a physical scalar Schur pivot, and a compatible named-partner hyperbolic packet, without pointwise oscillatory decay or post-rotation independence.

# QFORM-SUBCRITICAL-PAIR-TRACE-v1

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260922T190827Z-fleet02-B02-40617e89`.
Fresh owner control applied before this report: revision `2026-09-22.13` at observed main head `8b508713b9edf3ae1c92824be781da39a8c0d948`.
Status: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN**.

## 1. Exact target and correction discipline

The target remains the full arbitrary-product-law statement: independent real coordinates with one-dimensional densities bounded by one, arbitrary dimension, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, support, Gaussian, log-concavity, diagonal-basis, or post-rotation-independence hypothesis is added.

This run explicitly consumes the live corrections that prohibit: law-uniform pointwise Fresnel decay; generic semiproduct-cap substitutions for product provenance; arbitrary-joint rank-three coarea; positive conditional-projection-density moments; one-good-minor exhaustion; and the revision-13 suggestion that failure of a good physical triple automatically leaves a pure CLT geometry. In particular, the exact target family `A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)` is bank-controlled but neither uniformly localized nor purely diffuse, so no localized/CLT dichotomy is assumed.

The unweighted target-wide criterion `integral |phi_Q(t)| dt<infinity` is not claimed. I still do not have a source-valid exact-product counterexample to that stronger criterion. The successful mechanism below is a strictly weaker fractional trace `H_alpha(R)=sup_s E|R-s|^{-alpha}`. This avoids converting the owner's non-product illustrative examples into a target-class counterexample.

## 2. Source-pinned incoming results

1. Prior fleet02/B02 pair theorem: `yspennstate/math-open-problems@4d41fbacb2f0f17ebde23274d06397d5ab7ba147`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260922T183829Z-fleet02-B02-qform-r11/REPORT.md`. For an invertible indefinite physical `2 x 2` block `B`, with `D=|det B|`, `kappa=sigma_min(B)`, and arbitrary residual-dependent translation, the conditional pair-density envelope can be taken as

`Psi(tau)=D^(-1/2)[2sqrt(2)+log(T/|tau|)]`, `0<|tau|<=T`,

`Psi(tau)=4 kappa^(-1/2)|tau|^(-1/2)`, `|tau|>T`,

where `T=2D/kappa`.

2. Named partner fleet03/B02, completed report `yspennstate/math-open-problems@056867164c939f4e70988e762258f2542e32fd75`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T182919Z-fleet03-B02-qform-r12/REPORT.md`, proves for independent `X,U`, with `X` density cap one and `U` density cap `M`, and an independent bank `V`,

`R=2a XU+H(X,V)`

has for every `p>1`

`||p_R||_p <= p |a|^(-(1-1/p)) M^(1-1/p)`.

Its fresh addendum `yspennstate/math-open-problems@c83d7f618cd630af9757c44d4c8b5f74b3962de9` records the necessary restriction: no hidden `U`-dependent curvature may be placed inside `H`. The correction example `(U+X)^2` shows why an endpoint half-Riesz argument may fail if that restriction is discarded.

3. Current O0 structural source used only to locate the remaining debt: fleet02/B19 `yspennstate/math-open-problems@06913a3636bf0add597d8dcf16eca5cd2ccd92a2` proves a scale-free raw-third-compound decomposition into `r=0,1,2,3` packets. The `r=3` physical-row packet is already paid; the `r<=2` packets remain aggregate and must not be silently identified with an indefinite principal pair or scalar Schur pivot.

4. New compatible correction at brain commit `1a0bbd1c03f98cc935b6c9f6125ae9b7fb856d36` (`QFORM-NO-GOOD-TRIPLE-DOES-NOT-IMPLY-PURE-CLT-v1`) prevents a false localized-versus-pure-CLT exhaustion. Nothing below uses that implication.

## 3. Main analytic lemma: every subcritical fractional trace passes through the indefinite pair

For `0<alpha<=1/2`, define

`H_alpha(R)=sup_s E |R-s|^(-alpha)`.

### Theorem 3.1 — `QFORM-PAIR-FRACTIONAL-TRACE-TRANSDUCER-v1`

In the pair setting of source 1,

`||p_Q||_infinity <= C_alpha D^(alpha-1/2) kappa^(-alpha) H_alpha(R)`,

where

`C_alpha = 2^alpha exp(-1+2sqrt(2)alpha)/alpha`, for `0<alpha<=1/(2sqrt(2))`,

and

`C_alpha = 2^(alpha+3/2)`, for `1/(2sqrt(2))<=alpha<=1/2`.

At `alpha=1/2`, this is exactly the preceding B02 bound `4 kappa^(-1/2)H_(1/2)(R)`.

### Proof

It suffices to dominate the source envelope `Psi(tau)` by the claimed fractional kernel. On the inner region write

`x=|tau|/T in (0,1]`, `y=-log x>=0`.

The ratio of `Psi(tau)` to

`D^(alpha-1/2) kappa^(-alpha)|tau|^(-alpha)`

is

`2^alpha exp(-alpha y)(2sqrt(2)+y)`.                              (3.1)

The derivative in `y` has the sign of

`1-alpha(2sqrt(2)+y)`.

If `alpha>=1/(2sqrt(2))`, the expression is decreasing from `y=0`, giving maximum `2^(alpha+3/2)`. If `alpha<1/(2sqrt(2))`, the maximum is attained at

`y=1/alpha-2sqrt(2)`

and equals

`2^alpha exp(-1+2sqrt(2)alpha)/alpha`.                           (3.2)

On the outer region, the same ratio is

`4 (D/(kappa|tau|))^(1/2-alpha)`.

Since `|tau|>=2D/kappa`, its maximum is

`4*2^(-(1/2-alpha))=2^(alpha+3/2)`.                              (3.3)

For `alpha<1/(2sqrt(2))`, (3.2) dominates (3.3); at the threshold they agree. Thus

`Psi(tau) <= C_alpha D^(alpha-1/2)kappa^(-alpha)|tau|^(-alpha)`.

Averaging this conditional density over the residual variables proves Theorem 3.1. No independence between the pair translation and the residual is used.

## 4. A physical scalar pivot always has a uniform subcritical trace

### Lemma 4.1 — translated-square fractional potential

Let `Z` have a probability density bounded by one. For any `d!=0`, any random element `V` independent of `Z`, and arbitrary measurable `h(V),c(V)`, put

`R=d(Z+h(V))^2+c(V)`.

Then for every `0<alpha<1/2`,

`H_alpha(R) <= [2^(3alpha)/(1-2alpha)] |d|^(-alpha)`.             (4.1)

### Proof

For every real `s` and `u>0`, the exact one-dimensional sublevel set obeys

`Leb{x: |x^2-s|<u} <= 2sqrt(2) u^(1/2)`.                         (4.2)

If `s<0` this is immediate from a centered interval. If `s>=0`, the two cases `u>=s` and `u<s` give respectively

`2sqrt(s+u) <=2sqrt(2u)`

at the maximizing transition, and

`2[sqrt(s+u)-sqrt(s-u)]`,

whose maximum at fixed `u` again occurs at `s=u` and equals `2sqrt(2u)`.

The cap-one law therefore gives

`P(|(Z+h)^2-s|<u) <= min(1,2sqrt(2)u^(1/2))`.                    (4.3)

Layer cake with crossing point `u_0=1/8` yields

`E |(Z+h)^2-s|^(-alpha)`
` <= alpha*2sqrt(2) int_0^(1/8) u^(-alpha-1/2)du`
`    + alpha int_(1/8)^infinity u^(-alpha-1)du`
` = 2^(3alpha)/(1-2alpha)`.                                    (4.4)

The bound is uniform in the translation and target level, so conditioning and averaging over `V`, followed by scaling by `d`, proves (4.1).

## 5. New full-matrix branch: indefinite pair plus one scalar Schur pivot

Write the full matrix in original coordinates as

`A=[[B,C],[C^T,D_0]]`,

where `B` is an invertible indefinite physical `2 x 2` principal block. Completing the pair gives

`Q=(X+B^(-1)CZ)^T B (X+B^(-1)CZ) + Z^T S Z`,

`S=D_0-C^T B^(-1)C`.                                             (5.1)

Choose any residual original coordinate `k` with

`d=S_kk!=0`.

Completing this scalar square writes the entire residual, with no hypothesis on its remaining rank or signs, as

`Z^T S Z=d(Z_k+h(V))^2+c(V)`.                                   (5.2)

Taking `alpha=1/4` in Theorem 3.1 and Lemma 4.1 gives the clean bound

`boxed(
||p_Q||_infinity
 <= 16 exp(1/sqrt(2)-1)
    (D kappa |d|)^(-1/4)
 < 11.938 (D kappa |d|)^(-1/4).
)`                                                                (5.3)

Indeed

`C_(1/4)=4*2^(1/4) exp(1/sqrt(2)-1)`

and the square trace constant is `2^(7/4)`, whose product is exactly the coefficient in (5.3).

This is `QFORM-INDEFINITE-PAIR-SCHUR-PIVOT-QUARTER-v1`. The square shift may depend arbitrarily on every remaining residual coordinate; all remaining quadratic curvature is inside `c(V)`. Thus the fresh same-square correction is not an obstruction at the subcritical quarter trace: the endpoint `H_(1/2)` may blow up for a square, while `H_(1/4)` is uniformly finite.

There is also a determinant form. If `J` is the physical triple consisting of the pair plus coordinate `k`, then the Schur determinant identity gives

`|det A[J,J]| = D |d|`.

Hence

`boxed(
||p_Q||_infinity
 <= 16 exp(1/sqrt(2)-1)
    [kappa |det A[J,J]|]^(-1/4).
)`                                                                (5.4)

This does not claim that the bare three-large-eigenvalue hypothesis forces a triple with the product in (5.4) bounded below. It supplies the analytic payment once such a product-preserving triple is structurally extracted.

## 6. Named partner fleet03/B02 applied to an actual new inequality

Take the partner residual

`R=2a XU+H(X,V)`,

with the exact partner hypotheses. At `p=2`, source 2 gives

`||p_R||_2 <= L:=2 sqrt(M/|a|)`.                                (6.1)

For any probability density `r` with `||r||_2<=L`, Cauchy--Schwarz on `|u|<=R_0` and the mass bound outside give

`H_(1/4)(r)
 <= 2 L R_0^(1/4)+R_0^(-1/4)`.

Optimizing at `R_0^(1/4)=(2L)^(-1/2)` gives

`H_(1/4)(R) <= 2sqrt(2L)=4(M/|a|)^(1/4)`.                       (6.2)

Substituting into Theorem 3.1 at `alpha=1/4` yields the new partner-cascade inequality

`boxed(
||p_Q||_infinity
 <= 16*2^(1/4) exp(1/sqrt(2)-1)
    [M/(D kappa |a|)]^(1/4)
 < 14.197 [M/(D kappa |a|)]^(1/4).
)`                                                                (6.3)

This is an actual use of the named OTHER-account theorem. It retains its crucial source condition that `H(X,V)` has no hidden `U`-dependent curvature. The new square-pivot result (5.3) is complementary: it is precisely what remains valid in the same-square situation that defeats the partner endpoint if one incorrectly hides `U^2` inside `H`.

## 7. Exact regression

The checker saved in this immutable run verifies the pair-envelope optimization on a dense deterministic grid, the exact `alpha=1/4` constants, and the square sublevel-length cap. Its executed output is:

`alpha=0.25`
`pair_constant=3.549078305226400`
`square_H14_constant=3.363585661014858`
`pair_square_constant=11.937628897278433`
`pair_square_closed_form=11.937628897278433`
`partner_H14_multiplier=4.000000000000000`
`pair_partner_constant=14.196313220905601`
`square_sublevel_grid_max=2.828363483783505`
`square_sublevel_exact_cap=2.828427124746190`
`STATUS=PASS`

Checker source commit: `a83ea80584b133b22ea9dea9db1c819d548f9ee0`.
Executed output commit: `c4c52ff01ebe88692d1f5e77336e7bf169bef883`.
The finite grid is only a regression check; equations (3.1)--(6.3) are analytic proofs.

## 8. What this pays and the first unpaid implication

The analytic obstruction from the fresh same-square correction is now removed whenever an outer invertible indefinite physical pair has already been isolated: **any nonzero scalar diagonal in its physical Schur residual is enough for a finite density bound**, with the quantitative product (5.3). No endpoint half-Riesz estimate, pointwise Fresnel decay, conditional spectral cap, or post-rotation independence is needed.

The first unpaid implication is therefore structural and quantitative, not analytic:

> From the surviving third-compound/O0--O3 geometry under `s_3(A)>=1`, force either an already-paid ridge/cross-bank branch, or an invertible indefinite original-coordinate pair `B` together with a residual scalar coordinate satisfying a universal lower bound on `D*kappa*|d|` (equivalently `kappa*|det A[J,J]|` for the associated physical triple), or a genuinely affine product hyperbolic packet satisfying the named partner hypotheses and a universal lower bound on `D*kappa*|a|/M`.

The current B19 raw packets R0/R1/R2 do not by themselves establish this: their heavy objects are rows of an original-coordinate cross block, not automatically an indefinite principal pair, and their orthogonal row-space residual is not automatically the physical Schur complement. Those identifications remain unpaid.

The revision-13 localized-versus-CLT shortcut is also unavailable by the live fleet03/B16 correction. Therefore the next useful mechanism is to connect the scale-free raw R1/R2 packet identities to a **principal-pair/Schur-pivot product** or to a disjoint grouped hyperbolic bank without selecting one tiny coordinate minor.

No full-target theorem or counterexample is claimed.
