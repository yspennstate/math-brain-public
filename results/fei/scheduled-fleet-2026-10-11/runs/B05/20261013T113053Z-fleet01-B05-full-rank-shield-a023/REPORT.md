# B05 / A023 — full-rank shielding removes all finite defect-count dependence

## Outcome

**AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW.**  A full-rank affine-bilinear
control does more than pay two intersecting point-defect cylinders: it
shields an arbitrary Boolean coherent core \(D(y)\).  The squared Fourier law
is exactly flat, independently of \(D\).

For square invertible \(M\), the exact ledger is

\[
 H(P)=2m,\qquad U(P)=m,\qquad I_x(P)=m/2,
\]

and every adaptive/pruned restriction tree on the shield variables satisfies

\[
 U(Ph)-\sum_\ell w_\ell U(P_\ell h)\leq2I_x(P).
\]

For rectangular full-column-rank \(M\), the same class satisfies the bound
with constant \(4\).  Both constants are independent of dimension, bias,
defect count, cylinder overlap, tree depth, reveal order, leaf probability,
and arbitrary disjoint terminal core \(h\).

## Precise class extension

The preceding B05 theorem covered one point defect with arbitrary bilinear
rank at constant \(25/4\).  This run resolves the advertised next case—two
intersecting defect cylinders—and every finite or parametric number of them,
provided the bilinear map has full column rank.  More strongly, it permits
every Boolean \(D(y)\), not only a product or union of point defects.

This matters because the earlier obstruction was intersection of the
exceptional upper filters.  Here the exact signed node charges telescope to
one root reservoir of size \(U(P)\), so those filters are never charged
separately.  The physical \(x\)-pivotal events fund that reservoir once.

## Proof mechanism

Summing first over \(x\) forces \(My=a+\alpha\).  Full column rank makes this
fiber a singleton, so every nonzero Fourier coefficient has magnitude
\(2^{-m}\), whatever signs \(D\) places on the points.  In the square case
the support is the full \(2m\)-cube, giving \(U=m\) exactly.  In the
rectangular case \(U\leq H=2m\).  At least \(m\) physical selector rows are
nonzero and each contributes influence \(1/2\).

For the tree, the complete signed node charge is exactly
\(U(P)-\sum w_\ell U(P_\ell)\), hence at most \(U(P)\).  Tensor additivity of
\(U\) cancels the same arbitrary disjoint terminal \(h\) at root and leaves.
This also proves equality of the control-first and data-first endpoint
ledgers: reveal order changes the intermediate charges, not their sum.

## Verification

`CHECK_FULL_RANK_SHIELD.py` uses integer Walsh transforms.  It exhausts every
Boolean core and every invertible matrix for \(m\leq3\), exhausts smaller
rectangular instances with affine phases, checks seeded larger rectangular
instances, and separately checks products of two and three point-defect
cylinders.  The analytic proof does not depend on the finite check.

## Literature/scope guard

The flat-spectrum construction is the standard Maiorana--McFarland bent
mechanism.  Potapov's September 18, 2026 plateaued-function manuscript proves
an FEI bound for plateaued classes.  This report does not claim either fact
as new.  Its exact claim is the nonlocal complete-tree retained-\(U\) payment
and the arbitrary-core/cylinder-independence at full rank.

## Remaining unpaid step

When \(\operatorname{rank}M<m\), each surviving Fourier atom contains a
signed sum over a positive-dimensional fiber of \(D\).  Arbitrary coherent
cores can then interfere, and this proof supplies no dimension-independent
control by the available selector influence.  Next: freeze the codimension-
one fiber functional, compute its exact upper-set mismatch, and determine
whether data-core influence plus retained terminal \(U\) pays it once.

Full FEI remains **OPEN**.
