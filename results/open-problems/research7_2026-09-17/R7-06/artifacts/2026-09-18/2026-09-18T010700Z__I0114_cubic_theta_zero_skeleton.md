# I0114 / `omega*_9`: cubic-theta factorization and a uniform zero-response theorem

Date: 2026-09-18 UTC  
Track: `research7_2026-09-17/R7-06/`  
Target: canonical `I0114`, Sylvia Serfaty, *Lectures on Coulomb and Riesz gases*, Conjecture 11.1, dimension two.  
Scope: a rigorous theorem for the Hardin--Tenpas nine-point periodic milestone `omega*_9`. This note proves the previously missing all-Gaussian sign condition on the full zero-response skeleton of the `D=0` witness family and proves local compatibility of the two scalar envelopes at the double-contact point `p`. It does **not** prove `omega*_9` universally optimal and does not settle the global Cohn--Kumar conjecture.

## 1. Setup recovered from the preceding R7-06 reduction

The Hardin--Tenpas transformed `A2` chamber is

\[
\mathcal D=\{(x,y):\tfrac12\le y\le1,\ -1\le x\le T_3(y)\},
\qquad T_3(y)=4y^3-3y.
\]

For the nine-point square-family case the two nonidentity interpolation nodes are

\[
p=(-\tfrac12,1),\qquad q=(-1,\tfrac12).
\]

The low-degree invariant basis used in the preceding run contains

\[
\alpha=\frac{-1+2y(x+y)}3,
\qquad
\beta=\frac{-1+2x(x-3y+4y^3)}3.
\]

Let `Pi` be the contact projector onto `span{1,alpha,beta}` characterized by

\[
(\Pi V)(p)=V(p),\quad (\Pi V)(q)=V(q),\quad
(\Pi V)_x(p)=V_x(p).
\]

For the active coefficient face `D=0`, the preceding run proved

\[
H_C=(I-\Pi)F_a-C K_C,
\]
with

\[
K_C=\frac{(2y-1)(2y+1)(4x^2+4xy+4y^2-3)}6.
\tag{1.1}
\]

Write

\[
R_0=(I-\Pi)F_a.
\]

The exact scalar-envelope reduction says that a real `C` can satisfy `H_C>=0` on all of `D` only if

\[
R_0\ge0\quad\hbox{on }Z_K:=\{K_C=0\}\cap\mathcal D.
\tag{1.2}
\]

The previous run identified two nontrivial branches of `Z_K`:

\[
\Gamma_-(\theta)=\bigl(\cos(\theta+2\pi/3),\cos\theta\bigr),
\qquad 0\le\theta\le\pi/3,
\tag{1.3}
\]

and

\[
\Gamma_+(\theta)=\bigl(\cos(\theta-2\pi/3),\cos\theta\bigr),
\qquad 0\le\theta\le\pi/6.
\tag{1.4}
\]

Both start at `p`; `Gamma_-` ends at `q`. The aim here is to prove (1.2) for **every Gaussian parameter `a>0`**, exactly and without a grid.

## 2. B18 -- translate both conic branches to one scalar coordinate

### 2.1 The invariant coordinates collapse to one quadratic variable

On `Gamma_-`, define

\[
t=\cos(2\theta+\pi/3).
\tag{2.1}
\]

A direct trigonometric simplification gives

\[
\boxed{\alpha=\frac{t-1/2}{3}},
\qquad
\boxed{\beta=\frac{2t^2-2t-1}{3}}.
\tag{2.2}
\]

As `theta` runs from `0` to `pi/3`, `t` runs monotonically from `1/2` to `-1`.

On `Gamma_+`, put instead

\[
t=\cos(2\theta-\pi/3).
\tag{2.3}
\]

The **same identities** (2.2) hold. Here `t` runs from `1/2` to `1`.

For completeness, (2.2) may be checked without any geometric input. Substitute

\[
x=\cos(\theta\pm2\pi/3),\qquad y=\cos\theta
\]

into the displayed formulas for `alpha,beta`, use the addition formulas and `cos(2theta)=2cos^2(theta)-1`, and simplify. Thus every element of `span{1,alpha,beta}` restricts on either branch to the **same quadratic polynomial in `t`**.

### 2.2 Physical `A2` coordinates identify the two branches by Weyl symmetry

Use

\[
e_1=(1,0),\qquad e_2=(1/2,\sqrt3/2),\qquad
u=Ae_1+Be_2.
\]

The transformed variables are

\[
x=\cos(2\pi\nu_1),
\qquad
y=\cos(2\pi\nu_2/\sqrt3).
\]

On `Gamma_-`, equations (1.3) give

\[
A=\frac13,\qquad B=\frac\theta\pi,
\]
so that

\[
t=\cos(2\pi B+\pi/3).
\tag{2.4}
\]

On `Gamma_+`, the relation is `A+B=1/3`. The Weyl transformation

\[
W(A,B)=(A+B,-B)
\tag{2.5}
\]

preserves the quadratic form `A^2+AB+B^2`, hence preserves `A2`, and sends this branch to `A'=1/3`. Since the periodized Gaussian is Weyl invariant, the restrictions of `F_a` to the two branches are values of one common scalar function

\[
f_a(t),\qquad -1\le t\le1.
\tag{2.6}
\]

Thus the entire two-arc obstruction (1.2) is now a one-variable interpolation problem on one interval.

## 3. B18 continued -- exact cubic-theta product for the scalar restriction

The covolume of `A2` is `sqrt(3)/2`, and the dual quadratic form is

\[
|m e_1^*+n e_2^*|^2=\frac43(m^2-mn+n^2).
\]

Poisson summation therefore gives, up to a positive `a`-dependent scalar,

\[
F_a(A,B)
= C_a\sum_{m,n\in\mathbb Z}
q^{m^2-mn+n^2}e^{2\pi i(mA+nB)},
\qquad
q=e^{-4\pi^2/(3a)}\in(0,1),
\tag{3.1}
\]
with `C_a>0`.

Set `A=1/3`, replace `n` by `-n`, and let

\[
\omega=e^{2\pi i/3},\qquad z=\omega e^{-2\pi iB}.
\]

Then

\[
F_a(1/3,B)
=C_a\sum_{m,n\in\mathbb Z}
\omega^{m-n}q^{m^2+mn+n^2}z^n.
\tag{3.2}
\]

The double sum is exactly the cubic Jacobi function `b(q,z)` of Hirschhorn--Garvan--Borwein, *Cubic Analogues of the Jacobian Theta Function theta(z,q)*, Canadian Journal of Mathematics 45 (1993), 673--694, equation (1.13). Their product formula (1.22) is

\[
b(q,z)
=(q;q)_\infty(q^3;q^3)_\infty
\frac{(zq;q)_\infty(z^{-1}q;q)_\infty}
{(zq^3;q^3)_\infty(z^{-1}q^3;q^3)_\infty}.
\tag{3.3}
\]

The quotient in (3.3) cancels precisely the factors whose indices are divisible by three. Since `|z|=1`,

\[
(1-zq^n)(1-z^{-1}q^n)
=1-2\Re(z)q^n+q^{2n}.
\]

By (2.4),

\[
\Re z
=\cos(2\pi/3-2\pi B)
=-\cos(2\pi B+\pi/3)
=-t.
\]

Consequently the restriction has the exact factorization

\[
\boxed{
 f_a(t)=A_a
 \prod_{\substack{n\ge1\\3\nmid n}}
 \bigl(1+2tq^n+q^{2n}\bigr),
 \qquad -1\le t\le1,
}
\tag{3.4}
\]

where

\[
A_a=C_a(q;q)_\infty(q^3;q^3)_\infty>0.
\]

This is the crucial translation. It uses an old exact cubic-theta identity; no novelty is claimed for (3.3).

## 4. B4 -- strict absolute monotonicity on the whole zero skeleton

Every factor in (3.4) is strictly positive for `-1<=t<=1`, because

\[
1+2tq^n+q^{2n}\ge (1-q^n)^2>0.
\]

It is also affine in `t` with strictly positive slope `2q^n`. For every fixed integer `k>=1`, termwise differentiation of the convergent product gives

\[
\boxed{
 f_a^{(k)}(t)
 =k!\, f_a(t)
 \sum_{\substack{n_1<\cdots<n_k\\3\nmid n_j}}
 \prod_{j=1}^k
 \frac{2q^{n_j}}
 {1+2tq^{n_j}+q^{2n_j}}>0.
}
\tag{4.1}
\]

The differentiation is justified uniformly on `[-1,1]`: indeed

\[
\sum_{\substack{n\ge1\\3\nmid n}}
\frac{2q^n}{(1-q^n)^2}<\infty,
\tag{4.2}
\]

and the elementary symmetric sums in these majorants converge for every fixed order. Thus

\[
\boxed{f_a^{(k)}(t)>0\quad\text{for every }a>0,\ k\ge0,\ -1\le t\le1.}
\tag{4.3}
\]

So the Gaussian restriction to the full response-zero skeleton is not merely monotone; it is strictly absolutely monotone in the natural scalar coordinate `t`.

## 5. B4 -- Hermite error proves the full zero-response sign condition

By (2.2), the restriction of `Pi F_a` to either branch is a polynomial of degree at most two in `t`. It matches `f_a` at

\[
t=-1\quad(q),\qquad t=1/2\quad(p).
\]

It also matches the derivative with respect to `t` at `p`. To see this directly, on either branch at `theta=0` one has

\[
\frac{dy}{d\theta}=0,
\qquad
\frac{dx/d\theta}{dt/d\theta}=\frac12.
\]

Hence

\[
\left.\frac{d}{dt}F_a\right|_{p}
=\frac12 F_{a,x}(p),
\]

and the defining contact condition `(Pi F_a)_x(p)=F_{a,x}(p)` gives the same derivative for the projected polynomial.

Therefore `(Pi F_a)|_{Z_K}` is exactly the degree-two Hermite interpolant `H_a` to `f_a` with a simple node at `-1` and a double node at `1/2`. Newton's divided-difference remainder is

\[
\boxed{
 f_a(t)-H_a(t)
 =f_a[-1,\tfrac12,\tfrac12,t]
   (t+1)(t-\tfrac12)^2.
}
\tag{5.1}
\]

Because `f_a'''(t)>0` everywhere, every third divided difference in (5.1), including its repeated-node limits, is strictly positive. The polynomial factor in (5.1) is nonnegative on the entire interval `[-1,1]`. Thus

\[
\boxed{
R_0=(I-\Pi)F_a\ge0
\quad\text{on all of }Z_K
\quad\text{for every }a>0.
}
\tag{5.2}
\]

Moreover, equality in (5.2) occurs only at the prescribed contact points

\[
\boxed{t=-1\ (q)\quad\text{and}\quad t=1/2\ (p).}
\tag{5.3}
\]

Indeed, away from those two nodes the node product in (5.1) is strictly positive and the divided difference is strictly positive.

This completely discharges the branch-independent condition (1.2) from the preceding exact envelope theorem. In particular the second arc endpoint `t=1` has strict residual positivity.

## 6. B30 -- local gluing at the double-contact point `p`

The remaining scalar feasibility condition is the envelope overlap `C_-<=C_+`. The zero set can in principle obstruct such gluing because `R_0/K_C` is singular there. The theorem above shows that every regular zero-skeleton point other than the prescribed contacts is **repulsive** to finite envelope extrema: since `R_0>0` there while `K_C` changes sign transversely,

\[
\frac{R_0}{K_C}\to +\infty\quad(K_C\downarrow0),
\qquad
\frac{R_0}{K_C}\to -\infty\quad(K_C\uparrow0).
\tag{6.1}
\]

At the double contact `p`, both numerator and denominator vanish, so a local blow-up is required. Put

\[
h=x+\frac12,
\qquad v=y-1.
\]

An exact expansion of (1.1) at `p` is

\[
K_C
=3v+2h^2+2hv+10v^2
+\frac{16}{3}h^2v+\frac{16}{3}hv^2
+\frac{28}{3}v^3
+\frac83h^2v^2+\frac83hv^3+\frac83v^4.
\tag{6.2}
\]

In particular

\[
K_C=3v+2h^2+O(|h||v|+v^2+|h|^2|v|).
\tag{6.3}
\]

Write

\[
r_y=R_{0,y}(p),\qquad r_{xx}=R_{0,xx}(p).
\]

The contact conditions give `R_0(p)=R_{0,x}(p)=0`, hence

\[
R_0=r_yv+\frac12r_{xx}h^2
+O(|h||v|+v^2+|h|^3).
\tag{6.4}
\]

Because `K_{C,y}(p)=3`, the local zero curve has

\[
v=-\frac23h^2+O(h^3).
\tag{6.5}
\]

On that curve, (5.1) has a strictly positive quadratic leading term at `p`: the factor `(t-1/2)^2` is quadratic in `h`, while `t+1` and the divided difference stay strictly positive. Combining with (6.4)--(6.5) yields the strict differential inequality

\[
\boxed{
\frac12r_{xx}-\frac23r_y>0,
\qquad\text{equivalently}\qquad
\frac{r_y}{3}<\frac{r_{xx}}4.
}
\tag{6.6}
\]

Now approach `p` inside the chamber on parabolic scales

\[
v=-\lambda h^2,
\qquad \lambda\ge0,
\]
with `lambda` fixed and `h->0`. From (6.3)--(6.4), whenever `lambda!=2/3`,

\[
\boxed{
\frac{R_0}{K_C}
\longrightarrow
L(\lambda):=
\frac{\frac12r_{xx}-\lambda r_y}{2-3\lambda}.
}
\tag{6.7}
\]

A direct derivative gives

\[
L'(\lambda)=
\frac{\frac12(3r_{xx}-4r_y)}{(2-3\lambda)^2}>0
\tag{6.8}
\]

by (6.6). Therefore

\[
\inf_{0\le\lambda<2/3}L(\lambda)=\frac{r_{xx}}4,
\tag{6.9}
\]

while

\[
\sup_{\lambda>2/3}L(\lambda)=\frac{r_y}{3}.
\tag{6.10}
\]

The strict gap (6.6) is exactly the local compatibility inequality between the upper-envelope side and lower-envelope side:

\[
\boxed{
\sup_{K_C<0,\ z\to p}\frac{R_0(z)}{K_C(z)}
\ \le\ \frac{r_y}{3}
\ <\ \frac{r_{xx}}4
\ \le\ 
\inf_{K_C>0,\ z\to p}\frac{R_0(z)}{K_C(z)}
}
\tag{6.11}
\]

at the level of all finite parabolic blow-up limits. Thus the double contact `p` cannot itself be the mechanism by which the scalar envelopes cross in the wrong order.

The cusp contact `q`, where the chamber width is quadratic and `K_C` vanishes cubically in the natural cusp scale, is deliberately **not** claimed resolved by (6.11). Its local compactification requires a separate two-parameter cusp analysis. Likewise (6.11) is local; it does not exclude a genuine global active point away from the zero skeleton.

## 7. What has and has not been proved

### Proved in this note

1. Both branches of `K_C=0` are one scalar interval `t in [-1,1]` for the restricted `A2` Gaussian.
2. The restriction is the exact cubic-theta product (3.4).
3. It is strictly absolutely monotone in `t` for every Gaussian parameter.
4. The contact projector restricts to the `(-1; 1/2,1/2)` quadratic Hermite interpolant.
5. Hence `R_0>=0` on the **entire** zero-response skeleton, uniformly for all `a>0`, with equality only at `p,q`.
6. The local two-envelope blow-up at `p` has a strict compatibility gap; `p` cannot cause an envelope crossing.

### Still open for the `omega*_9` milestone

The exact envelope theorem from the previous run still requires the global inequality

\[
C_-(a)\le C_+(a)
\]

together with the scalar coefficient walls for every `a>0`. The present theorem removes the formerly independent zero-skeleton obstruction but does not prove this remaining overlap. The cusp `q` and possible global active points in the two sign components remain possible locations of failure. Therefore the frozen source-progress metric remains `m_sq=2`.

## 8. Dated source/prior-art note

As checked on 2026-09-18:

- Hardin--Tenpas, *Universally Optimal Periodic Configurations in the Plane*, arXiv:2307.15822 / *Discrete Analysis* 2025:26, proves the four-point `A2` periodic case and a distinct six-point periodic case, not `omega*_9` or global two-dimensional Cohn--Kumar universal optimality.
- Thomas Leble, *The hexagonal lattice is universally locally optimal*, arXiv:2511.03353 (2025), is explicitly a **local** universal-optimality theorem.
- Hirschhorn--Garvan--Borwein (1993), equation (1.22), supplies the old cubic-theta product identity used essentially in Section 3 above.
- A bounded fresh exact-title / `omega*_9` / nine-point `A2` / Cohn--Kumar follow-up search did not locate a later theorem settling this milestone or the global conjecture. That negative search is not a novelty certificate or proof of openness by itself.

Status relative to `I0114`: **PARTIAL / source OPEN in the checked record**. No publication-novelty claim is made.