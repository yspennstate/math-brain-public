# BT4 fleet02/B05 — simultaneous double neutral pivot collapses the long two-sink branch

Run: `20260922T042100Z-b05-bt4-e5df42d4`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-DOUBLE-PIVOT-CONFLUENCE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent target: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and control/source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem and a directed digon counts as a cycle. The oriented exact-outdegree-seven model below is only the inherited minimum-counterexample normal form after the valid digon reduction.

Fresh owner controls were read from `yspennstate/math-research-brain` at main commit `852dfd0f4852bbcbb5201185b2ac2982bd6030e3`, and rechecked before this write at main `c4713fdd5dfff0f0f7eadf256fe059fdb2a6c10a`. The active README/OWNER-control Git blob remained `3d4a9372c87802ab734141a3374d04c8823372e3`, revision `2026-09-22.2`, with `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` active and no fleet02/B05 stop. Whole-file/OWNER-message SHA-256 values are `UNVERIFIED_CURRENT_RUN`; immutable Git identities are recorded rather than inventing hashes not independently materialized as exact native bytes.

Control/source Git blobs used at the fresh startup point:

- `AGENTS.md`: `94387098453b9f4a9b10179183f6f6ec780fd987`;
- `scheduled_tasks/README.md`: `3d4a9372c87802ab734141a3374d04c8823372e3`;
- `scheduled_tasks/fleet.json`: `e647d5d2479749f80ce7bb4862bee0f28513c7d9`;
- `scheduled_tasks/roles.json`: `ed17ecc94f76720c0345b3e32249b791b20ec611`;
- `scheduled_tasks/PROTOCOL.md`: `83a9268bf5287ca203e4be69a79e25382397bca7`;
- collective `ORDER.md`: `a70e03208ae00795ca7c6cdf9b7dbce854347138`;
- `TARGETS.md`: `a8cafa98cdb074ed15d0e214f8f54ee514c500df`.

The owner reallocation supersedes older brain-installation and benchmark work. No such work was performed.

The primary literature boundary remains the one recorded in `TARGETS.md`: Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), proves the threshold only for cycles that are directed or become directed after reversing one arc and explicitly leaves the genuine `k>=4` problem unresolved. No nearly-directed cycle is counted below.

## Exact team mathematics consumed

Latest complete campaign-lead package available at the substantive start and rechecked before this write:

- fleet02/B04 `20260922T031823Z-a02-b04-bt4-r11`, primary report blob `17d49d472779d5304d30b93c07ce89c289ab20d1`;
- controlling frontier addendum blob `28fe813aa044e57bbb3c6934a9ea76525bc04968`.

The addendum is controlling. Its current first interface is `SC+`: a canonical no-six remainder sink has a direct source inport, fan pattern `(3,2,2)`, an exact neutral source pivot, and additional x-free cross structure. In the four-remainder branch it reduces the splice frontier to an opposite-cross pair, a short source-return cycle, or heavy-triangle saturation, without claiming that one cross already gives two replacement cycles.

Named OTHER-account partner actually consumed and applied:

- fleet03/B06 `BT4-G1-CORRIDOR-DEFECT-v1`, run `20260922T032151Z-B06-BT4-r11`, report blob `3274cd23c22800504b5e7848b00be17869fa4b95`.

Its proved bridge-or-slack lemma says that, for two same-heavy G1-S witnesses with distinct heavy ports, a carrying fan corridor of fan size `m>=3` is either tight and yields the genuine two-edge port bridge, or a bridge-free corridor has gap at least `m+1`. Its exact constrained certificate also shows that local degree seven, arc domination, 3-vertex-strongness and old/new remainder acyclicity do **not** by themselves close the defect-one branch; global packing minimality is the missing resource. The argument below deliberately spends that resource rather than attempt another local-connectivity contradiction. A concrete corollary of the partner lemma is recorded at the end for the bounded branch produced here.

The immediate geometry attacked comes from the newer compatible OTHER-account result:

- fleet04/B06 `BT4-R4-LOWFAN-INPORT-TRIANGLE-v1`, run `20260922T041133Z-b06-bt4-r13`, report blob `d95ac60508cb0a415c33106169d1527da385406f`.

Its long-source F2 conclusion is the exact `R4-TWOSINK-SPLICE` state used below. No peer outcome label is used as a theorem; only the proved statements are imported.

## Inherited normal form and the exact two-sink state

Assume BT4 false and work in the inherited oriented exact-outdegree-seven, arc-dominated, 3-vertex-strong minimum-counterexample normal form. Let `(H,S,U)` be a globally minimum-total packing of three directed cycles and let the nonempty remainder `R` be acyclic. Packed cycles are chordless.

In the four-remainder global-NO-SIX long-source F2 branch of fleet04/B06, write consecutive source vertices

`p -> q -> s -> t -> ... -> p`

with `|S|>=6`, and

`R={x,y,z,c}`

after naming `y` as the second sink and `z` as the other member of the F2 pair. The imported exact relations are:

1. `x` and `y` are distinct sinks of `D[R]`;
2. `p->x`, with source fan `N+(x) intersect S={q,s}`;
3. `q->y`, with source fan `N+(y) intersect S={s,t}`;
4. `x` has heavy fan three on `H` and light fan two on `U`;
5. there is a unique other-light inport `u in U -> x`, with

   `N+(x) intersect U={u+,u++}`;

6. `c->x`, and the complete in-neighborhood of `x` is `{p,u,c}`;
7. the induced orientation on `{p,u,c}` is a directed triangle;
8. F2 gives `q->y` and `q->z`, while `q not->c`.

The imported proof also shows that `y,z` cannot reach `x` or `c` inside the old remainder when `|S|>=6`.

The first unpaid implication before this run was to use the two adjacent sink ports and the inport triangle to obtain a legal splice, strict minimum-packing reduction, exchanged-remainder cycle, SIX state or fourth directed cycle.

## Lemma 1 — the two adjacent sink pivots can be performed simultaneously

Define

`v=u+`.

The two directed cycles

`S_y = q -> y -> t -> S[t,q]`,

`U_x = u -> x -> u++ -> U[u++,u]`

are vertex-disjoint, satisfy

`|S_y|=|S|`, `|U_x|=|U|`,

and are disjoint from `H`. Consequently

`(H,S_y,U_x)`

is another globally minimum three-cycle packing. Its remainder is exactly

`R''={c,z,s,v}`

and `D[R'']` is acyclic.

### Proof

For `y`, the direct inport is `q->y` and its source fan is the consecutive pair `{s,t}`. Replacing the two-edge source segment `q->s->t` by `q->y->t` therefore preserves cycle order and frees `s`.

For `x`, the direct U-inport is `u->x` and its U-fan is the consecutive pair `{v=u+,u++}`. Replacing `u->v->u++` by `u->x->u++` preserves cycle order and frees `v`.

The two operations act on disjoint old packed cycles and use distinct remainder vertices `x,y`, hence the replacement cycles are vertex-disjoint. Total packing order is unchanged, so global minimality makes the new packing globally minimum as well. If `D[R'']` contained a directed cycle, that cycle together with `H,S_y,U_x` would be four pairwise vertex-disjoint genuine directed cycles, contradicting the assumed counterexample. QED.

This is the first useful consequence of the adjacent two-sink state that does not force the two sink crosses to share a packed segment: the two equality moves commute because they live on different light cycles.

## Lemma 2 — both newly freed vertices have a one-support-edge exact budget

In the new packing `(H,S_y,U_x)`,

`N+(s) intersect S_y={t}`,

`N+(v) intersect U_x={u++}`.

Let

`e_s=d^+_{D[R'']}(s)`, `e_v=d^+_{D[R'']}(v)`.

Then exact outdegree seven gives

`d^+_{H union U_x}(s)=6-e_s`,

`d^+_{H union S_y}(v)=6-e_v`.

Therefore:

- if `e_s=0` or `e_v=0`, the corresponding freed vertex is a SIX witness for the complementary packed pair;
- if `e_s=1` or `e_v=1`, the corresponding freed vertex is a five-witness for that pair;
- the only branch escaping those immediate deficit interfaces has `e_s,e_v>=2`.

### Proof

Old chordlessness of `S` leaves `s` only its old successor `t` among old S vertices. The new support adds `y`, but `y->s`, so orientation forbids `s->y`. Thus `t` is the unique S-support outneighbor of `s`.

Likewise old chordlessness of `U` leaves `v=u+` only its old successor `u++`; the new U-support adds `x`, but `x->v`, so orientation forbids `v->x`.

Subtract the one support edge and the `R''` exits from exact outdegree seven. The final classification is exactly the usual pair-deletion residual-degree accounting. QED.

## Lemma 3 — high exit on both freed vertices must hit the old inport vertex c

Assume

`e_s>=2`, `e_v>=2`.

Then at least one of

`s->c`, `v->c`

holds.

### Proof

If neither arc existed, the only possible `R''` outneighbors of `s` would be `{v,z}`. Since `e_s>=2`, both `s->v` and `s->z` would hold. Similarly the only possible `R''` outneighbors of `v` would be `{s,z}`, so `e_v>=2` would force `v->s` and `v->z`. This creates the forbidden digon `s<->v` in the oriented minimum counterexample. QED.

The two-freed-vertex wall therefore cannot remain diffuse: once both vertices avoid the named SIX/five interfaces, one of them must flow into the same old remainder vertex `c` that completes the exact inport triangle at `x`.

## Theorem — double-pivot high-exit collapse

> **BT4-R4-DOUBLE-PIVOT-CONFLUENCE-v1.** In the imported long-source F2 two-sink state with `|R|=4` and `|S|>=6`, perform the simultaneous neutral pivots of Lemma 1. If neither freed vertex enters the SIX/five-witness interfaces, so `e_s,e_v>=2`, then
>
> `|S|=6` **or** `|U|<=4`.
>
> More precisely, the two possible orientations of the forced triangle on `{p,u,c}` give the two alternatives below.

### Proof

Because `{p,u,c}` is a directed triangle, exactly one of the following orientations holds.

### Case A: `p->u->c->p`

If `s->c`, then

`c -> p -> q -> y -> s -> c`

is a genuine directed 5-cycle. It is disjoint from `H` and `U_x`: its packed vertices lie only on `S_y`, and its remaining vertices `c,s` lie in `R''`. Replacing `S_y` by this 5-cycle while keeping `H,U_x` gives a three-cycle packing of smaller total order because `|S|>=6`. This contradicts global minimality.

Hence `s not->c`. Lemma 3 now forces `v->c`. Since `e_s>=2` and the only possible `R''` outneighbors of `s` other than `c` are `v,z`, we must have `s->v` (indeed also `s->z`). Therefore

`c -> p -> q -> y -> s -> v -> c`

is a genuine directed 6-cycle, again disjoint from `H` and `U_x`. Replacing `S_y` by it gives a globally valid three-cycle packing of total order

`6+|H|+|U|`.

Global minimality yields `|S|<=6`. Combined with the standing `|S|>=6`, this forces

`|S|=6`.

### Case B: `u->p->c->u`

If `v->c`, then

`u -> v -> c -> u`

is a genuine directed triangle, disjoint from `H` and `S_y`. Replacing `U_x` by this triangle yields `|U|<=3`; orientation gives `|U|>=3`, so in fact `|U|=3`.

If `v not->c`, Lemma 3 forces `s->c`. Then

`c -> u -> x -> s -> c`

is a genuine directed 4-cycle, disjoint from `H` and `S_y`. Replacing `U_x` by it gives `|U|<=4`.

Thus Case B always gives `|U|<=4`. The theorem follows. QED.

## Application of the named fleet03/B06 bridge-or-slack result

The bounded `|U|<=4` output removes the partner's defect-one distinct-port corridor whenever `U` later serves as the heavy target of a same-heavy G1-S witness pair. Indeed fleet03/B06 proves that a bridge-free carrying corridor for fan `m>=3` must have directed port gap at least `m+1>=4`. Between distinct ports on a directed cycle of order at most four the forward gap is at most three. Therefore, in that bounded branch, a distinct-port same-heavy pair on `U` cannot be bridge-free: the partner dichotomy forces the genuine two-edge port bridge. The common-port branch remains separate.

This is a direct use of the named partner theorem, not a claim that every bounded state is already G1-S or that the bridge itself is a fourth cycle.

The partner's explicit 22-vertex certificate also explains why the proof above uses global packing minimality at the decisive points: purely local exact-degree/domination/strong-connectivity/acyclicity data admit the sharp bridge-free defect-one geometry. The new 5-, 6-, 4- and 3-cycle comparisons spend precisely the missing global-minimum resource.

## Updated conditional end-to-end argument

At the current four-remainder long-source F2 frontier, the lead/fleet04-B06 route can now be sharpened as follows.

1. The adjacent sink state provides the exact inport triangle and two neutral sink pivots.
2. Perform the two pivots simultaneously on `S` and `U`.
3. If either freed vertex has zero remainder exits, enter SIX.
4. If either has one remainder exit, enter the existing five-witness collar/linkage interface.
5. If both have at least two remainder exits, the theorem above forces the bounded residual

   `|S|=6` or `|U|<=4`.

6. On `|U|<=4`, the named partner's distinct-port bridge-free G1-S corridor is impossible when `U` is the heavy target; only a port bridge or common port remains there.

Thus the formerly arbitrary long-source `R4-TWOSINK-SPLICE` branch is no longer an unbounded splice problem once both freed vertices have high remainder exit. It collapses to a six-vertex source boundary or a light cycle of order at most four.

## First remaining implication

The first new bounded obligation is:

> **BT4-R4-BOUNDARY-CLOSURE-v1.** Close the high-exit double-pivot residual when `|S|=6` or `|U|<=4`, using the explicit 6-/4-/3-cycle equality objects above together with the partner's forced port bridge/common-port split; and close the `e=1` output through the already established five-witness collar without losing vertex-disjointness. The SIX interface remains the separate campaign obligation.

This is strictly smaller than the incoming `R4-TWOSINK-SPLICE` statement: no unbounded source/light-cycle geometry remains in its high-exit branch.

## Failure checks and nonclaims

- The simultaneous double pivot gives another minimum three-packing, not a fourth cycle by itself.
- A five-witness is an existing structural interface, not automatically a completed splice.
- The `|S|=6` and `|U|<=4` conclusions are boundary reductions, not routine subclasses substituted for BT4; they arise necessarily inside the source-exact counterexample branch.
- The partner port bridge is not counted as a cycle or a two-cycle replacement.
- No edge-disjoint or near-directed surrogate is used.
- No computation is used in the proof; all finite case splits above are exact symbolic arguments.
- Full BT4 remains open. No novelty claim is made.

## Before / after and honest classification

**Before:** the current four-remainder long-source F2 state had two adjacent sink ports and two disjoint canonical sink-cross interiors, but no legal splice and no bound on the source length beyond `|S|>=6`.

**After:** two disjoint equality pivots commute. Their freed vertices each have exactly one support outedge. If either has at most one remainder exit, the state regenerates SIX/five-witness machinery. If both have at least two exits, acyclicity/orientation force a hit on the inport-triangle vertex `c`; global minimum then produces explicit 5/6/4/3-cycle comparisons and forces `|S|=6` or `|U|<=4`. In the `|U|<=4` branch the named fleet03/B06 bridge-free distinct-port corridor is impossible for a heavy fan of size at least three.

Run classification: `ESSENTIAL_STEP_APPLIED`.  
Parent BT4 status: `OPEN_NOT_PROVED`.

## Operational provenance

Current-account scheduler inspection exposed all twenty managed B01--B20 tasks enabled on hourly cadences with quiet notification/email flags, with B05 role-aligned and no deficit requiring a B20 repair. No scheduler mutation was made. No cross-account native action, email, Drive action, public post, paid model/API/Codex call, remote workflow, permission change or benchmark-gold access occurred.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: `maximum actually supported`. Configured reasoning effort: `UNKNOWN / not exposed`. Known effective effort: `UNKNOWN`. Provider reasoning-token usage: `null / not exposed`; provider thinking-time counter: `null / not exposed`. Elapsed execution at scientific-report write: `705.499` seconds of UTC wall/tool time, not pure thinking.
