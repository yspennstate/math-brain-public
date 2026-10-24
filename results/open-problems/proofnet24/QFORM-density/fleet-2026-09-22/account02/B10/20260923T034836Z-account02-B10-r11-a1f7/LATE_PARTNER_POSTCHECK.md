# account02/B10 r11 — late designated-partner postcheck

This is an additive source-bound correction to `REPORT.md`; the earlier immutable report is not rewritten.

During final source refresh, the designated partner `account03/B10` had advanced beyond r23b to

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T034310Z-account03-B10-QFORM-r25/REPORT.md`.

Later source wins. The statements below replace every occurrence in the earlier report/handoff that called r23b the “latest” partner or described the r23b generic collar as the final residual. The mathematical proof of `QFORM-MINORITY-HUB-TRANSVERSE-DISCRIMINANT-v1` itself is unchanged.

## 1. What r25 newly pays

In the only small-Pluecker collar left by r23b, r25 retains an ORIGINAL hub row `r_i=sqrt(c)e` with

`c>1/4`, `|alpha|:=|e^T Lambda e|<1/16`, and `||A_(i,-i)||_2>sqrt(1023)/64`.

It proves three further source-valid reductions.

1. `QFORM-NEARNULL-HUB-TRANSVERSEHEAVY-PAYMENT-v1`: if any second physical row has

`||(I-ee^T)r_j||^2>=1/4`,

then the full output density is essentially bounded by `<609`. Hence every unpaid r25 state satisfies

`||(I-ee^T)r_j||^2<1/4` for every `j!=i`.                         (P1)

2. `QFORM-ARBITRARY-HUB-COMPLEMENT-DIFFUSE-v1`: after conditioning on the ORIGINAL hub and whitening the ORIGINAL-coordinate complement, a diffuse complement is paid at determinant scale `3e[(1-c)D]^(-1/3)`; in particular `c<=7/8` gives `<6e` in that branch.

3. `QFORM-ARBITRARY-HUB-THREE-DELETION-v1`: if `c<=7/8`, after at most three ORIGINAL-coordinate deletions either a product-diffuse branch is continuously bounded by `<12e`, or at most three residual coordinates carry more than half of one complement-whitened direction. If `c>7/8`, the state is a quantitative near-coloop. Thus r25's own first unpaid implication is `QFORM-NEARNULL-HUB-LONGITUDINAL-LOCALIZATION-v1`.

## 2. Actual splice of the new B10 theorem into r25

The theorem proved in this run applies without any assumption on the second rows:

if `alpha=e^T Lambda e` has the minority inertia sign, then

`||p_Q||_infinity <=2sqrt(2pi)c^(-1/2)(alpha det Lambda)^(-1/4)`.

In r25's collar, `c>1/4` and `|det Lambda|>=1`. Therefore the concrete r25-visible-minority subbranch

`|alpha|>=2^(-10)`

obeys

`||p_Q||_infinity
 <=2sqrt(2pi)(1/4)^(-1/2)(2^(-10))^(-1/4)
 =32sqrt(pi)
 =56.7185232289... <56.719`.                                     (P2)

Combining (P1), r25's complement-whitening/three-deletion theorem, and (P2), any still-unpaid **visible-minority-hub** state may be restricted to

`0<|alpha|<2^(-10)`,                                              (P3)

`||(I-ee^T)r_j||^2<1/4` for every `j!=i`,                         (P4)

and, additionally, either

- `c>7/8` (quantitative near-coloop), or
- `c<=7/8` and at most three ORIGINAL residual coordinates carry more than half of one complement-whitened direction after the r25 greedy localization.

This is strictly narrower than both r23b's generic near-null hub/star collar and r25's full longitudinal-localization successor.

The corrected first unpaid implication for the **visible-minority-hub subbranch** is therefore

`QFORM-MINORITY-HUB-ULTRANEARNULL-LONGITUDINAL-LOCALIZATION-v1`:

> Under the r25 collar and localization alternatives above, prove a universal density bound when the physical hub Rayleigh quotient has the minority inertia sign and `0<|alpha|<2^(-10)`, retaining the nonzero hub square and all longitudinal/transverse overlap exactly.

The remaining hub-sign chamber in r25's successor is not claimed closed by this run.

## 3. Scope correction for the logarithmic square-peel family

The six-coordinate family in `REPORT.md`, Proposition 6.1, remains a valid exact-target counterexample to the **raw unconditional scalar-square half-Riesz envelope**: its envelope grows like `log(1/sqrt(eps))` while the actual density at the cone boundary is bounded by `pi sqrt(2)` via the required ruled theorem.

However, that family has transverse-heavy rows (indeed the large `w` and `v` rows have transverse leverage close to one), so r25's new Theorem 3.1 pays the family before entering the final transverse-light residual (P4). Therefore Proposition 6.1 must **not** be read as a falsifier of every possible half-Riesz-like estimate after all r25 hypotheses have been imposed. Its correct scope is: the naive square-peel envelope cannot serve as a uniform interface for the broader positive-`d` near-null collar; the fully r25-localized ultranear-null survivor remains open.

## 4. Final status after later-source reconciliation

- `QFORM-MINORITY-HUB-TRANSVERSE-DISCRIMINANT-v1`: unchanged and **PROVED**.
- Latest designated partner r25: **APPLIED at the concrete inequality (P2)**.
- r25 transverse-heavy and complement-whitening exits: **CONSUMED, not reproved**.
- `QFORM-NEARNULL-SQUARE-PEEL-LOG-LOSS-v1`: **valid mechanism falsifier in its stated broader collar scope**, but not a falsifier specifically of r25's final transverse-light localization chamber.
- Full exact-rank-three QFORM: **OPEN**.
- Full arbitrary-spectrum owner target: **OPEN**.
