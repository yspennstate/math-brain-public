# Fresh splice: global E2 disjointness closes the non-hub part of the B06 rank-two tube

This addendum is part of account03/B06 run `20260923T055008Z-account03-B06-qform-r27`. It uses a theorem completed after the main r27 report was drafted and does not alter the report's earlier claims.

## 1. Fresh source

Account01/B04 proved `QFORM-DISJOINT-E2-ENTROPY-HALVING-v1` in

`yspennstate/math-open-problems@e0f6866f77e8c38b5c482acaf55094f60d3f28ac`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T055035Z-account01-B04-QFORM-auto13/REPORT.md`.

For any ORIGINAL-coordinate cross block `B`, put

`Z2=e2(B^T B)=sum_(|S|=|T|=2) det(B[S,T])^2`.

Let `mu` be the determinant-squared row-pair marginal and let

`delta2=P(S cap S'=empty)`, `S,S' iid~mu`.

The theorem gives, for a genuine untouched original-coordinate square coefficient `a!=0`,

`||p_Q||_infinity
 <=4sqrt(2e)|a|^(-1/2) Z2^(-1/8) delta2^(-1/16)`                    (1.1)

whenever `delta2>0`. Its exact identity, valid also as a structural statement when `delta2=0`, is

`delta2=E_(S~mu)[ e2(B[S^c,J]^T B[S^c,J])/Z2 ]`.                    (1.2)

Thus small disjointness is not an analytic failure with no information: it means some determinant-weighted physical row pair destroys almost all residual two-volume when deleted.

## 2. Apply it to the live B06 transverse/rank-two tube

In the B06 transverse chamber inherited by r25/r27, the retained residual cross singular values satisfy

`s1 s2 > (4/5) G^2`.

Therefore

`Z2 >= s1^2 s2^2 > (16/25) G^4`.                                  (2.1)

Substituting (2.1) into (1.1) gives

`||p_Q||_infinity
 < 4sqrt(2e)(25/16)^(1/8)
   delta2^(-1/16)/sqrt(|a|G).`                                    (2.2)

The dimension-free coefficient before the disjointness penalty is

`4sqrt(2e)(25/16)^(1/8)=9.86165337086...`.

Choose the concrete collar

`delta2 >= 1/256`.

Since `(1/256)^(-1/16)=sqrt(2)`, equation (2.2) yields

`boxed:
 delta2>=1/256
 => ||p_Q||_infinity <13.947/sqrt(|a|G).
`                                                                        (2.3)

This payment retains every nonzero cross singular direction and sums all physical `2x2` curvature before inversion.

## 3. Failure is a quantitative two-row hub certificate

If the paid branch (2.3) fails because

`delta2<1/256`,

then (1.2) gives an actual physical row pair `S={i,j}` with

`boxed:
 e2(B[S^c,J]^T B[S^c,J]) < Z2/256.
`                                                                        (3.1)

Equivalently, under the canonical determinant-squared two-volume law, more than `255/256` of the row-pair mass intersects the two-vertex hub `{i,j}`. No claim is made that the single minor on `{i,j}` is large. This is exactly the aggregate-before-reciprocal form required by the live `QFORM-COHEAVY-SINGLE-ROW-EXTRACTION-FALSE-v1` correction.

Transposing gives the same dichotomy for physical column pairs. Hence the surviving low-third-volume / near-rank-two B06 chamber is further reduced:

* either determinant-weighted row-pair disjointness is at least `1/256`, and the actual outer square closes it with (2.3); or
* two physical rows capture all but `<1/256` of the complementary two-volume, and similarly on the column side after the transposed test.

The next structural problem is therefore a **two-row/two-column hub packet**, not an arbitrary diffuse rank-two tube. One must pay that grouped hub without selecting a single local minor and, in the global proof, still remove the factor `|a|^(-1/2)` in the zero/near-zero scalar-pivot branch.

## 4. Status

This addendum is a source-valid application of the fresh account01/B04 theorem to the exact B06 transverse scale. It proves a new paid-or-hub dichotomy, not the full QFORM conjecture. Essential boundedness is obtained in the paid outer-square branch; continuity is not claimed there.
