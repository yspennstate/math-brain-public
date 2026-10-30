# B19 independent review: biased activation-tower retained credit

## Result

**Primary packet:** A094 (proof-chain challenger)  
**Reviewed packet:** A023 (B05 amortized rarity budget)  
**Attempt:** `B19-A094-BIASED-TOWER-REVIEW-01`  
**Stable gap:** `B05_RARE_REFUNDS`  
**Verdict:** **INDEPENDENTLY ACCEPTED AT DECLARED SCOPE**

I independently reconstructed B05's scalar lemma, exact activation
recurrences, depth-uniform endpoint induction, and common-disjoint-core tree
telescope. No repair to the mathematical claims was needed.

The accepted theorem is:

> For every Boolean base `P`, every `c>=48/35`, and every finite `d`, if
> `U(P)<=cI(P)`, then the fresh-variable tower
> `F_1=A(wP)`, `F_k=A(B_kF_{k-1})`, with fair selectors and the fixed two-bit
> balancer `E B=-1/2`, satisfies `U(F_d)<=cI(F_d)`. For every finite adaptive
> or pruned tree querying tower variables and every one common disjoint
> terminal core `h`,
> `U(F_dh)-sum_l w_l U((F_d)_l h)<=cI(F_d)`.

The preceding independently accepted dense nullity-two shield theorem supplies
`c=2`, hence this tower family has `U<=2I` and, through the generic bridge,
`H<=6I` uniformly in dimension, shield orientation, coherent base core, tower
depth, activation rarity, reveal order, and pruning.

## Exact proof audit

1. The Fourier expansion of `A(q)` gives the exact identity
   `U(A(q))=U(q)/2+R(Eq)` and the claimed influence rule.
2. On `[-1,0]`, `R'''<0`; the endpoint derivatives force one interior minimum,
   so `R(t)<=max(R(-1),R(0))=1`.
3. The means obey `m_1=1/2` and `m_k=1/2-m_{k-1}/4`, hence
   `3/8<=m_k<=1/2`.
4. The deficit recurrence is
   `D_k<=D_{k-1}/2+3/2-(35/32)c`; the scalar term is nonpositive at
   `c>=48/35`.
5. The tree claim is an exact root-minus-leaves telescope. The common disjoint
   terminal packet cancels by tensor additivity; leaf `U>=0` leaves the endpoint
   bound.

The complete derivation is in `PROOF_REVIEW.md`.

## Independent finite reconstruction

`INDEPENDENT_CHECK.py` uses a direct, naive Walsh transform rather than the
author's FWHT implementation. It certified:

- all 278 Boolean truth tables in dimensions 0 through 3;
- 1,668 recurrence equalities;
- 524 eligible endpoint inequalities at `c=48/35`;
- 1,112 fixed-subset restriction-tree payments;
- 28 rare one-point-defect tower regimes;
- tensor additivity for `U` and `I`; and
- an explicit restriction non-closure witness.

Maximum recurrence error was `2.220e-15`; all assertions passed. These finite
checks are corroboration, not the all-parameter proof.

## Scope correction and class extension

The theorem supplies genuine movement beyond one-node rare cancellation: it
gives a depth- and rarity-independent retained-credit bound for a nested
negative-half biased tower over any endpoint-valid base, including arbitrary
dense-nullity-two shield cores.

The accepted quantifier is nevertheless narrower than an arbitrary hierarchy.
It requires:

- fresh disjoint variables at every level;
- fair activation selectors;
- one fixed balancer with mean `-1/2`;
- one common terminal core on a disjoint block; and
- an endpoint-valid base.

It does not cover biased outer selectors, reused variables, balancer means
approaching `+/-1`, leaf-dependent terminal cores, or coherent cores that
change through an overlapping hierarchy. The tower class is not
restriction-closed. The constant `48/35` is accepted as sufficient, not sharp.
The tree argument is not a nodewise single-use-credit theorem.

## Literature check

O'Donnell--Tan's 2013 composition theorem assumes disjoint inner blocks and a
product-biased outer FEI hypothesis; it does not provide this `U` recurrence or
cover shared-variable changing cores. Potapov's September 2026 plateaued paper
proves FEI for plateaued and partially bent classes but does not state this
upper-set retained-credit theorem. Details are in `LITERATURE_SCOPE.md`.

## Evidence and provenance

- Reviewed B05 final bundle:
  `yspennstate/math-open-problems@748f7eb102bb43b98f8b184729594601beb22c7c`,
  `reports/fei-2026-10-11/runs/B05/20261013T192810Z-fleet01-B05-biased-tower-retained-credit-a023/`.
- Reviewed B05 core package commit:
  `8246508874ee972c8761212b12e42931d8f890fc`.
- Brain mirror core commit:
  `bf70e14e86ef2a63a975f1a9bfa5a73f8082467c`.
- Previously accepted base review:
  `yspennstate/math-open-problems@b10d0889f9a326b40fe1028af9d8ebf936967367`,
  B19 run `20261013T145232Z-fleet01-B19-dense-nullity-two-review-a094`.
- Primary literature:
  O'Donnell--Tan arXiv:1304.1347; Potapov arXiv:2609.21563.

## Status and next unpaid step

The three B05 version-1 claims may be consumed as independently accepted at
the scope above. Packet A023 remains **IN PROGRESS** because its universal
criterion is not met. Full FEI remains **OPEN**.

The next useful attempt should replace the common-disjoint-core cancellation
with a quantitative transport for changing coherent cores, and must survive
shared variables, variable balancer bias, and leaf-dependent terminal spectra.
An endpoint telescope alone cannot pay those mismatches.
