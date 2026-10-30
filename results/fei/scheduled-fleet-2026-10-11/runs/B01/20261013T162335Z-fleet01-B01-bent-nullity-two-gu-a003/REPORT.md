# B01 / A003 — bent nullity-two GU obstruction

## Verdict

**PROVED EXACT FINITE WITNESS, PENDING INDEPENDENT REVIEW.** The frozen
candidate `G(P) <= 3 I(P)` survives this run, but its constant is now known
to be nearly sharp already on a genuine ten-variable member of the arbitrary
nullity-two shield class. The previous exact lower calibration was
`G/I = 277/96 = 2.885416...`; the new certificate proves

\[
 2.974 < G(P)/I(P) < 2.975.
\]

Since this witness is bent, `U(P)=I(P)=5`. Consequently every inequality
`G <= a I + b U` valid on this class must satisfy `a+b>2.974`.

This is a sharper quantitative obstruction, not a proof of `G<=3I`, not a
bound with `b<1`, and not full FEI. Full FEI remains **OPEN**.

## Frozen object and exact result

Let `x in F_2^4`, `y in F_2^6`, and

\[
 P(x,y)=(-1)^{x^TMy}D(y),\qquad M=(31,52,7,34),
\]

where each integer is the six-bit row mask in least-significant-bit physical
coordinate order and the 64-bit truth mask of `D=+1` is
`13594860716390676976`.

The checker proves, without floating-point decisions:

* `rank(M)=4=m-2` and all six physical columns are nonzero;
* every Walsh coefficient of `P` has magnitude 32, hence `P` is bent;
* `H(P)=10`, `U(P)=5`, and physical `I(P)=5` exactly;
* all twenty one-bit restrictions have 256 nonzero Walsh coefficients of
  magnitude 32;
* rational atanh-series enclosures for every occurring integer logarithm
  certify `2.974 < G/I < 2.975`.

The computed value is approximately
`G=14.871876482258559` and `G/I=2.974375296451712`.

## General pattern extracted

For a rank-`(m-2)` shield whose two-bit function on every kernel coset is
bent, the parent shield is bent by the exact fiber Walsh decomposition. If
all shield rows and physical columns are nonzero, every physical coordinate
has influence `1/2`. Thus for this expanding subclass

\[
 H(P)=2m-2,\qquad U(P)=I(P)=m-1.
\]

It follows that a GU' estimate on the subclass collapses on each such witness
to `G/I <= a+b`. The new ten-variable witness raises that necessary sum to
above `2.974`. This explains why trying to obtain `b<1` while retaining a
small `a` cannot ignore the upper-set asymmetry term.

## Search and falsification attempts

The bounded search used exact truth tables and Walsh transforms for scoring.
It first allowed arbitrary cores, then pivoted to moves preserving the bent
condition on every two-dimensional kernel fiber.

* data width 5: best arbitrary-core ratio found `2.865968627894475`;
* data width 6: best arbitrary-core ratio found `2.931661332284333`;
* data width 6, bent-fiber-preserving search: best ratio found
  `2.974375296451712` (the certified witness above).

No sampled case exceeded 3. These searches are not exhaustive and are not
used as proof of the upper bound.

## Exact remaining obstruction

For a bent parent on `n=2m-2` variables, each restriction has a uniform
spectral law on 256 points in the present `n=10` case. If `A_{i,eps}` is its
spectral support, then

\[
 U(P_{i=eps})=|A_{i,eps}|^{-1}
 \sum_{S\in A_{i,eps}}\log_2|A_{i,eps}\cap\{T:T\supseteq S\}|.
\]

The unpaid universal step is a dimension-independent lower bound on the sum
of these child upper-set logarithms strong enough to give `G<=3I` (or a GU'
bound with `b<1`). Balanced derivatives alone do not provide that bound.

## Scope and next action

This extends the exact obstruction from six to ten variables and isolates a
near-boundary bent instance. It does not settle a growing family and it does
not remove parameter dependence from the desired upper bound. The next
attempt should freeze the bent-support child inequality suggested above and
either prove it from the dual-bent derivative structure or search
bent-fiber shields at data width 7 for a certified crossing of 3.

## Sources and status

This run continues `B01_A003_ARBITRARY_NULLITY_TWO_FEI_v1` from canonical
package commit `99c60c7a5554f2a435016ad100ccb5d2d10a6bd0` (visible at later
canonical head `f108d34dd304d03aae2d28c5160c4a32a45758d3`). Control revision is
`2026-10-12.1`, source commit
`40210272c19f43fed84f6a67653f9a04b0e11e28`. The parent theorem remains
author-proved pending independent review. This new finite certificate also
requires independent reproduction. No literature-priority claim is made.
