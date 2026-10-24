# HARD7-03 idea before code — common-overlap pair correction

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

Target remains the admitted D0025 / Seppäläinen Problem 4 residual, frozen at `K=2` and `Q=(1/2)delta_{1/2}+(1/2)delta_1`. The tracked quantity is the rigorous lower bound `L <= Delta_2(Q)`. Carry-in is

`L = 2500000/29645831`.

The preceding run used B15/B25/B3. This run tries B24/B19/B5.

## B24 — replace the chosen shared predecessor by the extremal common predecessor

The four-step deterministic max inequality subtracts pair minima of adjacent time-three endpoints. Previous certificates lower-bounded each such pair minimum by choosing a single common time-two predecessor. This leaves an obvious structural loss whenever the two predecessor windows overlap in two sites.

Write `S_e=max{Y_j: j in W_e}` for the time-two predecessor maximum of the time-three endpoint `e`, and `T_3(e)=S_e+C_e`, with independent `C_e~Exp(1)`. For adjacent endpoints,

`min(T_3(e),T_3(e+1)) >= min(S_e,S_{e+1}) + min(C_e,C_{e+1})`

and

`min(S_e,S_{e+1}) >= max_{j in W_e cap W_{e+1}} Y_j`.

Hence, for `0<theta<1`,

`E exp(theta min(T_3(e),T_3(e+1))) >= [2/(2-theta)] E exp(theta max_{j in W_e cap W_{e+1}} Y_j)`.

This strictly strengthens the old one-predecessor bound on the four interior adjacent pairs while agreeing with it on the two outer pairs. Because the deterministic four-step identity separates the pair-minimum subtraction from the nonnegative triple-slack subtraction, this improvement can be combined with the already certified exact mixed-sign slack correction without double counting.

By reflection the six adjacent pairs have three common-window types:

- edge: `{Y_{-2}}`;
- outer: `{Y_{-2},Y_{-1}}`;
- inner: `{Y_{-1},Y_0}`.

If their exponential moments are `J_edge,J_outer,J_inner`, the new total pair correction should be

`C_cap(theta)=8/(2-theta)*(J_edge+J_outer+J_inner)`.

## B19 — make the common-window moment calculation algorithmic

Condition on the first-layer exponentials `(A_{-1},A_0,A_1)`. Every `Y_j=s_j+B_j` is a shifted independent unit exponential, with `s_j` a maximum of a fixed subset of the three `A` variables. On each of the six strict order cones, the shifts are order statistics. Use the exact conditional identity

`E exp(theta max_i(s_i+B_i)) = exp(theta m) + theta * sum_{empty != S} (-1)^(|S|+1) exp(sum_{i in S}s_i-(|S|-theta)m)/( |S|-theta )`,

where `m=max_i s_i`, and integrate each monomial over the order cone. The algorithm should both compute the three `J` values and verify any closed forms symbolically/exactly.

The candidate closed forms to test are

`J_edge = 1/(1-theta)^2`,

`J_outer = (8-5 theta)/((2-theta)^3(1-theta)^2)`,

`J_inner = 2(12-7 theta)/((3-theta)(2-theta)^3(1-theta)^2)`.

## B5 — re-optimize the Chernoff parameter after the structural correction

The old rational Chernoff point was chosen before the pair-overlap strengthening, so keep the theorem chain fixed and vary only `theta`. Numerical exploration is allowed only to choose a rational candidate; the final certificate must be exact rational arithmetic plus a positive Taylor lower bound for `exp(4 theta A)`. A promising rational point is `theta=723/1250`. The goal is to certify some `A<29645831/10000000`, hence move `L=1/(4A)` upward. No floating fit will be promoted as proof.