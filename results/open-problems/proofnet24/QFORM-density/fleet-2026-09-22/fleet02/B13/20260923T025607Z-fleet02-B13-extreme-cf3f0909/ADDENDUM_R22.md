# fleet02/B13 addendum — latest partner bi-hub structure plus anchored-four-volume obstruction

Status: PROVED TARGET-RELEVANT COMBINED OBSTRUCTION / FULL QFORM OPEN.

After the main report was written, the designated partner fleet03/B13 published a newer compatible result:

`yspennstate/math-open-problems@9710c3a91faa5a346fcbc214fe917e6bb12d2f1b`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T023454Z-fleet03-B13-qform-r22/REPORT.md`
and `ADDENDUM_JOINT_STAR.md`.

I apply it here to the scalar/anchored-four-volume theorem of the present run.

## 1. Two simultaneous necessary conditions for a large slab ratio

Let

`R = P(Q in J0)/|J0|`

for an admissible cap-one product law and a nondegenerate interval `J0`.

The main report proves that for every original coordinate `i` with `A_ii!=0` and every pair of disjoint sets `I,J` in its complement, if

`W_i(I,J)=sum det A[{i} union S,{i} union T]^2`

over `|S|=|T|=3`, then

`R < 20.870 [|A_ii|^4 W_i(I,J)]^(-1/12)` whenever `W_i(I,J)>0`.

Therefore every witness with ratio `R` necessarily satisfies

`boxed: |A_ii|^4 W_i(I,J) < (20.870/R)^12`                    (1.1)

for every such nonzero scalar pivot and anchored cut.

Now fix any disjoint physical cross block `M=A[K,L]` with

`Z=e_3(M^T M)>0`.

The partner r22 theorem says, at the useful choice `r=2/3`, either

`R <= C_3 Z^(-1/6),   C_3=9sqrt(3)e/2=21.1869100628...`,       (1.2)

or there are one physical row hub `h in K` and one physical column hub `k in L` whose third-volume inclusion marginals exceed `2/3`, hence whose joint third-minor mass obeys

`J_hk>Z/3`.                                                     (1.3)

Consequently, whenever

`R > C_3 Z^(-1/6)`,                                             (1.4)

the same witness simultaneously satisfies the bi-hub conclusion (1.3) and every anchored-four-volume smallness constraint (1.1).

This is `QFORM-EXTREME-BIHUB-ANCHORED4-OBSTRUCTION-v1`.

## 2. Insert the partner's joint-star compiler

The r22 addendum applies the completed fleet02/B02 joint-star block compiler. Reindex the hub row/column and write

`M=[[a,u^T],[v,N]]`.

From `J_hk>Z/3`, one of the following must hold:

`boxed: a^2 e_2(N^T N)>Z/12`                                  (2.1)

or

`boxed: ||u||^2 ||v||^2 ||P_(v^perp) N P_(u^perp)||_F^2>Z/12.` (2.2)

Inside the strict no-`tau`-pivot class, the same source gives

`a^2<tau(1+tau)`,

so the edge branch (2.1) strengthens to

`boxed: e_2(N^T N)>Z/[12 tau(1+tau)].}`                        (2.3)

Thus a large-ratio survivor with substantial cross three-volume is squeezed between two opposite kinds of matrix information:

* it has a quantitatively strong aggregate edge/E2 or two-star transverse resource, from (2.1)-(2.3); but
* every scalar-pivot anchored four-volume currency is quantitatively tiny at the scale (20.870/R)^12, from (1.1).

This excludes the possibility that the remaining bi-hub obstruction is merely an overlooked strong scalar Schur remainder. If a hub coordinate, or any other nonzero diagonal coordinate, carried a quantitatively nontrivial anchored four-volume, the present run's scalar glue would already provide a linear slab bound.

## 3. Extreme-product transfer remains exact

The partner r22 theorem also records the no-attainment finite-mixture purification: every strict slab violation admits a witness whose marginals are indicators of bounded finite unions of intervals of total measure one, with the same matrix and the same hub/volume geometry. Therefore the combined obstruction above can be studied entirely inside that finite-grid product-indicator class without assuming an attained global bathtub optimizer, a single interval, bounded support diameter, or bounded fragment count.

The anchored-four-volume restriction is matrix-only, so it survives this witness extraction unchanged.

## 4. Updated first unpaid implication

The first B13-relevant unpaid implication is now more precise:

`QFORM-BIHUB-RESOURCE-WITHOUT-ANCHORED4-v1` — in the strict no-pivot class, prove a dimension-free linear small-ball estimate for a bi-hub cross block satisfying either the edge/E2 resource (2.3) or the two-star resource (2.2), under the simultaneous absence of every quantitative scalar anchored-four-volume exit (1.1); or construct a genuine bounded-finite-union product-indicator counterexample sequence in this intersection class.

The key requirement is to use the aggregate E2/two-star resource before reciprocal minor selection and without diagonalizing random coordinates or deleting arbitrary same-bank curvature. Full N3, full QFORM and full continuity remain OPEN.
