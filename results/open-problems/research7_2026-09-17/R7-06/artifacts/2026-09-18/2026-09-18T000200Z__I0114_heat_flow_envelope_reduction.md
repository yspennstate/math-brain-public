# I0114 / `omega*_9`: projected heat flow, exact scalar envelope reduction, and the zero-response skeleton

Date: 2026-09-18 UTC  
Track: `research7_2026-09-17/R7-06/`  
Target: canonical `I0114`, Sylvia Serfaty, *Lectures on Coulomb and Riesz gases*, Conjecture 11.1, dimension two (Cohn--Kumar universal optimality of the triangular lattice).  
Scope of this note: a rigorous structural reduction for the Hardin--Tenpas nine-point periodic milestone `omega*_9`. It does **not** prove all-Gaussian optimality of `omega*_9` and does not settle the global Cohn--Kumar conjecture.

## 1. Recovered setup

Use the Hardin--Tenpas transformed `A2` fundamental triangle

\[
\mathcal D=\{(x,y):\tfrac12\le y\le 1,\ -1\le x\le T_3(y)\},
\qquad T_3(y)=4y^3-3y.
\]

For `omega*_9` the nonidentity interpolation nodes are

\[
p=(-\tfrac12,1),\qquad q=(-1,\tfrac12).
\]

The complete invariant space of `A2`-degree `<6` has basis

\[
1,\alpha,\beta,\gamma,\delta,
\]

where

\[
\alpha=\frac{-1+2y(x+y)}3,
\]

\[
\beta=\frac{-1+2x(x-3y+4y^3)}3,
\]

\[
\gamma=\frac{2T_2(x)T_2(y)+T_4(y)}3,
\]

\[
\delta=\frac{T_3(x)y+xT_5(y)+T_2(x)T_4(y)}3.
\]

Let `F=F_a` be the transformed `A2`-periodized Gaussian for parameter `a>0`. A degree-`<6` witness has the form

\[
g=c_0+A\alpha+B\beta+C\gamma+D\delta
\]

with nonconstant coefficients nonnegative. The required value contacts at `p,q` and top-boundary tangency at `p` leave `C,D` free and give

\[
A=\frac32F_x(p)+2C+\frac12D,
\]

\[
B=\frac12F_x(p)+C+\frac12D-\frac23\bigl(F(p)-F(q)\bigr),
\]

\[
c_0=F(p)+\frac12B.
\]

The previous final-recovery run established the response kernels

\[
K_C=\frac12+2\alpha+\beta+\gamma
 =\frac{(2y-1)(2y+1)(4x^2+4xy+4y^2-3)}6,
\tag{1.1}
\]

and

\[
K_D=\frac14+\frac12\alpha+\frac12\beta+\delta.
\tag{1.2}
\]

This note develops the exact parameter-continuation and all-domain consequences of (1.1).

## 2. B3: a parameter-independent contact projector

Define a linear operator `Pi` on smooth functions on `D` by requiring `Pi V` to lie in `span{1,alpha,beta}` and to reproduce exactly the three forced contact data

\[
(\Pi V)(p)=V(p),\qquad (\Pi V)(q)=V(q),\qquad
\partial_x(\Pi V)(p)=\partial_xV(p).
\]

Solving the three equations gives the explicit formula

\[
\Pi V=c_V+A_V\alpha+B_V\beta,
\]

where

\[
A_V=\frac32V_x(p),
\]

\[
B_V=\frac12V_x(p)-\frac23\bigl(V(p)-V(q)\bigr),
\]

\[
c_V=V(p)+\frac12B_V.
\tag{2.1}
\]

This is a genuine projector: `Pi 1=1`, `Pi alpha=alpha`, and `Pi beta=beta`.

By linearity, imposing the three forced contacts on

\[
g=c_0+A\alpha+B\beta+C\gamma+D\delta
\]

is equivalent to the identity

\[
\boxed{
 g=\Pi F+C(\gamma-\Pi\gamma)+D(\delta-\Pi\delta).
}
\tag{2.2}
\]

Hence

\[
\boxed{K_C=\gamma-\Pi\gamma,\qquad K_D=\delta-\Pi\delta.}
\tag{2.3}
\]

The full residual is therefore

\[
\boxed{
H_{C,D}:=F-g=(I-\Pi)F-C K_C-DK_D.
}
\tag{2.4}
\]

Equation (2.4) is stronger than treating each Gaussian parameter separately: all parameter dependence is isolated in the single projected function `(I-Pi)F`; the response directions are fixed polynomials once and for all.

For the active face `D=0` define

\[
H_0:=(I-\Pi)F.
\]

Then

\[
\boxed{H_C=H_0-C K_C.}
\tag{2.5}
\]

Every all-domain statement on this face is therefore a one-parameter semi-infinite linear feasibility problem.

## 3. B5: Gaussian parameter becomes an exact heat flow

The physical `A2`-periodized Gaussian is

\[
F_a^{\rm phys}(u)=\sum_{v\in A_2}e^{-a|u+v|^2}.
\]

For one summand in dimension two,

\[
\Delta_u e^{-a|u+v|^2}
=(-4a+4a^2|u+v|^2)e^{-a|u+v|^2}.
\]

Since

\[
\partial_a e^{-a|u+v|^2}=-|u+v|^2e^{-a|u+v|^2},
\]

termwise differentiation (valid for every `a>0` by Gaussian convergence) yields

\[
\boxed{
\partial_aF_a^{\rm phys}
=-\frac1{4a^2}\Delta_uF_a^{\rm phys}-\frac1aF_a^{\rm phys}.
}
\tag{3.1}
\]

Now set

\[
x=\cos(2\pi u_1),\qquad
 y=\cos(2\pi u_2/\sqrt3).
\]

For any smooth transformed function `V(x,y)`, the Euclidean Laplacian becomes

\[
\Delta_u V=4\pi^2\mathcal L V,
\]

where

\[
\boxed{
\mathcal L
=(1-x^2)\partial_{xx}-x\partial_x
+\frac13\bigl((1-y^2)\partial_{yy}-y\partial_y\bigr).
}
\tag{3.2}
\]

Thus the transformed periodized Gaussian satisfies

\[
\boxed{
\partial_aF_a
=-\frac{\pi^2}{a^2}\mathcal L F_a-\frac1aF_a.
}
\tag{3.3}
\]

The scalar term disappears under the normalization

\[
\tau=\frac{\pi^2}{a},\qquad U(\tau,x,y)=aF_a(x,y).
\]

Indeed, using `d tau/da=-pi^2/a^2`, (3.3) gives

\[
\boxed{\partial_\tau U=\mathcal L U.}
\tag{3.4}
\]

So the entire Gaussian parameter axis is exactly a forward heat flow for the fixed polynomial-coefficient operator `L`.

Because multiplication by the positive scalar `a` does not alter minorant feasibility, one may henceforth work with `U` instead of `F`. Define

\[
R_0(\tau):=(I-\Pi)U(\tau).
\]

Since `Pi` is parameter-independent,

\[
\boxed{
\partial_\tau R_0=(I-\Pi)\mathcal L U.
}
\tag{3.5}
\]

This is the exact continuation equation for the base residual. It avoids re-solving the interpolation system when the Gaussian parameter changes.

### Spectral consistency check

For an `A2` orbit polynomial `P_v` corresponding to a dual vector of squared norm `|v|^2`, the transformed operator satisfies

\[
\mathcal L P_v=-|v|^2P_v.
\]

Thus (3.4) evolves each Poisson/Fourier mode by `exp(-|v|^2 tau)`, exactly matching the Poisson representation. This independently checks the sign and normalization in (3.4).

## 4. B27: exact swap of the continuum quantifiers on `D=0`

Fix one Gaussian parameter and abbreviate

\[
R_0=(I-\Pi)U,\qquad K=K_C.
\]

We seek a coefficient `C` such that

\[
R_0(z)-C K(z)\ge0\qquad\hbox{for every }z\in\mathcal D.
\tag{4.1}
\]

Define the two scalar envelopes

\[
C_-(a):=\sup_{z\in\mathcal D:\ K(z)<0}\frac{R_0(z)}{K(z)},
\tag{4.2}
\]

\[
C_+(a):=\inf_{z\in\mathcal D:\ K(z)>0}\frac{R_0(z)}{K(z)}.
\tag{4.3}
\]

Also let

\[
Z_K:=\{z\in\mathcal D:K(z)=0\}.
\]

### Theorem 4.1 (exact scalar feasibility criterion)

There exists a real `C` satisfying (4.1) if and only if

\[
\boxed{R_0(z)\ge0\quad\hbox{for every }z\in Z_K}
\tag{4.4}
\]

and

\[
\boxed{C_-(a)\le C_+(a).}
\tag{4.5}
\]

When these hold, the complete set of all-domain feasible values is exactly the interval

\[
\boxed{[C_-(a),C_+(a)].}
\tag{4.6}
\]

If positive-definiteness also requires `C>=0` and `B>=0`, one simply intersects (4.6) with the corresponding scalar half-lines. In particular, on `D=0`,

\[
B=B_0+C,
\qquad
B_0=\frac12U_x(p)-\frac23(U(p)-U(q)),
\]

so the coefficient constraints add only

\[
C\ge\max\{0,-B_0\}.
\tag{4.7}
\]

`A=(3/2)U_x(p)+2C` is then positive whenever `C>=0`, because Hardin--Tenpas prove `U_x(p)>0`.

#### Proof

If `K(z)>0`, (4.1) is equivalent to

\[
C\le R_0(z)/K(z).
\]

Intersecting these inequalities over all positive-response points gives `C<=C_+`. If `K(z)<0`, division reverses the inequality and gives `C>=R_0(z)/K(z)`; intersecting gives `C>=C_-`. If `K(z)=0`, (4.1) reduces exactly to `R_0(z)>=0`. These conditions are plainly sufficient as well. This proves (4.4)--(4.6). The coefficient condition (4.7) is the explicit `B>=0` condition. QED.

The significance is conceptual and operational: the quantifier order

\[
\exists C\ \forall z\in\mathcal D
\]

has been replaced **exactly**, not approximately, by one lower scalar envelope, one upper scalar envelope, and a fixed one-dimensional zero-response set. No domain grid is involved in the theorem.

## 5. B3/B27: exact geometry of the zero-response skeleton

From (1.1), in the interior `y>1/2` the response vanishes precisely on

\[
x^2+xy+y^2=\frac34.
\tag{5.1}
\]

The conic can be parametrized by setting `y=cos theta`.

### Branch 1

For

\[
0\le\theta\le\frac\pi3,
\]

set

\[
\Gamma_-(\theta)
=\left(\cos(\theta+\frac{2\pi}3),\cos\theta\right).
\tag{5.2}
\]

A direct trigonometric calculation gives (5.1). This whole branch lies in `D`; it runs from

\[
p=(-\tfrac12,1)
\]

to

\[
q=(-1,\tfrac12).
\]

### Branch 2

For

\[
0\le\theta\le\frac\pi6,
\]

set

\[
\Gamma_+(\theta)
=\left(\cos(\theta-\frac{2\pi}3),\cos\theta\right).
\tag{5.3}
\]

This is the second root of (5.1) that lies inside `D`. It runs from `p` to the slanted-boundary point

\[
s=(0,\sqrt3/2).
\]

The remaining factor `2y-1` in (1.1) contributes only `q`, because the transformed domain degenerates to `x=-1` when `y=1/2`. Therefore

\[
\boxed{Z_K=\Gamma_-\cup\Gamma_+.}
\tag{5.4}
\]

### Physical-coordinate interpretation

Return to the physical fundamental triangle

\[
0\le u_1\le\frac12,
\qquad
0\le u_2\le\frac{u_1}{\sqrt3},
\]

with

\[
x=\cos(2\pi u_1),\qquad
 y=\cos(2\pi u_2/\sqrt3).
\]

Writing

\[
\theta=2\pi u_2/\sqrt3,
\]

branch (5.2) becomes the **straight line segment**

\[
\boxed{
 u_1=\frac13+\frac{u_2}{\sqrt3},
 \qquad 0\le u_2\le\frac{\sqrt3}{6}.
}
\tag{5.5}
\]

Branch (5.3) becomes the second straight line segment

\[
\boxed{
 u_1=\frac13-\frac{u_2}{\sqrt3},
 \qquad 0\le u_2\le\frac{\sqrt3}{12}.
}
\tag{5.6}
\]

Thus the algebraic zero-response conic is not geometrically mysterious: in physical `A2` coordinates it is a pair of straight torsion chords meeting at the interpolation point `p`.

### Consequence 5.1

Every witness on the `D=0` face has **exactly the same residual on these two chords**, because `K_C=0` there. Therefore

\[
\boxed{
R_0\ge0\text{ on the two physical segments (5.5)--(5.6)}
}
\tag{5.7}
\]

is an unavoidable branch-independent necessary condition for the entire proposed first atlas cell.

This isolates a one-dimensional theorem that can be proved independently with Jacobi-theta or total-positivity methods. Failure on either segment would kill the whole `D=0` face; success removes the only singular set in the envelope criterion.

## 6. B5: active-contact continuation without differentiating the optimizer

Let

\[
Q(\tau,z)=\frac{R_0(\tau,z)}{K(z)}
\]

on a fixed sign component of `K`.

Suppose, on a parameter interval, that `C_+` is realized at a unique nondegenerate interior minimizer `z_+(tau)` in `{K>0}`. Then

\[
\nabla_zQ(\tau,z_+(\tau))=0.
\]

Differentiating the value `C_+(tau)=Q(tau,z_+(tau))` and using stationarity cancels the derivative of the moving optimizer:

\[
\boxed{
\frac{dC_+}{d\tau}
=\frac{\partial_\tau R_0(\tau,z_+(\tau))}{K(z_+(\tau))}
=\frac{[(I-\Pi)\mathcal L U](\tau,z_+(\tau))}{K(z_+(\tau))}.
}
\tag{6.1}
\]

The same formula holds for a unique nondegenerate maximizer realizing `C_-`.

This is the envelope theorem specialized to the exact projected heat flow. It is valuable because continuation of the scalar feasibility gap

\[
G(\tau):=C_+(\tau)-C_-(\tau)
\tag{6.2}
\]

can be studied using only the heat-evolved residual evaluated at the active contacts.

### Slanted-boundary branch

The previous run proposed an active contact on the Weyl boundary

\[
z_s=(T_3(s),s),\qquad \frac12<s<1.
\]

Define

\[
Q_b(\tau,s)
=\frac{R_0(\tau,T_3(s),s)}{K(T_3(s),s)}.
\]

A nonendpoint active contact satisfies

\[
\partial_sQ_b(\tau,s)=0.
\tag{6.3}
\]

If

\[
\partial_{ss}Q_b(\tau_0,s_0)\ne0,
\]

then the implicit-function theorem gives a unique local branch `s=s(tau)` and

\[
\boxed{
 s'(\tau)
=-\frac{\partial_{\tau s}Q_b}{\partial_{ss}Q_b}.
}
\tag{6.4}
\]

Because `partial_s Q_b=0` along the branch,

\[
\boxed{
 \frac{d}{d\tau}Q_b(\tau,s(\tau))
 =\partial_\tau Q_b(\tau,s(\tau)).
}
\tag{6.5}
\]

Equations (3.5), (6.4), and (6.5) give the exact differential continuation system requested by B5. A rigorous parameter-cell proof can therefore be organized around sign bounds for a finite collection of scalar quantities rather than repeatedly solving a two-dimensional optimization problem from scratch.

## 7. What this does and does not prove

The note proves four exact facts:

1. the forced contacts define a fixed linear projector `Pi`, and the complete two-parameter residual is (2.4);
2. the normalized Gaussian parameter is an exact heat-flow time, `partial_tau U=L U`;
3. on `D=0`, global continuum feasibility is exactly equivalent to the scalar envelope gap (4.5) plus positivity on the fixed zero-response skeleton;
4. that skeleton is exactly two straight physical torsion segments, and nondegenerate active contacts have the continuation equations (6.1)--(6.5).

It does **not** prove that the skeleton residual is nonnegative for every `a`, that `C_-<=C_+` for every `a`, or that the active contacts have one fixed combinatorial type globally. Those are now the sharply isolated missing statements.

In particular, the frozen metric remains

\[
 m_{\rm sq}=2.
\]

A proof that (4.4), (4.5), and the coefficient constraints hold for every `a>0` would prove all-Gaussian `omega*_9` optimality within the Hardin--Tenpas framework; the Bernstein-mixture step would then still have to be written carefully to move the frozen metric to `m_sq=3`.

## 8. Next exact attack suggested by the reduction

The next run should not return to a two-dimensional blind search. The natural order is:

1. prove the branch-independent chord inequality (5.7) for all Gaussian parameters, preferably by rewriting the physical restriction to (5.5)--(5.6) as one-dimensional theta functions;
2. prove an active-set localization theorem showing where the extrema in (4.2)--(4.3) occur (the slanted boundary/top-left corner are the first candidates, but this must be proved rather than inferred from numerics);
3. use (3.5) and (6.1)--(6.5) to certify overlap of consecutive parameter cells by signs of scalar derivatives.

These are theorem-sized obligations. A numerical optimizer or a sampled residual grid cannot substitute for them.

## 9. Dated source-status note

Checked 2026-09-18. Hardin--Tenpas, *Universally Optimal Periodic Configurations in the Plane*, Discrete Analysis 2025:26 / arXiv:2307.15822, proves the four-point `A2` case and a distinct six-point periodic case, not `omega*_9` or the global two-dimensional conjecture. Thomas Leble, arXiv:2511.03353 (2025), proves universal **local** optimality of the hexagonal lattice among all point configurations, not global universal optimality. Serfaty's *Lectures on Coulomb and Riesz Gases* has a 2026 AMS book edition; the canonical R7-06 source locator remains the accessible arXiv preliminary version's Conjecture 11.1. A bounded fresh search found no later theorem settling the global dimension-two Cohn--Kumar conjecture or the specific `omega*_9` milestone. This is negative search evidence only, not a novelty certificate.
