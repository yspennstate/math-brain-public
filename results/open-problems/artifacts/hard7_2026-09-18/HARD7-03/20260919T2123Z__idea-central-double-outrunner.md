# HARD7-03 idea checkpoint — complete the strict local-minimum chamber before coding

Target remains D0025, the frozen K=2 binary site-disorder case. This note records the route before any checker is written in this run.

Previous work made the local-minimum baseline `Phi_theta(u,v) >= kappa` exact on all structural boundary strata with one positive predecessor gap and the other gap identically zero. The remaining obvious strict local-minimum chamber is therefore not another boundary event: it is the central configuration where *both* neighboring sliding-window maxima strictly exceed the central one.

Write

`S_e = max{Y_z : |z-e| <= 1, -2 <= z <= 2}`

and at the center put `T=S_0=max(Y_-1,Y_0,Y_1)`, `u=S_-1-S_0`, `v=S_1-S_0`. A direct max-identity check suggests

`u>0 and v>0  <=>  Y_-2>T and Y_2>T`.

This should be the unique strict `(+,+)` local-minimum chamber: nested windows forbid `(+,+)` at d=1,2 and their reflections. Thus B24 says to attack this central double-outrunner event first, rather than another arbitrary order cell.

The key B5 deformation is to scale the two overshoots by a parameter lambda in [0,1]. At lambda=0 one is back at the already solved baseline `(u,v)=(0,0)`; at lambda=1 one reaches the whole double-outrunner chamber. Coordinatewise monotonicity of `Phi_theta` makes this a monotone deformation, so any exact evaluation at lambda=1 is a legitimate positive correction.

There is a stronger simplification. Conditional on the first layer and on the inner maximum `T=t`, the outer variables are shifted unit exponentials with shifts `A_-1` and `A_1`. Since `T >= Y_0 >= max(A_-1,A_0,A_1)`, both outer shifts are <=t. On the event `Y_-2>t, Y_2>t`, exponential memorylessness says the two residual gaps

`E_L=Y_-2-t`, `E_R=Y_2-t`

are independent Exp(1), independently of the inner variables. Hence the exact excess over the local-minimum baseline factors as

`C_both(theta) = D(theta) * T_both(theta)`,

where

`D(theta)=E[Phi_theta(E_L,E_R)-kappa]`

and

`T_both(theta)=E[ exp(A_-1+A_1-(2-theta)T) ]`.

For one Exp(1) residual E,

`E exp(-(s-E)_+) = exp(-s)(1+s)`.

Therefore, with `b=2-theta`, `c=3-theta`,

`D(theta) = 2 theta [ (b^-2-c^-2) + (b^-3-c^-3) ] > 0`.

For `T=max(Y_-1,Y_0,Y_1)`, conditional on the first layer and writing the three deterministic shifts `s_j`, its density above `s_0=max(A_-1,A_0,A_1)` has the finite inclusion-exclusion expansion

`f_T(t)=sum_{empty != J subset {-1,0,1}} (-1)^{|J|+1}|J| exp(sum_{j in J}s_j-|J|t)`.

Thus `T_both(theta)` reduces on each of the six strict A-order cones to a finite sum of exponential-spacing integrals and is exactly rational for rational theta.

B19 checker plan, only after the above route is fixed: enumerate all 5!=120 strict orderings of the five Y-labels and certify the sign-pattern identities. In particular it should certify (i) no `(+,+)` chamber at d=1 or d=2, (ii) the earlier edge/near/center zero-gap event identities, and (iii) at d=0, `(+,+)` iff both outer Y's outrun the inner maximum. This makes the correction exhaustive for the previously missing strict local-minimum chamber rather than a sampled subevent.

If the exact correction is positive, subtract it only once at the central triple. It is disjoint from the old strict mixed-sign corrections and the structural zero-gap corrections by gap-sign pattern. Then test the same inherited rational Chernoff point first; only after proving movement consider changing theta. No simulation or finite-size particle system is evidence for the asymptotic source statement.