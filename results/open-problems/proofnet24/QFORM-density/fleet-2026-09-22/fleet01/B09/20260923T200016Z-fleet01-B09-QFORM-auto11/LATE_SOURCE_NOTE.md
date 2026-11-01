# Late-source reconciliation — newest completed fleet02/B09 result

After `REPORT.md` was committed, a fresh listing showed a newer **completed** designated partner result than the r19 report used in Section 7:

`yspennstate/math-open-problems@9e1e4143471b51c63460be8d1f536c3da0b4d8c5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T195612Z-fleet02-B09-QFORM-r20/REPORT.md`,

theorem `QFORM-STRONG3-WEAK4-ROBUST-CROSS-v1`.

This note supersedes only the phrases “newest completed designated partner” and the required partner application in Sections 1 and 7 of `REPORT.md`. The r19 inequality there remains valid mathematics and supporting input.

## Actual inequality from the newest completed partner theorem

Let `N=4096`. On an N-coordinate original source bank take four normalized Walsh vectors `z_0,z_1,z_2,z_3`. Add a disjoint literal physical coordinate `h`. Put

`R=[z_1,z_2,z_3]`,
`K=diag(1,1,-1)`,
`w=(sqrt(3)/2)e_h+(1/2)z_0`,

and for

`mu=sqrt(7)/384`

define

`A_mu=R K R^T+mu w w^T`.

The nonzero spectrum is exactly

`{1,1,-1,mu}`,

so this is target-valid. The partner theorem has strong-carrier scale `gamma=1`, and

`|mu|=sqrt(7)/384 < sqrt(7)/192 = kappa_0 gamma`.

Its only unpaid alternative would be a unit `u in R^3` and a set `H` of at most 576 ORIGINAL coordinates such that

`||(Ru)_H||^2>3/4`.

That alternative is impossible here. The hub coordinate contributes zero to `Ru`; every leaf row of the three-column Walsh frame has squared norm `3/N`, so by Cauchy--Schwarz

`||(Ru)_H||^2
 <=576*(3/4096)
 =1728/4096
 =0.421875
 <3/4`.

Therefore the partner's paid alternative necessarily holds, giving the concrete target inequality

`boxed:
 ||p_(X^T A_mu X)||_infinity
 <=88.453516030135...<88.454,`

and

`boxed:
 P{X^T A_mu X in L}<88.454 |L|`

for every interval `L`. The density is continuous.

The weak fourth term is not source-diagonal:

`mu(w^T X)^2`

contains the literal hub-leaf coupling `mu*(sqrt(3)/2) X_h <z_0,X>` and a dense leaf square, so this is a genuine bilinear/source-coordinate application rather than a separable control.

## Relation to this run's new theorem

The partner r20 theorem gives a **fork**: weak-fourth smoothing or localization of one of the three strong directions on at most 576 original coordinates. This run's `QFORM-TOP3-BALANCE-WEAK-FOURTH-v1` gives a complementary quantitative receiver when the strong-three frame itself has `q_3<1/3`, and its residual-stable theorem also keeps an additional nonzero operator-norm residual inside the actual cross block. Thus the two results fit cleanly: partner r20 identifies genuine strong localization as the remaining weak-fourth obstruction, while this run pays the balanced/residual-stable side with no row-volume-marginal gate.

Full QFORM remains OPEN.