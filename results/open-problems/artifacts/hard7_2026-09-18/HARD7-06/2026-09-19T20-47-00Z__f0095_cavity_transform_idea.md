# HARD7-06 F0095 — idea checkpoint before code

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

Methods for this iteration: **B18 / B27 / B19**. The research move is to stop treating the ACG contact function as an opaque one-dimensional residual and instead identify it exactly with a logarithmic-transform discrepancy between the incoming message law and an outgoing cavity law. This gives a precise fixed-point route and a theorem-sized structural reduction before any new certificate code.

## Message coordinates

For the q=3 ACG functional, put

\[
t=\frac{1-x}{3}\in[0,1/3],\qquad x=1-3t.
\]

If a Poisson multiset of incoming messages is `N={t_i}`, define

\[
A=\prod_i(1-t_i),\qquad B=\prod_i(1-2t_i),\qquad C=\prod_i(1-3t_i),
\]
\[
S(N)=3A-3B+C.
\]

Adding a new message `t` gives the exact affine identity

\[
S(N+\delta_t)=S(N)-3t\,(A-2B+C).
\]

Therefore define the outgoing cavity message

\[
R(N):=\frac{A-2B+C}{3A-3B+C}.
\]

Then

\[
F(N+\delta_t)-F(N)=\log(1-3tR(N)),\qquad F=\log S.
\]

The edge kernel transforms just as simply:

\[
1-\frac{(1-x)(1-y)}3=1-3ts.
\]

## Range lemma

For every finite multiset `N` with `t_i in [0,1/3]`,

\[
0\le R(N)\le \frac13.
\]

Proof. Let `f(u)=prod_i(1-u t_i)`. On `[1,3)` all factors are nonnegative and

\[
f''(u)=2f(u)\sum_{i<j}\frac{t_it_j}{(1-ut_i)(1-ut_j)}\ge0.
\]

Hence convexity gives

\[
A-2B+C=f(1)-2f(2)+f(3)\ge0.
\]

Also `C<=B`, so

\[
3(A-2B+C)\le3A-3B+C
\]

because the difference of the right side and the left side is `3B-2C>=0`. This proves the claim (with endpoint cases by continuity).

## Exact cavity-transform form of the contact potential

Let `a` now denote the full incoming law on `[0,1/3]`, including the neutral atom at `t=0`, and let `N_a` be a PPP of intensity `d a`. Define the cavity operator

\[
\mathcal C_d(a):=\operatorname{Law}(R(N_a)).
\]

The ACG functional becomes

\[
\Sigma_d(a)=\mathbb E\log S(N_a)-\frac d2\iint\log(1-3st)\,a(ds)a(dt).
\]

Its insertion/contact function is exactly

\[
\Phi_a(t)
=\int\log(1-3ts)\,\mathcal C_d(a)(ds)
-\int\log(1-3ts)\,a(ds).
\tag{*}
\]

Indeed the first integral is the Poisson add-one difference by the affine identity above, and the second is exactly the edge contribution. Therefore the already established first-variation formula becomes

\[
D\Sigma_d(a)[\delta_t-a]
=d\left(\Phi_a(t)-\int\Phi_a(s)a(ds)\right).
\tag{**}
\]

This is the key change of language (B18): the contact residual is not merely a numerical KKT object; it is a logarithmic-transform discrepancy between an incoming message law and its outgoing cavity image.

## Fixed-point theorem

1. If `a=C_d(a)`, then `Phi_a(t)=0` for every `t in [0,1/3]`, hence every mass-transfer first variation in (**) vanishes.
2. Conversely, if `Phi_a(t)=0` on any subset of `[0,1/3)` having an accumulation point, then `a=C_d(a)`.

For (2), both sides of (*) are real analytic in `t` on a neighborhood of `[0,1/3]`, since `0<=s<=1/3` implies `1-3ts>=2/3` on the square. Expanding at zero gives

\[
\Phi_a(t)
=-\sum_{k\ge1}\frac{3^k t^k}{k}
\left(
\int s^k\,\mathcal C_d(a)(ds)-\int s^k\,a(ds)
\right).
\]

Analytic continuation from the accumulation set forces every moment difference to vanish. Compact support on `[0,1/3]` makes the Hausdorff moment problem determinate, so the two measures coincide.

Thus a genuinely continuous/infinite-support stationary law (whose contact set has an accumulation point) must satisfy the exact distributional cavity equation. Finite-support stationary witnesses are the alternative branch: their contact set can remain discrete and they should be viewed as finite-dimensional approximants to the cavity law rather than arbitrary optimizer outputs.

## B27 — strengthen the quantifier on purpose

Instead of asking only for `Phi_a(t)>=0` for every insertion point, impose the stronger self-consistency equation

\[
\boxed{a=\mathcal C_d(a).}
\]

This is not asserted to solve F0095. It is a stronger equation whose solutions are automatically measure-stationary for the ACG variational functional. It converts the next search into a distributional fixed-point problem with a canonical operator.

## B19 — algorithm forced by the theorem

The constructive route is now:

1. iterate or solve `a=C_d(a)` near the current nontrivial branch;
2. evaluate `Sigma_d(a)` along that branch and locate its zero;
3. compress a candidate fixed-point law to finite support only after the distributional solve, using contact-aware quadrature rather than blind atom insertion;
4. certify the compressed witness with the existing one-sided Poisson/logarithm machinery.

The finite-support endpoint witness from the previous run is already extremely close to contact balance; the new theorem explains why. A population-dynamics experiment can guide the branch, but no simulation is promoted to a theorem or to movement of `W_3`.

## What would close the new route

A useful next theorem would be either (i) existence plus local uniqueness of the nontrivial fixed-point branch for `d` in an explicit interval containing 4.6865, with a rigorous discretization error from the branch to the ACG functional, or (ii) a direct one-sided quadrature theorem turning a fixed-point approximation into `Phi_a>=0` plus a certified negative `Sigma_d`. Either would be structurally stronger than another unsupported decimal support search.
