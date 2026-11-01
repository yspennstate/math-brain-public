# B20 / A096 — critical pruning synthesis

**Status:** one new exact structural lemma proved; complete saved inputs
reconciled at their actual review state. **Full FEI remains OPEN.**

## Mathematical movement

For a physical split at coordinate `i`, let `Delta_i H` be the entropy drop,
`d_i=I_i(f)`, and `R=H(f)/I(f)`.  If `Hbar,Ibar` are the averages of the two
children, then

```
Hbar - R Ibar = R d_i - Delta_i H.
```

Therefore, whenever `Delta_i H/d_i < R`, an actual nonconstant child has
strictly larger `H/I`.  A descendant-critical source must consequently obey

```
Delta_i H >= R(f) I_i(f)
```

at every relevant coordinate.  An `eta`-critical source has the quantified
version `Delta_i H >= R d_i - eta Ibar`.

For a fixed proposed FEI constant `C`, a minimum-dimensional counterexample
has the stronger property

```
Delta_i H - C I_i(f) >= H(f)-C I(f) > 0
```

for every coordinate, and it is prime under disjoint nonconstant tensor
factorization.  These conclusions use actual physical descendants, so the
pinned abstract support-component counterexamples do not apply.

## Cross-route consequence

The complete B01/A005 artifact proves that every fresh activation control in
the A002 hardness sequence has step ratio tending to `4`, while the global
ratio tends to the seed ratio.  For any seed ratio greater than `4+epsilon`,
the activated function therefore has a control with step ratio below its
global ratio.  The new identity supplies a higher-ratio physical child (the
active child, since the other child is constant).  Thus the embedding preserves
global `H/I` and downward `L/I`, but cannot itself be a descendant-critical
high-ratio endpoint above four.

This is the exact substitution connecting B01's endpoint audit to B11's
critical-source theorem.  It does not prove constant four: addressing and
one-point defects approach the boundary, while B05's rare-refund obstruction
shows why uncontrolled local estimates remain invalid away from a critical
endpoint.

## Evidence reconciliation

- B01/A005 is complete and byte-identical in the canonical and Brain paths;
  both new claims are contributor-proved, deterministically checked, and
  pending A086/A094 review.
- B11/A052 is complete in both repositories and byte-readback verified; its
  tensor-purity theorem is pending A090/A094 review.
- B20's prior terminal-compensation identity remains proved and saved; the B19
  strict-sign strengthening it consumes still needs a fresh reviewer.
- B07/A034 has a complete-looking canonical bundle, but this run did not find a
  verified Brain mirror.  It is recorded as incomplete delivery and not adopted
  as a complete saved result.

`LIVE_GAP_LEDGER.json` records source pins, review states, retired statements,
and nonoverlapping next actions.

## Verification

`python3 verify_critical_pruning.py` checks the exact split identity and
critical implication over all 14 nonconstant two-bit Boolean truth tables,
plus exact deficit additivity.  The all-dimensional theorem is the analytic
proof in `NEXT_LEMMA_DERIVATION.tex`.

## Remaining obstacle

The nearest unpaid lemma is now:

> Bound `min_i Delta_i H / I_i(f)` by a universal constant on
> descendant-critical, tensor-prime Boolean sources, or construct a genuine
> critical family for which this minimum diverges.

Qualitative connectedness or nonfactorization is insufficient because the B11
one-point-surgery embedding retains arbitrary core ratios.  A viable proof must
use the quantitative critical inequalities at every physical coordinate.

Independent review is pending; no packet is marked accepted or full FEI solved.
