# QFORM-CUBE-HOUSEHOLDER-BALL-DOMINATION-v1

Run: `20260924T101607Z-account03-B17-QFORM-auto11`  
Worker: `account03/B17` (Sharp constant and witnesses)  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Fresh control used: `yspennstate/math-research-brain@74bc5221e13544c025e96616cf8c563bcffbdeeb`, OWNER CONTROL revision `2026-09-22.15`.  
Status: supporting theorem proved; full QFORM remains OPEN. Essential boundedness is proved for the family below; continuity of the cube pushforward is not claimed.

## 1. Statement

Let
\[
C=[-1/2,1/2]^3,\qquad X\sim {\rm Unif}(C),
\]
so the three physical coordinates are independent cap-one laws. Let \(B\) be any real symmetric orthogonal \(3\times3\) matrix with signature \((2,1)\), equivalently
\[
B=I-2nn^\top,\qquad |n|=1.
\]
Then \(B\) has spectrum \(\{1,1,-1\}\), so it is an exact target matrix with three eigenvalues of absolute value one. The law of
\[
Q=X^\top B X
\]
is absolutely continuous and
\[
\boxed{\|p_Q\|_\infty\le \pi\sqrt{\frac32}
      =3.847649490485592\ldots .}
\]
The same conclusion, after reflecting the output, holds for signature \((1,2)\).

In particular, the canonical fully coupled reflection
\[
n=\frac1{\sqrt3}(1,1,1),\qquad
B_*=\frac13
\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix}
\]
has every matrix entry nonzero, yet its cube-input output density obeys the same global all-output bound.

This is a stress-family theorem, not the full arbitrary-law conjecture.

## 2. First essential implication: dominate the cube pushforward by a rotationally invariant ball

Put
\[
R=\frac{\sqrt3}{2},\qquad D_R=\{x\in\mathbb R^3:|x|\le R\}.
\]
The cube \(C\) lies inside \(D_R\). For every Borel set \(E\subset\mathbb R\), define the finite pushforward measures
\[
\nu_C(E)=\int_C {\bf1}_{\{x^\top Bx\in E\}}\,dx,
\qquad
\nu_D(E)=\int_{D_R}{\bf1}_{\{x^\top Bx\in E\}}\,dx.
\]
Pointwise inclusion gives
\[
\nu_C(E)\le \nu_D(E)\qquad\text{for every Borel }E.
\]
Notice that \(\nu_D\) is deliberately not normalized to be a probability measure; it is only a positive dominating measure.

Because the ball is rotation invariant, we may diagonalize \(B\) only inside the calculation of \(\nu_D\):
\[
x^\top Bx \longmapsto x_1^2+x_2^2-x_3^2.
\]
This does **not** rotate the independent cube law and therefore does not use any false post-rotation independence premise.

It remains to compute the ball pushforward density exactly.

## 3. Exact ball density

Use spherical variables \(x=r\omega\), \(0\le r\le R\), \(\omega\in S^2\), and write
\[
t=\omega_3,\qquad h(t)=1-2t^2.
\]
Since \(d\omega=2\pi\,dt\), for \(q\ne0\) the delta-function/coarea identity gives
\[
p_D(q)
=
\frac{\sqrt{|q|}}2
\int_{\substack{\operatorname{sgn}h=\operatorname{sgn}q\\
|h|\ge |q|/R^2}}
|h|^{-3/2}\,d\omega.
\]
Indeed, for fixed \(\omega\), the radial root is
\(r_0=\sqrt{q/h}\), and
\[
\int_0^R \delta(q-r^2h)r^2\,dr
=
\frac{r_0}{2|h|}
=
\frac{\sqrt{|q|}}{2|h|^{3/2}},
\]
provided \(q/h>0\) and \(r_0\le R\).

### Positive output

For \(0<q<R^2\), put
\[
\delta=\frac q{R^2},\qquad
a=\sqrt{\frac{1-\delta}{2}}.
\]
Then \(h>0\) exactly for \(|t|<1/\sqrt2\), and the radial cutoff leaves \(|t|\le a\). Since
\[
\int_{-a}^a(1-2t^2)^{-3/2}\,dt
=
\frac{2a}{\sqrt\delta},
\]
we obtain
\[
\boxed{
p_D(q)=\pi\sqrt2\,R\sqrt{1-\frac q{R^2}} .
}
\]
This is decreasing in \(q\).

### Negative output

For \(q=-r\), \(0<r<R^2\), put
\[
\delta=\frac r{R^2},\qquad
a=\sqrt{\frac{1+\delta}{2}}.
\]
Now the allowed set is \(|t|\ge a\), and
\[
\int_a^1(2t^2-1)^{-3/2}\,dt
=
\frac a{\sqrt\delta}-1.
\]
Accounting for both signs of \(t\),
\[
\boxed{
p_D(-r)=
\pi\sqrt2\,R\sqrt{1+\frac r{R^2}}
-2\pi\sqrt r .
}
\]
After division by \(\pi\sqrt2 R\), this branch is
\[
F(\delta)=\sqrt{1+\delta}-\sqrt{2\delta},
\qquad 0<\delta<1.
\]
Its derivative is
\[
F'(\delta)=\frac1{2\sqrt{1+\delta}}
-\frac1{\sqrt{2\delta}}<0,
\]
so the negative branch is also maximized as \(r\downarrow0\).

Consequently the ball density has the global cap
\[
\|p_D\|_\infty
=
\pi\sqrt2\,R
=
\boxed{\pi\sqrt{\frac32}}.
\]
As a normalization check, integrating the two displayed branches over
\([-R^2,R^2]\) gives \(4\pi R^3/3\), the volume of the ball.

## 4. Transfer from ball back to cube

The ball pushforward is absolutely continuous. Since
\(\nu_C\le\nu_D\) as finite measures, Radon--Nikodym domination implies
\[
\nu_C\ll {\rm Leb},\qquad
0\le p_Q(s)\le p_D(s)\quad\text{for a.e. }s.
\]
Therefore
\[
\boxed{
\|p_Q\|_\infty\le\pi\sqrt{\frac32}.
}
\]

This step proves absolute continuity of the cube output directly. It does **not**
show that its density has a continuous representative; continuity remains
unclaimed for this branch, consistent with the programme's separate regularity
question.

## 5. Exact partner application and witness separation

The completed designated-partner result
`account04/B17`, theorem
`QFORM-MACROFRAGMENTED-STRICTSLACK-DENSE-WITNESS-v1`,
is source-pinned at

`yspennstate/math-open-problems@4be63022324b82f254f1d7a4353a3e883f08d10a`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260924T011922Z-account04-B17-QFORM-r6/REPORT.md`.

It constructs exact admissible dense matrices with spectrum
\(\{1,1,-(1+1/m)\}\) and cap-one fragmented independent laws for which,
at \(\theta=0.01\),
\[
\liminf_m\|p_{Q_m}\|_\infty
\ge
3\sqrt2\,e^{-0.03}
=
4.117251705266084\ldots>4.
\]

Applying that completed partner result to the present theorem gives the actual
strict witness inequality
\[
\boxed{
\sup_{\substack{B=B^\top,\ B^2=I\\ \operatorname{spec}B=\{1,1,-1\}}}
\|p_{X^\top BX}\|_\infty
\le
\pi\sqrt{\frac32}
<
4
<
3\sqrt2 e^{-0.03}
\le C_* ,
}
\]
where \(X\) is the centered unit-cube product law and \(C_*\) denotes the optimal
universal constant, if finite.

The elementary middle certificate
\(\pi\sqrt{3/2}<4\) follows, for example, from
\(\pi<22/7\) and
\[
\frac32\left(\frac{22}{7}\right)^2<16.
\]

Thus the complete three-variable centered-cube orbit of the boundary spectrum
\((1,1,-1)\), including genuinely fully coupled rotations, is **not** extremal:
a source-valid fragmented higher-dimensional family already forces a strictly
larger universal constant. Letting the partner's \(\theta\downarrow0\) recovers
the known source-valid obstruction \(C_*\ge3\sqrt2\).

## 6. What this rules out, and what it does not

This theorem is global in the output level and uniform over every spectral
orientation of the exact signature \((1,1,-1)\). It rules out a broad and
natural rotated witness class without assuming independence after rotation.

It does not:
- cover arbitrary cap-one laws in three variables;
- cover unequal spectral magnitudes;
- prove the unrestricted universal upper bound;
- prove that \(3\sqrt2\) is the sharp universal constant;
- prove continuity of the cube pushforward density.

The next sharp-witness mechanism should therefore leave at least one of these
features: centered unit-cube input, three-dimensionality, or exact orthogonal
signature. The most relevant remaining stress directions are fragmented rough
laws under genuinely coupled rotations, non-orthogonal spectral magnitudes,
and additional active spectrum.

## 7. Correction compliance

No step uses:
- law-uniform pointwise van-der-Corput decay;
- post-rotation independence of eigen-coordinates;
- an arbitrary-joint rank-three coarea bound;
- a positive conditional projection-density moment;
- naive fiber-supremum integration;
- Monte Carlo extremality.

The only rotation occurs in the rotationally invariant **dominating ball**,
where no product-independence assertion is made.
