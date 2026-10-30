# fleet03/B13 r22 addendum — applying the newest joint-star compiler to the extreme bi-hub witness

Status: **PROVED TARGET-RELEVANT COROLLARY / FULL QFORM OPEN**.

This addendum applies a completed peer result published during the present run:

`yspennstate/math-open-problems@f7a221e0f40362a1ccad48cf81812f2143f3cc92`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T020523Z-fleet02-B02-QFORM-auto11-c1a7e2f4/REPORT.md`, Lemma `QFORM-JOINT-STAR-BLOCK-COMPILER-v1`.

It is applied to the actual bi-hub inequality proved in this B13 run, rather than merely cited.

## 1. Input from the main B13 report

Let `M=A[I,J]` be an ORIGINAL-coordinate cross block, let

`Z=e_3(M^T M)>0`,

and fix `1/2<=r<3/4`. If an admissible product law has a slab ratio exceeding

`C_r Z^(-1/6)`, `C_r=3e/((3-4r)sqrt(2r))`,

then the main report proves that there are a physical row `h` and column `k` with volume inclusion marginals

`alpha_h>r`, `beta_k>r`.

Consequently their joint third-minor mass

`J_hk=sum_(S contains h,T contains k) det(M[S,T])^2`

obeys

`J_hk>(2r-1)Z`.                                                   (1.1)

The designated fleet04/B13 purification also gives a bounded finite-union unit-product witness for every strict slab violation, with the same matrix and hence the same hubs.

## 2. Apply the completed peer compiler

Reindex the hubs first and write

`M=[[a,u^T],[v,N]]`.

The fleet02/B02 compiler proves the exact aggregate inequality

`sqrt(J_hk)
 <= |a| sqrt(e_2(N^T N))
    + ||u||_2 ||v||_2 ||P_(v^perp) N P_(u^perp)||_F`.           (2.1)

Therefore at least one of the two terms on the right is at least `sqrt(J_hk)/2`. Combining with (1.1) gives the new quantitative consequence

`boxed: a^2 e_2(N^T N) > ((2r-1)/4) Z`                          (2.2)

or

`boxed: ||u||_2^2 ||v||_2^2
        ||P_(v^perp) N P_(u^perp)||_F^2
        > ((2r-1)/4) Z.`                                      (2.3)

This is `QFORM-EXTREME-BIHUB-RESOURCE-COMPILER-v1`.

At the useful `r=2/3` specialization, every strict violation of

`P(Q in J)/|J| <= (9sqrt(3)e/2) Z^(-1/6)`

forces one of

`boxed: a^2 e_2(N^T N) > Z/12`                                 (2.4)

or

`boxed: ||u||^2||v||^2||P_(v^perp)NP_(u^perp)||_F^2 > Z/12.`    (2.5)

Thus a high slab ratio cannot hide behind an abstract Pluecker hub: it carries one of two explicit aggregate ORIGINAL-coordinate resources.

## 3. Additional simplification inside the strict no-pivot class

In the live no-`tau`-pivot class,

`|A_hh|<tau`, `|A_kk|<tau`,
`|A_hh A_kk-a^2|<tau`.

Hence

`a^2 < tau+tau^2=tau(1+tau)`.                                  (3.1)

If branch (2.2) occurs, then

`boxed:
 e_2(N^T N)
 > ((2r-1)Z)/(4 tau(1+tau)).`                                  (3.2)

At `r=2/3`,

`boxed: e_2(N^T N) > Z/[12 tau(1+tau)].}`                       (3.3)

So the edge-driven joint-star branch of a high-density no-pivot witness automatically contains a quantitatively large **aggregate residual two-volume**; the small physical edge cannot by itself carry the third-volume hub.

The other branch (2.3) is the genuine two-star/transverse packet. It remains unpaid in full generality because the same star-bank coordinates may also carry arbitrary nonseparable within-bank quadratic curvature; the completed pure rank-one-star theorem does not permit deleting that curvature.

## 4. Infinite slab functional endpoint

For a fixed matrix/law with infinite slab functional, the main B13 theorem can be applied for every `r<3/4`. Hence the row and column volume maxima must each be at least `3/4`. The joint mass is then at least `Z/2`, and the peer compiler recovers its endpoint resources

`a^2e_2(N^TN)>=Z/8`

or

`||u||^2||v||^2||P_(v^perp)NP_(u^perp)||_F^2>=Z/8`.

For a diverging sequence of finite slab ratios with `Z` bounded below, the same endpoint is approached quantitatively by taking `r` toward `3/4` while keeping `C_r Z^(-1/6)` below the observed slab ratio.

## 5. Remaining implication

The first B13-relevant gap is now more concrete than “handle the hub case”:

* **edge/E2 branch:** turn (3.2), together with the no-pivot small edge and arbitrary same-bank curvature, into a linear small-ball estimate; or
* **two-star branch:** turn (2.3) into a dependence-safe aggregate smoother without diagonalizing random coordinates or selecting one minor.

This addendum does not claim either conversion. Full N3, full QFORM, and full continuity remain OPEN.
