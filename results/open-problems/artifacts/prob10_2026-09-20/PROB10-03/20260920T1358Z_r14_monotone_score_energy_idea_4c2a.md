# PROB10-03 R14 — idea before code: monotone score/energy outer compiler

Status at start: OPEN/PARTIAL.  This note records the mathematical route before any checker is written.  No source endpoint is claimed here.

## Frozen setup

Use the dimensionless complete-third capacity chart from the preceding R14 report.  For `lambda=x-1>0`,

`F_lambda(t)=E_H exp[-lambda (t+H)_+^2/2]`, `u_lambda(t)=log F_lambda(t)`.

For fixed outer shift `a`, width `d>0`, and `m in (0,1)`, let

`nu_a(dt) proportional exp[m u_lambda(t)] exp[-(t-a)^2/(2 d^2)] dt`.

In the projective chart,

`a(v)=sqrt(w2/w0) v-1/sqrt(w0)`, `d^2=w1/w0`, `lambda=x-1`.

The three score/energy integrands whose outer `V` averages are `S1,S2,H1` are

`A1(a)=(E_{nu_a} u_lambda'(T))^2`,

`A2(a)=E_{nu_a} (u_lambda'(T))^2`,

`AH(a)=E_{nu_a} h_lambda(T)`,

where `h_lambda(t)=E_{rho_t}(t+H)_+^2` and `rho_t` is the inner hinge tilt.

## Attack A — exact monotone-likelihood-ratio compiler for all score/energy terms

Write the inner tilted variable `Y=t+H`.  Its density can be rewritten as

`rho_t(dy) proportional exp(t y) exp[-y^2/2-lambda y_+^2/2] dy`.

Hence `{rho_t}` is a one-parameter exponential family with monotone likelihood ratio in `t`.  Since `y_+^2` is increasing,

`h_lambda'(t)=Cov_{rho_t}(Y_+^2,Y)>=0`.

Gaussian convolution of the log-concave decreasing kernel `exp[-lambda y_+^2/2]` gives `u_lambda'<=0` and `u_lambda''<=0`.  Therefore `(u_lambda')^2` is nondecreasing.

The outer family also has exact MLR:

`d nu_{a2}/d nu_{a1}(t)=C exp[(a2-a1)t/d^2]` for `a2>a1`.

Consequently:

* `E_{nu_a} u_lambda'(T)` is nonincreasing and nonpositive, so `A1(a)` is nondecreasing;
* `A2(a)` is nondecreasing;
* `AH(a)` is nondecreasing.

This would extend the companion monotone-KL compiler from the two entropy terms to **all five** non-algebraic quantities in the four-residual system.  The outer `V` integration could then be enclosed by endpoint sums with exact Gaussian cell masses, with no `V` derivative bounds.

## Common envelope and tail plan

Differentiate under the inner tilt:

`u_lambda'(t)=-lambda E_{rho_t} Y_+`.

Thus pointwise

`(u_lambda')^2 <= lambda^2 h_lambda`.

The inner tilt is obtained from `N(t,1)` by a decreasing likelihood ratio `exp[-lambda y_+^2/2]`, so `rho_t <=_st N(t,1)` and

`h_lambda(t) <= T_1(t):=E(t+H)_+^2`.

The outer tilt is obtained from `N(a,d^2)` by the decreasing likelihood ratio `exp[m u_lambda(t)]`, hence `nu_a <=_st N(a,d^2)`.  Since `T_1` is increasing,

`AH(a) <= E_{N(a,d^2)}T_1(T)=T_s(a)`, `s^2=1+d^2`,

and therefore

`0<=A1(a)<=A2(a)<=lambda^2 AH(a)<=lambda^2 T_s(a)`.

For `a(v)=beta v-gamma`, `beta>0`, every `A_i(v)` is nondecreasing.  On a mesh, compact outer integration should therefore admit exact lower/upper endpoint sums.  For the right tail use

`T_s(a)<=a^2+s^2`

and the exact Gaussian moments to obtain

`int_R^infty T_s(beta v-gamma) phi(v) dv`
` <= beta^2[R phi(R)+Q(R)]-2 beta gamma phi(R)+(gamma^2+s^2)Q(R)`.

The left tail obeys `int_{-infty}^L A_i(v)phi(v)dv <= Phi(L) A_i(L)` by monotonicity.

## Attack B — exact parameter-sensitivity identities

For any integrable `G` not explicitly depending on `a,m`,

`d/da E_{nu_a}G(T)=Cov_{nu_a}(G(T),T)/d^2`,

`d/dm E_{nu_a}G(T)=Cov_{nu_a}(G(T),u_lambda(T))`.

Also `partial_lambda u_lambda=-h_lambda/2` and

`partial_lambda h_lambda(t)=-Var_{rho_t}(Y_+^2)/2 <=0`.

Hence, at fixed `(a,d,m)`,

`partial_lambda E_{nu_a}h_lambda(T)`
` = -1/2 E_{nu_a}Var_{rho_T}(Y_+^2) - (m/2)Var_{nu_a}(h_lambda(T)) <=0`.

So the score-energy integrand `AH` is increasing in outer shift `a` but decreasing in hinge stiffness `lambda`.  This is potentially useful for parameter-box enclosure in the Krawczyk stage.

## Attack C — dual/random-polytope route to test separately

Keep the exact dual identity: UNSAT iff `conv(0,-g_1,...,-g_M)` contains the Euclidean unit ball.  Instead of the already-retired one-facet first moment or deterministic epsilon net, test whether a Gaussian-width/statistical-dimension or halfspace-depth comparison yields a constant-density inradius bound.  The negation test is explicit: if the relaxation only yields origin-in-hull (`alpha>2`) or a uniform-VC error of order `sqrt(log alpha/alpha)`, record that it cannot compete with the current `12.3196344462` upper endpoint and do not promote it.

## Falsification plan before any promotion

1. Numerically sample broad strict-domain tuples and verify `A1,A2,AH` are nondecreasing in `a` and the common envelope holds.
2. Finite-difference the exact `partial_lambda AH` identity against quadrature and search for a sign violation.
3. Check the tail formula against direct high-order Gauss-Hermite integration.
4. Any numerical pass is only a self-check; the proof above, if complete after audit, is the substantive result.
