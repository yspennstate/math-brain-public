# r53 attribution correction — exact prior analytic receiver found

This addendum supersedes any wording in `REPORT.md` that suggests `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-MOVING-SQUARE-v1` is a novel analytic kernel.

## Exact prior theorem

After publication of the first r53 report, I re-read the source-pinned fleet03/B10 theorem at

- `yspennstate/math-open-problems@c1af196adade03e07456c8f6e783f952b0fa0e8d`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/fleet03-B10-20260922T121625Z-qform-r11/REPORT.md`

Its Theorem 2.1, `QFORM-DEPENDENT-PAIR-HYPERBOLIC-SQUARE-v1`, already proves the exact core statement:

If `X` has density cap `1`, `(Y,Z)` is independent of `X` with arbitrary joint density cap `H`, `a,b !=0`, and `F,theta` are arbitrary measurable functions, then

`T=2aXY+F(Y)+b(Z+theta(Y))^2`

has

`||p_T||_infinity <= 3*2^(2/3) H^(2/3)|a|^(-2/3)|b|^(-1/3)`.

Fleet02/B10 subsequently recorded the density-cap-`K` scaling of that theorem:

`||p_T||_infinity <=3*2^(2/3)H^(2/3)K^(2/3)|a|^(-2/3)|b|^(-1/3)`.

Therefore the r53 analytic formula

`3(2MK)^(2/3)|beta^2 gamma|^(-1/3)`

is exactly the same prior receiver after completing the square. **No novelty is claimed for that analytic kernel.**

## What r53 actually adds

The useful new proof transfer is only the following source-valid implication.

Let `R` be independent of `(S,C,D)`. Conditional on `R=r`, write

`gamma D^2+2h(r,C)D
 = gamma(D+h(r,C)/gamma)^2-h(r,C)^2/gamma`.

Then apply the already-proved fleet03/B10/fleet02-B10 theorem with

`X=S`, `Y=C`, `Z=D`,
`a=beta`, `b=gamma`,
`theta_r(C)=h(r,C)/gamma`,
`F_r(C)=F(r,C)-h(r,C)^2/gamma`.

The theorem's constant is uniform in `r`, so averaging in the genuinely independent source `R` gives the same bound. Thus the r53 result is best classified as:

`QFORM-PRIOR-HYPERBOLIC-SQUARE-INDEPENDENT-PARAMETER-LIFT-v1`

— an immediate source-valid conditional lift of an exact prior theorem, not a new analytic theorem.

## Concrete implication retained

The target-level consequence remains valid. For disjoint original-coordinate banks `I0,I1,J`,

`S=u^T X_I0`, `R=r^T X_I1`, `(C,D)=(v^T X_J,w^T X_J)`

with `v,w` orthonormal, the form

`Q=2d1SC+2d2RD+cC^2+2delta CD+gamma D^2`

is obtained by conditioning on `R` and applying the prior theorem with moving shift

`theta_r(C)=(d2 r+delta C)/gamma`.

Using Rudelson--Vershynin (`K<=sqrt(2)`) and Livshyts--Paouris--Pivovarov (`H<=2`) gives

`||p_Q||_infinity <=3*2^(5/3)|d1^2 gamma|^(-1/3)`.

This pays a **one-sided overlapping cross tail**: `2d2RD` shares the right variable `D` with `gamma D^2`, so it is not an independent additive remainder. The exact target family

`Q_eps=2SC+2eps RD+D^2`, `0<eps<1`,

still obeys

`||p_Qeps||_infinity <=3*2^(5/3)=9.524406311809198...`.

The partner-funnel splice in `REPORT.md` remains valid and gives `<9.964/s3(H)` for the stated SVD-aligned two-right-direction chamber. The full QFORM theorem remains OPEN.

## Source discipline

This addendum follows the owner instruction: when an exact prior solution is found, report it without claiming novelty or changing the target. No statement in the first report should be read as a publication-novelty claim.
