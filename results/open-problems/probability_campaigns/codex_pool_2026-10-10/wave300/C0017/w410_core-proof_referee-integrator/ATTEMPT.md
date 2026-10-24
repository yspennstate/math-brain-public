# C0017: the one-martingale trap and the missing lattice input

2026-10-10. The target is critical bond percolation on the square lattice at p=1/2. Wang Zhou's arXiv:2409.03235v6, Theorem 2, claims convergence of one Dobrushin exploration path to SLE6 under Caratheodory domain convergence and Condition C. Its mathematical correctness has not been settled by this packet. The 2026-09-07 intake's current-open label is historical, not a verified 2026 verdict.

## Independently checked conditional calculation

Let `g_t` solve `dg_t(z)=2/(g_t(z)-W_t)dt` with a continuous adapted real driver. For `0<a<b<c`, put `X=g_t(a)-W`, `Y_i=g_t(b_i)-W` with `b_1=b,b_2=c`, and stop while `0<X<Y_1<Y_2` remain separated. Let `C(u)=B(u;1/3,1/3)/B(1/3,1/3)` and `f(x,y)=C(x/y)`. Direct differentiation gives

`D f=C'(u)(1-u)/y>0`, `D^2 f=-(2/3)C'(u)(1-u^2)/(u y^2)`, and `A f=2C'(u)(1-u^2)/(u y^2)=-3D^2 f`, where `D=partial_x+partial_y`, `A=(2/x)partial_x+(2/y)partial_y`.

If `f(X,Y_1)` is a local martingale, its inverse `u=C^{-1}(f)` is a semimartingale on compact separated stops and `W=(g_t(a)-u g_t(b))/(1-u)` is a semimartingale. Write `W=V+N` with `Q=<N>`. Ito gives, as signed measures, `dV=-(1/3)(1/X+1/Y_i)(dQ-6dt)` for each `i`. Subtracting the two identities forces `dQ=6dt`, since `1/Y_1-1/Y_2>0`; then `dV=0`. This reproduces w408's local L1. Global Brownian identification additionally needs a countable family of stopped pairs whose localization stopping times increase to infinity; a pathwise choice of a pair after seeing the future is insufficient as a standalone localization argument. The square-lattice Cardy martingale approximation is still absent.

## New special-case counterexample: one Cardy martingale is insufficient

Fix `0<a<b`, put `u=a/b`, and take `0<=t<T<ab/4`. Define

`Y_t=sqrt(b^2-4t/u)`, `X_t=uY_t`, `W_t=(1+u)(b-Y_t)`,
`g_t(a)=W_t+X_t=(1+u)b-Y_t`, and `g_t(b)=W_t+Y_t=(1+u)b-uY_t`.

Since `Y'_t=-2/(uY_t)`, direct differentiation gives `g'_t(a)=2/X_t` and `g'_t(b)=2/Y_t`; the initial values are `a,b`. Thus these are the real marked-point solutions for the continuous deterministic driver `W`. Their ratio `X_t/Y_t=u` is constant, so `C(X_t/Y_t)` is a bounded (constant) martingale in any filtration. But `W'_t=2(1/X_t+1/Y_t)>0` and `<W>_t=0`, so `W` cannot be an SLE6 driver. A single Cardy test event, even known exactly at every stopped time, cannot identify Brownian driving. This says nothing against the percolation conjecture: the constructed driver is not asserted to arise from percolation.

## Hardest unproved input

For each of two distinct right boundary marks in a square-lattice Dobrushin domain, one needs a correctly oriented crossing/exit event whose Doob conditional probability remains jointly close, uniformly on separated stopped slits, to `C(X_delta/Y_delta,i)`; one also needs stopped driver/marked-point tightness and compatibility of the limiting filtration. Rotational invariance, RSW bounds and independent unexplored bonds do not alone establish this conditional Cardy identification. No proof of this input is supplied here. An independent referee (w413) should check the new one-martingale counterexample and its limits before a brain bundle is ingested.
