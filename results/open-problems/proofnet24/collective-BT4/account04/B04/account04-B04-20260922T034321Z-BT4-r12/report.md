# BT4 account04/B04 — four-remainder freed-vertex degree profile forces a return cross

Run: `account04-B04-20260922T034321Z-BT4-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-FREED-PROFILE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven has four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem, so a directed digon counts.

The current source check remains Bessy–Muis–Sereni–Steiner–Wiederrecht, *A relaxation of the Bermond–Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its source statement leaves the exact conjecture open for `k>=4` and proves the `2k-1` threshold only for directed-or-one-reversal cycles. Nothing below counts a near-directed cycle.

## Complete peer state actually consumed

Controlling campaign-lead version:
- account02/B04 `BT4-R4-SATURATION-COLLAPSE-v1`, canonical report commit `14ef93ae71f52c019c679c29fca4624e510f7b95`, blob `17d49d472779d5304d30b93c07ce89c289ab20d1`;
- its controlling frontier addendum commit `6424f407ecb508fb5dcb4612a1d976441f34910c`, blob `28fe813aa044e57bbb3c6934a9ea76525bc04968`.

The frontier addendum is controlling: global no-cross is already obsolete. In a `NO-SIX` state, if `x` is a sink of the acyclic remainder, then there is a light source cycle `S`, heavy cycle `H`, other light cycle `U`, and a direct inport `p in S -> x` with fan pattern
`(m_H(x),m_S(x),m_U(x))=(3,2,2)`,
`H not->x`, and
`N+(x) intersect S={p+,p++}`.
The neutral source pivot

`S* = p -> x -> p++ -> S[p++,p]`

frees `q=p+` and changes the remainder to

`R*=(R-{x}) union {q}`.

The lead also proves that after this pivot there are three endpoint-distinct cross-packed transitions into the three heavy targets of `x`, all avoiding `x`.

Named OTHER-account partner used substantively:
- account01/B05 `BT4-TCEX-v1`, canonical report commit `c03ac5520b1b712814607a8d1c97301dd8c9948b`, blob `f61ce94c50464f2d59491377df32f7e549db7242`. In particular I use its source-bound corrected path-fan input: an `R`-internal path of edge length `L` from a packed cycle `T` to a remainder vertex `z` implies `|N+(z) intersect T| <= L+1`.
- account01/B05 `BT4-RCC-v1`, shared handoff blob `3deb56019df0fa573e1f73e661f8efa48a098e35`. Its `(4,1,1,1)` collision profile is identified exactly below; under RCC's additional all-long/mate hypotheses it already yields a neutral compression or an `R`-dominator fork.

Compatible same-frontier input:
- account02/B05 `BT4-RSC-v6-postpivot-wall`, shared blob `7c14eaf41ddd4761ee256eb82e7e2994fac4806a`, which identifies the freed vertex `q=p+`, proves that its only outneighbor on `S*` is `p++`, and separates its post-pivot remainder-outdegree into the SIX/five-witness/two-arm cases.

No peer outcome label is used as proof; only the source-bound statements above are imported.

## Compact conditional end-to-end route

Assume BT4 false and use the inherited oriented exact-outdegree-seven minimum counterexample with a globally minimum three-cycle packing and acyclic remainder. The shared reductions give either a SIX branch or a `NO-SIX` sink with the canonical source-to-sink-to-heavy cross. The lead's neutral source pivot replaces the single sink interface by three `x`-free heavy-entry crosses. The remaining `|R|=4` obstruction is to understand the freed vertex `q=p+` and splice one of these interfaces without reusing packed segments.

The theorem below gives an exact post-pivot degree split. After it, the four-remainder part of `SC+` has only:
1. a SIX exit;
2. an additional return cross avoiding `q`; or
3. one of two low-fan profiles, `(2,2,1,2)` or `(2,1,1,3)`, with a forced reverse inport.

Thus a complete target proof still requires the separate SIX closure, the larger-remainder branches, and a splice/strict-reduction argument for the two low-fan profiles. This report proves only the structural reduction.

## Lemma 1 — exact freed-vertex accounting

Specialize to the lead's `|R|=4` canonical sink state and perform the neutral source pivot. Put `q=p+` and

`e = d^+_{R*}(q)`.

Then:

1. `q` has exactly one outneighbor on `S*`, namely `p++`;
2. `0 <= e <= 3`; and
3. exact outdegree seven gives
   `d^+_{H union U}(q)=6-e`.

If `e=0`, then after deleting `H union U` the residual outdegree of `q` is exactly one, so `q` is a SIX witness in the new packing.

If the post-pivot state stays in `NO-SIX`, then `e in {1,2,3}`.

### Proof

The old packed cycle `S` is chordless. Since `q=p+`, its old cycle successor is `p++`; every other old-`S` outarc from `q` would be a chord. The new cycle `S*` contains `x`, but `x->q` is one of the source-fan arcs, so orientation forbids `q->x`. Hence `q` has exactly one outneighbor on `S*`, namely `p++`.

The new remainder has four vertices, one of them `q`, so at most three are outneighbors of `q`, giving `0<=e<=3`. Exact outdegree seven then leaves `7-1-e=6-e` outarcs from `q` into `H union U`.

For `e=0`, the residual graph after deleting `H union U` contains just the one `S*` outarc from `q`, so this is exactly the SIX alternative. QED.

## Lemma 2 — a heavy freed fan forces a q-avoiding return cross

Assume the post-pivot state remains in `NO-SIX`, so `e>=1`. Let `T` be either `H` or `U` and put

`m = |N+(q) intersect T|`.

If `m>=3`, then there is a genuine cross-packed transition from `T` to a packed cycle different from `T`, with every internal vertex in `R*`, and this transition avoids `q`.

### Proof

Because the inherited counterexample is 3-vertex-strong, directed set-to-vertex Menger gives three directed `T`-to-`q` paths that are pairwise internally vertex-disjoint, have distinct starts on `T`, and meet only at `q`. Trim each path to its last vertex on `T`.

If a trimmed path meets `S*` or the other member of `{H,U}` before it reaches `q`, take the subpath from its last `T` vertex to its first vertex on that different packed cycle. Its endpoints lie on different packed cycles, its internal vertices lie in `R*`, and `q` occurs later on the original path, so this is the required `q`-avoiding cross.

Suppose instead that all three trimmed paths have every internal vertex in `R*`. Let their edge lengths be `L_1,L_2,L_3`. The corrected path-fan inequality source-bound in account01/B05 gives

`L_i >= m-1`.

The three path interiors are pairwise disjoint; they lie in the four-vertex set `R*` and all paths end at `q`. Hence

`4 >= 1 + sum_i (L_i-1) >= 1 + 3(m-2)`.

If `m>=4`, the right side is at least seven, impossible. Therefore the only possible no-cross case has `m=3`, and equality must hold throughout. Thus every `L_i=2`, and the three one-vertex interiors are precisely `R*-{q}`. Write them `r_1,r_2,r_3`; then each has an arc `r_i->q`.

But `e>=1`, so `q` has an outarc to at least one of `r_1,r_2,r_3`. This creates an opposite pair `q<->r_i`, a digon, contradicting the oriented minimal-counterexample reduction. Hence the assumed no-cross case is impossible. QED.

### Why the last step matters

The corresponding saturation count without the freed-vertex outarc would merely produce three tight length-two channels. Here the neutral pivot itself supplies `e>=1`, so equality saturation contradicts orientation. This is what turns the count into an actual return-cross theorem rather than another neutral-orbit description.

## Theorem — exact four-remainder freed-profile split

In the lead's `|R|=4` canonical no-six sink state, after the neutral source pivot, at least one of the following occurs:

**F0 — SIX.** `e=0`, so the freed vertex `q` is a SIX witness.

**F1 — forced return cross.** A member `T in {H,U}` has at least three outneighbors from `q`, and Lemma 2 supplies a `q`-avoiding cross from `T` to a different packed cycle.

**F2 — balanced two-exit profile.**
`e=2`,
`d_H^+(q)=d_U^+(q)=2`,
and hence the exact profile relative to `(H,U,S*,R*)` is

`(2,2,1,2)`.

Let `r_0` be the unique vertex of `R*-{q}` not dominated by `q`. Then either

`r_0 -> q`

or there is a direct packed inport

`H union U -> q`.

**F3 — full remainder outstar with low packed fan.**
`e=3`, the two packed fan sizes are `{2,1}`, so the exact profile is

`(2,1,1,3)`

up to interchanging `H,U`. Moreover `q` dominates every vertex of `R*-{q}` and there is a direct packed inport

`H union U -> q`.

### Proof

By Lemma 1, `e` is in `{0,1,2,3}`.

If `e=0`, this is F0.

Assume `e>=1`. The total fan into `H union U` is `6-e`.

- If `e=1`, this total is five, so one of `H,U` receives at least three outarcs from `q`. Lemma 2 gives F1.
- If `e=2`, the total is four. Unless the split is exactly `2+2`, one member receives at least three, giving F1. Thus the only no-F1 state is the exact `(2,2,1,2)` profile in F2.
- If `e=3`, the total is three. Unless the split is `2+1`, one member receives all three, giving F1. Thus the only no-F1 state is the exact `(2,1,1,3)` profile in F3.

It remains to prove the reverse-inport statements.

Among vertices of `S*`, the only possible in-neighbors of `q=p+` are `p` and `x`: `p->q` is the old cycle edge, `x->q` is one of the two exact source-fan arcs, and chordlessness of old `S` excludes every other old-`S` vertex from sending to `q`.

For F3, `q` sends to all three other vertices of `R*`, so orientation excludes every one of them from sending back to `q`. Delete the two vertices `{p,x}`. The inherited 3-vertex-strongness makes `D-{p,x}` strongly connected. Any path to `q` in this deletion has a final predecessor. That predecessor lies neither in `R*` nor in `S*`, by the preceding exclusions, and therefore lies in `H union U`. This is the asserted packed inport.

For F2, `q` sends to exactly two of the three other remainder vertices. Let `r_0` be the unique omitted vertex. If `r_0->q`, we have the first alternative. Otherwise no vertex of `R*` can enter `q`: the two dominated vertices are excluded by orientation and `r_0` is excluded by assumption. Again delete `{p,x}` and use strong connectivity. The final predecessor of a path to `q` must lie in `H union U`, giving the second alternative. QED.

## Application of the named partner result

The `e=1` profile has total `H union U` fan five. If its split is `4+1`, then, relative to the new packing `(H,S*,U)`, the freed remainder vertex has exact packed/remainder profile

`(4,1,1,1)`

up to relabeling. This is exactly the collision profile in account01/B05 `BT4-RCC-v1`. Therefore, whenever RCC's additional all-long and shortest-cycle mate hypotheses hold, that subcase already has the partner's neutral compression to an `s<=2` remainder, or its one-one `R`-dominator fork. The new Lemma 2 is complementary: it does not require those mate hypotheses and proves that every `e=1` state, including `3+2`, already exports a `q`-avoiding return cross from a heavy target.

Thus the partner's rigid collision mechanism and the present Menger saturation argument meet on the exact same freed-vertex degree profile rather than describing unrelated branches.

## Sharpened shared case tree

For the four-remainder part of the campaign lead's `SC+` frontier, after the canonical neutral source pivot there are now only:

1. **SIX** at the freed vertex (`e=0`);
2. **RETURN-CROSS** (`F1`), to be paired with the lead's three endpoint-distinct `x`-free crosses into `H`;
3. **LOWFAN-2** (`F2`): exact `(2,2,1,2)`, with either one reverse remainder inport `r_0->q` or a packed inport from `H union U`;
4. **LOWFAN-3** (`F3`): exact `(2,1,1,3)`, complete remainder outstar from `q`, and a packed inport from `H union U`.

This strictly narrows the post-pivot `e>=2` branch in account02/B05 `BT4-RSC-v6-postpivot-wall`: a branch with a fan of size at least three cannot remain only a same-support two-arm wall; it must already expose a new cross. Only F2/F3 survive as no-new-heavy-cross states.

## First exact unpaid implication

`BT4-R4-LOWFAN-SPLICE-v1`:

> Starting from F2 or F3, combine the forced reverse inport at `q` with the lead's three `x`-free transitions into the heavy cycle and the two-arm post-pivot escape structure. Prove that one obtains a legal pair of replacement cycles, a strict globally-minimum packing reduction, a directed cycle in an exchanged remainder, or a SIX state.

For F3 the remainder geometry is especially rigid: `q` sends to all three other remainder vertices, so every return to `q` must enter from the packing after deletion of `{p,x}`. For F2 there is only one possible remainder-side reverse entry, `r_0`. These are the exact structural facts the next splice must use.

The SIX branch and the campaign's larger-remainder branches remain separate. This report does not claim a full BT4 proof.

## Failure checks and scope

- `NO-SIX` is **not** assumed to survive the neutral pivot. The new `e=0` state is explicitly retained as a SIX exit.
- Lemma 2 requires `e>=1`; its final digon contradiction would be invalid at `e=0`.
- The three Menger paths are used only after trimming to their last `T` vertices. A visit to another packed cycle is converted immediately into the desired cross rather than silently treated as an `R`-internal path.
- The path-fan inequality is used with its source hypothesis: internal vertices in the current remainder and a minimum-total packing.
- The reverse-inport argument uses deletion of exactly two vertices `{p,x}`, which is permitted by inherited 3-vertex-strongness. It does not assume arbitrary indegree lower bounds.
- A cross-packed transition is not promoted to a fourth cycle or to two replacement cycles. The splice is still unpaid.
- No computation was used in this derivation.
- No target-level novelty or proof completion is claimed.

## Outcome

`ESSENTIAL_STEP_APPLIED`.

The current `|R|=4` post-pivot obstruction is reduced from a generic freed-vertex/two-arm state to a four-way exact split, and the no-new-cross residual consists only of two explicit low-fan degree profiles with forced reverse inports. The next decisive work is the `BT4-R4-LOWFAN-SPLICE-v1` splice, while the SIX and larger-remainder branches remain live.
