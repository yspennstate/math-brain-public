# BT4 fleet04/B05 — equality-collar capacity collapse

Run: `b05-20260922t061406z-r34`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Candidate: `BT4-HT-EQUALITY-COLLAR-ELIMINATION-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Target status: `OPEN_NOT_PROVED`

## Exact target and current source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem, so digons count.

Current-source checks used in this run:

- Bessy, Muis, Sereni, Steiner and Wiederrecht, *A relaxation of the Bermond–Thomassen conjecture*, arXiv:2608.12948 (13 August 2026): the genuine conjecture is still unresolved for every `k>=4`; their theorem allows each packed cycle either to be directed or to become directed after reversing one arc. That relaxation is not used here as a directed-cycle theorem.
- Lichiardopol, Pór and Sereni, *A Step toward the Bermond–Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979–992, DOI 10.1137/080715792: minimum outdegree five forces three vertex-disjoint directed cycles, and their strengthened two-cycle theorem allows at most two outdegree-two exceptions to minimum outdegree three.

No literature-search miss is treated as novelty evidence.

## Exact inherited mathematics consumed

I read the latest complete lead state `fleet02/B04`, run `20260922T051543Z-b04-bt4-r11`, primary scientific blob `9f1ec8ca9ab3f2737b9dddf98389826f5b926933` and controlling strengthening blob `aa71a6d910955a009b020ee77aba4a0da0052cdb`.

I also directly applied the named OTHER-account assigned partner result `fleet01/B06`, run `20260922T053614Z-fleet01-b06-bt4-r11`, candidate `BT4-HT-ALIGNED-CROSS-COLLAPSE-v1` plus its common-port strengthening, controlling scientific blob `542273320eb6f3cdf4c198fef8d6ae6a2dec435b`.

A fresh compatible exact-cage input was also read from `fleet02/B06`, candidate `BT4-HT-ARCMAX-CAGE-COLLAPSE-v2`, scientific blob `96fa9bdb0033fc6e6c3c42092e8259f882f8cd26`.

The precise inherited statements used below are restated before use. No peer outcome label is taken as proof.

## Compact conditional end-to-end argument

Assume BT4 false. The established team reduction passes to an oriented exact-outdegree-seven spanning subdigraph and chooses three disjoint directed cycles `P=(H,A,B)` minimizing total packed order and, among those, maximizing the number of arcs induced by the acyclic remainder. The genuine `k=3` theorem supplies the initial three-cycle packing. Chordlessness and the campaign's pair-deletion analysis then split into `SIX` and global `NO-SIX`.

In global `NO-SIX`, every survivor of deletion of any relevant packed pair retains at least two outneighbors: exact outdegree seven and the absence of a six-fan give this directly. The lead and partner machinery reduces the persistent four-remainder heavy-triangle branch to a rigid exact cage. In the aligned triangular-light subbranch, the assigned partner further reduces the only no-cross alternatives to two exact path-fan equality collars, indexed by a common remainder port `r1` or `r2`.

The theorem proved below eliminates **both** equality collars. Therefore, in that aligned same-heavy-`A` branch, the assigned partner's shortest-path dichotomy is forced into its genuine cross-packed output. A full BT4 proof would then follow from the remaining team debts: a genuine packed-port splice for that forced cross and for the same-heavy Hall branch, the separate `SIX` closure, and the other explicitly retained non-heavy-triangle configurations. None of those is assumed here.

The first essential local implication for this run was therefore:

> **EC-COLLAPSE.** In the exact-two-predecessor heavy-triangle cage with the forced triangular light support `A`, show that neither of the partner's no-cross equality collars
> `B->r0->r1` with `m_B(r1)=3` nor `B->r0->r1->r2` with `m_B(r2)=4`
> can occur in a BT4 counterexample.

This report proves EC-COLLAPSE.

## Exact cage and partner branch

Retain the lead's exact-two-predecessor heavy-triangle cage

`H = h0 -> h1 -> h2 -> h0`,

`R = {x,r0,r1,r2}`,

with saturation triangles

`hi -> ri -> x -> hi` for `i=0,1,2`,

and exact predecessor-chain data

`r0 -> r1,h1,x`,

`r1 -> r2,h2,x`.

The lexicographic packing exactifies the old remainder to

`r0->r1`, `r1->r2`, and `ri->x` for `i=0,1,2`,

with no `r0-r2` adjacency. It also gives

`N^+_{H∪R}(h0)={h1,r0}`,
`N^+_{H∪R}(h1)={h2,r1}`,
`N^+_{H∪R}(h2)={h0,r2}`,
`N^+_{H∪R}(r2)={x,h0}`.

In particular `h0,h1,h2,r2` are exact five-witnesses for the light pair `{A,B}`.

The lead/partner aligned branch forces

`A = p -> u -> v -> p`

to be a directed triangle, with

`p -> h0,r0,x`,
`x -> u,v`,
`h1 -> p,u,v`,
`A not-> h1`.

If `h2` is heavy on `B`, the branch is already the same-heavy Hall interface and is not treated by the collar theorem below. Thus consider the partner's remaining case, where `h2` is heavy on `A`. Since `A` is a triangle,

`h2 -> p,u,v`,

and the partner proves that `u` and `v` have one common remainder outneighbor `r_k`. That common port is heavy on `B`, and its shortest `B`-to-`r_k` path has the following exact alternatives if no earlier genuine cross-packed transition occurs:

- `k=0`: no pure-remainder route exists, so a genuine cross-packed transition is already forced;
- `k=1`: the only no-cross route is `B->r0->r1`, with `m_B(r1)=3` exactly and `r1->p`;
- `k=2`: the only no-cross route is `B->r0->r1->r2`, with `m_B(r2)=4` exactly and `r2->p`.

Here `m_B(q)=|N^+(q)∩B|`.

It remains to eliminate `k=1,2`.

## Lemma 1 — packed-cycle inport capacity

Let `B` be one of the packed chordless directed cycles in a globally minimum-total three-cycle packing, with `n=|B|`. Let `q` be a remainder vertex disjoint from the other two packed cycles. Suppose

`m_B(q) >= 2`.

Then at most one vertex of `B` sends to `q`. More precisely, if `b->q` for `b in B`, then

`m_B(q)=2`

and

`N^+(q)∩B = {b+, b++}`,

where successors are taken along the directed cycle `B`.

### Proof

For every target `c in N^+(q)∩B`, the walk

`b -> q -> c -> B[c,b]`

is a genuine directed cycle disjoint from the two untouched packed cycles. Let `d=dist_B(c,b)` be the forward distance from `c` to `b`. Its order is `d+2`. Global minimum of the three-cycle packing therefore gives

`d+2 >= n`,

hence

`d >= n-2`.                                                     (1)

Because the counterexample normal form is oriented, `q->b` is impossible when `b->q`, so the distance-zero target is absent. On a directed `n`-cycle only two vertices have forward distance to `b` at least `n-2`, namely `b+` and `b++`. Thus `m_B(q)<=2`. Since it was at least two, equality holds and the target set is exactly `{b+,b++}`. That target pair has the unique predecessor `b`, so no second vertex of `B` can send to `q`. QED.

This is a dependency statement, not an independence assumption: a two-target fan has **capacity one** for incoming packed vertices under minimum packing.

## Lemma 2 — short paths cannot feed a large fan

More generally, if a directed path from `b in B` to a remainder vertex `q` has length `L`, has no internal vertex on `B`, and `q` has `m=m_B(q)` distinct targets on `B`, then

`L >= m-1`.                                                     (2)

Indeed, closing the path through each target `c` and the segment `B[c,b]` gives a replacement cycle of order `L+dist_B(c,b)+1`. Minimum packing gives

`dist_B(c,b) >= n-L-1`.

There are only `L+1` possible distance values in `{n-L-1,...,n-1}`, so `m<=L+1`.

This recovers the exact path-fan inequality used by the partner and will be used below only for lengths one and two.

## Lemma 3 — the old sink has packed-inport capacity one

For the old remainder sink `x`, each light cycle has at most one vertex sending directly to `x`.

For `B`, if `b->x`, the inherited sink-fan equality gives

`N^+(x)∩B={b+,b++}`.

A proper consecutive two-block has one predecessor, so a second distinct `B`-inport to `x` is impossible. We use only the conclusion

`|{b in B: b->x}| <= 1`.                                      (3)

## Lemma 4 — exact light degree of r0

The cage has exactly

`N^+_{H∪R}(r0)={r1,h1,x}`.

Indeed the displayed three arcs are forced; `h0->r0` excludes `r0->h0`, the exact cage excludes `r0->h2` and `r0->r2`, and orientation handles reverse forced arcs. Since every vertex has outdegree exactly seven,

`|N^+(r0)∩(A∪B)|=4`.                                          (4)

But `p->r0`, so orientation excludes `r0->p`. As `A={p,u,v}`, `r0` has at most two targets on `A`. Consequently

`m_B(r0) >= 2`.                                                (5)

By Lemma 1, at most one vertex of `B` sends to `r0`.

This simple capacity inequality is the key new counting input.

## The k=2 equality collar is impossible

Assume the partner's `k=2` equality collar:

`B -> r0 -> r1 -> r2`,

`m_B(r2)=4`,

`r2->p`.

The displayed route has length three. If any vertex of `B` sent to `r2`, there would be a length-one `B`-to-`r2` path, contradicting Lemma 2 because `1 < 4-1`. If any vertex of `B` sent to `r1`, then appending `r1->r2` would give a length-two path to `r2`, again contradicting Lemma 2 because `2 < 3`. Hence

`B not-> r1` and `B not-> r2`.                                 (6)

Now use global `NO-SIX` for the deleted pair `H∪A`. Every `b in B` has at least two outneighbors in `B∪R`. Chordlessness of `B` supplies exactly one outneighbor inside `B`, namely `b+`. Thus every `b` must have an outneighbor in `R`.

By (6), that remainder outneighbor can only be `r0` or `x`. By Lemma 3, at most one vertex of `B` can use `x`. Therefore at least

`|B|-1`

vertices of `B` send to `r0`. But (5) and Lemma 1 say at most one vertex of `B` can send to `r0`. Hence

`|B|-1 <= 1`,

so `|B|<=2`, impossible in the oriented normal form, where every directed cycle has order at least three.

Thus the `k=2` equality collar cannot occur.

## The k=1 equality collar is impossible

Assume instead the partner's `k=1` equality collar:

`B -> r0 -> r1`,

`m_B(r1)=3`,

`r1->p`,

and `B not->r1`.                                                (7)

### Step 1: r2 cannot be heavy on B

The exact five-witness `r2` has a heavy target among `A,B`. Suppose first it is heavy on `B`, so `m_B(r2)>=3`.

If some `b in B` sent to `r2`, Lemma 2 with path length one would give `1>=m_B(r2)-1>=2`, impossible. Hence `B not->r2`.

Global `NO-SIX` for `H∪A` again forces every `b in B` to have, besides its unique successor on `B`, a remainder outneighbor. By (7) and `B not->r2`, only `r0` or `x` is available. Lemma 3 lets at most one vertex use `x`, so at least `|B|-1` vertices send to `r0`. Lemmas 1 and 4 allow at most one. Thus `|B|<=2`, contradiction.

Therefore `r2` is heavy on `A`.

### Step 2: three inport capacities force B to be a triangle

Since `A` is a triangle and `r2` is an exact five-witness, heaviness on `A` means

`N^+(r2)∩A=A`

and hence

`m_B(r2)=2`.                                                    (8)

Lemma 1 now gives

`|{b in B:b->r2}| <= 1`.                                      (9)

Let

`I0={b in B:b->r0}`,
`I2={b in B:b->r2}`,
`Ix={b in B:b->x}`.

Equation (7) says there is no `B->r1`. Global `NO-SIX` for `H∪A` therefore gives

`B subseteq I0 union I2 union Ix`.                             (10)

Lemmas 1, 3, 4 and (8) give

`|I0|<=1`, `|I2|<=1`, `|Ix|<=1`.                              (11)

Therefore `|B|<=3`. The normal form is oriented, so `|B|>=3`; hence

`|B|=3`.                                                       (12)

The equality path in (7) supplies a vertex `b0` with `b0->r0`, so `I0={b0}`. By (10)-(12), the three singleton capacities must cover all three vertices: `I0,I2,Ix` are pairwise disjoint singletons.

Write

`B=b0->b1->b2->b0`.

The remaining vertices `b1,b2` are assigned bijectively to `r2` and `x`.

Because `r0` has at least two `B`-targets and cannot target its in-neighbor `b0`, it targets exactly

`r0->b1,b2`.                                                   (13)

Because `r2` has exactly two `B`-targets, if `bj->r2` then it targets the other two vertices of the triangle. Likewise, if `bj->x`, the sink-fan equality makes `x` target the other two vertices.

There are only two cases.

#### Case A: b1->r2 and b2->x

Then (13) gives the genuine triangle

`C_B = b0 -> r0 -> b2 -> b0`.

It is disjoint from `H` and `A`. Replacing `B` by `C_B` leaves the four vertices

`{b1,r1,r2,x}`

outside the packing. They contain the directed triangle

`b1 -> r2 -> x -> b1`,

because `r2->x` is a cage arc and, since `b2->x`, the sink-fan equality makes `x` target the other two vertices `b0,b1` of the triangle `B`.

Thus

`H`, `A`, `C_B`, and `b1->r2->x->b1`

are four pairwise vertex-disjoint directed cycles, contradiction.

#### Case B: b2->r2 and b1->x

Now `r2` targets the other two vertices `b0,b1`, so

`C'_B = b2 -> r2 -> b1 -> b2`

is a genuine triangle disjoint from `H,A`. The new remainder is

`{b0,r0,r1,x}`.

It contains

`b0 -> r0 -> x -> b0`:

`b0->r0` is the equality-path inport, `r0->x` is a cage arc, and `b1->x` forces `x` to target the other two `B` vertices `b2,b0`.

Hence again we obtain four pairwise vertex-disjoint directed cycles, contradiction.

Both cases are impossible. Therefore the `k=1` equality collar cannot occur.

## Theorem — BT4-HT-EQUALITY-COLLAR-ELIMINATION-v1

In the exact-two-predecessor, four-remainder, global-`NO-SIX` heavy-triangle cage, assume the aligned light support is forced to be the triangle `A=p->u->v->p` and the partner's common-port branch has `h2` heavy on `A`. Then the two no-cross path-fan equality collars are impossible:

1. there is no `B->r0->r1` equality state with `m_B(r1)=3` and `r1->p`;
2. there is no `B->r0->r1->r2` equality state with `m_B(r2)=4` and `r2->p`.

Therefore the assigned partner's common-port shortest-routing dichotomy collapses to its **genuine cross-packed transition** output in this branch.

The proof is deterministic. It does not assume independent choices of packed ports or remainder exits. The key dependence accounting is the capacity-one statement of Lemma 1: once a remainder vertex has two targets on `B`, minimum packing permits at most one `B`-inport to it.

## Exact finite sanity check used

The hand proof above is primary. I also ran the following exact two-case check only for the final forced `|B|=3` split, to guard against a mistaken cyclic-order case distinction:

```python
# B is 0->1->2->0. 0 is the unique B-in-neighbor of r0.
for r2_in, x_in in [(1, 2), (2, 1)]:
    r0_targets = {1, 2}
    r2_targets = {0, 1, 2} - {r2_in}
    x_targets = {0, 1, 2} - {x_in}
    if r2_in == 1:
        replacement = "0-r0-2-0"
        remainder_cycle = "1-r2-x-1"
        ok = (1 in x_targets)
    else:
        replacement = "2-r2-1-2"
        remainder_cycle = "0-r0-x-0"
        ok = (0 in x_targets)
    print(r2_in, x_in, sorted(r0_targets), sorted(r2_targets),
          sorted(x_targets), replacement, remainder_cycle, ok)
```

Exact output:

```text
1 2 [1, 2] [0, 2] [0, 1] 0-r0-2-0 1-r2-x-1 True
2 1 [1, 2] [0, 1] [0, 2] 2-r2-1-2 0-r0-x-0 True
```

This check is auxiliary verification of the displayed two cases, not evidence for BT4 by itself.

## What changed and what remains unpaid

Before this run, the named partner's common-port theorem left two exact no-cross equality collars as live neutral-exchange objects. After this run, both are impossible. Thus the aligned same-heavy-`A` triangular branch must produce a genuine cross-packed transition.

The first remaining local implication is now `HT-CROSS-HALL-SPLICE`:

- in the same-heavy-`A` triangular branch, splice the now-compulsory genuine `B`-to-`H/A` cross with the lead's x-free heavy-fan escape/reciprocal interfaces;
- in the alternative same-heavy-`B` branch, close the Hall distinct-port/common-extra-port object together with the fourth-witness return;
- in either case, obtain two vertex-disjoint replacement cycles, a strict lexicographic decrease, a directed cycle in an exchanged remainder, a `SIX` exit, or a fourth disjoint directed cycle.

Separate campaign debts remain: the global `SIX` closure, the triangular F2/F3 witness-cover splice, and the seven-remainder triangle-pinwheel/support-carried omitted-sink branch. I do not replace any of those unpaid conditions by a renamed unsupported assertion.

## Failure checks and nonclaims

- The proof uses genuine directed cycles only.
- It uses the exact outdegree-seven, oriented, globally minimum packing normal form; it is not claimed for arbitrary nonminimal three-packings.
- `global NO-SIX` is used only to guarantee two residual outneighbors after deleting a packed pair.
- The path-fan inequalities are proved in Lemmas 1–2, not imported as a heuristic.
- The equality-collar elimination is a local branch theorem, not a proof of BT4.
- No nearly-directed cycle, edge-disjoint surrogate, bounded-order census, or peer PASS label is promoted to target-level evidence.
- No novelty claim is made.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

The two exact equality collars left by the assigned partner are eliminated, and the aligned common-port branch is forced into its genuine cross-packed transition output. Full BT4 remains open.
