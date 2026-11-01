# PROB10-06 idea before code — keep derivative mass inside the branch-gap denominators

Runtime model exposed to this worker: **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is unavailable, so reasoning level is **UNVERIFIED**; GPT-6/maximum is not claimed.

Parent problem remains the Lyons–Pemantle–Peres speed-monotonicity conjecture for supercritical Galton–Watson trees **without leaves**. Convention is fixed: child bias `beta` pushes away from the root; parent bias `lambda=1/beta` pushes toward the root. Thus the source conjecture is `ell'_lambda<=0` on the full transient parent-bias interval `0<lambda<E nu`. This note stays on the delimited `{2,3}` high-mixture route and does not overwrite the P01 minimum-one, NM13-05 `{3,4}`, or P03 terminal-critical routes.

The immediate predecessor proved (pending independent audit)

`P(nu=2)=1-p, P(nu=3)=p, p>=3/4  =>  ell'_lambda<0 for lambda<=12/5`,

by differentiating the exact branch-addition gap `J=c_2-c_3`. Its main remaining loss occurs in

`-J' <= 2 eta mu/a^2 + 2 mu^2/a^3`, `a=lambda-1`,

where every branch denominator is replaced by `a` before expectation. The intended new route is to keep one copy of each branch inside those denominators.

## Attack A — weighted branch-gap derivative (primary)

Write

`j=B_0 B_3/(D_2 D_3)`, `D_2=a+B_0+B_1+B_2`, `D_3=D_2+B_3`,

`U=-partial_lambda B >=0`, and define

`q=E[B/(a+B)]`, `r=E[B/(a+B)^2]`, `s=E[U/(a+B)]`.

Since `D_2>=a+B_0` and `D_3>=a+B_3`, direct differentiation of `j` should give the sharper factorized estimate

`-J' <= 2 q(s+r)`.

This is strictly stronger than the previous bound whenever the branch is nondegenerate, because

`q<=mu/a`, `r<=mu/a^2`, `s<=eta/a`.

Moreover, on the high-bias strip where the inherited pathwise upper bound is `0<=B<=u=(3-lambda)/3<a`, the maps

`x -> x/(a+x)` and `x -> x/(a+x)^2`

are increasing concave. Hence

`q <= mu/(a+mu) <= u/(a+u)`,
`r <= mu/(a+mu)^2 <= u/(a+u)^2`.

The critical new object is `s`, not `eta`.

There is an exact denominator identity from the escape recursion `B=S/(lambda+S)`:

`a+B = lambda(a+S)/(lambda+S)`.

Therefore

`U/(a+B)
 = S/[lambda(lambda+S)(a+S)]
   + sum_i U_i/[(lambda+S)(a+S)]`.

For the child-derivative term, dropping only the distinguished child's own nonnegative escape leaves a sibling kernel

`R_j = E[1/((lambda+T_j)(a+T_j))]`,

with `j=1,2` siblings. If the scalar map

`G(z)=z^2/((lambda z+1)(a z+1))`

is increasing and concave on the exact range of the harmonic inverse-sum

`H_j=(sum_{r=1}^j B_r)^(-1)`,

then the already proved type-vector reciprocal supersolution gives rigorous upper bounds on `R_1,R_2` by Jensen, exactly as in the predecessor's `K_1,K_2` step. This would yield a closed contraction

`s <= A_s + rho_s s`

with `rho_s` expected to be materially below the old `rho`, and then

`Delta <= (-J')/c_3 <= 2 q(s+r)/c_3`.

The first falsification task is therefore **not** a numerical endpoint search: prove or refute the required monotonicity/concavity region for `G`, including the two-sibling harmonic range. If global concavity fails, isolate the exact threshold and either subdivide analytically or abandon this route.

## Attack B — terminal-splice constants (independent backup)

P03's current finite-third-moment theorem proves existence of some terminal interval `(m-epsilon,m)` but gives no explicit `epsilon`. For the finite `{2,3}` law one can try to make every constant in its normalized recursion explicit, then compare the resulting terminal lower endpoint with `12/5` for `p>=3/4`. A rigorous overlap would close the entire transient interval for that restricted high-mixture family. This route is deliberately kept separate from Attack A; existence of a terminal neighborhood alone is not counted as an overlap.

## Attack C — exact derivative identity for the branch ratio (negation/obstruction probe)

Instead of bounding `-J'`, differentiate

`d=J/c_2`, `c_3/c_2=1-d`,

and retain the favorable term `-d h_2` in

`Delta=(-J'-d h_2)/c_3`.

The predecessor discarded it because only `h_2>=0` was used. Try to lower-bound `d h_2` from the same branch variables, or construct an exact counterexample showing no useful product lower bound follows from the available marginal information. This attack is genuinely different from weighted `s` and from the terminal splice.

Success criterion for this run: a complete proof/certificate that enlarges a rigorously covered `{2,3}` bias/mixture region with an explicit sign margin, or else a precise obstruction for Attack A together with a materially different successful/failed route. The full source problem stays OPEN/PARTIAL absent source-wide proof and independent validation.