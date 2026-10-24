# R15 idea note — adaptive-ray monotonicity for the last two-heavy F0111 cells

Date: 2026-09-20 UTC.  
Status: IDEA BEFORE REPOSITORY CHECKER / SELF_CHECK_ONLY / NOT CLAIMED.

The native Burdzy--Scheutzow Problem 7.2 / I0076 target remains at its mandatory retired handoff with no surviving frozen counterexample candidate. This note concerns only the retained PENDING F0111/Talagrand `k=2` screen and does not admit, claim, or reopen that source.

The immediately preceding report `runs/R15/20260920_0754Z_successor_screen_f0111_twoheavy_extremal_q102y.md` reduces the last dimension-30 full-support two-level Hessian-null cells `N=12,13` to a capped two-heavy `J` profile plus an explicit capped-convex `K` extreme point. The remaining `J` optimization is one scalar split. This route tries to remove that scalar too.

## Adaptive face ray

Use the exact complement-face inequality at the ray

` t = 1 + epsilon,   epsilon = c / log S,   c = 7/100, `

where `S=-29/k` is the exact contact normalization. Then `S^epsilon=e^c`, uniformly across both cells. For a two-heavy `J` profile write

`u+v=T_2`, `u>=v>=1`,

and

`H(u)= (1/t) log(u^t+v^t-1) + epsilon U_max log(u)log(v)`.

Differentiation gives

`H'(u)=(u^epsilon-v^epsilon)/(u^(1+epsilon)+v^(1+epsilon)-1)
       + epsilon U_max( log(v)/u - log(u)/v ).`

Since `x^(epsilon-1)>=1/x` for `x>=1`,

`u^epsilon-v^epsilon >= epsilon log(u/v)`.

Since `u,v<=S` and `S^epsilon=e^c`,

`u^(1+epsilon)+v^(1+epsilon)-1 <= e^c(u+v)`.

Thus `H'(u)>0` follows from

`R(u,v):= uv log(u/v)/[(u+v)(u log u-v log v)] > e^c U_max`.

The carried exact cell bounds should make this uniform. The prior certificate gives `U_max<9s/8`, `S<20/s`, `x<41/40`, `s<3/200`, and the heavy caps `r_*<1-15s` for `N=12`, `r_*<1-17s` for `N=13`. At the two-heavy endpoint the smaller coordinate obeys

`v >= S(x-1+C_N s)-(M-2) > 250`,

so `u/v < (2/25)/s`.

Split by `r=u/v`.

* If `1<=r<=e`, the mean value theorem and `log r >= (r-1)/r` give

  `R >= 1/[(r+1)(log u+1)] > 1/[4(log S+1)].`

  With `S<20/s`, `s<3/200`, and the carried exact bound `log(4000/3)<36/5`, this exceeds `(121/100)s`.

* If `r>=e`, then `u log u-v log v<=u log u`, hence

  `R >= [log r/(r+1)]/log S`.

  The function `log r/(r+1)` is unimodal, so on `e<=r<2/(25s)` its minimum is attained at an endpoint. The `r=e` endpoint is handled above. At `r=2/(25s)`, the ratio is bigger than `(40/19)s` once

  `(2/25)^5 > 20(3/200)^4`.

Finally, if `e^(7/100)<43/40`, then

`e^c U_max < (43/40)(9/8)s < (121/100)s`.

Therefore `H'(u)>0` throughout the ordered feasible split interval. The `J` extremizer is forced all the way to the heavy cap:

`u_1=S(1-C_Ns)`,
`u_2=S(x-1+C_Ns)-(M-2)`,
`u_3=...=u_M=1` (in the closure).

This would eliminate the last contact-distribution degree of freedom on `J`. Together with the exact capped-convex `K` extremizer from q102y, every remaining arbitrary-heterogeneity necessary condition would depend only on the two scalar null parameters `(delta,s)` (plus the explicit face ray above), rather than on any coefficient matrix or contact-mass vector.

## Validation plan

Only the finite rational/exponential inequalities above need a checker. The monotonicity proof itself is analytic and must be written on the report page. If the finite checks pass, archive only that arithmetic core; do not claim the `N=12,13` cells eliminated unless the resulting two-dimensional scalar inequality is itself certified over the full cells.

Section-B moves for this reduced object: **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT** (differentiate the adaptive split objective), **#13 FIND WHAT ONLY INCREASES** (prove the split objective is monotone), **#30 DO ONE SCALE/DIRECTION AT A TIME** (one adaptive face ray).