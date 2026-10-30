SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-24T01:18:28Z.
attacking: a fully coupled three-variable zero-physical-pivot Householder family, with arbitrary cap-one product inputs, globally in the output level.

# QFORM-B17 report: exact zero-pivot Householder branch

Status: **SUPPORTING TARGET-LEVEL BRANCH**. The full QFORM conjecture remains OPEN / NOT PROVED. The full continuity conclusion also remains open.

## 1. The exact family

Let \(X,Y,Z\) be independent real random variables with probability densities \(f_X,f_Y,f_Z\) satisfying \(0\le f\le1\). Let

\[
 n=(n_1,n_2,n_3),\qquad |n|=1,\qquad n_2^2=\frac12,
\]

and define the symmetric Householder involution

\[
 B=I_3-2nn^T.
\]

Then \(B^2=I_3\), so its spectrum is exactly \(\{1,1,-1\}\). The physical pivot in the second coordinate vanishes:

\[
 B_{22}=1-2n_2^2=0.
\]

Write

\[
 a=B_{12}=-2n_1n_2,\qquad d=B_{23}=-2n_2n_3.
\]

Because \(n_1^2+n_3^2=1/2\),

\[
 a^2+d^2=4n_2^2(n_1^2+n_3^2)=1.
\]

Define the orthogonal physical two-coordinate change

\[
 u=aX+dZ,\qquad v=-dX+aZ.
\]

This is **not** used to claim independence of \(u,v\). It is only a deterministic change of variables in the two-coordinate product law. Since the Jacobian is one, the joint density

\[
 \rho(u,v)=f_X(au-dv)f_Z(du+av)
\]

satisfies \(0\le\rho\le1\) and has total mass one.

The \(XZ\) principal block of \(B\) equals \(I_2-ww^T\), where \(w=(a,d)\). Hence in the \((u,v)\) coordinates it is \(\operatorname{diag}(0,1)\). Therefore the quadratic form is exactly

\[
 \boxed{Q=(X,Y,Z)^TB(X,Y,Z)=v^2+2uY.}
\]

This family is genuinely fully coupled whenever \(ad\ne0\): then \(B_{12},B_{13},B_{23}\ne0\). No rotation of the random vector is assumed to preserve independence.

## 2. Marginal cap retained in the coupling coordinate

Let \(g\) be the density of \(u=aX+dZ\). Since convolution cannot increase an \(L^\infty\) norm,

\[
 \|g\|_\infty\le \min\left\{\frac1{|a|},\frac1{|d|}\right\}
 =\frac1m,
 \qquad m:=\max(|a|,|d|).
\]

Because \(a^2+d^2=1\),

\[
 \frac1{\sqrt2}\le m\le1,
 \qquad
 1\le M:=\frac1m\le\sqrt2.
\]

This is the product-law input that replaces an unjustified arbitrary-joint coarea claim.

## 3. Exact conditional density kernel and two competing bounds

For \(u\ne0\), conditioning on \((u,v)\) gives the density

\[
 p_{Q\mid u,v}(q)=\frac1{2|u|}
 f_Y\!\left(\frac{q-v^2}{2u}\right).
\]

Since \(u\) has a density, \(P(u=0)=0\). Therefore

\[
 p_Q(q)=\int_{\mathbb R}\frac{J_q(u)}{2|u|}\,du,
\qquad
J_q(u):=\int_{\mathbb R}\rho(u,v)
 f_Y\!\left(\frac{q-v^2}{2u}\right)dv.
\]

Two bounds are available simultaneously.

First, \(f_Y\le1\) gives

\[
 J_q(u)\le\int\rho(u,v)dv=g(u).
\]

Second, \(ho\le1\) gives

\[
 J_q(u)\le\int_{\mathbb R}
 f_Y\!\left(\frac{q-v^2}{2u}\right)dv.
\]

With \(y=(q-v^2)/(2u)\), the two roots in \(v\) give the one-sided kernel

\[
 \sqrt{2|u|}\,|y-y_0|^{-1/2}.
\]

Because \(f_Y\) is a probability density with \(0\le f_Y\le1\), the one-dimensional bathtub inequality for the decreasing kernel \(s^{-1/2}\) yields

\[
 \int f_Y\!\left(\frac{q-v^2}{2u}\right)dv
 \le2\sqrt{2|u|}.
\]

Hence, uniformly in \(q\),

\[
 \boxed{
 p_Q(q)\le
 \int_{\mathbb R}
 \min\left\{
 \frac{g(u)}{2|u|},
 \frac{\sqrt2}{\sqrt{|u|}}
 \right\}du.}
\]

## 4. A sharp one-dimensional water-filling upper bound

Set

\[
 c(u)=\frac1{2|u|},\qquad
 t(u)=2\sqrt2\sqrt{|u|}.
\]

Then the integrand is

\[
 c(u)\min\{g(u),t(u)\}.
\]

Define \(h(u)=\min\{g(u),t(u)\}\). We have

\[
 0\le h(u)\le k(u):=\min\{M,t(u)\},
 \qquad
 \int h\le\int g=1.
\]

Since \(c(u)\) is even and strictly decreasing in \(|u|\), the ordinary bathtub principle for the linear functional \(\int c h\) shows that the largest possible value is obtained by filling the capacity \(k\) on the centered interval \([-R,R]\) until total mass one is used.

The crossover \(t(u)=M\) occurs at

\[
 u_0=\frac{M^2}{8}.
\]

For \(1\le M\le\sqrt2\), the mass in the saturated core is

\[
 2\int_0^{u_0}2\sqrt2\sqrt u\,du
 =\frac{M^3}{6}<1.
\]

Thus \(R>u_0\), and the mass constraint gives

\[
 \frac{M^3}{6}+2M(R-u_0)=1,
\]

hence

\[
 R=\frac{M^3+12}{24M}.
\]

The resulting density bound is

\[
\begin{aligned}
 p_Q(q)
 &\le
 2\int_0^{u_0}\frac{\sqrt2}{\sqrt u}\,du
 +2\int_{u_0}^{R}\frac{M}{2u}\,du\\
 &=2M+M\log\frac{R}{u_0}\\
 &=\boxed{
 B(M):=M\left[2+\log\left(\frac{M^3+12}{3M^3}\right)\right].}
\end{aligned}
\]

This bound is global in the output level \(q\).

## 5. Worst orientation and strict sub-\(3\sqrt2\) ceiling

Different zero-pivot Householder orientations correspond to \(M\in[1,\sqrt2]\). Differentiate:

\[
 B'(M)=2+\log\left(\frac{M^3+12}{3M^3}\right)-\frac{36}{M^3+12}.
\]

Writing \(x=M^3\), the last expression is

\[
 H(x)=2+\log\frac{x+12}{3x}-\frac{36}{x+12},
\]

with

\[
 H'(x)=\frac{24(x-6)}{x(x+12)^2}<0
 \qquad(1\le x\le2\sqrt2).
\]

Thus it suffices to check \(x=2\sqrt2\). Put

\[
 r=\sqrt2+\frac13>1.
\]

Using the elementary inequality \(\log r>2(r-1)/(r+1)\),

\[
 B'(\sqrt2)
 >\frac{4r}{r+1}-\frac{18}{6+\sqrt2}
 =\frac{422-297\sqrt2}{17}>0,
\]

because \(422^2-2\cdot297^2=1666>0\). Therefore \(B\) is increasing on the full admissible interval and

\[
 \boxed{
 \|p_Q\|_\infty
 \le C_{\rm ZPH}:=
 \sqrt2\left[2+\log\left(\sqrt2+\frac13\right)\right]
 =3.617859563383761\ldots.}
\]

Moreover \(\sqrt2+1/3<2<e\), so

\[
 C_{\rm ZPH}<3\sqrt2.
\]

Numerically the proved gap is

\[
 3\sqrt2-C_{\rm ZPH}=0.6247811237355245\ldots .
\]

The maximally mixed orientation is attained by

\[
 n=\left(\frac12,\frac1{\sqrt2},\frac12\right),
\]

for which

\[
 B=
 \begin{pmatrix}
 1/2&-1/\sqrt2&-1/2\\
 -1/\sqrt2&0&-1/\sqrt2\\
 -1/2&-1/\sqrt2&1/2
 \end{pmatrix}.
\]

Every off-diagonal entry is nonzero and the spectrum is exactly \(\{1,1,-1\}\).

## 6. Affine stability and ambient conditioning

The same proof tolerates arbitrary affine terms. After the \((X,Z)\mapsto(u,v)\) change, an affine perturbation has the form

\[
 \ell_u u+\ell_v v+\ell_Y Y+c.
\]

Translate \(u\) to absorb \(\ell_Y Y\), translate \(v\) to complete the square in \(v\), and retain \(\ell_u u\) as an \(u\)-dependent output shift. These translations preserve the joint cap \(\rho\le1\) and the marginal cap \(g\le M\), while the preceding estimates are uniform in the target level. Hence the same constant applies to \(Q+\ell\cdot(X,Y,Z)+c\).

Consequently, if such a \(3\times3\) physical principal block appears inside a larger form, conditioning on all other original independent coordinates produces only affine perturbations in this block and therefore gives the same conditional density ceiling. Averaging preserves the bound. This is a genuine target-level branch, but the bare three-large-eigenvalue hypothesis does not force such a principal block.

## 7. Completed partner result applied to an actual inequality

Use fleet04/B17's completed theorem `QFORM-EDGEWORTH-FRAME-DEFICIT-SHARP-v1`, scientific source

`yspennstate/math-open-problems@092be154e735f99a60d80dff46b648ae7bae01b7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260922T201827Z-fleet04-B17-QFORM-r2/REPORT.md`.

For a Householder matrix \(I-2nn^T\), the negative spectral coordinate weights are \(t_j=n_j^2\) and \(s_j=1-t_j\). At the maximally mixed zero-pivot orientation

\[
 (t_1,t_2,t_3)=\left(\frac14,\frac12,\frac14\right),
\]

so

\[
 \boxed{\sum_j s_jt_j=1-\sum_jt_j^2=1-\frac38=\frac58.}
\]

Therefore the partner's displayed periodic-frame inequality specializes to the strict extra sign-mixing deficit

\[
 \boxed{
 -\frac{\gamma_*}{20m}\sum_j s_jt_j
 =-\frac{\gamma_*}{32m},
 \qquad
 \gamma_*:=\frac{15}{4}-\sqrt{\frac{171}{32}}>0.}
\]

Numerically \(\gamma_*/32=0.04494827340270731\ldots\). Thus the same orientation is also penalized, rather than enhanced, in the partner's diffuse periodic Edgeworth regime. This is an actual application of a completed partner inequality, not a citation-only dependency.

## 8. Scope and remaining witness frontier

The theorem proves a uniform global density ceiling for every exact three-variable Householder involution having one zero physical diagonal, for arbitrary independent cap-one laws, and for arbitrary affine perturbations. It rules out this fully coupled zero-pivot mechanism as a source of a witness reaching the current lower frontier \(3\sqrt2\).

It does **not** prove the full conjecture: a general target matrix need not contain such an exact principal block; near-zero pivots, several additional spectral directions, and fully coupled three-row blocks away from the involution/zero-pivot algebra remain. Essential boundedness is proved in the stated branch. Continuity for arbitrary rough input densities is **not claimed** here.

No Gaussian, log-concavity, moment, compact-support, connected-support, post-rotation independence, arbitrary-joint coarea theorem, pointwise van-der-Corput decay, or Monte Carlo histogram is used.
