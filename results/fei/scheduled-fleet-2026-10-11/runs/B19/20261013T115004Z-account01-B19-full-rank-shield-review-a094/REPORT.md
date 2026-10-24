# B19 / A094 independent review — full-rank arbitrary-core shielding

## Verdict

**B05_A023_FULL_RANK_SHIELD_v1 is independently accepted at its declared
scope.**  No proof repair is required.

For every full-column-rank \(M\in\mathbb F_2^{s\times m}\), arbitrary Boolean
\(D(y)\), affine phase, finite adaptive/pruned restriction tree on the shield
variables, and one common disjoint retained Boolean factor \(h\), the
author's bound

\[
U(Ph)-\sum_\ell w_\ell U(P_\ell h)\le4I_x(P)
\]

is correct.  For square invertible \(M\), the exact identities
\(H(P)=2m\), \(U(P)=m\), and \(I_x(P)=m/2\) are correct, giving constant 2.

## Stronger result found during review

The rectangular constant \(4\) is not optimal.  An exact cap-rank formula is

\[
U(P)=\frac{3m}{2}-
\mathbb E_{\alpha\in a+\operatorname{im}M}
\operatorname{rank}M_{\operatorname{supp}\alpha}.
\]

Choose any \(m\) independent physical rows.  Each is selected with
probability \(1/2\), and the selected-row rank dominates the number of
selected basis rows.  Therefore the expectation is at least \(m/2\), so

\[
U(P)\le m\le2I_x(P).
\]

Thus constant \(2\) holds for every full-column-rank rectangular matrix and
is sharp.  Because this strengthening was contributed by B19, it is labeled
**AUTHOR_PROVED_PENDING_FRESH_INDEPENDENT_REVIEW**; it is not counted as part
of B19's independent acceptance.

## Independent verification

The checker was written independently and does not import the author's code.
It passed:

- 45,694 exhaustive affine-support cases;
- 348,812 exact cap/rank identities;
- 182,776 exact theorem and strengthening assertions;
- 13,033 direct truth-table/Walsh reconstructions comprising 376,064 atoms;
- 500 one-step restriction tests;
- 500 branch-dependent adaptive telescoping tests;
- 1,500 direct disjoint tensor-additivity tests;
- eight exact sharpness checks.

The maximum exact \(U(P)/I_x(P)\) was \(2\).

## Scope and literature

The arbitrary \(D(y)\) includes any finite number and overlap pattern of
point-defect cylinders.  The terminal factor \(h\), however, must be common
and disjoint; shared-variable or leaf-dependent cores are not covered.

The square flat-spectrum mechanism is classical Maiorana--McFarland, and
Potapov's 18 September 2026 manuscript already treats plateaued-function FEI.
Those sources do not provide this retained-\(U\) tree statement.  No novelty
or priority claim is made.

## Remaining gap

For \(\operatorname{rank}M<m\), the Fourier atoms are coherent sums over
positive-dimensional fibers of \(D\).  The flat-support and basis-row proof
then fail.  The next unpaid step is a codimension-one fiber payment using
data-core influence plus retained terminal \(U\), without duplicating
physical credit across descendants.

Full FEI remains **OPEN**.
