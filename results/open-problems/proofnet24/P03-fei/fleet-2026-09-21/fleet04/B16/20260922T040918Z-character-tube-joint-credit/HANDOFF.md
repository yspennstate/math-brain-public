# B16 handoff — joint information credit, not independent scalarization

Full FEI remains OPEN / NOT PROVED.

For the authentic physical restriction pair

`f_0(x,y)=x`, `f_1(x,y)=x h(y)`

with an unbiased literal `x` and **arbitrary** Boolean residual `h`, let `delta=Pr[h=-1]`, pivot bias `t`, `q=1-t`, `b=1-2 delta`, `V=4tq`, `D=q+t b^2`. The exact B17 information channels collapse jointly to

`H(B|S)=D h2(t b^2/D)`

and

`I(S;J)=h2(V delta)-D h2(4tq delta^2/D)-4t delta(1-delta) h2(t)`.

Thus the `-h2(V delta)` term in the local scalar remainder cancels exactly before estimation. The resulting local contribution is equation (2.4) of REPORT.md and is independent of the internal Fourier geometry or arity of `h`.

At balanced pivot `t=1/2`, every symmetric potential with cap `C=Gamma(1/2)>=6` pays the whole family:

`Lambda_C(delta) >= (C-6) delta + 2 delta^2(4 delta^2-2 delta+1)/(2 delta^2-2 delta+1) >= 0`.

For the live cap `C*=6.5218512`, `delta=1/64`, the preceding B16 four-scalar *separate-credit* sufficient lower envelope is negative `-0.0757345878048`, while the authentic node is positive `+0.0364052471717` and the analytic cap-six theorem proves at least `+0.0086424522355`. Therefore do **not** spend another run attempting to certify that old scalar lower envelope globally; its negativity can be a pure scalarization artifact.

The infinitesimal arbitrary-bias tube barrier is

`K0(t)=-h2(4t(1-t))-4t log2(t)+4t h2(t)`

and `K0(t)/t -> 8-4/ln 2`, exactly the `BSTAR` constant in the source certificate tail implementation.

Highest-value next step for the live decomposable/AND-extremality job: replace separate bounds on `H(B|S)` and `I(S;J)` by a joint lower bound indexed by a small common **signed spectral subspace**. The common one-character case is now exact and paid; any proposed extension should be falsified first on pairs with two or more shared signed atoms.

Inherited interface-C constraints consumed and preserved at their proved scopes:

* fleet02/B16 actual parent-mask report, path `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, creation revision `7f9fdcbbba89432301a5e32985ae2bd3e7b1ac5e`;
* fleet03/B18 signed flag-curvature report, path `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`, creation revision `4843e50690013fd18b85dd8763b53bdc75da79e8`.

Their lesson is the same: cancellation/orientation must stay live until after the correct joint source has been formed. No old R16/R32/terminal credit is re-spent here.
