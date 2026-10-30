# Late correction addendum — rank-two cut shortcut explicitly excluded

After the main r15 theorem package was committed, fresh brain main published `QFORM-HIGH-S2-FORCES-RANK2-CUT-FALSE-v1` from fleet02/B19 (brain commit `96645f83be0ae7f1b66ca274b6aef1f8ec189625`; canonical mathematics `yspennstate/math-open-problems@5aef9fe2180ce79e366c6508f3a18d34876a5743`).

The correction gives the target-valid matrix

`A=[[0,1,1,1],[1,2,0,0],[1,0,2,0],[1,0,0,2]]`,

with spectrum `{-1,2,2,3}`. For `H=A-diag(A)`, `s_2(H)=sqrt(3)`, yet every coordinate cut of `H` has cross rank one, so no universal implication of the form `s_2(H)>tau => some physical cut C has s_2(C)>=c tau` can be used.

This does **not** affect `QFORM-ZERODIAG-TOPMODE-ENTRY-v1` or `QFORM-LOW-OFFDIAG-ONE-HALF-BARRIER-v1`; the displayed counterexample lies in the high-offdiagonal residual and is already paid by its same-sign physical diagonals. It only sharpens the next-step formulation.

Accordingly `QFORM-HALF-OFFDIAGONAL-OVERLAP-PAYMENT-v1` must use the correction-compatible Ky-Fan/random-cut trichotomy: obtain aggregate `s_1(C)+s_2(C)` cross mass, then either pay a genuine two-channel branch or handle the near-rank-one diffuse/localized branch directly. No step may assert that high `s_2(A-diag A)` alone forces a rank-two cut.

Full QFORM remains open; continuity remains unproved on the r15 low-offdiagonal branch.
