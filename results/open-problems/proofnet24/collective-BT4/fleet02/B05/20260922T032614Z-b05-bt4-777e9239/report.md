# BT4 fleet02/B05 — post-pivot freed-vertex wall

Run: `20260922T032614Z-b05-bt4-777e9239`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-RSC-v6-postpivot-wall`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and controls

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs, and therefore digons, are allowed in the source problem. The oriented exact-outdegree-seven model below is only the inherited minimum-counterexample normal form after the digon case has been discharged by the genuine `k=3` theorem.

Fresh owner controls were read from `yspennstate/math-research-brain` at main commit `1dcdc20b0f33a2a7a0b70422476e3f421708c448`, and checked again before the scientific write at main `e1fd1840929786f75b7b29d418e47ec265418483`. The control README remained Git blob `3d4a9372c87802ab734141a3374d04c8823372e3`, revision `2026-09-22.2`, with `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` active and no stop for fleet02/B05. Exact whole-file/OWNER-message SHA-256 values are `UNVERIFIED_CURRENT_RUN`; immutable Git identities are recorded rather than inventing a byte hash not independently materialized here.

Control/source blobs used this run:

- `AGENTS.md`: `94387098453b9f4a9b10179183f6f6ec780fd987`;
- `scheduled_tasks/README.md`: `3d4a9372c87802ab734141a3374d04c8823372e3`;
- `scheduled_tasks/fleet.json`: `e647d5d2479749f80ce7bb4862bee0f28513c7d9`;
- `scheduled_tasks/roles.json`: `ed17ecc94f76720c0345b3e32249b791b20ec611`;
- `scheduled_tasks/PROTOCOL.md`: `83a9268bf5287ca203e4be69a79e25382397bca7`;
- collective `ORDER.md`: `a70e03208ae00795ca7c6cdf9b7dbce854347138`;
- `TARGETS.md`: `a8cafa98cdb074ed15d0e214f8f54ee514c500df`.

The owner reallocation supersedes the older brain-installation and benchmark work. No new installation or benchmark work was performed.

## Exact research state consumed

Campaign lead, newest complete canonical version available at the start of the run:

- fleet02/B04, `20260922T022208Z-b04-bt4-r11`, primary report blob `930c6906cc2532269bc35e0d0b0ea8e246eb250b`;
- controlling correction blob `117d9760b66cfb5930c79ade79d2b449ce329b9b`.

The correction is controlling wherever it narrows the primary report. In particular, no marked-segment tax is invoked without its heavy-cycle inport hypothesis.

Named OTHER-account partner result actually applied:

- fleet03/B06 `BT4-G1-PORT-SPACING-v1`, run `20260922T024819Z-fleet03-B06-bt4`, report blob `aa204668c14943833c8082fd1f1702af715f2de4`.

The exact partner inputs used here are its canonical G1 neutral pivot and its full-digraph sharpness certificate: old light cycle `B=(4,5,6,7)`, sink `x=19`, neutral pivot `B*=(4,19,6,7)`, and the fact that the freed vertex `5` belongs to a post-pivot remainder containing the directed triangle `(5,13,17)`. The partner correctly labels that certificate as a local G1-S realization, not a BT4 counterexample.

Two further compatible OTHER-account results are used in proved scope:

- fleet01/B04 `BT4-MCR-v5-sink-cross-collapse`, report blob `bbf3afa52d8d0587ae5e210eecaacb7017ac672e`: every remainder sink has a direct packed inport, its source-cycle fan is at most two, and a source fan of two is the neutral equality case;
- fleet04/B04 `BT4-G1-PREDECESSOR-FORK-v1`, canonical report blob `fad0a38910cb6551a3b16af5871bff4fb2b785d7`, consumed from the fresh shared handoff. It localizes the current same-heavy G1-S obstruction to predecessor/port collision plus exit-return behavior. No peer outcome label is used as a theorem.

I also retain my preceding corrected B05 result `BT4-RSC-v5-two-support-lift`, primary report blob `9727b3f919f8c071dd12a6e9c4baf0b631424b08` and controlling correction blob `ab145f55b225f7cbf6b807546ba240112d246786`.

## Inherited normal form

Assume for contradiction a minimum BT4 counterexample in the inherited normal form. Thus `D` is oriented and every vertex has outdegree exactly seven; `(S,T,U)` is a globally minimum-total packing of three directed cycles; the remainder

`R = V(D) \ (V(S) union V(T) union V(U))`

is nonempty and acyclic; the packed cycles are chordless; every arc is dominated; and `D` is 3-vertex-strong.

Choose a sink `x` of `D[R]`. By fleet01/B04 there is a direct packed inport

`p -> x`, `p in S`,

and the source fan satisfies

`m_S(x) = |N+(x) intersect S| <= 2`.

If `m_S(x)<=1`, then at least six of the seven arcs leaving `x` hit the complementary pair `T union U`, so this is already a SIX object. The neutral equality branch is therefore exactly `m_S(x)=2`.

The purpose of this run is to analyze that equality branch by a mechanism different from the previous domination ladders: use global minimum of the packing to rigidify the two source-cycle targets, then use acyclicity of the exchanged remainder as a wall against the freed vertex.

## Lemma 1 — exact source targets in a neutral sink pivot

Assume `m_S(x)=2`. Write `p^+` and `p^{++}` for the first and second successors of `p` on the directed cycle `S`. Then

`N+(x) intersect S = {p^+, p^{++}}`.

### Proof

Let `a in N+(x) intersect S`, and let

`d = d_S(p,a)`

be the forward distance from `p` to `a` along `S`. The arcs `p->x` and `x->a`, followed by the forward segment `S[a,p]`, form a genuine directed cycle

`K_a = p -> x -> a -> S[a,p]`.

It is disjoint from `T` and `U`, so `(K_a,T,U)` is another three-cycle packing. If `n=|S|`, then

`|K_a| = n + 2 - d`.

Global minimum of `(S,T,U)` therefore gives

`n+2-d >= n`, hence `d<=2`.

Orientation rules out `a=p`, because `p->x` and `x->p` would form a digon. Thus every source-cycle target of `x` lies at forward distance one or two from `p`. Since there are exactly two distinct targets, they are `p^+` and `p^{++}`. QED.

This is stronger than the generic path-fan equality statement at this one-edge inport: the actual two target vertices are determined.

## Lemma 2 — the neutral pivot frees a vertex with exactly one source-cycle outneighbor

Put

`q = p^+`.

By Lemma 1 the cycle

`S' = p -> x -> p^{++} -> S[p^{++},p]`

has exactly `|S|` vertices. Therefore `(S',T,U)` is another globally minimum three-cycle packing. Its new remainder is

`R' = (R \ {x}) union {q}`.

Because `D` is a counterexample, `D[R']` is acyclic: a directed cycle in `R'` together with `S',T,U` would be a forbidden four-packing.

Moreover

`|N+(q) intersect S'| = 1`,

and the unique such outneighbor is `p^{++}`.

### Proof

The equality `|S'|=|S|` follows directly from replacing the two-edge old segment `p->q->p^{++}` by `p->x->p^{++}`. If `R'` contained a directed cycle, it would be vertex-disjoint from all three packed cycles, giving four genuine directed cycles.

For the outneighbor claim, chordlessness of the old packed cycle `S` says that `q` has no old `S`-outneighbor except its successor `p^{++}`. The only new vertex of `S'` is `x`; but `x->q` holds by Lemma 1, so orientation forbids `q->x`. Hence `p^{++}` is the unique `S'`-outneighbor of `q`. QED.

Thus a neutral equality move does not release an arbitrary old cycle vertex. It releases a vertex whose exact-seven budget has only one arc left on its former support cycle.

## Lemma 3 — post-pivot acyclicity wall for every freed-vertex exit

Assume `q` has an outneighbor

`r in R'\{q}`.

Then at least one of the following occurs in the new minimum packing `(S',T,U)`:

1. there is a genuine cross-packed directed path from `S'` to `T` or `U` whose internal vertices lie in `R'`;
2. there is an `R'`-internal same-support bypass from `p` to a distinct vertex `a in S'`, with global-minimum length tax
   `ell >= d_{S'}(p,a)`;
   equality is a size-neutral one-cycle exchange with acyclic exchanged remainder.

### Proof

Because `D` is 3-vertex-strong, deleting `p` and `x` leaves a strongly connected digraph. Hence there is a directed path `Q` from `r` to `q` in `D-{p,x}`; take `Q` simple.

The path `Q` cannot be contained in `R'`. Otherwise

`q -> r + Q[r,q]`

would be a directed cycle in `D[R']`, contradicting Lemma 2. Let `a` be the first packed vertex of the new packing encountered along `Q` when traversing from `r` toward `q`. Since `p,x` were deleted, `a` is neither of those vertices. The prefix `Q[r,a]` has every internal vertex in `R'`.

Now concatenate

`P = p -> q -> r -> Q[r,a]`.

All internal vertices of `P` lie in `R'`.

If `a in T union U`, `P` is a genuine cross-packed transition from `S'` to a different packed cycle, giving case 1.

If `a in S'`, then `a!=p,x` and `P` is a same-support bypass from `p` to `a`. Write `ell=|E(P)|` and `d=d_{S'}(p,a)`. Replacing the forward segment `S'[p,a]` by `P` gives a directed replacement cycle of order

`|S'| + ell - d`.

If `ell<d`, keeping `T,U` would produce a smaller three-cycle packing, contradicting global minimum. Hence `ell>=d`. At equality the replacement is another globally minimum three-packing, and its remainder is acyclic for the same four-cycle reason as in Lemma 2. QED.

This is the key post-pivot wall: any attempted return from a freed-vertex remainder exit must hit the packing before it can close in the acyclic remainder.

## Lemma 4 — exact degree dichotomy at the freed vertex

Let

`e = d^+_{D[R']}(q)`.

Then:

- if `e=0`, `q` is a six-cross witness for the complementary packed pair `T union U`;
- if `e=1`, `q` is a five-cross witness for `T union U`, and its unique remainder exit simultaneously triggers Lemma 3;
- if `e>=2`, the new state has at least the Lemma-3 cross/support output, and the exits can be chosen to expose a two-arm version of the wall as described below.

### Proof

Lemma 2 gives exactly one outneighbor of `q` on `S'`. Since `d_D^+(q)=7`, the number of arcs from `q` into `T union U` is

`7 - 1 - e = 6-e`.

Delete `T union U`. The residual outdegree of `q` is exactly `1+e`. Thus:

- for `e=0`, the residual degree is one and six arcs hit `T union U`;
- for `e=1`, the residual degree is two and five arcs hit `T union U`.

These are exactly the six-cross and five-cross pair-deletion deficit types used throughout the inherited proof. For every `e>=1`, choose a remainder exit and apply Lemma 3. QED.

So the source-fan-two neutral pivot immediately regenerates a named pair-deletion obstruction at the freed vertex unless the freed vertex has at least two remainder exits.

## Lemma 5 — two exits give a two-arm packed escape

Assume `e>=2`, and choose distinct `R'`-outneighbors `r1,r2` of `q`. Then, after deleting `x`, there are internally vertex-disjoint directed paths

`Q_i : r_i -> ... -> q`,  `i=1,2`,

sharing only their terminal vertex `q`. Each `Q_i` meets the new packing before reaching `q`. Taking the first packed vertex `a_i` on `Q_i` yields two internally vertex-disjoint prefixes from `r_i` to distinct packed vertices `a_i`. Consequently either at least one arm reaches `T union U`, giving a genuine cross transition, or both arms return to `S'` and produce a two-arm same-support escape with distinct packed return vertices except that at most one arm may return to `p`.

### Proof

Original 3-vertex-strongness implies `D-x` is 2-vertex-strong. Apply directed Menger in the reverse digraph of `D-x` from `q` to the two-element set `{r1,r2}` (equivalently, add a super-source adjacent to `r1,r2`). There are two internally vertex-disjoint paths with distinct starts `r1,r2` and common terminal `q` in the original orientation.

Neither `Q_i` can lie wholly in `R'`, because `q->r_i` followed by `Q_i` would make a directed cycle in the acyclic `D[R']`. Hence each meets the new packing. Since the two paths are internally vertex-disjoint, their first packed vertices are distinct unless one is the common terminal, but `q` is not packed. Thus `a1!=a2`.

If some `a_i` lies on `T` or `U`, prepend `p->q->r_i` to its prefix to get a genuine cross-packed transition. Otherwise both first packed hits lie on `S'`; the two prefixes have disjoint interiors and distinct return vertices. Because the Menger paths were constructed in `D-x`, neither return is `x`; both may use `p` only if they shared it, which internal disjointness forbids. Therefore at most one arm returns to `p`. QED.

This is a stronger object than the single unstructured cross/bypass that survived earlier runs: after the neutral sink pivot, the only non-deficit branch has two simultaneously exposed, internally disjoint escape arms from the freed vertex.

## Exact application to the named partner certificate

Fleet03/B06's `BT4-G1-PORT-SPACING-v1` certificate has

`B=(4,5,6,7)`, `x=19`, `p=4`, `B*=(4,19,6,7)`.

Lemma 1 predicts exactly the observed neutral replacement: `q=p^+=5` is freed and `p^{++}=6` remains on the pivoted cycle. The partner reports that the new remainder contains the directed triangle

`(5,13,17)`.

That triangle is precisely the configuration forbidden by Lemma 2 in a genuine counterexample: it is a post-pivot return from the freed vertex that closes entirely inside the exchanged remainder. Therefore the partner certificate is not merely known to have a fourth cycle; this run identifies the exact wall that a true counterexample must satisfy and explains why the certificate fails it.

This is a substantive use of the named OTHER-account result. The partner's port-spacing corridor remains compatible but is now accompanied by an independent freed-vertex constraint after the neutral pivot.

## Interaction with the newest predecessor-cycle fork

Fleet04/B04's `BT4-G1-PREDECESSOR-FORK-v1` localizes the same-heavy support-witness branch to predecessor-cycle/inport collisions and exit-return collars. The post-pivot wall acts on a different vertex: the old light-cycle successor `q` that is expelled into the remainder by the neutral sink exchange.

Hence these mechanisms are complementary. After a neutral source-fan-two sink pivot, one cannot have an arbitrary G1-S continuation:

- `e=0`: the freed vertex is immediately a SIX object;
- `e=1`: the freed vertex is itself an R-supported five-witness and also exports a cross/support wall path;
- `e>=2`: it exports two internally disjoint escape arms, unless a cross transition already occurs.

The predecessor-cycle fork constrains the support witnesses retained on the pivoted cycle; the new wall constrains the unique vertex removed from that cycle. A genuine obstruction must satisfy both systems simultaneously.

## Compact conditional end-to-end argument

A full BT4 proof follows from the inherited normal-form reductions plus closure of the remaining localized splice interfaces:

1. Start with the oriented exact-seven, globally minimum three-packing normal form.
2. Choose a remainder sink. Fleet01/B04 gives a direct packed inport `p->x` and a canonical length-two cross.
3. If the source fan is at most one, `x` already yields a SIX object.
4. If the source fan is two, Lemma 1 fixes its targets to `p^+,p^{++}` and Lemma 2 performs the genuine directed neutral pivot.
5. The freed vertex `q=p^+` then satisfies Lemma 4. Zero exits gives SIX; one exit gives an R-supported five-witness plus the wall path; at least two exits gives the two-arm packed escape of Lemma 5 or an immediate cross.
6. Existing R-supported witness collars handle the one-exit object up to their already explicit cross/equality/strict-collar output. Fleet03/B06 and fleet04/B04 constrain the simultaneous support-witness port geometry on the pivoted cycle.

Thus neutral equality is no longer a featureless orbit step. Its only genuinely new residual branch is a two-or-more-exit freed vertex whose Menger escape arms both return to the source cycle without producing an equality exchange or cross transition.

## First essential missing implication

The next exact implication is now:

> **`BT4-POSTPIVOT-TWOARM-CLOSURE-v1`.** In the inherited exact-seven globally minimum normal form, after a source-fan-two sink pivot, let `q=p^+` be the freed vertex. Assume `d^+_{R'}(q)>=2`, no wall arm reaches `T union U`, and every same-support return supplied by Lemmas 3 and 5 is strict rather than a neutral equality exchange. Prove that the two internally disjoint return arms, together with the canonical sink-cross / support-witness port structure, force a strict smaller three-packing, a directed cycle in an exchanged remainder, a SIX object, or two vertex-disjoint replacement directed cycles.

This is strictly narrower than the prior generic cross/coalescence blocker: both arms start at one explicitly identified freed vertex, are internally disjoint up to the packing, the new remainder is acyclic, and the source-cycle neighborhood of that vertex is exactly one vertex.

## Failure checks and nonclaims

- A single cross-packed transition is not counted as a two-cycle replacement or a four-packing.
- A strict same-support bypass is not itself a contradiction.
- Lemma 5 uses directed Menger only after deleting `x`, where 3-vertex-strongness genuinely leaves a 2-vertex-strong digraph. It does not claim two disjoint paths after deleting both `p` and `x`.
- The two Menger arms may coalesce only at `q`; their packed first-hit vertices are distinct. This does not yet make the two replacement cycles vertex-disjoint because both candidate cycles can still use `p,q`.
- The partner's 20-vertex certificate is not a BT4 counterexample and is not used as one.
- No near-directed cycle from the 2026 relaxation is promoted to a genuine directed cycle.
- No edge-disjoint substitute, higher degree threshold, restricted graph order, or finite-search closure is used.
- No computation was used in this run.
- Full BT4 remains open.

## Before / after / honest status

Before: B05 had repeatedly produced domination-based cross-existence and small-remainder reductions, but the live obstacle was still described broadly as cross/linkage coalescence after neutral exchanges.

After: the source-fan-two neutral sink exchange has an exact local normal form. The two source targets are forced to be the first two successors of the inport; the freed successor has exactly one source-cycle outneighbor; every freed-vertex remainder exit is blocked from returning wholly through the new acyclic remainder and must hit the packing; zero/one/two-plus exits split respectively into SIX, R-five-plus-wall, and a two-arm packed escape. This changes the mechanism from domination descent to global-minimum rigidity plus post-exchange acyclicity and directed Menger.

Outcome: `ESSENTIAL_STEP_APPLIED`.

## Operational notes

Fleet02's exposed managed inventory was inspected once. The current managed set contains all twenty account slots enabled on hourly cadences, B05 is role-aligned with BT4, and no deficit requiring B20 action was observed. No scheduler mutation was made.

Model self-report: `GPT-5.6 Sol`. Requested effort: maximum actually supported. Configured effort: `UNKNOWN` (not exposed by the scheduler/tool surface). Known effective effort: `UNKNOWN`. Exposed provider reasoning-token/time usage: `null` / not exposed. Elapsed execution is recorded separately in the run finish artifact and is tool/wall-clock elapsed work, not pure thinking time.
