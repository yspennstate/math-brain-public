# account02/B09 addendum — single-pivot Schur-cross extraction is false

**Run:** `20260922T124417Z-account02-B09-QFORM-r2`  
**Classification:** `CANDIDATE_REFUTED` for the naive universal extraction strengthening; full QFORM conjecture remains OPEN.

This note sharpens the first unpaid implication in the main report. The new local theorem `QFORM-RANK2-SCHUR-PIVOT-v1` is valid, but the full spectral hypothesis cannot force one such physical pivot/cut with a uniform resource. In fact a standard hard target family has **no** nonzero pivot whose Schur complement admits any rank-two disjoint cross block at all.

## Source family

Consume account01/B19's canonical target-family construction:

- repository `yspennstate/math-open-problems`
- commit `072cf685a12893b44d555f14e4e610bcf2154037`
- path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260922T121338Z-b19-qform-r11/REPORT.md`

For `m>=2`, use coordinates `{0} union Y union Z`, with `|Y|=|Z|=m`, and define the symmetric matrix `A_m` by

- `A_{0y}=A_{y0}=m^(-1/2)` for every `y in Y`;
- `A_{zz'}=m^(-1)` for every `z,z' in Z`;
- every other entry zero.

Equivalently, with `u1=e0`, `u2=m^(-1/2)1_Y`, `u3=m^(-1/2)1_Z`,

`A_m = U [[0,1,0],[1,0,0],[0,0,1]] U^T`.

Hence the nonzero spectrum is exactly `{1,-1,1}`. Every `A_m` is a genuine full-target matrix.

## Proposition — `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE-v1`

For every `m>=2` and every physical coordinate `k` with `(A_m)_{kk}!=0`, the scalar-pivot Schur complement of `A_m` at `k` has the property that **every** disjoint original-coordinate cross block has rank at most one.

Thus no nonzero physical pivot of `A_m` satisfies the rank-two Schur-cross hypothesis of `QFORM-RANK2-SCHUR-PIVOT-v1`.

### Proof

The only nonzero diagonal entries of `A_m` occur in the `Z` group, and each equals

`d=1/m`.

Fix `k in Z`. The pivot couples only to the remaining `Z` coordinates, each coupling equal to `1/m`; it has no coupling to coordinate `0` or to `Y`.

Before eliminating `k`, the remaining `Z x Z` block is `J_{m-1}/m`. The rank-one Schur correction is

`[(1/m)1][(1/m)1]^T / (1/m) = J_{m-1}/m`.

Therefore the entire remaining `Z x Z` block cancels exactly. The scalar-pivot Schur complement consists only of the unchanged `0-Y` star:

`S_{0y}=S_{y0}=m^(-1/2)` for `y in Y`,

with every other entry zero.

Now take any disjoint coordinate partition `I|J` of any subset of the remaining coordinates. If `0 in I`, the cross block `S[I,J]` has nonzero entries only in the single row indexed by `0`; if `0 in J`, it has nonzero entries only in the single column indexed by `0`; if `0` is on neither side, the cross block is zero. Hence

`rank S[I,J] <=1`

for every disjoint cross block. QED.

Coordinates `0` and `Y` cannot serve as scalar pivots for the new theorem because their diagonal entries are exactly zero.

## Why this is decisive rather than a target counterexample

The same family is already known to be uniformly controlled by product-preserving aggregation. Writing

`Y_m=m^(-1/2) sum_{y in Y} X_y`,

`Z_m=m^(-1/2) sum_{z in Z} X_z`,

one has exactly

`X^T A_m X = 2 X_0 Y_m + Z_m^2`.

Account01/B19 applies account02/B10's hyperbolic-square theorem after the standard bounded-density rescaling of the aggregate variables and obtains a universal bound `<19.1`, uniformly in `m` and in all permitted input laws.

So this family refutes only the naive strengthening

> `s3(A)>=1` always yields a single nonzero physical pivot whose Schur complement has a quantitatively rank-two cross block.

It does **not** refute the QFORM conjecture.

## Corrected first unpaid implication

The main report's residual must be read as a genuine **dichotomy/aggregation** statement, not as a single-pivot extraction theorem:

`QFORM-SCHUR-CROSS-OR-DIFFUSE-AGGREGATION-v2`:

from `s3(A)>=1`, either obtain a quantitative rank-two Schur-cross pivot and apply `QFORM-RANK2-SCHUR-PIVOT-v1`, **or** detect a star/low-cross-rank aggregate geometry of the type above and pass to a high-cardinality product-preserving channel (hyperbolic-square / diffuse cross-block / separable-phase mechanism) before paying any reciprocal local minor.

The family `A_m` is now a mandatory regression test for any proposed universal pivot-selection lemma.
