SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-23T12:32:14Z.
attacking: extremal-product skeleton-or-spread closure through an aggregate two-hub bordered-volume random cut.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T123214Z-fleet03-B13-qform-r26`  
Status: worked partial derivation; full QFORM still OPEN.

Fix two original hub coordinates `U={u1,u2}` and a disjoint leaf set `T`. For `j in T`, write

`b_l=(A_{l,u1},A_{l,u2}) in R^2` for `l in T\{j}`,

`B_j` for the `(T\{j}) x 2` matrix with rows `b_l^T`, and

`c_j=(A_{l,j})_{l in T\{j}}`.

Define the leave-one-out bordered three-volume

`Z_j = det([B_j,c_j]^T [B_j,c_j])`

and `Z_* = sum_j Z_j`.

By Cauchy--Binet,

`Z_j = sum_{S subset T\{j}, |S|=3} det A[S, U union {j}]^2`.

If `G_j=B_j^T B_j` has rank two and `P_j=B_j G_j^{-1}B_j^T`, then the Gram Schur complement gives the exact Nystrom-residual identity

`Z_j = det(G_j) ||(I-P_j)c_j||_2^2`.

If `rank B_j<2`, both sides are zero. Thus `Z_*` is an aggregate, cancellation-free measure of leaf curvature not explained by the two-hub bank.

Now independently put each leaf into a row bank `R` with probability `theta` and into a column-leaf bank `C=T\R` otherwise. Define the selected disjoint-minor currency

`W(R,C)=sum_{j in C} sum_{S subset R, |S|=3} det A[S,U union {j}]^2`.

Every term in `Z_*` uses three row leaves and one distinct column leaf, hence

`E W = theta^3(1-theta) Z_*`.

The coefficient is maximized at `theta=3/4`, giving

`E W = (27/256) Z_*`.

Therefore there is a deterministic original-coordinate cut with

`W >= (27/256) Z_*`.

This is the first essential implication for this run. It turns an aggregate leave-one-out Nystrom residual into a genuine family of disjoint physical `3x3` cross minors before paying any reciprocal local minor. The next step is to combine this selected-family currency with the newest fractional-volume theorem and with the existing entropy-or-six-hub theorem, then transfer the resulting slab inequality to arbitrary cap-one laws using fleet04/B13's no-attainment purification theorem.

Sanity checks performed in the run: on a deterministic random finite matrix, Cauchy--Binet agreed with the Gram determinant to `3.6e-15`, and exact enumeration of all cuts gave `E W=(27/256)Z_*` to floating-point precision.
