# fleet02/B20 BT4 research report — lowfan return collapse

Run: `20260922T040022Z-fleet02-B20-bt4-r13`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Target: BT4  
Classification: `ESSENTIAL_STEP_APPLIED`  
FULL_TARGET_CHANGE: `NONE`  
MECHANISM_CHANGE: `YES — post-pivot F3 is reduced to CROSS/FOUR_CYCLES and the F2 reverse-remainder-inport branch is reduced to the same outcomes; the remaining F2 direct-packed-inport branch becomes an explicit neutral-orbit problem.`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

No full BT4 proof is claimed.

## Model / effort declaration

Model self-report: GPT-5.6 Sol. Requested effort: highest useful effort allowed by the current runtime. Configured effort: `UNKNOWN_NOT_EXPOSED`. Known effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token and thinking-time counters are not exposed. Wall-clock execution includes repository/tool time and is not pure thinking.

## Exact controlling inputs

Fresh campaign lead:
- controlling frontier addendum `fleet02-B04-20260922T031823Z-r11-frontier.md`, blob `a9064e9a9c82130029ee90f37991af3a34e75c54`.

Named OTHER-account partner:
- fleet04/B06 `BT4-SINKLINK-v1`, handoff `20260922T021002Z-fleet04-B06.md`, blob `e925675bebb02129deeec2b1902cc11b5e246dde`. I use this in the conditional end-to-end skeleton for the exact-six dual-collar / exchange-tax branch. Its cycle-supported witness is not transplanted into the present lowfan state: here the freed witness is in the remainder and has `e=2` or `e=3` remainder exits.

Other exact inputs used in the derivation:
- fleet02/B05 post-pivot two-arm theorem, handoff `20260922T0326Z-fleet02-B05.md`, blob `7c14eaf41ddd4761ee256eb82e7e2994fac4806a`;
- fleet04/B04 `BT4-R4-FREED-PROFILE-v1`, handoff `20260922T035130Z-fleet04-B04.md`, blob `91963fe8256cc0fce04d2f737e14915cb331bea5`;
- fleet03/B04 `BT4-R4-F3-TWOFAN-COLLAPSE-v1`, handoff `20260922T040151Z-fleet03-B04-F3-twofan-collapse.md`, blob `76bf4e46377212afac499a6be37410387cb5c183`.

The most recent three B20 substantive runs changed mechanism each time (six-fan collar/two-pivot collision, reserved-exit collision funnel, aligned ladder-ray exchange tax), so there is no three-run unchanged-gap trigger here.

Section-B method choices for this run: #19 make it an algorithm (turn the F2/F3 split into an explicit reduction procedure), #20 find why the algorithm fails (identify the unique neutral-orbit branch), and #30 localize one scale/direction at a time (solve F3, then the F2 reverse-inport branch, without pretending the remaining F2 orbit vanished).

## Inherited post-pivot normal form

Work in a finite loopless digraph with at most one arc per ordered pair, in the lead's oriented exact-outdegree-seven minimal-counterexample normal form. Fix a globally minimum packing of three vertex-disjoint directed cycles. In the sharp four-remainder NO-SIX sink branch, after the canonical neutral pivot write the packed cycles as `(S*,H,U)` and the acyclic remainder as `R*` with `|R*|=4`.

Use the lead/B05 notation: `p` is the predecessor on the source cycle, old sink `x` has been inserted on `S*`, and the freed vertex is `q=p+`. Thus

`S* = p -> x -> p++ -> S[p++,p]`,

`R*=(R-{x}) union {q}`,

and `q` has exactly one outneighbor on `S*`, namely `p++`.

Let `e=d^+_{R*}(q)`. fleet04/B04 reduces every non-SIX/non-heavy-cross state to:

- F2: `e=2`, profile `(H,U,S*,R*)=(2,2,1,2)`. If `r0` is the unique vertex of `R*-{q}` not dominated by `q`, then either `r0->q` or there is a direct packed inport from `H union U` to `q`.
- F3: `e=3`, profile `(2,1,1,3)` up to swapping `H,U`; `q` dominates all three vertices of `R*-{q}` and has a direct packed inport.

For `e>=2`, fleet02/B05 supplies two internally vertex-disjoint return arms from two distinct exits. If an arm first hits `H` or `U`, it is a genuine cross-packed transition. Otherwise the first packed hits are distinct vertices `a1,a2` on `S*`, giving two same-support bypasses from `p`; if the i-th bypass has length `ell_i` and forward source-cycle distance `d_i=d_{S*}(p,a_i)`, global packing minimality gives `ell_i>=d_i`, with equality a neutral same-support exchange.

## New theorem 1 — F3 cannot remain two-arm strict

**Lemma (F3 return collapse).** In F3, either a two-arm escape reaches `H union U`, or there is a neutral same-support exchange. Consequently, after at most one such neutral exchange, the state yields a genuine cross-packed transition or four vertex-disjoint directed cycles.

**Proof.** Assume neither arm reaches `H union U`; let their distinct first hits be `a1,a2 in S*\{p,x}`. Let `k_i>=1` be the number of vertices of `R*-{q}` used internally after the exit from `q` and before the first packed hit on arm i. Since the two return arms are internally vertex-disjoint and `R*-{q}` has only three vertices,

`k_1+k_2 <= 3`.

The bypass from `p` is `p->q` followed by the arm, hence

`ell_i = k_i+2`.

Suppose both bypasses are strict. Since all quantities are integers,

`d_i <= ell_i-1`,

so

`d_1+d_2 <= (k_1+k_2)+2 <= 5`.

But `a1,a2` are distinct and neither is `p` (distance 0) nor `x` (distance 1). Therefore the two smallest possible forward distances are 2 and 3, giving

`d_1+d_2 >= 5`.

Equality holds throughout. Hence `{d_1,d_2}={2,3}`, `k_1+k_2=3`, and each strict excess is exactly one. The arm ending at forward distance 3 uses two vertices after `q`, say

`p -> q -> r -> s -> p+++`.

F3 says `q` dominates every vertex of `R*-{q}`, so in particular `q->s`. Therefore

`p -> q -> s -> p+++`

is a same-support bypass of length 3 to a vertex at forward distance 3, i.e. a neutral exchange. Contradiction. This proves the first assertion.

Now perform any nontrivial neutral same-support exchange obtained this way. Its endpoint has distance at least 3, so the exchanged source segment contains `x` and `p++`; the new support contains `q`, while `x` returns to the new four-vertex remainder. Before the first pivot, `x` was a sink of the old remainder, hence had no arcs to that old remainder. Its exact outdegree-seven sink profile consisted of the source targets `q,p++` plus the `3+2` fan on `H,U` (up to relabeling). After the neutral exchange, `q` lies on the new support and `p++` lies in the new remainder, so `x` has exactly one support outneighbor, exactly one remainder outneighbor, and a packed fan of size at least three. If the exchanged remainder is cyclic, that cycle together with the three packed cycles gives four vertex-disjoint directed cycles. If it is acyclic, fleet04/B04's `e>=1` heavy-fan return-cross lemma applies to `x` and yields a genuine cross-packed transition. QED.

This strictly strengthens the F3 frontier: fleet03/B04 reduced the two-fan packed-inport subcase to a neutral pivot / lower branch; the counting above removes the entire two-arm-strict possibility before the packed-inport wedge needs separate treatment.

## New theorem 2 — F2 with reverse remainder inport collapses

Write `R*={q,r0,r1,r2}` with `q->r1,q->r2` and `q !-> r0`.

**Lemma (F2 reverse-inport collapse).** In the F2 subbranch `r0->q`, the B05 two-arm conclusion yields a cross-packed transition or a neutral same-support exchange; after a neutral exchange the state yields a cross-packed transition or four vertex-disjoint directed cycles.

**Proof.** Again suppose neither return arm first hits `H union U`. In the standard internally vertex-disjoint linkage supplied by B05, the two first-hit arms are disjoint outside their common source `q`. No arm can traverse `r0` before its first packed hit: if the arm from exit `ri` contained `r0`, then `q->ri->...->r0->q` would be a directed cycle wholly in acyclic `R*`. Thus each first-hit arm uses only its own exit vertex before reaching `S*`, and each induced bypass has length exactly 3:

`p -> q -> r_i -> a_i`.

If both were strict, then `d_{S*}(p,a_i)<=2`. The two hits are distinct and exclude `p` and `x`; among vertices at forward distance at most 2 the only remaining possibility is `p++`. Two distinct hits cannot both equal `p++`. Hence one bypass is neutral. The same post-exchange argument as above makes old `x` an `e=1`, support-degree-one, heavy-fan remainder vertex, so an exchanged-remainder cycle gives four cycles and otherwise fleet04/B04 gives a genuine cross. QED.

## Exact residual — F2 direct packed inport is a neutral-orbit problem

It remains to handle the other F2 alternative: `r0 !-> q`, so fleet04/B04 forces a direct packed inport `t->q` from some packed cycle `T in {H,U}`. In F2, q has exactly two outtargets on T only when T is the corresponding two-fan target cycle. For either target `b`,

`t -> q -> b -> T[b,t]`

is a directed cycle. Global minimum of the packed total forces `d_T(t,b)<=2`; orientation excludes `b=t`. Since the two targets are distinct, they are exactly `{t+,t++}`. Therefore

`T' = t -> q -> t++ -> T[t++,t]`

is a size-neutral packed-cycle exchange that frees `t+`.

This is the first exact unpaid lowfan implication now:

**BT4-R4-F2-NEUTRAL-ORBIT-CLOSURE.** For every inherited oriented exact-outdegree-seven globally minimum three-cycle packing with acyclic four-vertex remainder in the post-pivot F2 direct-packed-inport state above, prove that the neutral exchange on T cannot iterate in a closed orbit without producing at least one of: (i) a strict smaller three-cycle packing, (ii) a directed cycle in the exchanged remainder (hence four disjoint cycles), (iii) a SIX witness, or (iv) a genuine cross configuration that the current two-cycle replacement machinery converts to a legal strict replacement.

The quantifiers are universal over graph order, all permitted digraphs, all globally minimum three-cycle packings and all F2 states produced by the lead's neutral sink pivot. Digons are allowed in the original theorem; the oriented normal form is inherited from the lead's minimal-counterexample reduction, not assumed for arbitrary input digraphs.

## Conditional end-to-end status

Conditional on the campaign's existing minimal-counterexample reduction, sharp sink split, fleet04/B06 exact-six dual-collar/exchange branch, and the lead's canonical neutral pivot, all post-pivot lowfan states except the F2 direct-packed-inport neutral orbit above now reduce to SIX, CROSS, strict packing reduction, exchanged-remainder cycle, or the already isolated broader campaign branches. A CROSS is not itself counted as a fourth cycle. Thus this report does not close BT4; it removes F3 and the F2 reverse-remainder-inport branch as independent walls and localizes the lowfan obstruction to one explicit neutral orbit plus the campaign's still-open cross-to-replacement closure.

## Before / after / next method

Before: lowfan frontier = full F2/F3 splice closure.  
After: F3 -> CROSS/FOUR_CYCLES after at most one neutral same-support exchange; F2 with `r0->q` -> CROSS/FOUR_CYCLES; F2 direct-packed-inport -> explicit size-neutral exchange freeing `t+`.  
Target-level movement: none; BT4 remains open.  
Mechanism movement: material.  
Stagnation: no three-run unchanged implication; route changed from ladder-ray exchange tax to a finite lowfan return-collapse / neutral-orbit reduction.  
Next method: put a lexicographic monovariant on successive neutral exchanges (freed-vertex position, number/location of remainder exits, and support-distance of the forced packed inport). If a monovariant fails, construct the resulting periodic orbit explicitly and combine its repeated inport/outport incidences with the lead's three x-free crosses or fleet03/B05's corrected two-linkage trichotomy to force a strict two-cycle replacement.

No finite search, larger degree threshold, edge-disjoint relaxation, nearly-directed cycle, or one-reversed-arc theorem was substituted for the stated BT4 target.
