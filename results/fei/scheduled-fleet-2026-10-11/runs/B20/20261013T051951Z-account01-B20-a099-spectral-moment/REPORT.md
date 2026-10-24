# B20 / A099 — spectral-moment assembly and the collision factor

**Status:** analytic restricted theorem proved pending independent review; the raw-moment universal route is obstructed; full FEI remains **OPEN**.

## Exact movement

The newest A090 reconstruction repaired the B11 upper-set charge domain and
correctly reduced the universal leaf from coordinatewise control to the
aggregate inequality

\[
F_{1/2}(\widehat f^{,2})\le \kappa I(f)
\]

only on finite-dimensional `H/I` maximizers. This run applies that corrected
target to A099 and proves, for every probability law on subsets and every
retention `t`,

\[
F_t(p)\le\frac1{\ln2}\,\mathbb E[(1+t)^{|Y|}-1].
\]

The proof is all-dimensional. It linearizes each repaired coordinate charge,
counts the compatible later-coordinate subsets exactly, and then sums a
geometric series over the ordered members of the spectral set.

For a finite-dimensional maximizer `f`, at `t=1/2` this gives

\[
\frac{H(f)}{I(f)}\le
2+\frac2{\ln2}+\frac4{\ln2}\frac{M_{3/2}(f)}{I(f)}
-\frac{4\mathbb E\operatorname{Var}(g)+2\mathbb E b(g)}{I(f)},
\]

where

\[
M_{3/2}(f)=\sum_S\widehat f(S)^2((3/2)^{|S|}-1).
\]

Thus a universal bound `M_{3/2}<=kappa I` on maximizers would prove FEI with
constant `2+2/ln2+4*kappa/ln2`. In particular, a degree-`d` critical
candidate obeys the explicit arity-independent bound obtained from
`kappa=((3/2)^d-1)/d`.

## Exact obstruction and mechanism pivot

The raw moment loses the essential posterior collision factor. For the genuine
Boolean `n`-bit point defect,

\[
\frac{M_{3/2}}I=\frac2n((5/4)^n-1)\to\infty,
\]

while an exact computation gives

\[
\frac{F_{1/2}}I\to\frac12.
\]

Hence the moment majorant is exponentially loose on a canonical family with
`H/I -> 4`. This does not refute the maximizer-only moment hypothesis, because
point defects are not known to maximize every dimension; it does prove that
Booleanity alone cannot pay the aggregate target through this raw moment and
that the route overcharges a central near-extremal control.

The precise discarded factor is `m_J(A)/b_{J,A,i}`, the conditional
probability of the exact later-coordinate cell after the previously exposed
information. The next candidate is the collision-corrected functional
`Lambda_t` in equation (11) of `SPECTRAL_MOMENT_ASSEMBLY.tex`, with
`F_t<=Lambda_t/ln2`. Its universal payment on Boolean maximizers is open.

## Previous/new bound and class extension

- Previous: A099 gave the half-restriction equivalence but no analytic upper
  control of its aggregate envelope.
- New: an explicit all-dimensional upper bound in terms of an exponential
  Fourier-level moment, with a dimension-independent theorem on critical
  candidates whose normalized moment is bounded.
- Obstruction: the parameter cannot be removed by raw Booleanity; point
  defects make it grow exponentially while the true envelope stays bounded.
- Remaining leaf: pay the collision-corrected `Lambda_{1/2}` (or directly
  `F_{1/2}`) by influence on actual maximizers, using signed Boolean
  convolution or critical block-erasure constraints.

## Verification

Command:

`python3 verify_spectral_moment.py`

The checker exhausts all 65,812 Boolean truth tables through four variables,
verifies the new half-envelope majorant, and checks the exact point-defect
formula and its rigorous empty-cell upper bound through dimension 40. The
analytic proof, not enumeration, establishes the all-dimensional theorem.
Exact output is in `CHECK.out`.

Mandatory controls are preserved:

- parity has zero true envelope but a large raw moment, another allowed
  one-sided loss;
- point defects locate the exponentially bad step exactly;
- near tensors and addressing require no false overlap additivity;
- the theorem holds for arbitrary laws, but its critical FEI consequence is
  asserted only for genuine Boolean maximizers;
- all empty-spectrum, variance, and endpoint terms remain explicit.

## Sources and scope

- Owner control revision `2026-10-12.1`, Brain commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- B20/A099 half-restriction theorem, canonical commit
  `d41dd05c667aa82d22d66f02d93c067d794d809a`, source path
  `runs/B20/20261012T042605Z-account01-B20-a099-critical-half-u/`.
- B11 annealed upper-set theorem, canonical source commit
  `4f6254ff7ea2064aed023fe9efc7c27156b51cde`.
- A090 second reconstruction, local source-complete package
  `runs/B18/20261012T095632Z-account01-B18-a090-upper-set-second-review/`;
  it has no repository receipt because that review stream preserved its
  standing write restriction.

No novelty or full-FEI claim is made. Review targets: A090 (recused from the
input it repaired) and fresh A094 for this new theorem; A047/A092 should test
the collision-corrected functional. Consumer: A100.

## Adoption reconciliation

No new recipient-authored native receipt was supplied. Verified coverage
remains 20 local schedules; the requested other 60 remain intended but
unverified. The existing source-bound follow-up was not duplicated.

## Persistence receipts

The eight-file canonical package was committed at
`d7e8adef37b53b16b43934158f345159e2d08584`; the byte-identical Brain
handoff was committed at `2897ebcdecf5f9c02c62d21a78a957d0c97ac41d`.
All sixteen file readbacks were nonempty and matched the expected Git blob
SHAs. These receipts establish durable delivery, not mathematical acceptance
or independent review.
