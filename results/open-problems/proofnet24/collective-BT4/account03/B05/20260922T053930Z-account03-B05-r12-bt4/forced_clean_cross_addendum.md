# Addendum — the shifted-triple lock forces the clean four-port cross in the long-support case

Parent candidate: `BT4-HT-SHIFTED-TRIPLE-v1`  
Addendum candidate: `BT4-HT-FORCED-CLEAN-CROSS-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`

The parent report proved, in the lead's aligned four-remainder heavy-triangle cage, that either `|A|=3` or

`F=N+(h1) intersect A={p+,p++,p+++}`.

This addendum closes the apparent shifted-triple lock whenever `|A|>=4`.

## Lemma — domination of the third fan point must come from the other light support

Assume `|A|>=4`. Let `B` be the other light packed cycle. Then there exists `q in B` with

`q->h1` and `q->p+++`.

### Proof

Apply arc domination to the arc `h1->p+++`. Thus some vertex `q` satisfies

`q->h1,p+++`.

The lead's exact cage restrictions give the same location trichotomy used in its four-port lemma:

- `q!=x`, because the sink fan on `A` is exactly `{p+,p++}`;
- `q notin A`, because the inherited heavy-target condition is `A not->h1`;
- if `q` is in the old remainder, the only possible location is `r0`;
- if `q` is on `H`, the only possible location is `h0`;
- otherwise `q` lies on the other light cycle `B`.

The first two exceptional locations are impossible by strict packing exchanges.

If `q=r0`, then

`p -> r0 -> p+++ -> A[p+++,p]`

is a directed cycle. Since `dist_A(p,p+++)=3`, its order is `|A|-1`. It is vertex-disjoint from the old packed cycles `H` and `B`, so replacing `A` by it strictly reduces the total order of the globally minimum three-cycle packing, contradiction.

If `q=h0`, then

`p -> h0 -> p+++ -> A[p+++,p]`

is again a directed cycle of order `|A|-1`. It is disjoint from the saturation triangle

`T1=h1->r1->x->h1`

and from `B`. Thus replacing the old pair `(H,A)` by `(T1,C)` keeps three vertex-disjoint cycles and reduces total packed order by one, contradiction.

Therefore `q in B`. QED.

## Corollary — forced clean opposite-cross pair

Still assume `|A|>=4`. The arc `q->p+++` is a direct `B->A` cross. The old remainder sink `x` has exactly two outneighbors on the light support `B`; choose

`b in N+(x) intersect B`

with `b!=q`. Then

`p -> x -> b`

is an `A->B` cross. The two crosses have:

- distinct `A` ports `p` and `p+++`;
- distinct `B` ports `b` and `q`;
- disjoint remainder interiors (`{x}` and empty).

Hence the lead's clean four-port alternative is not merely optional in the aligned long-support branch: it is forced.

## Sharpened branch statement

In the aligned four-remainder heavy-triangle branch, one of the following holds:

1. `|A|=3`; or
2. there is a clean opposite pair of light-to-light crosses with four distinct packed ports and disjoint remainder interiors.

Thus the exact shifted triple is an intermediate rigidity statement, not a terminal lock. Combined with the assigned partner account04/B06 `BT4-SIX-DUAL-WALL-LIFT-v1`, the two previously different all-long obstructions now both feed the common `CROSS/BYPASS` splice frontier. The remaining target-level problem is to turn that source-valid port interface into two vertex-disjoint replacements, a strict smaller three-packing, or a fourth remainder cycle. Full BT4 remains open.

## Boundary check

When `|A|=3`, cyclically `p+++=p`; the strict `|A|-1` exchanges above are not available because the new two-edge path would close at the same port. This is a genuine short-support boundary and is not claimed closed here.
