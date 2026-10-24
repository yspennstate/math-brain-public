# HARD7-03 idea before code — exact mixed-sign triple-slack bonus

Target remains D0025 / Seppäläinen Problem 4, frozen test case `K=2`, `Q=(1/2)delta_{1/2}+(1/2)delta_1`, metric a rigorous lower bound `L <= Delta_2(Q)`.

The preceding checkpoint used the global envelope

\[
\Phi_\theta(u,v)\ge \kappa(\theta)e^{\min(u,0)+\min(v,0)},
\qquad \kappa(\theta)=\frac{\theta}{(2-\theta)(3-\theta)}.
\]

It throws away a systematic gain whenever exactly one predecessor gap is negative and the other is positive. The sliding-window geometry guarantees that this mixed-sign situation is the only nontrivial complement geometry, so attack that loss directly rather than adding another hard event.

Put

\[
a=1-\theta,\qquad b=2-\theta,\qquad c=3-\theta.
\]

For `v<0<=u`, split the exact integral for `Phi` at `t=u`. Direct integration gives

\[
\Phi_\theta(u,v)
=\theta e^v\left[
\frac{1-e^{-au}}{ab}+\frac{e^{-bu}}{bc}
\right].
\]

Hence, relative to the old envelope `kappa e^v`, the exact bonus is

\[
\theta e^v\left[
\frac{1-e^{-au}}{ab}-\frac{1-e^{-bu}}{bc}
\right].
\]

For `u>=0`,

\[
1-e^{-bu}\le \frac ba(1-e^{-au})
\]

because the difference has derivative `b(e^{-au}-e^{-bu})>=0`. Therefore

\[
\boxed{
\Phi_\theta(u,v)
\ge \kappa e^v+\frac{\kappa}{a}e^v(1-e^{-au})
}\qquad(v<0\le u).
\]

The coefficient `kappa/a` is sharp for this basis: after dividing the exact bonus by `e^v(1-e^{-au})` and sending `u downarrow 0`, the ratio tends to `kappa/a`.

Localize first to an edge, where on the strict chain

\[
Y_0>Y_1>Y_2
\]

we have `u=Y_0-Y_1>0`, `v=Y_2-Y_1<0`. The extra correction beyond the preceding checkpoint is at least

\[
\frac{\kappa}{a}(T_1-T_2),
\]

where

\[
T_1=E[e^{(\theta-1)Y_1+Y_2};Y_0>Y_1>Y_2],
\]

\[
T_2=E[e^{Y_2-aY_0};Y_0>Y_1>Y_2].
\]

There are two reflected edges. Conditional on the first-layer exponentials, the bases satisfy `u_0>=u_1>=u_2`; both `T_1` and `T_2` reduce to exponential monomials times at most one base gap, so the existing six order-cone calculus can integrate them exactly with rational arithmetic.

Methods for this run: B1 (change category: exact hazard/Laplace kernel), B24 (find the sharp universal coefficient in the mixed-sign minorant), B30 (localize to the edge chain before attacking near-edge/central configurations). The triple differs from the immediately preceding B7/B9/B17 run.