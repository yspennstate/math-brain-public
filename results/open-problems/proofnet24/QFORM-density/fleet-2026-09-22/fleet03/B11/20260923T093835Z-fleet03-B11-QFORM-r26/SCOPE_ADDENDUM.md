# r26 scope addendum — interaction with the existing defect and ridge receivers

This addendum narrows the interpretation of `REPORT.md`; it does not alter the structural counterexample proved there.

## 1. Exact interaction with the preceding fleet03/B11 defect dichotomy

The preceding B11 result is

`yspennstate/math-open-problems@c157c4b54b2b34fee3a7cc05d337c2fd654a77e7`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T061800Z-fleet03-B11-QFORM-r24/REPORT.md`.

In the sign-balanced pair-PSD chamber it writes `F=uu^T-A`, with `u_i=sqrt(A_ii)`, and proves: if `s_3(A)>=s`, then either a defect STAR has `sum_j F_ij^2>=s^2/4`, or a disjoint cut has defect second exterior volume at least `s^4/32`.

For the r26 family

`A=(1-2 delta)J + delta vv^T - delta uu^T + 2 delta I`

(all physical diagonals equal one), the defect is `F=J-A`. Fix any coordinate `i`. Relative to `(u_i,v_i)`, the other sign classes have counts `n/4-1,n/4,n/4,n/4`, and the corresponding off-diagonal defect values are `2delta,4delta,0,2delta`. Therefore

`q_i := sum_{j!=i} F_ij^2
     = (n/4-1)(2delta)^2 + (n/4)(4delta)^2 + (n/4)(2delta)^2
     = (6n-4)delta^2.`

At the critical scaling `delta=n^(-1/2)`, every row satisfies

`q_i=6-4/n`.

Thus r24's collective STAR certificate sees this family at fixed scale even though every fixed-size principal/cross packet loses its second singular direction. The r26 obstruction is therefore specifically to **bounded-cardinality packet extraction**, not to the earlier STAR/CROSS-2VOL aggregation.

## 2. The large-n member of this family is already paid by the spectral-window ridge theorem

Use the completed ridge-window theorem

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

It states: if `P` is the spectral projection onto all eigenspaces with `|lambda|>=1/64` and `max_i P_ii<=1/32`, then the full quadratic form has a continuous density with

`||p_Q||_infinity <= 288 sqrt(3e)/13 <64`,

while arbitrary smaller eigenvalues of either sign are allowed.

For the r26 family with `delta=n^(-1/2)`, the residual eigenvalue is `2/sqrt(n)`. Hence for `n>16384` it lies strictly below `1/64`, while the other three eigenvalues have modulus at least one. Therefore `P` is exactly the projection onto `span{1,u,v}`. Since `1/sqrt(n)`, `u/sqrt(n)`, `v/sqrt(n)` are orthonormal sign vectors,

`P_ii = 1/n+1/n+1/n = 3/n <1/32`.

Consequently, for every `n>16384` in this family,

`||p_Q||_infinity <64`,

and the density is continuous.

So the family is **not** a new unpaid QFORM branch. It is a clean witness that one cannot demand a fixed-size local packet as the structural bridge; a nonlocal diffuse/ridge receiver can and does pay it.

## 3. Corrected scope of the structural lesson

The strongest justified conclusion from r26 is:

> No universal proof can rely on the assertion that the three-large-eigenvalue hypothesis plus balanced near-rank-one physical correlations forces a uniformly conditioned witness on a bounded number of original coordinates.

It is **not** justified to claim that high-cardinality bank aggregation is the only possible repair. The existing spectral-window theorem shows that diffuse ridge leverage is another repair.

After combining the r24 defect theorem with the ridge-window theorem, the genuinely unpaid B11 survivor remains the high-spectral-leverage balanced defect receiver: pay the STAR/CROSS-2VOL alternatives when the spectral-window projection is not diffuse, in particular the high-augmented-leverage star and collective second-volume endpoints, while preserving original-coordinate product provenance.

## 4. Partner application remains valid

The fleet04/B11 sign-frustrated theorem used in `REPORT.md` remains an actual quantitative splice. If the same near-rank-one magnitudes carry a frustrated triangle, then with `eta=4delta` and diagonal scale one,

`||p_Q||_infinity <= 6 sqrt(pi)/(1-8delta)`.

For `delta<=1/128`, this is less than `11.344`. Thus sign frustration is paid uniformly; the r26 witness isolates the balanced-sign local-packet failure.

## 5. Rank-two control

The opposite-sign rank-two control remains

`p_(2XY)(t)=log(1/(2|t|))`

for independent `X,Y~Uniform[-1/2,1/2]`. In the r26 family, the third direction is globally spread: it is visible in the `u,v` bank contrasts and in the diffuse spectral projection, while disappearing from every bounded-cardinality block. This is precisely why a nonlocal receiver is needed.
