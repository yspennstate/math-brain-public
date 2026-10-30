# B12 / A058 — affine-defect binary-code GU theorem

**Run:** `20261014T122054Z-fleet01-B12-gu-affine-defect-code`  
**Gap:** `B12-A058-SHARED-COORDINATE-OVERLAP`  
**Attempt:** `A058-GU-AFFINE-DEFECT-CODE-16`  
**Status:** author-proved proper-class theorem, pending independent review;
universal GU and full FEI remain open.

## Frozen candidate and implication

For every affine subspace `V subseteq F_2^n`, of arbitrary dimension and
orientation relative to the physical coordinates, prove

\[
 G(1-2\mathbf1_V)\le\kappa_{pd}I(1-2\mathbf1_V),
 \qquad
 \kappa_{pd}=\frac14+\frac94\log_2\frac{16}{9}.
\]

The preceding run covered at most three exceptional points with constant
64.  This candidate instead covers defect sets of unbounded cardinality and
keeps the sharp point-defect constant.  Closure under physical restrictions,
disjoint products, and the already proved reused-character construction
would imply `U<=kappa_pd I` and

\[
 H\le(2+2\kappa_{pd})I
 =\left(\frac{41}{2}-9\log_2 3\right)I
 =6.2353374935\ldots I
\]

on the resulting class.

## Result

The candidate is proved at author level.

Represent `V` as one fiber of a full-rank binary matrix `A`.  Its spectrum is
the ordinary point-defect law embedded into the physical coordinate order by
the binary column matroid of `A`.

- Deleting a non-coloop relaxes the upper-cone order.  Its exact signed
  decrement is nonpositive, so it consumes no source-influence credit.
- At a coloop, the complete orientation-dependent posterior sum cancels
  between the root and the one active child.  The remaining decrement is
  exactly the ordinary rank-`m` point-defect decrement.
- Every nonzero physical column has influence `2^(1-m)`.  Summing only the
  coloops and using the sharp point-defect theorem yields
  `G<=kappa_pd I`.

This removes bounded defect count, bounded affine rank, coordinate alignment,
and injective/no-reuse assumptions.  Repeated columns, zero columns, arbitrary
affine translations, branch-dependent rank loss, and unbounded physical
dimension are included.

## Verification

`python3 CHECK.py` enumerated every binary subspace through six physical
coordinates:

- 3,283 nonconstant code embeddings;
- 2,663 coloop coordinate cases;
- 13,822 non-coloop coordinate cases;
- exact rational Walsh laws and influences;
- maximum non-coloop decrement ratio `0`;
- maximum coloop identity residual `2.78e-17` from binary logarithm evaluation;
- maximum aggregate ratio `2.1176687467547968`, attained by a rank-three
  coordinate point defect with irrelevant coordinates.

The enumeration is a reconstruction check, not the all-rank argument.  The
proof is the exact deletion/coloop calculation in `PROOF.md`.

## Signed-reserve accounting

No sign projection or unsigned indicator estimate is used.  Non-coloops are
paid by a negative signed posterior relaxation.  At coloops, the exact core
posterior `R` is retained in both root and child and cancels once.  The other
physical sign is an exact constant terminal.  Repeated columns add influence
but cannot create a hidden positive decrement.

## Scope and next action

This is an unbounded defect-count class but not universal GU.  The remaining
obstacle is a negative set that is a union of several affine fibers with
unequal spectral light masses.  The next attempt should analyze a two-fiber
union and preserve the fiber label as a posterior reserve, seeking a constant
independent of the number of fibers rather than iterating the present theorem.

