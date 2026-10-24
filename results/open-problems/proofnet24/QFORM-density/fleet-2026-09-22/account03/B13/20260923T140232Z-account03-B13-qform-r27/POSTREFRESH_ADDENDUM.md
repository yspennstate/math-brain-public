# account03/B13 r27 post-refresh addendum — exterior-energy compression of the cross leakage

This addendum is immutable and supplements `REPORT.md`; it does not replace it.

## Newer source consumed before final publication

After the main report was written, I read the newer designated-partner theorem at

`yspennstate/math-open-problems@82f9b7e9372c2434f27fd1f5a65e7148663516a7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260923T121154Z-account04-B13-nonattained-bathtub-r1/REPORT.md`.

For every actual slab witness of ratio `rho` and every disjoint physical cross block `B=A[U,V]`, it proves

`s_5(B) <= C_5/rho`,
`C_5=10 sqrt(2e)=23.316439815971...`.                              (A.1)

It also proves the exact no-attainment positive-kernel purification, so the extremal-product reductions in the main report can use this newer theorem directly.

I also read the immediately preceding account03/B13 run

`yspennstate/math-open-problems@affec8d34501adfa2c96706fc53086e84b316a12`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T133332Z-account03-B13-qform-r27/REPORT.md`,

which identifies cap-one laws with coordinatewise 1-expanding quantile transports, pure finite-union extremals with monotone gap maps, and the common Hessian `2A` on every fragment cell. The present canonical-fiber-core mechanism is complementary: it localizes positive **slab mass**, while that run removes fragment positions from the Hessian.

## A. Rank-four compression of physical cross leakage

Let `B` be the physical `U`-to-`V` block used in the main report. By Eckart--Young and (A.1), there exists a deterministic matrix `H` of rank at most four such that

`||B-H||_op=s_5(B)<=C_5/rho`.                                     (A.2)

This is a coefficient decomposition only; no random coordinates are rotated.

Fix a leaf spectral threshold `tau`, projection `P=P_tau`, and retained curvature `R_tau` as in the main report. Use the exact-range model cross matrix

`B_0=H P`.                                                        (A.3)

Then

`row(B_0) subset range(P)=range(R_tau)`                           (A.4)

and

`B-B_0=(B-H)+H(I-P)`.                                             (A.5)

Put

`eta_tau:=||H(I-P)||_op`.                                         (A.6)

On the canonical half-slab core with Euclidean radii `R_U,R_V`, the full centered model error therefore obeys

`|Q-Q_0|
 <= tau R_V^2
    +2(eta_tau+C_5/rho)R_U R_V
 =:Delta_tau^(4).`                                                (A.7)

If `d_tau>=3` and `max_j(P_tau)_{jj}<=1/2`, account01/B13's exact range theorem applies to `(R_tau,B_0)` and gives

`boxed:
 rho <= 2 M_tau
  [1+2 Delta_tau^(4)/|J|],
 M_tau=[4d_tau/(d_tau-2)]|pdet R_tau|^(-1/d_tau).
`                                                                    (A.8)

Thus, for `Lambda_tau=|pdet R_tau|^(1/d_tau)>=1`,

`boxed:
 rho <=24
 [1+2 tau R_V^2/|J|
    +4 eta_tau R_U R_V/|J|
    +(4 C_5/rho)R_U R_V/|J|].
`                                                                    (A.9)

This is an actual use of the newer account04/B13 exterior-energy inequality inside the new spectral-range slab compiler.

## B. Explicit moderate-spread consequence

If the canonical half-slab core satisfies

`R_U R_V <= rho |J|/(8 C_5)`,                                    (B.1)

then the partner-controlled rank-`>=5` cross remainder contributes at most

`2(C_5/rho)R_U R_V <= |J|/4`                                    (B.2)

to `Delta_tau^(4)`.

Therefore, in the diffuse retained-range branch with `Lambda_tau>=1`, any slab ratio `rho` much larger than the universal model constant can only survive through

`tau R_V^2 +2 eta_tau R_U R_V`,                                  (B.3)

where `H(I-P)` has rank at most four. In words: after the designated partner theorem is inserted, the cross-range obstruction on positive slab mass is no longer arbitrary-dimensional. It is a **bounded-rank (<=4) misaligned cross piece**, plus an explicit `rho^{-1}` error already charged on the canonical slab core.

This produces the refined missing implication

`QFORM-RANK4-MISALIGNMENT-OR-STAR-CLOSURE-v1`:

> combine the bounded-rank misaligned piece `H(I-P)` with the high-leverage physical principal-volume star from Theorem 5.1 of the main report, or show that its slab-core effect activates a completed grouped-bank/ridge or bordered-volume estimate. The rank-`>=5` cross remainder is already quantitatively negligible whenever (B.1) holds.

No small coefficient matrix is deleted globally. Every error term is retained in (A.7) and charged on a set carrying at least half of the actual slab mass.

Full QFORM and full continuity remain OPEN.
