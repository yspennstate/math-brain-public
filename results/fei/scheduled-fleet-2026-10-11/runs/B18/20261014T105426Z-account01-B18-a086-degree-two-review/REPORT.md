# B18 / A086 — independent degree-two GU proof audit

**Run:** `20261014T105426Z-account01-B18-a086-degree-two-review`  
**Audited claim:** `B11-A052-DEGREE-TWO-EXTREMAL-v1`  
**Stable gap:** `G-GU-EXTREMAL-STRUCTURE`  
**Prior status:** author-proved restricted theorem, independent review pending  
**Verdict:** **PASS at stated scope; no material repair.**  
**Universal GU / full FEI:** OPEN.

## Exact candidate and implication

The audited candidate is

\[
\forall n\ \forall f:\{-1,1\}^n\to\{-1,1\},\quad
\deg(f)\le2\Longrightarrow G(f)\le2I(f),\ H(f)\le2I(f).
\]

It removes the entire degree-at-most-two class from a minimal positive
residual counterexample to the frozen pair `(a,b)=(4,3/4)`.  It does not
bound the remaining degree-at-least-three signed KL rows.

## Review result

The all-dimensional step is valid: the Nisan--Szegedy theorem bounds the
number of relevant variables by `d*2^(d-1)`, hence four when `d=2`.
Dummy variables preserve every quantity in the claim.  The finite core is
also valid: exact author arithmetic exhausts 111 output-sign representatives,
and every logarithmic sign follows from a rational atanh enclosure.

An independent implementation reconstructed all 111 cases, all restrictions,
upper-set masses, `U,I,G,H`, and one-dummy-variable lifts.  It reproduced:

- 25 exact equality cases and 86 strict cases for `G<=2I`;
- minimum positive `2I-G` equal to 2;
- 25 exact equality cases and 86 strict cases for `H<=2I`;
- minimum positive `2I-H` equal to 1;
- maximum frozen residual equal to 0, attained only here by a constant;
- 444 dummy-variable invariance identities.

The minimum-counterexample deduction is correctly quantified.  For every
relevant coordinate of a dimension-minimal positive-residual source,

\[
\Delta_iG-\frac34\Delta_iU
\ge4\operatorname{Inf}_i+R_{4,3/4}(f).
\]

The reviewed theorem forces every nonconstant degree-two source to have
strictly negative residual, so a minimal positive-residual source has degree
at least three.

## Source reduction

I independently reconstructed the actual restriction induction: for a
restriction-closed class, universal `G<=aI+bU` gives
`U<=aI/(1-b)`.  Substitution in the reviewed granularity bound gives

\[
H\le\left(2+\frac{2a}{1-b}\right)I.
\]

Thus the degree-two pair `(2,0)` gives `U<=2I` and generic `H<=6I`; the
direct finite-core certificate sharpens the last constant to 2.

## First unsupported line

Universal GU still requires the quantitative high-degree row cut displayed
in `PROOF_REVIEW.md`.  Degree at least three alone supplies no dimension-free
reserve because its spectral mass may be arbitrarily small.

## Execution

Command:

`python b18_a086_degree2_review/independent_degree2_review.py`

Actual output is preserved in `CHECK.out`.  Arithmetic was integer Walsh plus
100-digit Decimal for the independent reproduction; the sign proof itself is
the separately audited rational enclosure in the author verifier.  No
randomness, symmetry beyond output sign, paid compute, protected source, or
scheduler mutation was used.

## Next action

B20/A097 should consume this review as a scope certificate only and continue
with a quantitative lower bound on the retained high-degree reserve in terms
of the signed row cut.  A second independent end-to-end reviewer is still
required for any universal proof.

Model/effort metadata: `UNKNOWN`.

