# PROB10-06 idea before code — impose stochastic-order monotonicity on the lower score box

Actual runtime model shown to this worker: GPT-5.6 Sol. Authenticated reasoning-effort telemetry is unavailable, so reasoning level is UNVERIFIED; GPT-6/maximum is prompt-only and is not claimed.

Parent source remains the Lyons–Pemantle–Peres speed-monotonicity conjecture for Galton–Watson trees without leaves, with P(nu=0)=0 and m=E nu>1. Child bias beta weights each child relative to the parent and larger beta pushes away from the root; parent bias lambda=1/beta is reciprocal, so the conjectured direction is increasing speed in beta on beta>1/m, equivalently decreasing speed in lambda on 0<=lambda<m.

## New route

The previous R02 report used the proved stochastic order `B | {nu=3} >=_st B | {nu=2}` only on the *upper* `h_2/c_2` score. It left the lower `h_3/c_3` score as a 5-dimensional independent interval box for conditional escape weights `Y_m`, then enumerated all 32 vertices. That discards a second consequence of the same coupling: for the four-branch term, if `Y_m=E[phi(T_m)]` conditional on exactly `m` type-3 descendants, then

`Y_0 <= Y_1 <= Y_2 <= Y_3 <= Y_4`.

The lower score envelopes `R_m^L(lambda)` are decreasing in `m` on the current strip. Therefore the worst lower weighted average is a linear-fractional optimization over a *monotone box*, not an independent box. Enforcing the order should remove spurious vertices that put a large weight on a low score while simultaneously putting a small weight on an earlier high score in a way impossible under stochastic ordering.

I will prove the finite-dimensional reduction exactly: for fixed p and lambda-envelope bounds `lo_m<=Y_m<=hi_m`, minimizing

`sum pi_m Y_m R_m / sum pi_m Y_m`

over `lo_m<=Y_m<=hi_m` and `Y_0<=...<=Y_4` occurs at a vertex of the order polytope. I will enumerate those extreme points exactly (not sample them), substitute them into the existing derivative certificate, and certify the resulting rational polynomials by Bernstein subdivision. Any endpoint gain is restricted-family PARTIAL progress only.

## Three materially different attacks this run

1. **Monotone-order polytope compression (primary):** enforce `Y_0<=...<=Y_4` in the lower `h_3/c_3` score and exact-optimize its linear-fractional objective. This attacks the current all-mixture bottleneck directly.
2. **Quantitative branch-addition ratio:** use the inverse-escape moment from the previous run to try to sharpen `3/4<=c_3/c_2<=1` quantitatively. This is independent of the lower-box geometry and may improve the p-to-theta conversion.
3. **Derivative-through-inverse-escape recursion:** test whether the new finite `E[1/B]` bound gives an L1 contraction or a finite bound on `E[(1/B)']` at lambda=2. If the natural contraction fails, record the exact obstruction rather than assume derivative control.

No code implementing the new certificate has been written or persisted before this note.