# BT4 account02/B20 — neutral-equality confinement for the dynamic exchange branch

Run: `20260922T010226Z-account02-B20-r11`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Outcome: `ESSENTIAL_STEP_APPLIED`
Target-level change: `NONE` — no full proof of k=4 is claimed.
Mechanism change: `YES` — the current dynamic neutral-exchange branch is confined by a new secondary-potential inequality, an exact unique-inport condition, and a five-fan splice obstruction.
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Exact target

Prove: every finite loopless digraph `D`, with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven, contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs and directed digons are permitted by the target. The current minimal-counterexample reductions eliminate digons only inside a hypothetical extremal counterexample; nothing below changes the source model.

## Exact inputs consumed

I use the latest complete account02 lead package

- `account02/B04/20260922T001806Z-b04-bt4-a1ceeb3c/report.md`, with its correction `correction.md`;

and the named completed other-account partner result

- `account04/B06/20260922T001024Z-b06-bt4-r43/report.md`, blob `08cf8f4283de825d533677d6edf5707523744a22`.

The latter supplies the fan-avoiding missing-arc saturation path and forced-exit mechanism that remains the designated way to attack the surviving splice branch. I also consume the later compatible account03/B05 correction

- `account03/B05/20260922T004115Z-account03-B05-BT4-r11/linkage_addendum.md`, blob `f1545c2e4a546d17150bb20bbc59650a29eb2672`,
- `linkage_correction.md`, blob `f19feaaea52a2a892e510bd8fe03dbb18290fcb5`,

which proves the source-valid marked-segment exchange and corrected two-linkage trichotomy.

No relaxed one-reversed-arc cycle, edge-disjoint surrogate, higher-degree theorem, finite search, or routine subclass is substituted for BT4.

## Conditional end-to-end chain before this run

Assume a counterexample exists and choose the standard extremal one: first minimum order, then maximum arc set. The current shared candidate gives an oriented, 3-vertex-strong normal form of exact outdegree seven and a three-cycle packing `(C1,C2,C3)` minimizing total covered vertices. Its remainder `R` is acyclic and every packed cycle is chordless.

For a sink `x` of `R`, a heavy packed cycle receives at least three arcs from `x`; the one-vertex exchange excludes a direct return from that heavy cycle to `x`. The corrected path-fan lemma says that an `R`-internal path of length `L` from a packed cycle `C` to `x`, where `m=|N+(x)∩C|`, satisfies `L>=m-1`. Pair deletion gives, for every pair of packed cycles, either a six-fan witness or three five-fan witnesses; a cycle-supported six-fan has no `R` exit and a cycle-supported five-fan has one `R` exit.

The named partner account04/B06 adds the following exact saturation mechanism. For suitable nonadjacent vertices `x,b`, adding the missing arc gives a four-cycle certificate; deleting the new arc leaves a directed `b`-to-`x` path `P` disjoint from three directed cycles, and `P-{x}` avoids all outneighbors of `x`. For a sink-heavy fan this bounds the final old-packing gateway, and if the predecessor of that gateway lies in `N+(x)` the replacement packing is forced to leave the old cycle immediately there.

Account03/B05 supplies the corrected cycle-supported exchange. Let `A,B,C` be the packed cycles, `S` a proper forward segment of `B` of size `s` containing a marked vertex `w`, and let `Q` be an `R`-internal bypass of `S` of length `ell`. If `b in A` satisfies `b->w` and

`m = |N+(w)∩A| >= 3`,

then

`ell >= m+s-1`.

At equality the fan on `A` is consecutive from the incoming port and the exchange is neutral: it produces another three-cycle packing with exactly the same total number of covered vertices. The first unpaid universal step is dynamic: rule out an endless sequence/orbit of such neutral exchanges, or turn it into two compatible exits/four disjoint directed cycles.

## New lemma 1 — quadratic confinement of every neutral marked-segment exchange

Among all three-cycle packings of minimum total covered size, choose one minimizing

`Phi = |A|^2 + |B|^2 + |C|^2`.

Suppose the corrected marked-segment exchange above is admissible and is neutral, i.e.

`ell = m+s-1`.

Write

`alpha=|A|`, `beta=|B|`, and `d=m-2`.

Then necessarily

`alpha - beta <= m-2`.                                      (1)

### Proof

At equality, the fan distances from the incoming port are the `m` distinct positive distances `1,...,m`. Taking the furthest fan target gives the neutral replacement used in the account03/B05 proof. Its two changed cycle lengths are exactly

`|A'| = alpha + 2 - m = alpha-d`,

`|B'| = beta - s + (ell-1) = beta+m-2 = beta+d`.

The third cycle is unchanged, and equality means total covered size is unchanged. Hence `(A',B',C)` is another minimum-total packing. By the secondary choice of `Phi`,

`0 <= Phi' - Phi`
`   = (alpha-d)^2 + (beta+d)^2 - alpha^2 - beta^2`
`   = 2d(beta-alpha+d)`.

Since `m>=3`, `d=m-2>0`. Therefore `beta-alpha+d>=0`, which is (1). QED.

### Consequence for the cycle-supported pair-deletion branch

Choose the complementary cycle `B` to be a shortest member of the minimum-total packing. If a five/six-fan witness `w in B` is heavy on a target cycle `A` with fan size `m`, then any neutral marked-segment exchange around `w` requires

`0 <= |A|-|B| <= m-2`.

Therefore, whenever `|A|-|B| >= m-1`, equality is impossible and the integer tax strengthens to

`ell >= m+s`.                                                (2)

For the relevant cycle-supported pair witnesses, `m<=6`, so neutral equality can survive only when the heavy target is within at most four vertices of the shortest source cycle; for a three-fan it must be within one vertex. This is the first genuine monovariant restriction on the dynamic equality orbit: the large cycle-length-gap regime no longer belongs to the unpaid neutral branch.

The exact change in the quadratic potential is

`Delta Phi = 2(m-2)((m-2)-(|A|-|B|))`.

Thus the borderline `|A|-|B|=m-2` is an exact length swap; smaller gaps are overshoots that increase `Phi`, while larger gaps would decrease `Phi` and are excluded by the extremal choice.

## New lemma 2 — neutral equality has exactly one inport from its heavy target

Under the same neutral-equality hypotheses, the marked vertex `w` has exactly one inneighbor on `A`.

Equivalently,

`|N-(w)∩A| = 1`.                                             (3)

### Proof

Let `F=N+(w)∩A`, `|F|=m`, and let `b in A` be any inport `b->w`. Equality in the marked-segment tax forces the `m` positive cyclic distances from `b` to the vertices of `F` to be exactly `1,...,m`. Because the extremal counterexample is oriented, `F` cannot be all of `A`: if `m=|A|`, then in particular `w->b`, forming a forbidden digon with `b->w`. Hence `m<|A|` and

`F={b^+,b^{++},...,b^{+(m)}}`,

a proper cyclic interval of length `m`.

If a second distinct `b' in A` also satisfied `b'->w`, the same equality argument applied with `b'` would force the identical set `F` to be the proper length-`m` cyclic interval immediately following `b'`. A proper cyclic interval on a directed cycle has a unique predecessor, so `b'=b`, contradiction. Thus the inport is unique. QED.

Hence if a heavy witness has two or more incoming arcs from its target cycle, the neutral branch is impossible and (2) again holds.

## New lemma 3 — every surviving neutral equality exposes a third-side inlink

Still in the exact 3-vertex-strong normal form, let `w in B` survive neutral equality with target `A`. Then some vertex outside `A union B` sends an arc to `w`:

`N-(w) ∩ (R union C) != emptyset`.                            (4)

### Proof

Three-vertex-strongness implies `d-(w)>=3`; otherwise deleting all at most two inneighbors of `w` destroys strong connectivity. Because `B` is chordless and the digraph is oriented, the only inneighbor of `w` on `B` is its predecessor `w^-`. Lemma 2 gives exactly one inneighbor on `A`. These account for only two inneighbors, so a third lies in `R union C`. QED.

Thus neutral equality does not merely say “no progress”: it forces an additional genuine cross-link from the remainder or the third packed cycle into the marked witness.

## New lemma 4 — five-fan remainder splice obstruction

Assume in addition that `w in B` is a cycle-supported **five-fan** witness for the pair `A union C`. In the exact-seven normal form it has exactly one outneighbor `r` in `R` besides its successor on `B` and its five pair-fan arcs.

Let `Q` be the neutral `R`-internal bypass of the proper `B`-segment `S` containing `w`, and let `B_Q` be the resulting bypass cycle. If Lemma 3 supplies `y in R` with `y->w`, then there is **no** directed `r`-to-`y` path in

`R - int(Q)`.                                                (5)

### Proof

If such a path `T` existed, then

`W = w -> r -> T -> y -> w`

would be a directed cycle. It uses only `w` and vertices of `R-int(Q)`. The bypass cycle `B_Q` uses vertices of `B-S` together with `int(Q)` and excludes `w`. Therefore `W` and `B_Q` are vertex-disjoint. Both are also disjoint from the untouched packed cycles `A` and `C`. Hence

`A, C, B_Q, W`

would be four pairwise vertex-disjoint genuinely directed cycles in `D`, contradicting the assumed counterexample. QED.

This turns the surviving five-fan equality into an exact DAG reachability cut: every forced remainder in-neighbor of `w` must lie outside the forward reachability of the unique `R` exit after deleting the bypass interior. That is a source-valid disjointness condition, not a degree average.

## What this does to the first unpaid universal step

The shared candidate previously allowed a neutral marked-segment exchange with little control over an exchange orbit. The new lemmas confine every such equality state simultaneously as follows:

1. the target/source cycle-length gap is at most `m-2` in the quadratic-minimum packing;
2. the heavy target contributes exactly one inport to the marked witness;
3. 3-vertex-strongness forces an additional inlink from the remainder or third packed cycle;
4. in the five-fan case, if that inlink comes from the remainder, the unique remainder exit cannot reach it outside the bypass interior, or four directed vertex-disjoint cycles already exist.

For a shortest complementary source cycle, either a large length gap or a second target inport immediately upgrades the marked-segment tax from `ell>=m+s-1` to the strict `ell>=m+s`. The only unresolved neutral orbit is therefore the near-balanced, unique-inport cage with an explicit third-side inlink and, for five-fans, an explicit forbidden reachability relation.

This directly uses the account04/B06 saturation/forced-exit result in the endgame: once the equality cage is reached, missing-arc saturation remains the mechanism that produces fan-avoiding return paths and replacement-cycle exits. The remaining proof obligation is now narrower: in the near-balanced unique-inport cage, combine the partner's saturation exits with the forced third-side inlink (and the five-fan reachability cut when available) to produce either a strict segment tax, a strictly better extremal packing, or two compatible exits yielding four cycles.

## Status and next method

`ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

The theorem itself has not moved from open to proved. What moved is the mechanism-level first unpaid step: neutral equality is no longer unconstrained. A universal secondary potential rules out every length-gap-decreasing equality, equality forces a unique inport and a third-side inlink, and the five-fan case gains a concrete disjoint-cycle reachability obstruction.

The next method should attack only the surviving near-balanced cage, not repeat static fan counting. In particular, combine account04/B06 fan-avoiding saturation paths with (4)-(5) and the corrected account03/B05 two-linkage trichotomy. A promising exact target is to show that the two internally disjoint `w^-`-to-`w^+` linkages cannot both respect the unique-inport cage and the five-fan reachability cut without either crossing a partner-forced exit or producing a second cycle in the pair-deletion residual digraph. The six-fan case must be handled separately because it has no remainder exit.

No claim of BT4 closure, unrestricted Bermond-Thomassen closure, or literature novelty is made.
