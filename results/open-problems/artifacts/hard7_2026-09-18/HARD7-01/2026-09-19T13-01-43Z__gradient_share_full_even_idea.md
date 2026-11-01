# HARD7-01 idea checkpoint — gradient shares plus sign-sector ground states

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

This note is deliberately written **before** checker code, in accordance with the new-methods-first policy. It is a route to test, not yet a verified theorem claim.

## New route

Keep the current weak-(B) recovery slice
\[
H_q(x)=\Big(\sum_{i=1}^n |x_i|^q\Big)^{2/q},\qquad q>2,
\]
and let
\[
H_q=\phi+\psi
\]
with `phi,psi` convex, positively 2-homogeneous, globally even, and `C^2` away from the origin. Unlike the preceding run, **do not assume coordinatewise unconditionality of either summand**.

The proposed route has two parts.

### 1. Coordinate gradient shares

At a smooth point with every coordinate nonzero define
\[
h_i(x):=\frac{\partial_i\phi(x)}{\partial_iH_q(x)}.
\]
The degeneracy of `Hess H_q` on the coordinate hyperplane `x_i=0` should force `partial_i phi=partial_i psi=0` there: since
\[
0\preceq \nabla^2\phi\preceq\nabla^2H_q
\]
and `(Hess H_q)_{ii}=0` on that face, positivity forces the entire `i`th Hessian row of `phi` to vanish there; 1-homogeneity of `grad phi` then kills the constant normal derivative on each face component. Convexity of the one-variable slices in `x_i` should then imply
\[
0\le h_i\le1.
\]
On `S_q={H_q=1}`, with `w_i=|x_i|^q` and `U=phi|_{S_q}`, Euler gives
\[
\sum_i w_i h_i=U.
\]
Using the exact inverse-Hessian metric and homogeneity,
\[
\Gamma_{H_q}(U)
=\frac{2}{q-1}\sum_iw_i(h_i-U)^2.
\]
Thus B9 suggests introducing a size-biased coordinate `I` with `P(I=i|x)=w_i`. Then
\[
\Gamma_{H_q}(U)=\frac{2}{q-1}\operatorname{Var}(h_I\mid x).
\]
B10 says the extremal `[0,1]` law at fixed mean is Bernoulli, hence
\[
\Gamma_{H_q}(U)\le \frac{2}{q-1}U(1-U).
\tag{A}
\]
This would improve the generic run-14 bound by the factor `1/(q-1)` and, crucially, would not use unconditionality of `phi`.

### 2. Full globally-even spectral gap, not merely the sign-invariant quotient

The preceding exact gap
\[
\lambda_{\rm unc}=\frac{nq}{2(q-1)}
\]
was proved only in the sign-invariant sector. Decompose a globally even function on the `2^n` orthants into sign characters `chi_S`. Global evenness allows only `|S|` even. In a nonempty sign sector the amplitude on the simplex has zero trace on every face indexed by `S`.

For the symmetric Dirichlet law with `alpha=1/q`, let `L` be the Wright--Fisher generator and put
\[
beta=1-alpha,\qquad h_S(w)=\prod_{i\in S}w_i^\beta.
\]
A direct calculation should give
\[
-Lh_S=\rho_S h_S,
\qquad
\rho_S=\frac{|S|(q-1)}{q^2}\big[n-1+(q-1)(|S|-1)\big].
\]
The ground-state representation should then yield the exact/at least sharp bottom of that Dirichlet sector. After multiplying by the Hessian-metric factor `q^2/[2(q-1)]`,
\[
\lambda_S
=\frac{|S|}{2}\big[n-1+(q-1)(|S|-1)\big].
\]
For globally even nontrivial sign sectors `|S|>=2`, so
\[
\lambda_S\ge n+q-2
>\frac{nq}{2(q-1)}\qquad(q>2).
\]
Therefore the **full globally-even** gap should still be
\[
\lambda_{\rm even}(H_q)=\frac{nq}{2(q-1)},
\tag{B}
\]
with the deficient first Dirichlet mode remaining the actual worst sector.

If (A) and (B) both survive checking, Poincare gives, for `V=Var(U)` and `M=m(1-m)`,
\[
\frac{nq}{2(q-1)}V
\le\frac{2}{q-1}(M-V),
\]
hence
\[
\boxed{\frac VM\le\frac{4}{nq+4}}.
\tag{C}
\]
Since
\[
\frac{4}{nq+4}\le\frac{2}{n+2}\qquad(q\ge2),
\]
this would prove the entire local common-degree correlation inequality on the `l_q^2` cone **without coordinatewise unconditionality of the summands**. At `n=3,q=4` it gives `V/M<=1/4`, stronger than both the source-slice target `2/5` and the previous projection sufficient target `19/55`.

## Method mapping

- **B13 FIND WHAT ONLY INCREASES:** use convex coordinate slices plus the degenerate Hessian budget to force the derivative shares into `[0,1]`.
- **B9 RANDOMIZE:** interpret the Hessian energy as the conditional variance of a size-biased random gradient share.
- **B10 DERANDOMIZE:** maximize that conditional variance by the Bernoulli endpoint law, then close the sign sectors by an explicit positive ground state.

The next step is to check every algebraic constant and the sign-sector ground-state eigenvalue exactly. No source closure, novelty, or metric movement is asserted in this idea checkpoint.