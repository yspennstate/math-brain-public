# B12 / A058 — exact GU closure under reused character cores

## Outcome

**PROVED, pending independent review:** the complete `U` and `G` composition
remainders factor exactly under unlimited character-only physical reuse.

Let `Y` be a shared physical block, let the residual blocks `X_j` be pairwise
disjoint, and set

\[
g_j(y,x_j)=\chi_{R_j}(y)f_j(x_j),\qquad
F=\prod_jg_j,qquad R=\triangle_jR_j.
\]

Then

\[
\boxed{U(F)=\sum_jU(f_j),\qquad G(F)=\sum_jG(f_j),}
\]

and

\[
\boxed{I(F)=|R|+\sum_jI(f_j).}
\]

Every shared core coordinate has `Delta_i U(F)=0`, including coordinates
that occur in many factors and coordinates cancelled by even multiplicity.
The complete signed overlap remainder is therefore zero; only the realized
odd-parity core contributes the nonnegative influence reserve `|R|`.

## GU implication

For any fixed `a>=0` and `0<=b<1`, if every residual satisfies

\[
G(f_j)\le aI(f_j)+bU(f_j),
\]

then the overlapping product satisfies the same pair, with no loss:

\[
\boxed{G(F)\le aI(F)+bU(F).}
\]

For a restriction-closed residual class, the reviewed GU induction therefore
gives the entire generated overlap class

\[
U(F)\le\frac{a}{1-b}I(F),\qquad
H(F)\le\left(2+\frac{2a}{1-b}\right)I(F).
\]

This removes the fresh/disjoint shared-variable hypothesis for arbitrary
character-core reuse, without dependence on dimension, factor count,
overlap count, reuse multiplicity, cancellation count, bias, or depth.

## Proof mechanism

The realized product is `F=chi_R product_j f_j`.  Every supported Fourier set
contains exactly `R`, so both its spectral probability and its upper-set mass
factor over the residual blocks.  This proves exact `U` additivity.  A
residual restriction changes one factor, whereas restricting a core
coordinate merely removes one deterministic character and preserves `U`.
Summing the resulting physical decrements proves exact `G` additivity.

This retains the actual sign and posterior support structure.  It does not
use the refuted fixed-sign projection or any unsigned coefficient-four
indicator payment.

## Verification

`CHECK.py` directly reconstructed all Fourier laws, upper-set masses,
restrictions, `U`, `G`, and influence in:

- 5,036 exhaustive overlap cases;
- 3,000 deterministic pseudorandom cases through 12 physical variables;
- 3,456 exhaustive cases with genuine character cancellation; and
- a deterministic four-core example verifying that every supported Fourier
  set has the predicted XOR core.

The maximum factorization error was exactly zero in the recorded binary
floating evaluation.  The proof itself is analytic and all-dimensional.

Command: `python3 CHECK.py`.  Deterministic seed: `47557138434`.

## Before/after scope

- **Before:** exact `H/I` closure was known for character-only overlap, but no
  corresponding `U/G` law or GU-pair preservation had been proved.
- **After:** `U`, every physical `Delta_i U`, and `G` are exact; any GU pair
  is preserved at arbitrary reuse depth.
- **Still open:** non-character shared coordinates, where core membership is
  random and a joint signed four-channel/posterior collision term remains.

No universal pair `(a,b)` is proved here.  Universal GU and full FEI remain
**OPEN**.  Independent review is pending.

