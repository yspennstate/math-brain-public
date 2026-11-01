# BT4 fleet03/B04 — F3 two-fan inport neutral collapse

Run: `20260922T035106Z-fleet03-B04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-F3-TWOFAN-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and assignment

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem, so directed digons count.

This slot's exact assignment is to use a genuinely different extremal/shortest-cycle or longest-path mechanism on the shared hard configurations, with the seven-outdegree budget explicit. This run therefore does not continue the earlier Menger/collar mechanism as its new proof step. It uses global minimum of the three-cycle packing and a neutral cycle replacement to collapse one of the current four-remainder residuals.

## Exact peer state consumed

Named OTHER-account partner consumed and applied:

- fleet04/B05, `BT4-COUNT-v3-FOUR-R-ESCAPE`, canonical report `proofnet24/collective-BT4/fleet04/B05/b05-20260922t020746z-r31/report.md`, creation commit `632e9bccbf1b5dec5db227580441652b58e85873`, report blob `1a21f9b5ea72de714311d6927183c73062323632`.

The exact partner conclusion used is that, in the inherited oriented exact-seven globally minimum three-packing with `|R|=4` and global NO-SIX, a featureless state is impossible: one gets a genuine cross-packed transition, a neutral minimum-packing exchange, or an explicit same-cycle remainder bypass. Its stated unpaid obligation is to consume the forced cross/bypass and to prevent a neutral orbit from merely regenerating the same obstruction.

Current controlling lead state also used:

- fleet02/B04, canonical sink-cross frontier shared blob `a9064e9a9c82130029ee90f37991af3a34e75c54`.

Current compatible refinement used:

- fleet04/B04, `BT4-R4-FREED-PROFILE-v1`, canonical report commit `5ee9a747d020fb77ab67dfc12844e1e623bf1a8e`, report blob `eae9c01b562dd2c417724aa0822117223026d796`.

Only source-bound mathematical statements are imported; no peer outcome label is used as proof.

## Inherited normal form and live F3 residual

Assume BT4 false and work in the inherited normal form: an oriented digraph `D` with exact outdegree seven at every vertex, a globally minimum-total packing of three chordless directed cycles, 3-vertex-strongness, and acyclic remainder. The lead's canonical NO-SIX sink pivot replaces the source light cycle `S` by

`S* = p -> x -> p++ -> S[p++,p]`

and frees `q=p+`, producing a four-vertex remainder `R*`.

The current freed-profile theorem reduces the no-new-heavy-cross state to two profiles. This report treats F3:

- the current packing is `(H,S*,U)`;
- `R*` has four vertices and is acyclic;
- `q` has exactly one outneighbor on `S*`;
- `q` dominates all three vertices of `R*-{q}`;
- the fan sizes from `q` into `H,U` are `{2,1}`;
- there is a direct packed inport `t->q` from some `T in {H,U}`.

Call the member of `{H,U}` receiving two `q`-arcs the **two-fan cycle** and the other the **one-fan cycle**.

The question is whether the F3 geometry can persist through a neutral exchange, which would leave the partner's four-remainder escape trapped in an equality orbit.

## Lemma 1 — an inport localizes every q-target to the last two predecessors

Let `T` be any packed cycle of length `n`, let `t in T` satisfy `t->q`, and let

`B = N+(q) intersect V(T)`.

Then

`B subset {t+,t++}`.

### Proof

For any `b in B`, the directed cycle

`Q_b = t -> q -> b -> T[b,t]`

uses only `q` outside `T`, hence it can replace `T` while remaining vertex-disjoint from the other two packed cycles. Its length is

`2 + d_T(b,t)`,

where `d_T(b,t)` is the forward distance on `T` from `b` to `t`.

Because the current three-cycle packing has globally minimum total size,

`2 + d_T(b,t) >= n`,

so

`d_T(b,t) >= n-2`.

Also `q->t` is impossible because `D` is oriented and `t->q`. On a directed `n`-cycle the only vertices other than `t` at forward distance at least `n-2` from `t` are `t+` and `t++`. Thus `B subset {t+,t++}`. QED.

In particular, if `T` is the two-fan cycle, then necessarily

`N+(q) intersect T = {t+,t++}`.                                      (1)

This is a pure extremal packing consequence; no linkage theorem is used.

## Lemma 2 — the two-fan inport gives a neutral pivot

Assume the packed inport `t->q` comes from the two-fan cycle `T`. Then

`T' = t -> q -> t++ -> T[t++,t]`

is a directed cycle of exactly the same length as `T`, and replacing `T` by `T'` frees `q'=t+`.

Moreover, relative to `T'`, the freed vertex `q'` has exactly one outneighbor on `T'`, namely `t++`.

### Proof

By (1), `q->t++`, so `T'` is directed. Its length is

`2 + d_T(t++,t) = 2 + (n-2) = n`.

Thus the replacement is size-neutral and preserves global minimum of the total three-packing.

The old cycle `T` is chordless, so `t+` has no old-`T` outneighbor other than `t++`. The only new vertex of `T'` is `q`. But (1) also gives `q->t+`, and orientation therefore forbids `t+->q`. Hence `q'=t+` has exactly the one support outarc `t+->t++` on `T'`. QED.

The new remainder is

`R' = (R* - {q}) union {q'}`,

again of size four. If `R'` itself contains a directed cycle then together with the three packed cycles we already have four disjoint cycles, so in a counterexample `R'` remains acyclic.

## Lemma 3 — a sink forces the new freed remainder degree down to at most two

Assume there is no genuine cross-packed transition already available from the inport cycle `T` to a different packed cycle. Then after the neutral pivot of Lemma 2,

`d^+_{R'}(q') <= 2`.

### Proof

Because `R*` is a finite DAG, choose a sink `s in R*`. F3 gives `q->s` because `q` dominates every other remainder vertex.

If a SIX witness exists for the current packing, that is already a separate campaign exit. So consider the remaining global-NO-SIX state. Since `s` is an `R*`-sink, all seven of its outgoing arcs go to the three packed cycles. Write their fan sizes in nonincreasing order as `a>=b>=c`. NO-SIX says every pair sum is at most five; equivalently each of `a,b,c` is at least two. Since `a+b+c=7`, necessarily

`(a,b,c)=(3,2,2)`.                                                    (2)

Let `C` be the heavy cycle receiving the three arcs. If `C != T`, then for any `c in N+(s) intersect C`,

`t -> q -> s -> c`

is a genuine cross-packed transition from `T` to `C`, with internal vertices `q,s` in the remainder. This is exactly the excluded cross. Therefore in the no-cross residual the heavy cycle in (2) is `T`, so

`|N+(s) intersect T| = 3`.                                            (3)

For each `b in N+(s) intersect T`, the cycle

`t -> q -> s -> b -> T[b,t]`

can replace `T` and is disjoint from the other two packed cycles. Global minimum therefore gives

`3 + d_T(b,t) >= n`,

or

`d_T(b,t) >= n-3`.                                                     (4)

Equation (3) plus (4) forces `s->t+` in every cycle length:

- if `n=3`, the three targets are all of `T`;
- if `n=4`, (4) excludes only `t`, so three targets force `{t+,t++,t+++}`;
- if `n>=5`, exactly the three vertices `t+,t++,t+++` have distance at least `n-3` from `t`, so all three are forced.

Thus `s->q'` after the neutral pivot. Since `D` is oriented, `q'->s` is impossible.

The new remainder `R'` has four vertices: `q'` and the three old vertices of `R*-{q}`, one of which is `s`. Therefore `q'` can dominate at most the other two, proving

`d^+_{R'}(q') <= 2`. QED.

## Theorem — F3 cannot regenerate through a two-fan neutral pivot

In an F3 state, if the guaranteed packed inport `t->q` comes from the two-fan cycle, then after the neutral replacement of Lemma 2 at least one of the following occurs:

1. **FOURTH CYCLE / SIX:** the exchanged remainder already contains a directed cycle, or the new state exposes a SIX witness;
2. **RETURN CROSS:** the new freed vertex `q'=t+` has remainder outdegree one, or has remainder outdegree two with an unbalanced packed fan, and the existing freed-profile heavy-fan lemma exports a genuine `q'`-avoiding cross-packed transition;
3. **F2:** the only no-cross/no-SIX residual has remainder outdegree two and exact profile `(2,2,1,2)` relative to the two non-support packed cycles, `T'`, and `R'`.

In particular, **F3 does not recur** after this neutral pivot.

### Proof

By Lemma 2, `q'` has exactly one support outneighbor on `T'`. By Lemma 3, its remainder outdegree `e'` is at most two in the no-cross residual. Exact outdegree seven leaves

`6-e'`

outarcs into the other two packed cycles.

- If `e'=0`, deleting those two cycles leaves `q'` residual outdegree one, so `q'` is a SIX witness.
- If `e'=1`, the two packed fans total five, so one has size at least three. The already-proved freed-profile heavy-fan lemma gives a `q'`-avoiding return cross.
- If `e'=2`, the two fans total four. Unless the split is exactly `2+2`, one fan has size at least three and again gives a return cross. The sole no-cross residual is therefore exact F2 `(2,2,1,2)`.

There is no case with `e'=3`, so F3 cannot recur. QED.

## Exact remaining F3 obstruction

The theorem sharply localizes what can remain if F3 is to avoid immediate collapse.

Let `C2` be the two-fan cycle and `C1` the one-fan cycle of `q`.

- There can be **no packed inport to q from `C2`** in a surviving F3 obstruction; any such inport triggers the theorem above.
- Since the inherited F3 theorem guarantees some packed inport from `C1 union C2`, at least one inport must therefore come from `C1`.
- If `b` is the unique `q`-target on `C1`, Lemma 1 says that for every inport `t->q` from `C1`, `b` is either `t+` or `t++`.
- If `b=t++` and `t+` is not itself an inport to `q`, the same neutral replacement frees `t+`; because neither direction between `q` and `t+` is present, the support-count part of Lemma 2 still holds and the collapse argument repeats. Hence a surviving one-fan state must contain the immediate-predecessor wedge

`b^- -> q -> b`,

possibly together with the second-predecessor inport `b^{--}->q`.

So the generic F3 reverse-inport obstruction has been reduced to a rigid **one-fan predecessor wedge**, with no reverse inport from the two-fan cycle.

This is the first unpaid state after the present theorem. A future splice must use that wedge together with the lead's three `x`-free transitions into the heavy cycle, or show that the optional second-predecessor inport forces a strict packing reduction.

## Direct application to the named partner's missing implication

Fleet04/B05's `BT4-COUNT-v3-FOUR-R-ESCAPE` left neutral equality exchanges as a possible four-remainder escape without proving that repeated neutral exchanges make progress. The theorem above pays one concrete part of that obligation: in F3, a neutral exchange generated by an inport from the two-fan cycle cannot simply regenerate F3. It strictly changes the state class to SIX, a genuine cross, or F2.

Thus the relevant equality orbit has a one-way structural descent

`F3(two-fan inport) -> {SIX, CROSS, F2}`,

not an F3 self-loop.

The remaining equality-orbit problem is confined to the one-fan predecessor-wedge residual described above and the separate F2 branch.

## Scope and failure checks

- The proof never promotes a cross-packed path to a fourth cycle; a cross is only linkage input.
- Every replacement cycle is written explicitly and uses only the replaced packed cycle plus named remainder vertices, so vertex-disjointness from the other two packed cycles is preserved.
- The seven-outdegree hypothesis is used exactly after each neutral pivot to obtain the residual fan totals.
- The sink argument uses the actual four-vertex DAG remainder and the global NO-SIX inequalities; if a SIX witness appears, it is retained as an exit rather than assumed away.
- The theorem deliberately treats the **two-fan inport** branch. It does not claim closure of the residual one-fan predecessor wedge, F2, the campaign's SIX branch, or larger remainders.
- No computation is used.
- No novelty claim is made.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

New proved step: the current four-remainder F3 obstruction cannot survive a neutral pivot based at an inport from its two-fan packed cycle; the pivot forces SIX, a genuine cross, or F2. The only F3 reverse-inport geometry left by this argument is a one-fan predecessor wedge with no inport from the two-fan cycle.

Full BT4 remains OPEN / NOT PROVED.
