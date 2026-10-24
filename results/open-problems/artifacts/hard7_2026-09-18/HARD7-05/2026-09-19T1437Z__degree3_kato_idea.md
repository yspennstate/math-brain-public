# HARD7-05 route note — degree-three quasimode with exact conditional-moment closure

New mathematical route written **before** the exact checker.

The preceding run certified a degree-two quasimode for the killed OU operator

\[
K=1_{(0,\infty)}P_r1_{(0,\infty)},\qquad r=287831/500000,
\]

and then used Kato--Temple plus the inherited exact certificate `tr(K^6)<0.15014436`.  The new attack is to test whether the first genuinely larger polynomial Galerkin space closes *algebraically* rather than by quadrature and whether its residual is small enough to move the frozen source bracket.

## Counterexample-first test

Before attempting a theorem, I numerically tested the degree-three generalized Ritz problem on

\[
V_3=\operatorname{span}\{1,x,x^2,x^3\}\,1_{\{x>0\}}.
\]

If the normalized residual were not materially smaller than the degree-two value `7.99e-6`, this route would be abandoned rather than certified.  The exploratory Ritz vector is close to

\[
(1,\ 0.701857,\ 0.025129,\ -0.012166),
\]

and the rational candidate

\[
c=(100000,70186,2513,-1217)^T
\]

gives exploratory values

\[
\mu\approx0.7284302708448,\qquad
\varepsilon^2\approx1.3909701\times10^{-6}.
\]

Thus the residual falls by a factor about `5.7`, so this route passes the counterexample-oriented stress test.

## Exact closure mechanism

For `X|Y=y ~ N(ry,s^2)`, `s=sqrt(1-r^2)`, write

\[
q(y)=\Phi(ry/s),\qquad p(y)=\phi(ry/s).
\]

The conditional positive moments needed through degree three are

\[
\begin{aligned}
J_0&=q,\\
J_1&=ryq+sp,\\
J_2&=(r^2y^2+s^2)q+rsy\,p,\\
J_3&=(r^3y^3+3rs^2y)q+(r^2sy^2+2s^3)p.
\end{aligned}
\]

Hence every Gram/Ritz entry `M_ij=<x^i,Kx^j>` and every squared-operator entry `N_ij=<x^i,K^2x^j>` for `0<=i,j<=3` reduces to five one-dimensional scalar moment families.  No numerical quadrature is needed:

- `A_m=int_0^inf y^m phi(y) q(y)dy`, `B_m=int_0^inf y^m phi(y)p(y)dy` close by one-step integration by parts;
- `U_m=int y^m phi q^2`, `V_m=int y^m phi qp`, `W_m=int y^m phi p^2` close by the recurrences already underlying the degree-two calculation, now only through degrees six.

The key recurrences are

\[
A_1=t/2+aB_0,\qquad A_m=(m-1)A_{m-2}+aB_{m-1},
\]

and

\[
U_1=t/4+2aV_0,\qquad U_m=(m-1)U_{m-2}+2aV_{m-1},
\]

with `a=r/s`; the Gaussian product moments `B_m,W_m` have elementary two-step recurrences.  This gives an exact rational-interval route to `mu` and `epsilon^2`.

## Three Section-B moves

- **B3 — PROVE SOMETHING STRONGER.** Replace the previous degree-two spectral capture by degree three and demand a strictly smaller certified residual before using it.
- **B11 — DUALIZE.** Compute `K^2` through the middle point of a three-step stationary AR(1) chain, turning an operator residual into scalar Gaussian moment recurrences.
- **B24 — FIND THE EXTREMAL OBJECT.** Use the sixth-trace budget adversarially: after spending at least `mu^6` on the top spectral point, the largest possible second eigenvalue is constrained by `tr(K^6)-mu^6`.  The intended exact coarse cap is `lambda_2<151/500=0.302`, sharper than the previous `0.31`.

If exact interval arithmetic confirms the exploratory values, the intended theorem target is

\[
\theta_{2,1/4}\ge 1434439/10^7=0.1434439,
\]

which would move the frozen width from `213121/2000000=0.1065605` to `1065561/10000000=0.1065561`.  If any exact comparison fails, no source metric movement will be claimed.
