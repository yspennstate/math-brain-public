SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T08:33:05Z.
attacking: N3 coordinate-minor aggregation — use the designated partner's rank-3/4 core alternative together with the no-pivot entry cap, and collapse a four-hub determinant ledger to a diffuse transverse-star survivor.

# Early substantive checkpoint

Full QFORM remains open. This checkpoint records the first new calculation before the final argument.

## 1. N3 gives an entrywise cap in original coordinates

Fix a no-pivot threshold `tau in (0,1]` in the already-proved N3 reduction: `|A_ii|<tau` and `|det A[{i,j},{i,j}]|<tau` for every physical pair. Then for `i != j`,

`A_ij^2 = A_ii A_jj - det A[{i,j},{i,j}]`,

hence

`|A_ij|^2 < tau^2+tau`.

Thus every entry of every original-coordinate cross block obeys

`|A_ij| <= delta_tau := sqrt(tau+tau^2)`.

This is a deterministic consequence of N3, not a small-random-perturbation assertion.

## 2. Tunable version of the designated partner's D5/rank-4 compression

Use account02/B07's completed compound-tail lemma at

`yspennstate/math-open-problems@67a5863d5e97c6b27499ccf7690d6008965f62c3`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T033624Z-account02-B07-fd9b69f8f3ff/REPORT.md`.

For the partner packet, `F=||M||_F`, `T2>=theta F^2`, and

`E3(M)>=(theta^2/6)F^6`.

The partner identity gives

`E5 >= (T4^2/20) E3`,

so if `E5 < eta F^10`,

`T4/F^2 < sqrt(120 eta/theta^2)`.

Let `epsilon in (0,1/64]` and choose

`eta_epsilon := epsilon^4 theta^6/17280`.

Then failure of the fifth-volume receiver implies

`T4/F^2 < epsilon^2 theta^2/12`.

With `a:=theta F/sqrt(12)`, this gives

`s5(M) <= sqrt(T4) < epsilon a`.

The same top-four E3 retention estimate used in the partner proof remains valid at this smaller tail scale and gives `s3(M)>=a`.

Hence split:

- if `s4(M)<=4 epsilon a`, take `M0=M3`; then `||M-M0||op<=4 epsilon a<=a/16`;
- if `s4(M)>4 epsilon a`, take `M0=M4`; then `||M-M0||op<epsilon a<=s3(M0)/16`.

Applying the required current volume-stability theorem `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba` to either left or right range projection, every case with a diffuse range projection is already continuously density-paid. Therefore an unpaid case has a physical heavy row and heavy column on both retained range projections.

In the rank-three survivor, actual (not truncated) physical row/column star norms satisfy

`||row_i(M)||, ||col_j(M)|| > a(1/sqrt(2)-4 epsilon)`.

In the rank-four survivor they satisfy

`||row_i(M)||, ||col_j(M)|| > epsilon a(2sqrt(2)-1)`.

The last inequalities follow by subtracting the operator tail from the heavy-row norm of the singular core. Combining with the N3 entry cap turns those stars into quantitatively diffuse original-coordinate stars rather than merely algebraically heavy singular-vector rows.

## 3. Concrete universal scale

On the inherited four-bank packet, failure of the large-star branch gives `F>kappa/Lambda`, where `kappa=1/(256 sqrt(3))`. Thus

`a >= a0 := theta kappa/(sqrt(12) Lambda)`.

At the standard `theta=1/16`, `Lambda=1`, `epsilon=1/64`,

`a0 = 4.069010416666667e-5`,

and every rank-four unpaid survivor has an actual row and column star of norm greater than

`(2sqrt(2)-1) epsilon a0 = 1.162482658860646e-6`.

For a sufficiently small fixed N3 threshold, the coordinatewise cap `delta_tau` is therefore a fixed small fraction of each such star norm. The final report will state the exact fixed threshold and also apply the same N3 entry cap to the newest four-hub E2 motif ledger.

Status: supporting structural progress only; no claim that the final diffuse-star curvature receiver is already proved.
