# BT4 handoff — account04/B05 x-free Hall heavy-triangle cage

Run: `b05-20260922t051421z-r34`  
Candidate: `BT4-HT-XFREE-HALL-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Inputs actually consumed

- lead account02/B04 `20260922T041847Z-b04-bt4-r11`, primary blob `596929efe56393d3ab515544fa33ec6a19e75c83`, controlling strengthening blob `8bfc5b33fb232c8543856d6d9ad3b0e8fdc3432c`;
- account01/B04 `BT4-R4-MAX-REMAINDER-ARC-COLLAPSE-v1`, blob `b9b700749e5723c819b6643aa16c67c38db6c569`, for the legitimate secondary choice maximizing arcs in the remainder among minimum-total three-packings;
- assigned partner account01/B06 fixed-pair/Menger-collar theorem, run `20260922T013522Z-b06-bt4-r11`;
- partner account01/B06 `BT4-R4-REGENERATED-SIX-v1`, blob `11d846b6ab2c724c302087fff920987e96042888`, checked for compatibility on the separate F2 line.

## New exact step

In the lead's exact-two-predecessor four-remainder heavy-triangle cage, write

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,
`hi->ri->x->hi`,
`r0->r1,h1,x`, `r1->r2,h2,x`,
`N^+_{H∪R}(r2)={x,h0}`,
`N^+_{H∪R}(h1)={h2,r1}`,
`N^+_{H∪R}(h2)={h0,r2}`.

Choose the minimum-total packing to maximize `Phi=|A(D[R])|`.

Three optional arcs die by explicit disjoint-cycle certificates:

- `r0->r2` gives `h0-r0-r2-h0` disjoint from `h1-r1-x-h1`;
- `r0->h2` gives `r0-h2-h0-r0` disjoint from `h1-r1-x-h1`;
- `r1->h0` gives `r1-h0-h1-r1` disjoint from `h2-r2-x-h2`.

The only remaining possible extra arc, `h0->r1`, would make the neutral packing obtained by replacing `H` with `T2=h2-r2-x-h2` have six remainder arcs, whereas the original remainder has five. Maximal `Phi` therefore excludes it.

Consequently the seven-vertex cage is exact and

`d^+_{H∪R}(h0)=d^+_{H∪R}(h1)=d^+_{H∪R}(h2)=d^+_{H∪R}(r2)=2`.

Thus `h0,h1,h2,r2` are four exact five-witnesses for the fixed light pair `{S,U}`. Each `h_i` has only its H-successor and the unique R exit `r_i` inside `H∪R`.

The missing saturation triangle `T0=h0-r0-x-h0` has a light three-hit witness `w` on one light support `L`, with `w->h0,r0,x`. A direct minimum-packing surgery shows `h0` cannot be heavy on `L`; its heavy light target is the other support.

For every `h_i`, let `A_i` be a heavy light target. The sink `x` has exactly two targets on `A_i`, while `h_i` has at least three. Choose a heavy-fan target `a_i` not hit by `x`. Domination of `h_i->a_i`, combined with the exact cage and the heavy-target no-inport theorem, produces an **x-free cross transition** ending at `a_i` whose R-interior is either empty or exactly `{r_{i-1}}`. Hence the three escapes have pairwise disjoint R-interiors.

Among the three `h_i`, two have the same heavy target `A`. For such a pair, put `X=N+(x)∩A`, `|X|=2`. Then either:

1. there are distinct representatives outside `X`, giving two x-free transitions to distinct target ports with disjoint R-interiors; or
2. Hall fails, forcing the exact collision
   `N+(h_i)∩A=N+(h_j)∩A=X∪{a}`
   for one common extra port `a`; both heavy fans then have size exactly three.

Finally apply the assigned account01/B06 collar theorem to the fourth witness `r2`. Since `|R|=4`, its strict `|R|>=3m-2>=7` branch is impossible. Thus it yields either another genuine packed cross or a neutral equality path; in the equality case the path avoids sink `x`, and appending `r2->h0` gives an x-free light-to-H return.

## First unpaid implication

`HT-PORT-CLOSE`: combine either the distinct-port x-free same-heavy pair, or the exact common-extra-port collision, with the partner cross/equality return to force a legal two-cycle splice, strict lexicographic packing reduction, exchanged-remainder cycle, SIX witness, or fourth disjoint directed cycle.

Remainder-interior disjointness and the fan-choice dependence are now paid; packed support order/collision is the remaining local obstruction. Separate campaign SIX and other SC+ configurations remain open.

No full BT4 proof or novelty claim is made.
