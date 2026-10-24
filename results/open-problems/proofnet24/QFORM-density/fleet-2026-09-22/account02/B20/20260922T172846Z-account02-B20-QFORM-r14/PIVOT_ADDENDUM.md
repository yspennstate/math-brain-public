# Pivot-packet addendum: row-heavy or disjoint-bank refinement

This addendum continues run `20260922T172846Z-account02-B20-QFORM-r14`. Full QFORM remains open.

## Theorem `QFORM-PIVOT-ROW-OR-DISJOINT-BANK-v1`

Assume the pivot alternative produced in the main report. Thus an original-coordinate cut is `L disjoint_union R`, a physical pivot `i in L` satisfies `|A_ii|>=alpha`, and

` s_1(C)>beta,  C=A[L,R]. `

Write the pivot row into the opposite bank as `r=A[i,R]` and delete that row from the outer cross matrix: `C'=A[L\{i},R]`. Then at least one of the following holds:

1. **row-heavy pivot:** `||r||_2 >= beta/sqrt(2)`;
2. **pivot-disjoint outer bank:** `s_1(C') > beta/sqrt(2)`.

For the current half-barrier constants `beta=499/4000`, the common threshold is

`499/(4000 sqrt(2)) > 0.0882.`

### Proof

The positive-semidefinite identity

`C^T C = C'^T C' + r^T r`

implies

`s_1(C)^2=lambda_max(C^TC)
 <= lambda_max(C'^TC')+lambda_max(r^Tr)
 = s_1(C')^2+||r||_2^2.`

If both alternatives failed, the right side would be at most `beta^2/2+beta^2/2=beta^2`, contradicting `s_1(C)>beta`. QED.

## Source-valid analytic currency in the row-heavy branch

Set

`Y=r X_R=sum_{j in R} A_ij X_j`.

Because `R` is a set of original physical coordinates, its coordinates remain mutually independent and independent of the pivot source `X_i`. The scalar Rogozin--Ball projection bound for a normalized linear form gives

`||p_Y||_infinity <= sqrt(2)/||r||_2`.

Therefore the row-heavy alternative implies the explicit universal marginal cap

`||p_Y||_infinity <= 2/beta = 8000/499 < 16.033.`

This is a marginal cap for the actual physical aggregate `Y`; it is **not** promoted to a conditional cap after exposing another linear combination of the same bank, and it does not assert independence between `Y` and the remaining quadratic self terms on `R`.

## Why this helps the first unpaid implication

For `a=A_ii`, the scalar-pivot completion is the exact identity

`Q = a (X_i + a^{-1} A_{i,-i}X_{-i})^2
     + X_{-i}^T (A_{-i,-i}-a^{-1}A_{-i,i}A_{i,-i}) X_{-i}.`

The new dichotomy says the strong pivot packet cannot hide entirely in an ambiguous overlap:

- either the completed-square shift contains a physical-bank linear aggregate with a dimension-free marginal density cap `<16.033`;
- or a cross bank of operator size `>499/(4000 sqrt(2))` survives after deleting the pivot coordinate and is therefore genuinely disjoint from the pivot source.

Neither alternative alone completes the density payment because arbitrary same-bank quadratic curvature remains. The next step must combine this dichotomy with an aggregate Schur-compound or grouped-bank argument. In particular, the row-heavy case may not use the refuted inference “bounded marginal/conditional cap implies an independent hyperbolic variable,” and the disjoint-bank case may not select a single tiny minor.
