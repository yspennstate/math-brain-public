# Fresh-control addendum — robust numerator third compound becomes one finite physical bank packet

Programme `QFORM-DENSITY-3EIG-20260922`; run `20260923T000441Z-account01-B07-QFORM-r13`.

This addendum was written after the final-control refresh exposed the newer OTHER-account result account03/B07 `20260923T000734Z-account03-B07-qform-r20`, canonical mathematics

`yspennstate/math-open-problems@391688138f7f481a2c8688c2d27f9508db7af6af`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T000734Z-account03-B07-qform-r20/REPORT.md`.

That result proves the exact original-coordinate coloring probabilities for all four overlap classes of a third compound. Its coloring argument is homogeneous: if a symmetric matrix `M` has total third-compound mass `C_3(M)` and `O_q` is its overlap-`q` component, then a lower bound on `O_q` scales linearly through the same coloring.

Apply it to the Schur numerator `N=dC-ww^T` in the robust branch of the main report. There

`C_3(N)>=L^3/12288`, `L=||N||_F^2>c0:=1/(3sqrt(200))`.

Since `C_3=O_0+O_1+O_2+O_3`, some `O_q>=C_3/4`. Therefore one of the following ORIGINAL-coordinate finite-bank packets exists:

1. `q=0`: six disjoint banks, accepted squared-third-minor mass at least

   `O_0/1296 >= C_3/5184 > c0^3/(12288*5184)`

   `=2.055630471496127e-13`.

2. `q=1`: five disjoint banks, accepted mass at least

   `(4/3125) O_1 >= C_3/3125 > c0^3/(12288*3125)`

   `=3.410044276555495e-13`.

3. `q=2`: four disjoint banks, accepted mass at least

   `O_2/128 >= C_3/512 > c0^3/(12288*512)`

   `=2.081325852389829e-12`.

4. `q=3`: three disjoint banks, accepted mass at least

   `(2/9) O_3 >= C_3/18 > c0^3/(12288*18)`

   `=5.920215757908845e-11`.

This strictly sharpens the robust-third-compound endpoint in the main report: **there is no longer an amorphous shared-overlap remainder.** Every robust `C_3(N)` state supplies one of four constant-mass, bounded-cardinality, original-coordinate packet types. The disjoint packet is already paid more sharply by the fair-cut argument in the main report (which yields `E_3>=C_3/256` and the density bound `<87.380`). The new information matters for `q=1,2,3`.

For `q=2`, the same account03/B07 result supplies the exact two-pivot Schur rung. For each physical pair `H`, whenever `N[H,H]` is invertible,

`sum_(r,c notin H) det N[H union {r},H union {c}]^2
 = det(N[H,H])^2 ||Schur_H(N)||_F^2`.

Singular pairs are kept as a distinct packet rather than divided through. For `q=1`, the already completed scalar identity turns a genuine shared pivot into pivot-square times the second compound of its exact Schur remainder, again with exact-zero pivots split off. Thus the robust branch now ends at finite product-preserving receivers, not at an overlap classification problem.

The updated first unpaid implication is correspondingly narrower:

`QFORM-NUMERATOR-RANKTUBE-OR-FINITEBANK-RECEIVER-v1`:

- pay the near-rank-one and near-rank-two numerator tubes without deleting their small singular directions; and
- pay the `q=1,2,3` constant-mass finite-bank packets through the exact-zero/genuine-Schur ladders, preserving original-product provenance.

This addendum does not promote any packet to a density theorem without its analytic receiver. Full QFORM and full continuity remain OPEN.
