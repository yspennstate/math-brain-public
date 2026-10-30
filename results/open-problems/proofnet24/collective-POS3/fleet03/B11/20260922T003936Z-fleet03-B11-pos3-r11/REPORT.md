# POS3 fleet03/B11 — order-polytope swap-defect reduction

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

This run follows the later owner-directed `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` allocation. The older benchmark/FEI duties in the native prompt are superseded for B11; no new benchmark work was performed.

## 1. Exact peer state consumed

The assigned fleet03/B11 task is to try a distinct order-polytope/correlation mechanism that improves the decisive pair-selection statement. I used the exact named-partner result from **fleet04/B19**, report commit `d9c8c3761d47861b28bcd63102eb625d596d51df`, blob `ce30dae79d698103f026d4d871033238489b1fb1`:

- restriction of a uniform linear extension to an autonomous subset is uniform on the induced subposet;
- therefore a cardinality-minimal POS3 counterexample has no proper autonomous nonchain;
- in particular an autonomous incomparable two-element module is balanced with probability exactly `1/2`.

I also use the already source-bound collective state:

- fleet02/B11: a minimal counterexample may be taken incomparability-connected, and the inherited strong-majority tournament is transitive;
- inherited I0122: the transitive strong-majority order decomposes into at least five maximal contiguous chain blocks;
- fleet01/B10: exact three-chain path/flux representation and the `>e(P)/3` heavy-slice normal form;
- fleet03/B19: connectedness alone does not force an endpoint-balanced pair or a small insertion slice.

The new argument below does not assume a uniform law after deleting a chain.

## 2. Order-polytope representation

Let `P` be a finite poset on `n` elements and let

`O(P) = {u in [0,1]^P : u_a <= u_b whenever a <_P b}`

be its order polytope. Up to the measure-zero coordinate-equality hyperplanes, `O(P)` is partitioned into the standard simplices indexed by linear extensions of `P`; every such simplex has Euclidean volume `1/n!`. Hence if `U` is uniform on `O(P)`, then the relative order of its coordinates is a uniform random linear extension.

For incomparable `x,y`, write

`A_xy = {u in O(P): u_x < u_y}` and `B_xy = {u in O(P): u_y < u_x}`.

Then

`p_xy := Pr_L(x precedes y) = vol(A_xy)/vol(O(P))`,

and `vol(A_xy)+vol(B_xy)=vol(O(P))`.

Let `T_xy` be the coordinate transposition swapping `u_x` and `u_y` and fixing every other coordinate. It preserves Lebesgue measure and is an involution.

Define the positive and negative swap-defect regions

`D^+_{xy} = {u in A_xy : T_xy u notin O(P)}`,

`D^-_{xy} = {u in B_xy : T_xy u notin O(P)}`.

### Theorem 2.1 — exact swap-defect identity

For every incomparable `x,y`,

`2 p_xy - 1 = [vol(D^+_{xy}) - vol(D^-_{xy})] / vol(O(P))`.

### Proof

Put `A^0=A_xy\D^+_{xy}` and `B^0=B_xy\D^-_{xy}`. By definition, `T_xy` maps `A^0` into `O(P)`, reverses the strict coordinate inequality, and is its own inverse. Therefore it is a measure-preserving bijection `A^0 <-> B^0`, so `vol(A^0)=vol(B^0)`.

Thus

`vol(A_xy)-vol(B_xy)=vol(D^+_{xy})-vol(D^-_{xy})`.

Divide by `vol(O(P))` and use `p_xy-(1-p_xy)=2p_xy-1`. ∎

This is the correlation quantity we need: a pair can be strongly biased only if the order polytope is substantially asymmetric under the corresponding coordinate transposition.

## 3. Exact characterization of the positive defect

Define

`P_y(x) = {z : z <_P y and z || x}`,

`S_x(y) = {z : x <_P z and z || y}`.

### Lemma 3.1 — blocker characterization

For `u in A_xy`, the swapped point `T_xy u` fails to lie in `O(P)` iff at least one of the following holds:

1. there is `z in P_y(x)` with `u_x < u_z < u_y`;
2. there is `z in S_x(y)` with `u_x < u_z < u_y`.

### Proof

Moving `y` left to the old `x` coordinate can violate only a predecessor constraint `z<y`; every predecessor already lying before the old `x` coordinate remains safe. Thus failure from the moved `y` occurs exactly when some predecessor `z<y` lies strictly between the two coordinates. Such a `z` cannot satisfy `z<x`, because then `u_z<=u_x`; and it cannot satisfy `x<z`, because `x<z<y` would imply `x<y` in the poset, contrary to incomparability. Hence it lies in `P_y(x)`.

Similarly, moving `x` right to the old `y` coordinate can violate only a successor constraint `x<z`; a violating successor strictly between the coordinates cannot be comparable with `y`, so it lies in `S_x(y)`. These are the only constraints changed by the transposition. ∎

The discrete version is identical: in a linear extension with `x` before `y`, swapping their positions fails exactly when some blocker of one of these two types lies between them.

## 4. Width-three compression to at most four canonical blockers

Let

`M^-_{xy} = Max(P_y(x))`, the set of poset-maximal predecessor blockers,

`M^+_{xy} = Min(S_x(y))`, the set of poset-minimal successor blockers.

### Lemma 4.1 — canonical compression

For a point of `A_xy`, existence of any predecessor blocker between `x,y` is equivalent (off a null boundary) to existence of some `m in M^-_{xy}` with `u_x<u_m<u_y`. Likewise any successor blocker can be replaced by some `s in M^+_{xy}`.

Consequently

`D^+_{xy}` is the union of the events

`{u_x<u_m}` for `m in M^-_{xy}` and `{u_s<u_y}` for `s in M^+_{xy}`.

Under the uniform-linear-extension interpretation, these have probabilities `Pr(x precedes m)` and `Pr(s precedes y)` respectively.

### Proof

If `z in P_y(x)` is a blocker, choose a maximal `m in P_y(x)` above `z`. Then `z<=m<y`, hence `u_z<=u_m<u_y`; since `u_x<u_z`, `m` is again between `x,y`. Conversely every maximal blocker is a blocker. The successor statement is dual. ∎

### Lemma 4.2 — width-three cardinality bound

If `width(P)<=3`, then

`|M^-_{xy}|<=2` and `|M^+_{xy}|<=2`.

### Proof

`M^-_{xy}` is an antichain and every member is incomparable with `x`; therefore `{x} union M^-_{xy}` is an antichain. Width at most three gives the first bound. Dually `{y} union M^+_{xy}` is an antichain. ∎

Thus every positive swap defect in width three is controlled by at most four explicit pair-order events.

## 5. New necessary structure in a POS3 counterexample

Assume now that `P` is a POS3 counterexample. The inherited exact state gives a transitive strong-majority total order `prec_*` extending `P`. Let `x prec_* y` be an **adjacent incomparable pair** in this order (equivalently a boundary pair between two consecutive maximal chain blocks).

Because `P` is a counterexample,

`p_xy > 2/3`.

By Theorem 2.1,

`vol(D^+_{xy}) - vol(D^-_{xy}) > vol(O(P))/3`,

so in particular

`vol(D^+_{xy}) > vol(O(P))/3`.  (5.1)

Now take `m in M^-_{xy}`. Since `m<y` in the poset, `m prec_* y`. Since `m||x` and there is no strong-majority element strictly between adjacent `x prec_* y`, we must have `m prec_* x`. Hence

`Pr(x precedes m) < 1/3`.

Similarly, for every `s in M^+_{xy}`, poset comparability gives `x prec_* s`, adjacency forces `y prec_* s`, and therefore

`Pr(s precedes y) < 1/3`.

Combining these strict minority bounds with the canonical-union formula and (5.1) gives the main new corollary.

### Corollary 5.1 — double-blocker certificate

In any width-at-most-three POS3 counterexample, every adjacent incomparable pair `x prec_* y` has at least **two** canonical positive blockers:

`|M^-_{xy}| + |M^+_{xy}| >= 2`.

Moreover every canonical blocker event is itself a strict minority event `<1/3`, while their union has probability `>1/3`.

### Proof

If there were zero canonical blockers, `D^+_{xy}` would be empty, contradicting (5.1). If there were exactly one, `D^+_{xy}` would equal a single canonical blocker event of probability `<1/3`, again contradicting (5.1). ∎

This is strictly stronger than merely knowing that the boundary pair is biased. It forces each majority-block boundary to be supported by a multi-witness local obstruction to coordinate transposition.

### Endpoint consequence

At the first chain-block boundary, there can be no predecessor blocker: any element before `x` in the strong-majority order lies in the same first chain block, hence is comparable with `x`. Therefore the first boundary has **two distinct minimal successor blockers**. They are incomparable with each other (both are minimal in `S_x(y)`) and each is incomparable with `y`, so together with `y` they form a three-element antichain. The two blockers must lie in distinct later chain blocks.

Dually, the last chain-block boundary has two distinct maximal predecessor blockers in distinct earlier blocks, forming a three-element antichain with its left endpoint.

This endpoint `3`-antichain requirement is a concrete new structural condition on the already-known `>=5` majority-block core.

## 6. Relation to the named-partner autonomous-module theorem

If the positive and negative blocker systems are both empty for an incomparable pair `{x,y}`, then every outside element is below both, above both, or incomparable with both. Thus `{x,y}` is an autonomous two-element antichain. The fleet04/B19 theorem then gives `p_xy=1/2` exactly.

The swap-defect identity recovers the same conclusion geometrically: both defect regions vanish, so `2p_xy-1=0`.

The new information here is what happens far from the autonomous case: an extreme adjacent majority pair in width three requires at least two canonical blocker witnesses, not merely one failure of autonomy.

## 7. A tempting stronger local route is false

One might hope to rule out the mixed case with one predecessor blocker and one successor blocker by proving that one of those blocker pairs must itself be balanced. That stronger statement is false even in width three.

On elements `0,...,5`, take the transitive closure of

`0<2, 0<4, 1<2, 1<3, 1<4, 1<5, 3<4, 5<2`.

With `x=0`, predecessor blocker `m=1`, successor blocker `s=2`, and `y=3`, exact enumeration gives `22` linear extensions, width `3`, and

`Pr(x<y)=15/22 > 2/3`,

`Pr(x<m)=3/11 < 1/3`,

`Pr(s<y)=3/22 < 1/3`.

So the two canonical minority events can together support an extreme positive swap defect. This six-point poset is **not** a counterexample to POS3: for example `Pr(2<4)=1/2` (also `Pr(3<5)=1/2`). The lesson is that the next proof must use the *global simultaneous system* of double-blocker certificates across all majority boundaries, not a one-boundary N-shaped argument.

## 8. Regression verification

A companion standard-library script `verify_pos3_swap_defect.py` checks:

1. the exact identity `|A|-|B|=|A_bad|-|B_bad|` in the discrete triangulation model;
2. equality of the full bad set with the canonical maximal-predecessor/minimal-successor blocker union;
3. the width-three `<=2` cardinality bound on each canonical side;
4. the bare four-point N-poset;
5. the six-point stronger-route adversary above;
6. every incomparable pair in the inherited 9-element fleet03/B19 certificate with `420` extensions.

The recorded terminal output is `POS3_SWAP_DEFECT_CHECK_PASS`. The proof is the analytic transposition argument above; enumeration is regression evidence only.

## 9. Exact next obligation

The parent problem remains open. The new residual can be stated without deleting a chain or changing the probability law:

> In a width-three minimal counterexample, the transitive strong-majority order has at least five chain blocks, and **every** adjacent block boundary carries a double-blocker certificate whose individual reversal events are each `<1/3` but whose canonical union is `>1/3`.

The next high-value step is to combine these certificates across consecutive boundaries. The endpoint certificates force genuine three-antichain witnesses in distinct blocks. The fleet01/B10 heavy-slice constraints and fleet03/B10 pinned majority-rank atoms give independent mass constraints on the same strong-majority geometry. A useful successor lemma would show that the required double-blocker systems cannot be aligned across all boundaries of a connected width-three, module-prime core, or else produce an explicit width-three poset realizing all constraints and thereby identify the missing invariant.

## 10. Claim status

- Order-polytope swap-defect identity: **PROVED**.
- Exact blocker characterization: **PROVED**.
- Width-three compression to at most four canonical positive blockers: **PROVED**.
- Double-blocker certificate for every adjacent strong-majority incomparable pair in a counterexample: **PROVED**.
- Endpoint three-antichain consequence: **PROVED**.
- Stronger claim that a mixed one-predecessor/one-successor blocker pattern locally forces balance: **REFUTED** by an exact 6-element width-three example.
- Width-three `1/3–2/3` parent target: **NOT PROVED**.

No novelty or priority claim is made. No benchmark gold, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, paid model/API/Codex execution, remote workflow, or public release was used.
