# R06 / I0056 — idea before code: count the full-pentagon edge boundary exactly

Source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake `I0056`.

The frozen `H_{5,5}` outer-vertex interval is already `[sqrt(5),sqrt(5)]`, width zero. The still-open source clause here is the tetrapentagonal graph `T=r{4,5}=M({4,5})` with face type `[4,5,4,5]`. The current rigorous mixed-face vertex interval is

`g84 <= Phi_V(T) <= 384566/484385`,

where `g84 ~= 0.7515326907765907` is the previous bootstrap lower bound.

The preceding bootstrap used the square-face *vertex* expansion of `H_{4,5}`. A different route is available on the pentagonal side: use the exact *edge* expansion of `H_{5,4}` and count its crossing edges by pentagon incidences in the normalized multiplicity-one core.

Descriptive Section-B moves for this run are **#21 ASK WHO ELSE HAS THIS SHAPE**, **#25 COUNT THE SAME THING TWICE**, and **#30 DO ONE SCALE/DIRECTION AT A TIME**. All 30 labels have appeared somewhere in the long I0056 history, so these are not represented as globally unused; they are different from the immediate predecessor triple #18/#3/#12.

## Proposed lemma

Continue with the reduced core `D` from the preceding report: connected, induced, hole-free, minimum internal degree at least two, and every exterior boundary vertex has exactly one neighbor in `D`. Let

- `a` = selected vertices of internal degree 2;
- `b` = selected vertices of internal degree 3;
- `o` = selected degree-4 vertices incident with the unbounded face;
- `i` = selected degree-4 vertices not incident with the unbounded face;
- `F_5` = number of bounded pentagonal faces;
- `L` = length of the unbounded-face boundary walk.

The preceding exact Euler identity gives

`F_5 = E-L-4`, with `E=2a+b`.

Write

`r := L-(a+b+o) >= 0`.

Then exactly

`F_5 = a-o-r-4`.                                           (P0)

Let `A_5` be the set of full pentagons, regarded as vertices of the regular tessellation `H_{5,4}`. Every edge of `H_{5,4}` is a medial vertex of `T`. Let `x` be the number of selected medial vertices incident with exactly one full pentagon. Then

`x = |partial_E^{H_{5,4}} A_5|`.

Now count incidences `(full pentagon, selected medial vertex)` two ways. There are `5F_5` incidences. A selected medial vertex contributes 0,1,or 2 according as zero, one, or both incident pentagons are full. The vertices contributing 2 are **exactly** the `i` interior degree-4 vertices:

1. If `v` is type `i`, no incident face sector belongs to the unbounded face. Hole-freeness and inducedness therefore force every ambient face incident with `v` to be a bounded full face, so both incident pentagons are full.
2. Conversely, if both pentagons incident with `v` are full, their two opposite sectors cover all four edges at `v`, hence all four graph neighbors of `v` are selected. If either incident square were not full, its opposite square vertex would be exterior and adjacent to two selected vertices, contradicting boundary multiplicity one. Thus both squares are full as well, so `v` is not incident with the unbounded face and is type `i`.

Hence

`5F_5 = x + 2i`.                                            (P1)

By Oh's sharp edge-isoperimetric theorem (and the earlier Haggstrom-Jonasson-Lyons / Higuchi-Shirai exact regular-tessellation value),

`Phi_E(H_{5,4}) = (5-2)*sqrt(1-4/((5-2)(4-2))) = sqrt(3)`.

Therefore

`x >= sqrt(3) F_5`.

Together with (P1),

`(5-sqrt(3))F_5 >= 2i`.

Using (P0) and `r>=0` gives the clean core inequality

`(5-sqrt(3))(a-o) - 2i >= 4(5-sqrt(3))`.                  (P)

This is new relative to the previous bootstrap and, at its previous homogeneous equality proportions, (P) is violated; so it should force a strictly larger lower bound.

## Expected bootstrap

Let `k=5-sqrt(3)` and `d=2/k=(5+sqrt(3))/11`. If a global lower bound `Phi_V(T)>=g>1/2` is already known, the interior-set inequality from the previous report remains

`b+o-gi >= 0`.                                             (C_g)

Divide (P) by `k` and add `(1-G)(C_g)`, where

`G=(g+d)/(g+1)`.

Because `d+g(1-G)=G`, this gives

`a+(1-G)b-G(o+i) >= 4`.

Thus the normalized core quotient `R=(a+b)/(b+o+i)` is strictly larger than `G`. If the normalization reduction is unchanged, this should prove

`Phi_V(T)>=g  =>  Phi_V(T)>=(g+d)/(g+1)`.

The fixed point is

`g_85 = sqrt(d) = sqrt((5+sqrt(3))/11) ~= 0.7823072407116643`.

Against the retained exact upper witness `384566/484385 ~= 0.7939263189405122`, the expected certified gap is about `0.01161907822884785`, cutting roughly 72.6% of the preceding `0.042393628...` gap.

## Validation obligations before promotion

- Recheck the `j(v)=2 iff v is type i` face-sector argument carefully; it is the nontrivial local step.
- Verify Oh's normalization is exactly unnormalized edge boundary over vertex count and gives `sqrt(3)` for `(p,q)=(5,4)`.
- Verify the affine combination and fixed-point/radical comparisons exactly.
- Do not call the result exact or closed; it is a stronger lower bound for one mixed-face source-valid graph. Full Question 6.20 remains PARTIAL and independent audits are still required.