# Gluing, qualitative regularity, and normal forms: provenance

This editorial note is not part of the mathematical exposition.
The chapter makes no claim of literature novelty.

## Materialized source records

The initial repository snapshot is
yspennstate/math-open-problems@36d0dc0c4ac0910e8d84ae64d443136df86242d5.
Paths below are relative to proofnet24/QFORM-density.

| Source | Blob SHA | Results used |
|---|---|---|
| fleet-2026-09-22/account01/B01/20260923T161404Z-account01-B01-qform-auto11/REPORT.md | fd9a501bce903ff071362a0181835108a1e06bb3 | Sharp product-density L2 identity; critical two-hub packet plus independent scalar L2 remainder; affine hyperbolic-edge corollary |
| fleet-2026-09-22/account04/B15/20260923T151702Z-account04-B15-pivoted-convolution-r6/REPORT.md | aa50353da124122aa6ba3d424aa3b974e819e4b0 | All-p Lp pair bound independent of the first diagonal coefficient; square L3/2 bound; pair-plus-square constant6 and C0 |
| fleet-2026-09-22/account01/B15/20260923T160313Z-account01-B15-QFORM-auto11/REPORT.md | 3e9b1b3a238066e482008271fe146909af3f02e3 | Arbitrary fixed-kernel equality for the universal constant; fixed-width box formulation and weak stability |
| fleet-2026-09-22/account03/B15/20260923T163043Z-account03-B15-qform-auto23/REPORT.md | 75b312446268e192ef14881bf48f8dc2bd017d8c | Countable Gaussian-heat formulation, unit-measure rational unions, generic rational matrices |

Two earlier regularity records were fetched separately from master and
are preserved verbatim, with separate metadata, under
source_snapshot/additional_claude. Their Git blob hashes were recomputed
and agree exactly with the fetch results:

| Additional source | Blob SHA | Local copy |
|---|---|---|
| fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md | b1b64ee58174080fb6fd1738ccfd4473131263fb | continuity_rank3_r11_REPORT.md |
| fleet-2026-09-22/account02/B15/20260922T150242Z-account02-B15-qform-r3/REPORT.md | 0dab7a20a37f66f28a623e0e5dd6837c0be6a02f | continuity_rank3_r3_REPORT.md |

Their retrieval is not represented as part of the earlier initial tree.
Metadata: source_snapshot/additional_claude/ADDITIONAL_CONTINUITY_SOURCES.json.

## Scope and proof details

### Critical two-hub packet

Theorem fg:two-hub retains an arbitrary finite measurable phase R(Y)
in the slope bank. The scalar L2 remainder Z is independent of both
physical hubs and that bank. This independence is used to factor the
characteristic function and cannot be omitted.

The proof obtains:

    |phi_packet(t)| <=pi P/|t|,
    integral |phi_Q| <=2T+2 pi^(3/2) P R2 T^(-1/2).

Optimization gives exactly3*2^(-2/3)(P R2)^(2/3).
With projectioncap2/sqrt(det(BB^T)) and the sharp productL2 bound,
the hyperbolic-edge constant is3 det(BB^T)^(-1/6)|c|^(-1/3).
No pointwise scalar Fourier decay is assumed.

### Rough product regularity

Theorem fg:fixed-matrix-continuity is fully proved for every fixed
real symmetric matrix of rank at least three and arbitrary affine
terms. It does not assert a universal matrix-independent height.

The manuscript strengthens the presentation of the source transversality
proof by proving uniform output stability under input L1 approximation
in an invertible physical block of dimension3 or4:

1. Critical ball contribution is O(r^(d-2)), with explicit constants
   C3=2pi and C4=4pi after the deterministic quadratic normalization.
2. Far-field contribution is at most d^(3/2)/(sigma R).
3. In a compact annulus, the region where at most one partial derivative
   is large lies in finitely many thin tubes. Its output density is
   O(delta^(d-2)).
4. On the complement, telescope the difference of two product densities.
   For the factor changed in coordinatei, integrate in another coordinate
   j with derivative>delta. At most two inverse branches give the bound
   2(d-1)/delta times the sum of input L1 errors.
5. Smooth compact cap-one approximations produce continuous output
   densities, including the critical value by the critical-ball bound.
   Uniform convergence gives C0 for the original rough inputs.
6. Symmetric one- or two-coordinate elimination supplies an invertible
   physical principal block of order3 or4. Conditioning outside that
   block and averaging continuous densities with a uniform fixed-block
   height proves the full-rank statement.

This proof avoids assumptions about continuity of rough traces,
post-rotation independence, or conditional projection density caps.
The fixed-block height M_B is proved directly, so the regularity result
does not depend on a dimension-dependent spectral theorem elsewhere.

### Fixed-kernel and countable normal forms

All normal forms in the chapter include arbitrary original-coordinate
affine terms. Accordingly, the countable class includes rational vectors
b as well as rational symmetric matrices. Constants are absorbed into
the output center.

The fixed-kernel formula retains the weight s3(A); omitting that weight
would not yield the stated fixed-scale equality. The weighted essential
height supremum equals the original normalized universal constant by
scaling the entire polynomial.

The countable proof uses an approximate bathtub threshold, which remains
valid when maximizing sets are not attained or some superlevel sets have
infinite measure. Unit-measure sets are approximated by finite rational
interval unions of exactly the same mass. Generic rational matrices are
obtained after a small outward spectral dilation, preserving s3>1.
No bounded number of intervals, bounded dimension, or finite search
certificate follows from this countable reformulation.

## Verification

- All constants and changes of variables were independently re-derived
  while writing.
- A separate reviewer independently verified the product identity,
  packet gluing, pair-plus-square theorem, all regularity lemmas, and
  fixed-matrix C0 theorem, as well as the complete fixed-kernel,
  fixed-box, and countable-heat normal forms. The review evidence is
  paper_work/SECOND_REVIEW_REGULARITY_GAUSSIAN.md.
- The full combined manuscript compiled successfully after this chapter
  was included. No overfull boxes appeared in that compile.
- Central cross-references used: four:projection, geom:ac, conj:main.
  Standard Plancherel and Young inequalities use the manuscript Fourier
  normalization; no additional bibliography entries are introduced.
