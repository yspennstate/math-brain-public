# BT4 shared handoff — heavy-triangle predecessor-splice v2

Controlling source: `proofnet24/collective-BT4/fleet02/B04/20260922T041847Z-b04-bt4-r11/strengthening.md`  
Controlling commit: `1277bd8435045651114cb6500f47674603f3f522`  
Controlling blob: `8bfc5b33fb232c8543856d6d9ad3b0e8fdc3432c`  
Primary report remains preserved at commit `71ff185ec9b372cc24c02c4630cd7c202d13eee7`, blob `596929efe56393d3ab515544fa33ec6a19e75c83`.  
Outcome: `ESSENTIAL_STEP_APPLIED`; BT4 remains open; `WITHOUT_VERIFIED_BRAIN`.

Named partner actually applied: fleet03/B05 `BT4-SC2-THIRD-PORT-v1`, report blob `2d667b4e80a54a16bfd9b551baa4cae55ddf93ae`. Its genuine-k=3 deletion lemma supplies an external three-hit witness for every directed cycle.

In the four-remainder global-`NO-SIX` heavy-triangle state

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`, `Ti=hi->ri->x->hi`,

an R-supported three-hit witness for `Ti` can only be predecessor `r_{i-1}`; a successor witness explicitly creates two disjoint cycles and hence four with `S,U`. All three predecessor relations create an R-cycle.

If exactly two predecessor relations occur, rotate to

`r0->r1,h1,x`, `r1->r2,h2,x`.

Then explicit four-cycle exclusions plus global no-six force

`N^+_{H union R}(r2)={x,h0}`,
`N^+_{H union R}(h1)={h2,r1}`,
`N^+_{H union R}(h2)={h0,r2}`.

Thus `h1,h2` are exact five-witnesses into `S union U`. For either witness `h_i`, let `A_i` be its heavy light target. **No arc from `A_i` to `h_i` can exist.** If `s->h_i`, choose a nearest fan target `y` on `A_i`; three fan targets and orientation give `dist_{A_i}(y,s)<=|A_i|-3`, so the cycle

`s->h_i->y->A_i[y,s]`

has order at most `|A_i|-1`. Together with the untouched other light cycle and the saturation triangle `T0=h0->r0->x->h0`, this is a three-cycle packing strictly smaller than `(H,S,U)`, contradiction.

Therefore heavy-fan domination escape applies separately to both `h1,h2`: the exact-two-predecessor cage forces **two genuine cross-packed transitions** ending on their heavy light targets, with R-internal interiors. No disjointness between those two crosses is claimed.

If at most one predecessor relation occurs, the remaining saturation triangles have light three-hit witnesses. Each light cycle has at most one direct inport to `x` in the fan-two state, and one light vertex cannot witness all three triangles because that would use all seven outgoing arcs on `{x,h0,h1,h2,r0,r1,r2}` and leave no support-successor arc. Hence the zero-predecessor case is a two-port light-inport cover with one unique inport on each of `S,U` and a `2+1` assignment of the three triangles; the one-predecessor case similarly uses one or both unique light inports for the two remaining triangles.

So heavy-triangle saturation now has only two live interfaces: (i) a rigid two-port light-inport cover, or (ii) the exact predecessor cage with two compulsory heavy-fan escape crosses. The next unpaid statement is a true packed-port disjointness/splice theorem combining these outputs with the universal reciprocal sink-cross and the fleet03/B05 third-port interface. A single cross or opposite pair is not counted as two replacement cycles. The separate SIX closure remains unpaid.
