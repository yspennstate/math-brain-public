# BT4 — account02/B20 r11 — unit-block pivot and cross collapse

Run: `20260922T091251Z-account02-B20-bt4-r11`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Target status: **OPEN_NOT_PROVED**  
Execution context: **WITHOUT_VERIFIED_BRAIN**

## Exact target and scope

The target is the k=4 Bermond–Thomassen conjecture in the owner-specified source model: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs/digons are allowed in the theorem statement and all graph orders are included.

The argument below works inside the inherited normalized oriented exact-seven minimal-counterexample branch supplied by the campaign chain: 3-vertex-strong, arc-dominated, with a globally minimum-total-order packing `(A,B,C)` of three pairwise vertex-disjoint directed cycles and acyclic remainder `R`. This is a conditional branch of the exact source problem, not a replacement of the digon-allowed theorem.

## Fresh control and scientific inputs

Fresh owner control was resolved from main before the scientific write; OWNER CONTROL remained revision `2026-09-22.2`, active programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, with new brain-installation/benchmark work stopped and B12–B18 retained on FEI.

Latest complete campaign lead actually consumed:
- account02/B04 `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, shared handoff blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`, canonical report commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`.

Named completed OTHER-account partner actually consumed:
- account04/B06 `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1`, shared handoff blob `47d7e7c2fd312fd647604bf61113c46fd980a237`, canonical report commit `3e7343cfd9de439c2e6ae8c39e71ddcbc956cde9`.
- Its role here is exact: once useful same-support bypasses, uncontrolled opposite-intersections and third-support mediation are excluded, the long A/B branch has rank-two connector families in both directions with opposite-direction remainder interiors disjoint. It does **not** say rank two automatically gives two disjoint cycles.

Fresh completed adversarial input actually used:
- account03/B05 `BT4-MONOTONE-QUADRANT-RANK-WALL-v1`, shared handoff blob `79dbbd71ee4b8c919951b5afd4a83c2c84830152`, canonical report commit `91a121c586b602b83a9d15d6c7937cdea3d665d8`.
- It proves that a monotone same-quadrant placement of two A→B and two B→A connectors can block every two-splice even when the four connector interiors are clean and all packed endpoints are distinct. Therefore the present run does **not** try to close BT4 by another rank increment; it exploits the extra collar geometry forced by a unit torus block.

Immediate same-slot mathematical inputs rechecked:
- B20 r17 `BT4-TORUS-FOURBLOCK-FAN-CAGE-v1`, report blob `f10128d630f2b6596f6d45c5ef1bb7b787d8ece2`.
- B20 r18 `BT4-R3-CAGE-COLLAR-ESCAPE-v1`, report blob `dcb490e726bb895696be8f9d91bf7ba52c60f9c3`. At this run's initial operational snapshot the r18 finish/receipt was not yet established, so r18 is treated as a readable mathematical partial, not as finalized fleet evidence. The collar calculation needed below is reproduced here.

The account02/B04 directory also contains the newer partial torus diagnostic `torus_order_output.txt` (blob `992389b6468e94b7034299e1fa1a169c4dc32d6e`), which records `canonical_two_splice=0` in all tested small torus-order families. It is diagnostic only, not a proof or finite substitute for the source problem.

## Compact conditional end-to-end campaign argument

Assume a BT4 counterexample and pass through the inherited normal-form reductions to the globally minimum three-packing `(A,B,C)` with acyclic remainder. The lead's clean-four-port theorem turns the heavy-triangle clean branch into a genuine CROSS or taxed same-support BYPASS. The named account04/B06 partner removes rank-one and uncontrolled opposite-intersection walls in the long two-support residual. The predecessor-torus reduction then yields a mixed signed torus cycle. B20 r17 reduces the minimum four-sign-block case to a genuine hub 4-cycle

`K0 = a0 -> b0 -> a1 -> b1 -> a0`

and an external vertex `z` with at least three outneighbors on `K0`. The r18 collar handles a remainder witness whose two same-support hub targets are nonconsecutive. The theorem below handles the remaining consecutive/unit-block case and shows that **every remainder-supported 3-of-4 witness in the exact-four-block cage already yields a genuine packed-to-packed transition, possibly after one same-size exchange, with an additional opposite-support collar of length at most two**.

This still does not close BT4: the fresh account03/B05 result shows that clean bidirectional connector multiplicity can remain globally parity-blocked. The next universal obligation is therefore a collar-sensitive cyclic-order/splice theorem, not another rank claim.

## Bookkeeping correction to r18

The qualitative r18 dichotomy is retained, but one label sentence is reversed. In r17 notation, plus blocks have lengths `p_i` and move in the `A` coordinate, while minus blocks have lengths `q_i` and move in the `B` coordinate. Hence:

- the two **A-hub** gaps are the two `p_i` lengths;
- the two **B-hub** gaps are the two `q_i` lengths.

Thus a consecutive A-hub pair means some `p_i=1`, and a consecutive B-hub pair means some `q_i=1`. The proof below uses support-order notation and is independent of this naming correction.

## New theorem — `BT4-R3-UNIT-PIVOT-CROSS-v1`

### Statement

Work in the inherited normalized branch and in the exact-four-sign-block torus cage. Let

`K0 = t0 -> u -> t1 -> u+ -> t0`

be the same hub 4-cycle, written so that `u,u+` are the two hubs on one packed support `S` and `t0,t1` are the two hubs on the other packed support `T`. Assume `u+` is the directed successor of `u` on `S`; equivalently the relevant torus block has length one. Let `z in R` be a 3-of-4 external witness with

`z->u` and `z->u+`.

Since `z` hits at least three vertices of `K0`, it also has an arc to at least one of `t0,t1`.

Then one of the following holds.

1. **Immediate packed-to-packed transition.** There is a directed path from a packed support different from `S` to `S`, with every internal vertex in `R`.

2. **Neutral pivot plus direct cross.** The only possible packed in-neighbor of `z` on `S` is `u^-`, and `u^-->z` exists. Then

`S' = u^- -> z -> u+ -> S[u+,u^-]`

is a genuine directed cycle with `|S'|=|S|`, disjoint from the other two packed cycles. Replacing `S` by `S'` is therefore a legal neutral three-packing exchange, frees `u` into the new remainder, and turns the third hub hit `z->t` (`t in {t0,t1}`) into a **direct packed-to-packed cross** from `S'` to `T`.

Moreover, in case 2 the opposite hub distance satisfies

`d_T(t0,t1) <= 2`.

Consequently:

- if `d_T(t0,t1)=1`, the three vertices `t0,t1,u+` form the genuine directed triangle
  `t0 -> t1 -> u+ -> t0`;
- if `d_T(t0,t1)=2`, writing `c` for the unique internal vertex of `T[t0,t1]`, the cycle
  `T' = t0 -> u -> t1 -> T[t1,t0]`
  is a second legal neutral exchange, replacing `c` by the freed hub `u`.

In particular, combining this theorem with the nonconsecutive-target collar gives the exact-four-block remainder-witness reduction

`R-supported 3-of-4 fan cage -> PACKED_CROSS`

(possibly after one neutral pivot), with the unit case carrying the extra `d_T<=2` collar.

### Proof

Let `s in S` satisfy `s->z`. For either target `h in {u,u+}`, the directed cycle

`s -> z -> h -> S[h,s]`

uses only the remainder vertex `z` off `S`, so it is disjoint from the other two packed cycles. Global minimum of the total order of the three-packing gives

`d_S(h,s)+2 >= |S|`.

The two distances corresponding to the distinct targets `u,u+` are distinct, so they must be the two largest possible values `|S|-2` and `|S|-1`. Therefore

`{u,u+} = {s^+,s^{++}}`.

Because `u+` is the successor of `u`, the order is forced: `s=u^-`, `s^+=u`, `s^{++}=u+`. Thus **the only possible S-inneighbor of z is `u^-`**.

#### Case A: `u^-` does not send to `z`

Then `S` has no arc into `z`. Fix the arc `z->u+`. Arc domination supplies a common predecessor `r1` with

`r1->z`, `r1->u+`.

If `r1` is on a packed support different from `S`, the desired packed-to-packed transition is already `r1->z->u+`. Otherwise `r1 in R`. Dominate `r1->z`; if the new common predecessor is still in `R`, continue backwards. The chain cannot repeat a remainder vertex, because a repetition would create a directed cycle entirely in `R`, contradicting acyclicity. Finiteness forces the chain to leave `R`. It cannot leave through `S`, since every chain vertex sends an arc into `z` and `S->z` is absent. Hence it first leaves through another packed support, producing a genuine packed-to-packed path with all internal vertices in `R`. This is conclusion 1.

#### Case B: `u^-->z`

Use the already present arc `z->u+`. The cycle

`S' = u^- -> z -> u+ -> S[u+,u^-]`

is directed and simple. It replaces the two-edge segment `u^- -> u -> u+` by the two-edge segment `u^- -> z -> u+`, so `|S'|=|S|`. Since `z in R`, `S'` is disjoint from the other two packed cycles. This proves the neutral pivot and frees `u` into the new remainder.

Because `z` has at least three outneighbors on `K0` and already hits the two S-hubs, it hits `t0` or `t1`. After the pivot, `z` is a packed vertex of `S'`, while `t0,t1` remain on `T`. Thus the third hit is now a **direct packed-to-packed cross**.

It remains to prove the opposite-support collar. The hub orientation gives the two-edge directed path

`t0 -> u -> t1`.

After the first pivot, `u` lies in the new remainder, so

`C = t0 -> u -> t1 -> T[t1,t0]`

is a genuine directed cycle disjoint from `S'` and the untouched third packed cycle. If `d=d_T(t0,t1)`, then

`|C| = |T| - d + 2`.

A value `d>2` would make `|C|<|T|`, and replacing `T` by `C` while keeping `S'` and the third packed cycle would strictly lower the total order of the three-packing, contrary to global minimality. Hence `d<=2`.

If `d=1`, the support arc `t0->t1`, together with the hub arcs `t1->u+` and `u+->t0`, gives the stated directed triangle. If `d=2`, the displayed cycle `C` has exactly the same order as `T`; writing `c` for the unique internal support vertex between `t0,t1`, it is precisely the second neutral pivot replacing `c` by `u`. This proves all claims.

## Why this is essential movement

The r18 remainder fan cage stopped at

`nonconsecutive double-hit -> CROSS`,
`consecutive double-hit -> UNIT_BLOCK`.

The new theorem removes `UNIT_BLOCK` as a free-standing obstruction. In the consecutive case either the domination chain already exits to another packed support or a forced same-size pivot moves the remainder witness onto the packing, after which its third hub hit is itself a direct cross. The same pivot exposes the old hub as a length-two path across the opposite support and global minimality compresses the opposite hub gap to at most two.

This is stronger than merely renaming the residual. It turns **every remainder location** of the four-block external 3-of-4 witness into the common packed-cross interface and adds a bounded local collar that is absent from a generic rank-two cross family.

## Interaction with the fresh OTHER-account rank wall

Account03/B05 `BT4-MONOTONE-QUADRANT-RANK-WALL-v1` is applied here as a genuine obstruction to an invalid next inference: even with two clean connectors in each direction and four distinct ports, monotone same-quadrant port order can force opposite pairing parity on the two supports, so no two-splice exists. Therefore the result above is **not** promoted to BT4 closure merely because a direct cross is now present.

The extra information available here is exactly what the generic rank wall lacks: after the neutral unit pivot, one opposite-support hub interval has length at most two, and when the length is one there is a directed triangle; when it is two there is a second exact neutral pivot. The next proof should exploit this collar before asking for more linkage.

## First essential unpaid universal implication

### `BT4-R-CAGE-CROSS-COLLAR-CLOSE-v1`

For every inherited oriented exact-seven, 3-vertex-strong, arc-dominated state with globally minimum three-packing and acyclic remainder, in the exact-four-block torus branch with a remainder-supported external 3-of-4 witness, use the reduction above to obtain a packed-to-packed cross. Then prove that the cross, together with the named partner's reciprocal rank-two connector family and the collar geometry produced here, forces one of:

1. two genuinely directed vertex-disjoint replacement cycles yielding a strict lexicographic packing improvement or a directed cycle in the exchanged remainder;
2. a compatible same-support bypass family with the required minimum-packing tax;
3. third-support mediation, SIX/H5, or a previously bounded short-support state; or
4. four vertex-disjoint genuinely directed cycles.

The collar subcases are explicit:

- `d_T(t0,t1)=1`: exploit the directed triangle `t0->t1->u+->t0` and the direct cross from the pivoted support;
- `d_T(t0,t1)=2`: execute/track the second neutral pivot and prove that the resulting two-pivot state either changes the connector matching parity, creates an accepted bypass/collision, or yields a strict descent.

A proof must respect the account03/B05 monotone-quadrant counterexample: clean rank two alone is not enough.

Separate global debts remain the support/third-support locations of the four-block 3-of-4 witness, the >=6-sign-block torus staircase, and the other campaign SIX/H5/F2/F3/support-carried branches. A single CROSS is not a fourth cycle.

## Last-three comparison and stagnation

The three latest readable substantive B20 mechanisms are materially different:
- r16: opposite-intersection bypass + 2x2 splice tax/cyclic matching;
- r17: four-sign-block torus topology + hub C4 + 3-of-4 witness;
- r18: nonconsecutive remainder double-hit collar + domination escape.

This run executes a new exact neutral-pivot mechanism in the r18 unit residue and obtains the new opposite-support `<=2` collar. The same universal implication has therefore not remained unchanged for three substantive runs; no forced stagnation pivot is triggered.

`FULL_TARGET_CHANGE = OPEN -> OPEN`.

`MECHANISM_CHANGE = UNIT_BLOCK OR CROSS -> CROSS in all remainder-witness cases, with a triangle/double-neutral-pivot collar in the unit case`.

## Integrity

No finite graph search, relaxed one-reversed-arc theorem, larger degree threshold, edge-disjoint substitute, routine subclass, installation work, benchmark work or brain-readiness claim was used. No authenticated brain retrieval/context use occurred. Existing artifacts and sealed benchmark material were not modified or exposed.
