# BT4 fleet01/B06 — aligned heavy-triangle cross collapse

Run: `20260922T053614Z-fleet01-b06-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-HT-ALIGNED-CROSS-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem, so digons count. The current campaign source record retains Bessy--Muis--Sereni--Steiner--Wiederrecht (arXiv:2608.12948, 13 August 2026) as an explicit statement that the genuine case remains unresolved for every `k>=4`; their theorem permits one reversed arc and is not substituted here.

The inherited genuine lower-parameter input is Lichiardopol--Pór--Sereni: minimum outdegree five forces three vertex-disjoint directed cycles, and their stronger `k=2` theorem says that if every vertex has outdegree at least three except at most two vertices of outdegree two, then two vertex-disjoint directed cycles exist.

## Exact team state consumed

The controlling lead state is fleet02/B04 run `20260922T051543Z-b04-bt4-r11`:

- primary report commit `07e6d15d1504e1d11d588ee8b637e9b4710a3d7a`, blob `9f1ec8ca9ab3f2737b9dddf98389826f5b926933`;
- controlling strengthening blob `aa71a6d910955a009b020ee77aba4a0da0052cdb`.

Its exact heavy-triangle setup is used below. In the exact-two-predecessor cage,

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

with saturation triangles `Ti=hi->ri->x->hi`, and the old remainder has exact chain arcs

`r0->r1`, `r1->r2`, `r0->x`, `r1->x`, `r2->x`.

A light three-hit witness for `T0` is

`p in A`, `p->h0,r0,x`, and `N+(x) intersect A={p+,p++}`.

If `h1` is heavy on this same light support `A`, put

`F=N+(h1) intersect A`, `|F|>=3`.

The lead proves `A not->h1`. It then obtains the aligned dichotomy: either `F={p,p+,p++}`, or choose `a in F\{p,p+,p++}` and obtain a clean opposite light-cross pair with four distinct packed ports and disjoint remainder interiors. The controlling strengthening further proves that the exact consecutive case `F={p,p+,p++}` forces `|A|=3`.

Named OTHER-account result actually applied to the residual branch tree: fleet03/B05 `BT4-SC2-THIRD-PORT-v1`, run `20260922T034032Z-fleet03-B05-BT4-r13`, report blob `2d667b4e80a54a16bfd9b551baa4cae55ddf93ae`. In a long-light pure opposite-cross residual, its minimum return-cycle argument forces a packed endpoint outside the common two ports, or a same-support bypass with exact tax `ell>=d`. Thus, after the aligned branch is collapsed below, the nonaligned long-light reciprocal-cross branch does not remain an isolated two-port obstruction; it feeds the third-port/collar splice interface.

No peer outcome label is used as proof; the exact statements above are the consumed inputs.

## Compact conditional end-to-end chain

Assume a BT4 counterexample and work in the inherited oriented exact-outdegree-seven, arc-dominated, 3-vertex-strong normal form. Choose a globally minimum-total packing `(H,S,U)` of three directed cycles and, among those, maximize the number of arcs induced by its acyclic remainder. Pair deletion gives the SIX / global-NO-SIX split. Existing team work reduces the global-NO-SIX four-remainder source to finite sink/cage interfaces and reduces long-light reciprocal crossings to port-separated third-port or same-support-collar interfaces.

In the heavy-triangle cage, the current lead isolates an aligned residual in which the `T0` light witness `p` lies on the heavy target `A` of `h1`. The lead left either a clean four-port opposite-cross pair or the short-light triangle. The theorem below eliminates the clean alternative completely. Hence the aligned branch is forced directly into the light-triangle residual. In the nonaligned long-light reciprocal-cross branch, the named fleet03/B05 theorem applies and forces a third packed port or quantified same-support bypass. Therefore, after this run, the first unpaid implication inside the aligned heavy-triangle line is the short-light-triangle neutral-exchange splice, not the clean-cross splice.

## Lemma 1 — any aligned off-window heavy target is exactly the third successor

Assume the aligned setup above and suppose

`a in F \ {p,p+,p++}`.

Let

`ell = dist_A(p,a)`, `d = dist_A(a,p)=|A|-ell`.

Then `ell>=3`. Consider

`C_a = p -> h0 -> h1 -> a -> A[a,p]`.

This is a genuine directed cycle. It is vertex-disjoint from

`T2 = h2 -> r2 -> x -> h2`

and from the other light packed cycle `B`. Hence `(C_a,T2,B)` is a legal three-cycle packing. Its total order is

`|C_a|+|T2|+|B| = (d+3)+3+|B| = |A|+|B|+6-ell`.

The original packing has total order

`|H|+|A|+|B| = |A|+|B|+3`.

Global minimum therefore gives

`|A|+|B|+3 <= |A|+|B|+6-ell`,

so `ell<=3`. Since `ell>=3`, necessarily

`ell=3`, hence `a=p^{+3}` and `|A|>=4`.

Thus a clean aligned target cannot occur farther than the third successor. In the only remaining off-window location, the replacement `(C_a,T2,B)` is neutral in total packed order.

## Lemma 2 — global NO-SIX excludes even the third-successor target

Retain `a=p^{+3}` from Lemma 1. Let `z=p+`.

Use the global-NO-SIX branch for the pair of packed cycles `H union B`. The six-fan alternative for this pair is absent. Since every vertex has outdegree exactly seven, the pair-deletion dichotomy therefore gives

`d^+_{D-(H union B)}(z) >= 2`.

Now

`D-(H union B)` contains `A union R` around `z`. Because the packed cycle `A` is chordless and the counterexample is oriented, the only outneighbor of `z` on `A` is its directed successor `p++`. Therefore `z` must have an outneighbor in `R`.

The sink-fan equality gives `x->z`, so orientation excludes `z->x`. Hence

`z->r_i`

for some `i in {0,1,2}`. But every `r_i` sends to `x`. Therefore

`W = z -> r_i -> x -> z`

is a genuine directed triangle.

The three cycles

`H`, `B`, `W`

are pairwise vertex-disjoint. Their total order is

`3+|B|+3 = |B|+6`.

Since Lemma 1 gave `|A|>=4`, the original packing has order

`3+|A|+|B| >= |B|+7`.

Thus `(H,B,W)` is a strictly smaller legal three-cycle packing, contradicting global minimum.

Therefore no vertex `a in F\{p,p+,p++}` exists.

## Theorem — aligned heavy-triangle witness forces a triangular light support

In the exact-two-predecessor heavy-triangle cage in global NO-SIX, assume the `T0` light witness `p` lies on the same light support `A` on which `h1` is heavy. Then

`N+(h1) intersect A = {p,p+,p++}`,

and consequently

`|A|=3`.

Proof: Lemmas 1--2 force `F subseteq {p,p+,p++}`; since `|F|>=3`, equality holds. The current lead strengthening `aa71a6d910955a009b020ee77aba4a0da0052cdb` proves that this exact consecutive fan lock forces `A` itself to be a directed triangle. QED.

This strictly improves the current lead dichotomy. The clean four-port opposite-cross alternative cannot actually survive in the aligned heavy-triangle cage; the aligned branch is forced directly to the short-light triangle.

## Corollary — the forced triangle immediately creates neutral remainder transfers

Write the forced light triangle as

`A = p -> u -> v -> p`,

where `u=p+`, `v=p++`. The sink fan gives `x->u,v`.

For either `z in {u,v}`, global NO-SIX for the pair `H union B` again gives at least two outneighbors of `z` in `A union R`. Chordlessness gives exactly one outgoing neighbor on `A`, so `z` has an outneighbor in `R`. Since `x->z`, orientation excludes `z->x`, and therefore

`z->r_i`

for some `i in {0,1,2}`. Hence

`W_z = z -> r_i -> x -> z`

is a directed triangle disjoint from `H` and `B`.

Because `|A|=3`, replacing `A` by `W_z` preserves total packed order. The exchanged remainder is

`R_z = (R\{r_i,x}) union (A\{z})`,

has four vertices, is acyclic (otherwise there is already a fourth cycle), and by the lead's lexicographic choice has at most the old remainder's five induced arcs.

Thus the short-light branch is not a static triangle: it carries at least two explicit neutral triangle transfers, one from each of the two sink-fan vertices `u,v`. These transfers share `x`, so they cannot simply be counted as two disjoint cycles; no false disjointness claim is made.

## Exact remaining implication

The first unpaid implication on this aligned line is now:

**BT4-HT-TRIANGLE-TRANSFER-SPLICE-v1.** In the exact heavy-triangle cage with forced triangular aligned light support `A=p->u->v->p`, use the two neutral transfers `u->r_i->x->u` and `v->r_j->x->v`, the exact old remainder chain, and the lead's lexicographic `Phi<=5` condition on every exchanged four-vertex remainder to force one of:

1. a directed cycle in an exchanged remainder;
2. a strict smaller three-cycle packing;
3. SIX;
4. a packed-port interface that the established reciprocal/third-port machinery converts to a legal disjoint replacement; or
5. a fourth vertex-disjoint directed cycle.

The two transfer triangles both use `x`, so any proof that simply treats them as disjoint is invalid. The remaining work is a genuine shared-sink rerouting problem.

For the separate nonaligned long-light branch, fleet03/B05 `BT4-SC2-THIRD-PORT-v1` already converts the reciprocal two-port obstruction into a third packed port or a quantified same-support bypass. SIX, triangular F2/F3 witness-cover splice, and the seven-remainder triangle-pinwheel remain separate campaign debts.

## Honest status

`ESSENTIAL_STEP_APPLIED`, not a full proof. The aligned clean-cross branch is eliminated, and the short-light residual gains explicit neutral transfer cycles. Full BT4 remains open.
