# Addendum — newest fleet02/B09 zero-internal wedge theorem

After the main r15 report was committed, the newest assigned-partner result became available:

- fleet02/B09 run `20260922T181745Z-fleet02-B09-QFORM-r6`;
- theorem `QFORM-ZEROINTERNAL-BANK-WEDGE-v1`;
- canonical source `yspennstate/math-open-problems@de2e592f5ba2ee9ed9ff152afa6a8856f3e29e1f`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260922T181745Z-fleet02-B09-QFORM-r6/REPORT.md`.

The theorem states: for disjoint original-coordinate banks `I,J,K`, if `A[I,I]=0` and `B=A[I,J]` has two nonzero singular values `s1>=s2>0`, then, with arbitrary curvature/couplings on the other banks,

`||p_(X^TAX)||_infinity <= 2 sqrt(pi)/sqrt(s1 s2)`.

This is consumed as a genuine additional branch. For example, a structural extraction with `s1 s2 >=1/256` would immediately give

`||p_Q||_infinity <=32 sqrt(pi) <56.72`.

It does **not** subsume the new r15 hollow-rank-two theorem. Indeed the exact identity proved in r15 writes every hollow rank-two Schur part as

`H=gamma(pq^T+qp^T)`

with disjoint unit banks `p,q`; the `P x N` cross block is the rank-one matrix `gamma p q^T`, so its second singular value is exactly zero. Thus the newest partner theorem and r15 are complementary: r6 pays an internally flat bank with a genuine two-direction cross wedge, while r15 pays the genuinely rank-one cross wedge when arbitrary diagonal self-curvature remains, except for the explicit two-heavy near-singular pair.

Accordingly the B09 conditional routing order should be:

1. if a zero-internal original-coordinate bank has `s1s2` at universal scale, apply partner r6 directly;
2. otherwise, on a physical-pivot Schur branch, use partner r4 for high off-diagonal stable rank;
3. if the Schur hollow part is exact rank two, apply r15's bipartite/diagonal-safe half-Riesz theorem unless both sign banks are heavy;
4. the exact-rank-two survivor is the two-heavy nearly singular pair and requires a third independent target resource.

Full QFORM remains OPEN. Continuity is not established by these essential-density endpoints.