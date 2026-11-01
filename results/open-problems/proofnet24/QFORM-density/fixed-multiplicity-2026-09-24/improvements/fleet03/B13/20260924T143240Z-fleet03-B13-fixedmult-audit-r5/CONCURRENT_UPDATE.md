# Concurrent source reconciliation — nine-direction constant 2506

Run: `20260924T143240Z-fleet03-B13-fixedmult-audit-r5`.

After this run's immutable `IMPROVEMENT.md` and audit report were committed, fleet03/B14 published a newer source-pinned sharpening:

- commit `83a4f3cc8a6f45e13555226fb97b5e6e1483c782`;
- theorem `QFORM-NINE-FEJER-2506-v1`;
- conclusion `s_9(A)>=s>0 => ||p_Q||_(infinity,ess)<2506 K^2/s`, with a canonical `C_0` representative supplied by the separately completed affine fixed-instance regularity theorem.

This supersedes the numerical constant `2582` used in Section 4 of this run's earlier immutable improvement artifact. It does **not** change the new multiplicity-eight obstruction proved in that artifact.

Applying the designated fleet04/B13 no-attainment purification theorem (`math-open-problems@d9f6bcd057b7804ea7ba06fea8dad5f54e357990`) to the updated slab kernel gives the actual current extremal-product statement

```
sup_{0<=f_i<=1, int f_i=1}
  P{x^T A x+b^T x+c in I}
=
sup_{|E_i|=1}
  |{x in prod_i E_i : x^T A x+b^T x+c in I}|
<2506 (K^2/s) |I|
```

with the usual normalization/scaling understood. Bounded finite-union product sets may be used as epsilon-witnesses, but there is no single-interval, centered-uniform, bounded-diameter, or fixed-fragment-count extremality claim.

Current status after reconciliation: threshold nine has the newer `<2506 K^2/s` source-backed candidate; multiplicity eight remains open; the unrestricted three-eigenvalue QFORM conjecture remains open.
