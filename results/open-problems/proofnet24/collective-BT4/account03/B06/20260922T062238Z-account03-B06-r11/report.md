# BT4 account03/B06 — both-repeat F3 collapses to a 3/4-cycle with a packed three-hit apex

Run: `20260922T062238Z-account03-B06-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-F3-SHORT-RETURN-APEX-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED` with one stronger local shortcut `CANDIDATE_REFUTED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Target status: `OPEN_NOT_PROVED`

## Exact target and assignment

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source statement, so digons count before the standard minimal-counterexample reduction.

The exact account03/B06 assignment is to use constrained search and symbolic families to test the decisive BT4 lemma while retaining a whole original directed graph and an explicit cycle-packing certificate. The assigned OTHER-account partner is `account04/B04`.

The current external source boundary remains the collective target record: Bessy--Muis--Sereni--Steiner--Wiederrecht, arXiv:2608.12948 (13 August 2026), prove a one-reversed-arc relaxation and explicitly leave the genuine Bermond--Thomassen conjecture open for every `k>=4`. No relaxed cycle is counted below.

## Exact inherited state consumed

### Named partner

I consumed the complete assigned-partner run

`account04/B04`, `20260922T051604Z-account04-B04-BT4-r14`, candidate `BT4-R4-ARCMAX-TRIANGLE-COLLAPSE-v1`, canonical report blob `2f802a03755394931009175d7b6a5f94b0b2b084`.

Its relevant theorem chooses a three-cycle packing lexicographically: first minimum total packed order, then maximum number of arcs in the acyclic remainder. In the four-remainder global-NO-SIX low-fan branch, a surviving F3 state has:

- a post-pivot source triangle `S*=p->x->s->p`;
- another light packed cycle `U`;
- three old-remainder vertices `K={r1,r2,r3}`;
- a freed source vertex `q`, with `q->K`;
- `K->x`;
- `p->q,x`;
- a unique possible `U`-inport `u->x`;
- for every `r in K`, the saturation triangle `T_r=q->r->x->q` has an external three-hit witness in `{p,u}`.

The old and neutral exchanged remainders remain acyclic and tied for the secondary remainder-arc maximum.

### Immediate B06 predecessor theorem

The preceding account03/B06 theorem `BT4-R4-F3-MAJORITY-CROSS-v1`, report blob `697fde372dee5fec64d03923523d13fc6edcab7a`, defines

`A={r in K : p witnesses T_r}` and `B={r in K : u witnesses T_r}`.

Then `A union B=K`; if `|A|>=2`, domination of `p->x` gives a short `U->S*` path

`u->p` or `u->r->p` with `r in K\A`;

if `|B|>=2`, domination of `u->x` gives a short `S*->U` path

`p->u` or `p->r->u` with `r in K\B`.

When both sets repeat, the two possible one-vertex interiors lie in disjoint sets `K\A` and `K\B`.

The previous unpaid implication was to turn those short crosses into an actual splice. This report closes one entire subcase of that port-extraction debt: the **both-repeat** branch.

## Compact conditional route

Assume a BT4 counterexample and enter the inherited exact-seven oriented, arc-dominated, 3-vertex-strong normal form with the lexicographic minimum three-cycle packing. Enter the four-remainder arc-maximal F3 state above.

If only one of `A,B` repeats, the previous one-way short-cross branch remains live. Suppose instead

`|A|>=2` and `|B|>=2`.                                              (BR)

The theorem below proves that (BR) is much more rigid than merely having two opposite crosses:

1. the two short opposite paths form an actual simple directed cycle `W` of order three or four;
2. `W` meets the packed support in exactly the two ports `{p,u}` and has one or two current-remainder vertices internally;
3. every current-remainder vertex outside `W`, and also `x`, has at most two outneighbors on `W`;
4. therefore the genuine `k=3` deletion theorem forces a **packed** vertex outside `W` with at least three outneighbors on `W`.

Thus the both-repeat F3 branch is reduced to a short return cycle carrying a third packed apex. The remaining splice obligation is now a finite port-location problem rather than arbitrary cross extraction.

## Theorem — BT4-R4-F3-SHORT-RETURN-APEX-v1

Work in the arc-maximal triangular F3 state and assume (BR). Let the two short paths supplied by `BT4-R4-F3-MAJORITY-CROSS-v1` be

`P: u -> ... -> p`,
`Q: p -> ... -> u`.

Then:

1. `P union Q` is a simple directed cycle `W` of order `3` or `4`.
2. `W` meets the current packing exactly in `{p,u}`. Its other vertices lie in `K`, one on each of the disjoint sets `K\A`, `K\B` when the corresponding cross is indirect.
3. The profile `A=B=K` is impossible.
4. Every vertex of the current remainder `R*={q} union K` outside `W` has at most two outneighbors on `W`; the packed vertex `x` has zero outneighbors on `W`.
5. Consequently there is a packed vertex

   `c in H union (S*\{p,x}) union (U\{u})`

   with at least three outneighbors on `W`.
6. If `|W|=3`, every such three-hit witness hits both packed ports `p,u`. If `|W|=4`, a three-hit witness that misses one of `p,u` must hit the other packed port and both remainder interiors.

### Proof

Because `|A|>=2`, the previous theorem supplies `P` with either no interior or a single interior in `K\A`. Because `|B|>=2`, it supplies `Q` with either no interior or a single interior in `K\B`. Since

`(K\A) intersect (K\B) = K\(A union B) = empty`,                  (1)

the two interiors are disjoint.

They cannot both be empty. If they were, the oriented graph would contain both arcs `u->p` and `p->u`, a digon. Hence `P union Q` is a simple directed cycle containing `p,u` and one or two remainder interiors. Therefore `|W|` is three or four.

This also rules out `A=B=K`: in that profile the predecessor-location proof from the previous theorem leaves no remainder option for either dominated arc, forcing both direct arcs `u->p` and `p->u`, impossible in the oriented normal form. This proves (1)--(3).

Let `I=V(W) intersect K`, so `1<=|I|<=2`. Consider a vertex `t in K\I`.

If `t in A intersect B`, then `p->t` and `u->t`, so orientation forbids both `t->p` and `t->u`. Thus `t` can hit only the vertices of `I`, at most two.

Suppose `t notin A`. Since `|A|>=2` and `|K|=3`, `K\A={t}`. Because `t` was not used as the interior of `P`, the `u->p` cross must be direct. The opposite cross cannot also be direct, so `Q` has exactly one remainder interior and `|I|=1`. Also `A union B=K` gives `t in B`, hence `u->t` and orientation forbids `t->u`. Even allowing a possible arc `t->p`, vertex `t` can hit at most `p` plus the one remainder interior, hence at most two vertices of `W`. The case `t notin B` is symmetric.

Next, `q` sends to every vertex of `K`, but in the both-repeat branch both `p` and `u` witness at least one saturation triangle, so `p->q` and `u->q`. Orientation therefore forbids `q->p,u`; hence `q` hits exactly the vertices of `I`, at most two.

Finally, `p->x`, `u->x`, and `K->x`. Orientation therefore gives no arc from `x` to either packed port or to any remainder interior of `W`. Thus

`d_W^+(x)=0`.                                                     (2)

This proves the hit cap in (4).

Apply the standard genuine `k=3` deletion threshold to the actual directed cycle `W`. If every vertex outside `W` had at most two outneighbors on `W`, then deleting `W` from the exact-outdegree-seven digraph would leave minimum outdegree at least five. The genuine `k=3` theorem would then give three vertex-disjoint directed cycles in `D-W`, producing four together with `W`, contradiction. Hence some vertex outside `W` has at least three outneighbors on `W`.

By the hit cap, that vertex is not in the current remainder, and by (2) it is not `x`. The only remaining locations are the packed supports listed in (5). This gives the packed three-hit apex `c`.

If `|W|=3`, three hits mean all three vertices, including both `p` and `u`. If `|W|=4`, a three-hit witness missing one packed port must hit the other port and both remainder interiors. QED.

## What this removes from the F3 branch

The 13 symbolic witness-cover patterns in which both `p` and `u` repeat no longer terminate at “two short opposite crosses.” One profile, `A=B=K`, is impossible outright. Every realizable both-repeat profile gives a 3- or 4-cycle `W` and then a packed three-hit apex.

The remaining port problem is correspondingly narrower:

- **triangle return:** a packed apex hits both light ports and the unique remainder interior;
- **quadrilateral return:** a packed apex hits at least one light port; if it misses the other, it hits both exclusive remainder interiors.

The one-way profiles where only `p` or only `u` repeats remain separate and are not claimed closed.

## Symbolic-family verification

The attached checker enumerates all `3^3=27` assignments of the three saturation triangles to `p-only`, `u-only`, or `both`.

It finds:

- 13 both-repeat cover profiles;
- one all-both profile, which has no orientation-admissible opposite-cross realization because it would require the forbidden digon `p<->u`;
- 24 admissible choices of the two domination outputs across the remaining both-repeat profiles;
- 18 triangular return cycles;
- 6 quadrilateral return cycles.

For every admissible symbolic scenario it verifies the set-theoretic remainder hit cap used in the proof. This computation is a finite sanity check only; the proof above is uniform.

Checker commit: `f20a11947133a0ea79ec8ef844ff01aa097f7271`.  
Checker Git blob: `666be9f1b8b29ffdd47a2ce2bc1948ff38247528`.  
Checker SHA-256: `e744bf0c08c29d6513efdee5ece03fcf0a5d0b3e88385f569dd4e268ed0067c9`.

Output commit: `21e3507d38afa28c02f8d27000a541a182570335`.  
Output Git blob: `6c145abdcea2be133f952011212607418c411d15`.  
Output SHA-256: `7513eb83d5656c791ee711647afe921901aba841f7bb7e80d0c8e906d212a847`.  
Validated payload SHA-256: `ff81d95309d12b07c99794d894ddbfcac0492225d12edbdd785e6b07b2230220`.

## Exact constrained full-graph sharpness certificate

The stronger local shortcut

> “in the both-repeat F3 state the two short opposite paths can always be chosen to form a triangle”

is false under the inherited local normal-form, arc-maximality and exchanged-remainder acyclicity hypotheses.

The checker contains a complete 18-vertex oriented digraph with all 126 arcs explicitly encoded. It verifies:

- every outdegree is exactly seven;
- the packed cycles `H=(0,1,2,3,4,5)`, `U=(6,7,8,9,10)`, `S*=(11,12,13)` are chordless;
- every arc has a common predecessor;
- deleting any zero, one or two vertices leaves a strongly connected digraph;
- the old remainder and post-pivot remainder are acyclic;
- the old remainder has four induced arcs, and all three neutral saturation-triangle exchange remainders are also acyclic with four induced arcs;
- the exact F3 cover is

  `15:{p,u}`, `16:{p}`, `17:{u}`,

  so `A={15,16}`, `B={15,17}`;
- `p` and `u` are nonadjacent;
- the unique common predecessor of `p->x` is `17`, and the unique common predecessor of `u->x` is `16`.

Hence the two domination paths are forced to be

`u->17->p`,
`p->16->u`,

and the short return is the genuine quadrilateral

`W=(u,17,p,16)`.

The certificate also shows why the theorem above does **not** claim that every packed three-hit apex must hit both ports: vertex `9` hits `{17,p,16}` and misses `u`.

This certificate is deliberately not a BT4 counterexample. It contains the explicit four pairwise vertex-disjoint directed triangles

`(0,1,10)`, `(2,3,8)`, `(4,5,7)`, `(6,14,16)`.

Thus it refutes only the stronger local triangle shortcut. The repaired universal statement is exactly the 3/4-cycle-plus-packed-apex theorem above; any further closure must use the global no-four-packing condition or the already available splice machinery.

## Exact next implication

`BT4-R4-F3-APEX-SPLICE-v1`:

> In the arc-maximal F3 both-repeat branch, start from the short return cycle `W` and its packed three-hit apex. Use the apex support location together with the reciprocal/third-port/heavy-entry interfaces to force either two vertex-disjoint replacement cycles, a strict smaller three-cycle packing, a directed cycle in an exchanged remainder, SIX, or a fourth directed cycle. In the only non-double-port apex geometry, `W` is a quadrilateral and the apex hits both remainder interiors plus one packed port; exploit that exact pattern rather than assuming a common apex to both light ports.

The single-repeat F3 profiles, F2, and the independent SIX/short-support branches remain explicit debts.

## Honest status

`ESSENTIAL_STEP_APPLIED` with a stronger local `CANDIDATE_REFUTED`.

The both-repeat F3 port-extraction problem has been reduced from two arbitrary short opposite crosses to an actual 3/4-cycle with a forced third packed apex. The exact full-graph certificate shows the quadrilateral alternative is genuinely needed at the local level. Full BT4 remains `OPEN_NOT_PROVED`; no target-level proof, counterexample, publication claim, or novelty claim is made.
