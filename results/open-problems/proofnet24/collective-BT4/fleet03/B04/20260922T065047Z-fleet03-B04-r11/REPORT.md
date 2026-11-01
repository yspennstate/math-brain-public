# BT4 fleet03/B04 — common-port support collapse to B3/B4

Run: `20260922T065047Z-fleet03-B04-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-HT-COMMON-PORT-SUPPORT-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Target status: `OPEN_NOT_PROVED`

## Target and source boundary

Target: every finite loopless digraph with at most one arc per ordered vertex pair and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles; opposite arcs are allowed in the source problem, so digons count.

A current source check still has Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), stating that the genuine conjecture remains unresolved for every `k>=4`. Their theorem permits cycles that become directed after reversing one arc; no such relaxed object is counted here.

## Exact other-account result consumed

Assigned partner actually consumed: `fleet04/B05`, run `b05-20260922t061406z-r34`, candidate `BT4-HT-EQUALITY-COLLAR-ELIMINATION-v1`, canonical report blob `4720ee1408bd58b0ce7ca36ef05b402600f0a5c8`.

The partner works in the exact four-remainder, global-`NO-SIX`, heavy-triangle cage and proves that in the same-heavy-`A` triangular branch the two pure-remainder equality collars are impossible. Hence its common-port shortest-routing dichotomy must emit a genuine packed cross. Its first unpaid local implication is `HT-CROSS-HALL-SPLICE`.

I do not copy that outcome label as proof. The exact cage facts used below are restated explicitly.

## Inherited exact cage

Assume a hypothetical BT4 counterexample has already been reduced to the team's oriented exact-outdegree-seven normal form. Choose three disjoint directed cycles `(H,A,B)` with minimum total packed order, and among those maximize the number of arcs induced by the acyclic remainder. In the partner branch,

`H = h0 -> h1 -> h2 -> h0`,

`A = p -> u -> v -> p`,

`R = {x,r0,r1,r2}`.

The exact cage contains

`h0->r0`, `h1->r1`, `h2->r2`,

`r0->r1`, `r1->r2`,

`ri->x` for `i=0,1,2`,

`x->hi` for `i=0,1,2`,

and

`r0->h1`, `r1->h2`, `r2->h0`.

The old remainder has no other arcs. In particular `x` is its sink. The aligned triangle state also has

`p->h0,r0,x`,

`x->u,v`,

`h1->p,u,v`,

and in the same-heavy-`A` branch

`h2->p,u,v`.

The partner proves that `u` and `v` have a common remainder outneighbor `r_k`, `k in {0,1,2}`, and that this common port is heavy on `B`; write

`m_B(q)=|N+(q) intersect B|`.

Thus

`m_B(r_k)>=3`.                                                 (1)

Two partner capacity facts are also inherited and used exactly:

1. If a remainder vertex `q` has `m_B(q)>=2`, then at most one vertex of `B` can send directly to `q`; if `m_B(q)>=3`, no vertex of `B` can send directly to `q`. This is the minimum-packing path/fan inequality applied at path length one.
2. The old sink `x` has at most one `B`-inport.

Finally, `r0` has `m_B(r0)>=2`. The exact five-witness `r2` also has `m_B(r2)>=2`: if it is heavy on `A`, the fact that `A` is a triangle forces exactly three `A` targets and hence two `B` targets; if it is heavy on `B`, it has at least three `B` targets.

Therefore

`cap_B(x)<=1`, `cap_B(r0)<=1`, `cap_B(r2)<=1`,               (2)

where `cap_B(q)=|{b in B:b->q}|`, while from (1)

`cap_B(r_k)=0`.                                                (3)

## Lemma 1 — every B vertex needs a remainder exit

Every vertex `b in B` sends to at least one vertex of `R`.

### Proof

Delete `H union A`. In global `NO-SIX`, no surviving vertex can lose six or seven of its seven outgoing arcs to the deleted pair, so every surviving vertex has at least two outneighbors in `B union R`. The packed cycle `B` is chordless, and the normal form is oriented, so a vertex of `B` has exactly one outneighbor in `B`, namely its successor. Its second surviving outneighbor must lie in `R`. QED.

This is the only place where the degree-seven budget and global `NO-SIX` are used to force coverage of every `B` vertex.

## Lemma 2 — middle common port forces B to be a triangle

If `k=1`, then `|B|=3`.

### Proof

The heavy common port `r1` receives no arc from `B` by (3). By (2), each of `r0,r2,x` receives arcs from at most one vertex of `B`. Lemma 1 says every vertex of `B` must send to at least one of those three ports. Hence

`|B| <= cap_B(r0)+cap_B(r2)+cap_B(x) <= 3`.

The normal form is oriented, so every directed cycle has order at least three. Thus `|B|=3`. QED.

This conclusion does not assume the partner's now-eliminated pure-remainder equality collar. It therefore remains valid in the compulsory-cross branch.

## Lemma 3 — an r1-to-h0 arc already gives four disjoint cycles

The arc `r1->h0` is impossible in a counterexample.

### Proof

If `r1->h0`, then

`C0 = h0 -> r0 -> r1 -> h0`

is a directed triangle. Independently,

`C1 = h1 -> h2 -> r2 -> x -> h1`

is a directed 4-cycle, using the packed edge `h1->h2`, the cage arc `h2->r2`, the remainder arc `r2->x`, and the saturation arc `x->h1`.

`C0` and `C1` are vertex-disjoint. Both are disjoint from the packed light cycles `A` and `B`. Therefore `A,B,C0,C1` are four pairwise vertex-disjoint genuinely directed cycles, contradiction. QED.

This is a direct target-level contradiction inside the branch; no packing exchange or relaxed cycle is used.

## Lemma 4 — off-centre common ports create an exact r1 hub

Assume `k in {0,2}` and `|B|>=4`. Then there is a unique vertex `b* in B` such that

`r1->b*`,                                                     (4)

and in fact

`N+(r1) = {r2,h2,x,p,u,v,b*}`.                                (5)

Moreover at least `|B|-2` vertices of `B` send to `r1`.

### Proof

If `k=0`, the common heavy port `r0` receives no `B`-inport, while `r2` and `x` each have capacity at most one. If `k=2`, the common heavy port `r2` receives no `B`-inport, while `r0` and `x` each have capacity at most one. By Lemma 1, in either case all but at most two vertices of `B` must use `r1` as a remainder exit. Therefore

`cap_B(r1) >= |B|-2 >= 2`.                                    (6)

If `m_B(r1)>=2`, the inherited minimum-packing inport-capacity lemma would give `cap_B(r1)<=1`, contradicting (6). Hence

`m_B(r1)<=1`.                                                  (7)

Inside `H union R`, the exact cage forces

`r1->r2,h2,x`,

while orientation excludes `r1->r0` because `r0->r1`, and excludes `r1->h1` because `h1->r1`. Thus outside `B`, the only possible additional outneighbors of `r1` are

`h0,p,u,v`.

Since `d+(r1)=7` and (7) allows at most one `B` target, `r1` must send to at least three of these four vertices. Lemma 3 excludes `r1->h0`, so necessarily

`r1->p,u,v`.

The six outside-`B` arcs

`r1->r2,h2,x,p,u,v`

are now forced. Exact outdegree seven therefore forces exactly one `B` target `b*`, proving (4)-(5). QED.

## Lemma 5 — global packing minimality caps the r1 funnel at two B inports

Under Lemma 4, at most two vertices of `B` send to `r1`.

### Proof

Let `n=|B|` and let `b->r1` with `b in B`. Because `r1->b*` and the normal form is oriented, `b!=b*`. Let `d_B(b*,b)` be the forward distance on the directed cycle `B` from `b*` to `b`.

Then

`C_b = b -> r1 -> b* -> B[b*,b]`

is a genuine directed cycle. It is disjoint from `H` and `A`, so replacing packed cycle `B` by `C_b` gives another three-cycle packing `(H,A,C_b)`. Its order is

`|C_b| = d_B(b*,b)+2`.

Global minimum of the original total packed order implies

`d_B(b*,b)+2 >= n`,

hence

`d_B(b*,b) >= n-2`.                                           (8)

Among vertices of a directed `n`-cycle distinct from `b*`, only the predecessor and second predecessor of `b*` have forward distance at least `n-2`. Therefore at most two vertices of `B` can send to `r1`. QED.

## Theorem — common-port support collapse

In the same-heavy-`A` triangular common-port branch of fleet04/B05, the other packed light support satisfies

`|B| <= 4`.                                                     (9)

More precisely:

1. if `k=1`, then `|B|=3`;
2. if `k in {0,2}` and `|B|>=4`, then `|B|=4` and the remainder-exit geometry is exact.

For the second case, write

`B = b0 -> b1 -> b2 -> b3 -> b0`

with `b0=b*`, the unique `B` target of `r1`. Then

`b2->r1`, `b3->r1`, `r1->b0`,                                (10)

and these are the only `B-r1` arcs in the indicated directions. Let

`s = r2` if `k=0`, and `s = r0` if `k=2`.

The remaining two vertices `b0,b1` must send to `x` and `s` bijectively:

`{b0,b1}` has one outarc to `x` and one outarc to `s`, from distinct sources.  (11)

### Proof

The `k=1` case is Lemma 2. Now let `k in {0,2}`. If `|B|<=3`, there is nothing to prove. If `|B|>=4`, Lemma 4 gives at least `|B|-2` `B`-inports to `r1`, while Lemma 5 gives at most two. Hence

`|B|-2 <= 2`,

so `|B|<=4`. Therefore `|B|=4`.

Equality forces exactly two `B`-inports to `r1`. By (8) they are precisely the two vertices at forward distances two and three from `b0=b*`, namely `b2,b3`, proving (10).

Vertices `b0,b1` still require remainder exits by Lemma 1. They cannot use the heavy common port `r_k`; they do not send to `r1` by (10). The only available ports are `x` and `s`, each of which has `B`-inport capacity at most one by (2). Thus `b0,b1` use these two ports bijectively, proving (11). QED.

## Effect on the partner's first missing implication

Before this run, `HT-CROSS-HALL-SPLICE` had to splice the partner's compulsory genuine cross while `B` could have arbitrary order. The theorem removes that freedom in the entire same-heavy-`A` triangular common-port branch:

- the middle common port `k=1` forces `B` to be a triangle;
- the two off-centre common ports reduce either to a triangle or to one exact directed 4-cycle with the hub pattern (10)-(11);
- in the 4-cycle state, `r1` hits every vertex of `A` and has exactly one `B` target.

Thus the next splice calculation is finite at the packed-support level: only `B3` and the exact `B4` funnel remain in this branch. The genuine cross produced by fleet04/B05 must now be closed inside those bounded support geometries, together with the existing x-free Hall/return interfaces. The same-heavy-`B` Hall branch and the campaign's separate `SIX`, F2/F3, and seven-remainder branches remain unpaid.

No full BT4 proof and no novelty claim are made. Every cycle displayed above is a genuinely directed cycle in the original digraph, and every disjointness statement is explicit. The graph is not modified, so the exact seven-outdegree hypothesis is preserved throughout.
