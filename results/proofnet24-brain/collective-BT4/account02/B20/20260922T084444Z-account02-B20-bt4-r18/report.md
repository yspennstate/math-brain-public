# BT4 — B20 r18 — remainder fan-cage collar escape

Run: `20260922T084444Z-account02-B20-bt4-r18`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Target status: **OPEN_NOT_PROVED**  
Execution context: **WITHOUT_VERIFIED_BRAIN**

## Exact target and scope

The target is the k=4 Bermond–Thomassen statement in the owner's source model: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles; opposite arcs/digons are allowed in the theorem statement and all graph orders are included.

The derivation below is inside the inherited normalized oriented exact-seven minimal-counterexample branch supplied by the campaign lead chain. Thus the original digon-allowed target is not silently replaced by the oriented branch: earlier campaign reductions are part of the conditional end-to-end argument.

## Fresh controls and scientific dependencies actually consumed


Latest complete campaign lead actually consumed:
- account02/B04, `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, canonical report commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`, shared handoff Git blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`.

The newer account02/B04 directory `20260922T081646Z-b04-bt4-r11` was also inspected. At the scientific snapshot used here it contained a start plus `torus_order_check.py` / `torus_order_output.txt`, but no complete report. Its diagnostic output continued to show `canonical_two_splice=0` in the tested torus order families, so it was treated as a partial diagnostic, not as a replacement for the latest complete lead candidate.

Named completed OTHER-account partner actually used:
- account04/B06, `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1`, canonical report commit `3e7343cfd9de439c2e6ae8c39e71ddcbc956cde9`, shared handoff Git blob `47d7e7c2fd312fd647604bf61113c46fd980a237`.
  Its rank/intersection collapse is the reason the residual long-support branch may be passed to the clean rank-two / predecessor-torus geometry rather than waiting on an uncontrolled intersecting-connector case.

Immediate inherited B20 input:
- account02/B20 r17, `BT4-TORUS-FOURBLOCK-FAN-CAGE-v1`, report blob `f10128d630f2b6596f6d45c5ef1bb7b787d8ece2`.
  In the exact four-sign-block torus branch it constructs the alternating hub cycle
  `K0=a_{alpha0}->b_{beta0}->a_{alpha1}->b_{beta1}->a_{alpha0}`
  and, by applying the k=3 theorem after deleting `K0`, forces an external vertex `z` with at least three outneighbors on `K0`.

## Compact conditional end-to-end argument

Assume a BT4 counterexample. The lead chain passes to an inherited normalized branch with an oriented exact-seven, 3-vertex-strong, arc-dominated digraph and a globally minimum-total-order packing `(A,B,C)` of three pairwise vertex-disjoint directed cycles, with acyclic remainder `R`.

The named account04/B06 result eliminates the rank-one and uncontrolled opposite-intersection defects in the long pure two-support linkage branch. The predecessor-torus reduction then gives a mixed signed predecessor cycle. B20 r17 shows that the minimum-block case has exactly two plus blocks and two minus blocks, primitive winding, the genuine hub 4-cycle `K0`, and an external 3-of-4 witness `z`.

If the external witness lies in the remainder, the theorem below reduces every non-unit-block double-hit to a genuine packed-to-packed transition through the remainder. Thus the exact-four-block remainder-witness branch reduces to either a **unit torus block** or the already explicit **cross/splice interface**. To finish the entire BT4 campaign one must still close that unit-block/cross interface, the support-carried and third-support `z` locations, the >=6-sign-block torus staircase, and the other named SIX/H5/F2/F3 branches. No one of those closures is asserted here.

## New theorem: `BT4-R3-CAGE-COLLAR-ESCAPE-v1`

### Statement

Work in the inherited normalized branch above. Let `S` be one of the packed directed cycles and `z in R`. Suppose `z` has arcs to two distinct vertices `x,y in S`.

1. **Two-target inport collar.** If some `s in S` satisfies `s->z`, then
   `{x,y}={s^+,s^{++}}`,
   where successors are taken in the directed orientation of `S`. In particular, if `x,y` are not consecutive on `S`, then there is no arc from `S` into `z`.

2. **Domination escape.** If `x,y` are nonconsecutive and the inherited arc-domination property holds, then for either chosen target `h in {x,y}` there exists a directed path
   `t -> r_k -> ... -> r_1 -> z -> h`
   whose initial vertex `t` lies on one of the other two packed cycles `T != S`, and every internal vertex `r_j,z` lies in `R`. Hence there is a genuine packed-to-packed directed transition from `T` into `S` through the acyclic remainder.

3. **Exact-four-block fan-cage consequence.** In the r17 exact-four-block torus cage, suppose `z in R` has at least three outneighbors on `K0`. By pigeonhole, one support `S in {A,B}` has both of its two hub vertices in `N^+(z)`. If `S=B`, those two hubs split the directed cycle `B` into arcs of lengths `p_0,p_1`, the two plus-block lengths. If `S=A`, the analogous two gaps are the two minus-block lengths `q_0,q_1`. Therefore either one relevant block length is `1`, or the two hubs are nonconsecutive and conclusion (2) supplies a genuine packed-to-packed transition ending at one of the hub vertices.

Equivalently, the generic remainder 3-of-4 fan cage is not a new free-standing obstruction:

`R-witness + exact four blocks -> UNIT_BLOCK or CROSS_TRANSITION`.

### Proof of the two-target inport collar

Let `n=|S|` and let `d_S(t,s)` denote the number of directed edges on the forward segment of `S` from `t` to `s`.

Assume `s->z`. For each target `t in {x,y}`, the walk

`C_t = s -> z -> t -> S[t,s]`

is a genuinely directed cycle. It uses only the remainder vertex `z` outside `S`, hence it is vertex-disjoint from the other two packed cycles. Replacing `S` by `C_t` therefore gives another legal three-cycle packing. Global minimum of the total packed order gives

`|C_t| = d_S(t,s)+2 >= |S| = n`,

so

`d_S(t,s) >= n-2`.

The two values `d_S(x,s)` and `d_S(y,s)` are distinct elements of `{0,...,n-1}` because `x != y`. Hence they are exactly `n-2` and `n-1`. Those are precisely the forward distances to `s` from `s^{++}` and `s^+`, respectively. Thus `{x,y}={s^+,s^{++}}`.

Consequently, if `x,y` are nonconsecutive, no such `s` can exist, so `S` has no arc into `z`.

### Proof of domination escape

Assume now that `x,y` are nonconsecutive, hence `S -> z` is absent. Fix `h in {x,y}` and the arc `z->h`.

By the inherited arc-domination property, the arc `z->h` has a common predecessor `r_1` with

`r_1->z` and `r_1->h`.

Because `S->z` is absent, `r_1` is not on `S`. If `r_1` lies on one of the other packed cycles, we already have the directed transition `r_1->z->h` and are done.

Otherwise `r_1 in R`. Apply arc domination to `r_1->z`; obtain `r_2` with

`r_2->r_1` and `r_2->z`.

Again `r_2` cannot lie on `S`. If it lies on another packed support, stop. Otherwise continue inside `R`, always dominating the current arc `r_j->z` to obtain `r_{j+1}->r_j` and `r_{j+1}->z`.

This predecessor chain cannot repeat an `R` vertex: a repetition would create a genuinely directed cycle wholly inside `R`, contrary to acyclicity. Since the digraph is finite, the chain must eventually leave `R`. It cannot leave through `S`, because every chain vertex has an arc to `z` and `S->z` is absent. Thus it first leaves through one of the other packed cycles `T != S`, at a vertex `t`, producing

`t -> r_k -> ... -> r_1 -> z -> h`.

All internal vertices lie in `R`, exactly as claimed.

### Proof of the exact-four-block consequence

The hub cycle has two vertices on `A` and two on `B`; a 3-of-4 outneighborhood therefore contains both hubs of at least one support `S`.

By the r17 torus bookkeeping, the two `B` hubs split `B` into the two plus-block lengths `p_0,p_1`, and the two `A` hubs split `A` into the two minus-block lengths `q_0,q_1`. The two hubs of `S` are consecutive exactly when one of the corresponding two gap lengths equals `1`.

If a relevant gap is `1`, record `UNIT_BLOCK`. Otherwise both gaps are at least `2`, so the two targeted hubs are nonconsecutive. Parts (1) and (2) then forbid every `S->z` inport and force a packed-to-packed transition through `R` into the targeted hub support. This is the claimed `UNIT_BLOCK or CROSS_TRANSITION` dichotomy.

## Why this is not merely an auxiliary renaming

Before r18, the r17 exact-four-block reduction stopped at a remainder-supported `3-of-4` fan witness on `K0`. The new theorem consumes global minimum of the three-packing and arc domination to convert every non-unit double-hit into an actual directed transition between packed supports, with its internal vertices certified to lie in the acyclic remainder. The unpaid state is therefore strictly smaller: only unit-gap cages and the already identified cross/splice closure remain for the remainder-witness location.

This is mechanism movement, not target closure. It does not prove that a single cross transition alone yields a fourth disjoint cycle.

## First essential missing implication after this run

`BT4-TORUS-UNIT-BLOCK-CROSS-SPLICE-v1`:

For every inherited normalized exact-seven oriented minimal counterexample and every exact-four-block torus hub cage `K0`, if the external 3-of-4 witness lies in `R`, prove that either

- a unit relevant torus block (`p_i=1` or `q_i=1`) yields a legal strict/neutral exchange ending in a directed cycle in the exchanged remainder, SIX/H5, or four disjoint directed cycles; or
- the packed-to-packed transition forced by `BT4-R3-CAGE-COLLAR-ESCAPE-v1`, together with the existing reciprocal/rank-two connector data, can be paired into two vertex-disjoint replacement directed cycles or another accepted strict descent.

All cycles in this implication are genuinely directed and vertex-disjoint where required; no edge-disjoint, one-reversed-arc, higher-degree, subclass, or finite-search substitute is allowed.

A natural next attack is to exploit the unit block as a fixed adjacent hub pair: any return into the predecessor of that pair creates a length-two support bypass, while failure of all such returns constrains the reciprocal connector endpoints to one cyclic side. For the CROSS_TRANSITION branch, the next useful invariant is first intersection of the forced domination ladder with the partner's opposite rank-two connector family; intersection should create a same-support bypass, while disjointness should create a legal two-splice candidate.

## Last-three substantive-run comparison / stagnation

The three immediately preceding B20 mechanisms were materially different:
- r15: Hall common-source collapse;
- r16: opposite-intersection bypass plus 2x2 splice tax;
- r17: predecessor-torus four-block hub cage.

This r18 run executes a fourth mechanism—packing-minimality collar plus domination escape. Therefore the same universal implication has not remained unchanged for three substantive runs, and no forced stagnation pivot is triggered.

FULL_TARGET_CHANGE: `OPEN -> OPEN`.
MECHANISM_CHANGE: `remainder 3-of-4 fan witness` -> `unit torus block OR genuine packed-to-packed remainder transition`.

## Keeper reconciliation summary

Fresh exposed scheduler inventory showed all managed account02 markers `B01` through `B20` present, enabled, hourly, unique, role/title/prompt aligned with the collective allocation (B12–B18 retained on FEI), and quiet. No re-enable, recreation, schedule change, title/prompt mutation, or B19 fallback was warranted in this invocation.

For completed hour `07Z`, canonical login files are present for 17/20 slots; the three missing canonical logins are B05, B11 and B20. Missing login alone is not treated as an outage. Registration health and recent-execution evidence remain separate from login evidence. For the current partial `08Z` snapshot inspected before finalization, canonical login files are established for B01, B02, B04, B06, B07, B08, B09, B10, B11, B12, B14, B15, B16, B18, B19 and B20; B03, B05, B13 and B17 were not present at that snapshot. Partial-hour absence is not failure evidence. Start and finalized-receipt evidence are tracked separately in the machine-readable recovery summary; lack of compact proof is recorded as `NOT_ESTABLISHED`, never promoted to `ABSENT` or `STOPPED`.

No scheduler mutation was performed.

## Result classification

**ESSENTIAL_STEP_APPLIED**

No full BT4 proof is claimed. No unrestricted Bermond–Thomassen closure is claimed. No all-account rollout is claimed.
