# Strengthening — the consecutive heavy-fan lock collapses to a light triangle

Run: `20260922T051543Z-b04-bt4-r11`  
Controls: same as the immutable primary report.  
Outcome remains: `ESSENTIAL_STEP_APPLIED`.  
Brain status remains: `WITHOUT_VERIFIED_BRAIN`.

This addendum strengthens Lemma 3.1 of the primary report at commit `07e6d15d1504e1d11d588ee8b637e9b4710a3d7a`, Git blob `9f1ec8ca9ab3f2737b9dddf98389826f5b926933`. The primary report's statements remain valid; this addendum is controlling for its exact-consecutive-triple alternative.

## Setup

Retain the exact-two-predecessor heavy-triangle cage

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

and the saturation triangles `Ti=hi->ri->x->hi`.

The primary report proved that the old remainder is the exact chain

`r0->r1->r2`, with `ri->x` for all `i`,

and that a light three-hit witness for `T0` has

`p in A`, `p->h0,r0,x`, and `N+(x) intersect A={p+,p++}`.

Assume `h1` is heavy on the same light support `A`. Lemma 3.1 gave the dichotomy:

- a clean opposite `A<->B` cross pair with four distinct packed ports and disjoint remainder interiors; or
- the exact consecutive fan lock
  `N+(h1) intersect A={p,p+,p++}`.

## New lemma — the fan lock forces `A` itself to be a directed triangle

Assume the exact consecutive fan lock. Then `h1->p`.

Together with the light witness arc `p->h0` and the heavy-triangle arc `h0->h1`, this gives the genuine directed triangle

`C = p -> h0 -> h1 -> p`.

The saturation triangle

`T2 = h2 -> r2 -> x -> h2`

is vertex-disjoint from `C`: `C` uses only `p,h0,h1`, while `T2` uses `h2,r2,x`. Both are disjoint from the other light packed cycle `B`.

Hence

`C, T2, B`

are three pairwise vertex-disjoint directed cycles of total order

`3 + 3 + |B|`.

The original globally minimum packing `(H,A,B)` has total order

`3 + |A| + |B|`.

Global minimum therefore gives

`3+|A|+|B| <= 6+|B|`,

so `|A|<=3`.

The counterexample is oriented, so every directed cycle has order at least three. Therefore

`|A|=3`.

QED.

## Strengthened aligned-port alternative

Whenever the `T0` light witness lies on the heavy target of `h1`, exactly one of the following holds:

1. there is a clean opposite light-cross pair with four distinct packed ports and disjoint remainder interiors; or
2. that heavy light support is a directed triangle.

Thus the aligned branch has **no long-support consecutive-fan lock**. The only packed obstruction left after the clean-cross alternative is a short light triangle. In the nonaligned branch the `T0` witness remains confined to the other light support and should be combined with the universal reciprocal cross / fleet03-B05 third-port mechanism.

This is still not BT4 closure. The clean pair needs a genuine two-cycle splice, and the short-light triangle must be closed together with the exact cage or routed to an already-proved branch. SIX and the seven-remainder triangle-pinwheel remain separate explicit debts.
