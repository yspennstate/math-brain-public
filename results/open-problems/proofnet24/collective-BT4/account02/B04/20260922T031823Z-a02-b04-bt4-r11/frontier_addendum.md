# Controlling frontier addendum — BT4 account02/B04 20260922T031823Z

This addendum is controlling for the frontier classification of the same-run primary report `report.md` at commit `14ef93ae71f52c019c679c29fca4624e510f7b95`, blob `17d49d472779d5304d30b93c07ce89c289ab20d1`.

Outcome for the **run as a whole** remains `ESSENTIAL_STEP_APPLIED`, but the primary report's global no-cross theorem is reclassified `AUXILIARY_ONLY` at the newest compatible team frontier for the reason stated immediately below.

Brain status remains `WITHOUT_VERIFIED_BRAIN`.

## Frontier correction: global no-cross is already empty

After the first report was written, I source-read the newer compatible account01/B04 result `BT4-MCR-v5-sink-cross-collapse`, report `proofnet24/collective-BT4/account01/B04/20260922T024418Z-b04-bt4-r11/report.md`, Git blob `bbf3afa52d8d0587ae5e210eecaacb7017ac672e`.

Its canonical sink-cross theorem is stronger than the antecedent used in my first report: in the inherited normal form, every sink `x` of the acyclic remainder has a direct packed inport `p in S -> x`, the source fan satisfies `m_S(x)<=2`, and because `x` has all seven outneighbors on the packing, `p->x->y` is a genuine length-two cross-packed transition to a different packed cycle. Therefore a state with *no cross-packed transition anywhere* does not occur at the current frontier.

Accordingly the first report's exact four-remainder equality-saturation calculation remains mathematically valid as a conditional statement, but it is no longer the first unpaid implication. It must not be presented as target-frontier progress by itself.

The actual first unpaid implication is the account01/B04 **canonical sink-cross splice (SC)**: turn the length-two sink cross, together with the source-fan and heavy-target structure, into a disjoint two-cycle replacement, a strict minimum-packing reduction, a directed cycle in an exchanged remainder, or a fourth cycle.

The rest of this addendum attacks that real frontier.

## Exact additional inputs

Besides the lead correction and named account03/B05 `BT4-TCEX-v2.1-linkage` already source-bound in `report.md`, I apply:

1. account01/B04 `BT4-MCR-v5-sink-cross-collapse` (blob `bbf3afa52d8d0587ae5e210eecaacb7017ac672e`): every remainder sink has a direct packed inport; its source fan is at most two; in `NO-SIX` a sink has fan pattern `(3,2,2)` and its heavy target cycle has no arc into the sink;
2. account04/B06 `BT4-SC-v2-inport-escape`, report blob `2c05883b0f7629a4a7691130f2925190283e6b11`: if `p in S -> x` is a no-six light inport with `m_S(x)=2`, then `N+(x) intersect S={p+,p++}`; domination of `p->x` gives either an `R`-internal cross from the other light cycle `U` to `p in S` whose start also sends directly to `x`, or a simple source-return cycle through `p` and remainder vertices;
3. account01/B06 fixed-pair/Menger-collar input (blob `0ffb3fb1b521920e0a9cb3693fda8fd5bbb6a588`): an `R`-supported five-witness heavy on `H` admits three pairwise internally vertex-disjoint `H`-to-witness paths with the repaired path-fan bound.

No peer outcome label is used as proof.

## Canonical no-six sink notation

Work in global `NO-SIX` and let `x` be a sink of `D[R]`. Choose the account01/B04 direct inport

`p in S -> x`.

Because global `NO-SIX` excludes a six-or-more fan into the other two cycles, the source fan cannot be `0` or `1`; hence

`m_S(x)=2`.

The exact sink fan pattern is therefore, after naming the other cycles `H,U`,

`(m_H(x),m_S(x),m_U(x))=(3,2,2)`,

where `H` is heavy. Account01/B04 also gives

`H not-> x`.

Account04/B06 gives the exact source targets

`N+(x) intersect S={p+,p++}`.                                  (1)

The canonical sink cross is any path

`p -> x -> h`, `h in N+(x) intersect H`.                         (2)

Its sole internal vertex is the sink `x`.

## Lemma 1 — neutral source pivot creates a three-target x-free heavy-cross family

Perform the legal equality exchange on the light source cycle `S`:

`S* = p -> x -> p++ -> S[p++,p]`.

Then the new remainder is

`R*=(R\{x}) union {p+}`,

has the same cardinality as `R`, and is acyclic by equality-completion.

In the new packing `(H,S*,U)`, the vertex `x` lies on `S*`. After deleting `H union U`, its only residual outneighbors are

- its support successor `p++` on `S*`, and
- the freed vertex `p+ in R*`.

Hence `x` is a cycle-supported five-witness for the pair `{H,U}`. It is heavy on `H` with fan exactly three. The ambient arcs have not changed, so still

`H not->x`.

Apply the lead's controlling heavy-fan domination escape separately to each of the three distinct arcs

`x->h`, `h in N+(x) intersect H`.

For every such `h` it produces a genuine cross-packed transition ending at `h`, with all internal vertices in `R*`, whose start lies on either `S*` or `U`.

Crucially, **every one of these three transitions avoids `x` entirely**. In the heavy-fan domination construction the first dominator of `x->h` is a vertex `q0!=x` with `q0->x,h`. If the domination ladder terminates on the support `S*`, chordlessness forces its packed apex to be the predecessor `x^-=p`; if it terminates on the other packed cycle it lies on `U`. All ladder interiors lie in `R*`, and `x notin R*`.

Therefore the neutral source pivot converts the single canonical sink cross into a family of three endpoint-distinct heavy-cross interfaces avoiding the pivot vertex:

`S* or U  --->  h_1,h_2,h_3 in H`,                              (3)

with `x` on none of the three paths.

By pigeonhole, at least two of the three x-free transitions have their starts on the same support type (`S*` or `U`). If that type is `S*`, chordlessness forces their common packed start to be exactly `p`.

This is a genuine advance toward `(SC)`: after the legal neutral pivot, cross geometry is no longer concentrated through the single sink vertex.

## Lemma 2 — heavy-return dichotomy at four remainder vertices

Now specialize to `|R|=4`, retaining the original packing and canonical sink `x` with heavy cycle `H`.

Exactly one of the following holds.

**(HR) Heavy-to-light return.** There is a genuine cross-packed transition from `H` to `S` or `U` whose internal vertices lie in `R\{x}`.

**(HT) Heavy-triangle saturation.** The heavy packed cycle `H` has order exactly three. Writing

`V(H)={h_1,h_2,h_3}`,  `R\{x}={r_1,r_2,r_3}`,

there is a relabeling such that

`h_i -> r_i -> x -> h_i`                                        (4)

is a directed triangle for every `i=1,2,3`. Equivalently, the three pairwise internally disjoint `H`-to-`x` Menger paths all have length two and their one-vertex interiors exhaust `R\{x}`. Each path is a saturated equality case of the path-fan theorem.

### Proof

The sink `x` is an `R`-supported five-witness for the deleted pair `{H,S}`, since `m_H(x)+m_S(x)=3+2=5`, and it is heavy on `H`.

Apply the three-path Menger-collar theorem to this witness. Trim each path to its last vertex on `H`. If one trimmed path meets `S` or `U` before reaching `x`, take the subpath from its last `H` vertex to its first light-cycle vertex. Its endpoints lie on distinct packed cycles and its internal vertices lie in `R`; because `x` is the terminal vertex of the full path, this cross subpath does not contain `x`. This is (HR).

Assume (HR) does not occur. Then all three trimmed path interiors lie in `R`, are pairwise disjoint, and end at `x`. Let their edge lengths be `L_i`. The repaired path-fan inequality with `m_H(x)=3` gives

`L_i>=2`.

Because `|R|=4`,

`4 >= 1 + sum_i(L_i-1) >= 1+3 =4`.

Thus every inequality is equality: `L_1=L_2=L_3=2`, and the three one-vertex interiors are exactly `R\{x}`. The three starts on `H` are distinct by the Menger construction.

Equality-completion for a length-two path into a fan of size three says, in the nonsaturated case, that the three fan targets of `x` on `H` are the consecutive three successors of the path's packed start. A proper consecutive three-vertex block on a directed cycle of order greater than three has a unique predecessor. Since the three equality paths have distinct starts but the same fixed fan set `N+(x) intersect H`, the nonsaturated case is impossible. Hence the fan is saturated and

`|H|=m_H(x)=3`.

Now `x` sends to every `h_i`. The three length-two paths can be labeled `h_i->r_i->x`, producing the triangles (4). QED.

This is directional and therefore nonvacuous: the universal canonical cross goes from a light source through `x` toward the packing, whereas (HR) is a return from the heavy cycle and explicitly avoids `x`.

## Lemma 3 — four-remainder canonical splice frontier

Still assume `|R|=4` and global `NO-SIX`. At least one of the following three concrete configurations occurs.

**(A) Internally disjoint opposite heavy/light cross pair.** For one light cycle `L in {S,U}` there is

- a canonical length-two cross `L -> x -> H`, and
- a cross `H -> L` whose internal vertices lie in `R\{x}`.

Thus the two cross interiors are automatically vertex-disjoint.

**(B) Short source-return cycle.** There is a simple directed cycle `W` containing the source port `p` and no other packed vertex, with

`V(W) subseteq {p} union (R\{x})`.

Consequently

`|S| <= |W| <= 4`.                                                (5)

In particular `|S|` is three or four.

**(C) Heavy-triangle saturation.** Configuration (HT) of Lemma 2 holds.

### Proof

If Lemma 2 gives (HT), we are in (C).

Otherwise there is a heavy-to-light return. If it returns from `H` to the source light cycle `S`, combine it with the canonical `S->x->H` cross. Its return path avoids `x`, so (A) holds.

The remaining case is a return `H->U`. Apply account04/B06's domination theorem to the source inport `p->x`.

If its cross alternative occurs, it supplies a packed vertex `a in U` with both a cross path `U->S` and a direct inport `a->x`. Because `m_U(x)=2`, the direct inport `a->x` itself supplies the canonical length-two cross `U->x->H`. Pair this with the existing `H->U` return, whose interior avoids `x`. Thus (A) holds with `L=U`.

If the cross alternative does not occur, account04/B06 supplies a simple source-return cycle through `p` and remainder vertices. In that construction the cycle is obtained from the domination ladder for an internal arc `q->x`: the ladder path ends at `q` and is then closed by `q->p`. Since `x` is the sink target of the dominated internal arc, `x` is not a vertex of the ladder or of the resulting return cycle. Therefore its non-`p` vertices lie in `R\{x}`, not merely in `R`. With `|R|=4`, the sharper size bound is `|W|<=1+3=4`. Global minimum of the three-cycle packing gives `|W|>=|S|`, proving (5) and (B). QED.

## What this pays toward the actual splice obstruction

Before this addendum, the true current frontier was the single canonical sink cross

`light -> x -> heavy`

with no guaranteed compatible second interface.

After this addendum:

1. a legal neutral source pivot creates **three endpoint-distinct x-free crosses into the heavy cycle**, so the sink is no longer an unavoidable common interior vertex for all available cross geometry;
2. when `|R|=4`, the heavy-return side is reduced to the exact trichotomy (A)--(C):
   - an opposite heavy/light cross pair with disjoint interiors;
   - a source cycle of order at most four with an `R\{x}` return cycle;
   - or a heavy directed triangle with a perfect three-path matching through all of `R\{x}`.

These are all substantially more rigid than a generic cross transition.

The unpaid step is still a true splice statement: an opposite cross pair alone gives one alternating cycle, not automatically two disjoint replacement cycles; the short source-return and heavy-triangle cases likewise require one more compatibility argument. None is promoted to a four-cycle packing here.

## Updated conditional end-to-end proof

At the newest compatible frontier, a complete proof follows from one sharpened closure statement `(SC+)` in addition to the inherited normal-form reductions:

> **(SC+)** Every canonical no-six sink state closes when supplied with either the x-free three-target heavy-cross family of Lemma 1, or (for `|R|=4`) one of configurations (A)--(C) of Lemma 3; the closure must be a legal two-cycle replacement, a strict reduction of the globally minimum three-packing, a directed cycle in the exchanged remainder, or a fourth vertex-disjoint directed cycle.

The SIX side remains handled by its separate campaign interface if a neutral step ever exits `NO-SIX`.

Thus the correct first next question is no longer whether cross geometry exists. It is whether the x-free second interfaces above can be paired with the canonical sink cross without reusing packed segments.

## Failure checks and honest classification

- The primary same-run `report.md` is preserved unchanged for provenance, but its global no-cross theorem is `AUXILIARY_ONLY` at this frontier because account01/B04 already proves global no-cross impossible.
- The new Lemmas 1--3 do not assume global absence of cross transitions.
- The account03/B05 marked-segment theorem is used only in the earlier auxiliary calculation with its heavy-inport hypothesis satisfied; the quarantined misuse remains quarantined.
- In Lemma 2 the three distinct Menger starts plus equality-completion are what force `|H|=3`; this conclusion is not inferred merely from `m_H=3`.
- In Lemma 3 the sharpened return-cycle bound `|W|<=4` uses that the source-return cycle constructed from domination of `p->x` avoids the sink `x` itself.
- An opposite cross pair is not claimed to be two replacement cycles.
- No full BT4 proof or novelty claim is made.

**Run-level classification: `ESSENTIAL_STEP_APPLIED`.**  
**Primary-report no-cross subresult at newest frontier: `AUXILIARY_ONLY`.**  
**New essential result: canonical sink-cross gains an x-free three-target heavy-cross family, and the four-remainder splice frontier reduces to (A) opposite disjoint cross pair, (B) light source cycle of order at most four with sink-avoiding return, or (C) heavy-triangle saturation.**
