# PROB10-03 / R14 — projective slope-simplex normal form, sharp kernel curvature, and gap continuation

Date: 2026-09-20 UTC.

Target is the exact-radius negative spherical Gaussian perceptron at `kappa=-1`. This note concerns only the complete third-full stationary reduction already source-matched in the preceding PROB10/T03 reports. It does **not** promote a finite-lift numerical point to a source endpoint.

## 1. Strict third-full geometry and projective coordinates

Work on the strict overlap domain

\[
0<p_3<p_2<1,\qquad 0<q_3<q_2<1.
\]

Put

\[
w_0=1-p_2,\qquad w_1=p_2-p_3,\qquad w_2=p_3,
\]

and the three secant slopes

\[
r_0=\frac{1-q_2}{w_0},\qquad
r_1=\frac{q_2-q_3}{w_1},\qquad
r_2=\frac{q_3}{w_2}.
\]

Then

\[
w_0+w_1+w_2=1,\qquad
r_0w_0+r_1w_1+r_2w_2=1.
\]

The preceding exact q-sector reduction shows that the strict admissible cone is

\[
r_1>r_2>0,\qquad r_1^2<r_0r_2.
\]

Define

\[
x=\frac{r_0r_2}{r_1^2}>1,\qquad
y=\frac{r_1}{r_2}>1.
\]

### Theorem R14-T03-PROJECTIVE

Set

\[
Z=xy^2w_0+yw_1+w_2.
\]

Then the slope normalization is exactly

\[
r_2=\frac1Z,\qquad
r_1=\frac yZ,\qquad
r_0=\frac{xy^2}{Z}.
\]

Conversely, every

\[
w_i>0,\quad w_0+w_1+w_2=1,\quad x>1,\quad y>1
\]

defines a unique strict overlap pair by

\[
p_2=1-w_0,\qquad p_3=w_2,
\]
\[
q_3=\frac{w_2}{Z},\qquad
q_2=\frac{yw_1+w_2}{Z},
\]

and this pair automatically satisfies `0<q3<q2<1`, `r1>r2>0`, and `r1^2<r0 r2`.

Under this change of variables the exact algebraic q-sector reconstruction collapses to

\[
\boxed{
c_2=\frac{(x-1)\sqrt Z}{xyw_0},\qquad
c_3=\frac{(y-1)\sqrt Z}{yw_1},\qquad
\gamma_p=\frac{xy}{2\sqrt Z}.
}
\]

Moreover, for

\[
A_q=2\gamma_p-c_2(1-q_2),\qquad
D_q=A_q-c_3(q_2-q_3),
\]

one has the identities

\[
\boxed{
A_q=\frac y{\sqrt Z},\qquad
D_q=\frac1{\sqrt Z},\qquad
\frac{A_q}{2\gamma_p}=\frac1x,\qquad
\frac{D_q}{A_q}=\frac1y.
}
\]

Thus every logarithm and denominator in the closed q-Gaussian sector is automatically in its strict domain.

Finally,

\[
\frac{c_3}{c_2}
=
\frac{x(y-1)w_0}{(x-1)w_1},
\]

so the remaining hierarchy inequality `c2>c3>0` is exactly

\[
\boxed{(x-1)w_1>x(y-1)w_0.}
\]

#### Proof

The definitions give

\[
r_1=yr_2,\qquad r_0=xy^2r_2.
\]

Substitution into \(\sum_i r_iw_i=1\) yields \(r_2Z=1\), proving the slope formulas. The converse follows by direct substitution. Since \(Z>yw_1+w_2\), the formula for \(q_2\) is strictly below one, while all other strict overlap inequalities are immediate.

Substituting \(q_3=r_2p_3\), \(q_2-q_3=r_1(p_2-p_3)\), and \(1-q_2=r_0(1-p_2)\) into the already-proved q-sector formulas gives

\[
c_3=\frac{r_1-r_2}{r_1\sqrt{r_2}\,w_1},
\]
\[
\gamma_p=\frac{r_0\sqrt{r_2}}{2r_1},
\]
\[
c_2=\frac{r_0r_2-r_1^2}{r_0r_1\sqrt{r_2}\,w_0}.
\]

Inserting \(r_2=Z^{-1},r_1=yZ^{-1},r_0=xy^2Z^{-1}\) proves the displayed reconstruction. The formulas for \(A_q,D_q\) then follow by one-line cancellation. QED.

## 2. Positive-gap scale reconstruction becomes elementary

The preceding scale-Euler theorem gives, at every strict full stationary point,

\[
\Psi_3=2\gamma_{\rm sq}
-\frac{r_1}{r_0\sqrt{r_2}}.
\]

The projective coordinates make the scale term

\[
S:=\frac{r_1}{r_0\sqrt{r_2}}
=\frac{\sqrt Z}{xy}.
\]

Hence prescribing a comparison gap \(\delta\ge0\) gives

\[
\boxed{
\gamma_{\rm sq}(\delta)
=\frac12\left(\frac{\sqrt Z}{xy}+\delta\right)
}
\]

and, since \(B=c_2/(4\gamma_{\rm sq})\),

\[
\boxed{
B(\delta)
=
\frac{(x-1)\sqrt Z}
{2w_0(\sqrt Z+\delta xy)}.
}
\]

At capacity, \(\delta=0\), this reduces to the particularly simple identity

\[
\boxed{B=\frac{x-1}{2w_0}.}
\]

This removes the largest cancellation in the previous formula
\[
B=\frac{r_0r_2-r_1^2}{2w_0r_1^2}.
\]

## 3. The two algebraic c-sector terms are automatically positive

Let `A_c3,A_c2` denote the algebraic q-Gaussian derivatives appearing in the entropy/KL c-stationarity equations from the preceding T03 work.

Define

\[
k(y)=\frac{y(y\log y-y+1)}{(y-1)^2},
\qquad
h(x)=\frac{x(x-1-\log x)}{(x-1)^2}.
\]

### Theorem R14-T03-CSECTOR-NORMALFORM

In projective coordinates,

\[
\boxed{
A_{c_3}
=
\frac{w_1}{2Z}
\left[w_2+w_1k(y)\right]
}
\]

and

\[
\boxed{
A_{c_2}
=
\frac{w_0}{2}
\left[
1-\frac{xy^2w_0}{Z}h(x)
\right].
}
\]

For every \(x>1,y>1\),

\[
k(y)>0,\qquad 0<h(x)<1.
\]

Therefore throughout the strict projective domain,

\[
\boxed{
A_{c_3}>\frac{w_1w_2}{2Z}>0,
}
\]

and, because \(xy^2w_0/Z=r_0w_0=1-q_2<1\),

\[
\boxed{
A_{c_2}>\frac{w_0q_2}{2}>0.
}
\]

#### Proof

Substitute the projective formulas for `Aq,Dq,c2,c3,p,q` into the explicit source derivatives

\[
A_{c_3}
=
\frac12(p_2q_2-p_3q_3)
-\frac{\log(D_q/A_q)}{2c_3^2}
-\frac{q_2-q_3}{2c_3D_q}
-\frac{q_3(q_2-q_3)}{2D_q^2},
\]

\[
A_{c_2}
=
\frac12(1-p_2q_2)
-\frac{\log(A_q/(2\gamma_p))}{2c_2^2}
-\frac{1-q_2}{2c_2A_q}
+\frac{1-q_2}{2c_3}\left(\frac1{A_q}-\frac1{D_q}\right)
-\frac{q_3(1-q_2)}{2D_q^2}.
\]

Exact simplification gives the displayed formulas; the attached SymPy checker verifies these identities symbolically.

For \(y>1\), \(y\log y-y+1>0\) because its derivative is \(\log y>0\) and it vanishes at one. Thus \(k(y)>0\).

For \(x>1\), \(x-1-\log x>0\), so \(h(x)>0\). Also \(h(x)<1\) is equivalent to

\[
x(x-1-\log x)<(x-1)^2,
\]

or

\[
1-x+x\log x>0.
\]

The last function vanishes at one and has derivative \(\log x>0\). QED.

### Certification consequence

The previous entropy form required separately checking signs of the algebraic c-sector sides. Those signs are now structural consequences of the projective cone. A validated root search in `(w0,w2,x,y)` no longer spends interval budget proving positivity of `Aq,Dq,A_c2,A_c3` or the log arguments.

## 4. Sharp global curvature of the one-step hinge kernel

Fix \(B>0\), \(s>0\), and

\[
f(x)=\mathbb E_H e^{-B(x+sH)_+^2},
\qquad u(x)=\log f(x).
\]

Put

\[
A=1+2Bs^2.
\]

### Theorem R14-T03-KERNEL-CURVATURE

For every real \(x\),

\[
\boxed{
-\frac{2B}{A}\le u_{xx}(x)\le0.
}
\]

Further, if \(\rho_x\) is the normalized tilted H-law

\[
\frac{d\rho_x}{d\gamma_H}
=
\frac{e^{-B(x+sH)_+^2}}{f(x)},
\]

then

\[
u_B=-\mathbb E_{\rho_x}(x+sH)_+^2,
\qquad
u_x=-2B\mathbb E_{\rho_x}(x+sH)_+,
\]

and consequently

\[
0\le -u_B(x)\le x^2+s^2,
\]
\[
|u_x(x)|^2\le 4B^2(-u_B(x))
\le4B^2(x^2+s^2),
\]
\[
0\le -u(x)\le B(x^2+s^2).
\]

#### Proof of the upper curvature bound

The function \(y\mapsto e^{-By_+^2}\) is log-concave because \(y_+^2\) is convex. Gaussian convolution preserves log-concavity, hence \(f\) is log-concave and \(u_{xx}\le0\).

#### Proof of the lower curvature bound

Write

\[
e^{-By_+^2}=e^{-By^2}h(y),
\qquad
h(y)=e^{By_-^2}.
\]

Since \(y_-^2\) is convex, \(h\) is log-convex. Completing the square in the Gaussian convolution gives

\[
f(x)
=
A^{-1/2}e^{-Bx^2/A}
\,\mathbb E\,
h\!\left(\frac{x}{A}+\frac{s}{\sqrt A}Z\right).
\]

Gaussian convolution preserves log-convexity by Hölder's inequality: if \(h\) is log-convex, then \(z\mapsto \mathbb E h(z+\tau Z)\) is log-convex. Hence

\[
x\mapsto u(x)+\frac{B}{A}x^2
\]

is convex. This is exactly \(u_{xx}\ge-2B/A\).

The derivative identities follow by differentiation under the integral. For the moment bounds, exponential tilting by \(e^{-Bt}\) decreases the mean of the nonnegative statistic \(t=(x+sH)_+^2\), because its B-derivative is minus its variance. Thus

\[
-u_B(B)\le -u_B(0)=\mathbb E(x+sH)_+^2\le x^2+s^2.
\]

Cauchy--Schwarz gives the score bound. Finally \(u(0)=0\) as a function of B and

\[
-u(B)=\int_0^B[-u_t(t)]dt
\le B(x^2+s^2).
\]
QED.

## 5. Uniform outer-tail control for the nested third-full moments

Write

\[
d^2=p_2-p_3,\qquad
a(v)=\sqrt{p_3}\,v-1,
\qquad
X=dU+a(v),
\]

and

\[
F(v)=\log\mathbb E_U e^{m u(X)},
\qquad
\langle\cdot\rangle_v
=
\frac{\mathbb E_U[(\cdot)e^{m u(X)}]}
{\mathbb E_U e^{m u(X)}}.
\]

Here \(m=c_3/c_2\in(0,1)\).

Differentiation gives

\[
F'(v)=m\sqrt{p_3}\,\langle u_x\rangle_v,
\]

\[
F''(v)
=
mp_3\langle u_{xx}\rangle_v
+
m^2p_3\operatorname{Var}_v(u_x).
\]

By Prékopa, \(F\) is concave, while the sharp kernel lower-curvature bound gives

\[
\boxed{
-\frac{2mBp_3}{A}\le F''(v)\le0.
}
\]

If

\[
S_0\ge|\langle u_x\rangle_{v=0}|,
\qquad
C_1=\frac{2B\sqrt{p_3}}{A},
\]

then for all \(v\),

\[
\boxed{
|\langle u_x\rangle_v|
\le S_0+C_1|v|.
}
\]

The inner tilted U-law has log-density

\[
-\frac{U^2}{2}+m u(dU+a(v))-\log Z_v.
\]

Since \(u_{xx}\le0\), this law is 1-strongly log-concave; hence by Brascamp--Lieb

\[
\operatorname{Var}_v(U)\le1.
\]

Gaussian integration by parts gives

\[
\langle U\rangle_v=md\langle u_x\rangle_v.
\]

Therefore

\[
\langle X^2+s^2\rangle_v
\le
E_2(v),
\]

where

\[
\boxed{
E_2(v)
=
1-p_3+
\left(
|a(v)|+md^2[S_0+C_1|v|]
\right)^2.
}
\]

Consequently the exact nested integrands obey

\[
\langle u_x\rangle_v^2
\le [S_0+C_1|v|]^2,
\]

\[
\langle u_x^2\rangle_v
\le4B^2E_2(v),
\]

\[
\langle -u_B\rangle_v
\le E_2(v),
\]

\[
-\langle u\rangle_v
\le B E_2(v).
\]

For the inner entropy

\[
D_U(v)=
KL(\nu_v\|\gamma_U)
=
m\langle u\rangle_v-F(v),
\]

Jensen gives

\[
\boxed{
0\le D_U(v)
\le mB[1-p_3+a(v)^2].
}
\]

For the one-step H entropy,

\[
D_H(v)
=
m\left\langle
KL(\rho_X\|\gamma_H)
\right\rangle_v,
\]

the pointwise identity
\[
KL(\rho_x\|\gamma_H)=Bu_B(x)-u(x)
\]
and \(Bu_B\le0\) give

\[
\boxed{
0\le D_H(v)\le mB E_2(v).
}
\]

Every quantity needed by the entropy-stable four-overlap compiler therefore has at most a quadratic envelope in \(|v|\). The outer Gaussian tails are consequently explicit. For example, if
\[
S(v)\le C_0+C_1|v|,
\]
then for \(V\sim N(0,1)\),

\[
\mathbb E[S(V)^2{\bf1}_{|V|>T}]
\le
2\left[
C_0^2Q(T)+2C_0C_1\phi(T)
+C_1^2(T\phi(T)+Q(T))
\right].
\]

This removes the unproved outer-tail step from a future directed-interval certificate: only a compact V-window and the remaining inner integration must be enclosed numerically.

## 6. A separate deformation identity in the prescribed comparison gap

Let a smooth strict-interior branch of full stationary points be parametrized by density \(\alpha\), and let

\[
\delta=\Psi_3.
\]

The stationary envelope identity from the source objective is

\[
\frac{d\Psi_3}{d\alpha}=-\frac{Q}{c_3}>0.
\]

Hence wherever the branch is nonsingular,

\[
\boxed{
\frac{d\alpha}{d\delta}
=
-\frac{c_3}{Q}>0.
}
\]

The preceding one-dimensional power-mean collapse gives

\[
L\le Q\le mL<0,
\]

where

\[
L=
\mathbb E_V\log
\mathbb E_U f(X)
\]

collapses to a one-dimensional Gaussian expectation and \(m=c_3/c_2\). Therefore

\[
\boxed{
\frac{c_3}{-L}
\le
\frac{d\alpha}{d\delta}
\le
\frac{c_2}{-L}.
}
\]

Thus, once one stationary root on a branch is certified, movement in the positive comparison-gap parameter can be controlled with a one-dimensional envelope rather than by reevaluating the full objective.

## 7. What this does and does not prove

This note does **not** change the rigorous source bracket. It supplies three exact ingredients for the next third-full certification attempt:

1. a bijective projective chart that makes the q-sector and domain constraints algebraic and cancellation-free;
2. sharp global kernel curvature and explicit quadratic outer-tail envelopes for every score/KL quantity in the entropy-stable four-overlap residual;
3. an exact positive-gap continuation law controlled by the one-dimensional collapsed quantity `L`.

A numerical scout at the archived `delta=10^-3` point was used only to falsify the formulas. It also shows that the raw Euclidean Jacobian condition number in `(w0,w2,x,y)` is worse than in `(p2,p3,q2,q3)`; therefore the projective chart should be used for interval domain/cancellation control, not advertised as an automatic conditioning improvement. A weighted/preconditioned Krawczyk map remains necessary.
