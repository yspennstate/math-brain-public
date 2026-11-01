# BT4 fleet04/B06 — triangle witness collision collapses to clean CROSS or bounded BYPASS

Run: `20260922T061043Z-b06-bt4-auto11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-TRIANGLE-PORT-LIFT-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs, hence digons, are allowed in the source statement.

Fresh source verification during this invocation retained the same external boundary. Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), explicitly state that the genuine Bermond--Thomassen conjecture remains unresolved for all `k>=4`; their threshold `2k-1` theorem allows one reversed arc and is not substituted here for a directed cycle. Lichiardopol--Pór--Sereni, *A Step toward the Bermond--Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992, DOI `10.1137/080715792`, prove the genuine `k=3` case and the strengthened `k=2` statement that a digraph in which every vertex has outdegree at least three except at most two vertices of outdegree two contains two vertex-disjoint directed cycles.

No literature-search miss is used as a novelty claim.

## Exact team state consumed

Latest complete lead version read and applied: fleet02/B04 `20260922T051543Z-b04-bt4-r11`, primary report commit `07e6d15d1504e1d11d588ee8b637e9b4710a3d7a`, Git blob `9f1ec8ca9ab3f2737b9dddf98389826f5b926933`, with controlling strengthening commit `1e394073bccc5d223382ae9c66eb71394ac8964c`, blob `aa71a6d910955a009b020ee77aba4a0da0052cdb`. Its lexicographic heavy-triangle cage and exact neutral remainders are used below.

Named OTHER-account assigned partner actually consumed and applied: fleet01/B04 `BT4-HT-TRIANGLE-BOUNDARY-COLLAPSE-v1`, run `20260922T054707Z-b04-bt4-r11`, canonical report commit `74d6202d71aebcda2580fe8e8db47ee29c013b1a`, Git blob `36c1d8eb86ce397198545a2b021bd6f8effade4b`, shared handoff commit `b850154be5439b79de2488b86b025a005eab3647`. That result proves that the aligned triangular light-support boundary is either SIX or has at least two distinct remainder exact-five witnesses, each yielding a source-valid packed-to-packed cross generator by domination.

Compatible disjointness machinery retained, without promoting its outcome label: fleet03/B05 `BT4-SC2-THIRD-PORT-v1`, canonical blob `2d667b4e80a54a16bfd9b551baa4cae55ddf93ae`, and corrected linkage/segment machinery in shared commit `5d6f5aca03679094f820de73cbd226a056a77499`.

## Inherited normal form and the exact triangular state

Assume BT4 false and enter the team's inherited minimal-counterexample normal form: the counterexample is oriented, exact outdegree seven, arc-dominated, and 3-vertex-strong. Choose a three-cycle packing minimizing total packed order and, subject to that, maximizing the number of arcs in the acyclic remainder.

In the lead's exact four-remainder heavy-triangle cage write

`H=h0->h1->h2->h0`,
`R={x,r0,r1,r2}`,
`Ti=hi->ri->x->hi`.

The old remainder is the exact five-edge DAG

`r0->r1`, `r1->r2`, `r0->x`, `r1->x`, `r2->x`.

In the aligned short-support branch the light cycle is

`A=p->p+->p++->p`,

with

`p->h0,r0,x`,
`N+(x) intersect A={p+,p++}`,
`h1->p,p+,p++`.

The partner's neutral packing is

`C0=p->r0->h1->p`,
`T2=h2->r2->x->h2`,
`B`,

with exact four-vertex acyclic remainder

`R0={h0,r1,p+,p++}`.                                      (1)

The partner applies the strengthened two-cycle theorem to `D-(T2 union B)`. If SIX does not already occur, there are at least two distinct vertices of `R0` with residual outdegree exactly two, hence exactly five outgoing arcs into `T2 union B`. Each has a heavy target among `T2,B` and generates a cross by the partner's source-valid domination argument.

From now on assume this non-SIX alternative. If a SIX witness exists anywhere in the branch, it is already routed to the team's separate SIX frontier. Therefore the inherited global-NO-SIX sink facts may also be used: the old sink `x` has fan profile `(3,2,2)`, no heavy-cycle inport, and a unique direct inport on each light support. In particular, write

`b0 in B`, `b0->x`,                                            (2)

for the unique direct `B`-inport of `x`.

## Lemma 1 — the neutral triangle `C0` has a forced three-hit witness on `B`

There exists `q in B` such that

`q->p`, `q->r0`, `q->h1`.                                   (3)

### Proof

Every directed cycle in a BT4 counterexample has an external three-hit witness: otherwise deleting that cycle lowers every remaining outdegree by at most two, leaving minimum outdegree at least five, and the genuine `k=3` theorem supplies three further disjoint directed cycles.

Apply this to `C0={p,r0,h1}`. We show that no vertex outside `B` can hit all three vertices of `C0`.

- `x` hits `h1`, but `x not->p` because its `A`-fan is exactly `{p+,p++}`, and `x not->r0` because `r0->x` and the graph is oriented.
- `h2 not->h1` because `h1->h2`, so `h2` can hit at most `{p,r0}`.
- `r2 not->r0`: otherwise the old remainder arcs `r0->r1->r2->r0` form a directed cycle. Thus `r2` can hit at most `{p,h1}`.
- `h0 not->p` because `p->h0`; although `h0->r0,h1`, it therefore has only two hits.
- `r1 not->r0,h1` because `r0->r1` and `h1->r1`, so it has at most one hit.
- `p+ not->p,h1` because `p->p+` and `h1->p+`, so it has at most one hit.
- `p++ not->h1` because `h1->p++`; it may hit `p` and `r0`, but at most two vertices of `C0`.

The external three-hit witness must therefore lie on `B`, proving (3). QED.

This witness is useful because it supplies a direct `B->C0` cross to **any** chosen port of the triangle `C0`.

## Lemma 2 — among the partner's two deficit witnesses, one is `B`-heavy

Let `w1,w2` be two distinct exact-five witnesses in `R0` supplied by the partner. At least one of them lies in

`{h0,p+,p++}`                                                (4)

and sends at least three arcs into `B`.

### Proof

Only one vertex of `R0` is `r1`, so at least one witness `w` is in (4).

If `w=h0`, then `h2->h0` and `x->h0`, so orientation forbids `h0->h2,x`; among the three vertices of `T2`, `h0` can hit at most `r2`. Since `w` sends exactly five arcs into `T2 union B`, it sends at least four into `B`.

If `w=p+` or `w=p++`, then `x->w`, so orientation forbids `w->x`. It can hit at most the other two vertices `h2,r2` of `T2`, hence at least three of its five external fan arcs go into `B`. QED.

Fix such a witness `w`, and put

`m=|N+(w) intersect B| >= 3`.                               (5)

The partner's strict minimum-packing argument also gives

`B not->w`.                                                   (6)

Indeed, any inarc from `B` into a vertex with at least three fan targets on `B` would create a strictly shorter replacement of `B`.

## Lemma 3 — choose a fan target away from both fixed reverse ports

There exists

`b in N+(w) intersect B`                                    (7)

with

`b notin {q,b0}`.                                            (8)

This is immediate from (5), since at most two vertices are forbidden.

Apply arc domination to the chosen fan arc `w->b`. Following the partner's finite domination lift through the acyclic remainder gives a path

`P : s -> z_k -> ... -> z_0 -> b`                           (9)

whose internal vertices lie in `R0`, whose source `s` is packed, and whose target is the chosen `b in B`. Because of (6), the packed source is not on `B`; hence

`s in C0 union T2`.                                          (10)

If `s in C0`, or `s in T2\{x}`, we already have a port-separated opposite pair. The only apparent collision is

`s=x`.                                                       (11)

The next lemma removes exactly this common sink port.

## Lemma 4 — sink-port lift

Assume the domination cross in (9) has source `s=x`. Then there is another `R0`-internal path

`P' : s' -> ... -> b`                                        (12)

with

`s' in {p,r0,r2,b0}`.                                        (13)

### Proof

There are two cases.

If (9) has a nonempty `R0` interior, let `u` be its first internal vertex; then `x->u`, followed by an `R0`-internal suffix from `u` to `b`.

If (9) is the direct arc `x->b`, then `x` was the packed dominator of the chosen fan arc `w->b`, so `x->w` as well. In this case put `u=w`; the suffix is simply `w->b`.

Thus in either case we have

`x->u` and `u -> ... -> b`,                                 (14)

with every vertex from `u` through the last internal vertex lying in `R0`.

Dominate the arc `x->u`. There is a vertex `y0` with

`y0->x,u`.                                                    (15)

If `y0` is packed, stop. If `y0 in R0`, then in fact `y0=r1`: by (1) and the original sink fan, `x->h0,p+,p++`, while `r1->x`, so orientation leaves `r1` as the only member of `R0` that can point to `x`.

In that sole remainder case, dominate `r1->x`. A dominator `y1` satisfies

`y1->r1,x`.                                                   (16)

It cannot again lie in `R0`, because no member of `R0\{r1}` can point to `x`, and loops are absent. Hence `y1` is packed. Concatenating (15)--(16), when needed, with the suffix in (14) yields (12), with all internal vertices in `R0`.

It remains to locate the packed source `s'`. It points directly to `x`. In the neutral packing `(C0,T2,B)`, the packed inports to `x` are exactly:

- `p` and `r0` on `C0`;
- `r2` on `T2`;
- the unique light inport `b0` on `B`.

The other vertices `h1,h2` are dominated by `x` in the opposite direction, and `x` itself is not a source. This proves (13). QED.

The important point is that a cross whose apparent source is the common sink port `x` cannot remain stuck there: arc domination of its first sink-exit lifts the source to a different packed port, with at most the single remainder vertex `r1` inserted before the old suffix.

## Theorem — triangle witness collision reduces to clean CROSS or a bounded same-support BYPASS

> **BT4-TRIANGLE-PORT-LIFT-v1.** In the partner's non-SIX triangular aligned boundary, one of the following holds:
>
> 1. there is a clean opposite cross pair between `B` and one of `C0,T2`, with four distinct packed ports and disjoint remainder interiors; or
> 2. there is a distinct-port `R0`-internal same-support bypass
>    `J:b0->...->b`
>    on `B`, satisfying
>    `1 <= d_B(b0,b) <= |E(J)| <= 5`,
>    where `d_B(b0,b)` is the forward directed distance from `b0` to `b` on `B`.
>
> In particular, the two remainder exact-five witnesses supplied by fleet01/B04 do **not** leave an unresolved generic ladder-coalescence obstruction. Their collision geometry routes to the same clean `CROSS/BYPASS` interface already present elsewhere in the campaign.

### Proof

Choose the non-`r1` witness `w` and target `b` from Lemmas 2--3, and build the domination cross (9).

**Case A: `s in C0`.** By (8), `b!=q`. The fixed vertex `q` from Lemma 1 has direct arcs to all three vertices of `C0`; choose a port `t in C0` with `t!=s`. Then

`P:s->...->b`, `q->t`

are opposite `C0<->B` crosses with distinct `C0` ports `s,t`, distinct `B` ports `b,q`, and disjoint remainder interiors (the second cross is direct). This is alternative 1.

**Case B: `s in T2\{x}`.** Use the fixed direct inport `b0->x`. By (8), `b!=b0`. The two paths

`P:s->...->b`, `b0->x`

are opposite `T2<->B` crosses. Their `T2` ports are distinct because `s!=x`; their `B` ports are distinct because `b!=b0`; and their remainder interiors are disjoint because the reverse cross is direct. Again alternative 1 holds.

**Case C: `s=x`.** Apply Lemma 4.

- If `s' in {p,r0} subset C0`, use the same fixed `q->t` construction as in Case A, choosing `t!=s'`.
- If `s'=r2 in T2`, use `b0->x` as in Case B; the two `T2` ports are now explicitly `r2` and `x`.
- If `s'=b0`, then (12) is a same-support path

  `J:b0->...->b`

  with all internal vertices in `R0`. By (8), `b!=b0`, so the ports are distinct. Closing `J` with the forward `B[b,b0]` segment gives a directed replacement of `B` disjoint from `C0,T2`. Since `(C0,T2,B)` is globally minimum, if `ell=|E(J)|` and `d=d_B(b0,b)`, then `ell>=d`; otherwise the replacement cycle would be shorter than `B`. Finally `J` has at most the four vertices of `R0` internally, so `ell<=5`. Hence

  `1<=d<=ell<=5`.

  This is alternative 2.

All cases are exhausted. QED.

## Why this is a genuine advance over the partner handoff

The assigned partner had already manufactured **two** exact-five/cross generators, but correctly left their domination-ladder collision unresolved. The theorem above uses the exact neutral triangle geometry rather than counting the two generators as two cycles. Only one non-`r1` witness is needed after the partner's multiplicity guarantees its existence. The second essential ingredient is the forced `B` three-hit witness of `C0`. The third is the sink-port lift: if a cross terminates at the common source `x`, arc domination moves that source to `p`, `r0`, `r2`, or `b0`, with the four-vertex acyclic remainder making the lift finite and explicit.

Thus the short-triangle branch no longer has a separate “two cross generators may coalesce” debt. It reaches a clean four-port opposite-cross pair or a quantified same-support bypass of length at most five.

## Compact conditional end-to-end argument after this run

Assume a BT4 counterexample. The inherited reductions give the exact-seven oriented, arc-dominated, 3-vertex-strong normal form with a globally minimum three-cycle packing and acyclic remainder. Pair deletion gives the campaign's SIX/five-witness alternatives. The lead's lexicographic four-remainder analysis and fleet03/B05 reduce the aligned heavy-triangle branch as follows:

- long aligned light support -> forced clean four-port opposite cross;
- triangular aligned light support -> fleet01/B04 gives SIX or two remainder exact-five/cross generators;
- this report sends the latter generator state -> clean four-port opposite cross or bounded same-support `B` bypass.

Therefore the aligned heavy-triangle branch now has no independent long-support lock, short-support lock, or generic domination-ladder collision. Its non-SIX residue is entirely at the **common clean-CROSS / quantified-BYPASS splice frontier**.

A complete BT4 proof still requires the following explicit unpaid implications:

1. convert the clean opposite-cross interface (including the short-cycle version obtained here) into two vertex-disjoint replacement cycles, a strict smaller three-packing, a directed cycle in an exchanged remainder, or an equivalent contradiction;
2. close the bounded same-support bypass/equality-collar state rather than counting the bypass itself as closure;
3. close the separate general SIX/H5 residuals and the retained seven-remainder triangle-pinwheel/support-carried branches.

No one of these arrows is assumed here.

## Failure checks and nonclaims

- Two cross generators are not counted as two directed cycles.
- A clean opposite-cross pair is not itself counted as two replacement cycles.
- A same-support bypass is retained with the exact minimum-packing tax `ell>=d`; strict/equality cases are not silently collapsed.
- The sink-port lift uses arc domination only on arcs that actually exist (`x->u`, and, in the sole remainder predecessor case, `r1->x`).
- The assertion that only `r1` in `R0` can point to `x` uses orientation together with `x->h0,p+,p++` and `r1->x`.
- The packed-source list `{p,r0,r2,b0}` uses the inherited global-NO-SIX unique-light-inport statement. If a SIX witness occurs instead, the argument routes to SIX and does not use uniqueness.
- The genuine 2009 `k=3` theorem, not the 2026 one-reversal relaxation, is used for the three-hit witness of `C0`.
- No computation or code was used in this report.
- Full BT4 remains open. No novelty claim beyond this private proof attempt is made.

## Honest outcome

`ESSENTIAL_STEP_APPLIED`.

The newest assigned-partner state is advanced from “two source-valid cross generators with unresolved ladder coalescence” to a proved source-valid dichotomy: **clean four-distinct-port opposite CROSS, or a distinct-port same-support BYPASS with forward distance and path length at most five**. The next mathematical target is the actual two-cycle splice/equality-collar closure, not another cross-existence argument.

Model self-report: `GPT-5.6 Sol`. Requested effort: maximum actually supported. Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token/thinking-time telemetry: not exposed. Brain status: `WITHOUT_VERIFIED_BRAIN`.