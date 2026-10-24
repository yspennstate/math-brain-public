# B11 / A052 — degree-two extremal class removed from frozen GU

**Status:** proved at the stated all-dimensional restricted scope; independent review pending. Universal GU and full FEI remain open.

## Frozen candidate and prior bound

- Packet: **A052**, stable gap `G-GU-EXTREMAL-STRUCTURE`.
- Claim version: `B11-A052-DEGREE-TWO-EXTREMAL-v1`.
- Frozen pair: ((a,b)=(4,3/4)).
- Prior source-bound endpoint:
  \[
  G\le D_{\ge2}+\tfrac12V_1+\frac{2}{\ln2}I,
  \]
  with the remaining row-cut required only on tensor-prime positive-residual sources.
- Minimal-source condition: every relevant coordinate of a dimension-minimal positive-residual source obeys
  \[
  \Delta_iG-\tfrac34\Delta_iU\ge4\operatorname{Inf}_i+R_{4,3/4}(f).
  \]

## Result

For every genuine Boolean function of Fourier degree at most two, in every dimension,

\[
\boxed{G(f)\le2I(f)},\qquad \boxed{H(f)\le2I(f)}.
\]

The constants are sharp.  The Nisan–Szegedy junta theorem reduces the class to at most four relevant variables.  Exact Walsh enumeration modulo global output sign leaves 111 degree-two functions.  Symbolic prime-log expressions and rational outward enclosures certify all signs: 25 equality cases, 86 strict (G)-cases, minimum positive (2I-G) equal to (2); the minimum positive (2I-H) is (1).

This uses the minimal-counterexample framework substantively: any minimal positive-residual counterexample to (G\le4I+3U/4) must have Fourier degree at least three.  Thus the complete low-degree class is removed from the critical source, rather than merely supplying a necessary condition.

## GU implication and scope

The class is closed under physical restrictions, so (G\le2I) is a valid restricted GU pair ((2,0)).  The audited induction yields (U\le2I) and the generic reduction yields (H\le6I); the direct finite-core theorem sharpens this to (H\le2I).

This is not universal GU.  It does not control arbitrarily small level-(\ge3) mass or the remaining signed (D_{\ge2}+V_1/2) row-cut.  A failed or restricted class theorem is not a disproof of FEI.

## Verification

`verify_degree_two_extremal.py` uses exact rational FWHT, exact upper sums, exact restrictions, symbolic prime-log aggregation, and the explicit rational atanh-series remainder.  No floating-point sign decision is used.

## Next action

Combine the child-residual inequalities with the first nonzero level-(\ge3) signed KL row.  The needed next lemma must be quantitative in high-degree mass and must retain (B_i-\Gamma_i), rather than only asserting degree at least three.

Model/effort metadata: `UNKNOWN`.
