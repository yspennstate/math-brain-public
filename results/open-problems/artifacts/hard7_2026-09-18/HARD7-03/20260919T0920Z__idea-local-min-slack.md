Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# HARD7-03 idea before code — replace endpoint domination by local-minimum predecessor geometry

Active claim: `D0025`, Seppäläinen Problem 4. Frozen test case remains `K=2`, `Q=(1/2)delta_{1/2}+(1/2)delta_1`, metric a rigorous lower bound `L <= Delta_2(Q)`. Previous checkpoint: `L=3125/37092` from `G_1(0)<=9273/3125`.

Methods this run: **B5 / B13 / B19**, different from previous B8 / B18 / B25.

## B5: add the two predecessor-gap parameters

For one triple-slack term, condition on layer-two sliding maxima

`a=S_{d-1}, b=S_d, c=S_{d+1}`

and fresh iid unit exponentials `C_L,C_M,C_R`. Put `u=a-b`, `v=c-b`. The conditional slack is

`F_theta(a,b,c)=e^{theta b} Phi_theta(u,v)`

with

`Phi_theta(u,v)=E[(e^{theta min(u+C_L,v+C_R)}-e^{theta C_M})_+]`.

Using `(e^{theta x}-e^{theta y})_+=theta integral_y^x e^{theta t} dt` on `x>y`, independence gives the exact two-parameter representation

`Phi_theta(u,v)=theta int_0^infty e^{theta t}(1-e^{-t}) exp(-(t-u)_+-(t-v)_+) dt`.

This makes the discarded slack a monotone function of the two geometric gaps instead of forcing a single layer-two endpoint to dominate all neighboring windows.

## B13: local-minimum event is enough

`Phi_theta(u,v)` is coordinatewise nondecreasing in `(u,v)`. Hence on the event

`E_d={S_d <= S_{d-1} and S_d <= S_{d+1}}`

we have `u,v>=0` and therefore

`Phi_theta(u,v) >= Phi_theta(0,0) = kappa(theta)`

where

`kappa(theta)=theta/((2-theta)(3-theta))`.

Thus the exact triple slack satisfies the stronger lower bound

`R_d(theta) >= kappa(theta) E[e^{theta S_d}; E_d]`.

The previous report used much smaller sufficient events on which one layer-two `Y_j` dominated every window needed at location `d`. The local-minimum condition is the actual condition needed for the universal `kappa` factor and strictly enlarges the usable event.

## Exact decomposition of the local-minimum events

Write

`Y_-2=A_-1+B_-2`,
`Y_-1=max(A_-1,A_0)+B_-1`,
`Y_0=max(A_-1,A_0,A_1)+B_0`,
`Y_1=max(A_0,A_1)+B_1`,
`Y_2=A_1+B_2`.

For `d=2`, `E_2` is exactly `Y_2>=Y_1`; this is the previous edge weight.

For `d=1`, with `S_1=max(Y_0,Y_1,Y_2)`, the event `E_1` is the disjoint union

1. `Y_1=max(Y_0,Y_1,Y_2)`, and
2. `Y_-1 >= Y_2 >= max(Y_0,Y_1)`.

For `d=0`, with `S_0=max(Y_-1,Y_0,Y_1)`, the event `E_0` is the disjoint union

1. `Y_0=max(Y_-1,Y_0,Y_1)`,
2. `Y_2 >= Y_-1 >= max(Y_0,Y_1)`, and
3. its reflection `Y_-2 >= Y_1 >= max(Y_-1,Y_0)`.

These decompositions follow simply by conditioning on which of the three variables attains the central-window maximum; ties have probability zero.

## B19: exact order-cone algorithm for chain events

Conditional on the three first-layer `A` variables, every `Y_j=u_j+B_j` is a shifted unit exponential. Weighted target-max events are already handled by the six `A`-ordering cones from the previous checkpoint. For a new chain event

`Y_U >= Y_T >= Y_l for all l in L`

with weight `e^{theta Y_T}`, condition on `Y_T=y`. The lower variables contribute CDF factors `prod_l (1-e^{-(y-u_l)})`, and the upper variable contributes survival factor `1` for `y<=u_U` and `e^{-(y-u_U)}` for `y>u_U`. Expanding the finite product and splitting once at `u_U` leaves only exponential integrals. On each of the six first-layer order cones all bases are one of the three order statistics, so every term is an exact rational function of rational `theta`.

This run will test whether the resulting exact local-minimum subtraction lowers the certified four-layer Chernoff shape bound below `9273/3125`. No finite simulation is being used as proof.
