# HARD7-03 idea before code — near-edge structural zero-gap triple slack

Runtime identification for this invocation: GPT-5.6 Sol; reasoning telemetry is unavailable (`UNVERIFIED`), so this is not claimed to be GPT-6 maximum.

Carry-in: the immutable 19:21Z checkpoint certified `L = 50000/584101 <= Delta_2(Q)` for the frozen `K=2`, `Q=(delta_{1/2}+delta_1)/2` case. Its new edge correction used the structural equality branch `Y_0>Y_2>Y_1`, where one predecessor gap is exactly zero. The report explicitly identified analogous near-edge/central equality strata as the next recoverable slack.

This run uses a different method triple: **B11 / B14 / B25**.

## New branch

For the right near-edge triple (`d=1`) write

- `S_0=max(Y_{-1},Y_0,Y_1)`,
- `S_1=max(Y_0,Y_1,Y_2)`,
- `S_2=max(Y_1,Y_2)`,
- `M=max(Y_1,Y_2)`, `U=Y_{-1}`.

On the strict event

`E_near = { U > M > Y_0 }`

we have `S_0=U>S_1=S_2=M`; hence the triple-slack gaps are `u=U-M>0`, `v=0`. This event is disjoint from the already corrected strict mixed-sign near-edge branch `{Y_{-1}>Y_0>max(Y_1,Y_2)}`.

For `a=1-theta`, `b=2-theta`, `c=3-theta`, the inherited exact boundary bonus is

`B0(u)=theta/(a*b)*(1-exp(-a*u)) - theta/(b*c)*(1-exp(-b*u))`.

The proposed new correction is

`C_near0 = E[ exp(theta*M) B0(U-M) ; U>M>Y_0 ]`.

## B11 — Laplace dualization of the boundary gap

Define

`T_r = E[exp(theta*M-r(U-M)); U>M>Y_0]`, `r in {0,a,b}`.

Conditioning on the first-layer shifts, the deterministic inequalities are

`s0=max(A_-1,A_0,A_1) >= sU=max(A_-1,A_0), s1=max(A_0,A_1) >= s2=A_1`.

On the event, `M>Y_0>=s0`, so every relevant exponential is already in its pure tail. Conditional on `M=m`,

`E[exp(-r U); U>m] = exp(sU-(1+r)m)/(1+r)`.

Therefore the entire dependence on `r` collapses:

`T_r = T_0/(1+r)`.

Consequently

`C_near0 = theta*T_0*(1/b^2 - 1/c^2) > 0`.

So the problem reduces to one positive scalar `T_0`.

## B25 — count the maximum directly

Given the first layer, for `m>=s0` the density of `M=max(Y_1,Y_2)` is

`f_M(m)=exp(s1-m)+exp(s2-m)-2 exp(s1+s2-2m)`.

Also `P(Y_0<m)=1-exp(s0-m)` and `P(U>m)=exp(sU-m)`. Direct integration from `m=s0` gives

`T_0 | A = [exp(sU+s1-b*s0)+exp(sU+s2-b*s0)]/(b*c)
            - 2 exp(sU+s1+s2-c*s0)/(c*d)`,

where `d=4-theta`.

Each term is an exponential monomial in first-layer order statistics. On each of the six strict order cones of `(A_-1,A_0,A_1)` it integrates to a product of reciprocal positive rational rates; hence rational `theta` gives an exact rational certificate.

## B14 — reflect without overlap

Reflection sends the right near-edge branch to the left near-edge branch. They belong to distinct fourth-step endpoints (`d=1` and `d=-1`), so their triple-slack contributions add exactly. If the exact integral is positive, the inherited four-step envelope improves by

`Delta U_4 = - 2*C_near0/(1-theta)`.

Only after this idea is committed and read back should an exact-arithmetic checker be written. No claim about metric movement is made in this idea note itself.