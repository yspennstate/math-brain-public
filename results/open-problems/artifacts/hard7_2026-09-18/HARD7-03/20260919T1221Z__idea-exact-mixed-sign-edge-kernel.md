# HARD7-03 idea before code — integrate the exact mixed-sign kernel, not its uniform minorant

Target remains D0025 / Seppäläinen Problem 4, frozen test case `K=2`, `Q=(1/2)delta_{1/2}+(1/2)delta_1`, frozen metric a rigorous lower bound `L <= Delta_2(Q)`.

Previous checkpoint: `L = 2500000/29649457`, obtained from `G_1(0) <= 29649457/10000000` after using, on the strict chain `Y0>Y1>Y2`, the one-basis lower bound

`Phi_theta(u,v) - kappa e^v >= (kappa/a)e^v(1-e^{-a u})`,

with `a=1-theta`, `b=2-theta`, `c=3-theta`, `kappa=theta/(bc)`, `v<0<=u`.

The new route is to stop optimizing a single coefficient before integration. The exact mixed-sign excess is

`B_theta(u,v)=theta e^v[(1-e^{-a u})/(ab) - (1-e^{-b u})/(bc)]`.

Subtracting the previous one-basis minorant leaves

`R_theta(u,v)=theta e^v/(abc) * [ b(1-e^{-a u}) - a(1-e^{-b u}) ]`.

For `u>0`, the bracket is strictly positive because its derivative is `ab(e^{-a u}-e^{-b u})>0`; at `u=0` it vanishes, while as `u->infinity` it tends to `b-a=1`. Thus the preceding coefficient-sharp minorant is only locally sharp at the origin and discards a nonzero large-gap boundary contribution.

On the chain `Y0>Y1>Y2`, after multiplying by the inherited `e^{theta Y1}` factor, define

`T1=E[e^{(theta-1)Y1+Y2}; chain]`,
`T2=E[e^{Y2-aY0}; chain]`,
`T3=E[e^{Y1+Y2-bY0}; chain]`.

Then the **exact** mixed-sign edge gain is

`E_exact = theta/(ab)(T1-T2) - kappa(T1-T3)`.

The previous gain was only `(kappa/a)(T1-T2)`. The new quantity `T3` has a clean conditional form when the shifted-exponential bases satisfy `u0>=u1>=u2`:

`T3|u = exp(u1+u2-bu0)/2 * [ ((u0-u2)^2-(u1-u2)^2)/c + 2(u0-u2)/c^2 + 2/c^3 ]`.

This turns the extra work into first and second moments of independent exponential gaps on each of the six `A`-order cones, hence exact rational arithmetic.

Methods for this run:
- **B29 (add points at infinity):** inspect `u=0` and `u=infinity`; the discarded remainder is zero at the former but strictly positive at the latter, exposing why the locally sharp basis is globally wasteful.
- **B27 (swap quantifiers):** replace “find one coefficient valid for every `u`, then integrate” by “integrate the exact `u`-dependent excess on a source-relevant order cone.”
- **B21 (ask who else has this shape):** recast the needed integral as a phase-type / exponential-gap moment calculation; squared gaps are obtained by second moments of sums of independent exponential spacings.

Only after this exact route is algebraically complete should a checker be built. The checker should reconstruct the full previous correction, compute `T1,T2,T3`, verify the exact edge gain strictly exceeds the old minorant gain, and then test a smaller rational `G_1(0)` certificate by positive Taylor lower bounding `exp(4 theta A)`.
