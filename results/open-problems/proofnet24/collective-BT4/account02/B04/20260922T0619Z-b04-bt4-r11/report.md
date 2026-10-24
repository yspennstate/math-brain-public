# BT4 lead report — clean four-port witness lift and SC2-hypothesis correction

Run: `20260922T0619Z-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Role: account02/B04 lead  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Subclaim correction: `CANDIDATE_REFUTED` for the previous direct invocation of `BT4-SC2-THIRD-PORT-v1` on a four-port mixed cycle  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Target status: `OPEN_NOT_PROVED`

## 1. Source-exact target and literature boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are permitted in the source problem, so directed digons count.

The source boundary was refreshed this run. Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), explicitly states that the genuine conjecture remains unresolved for every `k>=4`; its `2k-1` theorem permits each packed cycle either to be directed or to become directed after reversing one arc. No such nearly-directed object is counted here. Lichiardopol--Pór--Sereni, *A Step toward the Bermond--Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992, proves the genuine `k=3` input: minimum outdegree five gives three vertex-disjoint directed cycles, and also the strengthened `k=2` result used by the team.

## 2. Exact inherited mathematics actually consumed

### Lead state

I start from the immediately preceding account02/B04 lead report

`proofnet24/collective-BT4/account02/B04/20260922T051543Z-b04-bt4-r11/report.md`,

scientific commit `07e6d15d1504e1d11d588ee8b637e9b4710a3d7a`, Git blob `9f1ec8ca9ab3f2737b9dddf98389826f5b926933`, together with its controlling strengthening blob `aa71a6d910955a009b020ee77aba4a0da0052cdb`.

The inherited normal form is a hypothetical oriented exact-outdegree-seven counterexample `D`, arc-dominated and 3-vertex-strong, with a three-cycle packing chosen lexicographically: minimize total packed order, then maximize the number of arcs induced by the acyclic remainder. Packed cycles are chordless.

The live four-remainder heavy-triangle cage is

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

with saturation triangles

`Ti=hi->ri->x->hi`.

The old remainder arcs are exactly

`r0->r1`, `r1->r2`, `r0->x`, `r1->x`, `r2->x`,

and the exact cage also contains `r0->h1`, `r1->h2`, `h0->r0`, `h1->r1`, `h2->r2`. The old remainder sink is `x`.

For the `T0` deletion witness there is a light support `A` and a vertex `p in A` with

`p->h0,r0,x`,

and sink-fan equality

`N+(x) intersect A = {p+,p++}`.

### Named partner account03/B05

I read and apply the exact account03/B05 results rather than their outcome labels.

1. `BT4-SC2-THIRD-PORT-v1`, report blob `2d667b4e80a54a16bfd9b551baa4cae55ddf93ae`. Its crucial premise is a minimum opposite-cross return cycle `K=P union Q` whose two cross arms have the **same two packed endpoints**, so `K` meets the old packing at exactly two vertices `{p,a}`. The genuine `k=3` deletion theorem then forces a three-hit witness to hit an internal remainder vertex of `K`, and domination converts that internal hit into a third packed port or a distinct-port same-support bypass.

2. `BT4-HT-SHIFTED-TRIPLE-v1`, report blob `63fc0bf48372601801b40571f6610820ed31e96b`. In the aligned heavy-triangle branch, if `h1` is heavy on `A` and `|A|>=4`, then

`N+(h1) intersect A = {p+,p++,p+++}`.

If `h1->p`, global minimum instead forces `|A|=3`.

3. Its controlling addendum `BT4-HT-FORCED-CLEAN-CROSS-v1`, blob `e1d5aa82bc8d24be39cb7c34a0ef92ccd878dacd`. In the `|A|>=4` branch, domination of `h1->p+++` yields a vertex `q` on the other light support `B` with

`q->h1,p+++`.

Choose `b in N+(x) intersect B` with `b!=q`. Then there is a clean opposite light-cross pair

`P : p -> x -> b`,

`Q : q -> p+++`,

with four distinct packed ports and disjoint remainder interiors.

I also use the compatible account01/B05 theorem `BT4-COMPATIBLE-BYPASS-CONDENSATION-v1`, report blob `9033957c23706f309a7007530fb65868d736eb61`: once a family of same-support remainder bypasses is compatible, simultaneous switching converts a dependency circuit into a fourth directed cycle, while a full-cover acyclic dependency family regenerates a canonical sink/five-witness state. I do not infer compatibility or full coverage from one bypass.

## 3. Compact conditional end-to-end route

A complete BT4 proof follows from the inherited reductions plus closure of the remaining explicit interfaces as follows.

1. A minimal counterexample can be taken oriented: deleting a digon removes at most two outneighbors from every other vertex, after which the genuine `k=3` theorem supplies three cycles disjoint from the digon. Retain seven outgoing arcs at each vertex to obtain the exact-seven spanning normal form.
2. The genuine `k=3` theorem supplies three disjoint directed cycles. Choose a globally minimum-total packing and then maximize the acyclic-remainder arc count. The remainder is acyclic, packed cycles are chordless, and the inherited reductions give arc domination and 3-vertex-strongness.
3. Pair-deletion/deficit analysis splits the campaign into `SIX` and global `NO-SIX`. Existing compatible work turns the principal no-six sink states into exact `(3,2,2)` / five-witness / reciprocal-cross / neutral-pivot interfaces, and turns the all-long exact-six wall into `CROSS/BYPASS` or a short-support boundary.
4. In the four-remainder heavy-triangle branch, the previous lead plus account03/B05 reduce the aligned long-support state to the clean four-port pair `P,Q` above. The triangle support boundary is separately reduced by account01/B04 to `SIX` or multiple cross generators.
5. The present report proves that the clean four-port pair **always produces another genuine packed-to-packed CROSS or a distinct-port same-support remainder BYPASS**, despite the failure of the old direct invocation of `BT4-SC2-THIRD-PORT-v1`.
6. Hence the aligned long-support heavy-triangle branch now feeds the common `CROSS/BYPASS` splice frontier without an unsupported SC2 premise. Full BT4 remains conditional on: (a) `SIX` closure; (b) a universal compatible CROSS/BYPASS splice/selection theorem, including coalesced-port cases; (c) the remaining bounded F2/F3 short-support states; and (d) the seven-remainder triangle-pinwheel/support-carried omitted-sink branch.

The first local missing implication after this report is therefore no longer “obtain a third interface from the clean pair.” It is the strictly narrower **coalesced-port CROSS/BYPASS splice**: when the new interface has no fresh packed endpoint, convert the resulting repeated four-port geometry into two vertex-disjoint replacement cycles, a strict smaller three-packing, a cyclic exchanged remainder, or a compatible bypass family covered by the condensation theorem.

## 4. Correction — the old direct SC2 application was not source-valid

The previous lead report said that the clean four-port pair was “stronger than” the input of account03/B05 `BT4-SC2-THIRD-PORT-v1`, so that the theorem could be invoked directly after forming a minimum return cycle. This implication is not justified.

The SC2 theorem uses opposite paths with **common packed endpoints**:

`a -> ... -> p`, `p -> ... -> a`.

Their union is a directed cycle meeting the old packing at exactly `{p,a}`. Consequently a three-hit witness for that cycle must hit a remainder-internal vertex, since there are only two packed vertices available.

The clean heavy-triangle pair has **four distinct packed ports**:

`p -> x -> b`, `q -> p+++`.

To close these arms into a directed cycle one must add old-support segments. Put `a3=p+++` and define

`K = p -> x -> b -> B[b,q] -> q -> a3 -> A[a3,p] -> p`.       (1)

This is a genuine simple directed cycle, but it contains all packed vertices of the support segments `B[b,q]` and `A[a3,p]`, not merely four ports and certainly not only two packed vertices. The three-hit witness supplied by the genuine `k=3` theorem may therefore put all of its hits on packed vertices of `K`. The internal-remainder-hit inference used by `BT4-SC2-THIRD-PORT-v1` is absent.

Thus the partner theorem remains valid, but its direct use on (1) is rejected. This is a dependency/hypothesis correction, not a counterexample to BT4 or to the SC2 theorem.

## 5. New theorem — BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1

### Statement

Assume the inherited oriented, arc-dominated, minimum-packing normal form and the aligned four-remainder heavy-triangle state with `|A|>=4`. Let

`P : p -> x -> b`,

`Q : q -> a3`, where `a3=p+++`,

be the account03/B05 clean opposite pair, with `p,a3 in A`, `b,q in B`, all four ports distinct, and `x in R`. Let `K` be the mixed directed cycle (1).

Then there exists at least one directed path `J:c->...->w` satisfying:

- `c,w` are distinct vertices on the old packed cycles `H,A,B`;
- every internal vertex of `J` lies in the old remainder `R`;
- either `c,w` lie on different packed cycles, so `J` is a genuine cross-packed transition, or `c,w` lie on the same packed cycle, in which case `J` is a genuine distinct-port same-support bypass;
- in the same-support case, if `ell` is the edge length of `J` and `d` is the forward support distance from `c` to `w`, then global minimum gives `ell>=d`; equality is neutral and `ell>d` is a strict collar.

If the witness producing `J` is itself packed, then `J` can be taken as a direct cross. The only possibility for the source endpoint of a domination-lifted `J` not to be a new packed port is that the domination ladder terminates at an already-used packed port; that is precisely the residual four-port coalescence case.

### Proof

The cycle `K` is genuine and simple. Its pieces lie successively on `A`, the old remainder vertex `x`, `B`, and `A`; the four packed ports are distinct and the two old packed cycles are disjoint.

Apply the genuine `k=3` deletion theorem to `K`. In a BT4 counterexample, some vertex

`v notin V(K)`

has at least three distinct outneighbors on `K`. Otherwise every vertex of `D-K` loses at most two of its seven outgoing arcs, so `delta+(D-K)>=5`; the Lichiardopol--Pór--Sereni theorem gives three disjoint directed cycles in `D-K`, and together with `K` they form the forbidden four-pack.

There are two location cases for `v`.

#### Case 1: v is packed

Suppose first `v` lies on one of the old packed cycles.

If `v in H`, every packed hit of `K` lies on `A` or `B`, hence is already a cross arc from `H`. Since only one vertex of `K` is in the old remainder, namely `x`, at least two of the three hits are packed, so a direct cross exists.

If `v in A`, chordlessness of `A` says that `v` has at most its support successor as an outneighbor on `A`. Among at least three hits on `K`, at most one can therefore lie on the `A` part of `K`, and at most one is the remainder vertex `x`. Hence at least one hit lies on `B`, giving a direct `A->B` cross.

The same argument with `A,B` interchanged applies if `v in B`.

Thus a packed witness always gives a direct genuine cross. Notice that the source `v` lies outside `K`, so in particular it is not one of the four original clean-pair ports.

#### Case 2: v lies in the old remainder

Now assume `v in R`. Since `v notin K` and the only old-remainder vertex of `K` is `x`, we have `v!=x`. Of the at least three hits of `v` on `K`, at most one is `x`; choose a packed hit

`v -> w`,                                                    (2)

where `w` lies on `H,A`, or `B` (in fact here on `A` or `B`).

Use the inherited arc-domination property on (2). If a dominator `v1` of the arc `v->w` lies in `R`, then

`v1->v,w`.

If `v1` is still in `R`, dominate `v1->w` and continue. This constructs a backwards chain

`... -> v2 -> v1 -> v -> w`,                                  (3)

all of whose current remainder vertices also send directly to `w`.

The process cannot remain in `R` forever. The old remainder is finite and acyclic; a repeated remainder vertex would create a directed cycle in `D[R]`. Therefore the first vertex outside `R` encountered in the domination chain is packed; call it `c`. Then (3) truncates to a directed packed-to-packed path

`J : c -> ... -> v -> w`                                      (4)

whose internal vertices all lie in `R`.

The endpoints are distinct. At the last domination step the packed apex `c` has the direct arc `c->w`; if `c=w`, this would be the forbidden loop `w->w`.

If `c,w` lie on different packed cycles, (4) is a genuine cross. If they lie on the same packed cycle `T`, replace the forward support segment `T[c,w]` by `J`. The other two packed cycles are untouched because the interior of `J` is wholly in `R`. If `ell<d_T(c,w)`, this replacement gives a three-cycle packing of strictly smaller total order, contradicting global minimum. Hence

`ell >= d_T(c,w)`.                                             (5)

Thus (4) is a distinct-port same-support bypass carrying the exact minimum-packing tax (5).

This proves the theorem. QED.

## 6. Why this is genuinely stronger than the corrected dependency state

The theorem does not repair the old SC2 argument by pretending the mixed cycle has only two packed vertices. Instead it uses the actual four-port cycle and splits the deletion witness by location.

- A packed witness automatically gives a direct cross because chordlessness prevents three hits from remaining on its own packed support.
- A remainder witness has at least two packed hits because `K` contains only one remainder vertex; any such hit is lifted by repeated domination to a packed-to-packed path.
- A same-support output is not called a contradiction; it is retained with the exact exchange inequality `ell>=d`.

Hence the clean four-port state **cannot terminate merely because the SC2 internal-hit premise fails**. It always emits a genuine `CROSS/BYPASS` object in the original digraph.

There is one important nonclaim. For a remainder witness, the terminal packed apex `c` in (4) need not be outside the original four-port set `{p,a3,b,q}`. If `c` is a fresh packed vertex, the account03/B05 “third port” objective is achieved. If `c` is an old port and (4) is same-support, the bypass machinery applies. The only locally new obstruction is therefore an additional cross whose two packed endpoints are both among the four old ports. I do not count that coalesced cross as two replacement cycles.

## 7. Direct attack on the new first missing inference

Call the residual statement `BT4-FOUR-PORT-COALESCENCE-v1`:

> In the exact aligned heavy-triangle clean-pair state, suppose every domination-lifted output of `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1` that is not already a same-support bypass is a cross with both endpoints in `{p,a3,b,q}`. Prove that the resulting finite four-port cross geometry yields two vertex-disjoint replacement cycles, a strict smaller three-packing, a directed cycle in an exchanged remainder, or a compatible bypass family to which `BT4-COMPATIBLE-BYPASS-CONDENSATION-v1` applies.

The present run narrows this further.

If the external three-hit witness is packed, its source lies outside `K`; therefore its direct cross has a fresh source port and cannot be in the four-port-coalesced residual. Consequently **four-port coalescence is possible only when the three-hit witness lies in the old remainder and the domination ladder returns to an old port**.

Moreover the terminal packed apex directly hits the chosen packed target `w`, not merely by a long path. Thus the residual contains an additional **direct** cross among the four ports, while the lifted path through the witness supplies a second realization of the same endpoint relation with nonempty remainder interior. This endpoint-matched direct/path pair is extra structure unavailable in the generic CROSS frontier.

This is the first still-unpaid local implication. It is now a finite endpoint-coalescence problem, not the earlier unrestricted request to manufacture a third port from a four-port cycle.

## 8. Interaction with the newest compatible bypass theorem

Account01/B05 `BT4-COMPATIBLE-BYPASS-CONDENSATION-v1` applies immediately whenever repeated uses of the witness lift produce same-support bypasses whose remainder interiors and replaced support segments can be selected compatibly. A dependency circuit then gives a fourth directed cycle. A compatible family consuming all old remainder vertices regenerates a sink/five-witness state rather than an unstructured collar.

The present theorem does **not** assert that one bypass already covers the remainder or that two outputs are compatible. Its value is that the aligned clean-pair branch now joins the same CROSS/BYPASS accumulation mechanism as the account04/B06 exact-six wall and the account03/B06 F3 short-cross state.

## 9. Failure checks and boundaries

- `BT4-SC2-THIRD-PORT-v1` itself is not refuted. Only its direct application to the four-port mixed cycle is rejected because the two-packed-vertex premise fails.
- The cycle `K` in (1) is genuinely directed in the original graph; no reversed-arc relaxation is used.
- The three-hit lemma uses the genuine minimum-outdegree-five `k=3` theorem on `D-K` after checking the exact loss of at most two outgoing neighbors.
- In the remainder-witness case, the domination process is finite because `D[R]` is acyclic. No compactness or average-degree argument is used.
- A cross is not counted as a fourth cycle. A bypass is not counted as a contradiction. Equation (5) is the exact minimum-packing tax and allows equality.
- The separate `SIX`, F2/F3 bounded-support, and seven-remainder triangle-pinwheel debts remain open.
- No finite computation was needed for this theorem; there is therefore no numerical certificate to promote.

## 10. Honest status

`ESSENTIAL_STEP_APPLIED`.

A real hypothesis gap in the previous clean-pair-to-SC2 transfer was found and preserved rather than hidden. The gap is replaced by the source-valid theorem `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`: every clean four-port heavy-triangle state emits a genuine CROSS or same-support BYPASS through the actual mixed cycle, the genuine `k=3` deletion theorem, chordlessness, and domination. The first local debt is reduced to four-port endpoint coalescence for a remainder-supported witness, plus the already-separate global SIX/short-support/pinwheel closures. BT4 remains open.
