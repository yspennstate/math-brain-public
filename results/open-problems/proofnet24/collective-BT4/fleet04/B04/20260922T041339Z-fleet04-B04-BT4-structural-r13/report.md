# BT4 fleet04/B04 — packed-inport collar and anchored low-fan routing split

Run: `20260922T041339Z-fleet04-B04-BT4-structural-r13`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-LOWFAN-PORT-SPLIT-v2`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Directed digons count in the source problem.

Fresh bounded literature check on 22 September 2026 recovered Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), whose abstract explicitly states that the genuine conjecture remains unresolved for all `k>=4` and proves only the one-reversed-arc relaxation. No search miss is used as a novelty certificate.

## Exact inherited state consumed

Controlling campaign-lead package:

- fleet02/B04 `BT4-R4-SATURATION-COLLAPSE-v1`, run `20260922T031823Z-a02-b04-bt4-r11`, primary report blob `17d49d472779d5304d30b93c07ce89c289ab20d1`;
- its controlling frontier addendum blob `28fe813aa044e57bbb3c6934a9ea76525bc04968`.

The addendum is controlling. In a canonical persistent `NO-SIX` state, a sink `x` of the acyclic remainder has a light source cycle `S`, heavy cycle `H`, other light cycle `U`, a direct source inport `p in S -> x`, fan pattern

`(m_H(x),m_S(x),m_U(x))=(3,2,2)`,

`H not->x`, and exact source targets

`N+(x) intersect S={p+,p++}`.

The neutral source pivot

`S* = p -> x -> p++ -> S[p++,p]`

frees `q=p+` and gives

`R*=(R-{x}) union {q}`.

The lead also supplies three endpoint-distinct `x`-free cross-packed transitions ending at the three heavy targets of `x`.

Immediate same-slot predecessor actually used:

- fleet04/B04 `BT4-R4-FREED-PROFILE-v1`, report blob `eae9c01b562dd2c417724aa0822117223026d796`.

For `|R|=4`, writing `e=d^+_{R*}(q)`, that report proved the post-pivot split: `e=0` is a SIX exit; any fan of size at least three from `q` into `H` or `U` produces a `q`-avoiding return cross; and absent those outputs only the following low-fan profiles remain:

- **F2:** `e=2`, profile `(H,U,S*,R*)=(2,2,1,2)`. If `r0` is the unique vertex of `R*-{q}` not dominated by `q`, then `r0->q` or `H union U -> q`.
- **F3:** `e=3`, profile `(2,1,1,3)` up to swapping `H,U`. The vertex `q` dominates all three vertices of `R*-{q}` and `H union U -> q`.

Named OTHER-account partner result used substantively:

- fleet01/B05 `BT4-G1-DOUBLE-SINK-SPLICE-v1`, run `20260922T032838Z-b05-bt4-r11`, report blob `706c6cfa4f837209234ff5196dd8df9171e90bab`.

Its exact inputs used below are: for a support five-witness `z` on a chordless support cycle `B`, with unique remainder exit `e`, if the fixed-pair residual has remainder outdegree at least three, then every shortest exit-to-remainder-sink path of length `L` ending at `s` has terminal fan `T_s=N+(s) intersect B` of size `k>=3` with `L>=k-2`; in the short regime `T_s` lies in the first `L+2` strict successors of `z`. For two support witnesses, vertex-disjoint exit-to-sink paths plus two terminal support segments that are vertex-disjoint give two disjoint replacement cycles and therefore four cycles with the untouched packed pair.

No peer outcome label is treated as proof; only the source-bound statements above are imported.

## Compact conditional end-to-end location

Assume BT4 false and work in the inherited oriented exact-outdegree-seven, 3-vertex-strong, arc-dominated minimum counterexample with a globally minimum-total packing of three chordless directed cycles and acyclic remainder.

The lead reduces a persistent no-six sink to the `(3,2,2)` source-pivot state. The preceding fleet04/B04 run reduces the four-remainder post-pivot obstruction to SIX, a return cross, or F2/F3. This run attacks exactly F2/F3.

The first new mechanism is a general minimum-packing collar for any direct packed inport to a remainder vertex. It converts almost every F2/F3 packed return into a second neutral pivot on `H` or `U`. The only no-second-pivot exceptions are then an exact remainder-only F2 return and an exact single-port F3 return. In the F3 exception, the partner's double-sink splice further reduces the no-R-five support branch to coalescence, a unique remainder sink, or an exact three-successor terminal-fan corridor.

The remaining SIX and larger-remainder branches are not claimed closed.

## Lemma 1 — packed-inport two-step collar

Let `(A,B,C)` be any globally minimum-total three-cycle packing in the inherited oriented counterexample, let `R` be its acyclic remainder, let `q in R`, and let `T` be one of the packed directed cycles. Suppose

`c in T -> q`

is a direct packed inport. Then every `y in N+(q) intersect T` satisfies

`d_T(c,y) <= 2`,

where `d_T(c,y)` is the forward distance on the directed cycle `T`. Consequently

`N+(q) intersect T subset {c+,c++}`.

If the fan has size two, it is exactly `{c+,c++}`. Whenever `q->c++`, the cycle

`T_q = c -> q -> c++ -> T[c++,c]`

has exactly `|T|` vertices and is a legal size-neutral globally minimum exchange. Its exchanged remainder is `(R-{q}) union {c+}` and must be acyclic in a counterexample, since otherwise the exchanged remainder cycle together with `T_q` and the two untouched packed cycles would already give four disjoint directed cycles.

### Proof

Fix `y in N+(q) intersect T`. Since `D` is oriented and `c->q`, we cannot have `y=c`. Put `n=|T|` and `a=d_T(c,y)`, so `1<=a<=n-1`.

The arcs `c->q` and `q->y`, followed by the forward segment `T[y,c]`, form a directed cycle `K_y` disjoint from the other two packed cycles. It has

`|K_y| = 2 + d_T(y,c) = 2 + n-a`

vertices. Replacing `T` by `K_y` gives another three-cycle packing, so global minimum of the original total packing size forces

`n <= |K_y| = n-a+2`.

Hence `a<=2`. This proves the collar. If there are two distinct targets they must be `c+` and `c++`. For `y=c++`, the displayed count is equality, so the exchange is size-neutral. If its new remainder contained a directed cycle, the two untouched packed cycles, `T_q`, and that remainder cycle would form four disjoint cycles; therefore the exchanged remainder is acyclic in a counterexample. QED.

### Exact significance

A direct packed return into the freed vertex cannot land at an arbitrary port relative to its outgoing fan. It is locked to a two-successor window. A two-fan direct return is automatically an equality pivot on that packed cycle.

## Corollary 2 — F2 has only a second pivot or a pure remainder return

In F2, `q` has exactly two outneighbors on each of `H` and `U`. Therefore exactly one of the following useful states occurs:

- **F2-PIVOT:** some vertex of `H union U` sends directly to `q`; on the corresponding cycle `T`, Lemma 1 forces the two targets of `q` to be `{c+,c++}`, and `T` admits the neutral pivot `c->q->c++->T[c++,c]`;
- **F2-RONLY:** there is no direct inport `H union U -> q`. Then the preceding F2 reverse-inport dichotomy forces `r0->q`, where `r0` is the unique remainder vertex not dominated by `q`.

Thus, if one excludes a second packed neutral pivot, F2 is not an arbitrary reverse-interface branch: its only available non-source reverse entry is the distinguished remainder arc `r0->q`, while `q` sends to the other two vertices of `R*-{q}`.

### Proof

If an inport `c in T ->q` exists with `T in {H,U}`, the fan of `q` into `T` has size two, so Lemma 1 gives F2-PIVOT. If no such inport exists, the earlier F2 theorem leaves only `r0->q`. QED.

## Corollary 3 — F3 has only a second pivot or one exact single packed port

Relabel F3 so that

`|N+(q) intersect H|=2`,
`|N+(q) intersect U|=1`.

Write `N+(q) intersect U={y}`. Recall that some direct inport from `H union U` to `q` is forced.

Then either a size-neutral pivot exists on `H` or `U`, or the following exact obstruction holds:

**F3-SINGLEPORT:**

1. `H not-> q`;
2. `N^-(q) intersect (H union U)={y^-}`;
3. the unique packed inport is `y^- -> q`, while the unique `U`-target is `q->y`;
4. `q` still dominates every vertex of `R*-{q}`.

### Proof

If any `c in H` sends to `q`, the H-fan has size two and Lemma 1 gives a neutral pivot immediately.

So suppose no H-inport exists. At least one U-inport `c->q` exists. Since the U-fan is the singleton `{y}`, Lemma 1 says `y` is either `c+` or `c++`. If `y=c++`, Lemma 1 again gives a neutral pivot. Therefore, if no second pivot exists, every U-inport must satisfy `y=c+`, hence `c=y^-`. There is only one such vertex. This proves items 1--3; item 4 is the inherited F3 profile. QED.

### Exact significance

The formerly generic F3 packed reverse entry is reduced to one directed two-edge interface on the one-fan cycle:

`y^- -> q -> y`,

with no heavy-cycle inport at all. Any second predecessor port, any inport from the two-fan cycle, or any distance-two inport already yields another neutral minimum-packing exchange.

## Lemma 4 — partner-anchored routing split inside F3-SINGLEPORT

Assume the post-pivot packing remains globally `NO-SIX`, is in F3-SINGLEPORT, and for the fixed pair `{H,U}` there is no five-witness in `R*`.

Then there are at least three cycle-supported five-witnesses on `S*`; one is `x`. Every such witness has exactly its support successor plus one unique remainder exit. Let `z!=x` be any other support witness, and let `e_z in R*` be its unique remainder exit. Since the fixed-pair remainder vertices have residual outdegree at least three, fleet01/B05 `BT4-G1-DOUBLE-SINK-SPLICE-v1` applies.

At least one of the following occurs:

- **C0 — q-coalescence:** `e_z=q`;
- **C1 — unique-sink bottleneck:** `R*` has a unique sink;
- **C2 — anchored double-sink corridor:** there are two distinct sinks `s_x,s_z` with the one-edge vertex-disjoint routes

  `q -> s_x`,
  `e_z -> s_z`,

  and, unless the partner splice already gives four disjoint cycles, each sink has exactly three outneighbors on `S*`. If `|S*|>=4`, these are exactly the first three strict successors of the corresponding witness:

  `N+(s_x) intersect S* = {x+,x++,x+++}`,

  `N+(s_z) intersect S* = {z+,z++,z+++}`,

  and the partner's all-crossing corridor holds:

  `{x+,x++,x+++} subset (x,z]_{S*}`

  or

  `{z+,z++,z+++} subset (z,x]_{S*}`.

  If `|S*|=3`, C2 itself closes BT4 by the partner double-sink splice, so no counterexample reaches a three-vertex support cycle in C2.

### Proof

Post-pivot global NO-SIX gives at least three exact five-witnesses for the deleted pair `{H,U}`. By hypothesis none lies in `R*`, so they lie on `S*`. Chordlessness of `S*` means a support five-witness has only its cycle successor as an `S*` outneighbor; residual degree two therefore leaves a unique `R*` exit. The vertex `x` is one such witness and its unique exit is `q`.

No R-supported five-witness plus NO-SIX means every vertex of `R*` has residual outdegree at least three in `D-(H union U)`. This is exactly the fixed-pair hypothesis used by the fleet01/B05 sink-fan collar.

Take `z!=x`. If `e_z=q`, C0 holds. Assume `e_z!=q`. If `R*` has a unique sink, C1 holds. Otherwise choose a sink `s_z` reachable from `e_z`, and choose another sink `s_x!=s_z`.

F3 gives `q->r` for every `r in R*-{q}`, hence in particular `q->s_x`; this is a one-edge route. The partner collar implies `e_z` itself is not a sink. Also `q->e_z`, so acyclicity of `R*` forbids any directed path from `e_z` back to `q`. A path from `e_z` ending at `s_z` cannot pass through the distinct sink `s_x`. Thus a shortest `e_z`-to-`s_z` path is vertex-disjoint from `q->s_x`.

Because `|R*|=4`, the four distinct vertices `q,s_x,e_z,s_z` exhaust `R*`; there is no room for an internal vertex on the second path. Hence `e_z->s_z` is also one edge.

Apply the partner sink-fan collar to these two support witnesses. Their path lengths are `L_x=L_z=1`. The terminal sink fans have sizes `k_x,k_z>=3`, while `L>=k-2` gives `k_x,k_z<=3`; hence both are exactly three. If `|S*|>=4`, the partner short-window conclusion puts each 3-element fan into the first three strict successors of its witness, so equality of sets follows. The partner double-sink lemma says that disjoint choices of terminal support segments would give four cycles. Therefore all choices cross, and its interval argument yields the displayed corridor.

If `|S*|=3`, each terminal fan is all of `S*`. Choose `b_x=x` and `b_z=z`; the two support segments are the disjoint singletons `{x}` and `{z}`. The two remainder routes are disjoint, so the partner lemma yields four cycles, contradiction. Thus C2 cannot survive with `|S*|=3`. QED.

## The new structural theorem

> **BT4-R4-LOWFAN-PORT-SPLIT-v2.** In the inherited four-remainder canonical sink state, after the neutral source pivot and after excluding an immediate SIX or the already-proved fan-at-least-three return-cross output, every F2/F3 low-fan state has one of the following:
>
> 1. a second size-neutral globally minimum pivot on `H` or `U`;
> 2. F2-RONLY: no `H/U` inport and the unique undominated remainder vertex satisfies `r0->q`;
> 3. F3-SINGLEPORT: after labels, `q` has H/U fans `(2,1)`, no H-inport, and the only H/U inport is `y^- -> q -> y` on the one-fan cycle;
> 4. a post-pivot SIX state elsewhere.
>
> In branch 3, if the fixed pair `{H,U}` has an R-supported five-witness, that is an explicit separate `R5` output. Otherwise the support side further splits by Lemma 4 into q-coalescence, a unique R-sink, or the exact partner-anchored three-successor corridor; the three-vertex support case of the last alternative already yields four cycles.

This is a strict structural narrowing of `BT4-R4-LOWFAN-SPLICE-v1`. The generic phrase "forced reverse inport" is replaced by either an actionable equality pivot or one of two explicit exceptional port geometries.

## First exact unpaid implication after this run

The first local implication is now:

`BT4-R4-EXCEPTIONAL-PORT-CLOSURE-v1`:

> Close F2-RONLY and F3-SINGLEPORT. In F3-SINGLEPORT, if there is no R-five witness, it is enough to close the q-coalesced branch, the unique-sink branch, and the exact three-successor corridor of Lemma 4. Any closure must produce a legal two-cycle replacement, a strict decrease of the globally minimum three-packing, a directed cycle in an exchanged remainder, a SIX/lower-k exit, or four vertex-disjoint directed cycles.

A promising next mechanism is to combine the lead's three endpoint-distinct `x`-free heavy-entry transitions with the newly rigid reverse ports. In F3-SINGLEPORT there is only one direct H/U return port into `q`, on the one-fan cycle, while the support-corridor branch supplies two one-edge remainder routes and exact consecutive three-fans. In F2-RONLY the only non-source reverse entry is `r0->q`, with `q` pointing to the other two remainder vertices. These are now finite port-ordering problems rather than arbitrary linkage states.

The campaign still separately owes the SIX closure and larger-remainder branches. No full BT4 proof is claimed.

## Failure checks and nonclaims

- A neutral exchange is not a strict contradiction; it is an equality move and may belong to a finite orbit.
- The collar uses global minimum total packing size, not minimum individual cycle length.
- The new cycle `c->q->y->T[y,c]` is counted with `q` once and with the forward T-segment from `y` to `c`; the count is `n-d_T(c,y)+2`.
- F2-RONLY means no inport from `H union U`; the known inverse source-pivot ports from `S*` are not being denied.
- F3-SINGLEPORT classifies direct inports from `H union U`, not arbitrary longer paths to `q`.
- Lemma 4 is used only when the post-pivot state is globally NO-SIX and the fixed pair has no R-supported five-witness. Otherwise the SIX/R5 outputs are retained instead of silently discarded.
- The fleet01/B05 double-sink lemma is applied only after proving vertex-disjoint sink routes. Coalesced exits and a unique sink are preserved as separate branches.
- No tournament restriction is used.
- No computation was used in the proof above.
- No full proof and no novelty claim are made.

## Status

`ESSENTIAL_STEP_APPLIED`.

Before: the four-remainder post-pivot frontier had two low-fan profiles with a generic reverse-inport obligation.

After: every H/U direct reverse inport is trapped in a two-successor collar. F2 either pivots again or has only the distinguished remainder return `r0->q`; F3 either pivots again or has exactly one direct H/U inport, the immediate predecessor-to-q-to-target interface on its one-fan cycle. In the latter branch, the latest assigned partner's double-sink theorem further collapses the no-R-five support geometry to coalescence, a unique sink, or an exact consecutive three-fan corridor, with the support triangle case closed.

BT4 remains OPEN / NOT PROVED.
