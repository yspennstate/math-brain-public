# B12 / A057 — sharp local theorem for three parallel affine cosets

**Run:** `20261013T092029Z-account01-B12-parallel-triple-local`  
**Primary packet:** A057 (Coherent restriction remainder)  
**Gap:** `B12-A057-COHERENT-HIERARCHY-v15`  
**Status:** local class extension PROVED; hierarchy transfer OPEN; full FEI OPEN.

## Result

The preceding fixed-three-piece estimate had constant
`24 ln(3)+4/e = 27.838212692720404`.  For the unbounded family consisting of
three distinct parallel affine cosets, the parameter dependence is removed:
\[
 \Omega\le 8\ln(2) I(d).
\]
The constant is dimension-, codimension-, bias-, orientation-, and
overlap-independent, and is asymptotically sharp in this class.

Three quotient points always form an affine two-plane.  Their union is the
preimage of that plane with its fourth parallel coset removed.  This makes the
Walsh spectrum exactly two-level: magnitude `3y` on the plane annihilator and
`y` on the remainder of the smaller annihilator.  The physical boundary is
also exact.  If `m_V` and `m_U` count coordinate axes outside the small and
large direction spaces, respectively, then
`I(s)=y(m_V+2m_U)/2`.  Rank gives `m_V>=k`, `m_U>=k-2`, and the selector tax
gives `I(d)>=y(3k-1)/4`.  These identities pay the exact entropy formula with
the sharp `8 ln(2)` constant.  The full proof is in
`PARALLEL_TRIPLE_THEOREM.tex`.

## Why it matters

This is the first three-piece class in this stream whose constant does not
grow with the number-of-pieces proof mechanism.  It handles arbitrary
physical overlap and all codimensions, not only a finite numerical range.
It identifies the useful structure as a nested-flat difference
`1_D-1_E`, rather than pairwise collision separation.

## Independent correction incorporated

B19/A091 independently accepted the previous one-node two-coset theorem but
refuted its advertised hierarchy corollary at its literal scope.  Commit
`0f2769f79b04a9a98ad26b3c9fa1c2d94f9cac98` supplies a two-free-coordinate
cylinder extension with repeated local charge.  Therefore this report makes
no hereditary or hierarchy-payment claim.  The correction is a mathematical
status change, not a cosmetic caveat.

## Verification

`check_parallel_triples.py` uses exact rational Walsh transforms and exact
physical influence, with 70-digit decimal logarithms.  It exhaustively checks
all 1,628 parallel triples through four ambient variables, including the
two-shell spectrum, the exact influence formula, and the local inequality.
It also evaluates the coordinate-minimal parametric family through `k=30`.
There is no randomness.  The computation corroborates but does not replace
the all-dimensional proof.

## Precise remaining gap

The local charge still uses complete `I(d_v)`.  The free-coordinate falsifier
shows that complete reached-source influence can be charged repeatedly down a
nonreusing restriction tree.  The next unpaid step is to decide whether the
parallel-triple proof admits a directional strengthening
`Omega_v <= 8 ln(2) I_{B_v}(d_v)` for an explicitly owned coordinate block;
if not, identify the minimal terminal reserve.  Nonparallel triple collision
graphs also remain open.  No full-FEI conclusion is claimed.

