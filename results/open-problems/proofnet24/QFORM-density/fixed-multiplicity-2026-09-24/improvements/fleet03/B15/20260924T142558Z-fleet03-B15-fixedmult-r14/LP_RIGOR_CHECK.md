# Rigor check — all-finite-Lp/Orlicz addendum

## Fourier endpoint

Set `a=pi C_*`. From `|phi(t)|<=min(1,a/|t|)` and `q>1`,

`int |phi|^q <=2a+2 a^q int_a^infinity t^(-q)dt
              =2a q/(q-1)`.

For `p=q/(q-1)>=2`, this is `2 pi C_* p`. The inverse Fourier operator with the manuscript convention has interpolation bound

`||F^{-1}g||_p <=(2pi)^(-1/q)||g||_q`,

so

`||p_Q||_p <=(C_* p)^(1/q)=(C_*p)^(1-1/p)`.

To avoid assuming a density, replace the output measure `mu` by `mu*g_epsilon`. Its Fourier transform is `phi(t)e^{-epsilon t^2}`, hence has the same `L^q` bound. Uniform `L^p` boundedness and reflexivity give a weakly convergent subsequence; weak convergence of the convolved probability measures to `mu` identifies the `L^p` weak limit with `mu`. Lower semicontinuity preserves the bound. This proves absolute continuity and the stated norm.

## Orlicz series

For each integer `m>=1`,

`int p^m <=(C_*m)^(m-1)`.

Thus Tonelli gives

`int(exp(p/(eC_*))-1)
 <=(1/C_*) sum_(m>=1) m^(m-1)/(e^m m!)`.

The rooted labelled tree exponential generating function is the unique nonnegative solution of `T=z exp(T)` on `0<=z<=1/e`. At `z=1/e`, `T=1`, so the series equals one. This establishes the bound `<=1/C_*` without an asymptotic estimate.

For a measurable set `E` of length `delta`,

`(1/delta) int_E exp(p/(eC_*))
 <=1+1/(C_*delta)`.

Convexity/Jensen gives

`exp(P(E)/(eC_*delta))
 <=1+1/(C_*delta)`,

hence

`P(E)<=eC_*delta log(1+1/(C_*delta))`.

## Constants

With `delta_*=0.854335140191133771...` and `g_*=delta_*^2/2`,

`C_*=sqrt(e) g_*^(-1/4)=2.121243892402635...`,

`e C_*=5.766138726447817...`.

## Endpoint limitation

The bound `||p||_p=O(p)` as `p->infinity` is not an `L^infinity` estimate; logarithmically unbounded densities can have this growth. The addendum therefore does not close multiplicity eight.

Verdict: **PASS (self-check)** for the analytic compiler from the strong-cross `1/|t|` envelope to finite `L^p`, Orlicz control and near-linear measurable-set concentration.
