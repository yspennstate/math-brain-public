# One-shared-coordinate block potential

## Definition

Let

\[
q(y)=y\log_2(1/y)+\frac{2y}{\ln2},\qquad q(0)=0.
\]

Then the reviewed singleton potential is `phi(t)=q(t^2)`. On `[0,1]`,

\[
q'(y)=\frac{1-\ln y}{\ln2}>0,
\qquad q''(y)=-\frac1{y\ln2}<0.
\]

Fix a physical coordinate `x`. For a Boolean `f(x,u)` define

\[
\Lambda_x(f)=q(\widehat f(\emptyset)^2+\widehat f(\{x\})^2)
+\sum_{i\in u}q\!\left(
\widehat f(\{i\})^2+\widehat f(\{i,x\})^2
\right).
\]

This stores each singleton together with the coefficient that can be shifted
into it by multiplication through `x`.

Write `Lambda_x^o(f)` for the same sum with the first mean/shared block
removed, and put
`E_x(f)=fhat(emptyset)^2+fhat({x})^2`.

## Theorem 1: one-shared-coordinate product law

Let `f(x,u)` and `g(x,v)` be Boolean, with `u` and `v` disjoint. Then

\[
\boxed{\Phi(fg)\le
\Lambda_x^\circ(f)+\Lambda_x^\circ(g)
+\min\{q(E_x(f)),q(E_x(g))\}
\le \Lambda_x(f)+\Lambda_x(g).}
\]

### Proof

Write

\[
m_g=\widehat g(\emptyset),\qquad d_g=\widehat g(\{x\}),
\quad A_g=\begin{pmatrix}m_g&d_g\\d_g&m_g\end{pmatrix}.
\]

For a private coordinate `i` of `f`, put
`a_i=\widehat f(\{i\})` and `b_i=\widehat f(\{i,x\})`. Fourier convolution
on the shared bit gives

\[
\binom{\widehat{fg}(\{i\})}{\widehat{fg}(\{i,x\})}
=A_g\binom{a_i}{b_i}.
\]

The eigenvalues of `A_g` are

\[
m_g\pm d_g=\mathbb E[g\mid x=\pm1],
\]

so `||A_g||_op<=1`. Therefore

\[
\widehat{fg}(\{i\})^2
\le \widehat{fg}(\{i\})^2+\widehat{fg}(\{i,x\})^2
\le a_i^2+b_i^2.
\]

Monotonicity of `q` pays every private `f` singleton by its `x`-block in
`Lambda_x(f)`. The symmetric argument pays every private `g` singleton.

For the shared singleton, set
`alpha_+=m_f+d_f`, `alpha_-=m_f-d_f` and define `beta_+/-` similarly for
`g`. Then

\[
\widehat{fg}(\emptyset)^2+\widehat{fg}(\{x\})^2
=\frac{\alpha_+^2\beta_+^2+\alpha_-^2\beta_-^2}{2}
\le m_f^2+d_f^2,
\]

because `|beta_+/-|<=1`. Hence the shared singleton is paid by the first
block of `Lambda_x(f)`. Interchanging `f,g` yields the symmetric minimum.
Summing proves the sharpened theorem and hence the simpler displayed
`Lambda_x(f)+Lambda_x(g)` bound.

## Theorem 2: physical revelation law

For every Boolean `f(x,u)`,

\[
\boxed{\frac12\Phi(f\mid x=1)+\frac12\Phi(f\mid x=-1)
\le \Lambda_x(f).}
\]

### Proof

For each private `i`, restriction gives singleton coefficients `a_i+b_i`
and `a_i-b_i`. Their squared average is `a_i^2+b_i^2`. Concavity of `q`
therefore gives

\[
\frac12q((a_i+b_i)^2)+\frac12q((a_i-b_i)^2)
\le q(a_i^2+b_i^2).
\]

Sum over `i`. The nonnegative mean/shared block in `Lambda_x(f)` is unused.

## Scope and implication

The B05 majority/rare-gate obstruction is absorbed exactly because
`Lambda_x(xK_n)` contains `Phi(K_n)` in its `{i,x}` blocks. Thus the failed
scalar potential has a dimension-independent one-overlap replacement.

This does not prove full FEI. `Lambda_x` is not yet bounded by `I` or `U`, and
the theorem does not prevent the same block from being charged again at a
second reused coordinate. The remaining universal target is a signed stopping
rule that owns each block at its first physical revelation and telescopes the
unused block energy across arbitrary overlap depth.
