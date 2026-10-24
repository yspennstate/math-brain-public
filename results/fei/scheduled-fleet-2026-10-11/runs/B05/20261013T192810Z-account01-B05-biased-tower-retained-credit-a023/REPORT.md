# B05 / A023 — biased-tower retained credit

## Outcome

**AUTHOR_PROVED_RESTRICTED_ALL_DEPTH_THEOREM_PENDING_INDEPENDENT_REVIEW.**

The preceding B05 theorem supplied (U(P)\le2I(P)) for every dense
nullity-two bilinear shield with arbitrary Boolean coherent core.  The
preceding B01 theorem supplied a biased AND-balancer tower but used the
coarse endpoint threshold (72/35).  This run proves the sharper one-sided
scalar lemma (R(t)\le1) for (t\in[-1,0]) and obtains the invariant
threshold

\[
\boxed{c\ge48/35.}
\]

For every Boolean base (P) with (U(P)\le cI(P)), define

\[
F_1=A(wP),\qquad F_k=A(B_kF_{k-1}),
\]

where (w) is a fresh fair character, every (B_k) is a fresh two-bit AND
sign of mean (-1/2), and every (A) uses a fresh fair selector.  Then

\[
U(F_d)\le cI(F_d)qquad(d\ge1).
\]

Consequently every finite adaptive/pruned restriction tree on the physical
tower variables, with any common disjoint Boolean terminal core (h), obeys

\[
\boxed{
U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h)le cI(F_d).
}

For every preceding dense nullity-two shield one may keep (c=2) exactly,
so the retained-credit constant is two and

\[
H(F_d)\le6I(F_d).
\]

The constants are independent of shield dimension, dense kernel
orientation, coherent core, depth, terminal rarity, pruning, reveal order,
and terminal-core complexity.  Full FEI remains **OPEN**.

## Packet and bounded objective

- Stream/packet: B05 / A023.
- Attempt: `B05-A023-BIASED-TOWER-RETAINED-11`.
- Stable gap: `B05_RARE_REFUNDS`.
- Frozen objective: determine whether the new fixed-bias tower admits a
  depth-independent complete-tree (U)-payment without weakening the
  nullity-two endpoint constant.

The answer is yes.  The earlier (72/35) loss came only from the global
bound (R<7/4); the actual tower samples (R) solely on the negative half
of its domain, where (R\le1).

## Mathematical delta

- Previous B05 scope: a single dense nullity-two shield, arbitrary
  restriction tree, and a common disjoint terminal core, with constant two.
- New scope: arbitrary nested depth of genuinely biased positive-level AND
  balancers and fair half-activations above that shield.
- Previous biased-tower endpoint threshold: (72/35).
- New threshold: (48/35); in particular (c=2) is preserved rather than
  enlarged.
- Newly uniform parameters: tower depth and terminal rarity (2^{-d}), in
  addition to all parameters already uniform in the dense shield theorem.

## Proof mechanism

The exact recurrences are

\[
U(F_k)=\tfrac12U(F_{k-1})+\tfrac12+R(-m_{k-1}/2),
\qquad
I(F_k)=\tfrac12I(F_{k-1})+1+\tfrac14m_{k-1},
\]

with (3/8\le m_{k-1}\le1/2).  A third-derivative argument shows that
(R) has one interior minimum and no interior maximum on ([-1,0]), hence
(R(t)\le R(0)=1).  Therefore

\[
U(F_k)-cI(F_k)
\le\tfrac12[U(F_{k-1})-cI(F_{k-1})]
+\tfrac32-\tfrac{35}{32}c,
\]

which closes for (c\ge48/35).  The complete signed tree charge telescopes
to root (U) minus nonnegative leaf (U), and the common disjoint terminal
packet cancels exactly once.  No nodewise positive-credit claim is made.

## Verification

`CHECK_BIASED_RETAINED.py` independently reconstructs Walsh spectra, (U),
influence, the tower, restrictions, pruned-tree ledgers, and terminal tensor
products.  It passed:

- 20,001 samples of the scalar bound on ([-1,0]);
- 294 Boolean bases and 866 direct towers;
- 1,732 exact recurrence checks;
- 3,408 endpoint-transfer checks;
- 552 independently pruned trees with 2,901 total leaves; and
- 184 direct terminal-core tensor-cancellation checks.

The maximum recurrence discrepancy was (4.441\times10^{-16}).  The
analytic proof, not the finite grid, proves the all-parameter theorem.

## Obstruction tests and exact remaining gap

- Rare leaves are included at arbitrary finite depth; the logarithmic packet
  is retained in root (U), not charged nodewise.
- Arbitrary base spectra, including point defects, were tested; the theorem
  assumes only the explicit base endpoint.
- The dense nullity-two base already includes shared shield/core variables;
  the new tower variables themselves remain fresh and disjoint.
- The theorem does not address biased outer selectors, physical-variable
  reuse, a balancer bias tending to (\pm1), or changing overlapping cores
  between levels.

The next unpaid step is a one-parameter biased-balancer family.  One must
track the analogue of (R(t)\le1) together with the selector-energy offset
and decide whether the endpoint threshold stays bounded as the balancer mean
approaches (\pm1).  A bias-dependent divergent constant would remain a
proper-class result and would not close full FEI.

## Status and routing

Claims are author-proved and require independent A087/A094 or B19 review.
Route to A024 for biased-child normalization and to B01/B18/B20 for the
endpoint/GU interface.  A023 is not complete, native Brain adoption is not
claimed, and full FEI remains open.
