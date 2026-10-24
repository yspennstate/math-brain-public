# B05 / A023 — negative near-constant point-defect retained credit

## Result

**AUTHOR PROVED, INDEPENDENT REVIEW PENDING.**

For `N_r=-Q_r`, where `Q_r` is `+1` except at one point, define on fresh
disjoint variables

\[
F_1=A(wP),\qquad F_k=A(N_{r_k}F_{k-1}),\qquad r_k\ge2.
\]

This run proves the all-rank, all-depth closure

\[
U(P)\le\frac{16}{9}I(P)
\Longrightarrow
\boxed{U(F_d)\le\frac{16}{9}I(F_d)}.
\]

It also proves that every finite adaptive/pruned restriction tree on the
physical tower variables, with any one common disjoint terminal Boolean core
`h`, obeys

\[
\boxed{U(F_dh)-\sum_lw_lU((F_d)_lh)\le\frac{16}{9}I(F_d)}.
\]

Thus `H(F_d)<=50I(F_d)/9`.  Constants are independent of base dimension,
rank sequence, negative bias approaching `-1`, activation probability, depth,
reveal order, pruning, and common terminal-core complexity.

## Mathematical delta

- Previous negative point-defect endpoint: `U<=56I/27` from the B01
  reflection argument; no separately recorded sharp retained-tree theorem for
  this sign-flipped arbitrary-rank family.
- New endpoint and tree loss: `U<=16I/9`, improving `56/27` to `16/9`.
- Newly covered class: arbitrary finite sequences of negative near-constant
  point defects, including biases tending to `-1` and arbitrarily rare
  terminal activation.

The decisive observation is that the exact mean recursion keeps
`m_k in [1/4,1/2]`.  Hence the input to the accepted negative-side scalar is
`-s_k` with `s_k>=1/8`.  The accepted cap `R(-s)<=1` is then fully paid by
the physical selector influence at coefficient `16/9`.  The defect block
itself satisfies the stronger `U(N_r)<7I(N_r)/4` for `r>=4`, with the two
small ranks checked analytically.

## Verification

`PROOF.md` gives the complete analytic proof.  `CHECK.py` independently uses
integer/rational Walsh arithmetic for direct towers, verifies exact state
recurrences, tests both reveal orders in pruned trees, and checks cancellation
of a common disjoint terminal factor.  The executed output is in `CHECK.out`.
The numerical work is corroborative; the theorem is analytic.

## Source pins

- control revision: `40210272c19f43fed84f6a67653f9a04b0e11e28`;
- accepted negative-side scalar source package: canonical
  `748f7eb102bb43b98f8b184729594601beb22c7c`, independently reconstructed in
  repository state `65b51cca2b512ecb514e83de5a2ec68088cac78d`;
- prior negative point-defect theorem: `0a36d53f1ae1e53c96f29a0128c54003570576b0`;
- positive-tower scope correction used for wording:
  `f9e5ba18eb5860b3c985ca2a1e983ddc851e29d0`.

## Scope and remaining unpaid step

This is a proper-class endpoint telescope, not the A023 first-revelation
credit-ownership mechanism and not a universal upper-set payment.  It assumes
fresh disjoint blocks, fair selectors, an endpoint-valid base, and one common
disjoint terminal core.  The next unpaid step is to control a changing or
overlapping coherent core through the hierarchy (or to produce a certified
falsifier), while retaining the signed `B_i-Gamma_i+KL_i` ledger.  Full FEI
remains **OPEN**.
