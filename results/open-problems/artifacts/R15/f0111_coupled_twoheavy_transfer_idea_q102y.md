# R15 idea note — coupled two-heavy transfer reduction for the last F0111 cells

Date: 2026-09-20 UTC.  
Status: IDEA BEFORE VALIDATION / SELF_CHECK_ONLY / NOT CLAIMED.

The native Burdzy--Scheutzow Problem 7.2 / I0076 target remains at its mandatory retired handoff with no surviving frozen counterexample candidate. This note concerns only the already-retained PENDING F0111/Talagrand `k=2` screen and does not admit or claim that source.

The preceding report `runs/R15/20260920_0656Z_successor_screen_f0111_complement_energy_p101x.md` reduced the last dimension-30 full-support two-level Hessian-null cells `N=12,13` to a coefficient-free complement-energy gate, but left a high-dimensional optimization over the `J` contact masses. The present route attacks that remaining optimization rather than adding another generic entropy bound.

## 1. Reuse the exact complement-face inequality at one ray

For a hypothetical contact, let `u_i=e^{q_i}` on `J`, let `M=30-N`, and let

`E_JJ = sum_{i<j in J} B_ij q_i q_j`,  `E_KK = sum_{i<j in K} B_ij q_i q_j`.

The previous exact identity gives, for every `t>1`,

`E_KK + (t-1) E_JJ >= log S - sum_{j in K} r_j q_j - (1/t) log(sum_{i in J} u_i^t -(M-1))`.

Here the `sum_J q_i` terms cancel exactly. This form separates the complementary `K` entropy moment and a convex power sum over `J`.

## 2. Scalar upper bound for the total J--J coefficient mass

The residual Gram representation also controls the unweighted aggregate J--J pair coefficient mass. If

`T = ||sum_{j in K} w_j||^2 <= Tcap = y(N-L_K)`, 

then summing the Gram identity over `J` gives

`U_J := sum_{i<j in J} B_ij = 1/2 [ (b/a)^2 T - x + A_J x^2 ]`.

Therefore

`U_J <= Umax := 1/2 [ (b/a)^2 Tcap - x + A_J x^2 ]`.

Since all `B_ij>=0`,

`E_JJ <= Umax q_(1) q_(2)`,

where `q_(1)>=q_(2)` are the two largest `J` coordinates.

This cap is cruder than the preceding GRAMCAP in one respect, but it couples extremely cleanly to the same two coordinates that maximize the convex face power sum.

## 3. Couple the two adversarial terms before maximizing

Let

`H_t(u_1,...,u_M) = (1/t) log(sum_i u_i^t -(M-1)) + (t-1) Umax log u_(1) log u_(2)`.

The contact constraints give

`u_i >= 1`,

`sum_i u_i = S x`,

and the projective/heavy caps give an explicit scalar upper bound `u_i<=u_cap`.

The key proposed reduction is a mass-transfer monotonicity statement:

> For `t>1`, if a third coordinate `u_3>1` and either of the two largest coordinates has room below `u_cap`, moving a small amount of mass from `u_3` to that larger coordinate does not decrease `H_t`.

Reason: `u -> u^t` is strictly convex, so transferring mass from a smaller coordinate to a larger one increases the power sum. The product `log u_(1) log u_(2)` is unchanged if mass is transferred to `u_(1)` with `u_(2)` fixed, and increases when the first coordinate is capped and transfer is made to `u_(2)`. Iterating leaves at most two coordinates above the lower bound 1, except for saturation forced by `u_cap`.

Thus the high-dimensional worst case should reduce exactly to a one-variable problem. Put

`T2 = S x -(M-2)`.

Then every extremizer of the coupled relaxation is represented by

`u_1+u_2=T2`,

`1<=u_1,u_2<=u_cap`,

and all remaining `J` coordinates equal 1. The adversarial term becomes

`h_t(u) = (1/t) log(u^t+(T2-u)^t-1) + (t-1) Umax log u log(T2-u)`

on the explicit interval

`max(1,T2-u_cap) <= u <= min(u_cap,T2-1)`.

This is the main new route: the last arbitrary-heterogeneity `J` optimization collapses from dimension 17 or 18 to one scalar.

## 4. K-side convex extremizer

Likewise, with `v_j=e^{q_j}>=1`, fixed sum `sum_K v_j=U_K=N+eta_K`, and the residual coordinate cap `v_j<=S/A_K=(N+eta_K)/L_K`, the quantity

`sum_{j in K} r_j q_j = (1/S) sum_j v_j log v_j`

is maximized by convex concentration: fill as many coordinates as possible to the cap, then one residual coordinate, with all remaining coordinates equal to 1. This removes the K-distribution as well.

The preceding complement-energy inequality can therefore be tested using only the scalar null parameters `(delta,s)`, one `J` split variable `u`, and one ray parameter `t`.

## 5. What must be validated next

1. Prove the mass-transfer lemma with all cap/order boundary cases, not just at smooth interior points.
2. Derive the exact K-side capped-convex formula.
3. Scan the exact scalar feasible bands for `N=12,13` only as a route finder; numerical samples are not proof.
4. If a simple fixed or scalar-dependent ray `t` leaves a uniform signed margin after the exact reductions, replace the scan by exact rational/interval or Bernstein certification and archive its output.
5. Do not declare either cell eliminated unless the full scalar bands and all cap cases are certified.

Section-B moves for this route: **#13 FIND WHAT ONLY INCREASES** (mass-transfer monovariant), **#24 FIND THE EXTREMAL OBJECT** (capped two-heavy extremizer), **#30 DO ONE SCALE/DIRECTION AT A TIME** (one face ray and one remaining scalar split).
