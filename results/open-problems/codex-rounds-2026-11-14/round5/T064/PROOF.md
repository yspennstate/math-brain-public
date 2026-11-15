# The determinant-weighted random wave at a saddle

All lengths have wavenumber one. The field has covariance
\(J_0(|x-y|)\), and \(\phi(t)=e^{-t^2/2}/\sqrt{2\pi}\).
Total variation is \(d_{\rm TV}(P,Q)=\sup_E|P(E)-Q(E)|\).

Let \(\mathbb P_t\) be the Gaussian conditional law given
\(f(0)=t,\nabla f(0)=0\). Define its saddle Palm law by

\[
 \mathbb E_t^*[H(f)]
 =\frac{\mathbb E_t[(-\det\nabla^2f(0))_+H(f)]}
              {e^{-t^2}/4}.                                      \tag{1}
\]

This is the normalized determinant weighting used to count saddles
of height \(t\) by Kac–Rice. It is not conditioning on crossing
pivotality. Formula (1) fixes its meaning, including at every specified
level rather than only almost every level.

## Proposition

Take independent random variables \(G,\Theta,(a_n,b_n)_{n\geq3}\),
where \(G\) has density \(g e^{-g}\), \(g>0\), \(\Theta\) is
uniform on \([0,2\pi)\), and the \(a_n,b_n\) are standard normals.
Then the field under \(\mathbb P_t^*\) has the representation

\[
 F_t(r,\theta)=tJ_0(r)
    +2\sqrt{t^2+G}\,J_2(r)\cos(2\theta-\Theta)
    +\sqrt2\sum_{n=3}^{\infty}J_n(r)
                     (a_n\cos n\theta+b_n\sin n\theta).            \tag{2}
\]

Use the same random variables for every \(t\), and set
\(H_t=F_t-tJ_0(|\cdot|)\). On every closed annulus
\(A=\{R\leq|x|\leq S\}\), \(0<R<S<\infty\),

\[
 d_{\rm TV}(\mathcal L(H_t|_A),\mathcal L(H_s|_A))
      =\delta(|t^2-s^2|),                                        \tag{3}
\]

where \(\delta(0)=0\) and, for \(a>0\),

\[
 \delta(a)=(1-e^{-a})\exp\!\left(-\frac{a}{e^a-1}\right)
       \leq \min(1,a/e),\qquad
 \delta(a)=\frac a e-\frac{a^3}{24e}+O(a^5).                       \tag{4}
\]

In contrast, for \(s\ne t\),

\[
 d_{\rm TV}(\mathcal L(F_t|_A),\mathcal L(F_s|_A))=1.              \tag{5}
\]

There is also a useful coupling in the uniform norm. Put
\(M_j(R)=\sup_{r\geq R}|J_j(r)|\), \(j=0,2\). The coupling (2)
satisfies

\[
 \mathbb E\sup_{|x|\geq R}|F_t(x)-F_s(x)|
 \leq |t-s|M_0(R)
       +\frac{\sqrt\pi}{2}|t^2-s^2|M_2(R).                        \tag{6}
\]

In particular the right side is
\(O((|t-s|+|t^2-s^2|)R^{-1/2})\) for \(R\geq1\), with an
absolute implied constant. The supremum is of the difference of two
fields sharing all higher modes; no boundedness of either field on the
whole plane is asserted.

## 1. Fourier modes and the first two jets

Use the real Fourier–Bessel representation

\[
 f(r,\theta)=a_0J_0(r)+\sqrt2\sum_{n=1}^{\infty}J_n(r)
                  (a_n\cos n\theta+b_n\sin n\theta),              \tag{7}
\]

with independent standard normal coefficients. Its normalization can
be checked from the Bessel addition identity:

\[
 J_0(r)J_0(s)+2\sum_{n\geq1}J_n(r)J_n(s)
          \cos(n(\theta-\psi))=J_0(|x-y|).
\]

Thus (7) is the variance-one field in the question. The representation
is also discussed in Section 2.1 of [2]; addition identities are in [3].
For completeness, convergence causes no hidden conditioning issue.
The defining series for \(J_n\) gives, for \(r\leq S\),

\[
 |J_n(r)|\leq (S/2)^n e^{S^2/4}/n!.
\]

For any \(\varepsilon>0\), the sum of probabilities that a Gaussian
coefficient exceeds \(e^{\varepsilon n}\) in absolute value is finite.
Hence almost surely all but finitely many coefficients satisfy that
bound. The factorial estimate gives locally uniform convergence.
The Cartesian series for \(J_n(r)e^{in\theta}\), obtained by replacing
\(r^ne^{in\theta}\) by \((x+iy)^n\), gives the same convergence for
every fixed number of derivatives: differentiation introduces only
polynomial factors in \(n\) and in the series index. It follows that
(7) and its finite-mode modifications define smooth fields and that
their jets and circular Fourier coefficients can be taken term by term.

The first terms are

\[
 J_0(r)=1-r^2/4+O(r^4),\quad
 J_1(r)=r/2+O(r^3),\quad J_2(r)=r^2/8+O(r^4).
\]

Since \(r^2\cos2\theta=x^2-y^2\) and
\(r^2\sin2\theta=2xy\),

\[
 f(0)=a_0,\qquad \nabla f(0)=(a_1,b_1)/\sqrt2,
\]

\[
 \nabla^2f(0)=
 \begin{pmatrix}
 -a_0/2+a_2/(2\sqrt2)&b_2/(2\sqrt2)\\
 b_2/(2\sqrt2)&-a_0/2-a_2/(2\sqrt2)
 \end{pmatrix}.                                                   \tag{8}
\]

In particular the trace is \(-f(0)\), as required by the Helmholtz
equation. Conditioning on the first jet sets \(a_0=t\), \(a_1=b_1=0\)
and leaves all coefficients of order at least two unchanged.

## 2. The determinant tilt

Under this Gaussian conditioning write

\[
 a_2=\sqrt{2U}\cos\Theta,\qquad b_2=\sqrt{2U}\sin\Theta.
\]

The polar-coordinate Jacobian in the two-dimensional standard normal
density gives independent \(U\sim\mathrm{Exp}(1)\) and uniform
\(\Theta\). Equation (8) gives

\[
 \det\nabla^2 f(0)=(t^2-U)/4.
\]

Its negative part has expectation

\[
 \frac14\int_{t^2}^{\infty}(u-t^2)e^{-u}\,du=e^{-t^2}/4.          \tag{9}
\]

After multiplying by this weight and dividing by (9), the density of
\(U\) is

\[
 (u-t^2)e^{-(u-t^2)}\,\mathbf1_{u>t^2}.
\]

Consequently \(U=t^2+G\) under the tilted law. The weight depends on
neither the angle nor the higher modes, so their independence is
preserved. Substitution in (7) proves (2).

Two further checks follow directly. At the distinguished saddle,

\[
 \det\nabla^2F_t(0)=-G/4,\qquad
 \lambda_\pm=(-t\pm\sqrt{t^2+G})/2.                               \tag{10}
\]

The eigenvalues have opposite signs for every real \(t\), almost
surely. At \(t=0\), ordinary first-jet conditioning would give
\(\mathbb E U=1\), whereas saddle counting gives \(\mathbb E U=2\).
Replacing the Palm field by that Gaussian conditioning therefore
changes its law even at zero level.

The gradient zero density is \(1/\pi\). Multiplying (9) by that
density and \(\phi(t)\) independently recovers the preceding report's
saddle height intensity

\[
 s(t)=\phi(t)e^{-t^2}/(4\pi).                                     \tag{11}
\]

## 3. Exact total variation

Let \(p(v)=v e^{-v}\mathbf1_{v>0}\). The latent variables for \(H_t\)
and \(H_s\) differ only in the translated gamma variable
\(U=t^2+G\) or \(U=s^2+G\). The angle and the higher coefficients
have a common independent law. Products with the same independent
law preserve total variation, and taking a measurable function cannot
increase it. It follows that the left side of (3) is at most
\(d_{\rm TV}(G+a,G)\), with \(a=|t^2-s^2|\).

This upper bound is attained by observing the field on the annulus.
Choose \(r\in(R,S)\) with \(J_2(r)\ne0\); such a radius exists since
\(J_2\) is analytic and not identically zero. Circular Fourier
integration of \(H_t\) gives

\[
 C=\frac1\pi\int_0^{2\pi}H_t(r,\theta)\cos2\theta\,d\theta
        =2\sqrt U J_2(r)\cos\Theta,
\]

\[
 D=\frac1\pi\int_0^{2\pi}H_t(r,\theta)\sin2\theta\,d\theta
        =2\sqrt U J_2(r)\sin\Theta.
\]

Thus \(U=(C^2+D^2)/(4J_2(r)^2)\) is a measurable function of the
restriction. This gives the reverse total variation inequality.

It remains to compute the one-dimensional distance. For \(a>0\),
the densities \(p(v)\) and \(p(v-a)\) cross once on \((a,\infty)\),
at

\[
 c=\frac{a}{1-e^{-a}},\qquad c-a=\frac{a}{e^a-1}.
\]

Indeed their ratio on that interval is
\(v e^{-a}/(v-a)\), strictly decreasing from infinity to \(e^{-a}\).
For \(v<c\) the original density is larger. Writing
\(P(v)=1-(1+v)e^{-v}\) for \(v\geq0\), the total variation distance
is the integral of the positive density difference,

\[
 P(c)-P(c-a)
 =(1-e^{-a})e^{-(c-a)}=\delta(a).
\]

To prove the bound without relying on the explicit formula, extend
\(p\) by zero to the negative axis. It is absolutely continuous and

\[
 \int_{\mathbb R}|p'(v)|\,dv=2/e,
\]

since it increases from zero to \(1/e\) on \([0,1]\), then decreases
to zero. The fundamental theorem of calculus and Tonelli give

\[
 \frac12\int|p(v)-p(v-a)|\,dv
 \leq\frac a2\int|p'(v)|\,dv=a/e.
\]

The bound by one is automatic. Finally,

\[
 \delta(a)=2\sinh(a/2)\exp[-(a/2)\coth(a/2)]
\]

has expansion \(a/e-a^3/(24e)+O(a^5)\), proving (4).
For \(s=0\), the distance is therefore \(t^2/e+O(t^6)\).

## 4. Coupling and the uncentered singularity

The shared-variable coupling in (2) gives the exact difference

\[
 F_t-F_s=(t-s)J_0(r)
 +2\big(\sqrt{G+t^2}-\sqrt{G+s^2}\big)J_2(r)
                              \cos(2\theta-\Theta).              \tag{12}
\]

Rationalization shows

\[
 2|\sqrt{G+t^2}-\sqrt{G+s^2}|
 \leq |t^2-s^2|/\sqrt G.
\]

Here \(G>0\) almost surely and
\(\mathbb E[G^{-1/2}]=\Gamma(3/2)=\sqrt\pi/2\). Taking the
supremum and expectation proves (6). The fixed-order asymptotics
\(J_j(r)=O(r^{-1/2})\), for \(j=0,2\), from [4] give the stated
large-radius rate.

To prove (5), choose a radius in \((R,S)\) at which \(J_0\ne0\).
Circular averaging of (2) gives exactly

\[
 \frac1{2\pi}\int_0^{2\pi}F_t(r,\theta)\,d\theta=tJ_0(r).
\]

This deterministic statistic distinguishes every pair of different
levels with probability one. Thus small uniform differences under a
coupling do not imply small total variation for the uncentered fields.

## 5. Use in a pivotal count and its remaining limitation

Let \(Q\) be a rectangle and let \(M(x,t,h)\) be any nonnegative
measurable mark, evaluated on the field translated so that the
distinguished saddle is at zero. Marked Kac–Rice, followed by (1),
gives

\[
 \mathbb E\sum_{\substack{x\in Q^\circ:\nabla f(x)=0\\
                          \det\nabla^2f(x)<0}}
       M(x,f(x),f(x+\cdot))
 =\int_{Q^\circ}\int_{\mathbb R}
       s(t)\,\mathbb E[M(x,t,F_t)]\,dt\,dx.                       \tag{13}
\]

The sum is over interior saddles. The one-point formula applies because
the gradient is nonsingular, the field is smooth, and the Gaussian
Hessian has finite moments. Bounded measurable marks follow from the
marked formula; nonnegative marks follow by monotone convergence.
More explicitly, its integrand before normalization is
\(p_{\nabla f(0)}(0)\phi(t)
\mathbb E_t[(-\det\nabla^2 f(0))_+M(x,t,f)]\).
Stationarity supplies this conditional law at every translated location.
Now \(p_{\nabla f(0)}(0)=1/\pi\), and (1) and (9) turn the
integrand into \(s(t)\mathbb E[M(x,t,F_t)]\), as displayed in (13).
There is no independence assumption about the mark or the Hessian.
Equation (13) is precisely the determinant-weighted form of the
conditional arm input, and (2) supplies its full field law.

For example, take the mark to be the indicator that \(x\) is the
unique crossing threshold location in \(Q\), and restrict its height
to a Borel set. The genericity and measurability facts from Lemma 2.9
of [1] justify this mark (give it value zero on nongeneric functions).
Then the contribution of interior threshold locations to the threshold
height density is, for almost every \(t\),

\[
 q_{\rm int}(t)=s(t)\int_{Q^\circ}
  \mathbb P\{0\text{ is the threshold location of }F_t
                         \text{ in }Q-x\}\,dx.                  \tag{14}
\]

The complete threshold law also has edge and corner contributions;
their domination from round 4 is retained. Dropping the probability
in (14) recovers its area bound.

For any fixed measurable field event \(E\) on an annulus, (3) yields
the rigorous comparison

\[
 |\mathbb P(F_t-tJ_0\in E)-\mathbb P(F_0\in E)|\leq\delta(t^2).
                                                                    \tag{15}
\]

However, arms emerging from the saddle at height \(t\) concern the
signs of \(F_t-t\), not of \(F_t-tJ_0\). In terms of \(H_t\),

\[
 F_t-t=H_t-t(1-J_0(r)).                                          \tag{16}
\]

Even after (15), the event has a varying radial level
\(t(1-J_0(r))\), asymptotic to \(t\), rather than zero. One may
transfer any specified measurable arm event at that radial level
from \(H_t\) to \(F_0\) with error at most \(\delta(t^2)\), but
cannot then replace the radial level by zero without another estimate.
Thus (3) does not supply a macroscopic arm bound, improve the
\(o(R^{-2})\) crossing-stability window, or establish RSW or a
conformal limit. No literature priority is asserted for these derived
identities.

## Sources opened

[1] Stephen Muirhead, Alejandro Rivera and Hugo Vanneuville, with an
appendix by Laurin Köhler-Schindler, *The phase transition for planar
Gaussian percolation models without FKG*,
[arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3).
Used for threshold genericity and measurability and for checking the
preceding report's strict-path argument.

[2] Dmitry Beliaev, *Gaussian fields and percolation*,
[arXiv:2207.13448](https://arxiv.org/abs/2207.13448), Section 2.1.
Used for the standard Fourier–Bessel representation.

[3] NIST Digital Library of Mathematical Functions,
[Section 10.23](https://dlmf.nist.gov/10.23), addition identities, and
[Section 10.2](https://dlmf.nist.gov/10.2), defining series.

[4] NIST Digital Library of Mathematical Functions,
[Section 10.17](https://dlmf.nist.gov/10.17), fixed-order large-argument
Bessel asymptotics.
