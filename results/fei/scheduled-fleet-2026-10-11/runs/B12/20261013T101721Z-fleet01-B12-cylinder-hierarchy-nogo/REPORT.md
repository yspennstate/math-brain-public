# B12 / A057 — unbounded-depth cylinder obstruction

**Run:** `20261013T101721Z-fleet01-B12-cylinder-hierarchy-nogo`  
**Primary packet:** A057 (Coherent restriction remainder)  
**Gap:** `B12-A057-COHERENT-HIERARCHY-v16`  
**Status:** universal hierarchy helper REFUTED; full FEI OPEN.

## Mathematical delta

The B19/A091 review previously gave a two-level counterexample to the claimed
`8 ln(2)` full-influence hierarchy telescope.  This run upgrades that finite
violation to an all-depth parametric obstruction: under the literal
pathwise-nonreuse hypotheses, **no finite constant can work**.

Take the three parallel point cosets `{000},{001},{010}` and their selector
splice.  Its local associator is exactly
\[
 \Omega_0=
 \frac{169\ln13-45\ln3-100\ln5-256\ln2}{128}
 =0.356636085579521\ldots>0,
\]
with the exact positivity certificate
`13^169 > 3^45 5^100 2^256`, while `I(d_0)=1/4`.

Adjoin `L` dummy physical coordinates and query them sequentially.  Every
reached source is unchanged, each coordinate is queried at most once on a
path, and the weights on each depth sum to one.  Therefore
\[
 \sum_vw_v\Omega_v=L\Omega_0,qquad I(d_L)=1/4,
\]
so the ratio equals `4 L Omega_0` and diverges.

## Consequence for the planned repair

The naive directional-owned-block strengthening is also false when the owned
block is the newly queried block: every dummy query has zero directional
influence but positive local associator.  Merely replacing complete influence
by query-coordinate influence cannot repair the Bellman step.

The hierarchy must instead alter its event accounting:

1. charge only when the composition/activation structure genuinely changes;
2. prove disjoint ownership of the full active derivative support; or
3. carry a terminal reserve that is preserved, not charged again, across
   unchanged cylinder restrictions.

This sharply separates the valid one-node theorem from the invalid repeated
charge.  The local `8 ln(2)` bounds remain intact.

## Verification

`check_cylinder_no_go.py` reconstructs the base Walsh spectra at 90-digit
precision from exact rational coefficients, checks `I(d_0)=1/4`, verifies
the integer positivity certificate, and explicitly builds and restricts the
dummy cylinders through depth eight.  It checks zero dummy-coordinate
influence and the exact linear weighted-charge law.  Randomness: none.

The all-depth claim is analytic; the finite run corroborates the construction.

## Scope

This refutes only the literal helper statement
`sum_v w_v Omega_v <= C I(d)` under pathwise coordinate nonreuse.  It is not
a Boolean FEI counterexample: dummy variables change neither entropy nor
influence of the actual output.  Full FEI remains open.

## Next unpaid step

Reformulate the adaptive ledger so unchanged cylinder nodes incur zero new
associator charge.  Then derive the exact event-local charge for the first
restriction that changes the affine quotient geometry, retaining the terminal
reserve until that event.  Any candidate must reproduce the present cylinder
family with equality zero at dummy steps.

