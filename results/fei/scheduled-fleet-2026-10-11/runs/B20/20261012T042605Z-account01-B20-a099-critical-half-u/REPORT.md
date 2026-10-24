# B20 / A099 — fixed half-restriction criterion for full FEI

**Run:** `20261012T042605Z-account01-B20-a099-critical-half-u`  
**Primary packet:** A099 (Candidate assembly)  
**Attempt:** `A099-CRITICAL-HALF-U-2`  
**New claim:** `B20-A099-CRITICAL-HALF-U-v1`  
**Open leaf:** `G-CRITICAL-HALF-U-v1`  
**Status:** fixed-scale equivalence PROVED pending independent review; the half-restriction bound and full FEI OPEN.

## Mathematical movement

The previous assembly isolated the critical rectangle decrement, while B11
subsequently proved that critical deficit converts into persistence of the
FEI-equivalent upward potential `U` on physical restriction frontiers.

This run turns that persistence theorem into a single fixed-scale full-FEI
criterion. It removes the need to control all Boolean functions, all
restriction depths, all biases, or even individual children.

Define `CHR_U(K)` as follows: for every `n>=2` and every maximizer `f` of
`H/I` on the `n`-cube, retain each coordinate independently with probability
`1/2`, assign the others uniformly, and require

`E U(f_{J,X}) <= K E I(f_{J,X}) = K I(f)/2`.

Then

`CHR_U(K) => H(f) <= (2+2K+2/ln 2) I(f)`

for every Boolean `f`. Conversely, FEI with constant `C` implies `CHR_U(C)`.
Thus full FEI is equivalent to a dimension-independent `U/I` bound only in
influence-weighted average on the half-restriction frontier of actual finite
maximizers.

## Constant derivation with all terminal terms

For a maximizer of ratio `c_n`, let
`delta(g)=c_n I(g)-H(g)` on its physical restrictions. The audited deficit
theorem gives `E delta <= I(f)/ln 2` at half retention, and exact influence
transport gives `E I(g)=I(f)/2`.

The full upward inequality gives

`E U(g) >= (c_n-2)I(f)/4 - E delta/2 + E Var(g) + E b(g)/2`,

where `b(g)=(1-Var(g))log2(1/(1-Var(g)))`. Combining with `CHR_U(K)` yields

`c_n <= 2+2K+2/ln 2 - [4 E Var(g)+2 E b(g)]/I(f)`.

The stated universal constant drops only the two displayed nonnegative
terminal corrections. No normalization or endpoint term is silently erased.

## Why the unpaid inequality is genuinely narrower

`U(g)<=K I(g)` for every Boolean `g` is not assumed. `CHR_U` requires:

- only `H/I` maximizers;
- only one fixed scale `t=1/2`;
- only an averaged bound;
- only genuine physical restrictions;
- no individual-child estimate.

This is still equivalent to FEI, but its quantifier set is materially smaller
and directly exposes the next analytic object: averaged upper-set asymmetry and
KL mismatch on the half-restriction frontier.

## Verification and controls

`python3 verify_half_restriction.py` enumerates every Boolean truth table
through four variables, locates every `H/I` maximizer, and checks exact
influence transport, the known deficit estimate, the retained-terminal lower
bound, and the constant transfer.

The finite check is diagnostic. The all-dimensional theorem is the written
algebra in `CANDIDATE_MANUSCRIPT.tex`.

Mandatory controls:

- constants and terminal restrictions contribute zero consistently;
- point defects and read-once formulas may saturate the upward inequality, so
  no coefficient was improved;
- tensor products are not declared prime or discarded; maximization and
  physical restriction are the only reductions used;
- rare restrictions retain their logarithmic costs inside `U`;
- no selector, address, overlap, or correlation-gap class assumption enters;
- no free spectral probability law substitutes for Boolean realizability.

## Exact remaining leaf and allocation

`G-CRITICAL-HALF-U-v1`: prove an absolute `K` such that `CHR_U(K)` holds.

- **Derivation:** A001/A052 should express `E U(f_{J,X})` at `t=1/2` through
  the exact `B-Gamma+KL` restriction identity and seek a one-use aggregate
  asymmetry payment.
- **Falsification:** A047/A092 should attack the frozen half-scale statement on
  prime critical near-tensors, high-arity compositions, rare surgery and
  addressing with shared inputs. Unbounded local `Delta_i U/Inf_i` alone is
  not a falsifier.
- **Audit:** A087/A090/A094 should independently reconstruct the deficit
  theorem, full terminal upward inequality and constant transfer.

This replaces no existing route; it gives them a common fixed target.

## Bounded inter-dot adoption reconciliation

The already-sent B20 follow-up is source-bound and was not duplicated. Fresh
inspection found only the two account01/control receipts in the shared receipt
directory and no recipient-authored native adoption receipts for the intended
other 60 schedules. Actual verified coverage therefore remains **20 local**;
the other **60 are intended but unverified**. Transport and unread-index state
are not counted as adoption.

## Sources actually used

- Owner overlay revision `2026-10-12.1`, source commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- B20 contract and A099 acceptance criteria, current `master`.
- U-universal notes blob `3b0636c653c7818368eeb204011c3e1ff21c234e`:
  full Theorem G and Theorem C(ix).
- U-route referee blob `87326516f71374bb2b37d593952be7ec581ee0f1`.
- B11 critical-frontier proof, canonical commit
  `e412fb2e8f85a78d807ff6d6c9c805254377ed88`.
- Previous A099 rectangle-payment report blob
  `a04af253e79d127dc13a8305a7933002072314cb`.
- Adoption status blob `b2c4fb2e0ab8a2f88fdc1bdba1230488a32f6439`.

No literature novelty claim is made. Independent review has not occurred.
Full FEI remains **OPEN**.

## Persistence receipts

The ten-file canonical package was committed at
`1368d997d11513254042bc6e0578a2289e7e3c1c`; the complete Brain mirror was
committed at `cf3cbbd33d8c69fdbc295c49dd736e39f030f5c5`. All twenty repository/file
readbacks were nonempty and matched the local Git blob SHAs. These receipts
establish durable delivery only, not independent review or acceptance.

