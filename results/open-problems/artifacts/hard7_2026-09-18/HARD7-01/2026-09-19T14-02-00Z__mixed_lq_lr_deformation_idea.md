Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise.

# HARD7-01 idea before code — mixed `l_q^2 + eps l_r^2` deformation

Methods: **B5 / B6 / B30**.

The previous run proved the cone-variance criterion on the exact total potential

\[
H_q(x)=\|x\|_q^2,
\]

for arbitrary smooth globally-even convex complementary two-homogeneous splits. The obstruction is deformation away from the exact `l_q^2` total potential. This note records a route that genuinely leaves that family while preserving a strict source-valid local covariance inequality.

## Deformation family

Fix `n>=2`, `r>=q>2`, `eps>=0`, and set

\[
H_{q,r,\varepsilon}(x)=H_q(x)+\varepsilon H_r(x),\qquad H_s(x)=\|x\|_s^2.
\]

This is even, convex, positively two-homogeneous and `C^2` off the origin. Let

\[
H_{q,r,\varepsilon}=\phi+\psi
\]

with `phi,psi` convex, positively two-homogeneous, globally even and `C^2` off the origin. On `S_H={H=1}` put `U=phi` and `m=E U` under cone measure `nu_H`.

The inherited exact covariance identity is

\[
\operatorname{Cov}(\phi(X),\psi(X))
=\frac n2\left[m(1-m)-\left(\frac n2+1\right)\operatorname{Var}_{\nu_H}(U)\right].
\]

Thus it suffices to prove

\[
\frac{\operatorname{Var}(U)}{m(1-m)}\le \frac{2}{n+2}.
\]

## B5 — add `eps` and preserve bounded gradient shares

For every `s>2`, both `partial_i H_s` and the `ii` Hessian entry vanish on the coordinate face `x_i=0`. Hence the same face-degeneracy argument as the previous run gives, for `x_i != 0`,

\[
h_i:=\frac{\partial_i\phi}{\partial_i H}\in[0,1].
\]

Define

\[
p_i=\frac{x_i\partial_iH}{2H}.
\]

Then `p_i>=0`, `sum p_i=1`, and Euler's identity gives

\[
U=\sum_i p_i h_i.
\]

So the bounded-share mechanism survives this non-`l_q` deformation exactly.

## B6 — deform the Hessian metric from the solvable `H_q`

Write `A_s=nabla^2 H_s`, `g_s=nabla H_s`, and

\[
D_s=\operatorname{diag}(\partial_iH_s/x_i).
\]

For `s>2`,

\[
A_s=(s-1)D_s-(s-2)\frac{g_sg_s^T}{2H_s}.
\]

The rank-one Cauchy inequality gives `D_s-g_sg_s^T/(2H_s) >= 0`, hence

\[
D_s\preceq A_s\preceq (s-1)D_s.
\]

For `r>=q`, normalize `||x||_q=1`. Then

\[
\frac{\partial_iH_r}{\partial_iH_q}
=|x_i|^{r-q}\|x\|_r^{2-r}
\le M,
\qquad
M:=n^{(r-2)(1/q-1/r)}.
\]

The same bound holds for `D_r/D_q`, so

\[
A_r\preceq (r-1)M A_q,
\qquad
A_q\preceq A_H\preceq [1+\varepsilon(r-1)M]A_q.
\]

For the degree-zero extension `U=phi/H`, set `z=nabla U`. Then `x dot z=0` and

\[
z_i=(\partial_iH)(h_i-U).
\]

The exact inverse formula

\[
A_q^{-1}=\frac1{q-1}D_q^{-1}
+\frac{q-2}{q-1}\frac{xx^T}{2H_q}
\]

loses its radial term because `x dot z=0`. Since `A_H>=A_q` and

\[
\frac{\partial_iH}{\partial_iH_q}
=1+\varepsilon\frac{\partial_iH_r}{\partial_iH_q}
\le 1+\varepsilon M,
\]

one obtains pointwise on `S_H`

\[
\Gamma_H(U)=z^TA_H^{-1}z
\le \frac{2(1+\varepsilon M)}{q-1}
\sum_i p_i(h_i-U)^2
\le c_\varepsilon U(1-U),
\]

where

\[
c_\varepsilon:=\frac{2(1+\varepsilon M)}{q-1}.
\]

## Spectral-gap stability under the same deformation

On the common angular quotient, cone measure for a two-homogeneous potential has density proportional to `H^{-n/2}`. With `H_q=1`,

\[
\delta_0\le H_r/H_q\le1,
\qquad
\delta_0:=n^{-2(1/q-1/r)}.
\]

Therefore the normalized Radon density `rho=dnu_H/dnu_q` obeys

\[
R^{-1}\le \rho\le R,
\qquad
R:=\left(\frac{1+\varepsilon}{1+\varepsilon\delta_0}\right)^{n/2}.
\]

Also

\[
A_H^{-1}\succeq
\frac1{1+\varepsilon(r-1)M}A_q^{-1}.
\]

Using the previous run's full globally-even `H_q` gap

\[
\lambda_q=\frac{nq}{2(q-1)},
\]

measure comparison gives

\[
\lambda_H
\ge
\frac{\lambda_q}{R^2[1+\varepsilon(r-1)M]}.
\]

Poincare plus the pointwise energy cap yields

\[
\frac{\operatorname{Var}(U)}{m(1-m)}
\le \frac{c_\varepsilon}{\lambda_H+c_\varepsilon}.
\]

A sufficient condition for the source-required cone variance ratio is therefore

\[
\boxed{
R^2[1+\varepsilon(r-1)M][1+\varepsilon M]\le \frac q2.
}
\]

This is strict at `eps=0` whenever `q>2`, so it produces a genuine open deformation family beyond the exact `l_q^2` cone.

## B30 — explicit first nontrivial calibration

Take

\[
(n,q,r)=(3,4,6).
\]

Then

\[
M=3^{1/3}<3/2,
\qquad
\delta_0=3^{-1/6}>4/5.
\]

For every `0<=eps<=1/12`,

\[
R^2\le (65/64)^3,
\]

and

\[
R^2[1+5\varepsilon M][1+\varepsilon M]
\le
(65/64)^3(13/8)(9/8)
=\frac{32131125}{16777216}<2=\frac q2.
\]

Hence the full arbitrary-split local covariance inequality remains valid throughout the genuinely mixed family

\[
H(x)=\|x\|_4^2+\varepsilon\|x\|_6^2,
\qquad 0\le\varepsilon\le1/12.
\]

Using the same rational envelopes,

\[
\lambda_H\ge \frac{16}{13}(64/65)^3,
\qquad
c_\varepsilon\le 3/4,
\]

so

\[
\frac{\operatorname{Var}(U)}{m(1-m)}
\le
\frac{10710375}{27487591}
<\frac25,
\]

with exact slack

\[
\frac25-\frac{10710375}{27487591}
=\frac{1423307}{137437955}>0.
\]

This does **not** move the source metric `D_B`: it is a deformation-stable local/common-degree theorem, not the full dilation theorem for arbitrary even log-concave measures. It does move the mathematical checkpoint from one exactly solvable cone to an explicit nontrivial one-parameter neighborhood outside that cone.