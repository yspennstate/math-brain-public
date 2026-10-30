# BT4 fleet02/B05 — U1 external-dominator escape and forced cross-cycle defect repair

Run: `20260922T005110Z-b05-bt4-13b45ffe`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Candidate: `BT4-RSC-v3-dominator-escape`
Outcome: `ESSENTIAL_STEP_APPLIED`
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source scope

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem and a digon counts as a directed cycle.

The current primary-source check remains Bessy–Muis–Sereni–Steiner–Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). It explicitly leaves the genuine directed-cycle conjecture open for every `k>=4` and proves at threshold `2k-1` only four disjoint cycles each of which is directed or can be made directed by reversing one arc. This run does not promote a one-reversal cycle to a directed cycle.

Control/source identities consumed at run start were: common-control commit `370853819029cd4eb753e8b2fb83c9994457e8a2`; AGENTS blob `94387098453b9f4a9b10179183f6f6ec780fd987`; README/OWNER blob `3d4a9372c87802ab734141a3374d04c8823372e3`; fleet blob `e647d5d2479749f80ce7bb4862bee0f28513c7d9`; roles blob `ed17ecc94f76720c0345b3e32249b791b20ec611`; PROTOCOL blob `83a9268bf5287ca203e4be69a79e25382397bca7`; collective ORDER blob `a70e03208ae00795ca7c6cdf9b7dbce854347138`; TARGETS blob `a8cafa98cdb074ed15d0e214f8f54ee514c500df`; ASSIGNMENTS blob `fe144a4be3522d57f8cb2dc40b1fc57df7c7f7da`. Owner revision was `2026-09-22.2`; no later stop was present at the start read.

## Exact peer mathematics consumed

I used the campaign lead fleet02/B04 run `20260922T001806Z-b04-bt4-a1ceeb3c`: report blob `d82fc84180bc66fd660c6c79f9a7f26332bdae72` and correction blob `ef92cfc95fab44c1e256757de5fae4ec4b28e36b`. The correction is controlling where it narrows the equality case.

I also consumed the named OTHER-account partner fleet03/B06 run `20260922T002129Z-fleet03-B06-bt4-r11`, report blob `81a20ff15088e74009551fffd8e9f4812b781819`, candidate `BT4-RSC-v2-tight-port`. Its decisive U1 inputs are the tight consecutive fan, single-port boundary, equal-size exchange and acyclic exchanged remainder/inversion prohibition.

Two compatible dependencies were used rather than rederived: fleet01/B04 `BT4-MCR-v2`, report blob `79c91a55da8f23489bf3a18c8fc874e588b5ce12`, for the corrected path-fan lemma and six-fan-or-three-five-fans pair-deletion amplification; and fleet04/B05 handoff `BT4-COUNT-v1`, blob `9ce99798e661e4d14b2b27a0f647b909eff715b4`, for the no-six-fan consequence that every remainder sink has fan pattern `(3,2,2)` up to permutation.

## Conditional end-to-end route retained

Assume a counterexample and pass to the lead's exact-seven, oriented, arc-dominated normal form retaining a globally minimum three-cycle packing `C1,C2,C3` with DAG remainder `R`. Refine by the partner's longest-remainder-path choice. Let `x` be the chosen sink and `C` a heavy packed cycle.

The route is now:

1. a strict `C`-to-`x` return shorter than `m-1`, where `m=|N+(x)∩C|`, contradicts the corrected path-fan lemma;
2. in nonsaturated U1, a tight return of length `m-1` has the partner's unique port and consecutive fan and yields an equal-size exchange `C*`; its exchanged remainder `R'` must remain acyclic;
3. pair deletion supplies a six-fan witness or three five-fan witnesses for every packed-cycle pair;
4. the new lemma below shows that a tight U1 return cannot keep all one-reversal/transitive-triangle defects inside the tight theta: arc domination forces an external fork into `R\P` or another packed cycle;
5. therefore the next universal step is genuinely a two-cycle/cross-packing rerouting statement. A remainder-only repair is impossible in the `R\P` branch because it would contradict acyclicity of `R'`.

If that final cross-packing rerouting is proved, it creates either a shorter three-cycle packing or a fourth directed cycle; either contradicts the assumed minimum counterexample. The saturated whole-cycle-fan U1 branch `m=|C|` is not covered by the new lemma and remains separate.

## Setup for the new U1 lemma

Work in the nonsaturated U1 branch of the named partner. Write the chordless directed cycle as

`C=(b=b_0,b_1,b_2,...,b_{r-1},b)`

with `3<=m<r`. Choose the tight return so that

`P: b=p_0 -> p_1 -> ... -> p_(m-1)=x`

and `p_1,...,p_(m-1)` lie in `R`, with `p_1 -> ... -> x` a shortest `R`-path of length `m-2`. The partner proves

`N+(x) ∩ C = {b_1,...,b_m}`.

Replacing `C` by the equal-size cycle

`C* = b -> p_1 -> ... -> x -> b_m -> ... -> b`

frees `F={b_1,...,b_(m-1)}` and consumes `Q={p_1,...,p_(m-1)}`. Thus

`R'=(R\Q) union F`

is acyclic in a true counterexample.

We repeatedly use the following target-location form of the corrected path-fan proof. If `p_h -> b_i`, then

`i <= h+1`.                                                     (TL)

Indeed, if `i>=h+2`, then `b -> p_1 -> ... -> p_h -> b_i` followed by the forward segment of `C` back to `b` is a directed cycle shorter than `C`, contradicting minimum total packing size.

## New lemma — external-dominator escape from every noninitial freed vertex

**Lemma.** For every `i` with `2<=i<=m-1`, there exist an index

`i-1 <= j_i <= m-1`

and a vertex

`d_i notin V(C) union {p_1,...,p_(m-1)}`

such that

`d_i -> p_(j_i)` and `d_i -> b_i`.                                (E_i)

Equivalently, the arc `p_(j_i)->b_i` lies in the transitive triangle

`d_i -> p_(j_i) -> b_i`, together with `d_i -> b_i`,

whose one reversed-arc defect is exactly the absent reverse direction `b_i -> d_i`.

### Proof

Fix `i` in `2,...,m-1`. The fan identity gives `x=p_(m-1) -> b_i`. Since every arc of the exact-seven minimum counterexample is dominated, choose a vertex `z` with

`z->x` and `z->b_i`.

First, `z` cannot lie on `C`. Since `C` is chordless, the only vertex of `C` that can send an arc to `b_i` is its predecessor `b_(i-1)`. But `b_(i-1)->x` would be a direct arc from the heavy cycle `C` to `x`, impossible because `m>=3` by the one-vertex minimum-packing exchange lemma.

If `z` is outside both `C` and the `R`-vertices of `P`, we are done with `j_i=m-1`. Otherwise `z=p_h` for some `h<=m-2`. By (TL), `p_h->b_i` implies `h>=i-1`.

Now dominate the arc `p_h->b_i`. Let `z'` dominate it, so `z'->p_h` and `z'->b_i`.

A dominator `z'` cannot lie on `C`. Chordlessness would again force `z'=b_(i-1)`. If `h>=2`, the path

`b_(i-1) -> p_h -> p_(h+1) -> ... -> x`

has length `m-h <= m-2`, contradicting the path-fan lower bound `m-1` for every `C`-to-`x` return through `R`. If `h=1`, then necessarily `i=2`; now `b_1->p_1` would be a second `C`-port into the boundary layer at distance `m-2` from `x`, contradicting the partner's single-port boundary lemma, whose unique tail is `b`.

If `z'` lies on the path, say `z'=p_t`, then acyclicity of `R` forces `t<h`: if `t>h`, the existing path `p_h->...->p_t` together with `p_t->p_h` is a directed cycle, while `t=h` would require a loop. Applying (TL) to `p_t->b_i` also gives `t>=i-1`.

Thus every time domination stays on `P`, the path index strictly decreases while remaining at least `i-1`. The process is finite. At index `i-1` no further path vertex can dominate the current arc, because a path dominator would have to satisfy simultaneously `t<i-1` and `t>=i-1`. We already excluded a dominator on `C`. Hence some domination step exits `C union P`, yielding `(E_i)`. QED.

## Terminal fork corollary and the exact defect location

Take `i=m-1`. Then `j_i` can only be `m-2` or `m-1`, so there is a vertex

`d notin C union P`

with

`d->b_(m-1)` and either `d->x` or `d->p_(m-2)`.                  (TF)

This is substantially tighter than a generic external-neighbor statement: the external vertex hits the final freed vertex and one of the last two vertices of the tight return.

Its location has only two types.

- If `d in R\Q`, then `d` reaches `x` inside `R` in at most two arcs. After the equal-size exchange both `d` and `b_(m-1)` lie in `R'`, and `d->b_(m-1)` is an arc of `R'`. Since `R'` is acyclic, **there is no directed path in `R'` from `b_(m-1)` back to `d`**. Thus the reverse-defect cannot be repaired wholly inside the exchanged remainder.
- If `d` lies on one of the other packed cycles `A`, then `d->x` is a direct return from `A`, forcing `|N+(x)∩A|<=2`; or `d->p_(m-2)->x` is a two-edge return, forcing `|N+(x)∩A|<=3` by the corrected path-fan lemma. Hence the exported defect is already attached to a light/at-most-three-fan packed cycle, exactly the geometry needed for a two-cycle splice rather than an uncontrolled global path.

So the recent relaxation's one-reversal obstruction has a precise form in the hardest tight branch: local domination repeatedly pushes the transitive-triangle defect out of the tight theta, but acyclicity prevents a remainder-only reverse path. Any successful repair must therefore use a packed cycle and preserve disjointness by a simultaneous exchange.

## Interaction with the no-six-fan counting branch

I also applied fleet04/B05 `BT4-COUNT-v1`, not as a substitute for the named partner. In the global no-six-fan branch, every remainder sink has sorted fan pattern `(3,2,2)`. Therefore a heavy U1 cycle necessarily has `m=3`.

The terminal fork then collapses to the exact two-step geometry

`b -> p_1 -> x`,
`N+(x)∩C={b_1,b_2,b_3}`,

and some `d outside C union {p_1,x}` satisfies

`d->b_2` and (`d->x` or `d->p_1`).

Thus the no-six-fan U1 branch does not contain an arbitrarily long unresolved return: it contains a single exported transitive-triangle defect adjacent to the last one or two levels of the sink collar. The pair-deletion theorem simultaneously supplies, for each of the two pairs involving `C`, at least two additional five-witnesses beyond the sink `x`. The remaining task is to force one of those witness supports to provide the necessary cross-cycle return/two-cycle splice through this explicit fork.

## What failed / what is not claimed

The new lemma does **not** prove that the vertices `d_i` are distinct. Outdegree seven alone permits concentration: a single external vertex may dominate several `p_j->b_i` arcs by using one arc into the path and several arcs into `C`. Any later argument that counts `m-2` distinct ports from the lemma is invalid without an additional separation argument.

Nor does the lemma prove a remainder-only repair. In the `d_i in R\Q` case such a repair is actually impossible after the equal-size exchange, because `d_i->b_i` lies in the acyclic `R'`. This explicitly eliminates a tempting but wrong mechanism and shows why the next step has to be a disjoint two-cycle exchange or a packed-cycle-assisted linkage.

The saturated branch `m=r` remains outside the partner's proper-block single-port lemma and outside this result. No claim is made for that branch here.

## Exact computation used

`escape_chain_checker.py` checks only the finite index descent `3<=m<=7` implied by exact outdegree seven. It is a sanity check, not the graph-theoretic proof. Exact stdout is archived in `checker_output.txt`; final line:

`PASS cases=15 m_range=3..7 forced_external=true`

For each pair `(m,i)` it enumerates all possible strictly decreasing on-path domination chains permitted by `i-1<=h<j` and confirms that the longest internal chain has length exactly `m-i` before an external dominator is forced.

## First remaining implication

The first essential missing implication for `BT4-RSC-v3-dominator-escape` is now:

> In the nonsaturated U1 terminal-fork configuration `(TF)`, combine the six-fan-or-three-five-fans witnesses for the two pairs involving `C` with the external fork. Prove that either (a) a witness-supported path gives a legal simultaneous two-cycle splice through a packed cycle, or (b) the witness support forces a directed cycle in the exchanged remainder `R'`, contradicting its acyclicity. In the no-six-fan branch it suffices to prove this for the explicit `m=3`, `(3,2,2)` geometry above. A path confined to `R'` from `b_(m-1)` to an `R'`-fork vertex cannot be assumed; it is forbidden by acyclicity and must be replaced by a cross-cycle linkage.

This is narrower than the partner's previous generic request to make an amplified witness create an inversion: the location of the first compulsory outside port is now explicit.

## Status

`ESSENTIAL_STEP_APPLIED`, not a full proof. BT4 remains open. No benchmark answer, installation work, production state, private archive, broad mixed-domain memory, or held-out data was used.

Next recipients: campaign lead `fleet02/B04`, named partner `fleet03/B06`, and fleet02/B20 for account-local research visibility.
