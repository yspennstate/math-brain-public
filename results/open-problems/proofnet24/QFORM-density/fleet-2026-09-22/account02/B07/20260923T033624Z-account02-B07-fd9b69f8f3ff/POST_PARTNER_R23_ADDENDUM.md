# Post-report partner application: rank-3/4 biheavy core to actual physical edge/E2

A newer designated-partner result appeared after `REPORT.md` was committed: account03/B07 r23,

`yspennstate/math-open-problems@e24329a6a315b96a87b3efc608473ef0554f3b8d`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T033734Z-account03-B07-qform-r23/REPORT.md`.

Its Lemma `QFORM-PHYSICAL-ROWCOL-EDGE-OR-E2-v1` is general matrix algebra and is compatible with the new rank-3/4 survivor in this run. Applying it gives a strictly more physical endpoint than the original report.

## 1. Transfer the new singular-core heaviness back to the actual matrix

In `QFORM-T4-D5-OR-RANK34-BIHEAVY-v1`, the unpaid branch gives a top-`r` singular truncation `M_r`, `r in {3,4}`, and physical row/column coordinates `i,a` such that

`||e_i^T M_r||, ||M_r e_a|| > a0/(16sqrt(2))`,                 (1.1)

where

`a0=theta F/sqrt(12)`, `F=||M||_F`.                            (1.2)

Because `M_r` and `M-M_r` use disjoint singular directions, their physical row vectors are orthogonal on the right and their physical column vectors are orthogonal on the left. Hence for the ACTUAL cross block `M`,

`alpha:=||e_i^T M|| >=||e_i^T M_r||`,
`beta :=||M e_a|| >=||M_r e_a||`.                              (1.3)

Therefore

`boxed: alpha beta > a0^2/512 = theta^2 F^2/6144.`             (1.4)

No truncated coefficient is substituted into the quadratic form.

## 2. Apply the partner's actual physical row/column lemma

Permute the ACTUAL physical row `i` and column `a` to the front and write

`M=[[b,r^T],[c,D]]`.                                           (2.1)

Define the complete incident physical second-minor mass

`Z_ia=sum_{k!=i,l!=a} det M[{i,k},{a,l}]^2
     =||bD-cr^T||_F^2`.                                        (2.2)

Partner r23 proves that one of

`|b|>alpha beta/(4F)`                                          (2.3)

or simultaneously

`||r||||c|| >=(15/16)alpha beta`,
`sqrt(Z_ia)>=(11/16)alpha beta`                                (2.4)

holds. Substituting (1.4) gives the following new consequence.

### `QFORM-RANK34-BIHEAVY-TO-ACTUAL-E2-EDGE-v1`

Every unpaid rank-3/4 biheavy state from the main report has ACTUAL original coordinates `i,a` satisfying one of:

**Physical-edge branch**

`boxed: |M_ia| > theta^2 F/24576.`                             (2.5)

Since the inherited four-bank packet has `CRF>kappa`,

`boxed: C R |M_ia| > theta^2 kappa/24576.`                     (2.6)

Thus the outer two disjoint stars and one actual core edge carry a dimension-free product resource.

**Incident-E2 branch**

`boxed: ||M[i,-a]|| ||M[-i,a]|| > (5 theta^2/32768)F^2,`       (2.7)

and

`boxed: sqrt(Z_ia) > (11 theta^2/98304)F^2,`                   (2.8)

hence

`boxed: Z_ia > (121 theta^4/98304^2)F^4.`                      (2.9)

This is a complete incident second-compound bank, not a selected `2x2` minor.

## 3. Product-provenance currency on the incident-E2 branch

The two actual incident stars `r` and `c` live on disjoint original-coordinate banks. Applying the completed product-projection inequality already used source-validly by partner r23 gives

`||p_(r^T X,c^T X)||_infinity <=2/(||r||||c||)
 < 65536/(5 theta^2 F^2).`                                    (3.1)

On the present branch the large outer-star alternative failed, so `F>kappa/Lambda`; therefore

`boxed:
 ||p_(r^T X,c^T X)||_infinity
 < 65536 Lambda^2/(5 theta^2 kappa^2).
`                                                               (3.2)

This joint cap is retained only as product-linear provenance. It is not asserted to bound an arbitrary curved pushforward by itself.

## 4. Revised first unpaid implication

The main report's support-diffuse rank-3/4 survivor is now compiled further into literal physical data. The first unpaid implication becomes

`QFORM-T4-RANK34-PHYSICAL-E2-EDGE-RECEIVER-v1`:

pay either the edge-times-two-outer-stars resource (2.6), or the incident-E2-plus-two-inner-stars resource (2.7)-(2.9), while retaining arbitrary same-bank quadratic curvature and the true small but nonzero singular remainder. Bounded determinant-support portions are still paid by the previous physical-core theorem; the exact diffuse bi-anchor family remains the regression against a false bounded-cardinality core claim.

Full QFORM and global continuity remain OPEN. This addendum applies the newest designated-partner mathematics at an actual inequality; no independent review of the combined statement is claimed.
