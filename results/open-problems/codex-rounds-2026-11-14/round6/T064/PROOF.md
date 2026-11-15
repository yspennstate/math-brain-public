# Arm stability at the height of a conditioned saddle

Lengths have wavenumber one. Put \(\phi(v)=e^{-v^2/2}/\sqrt{2\pi}\),
and let \(A_{R,S}=\{x:R\leq |x|\leq S\}\), where \(0<R<S\).
The event \(\mathcal A(g,v;R,S)\) means that four pairwise disjoint
paths join the two boundary circles, in alternating cyclic order,
two in \(\{g>v\}\) and two in \(\{g<v\}\). Endpoints belong to the
circles. The paths, including their endpoints, satisfy strict signs.
Equivalently one can use polygonal paths with endpoints in boundary
arcs and then take countable unions and intersections; this also gives
measurability. Only invariance under an orientation-preserving
homeomorphism of the annulus preserving each boundary component is
used below.

Let \(F_t\) have the normalized saddle determinant law from round 5:

\[
 F_t=tJ_0(r)+2\sqrt{t^2+G}J_2(r)\cos(2\theta-\Theta)
       +\sqrt2\sum_{n\geq3}J_n(r)(a_n\cos n\theta+b_n\sin n\theta),
 \qquad G\sim\operatorname{Gamma}(2,1).                    \tag{1}
\]

All variables on the right are independent; the angle is uniform and
the coefficients are standard normals. Define the own-height arm
probability

\[
 p_*(t;R,S)=\mathbb P\{\mathcal A(F_t,t;R,S)\}.
\]

This is the saddle law, not the law conditioned on crossing pivotality.

## Proposition

There are absolute constants \(R_0\geq1\) and \(C<\infty\) with the
following properties. For \(S>R\geq R_0\), there are nonnegative
explicit Gaussian conditional-moment densities \(k_2(r,v)\) and
\(k_1(r,v)\), given in (7)–(8), such that, with
\(I_t=[\min(0,t),\max(0,t)]\),

\[
\begin{split}
 |p_*(t;R,S)-p_*(0;R,S)|\leq {}&\delta(t^2)\\
 &+\int_{I_t}\left[2\pi\int_R^S r k_2(r,v)\,dr
                 +2\pi R k_1(R,v)+2\pi S k_1(S,v)\right]dv,
                                                               \tag{2}
\end{split}
\]

where

\[
 \delta(a)=(1-e^{-a})\exp[-a/(e^a-1)]\leq a/e,
 \qquad \delta(0)=0.
\]

Uniformly for \(|v|\leq1\) and \(r\geq R_0\),

\[
 |k_2(r,v)-\alpha(v)|+|k_1(r,v)-\beta(v)|\leq Cr^{-1/2},       \tag{3}
\]

where

\[
 \alpha(v)=\frac{\phi(v)}{4\pi}(v^2-1+2e^{-v^2}),\qquad
 \beta(v)=\frac{\phi(v)e^{-v^2}}{2\pi}
              +\frac{v\phi(v)\operatorname{erf}(v)}{2\sqrt\pi}.
\]

More precisely, uniformly in the same range,

\[
 \begin{split}
 k_2(r,v)&=\alpha(v)+(v^2-1)\alpha(v)J_0(r)+O(r^{-1}),\\
 k_1(r,v)&=\beta(v)-[\beta(v)+v\beta'(v)]J_0(r)+O(r^{-1}).
 \end{split}                                                   \tag{3a}
\]

Consequently, for \(|t|\leq1\), (2) is at most

\[
\begin{split}
 \delta(t^2)&+\pi(S^2-R^2)\int_{I_t}\alpha(v)\,dv
           +2\pi(R+S)\int_{I_t}\beta(v)\,dv\\
 &+C|t|\big[S-R+\sqrt R+\sqrt S+1\big].                     \tag{4}
\end{split}
\]

The same statements hold for any sign-connectivity event invariant
under the stated annular homeomorphisms. For fixed \(\lambda>1\),
\(S=\lambda R\), and \(t_R=o(R^{-2})\), the probabilities in (2)
differ by \(o(1)\). In particular the previous report's residual
comparison extends to arms measured at the saddle's own height on
these annuli. No decay of \(p_*(0;R,\lambda R)\) is asserted.
The constants \(R_0,C\) are proved to exist; no numerical values for
them are certified here.

## 1. Rechecking the saddle law

The ordinary first-jet-conditioned Gaussian field at height zero is

\[
 h=\sqrt2\sum_{n\geq2}J_n(r)(a_n\cos n\theta+b_n\sin n\theta).
                                                               \tag{5}
\]

Write \(A=a_2,B=b_2,U=(A^2+B^2)/2\). Under this Gaussian law,
\(U\) is exponential with mean one. At height \(t\), the Hessian
determinant is \((t^2-U)/4\). Its saddle-weighted normalizer is

\[
 \tfrac14\int_{t^2}^\infty(u-t^2)e^{-u}\,du=e^{-t^2}/4.
\]

The normalized density of \(U\) is therefore
\((u-t^2)e^{-(u-t^2)}\mathbf1_{u>t^2}\), which proves (1).
In particular, the zero-height saddle law is exactly

\[
 d\mathbb P_0^*=U\,d\mathbb P_h.                              \tag{6}
\]

This identity is essential in the critical-value count. Dropping the
weight \(U\) would count the wrong conditional field.

For completeness, the density of \(G\) is \(q(g)=ge^{-g}\) on the
positive axis. The two densities \(q(u)\), \(q(u-a)\) cross at
\(c=a/(1-e^{-a})\). Their positive difference integrates to
\((1-e^{-a})e^{-a/(e^a-1)}\). Thus the residual fields
\(F_t-tJ_0\) and \(F_0\) have total variation at most \(\delta(t^2)\).
Equality follows by recovering their second circular Fourier mode,
as in round 5, but the upper bound suffices here.

## 2. The radial division and the exact densities

Put \(w(r)=1-J_0(r)\). The spectral integral for \(J_0\) is the
average of \(\cos(r\cos\vartheta)\). For every \(r>0\), this is
strictly less than one, since the integrand is at most one and is
strictly smaller on a set of positive measure. Thus \(w>0\).
Define \(Y=h/w\). Under the measure (6), this is \(F_0/w\).

All expectations and densities in this section refer to the Gaussian
law (5). At \(x=(r,0)\), use the orthonormal radial and tangential
directions \(e_r,e_\tau\). Write \(h_r,h_\tau\) for directional
derivatives and \(D^2h\) for the Cartesian Hessian. Set

\[
\begin{split}
 k_2(r,v)={}&w(r)\,p_{(h,\nabla h)}(vw,v\nabla w)\\
 &\quad\times\mathbb E\left[U\,|\det(D^2h-vD^2w)|
             \mid h=vw,\nabla h=v\nabla w\right].              \tag{7}
\end{split}
\]

For the circle of radius \(r\), parameterized by arclength, let

\[
 h_{ss}=e_\tau^TD^2h\,e_\tau-h_r/r.
\]

The curvature term \(-h_r/r\) is part of this derivative. It occurs
on both circles, independent of the orientation of their arclength
parameterizations. Define

\[
 k_1(r,v)=w(r)\,p_{(h,h_\tau)}(vw,0)
       \mathbb E[U|h_{ss}|\mid h=vw,h_\tau=0].                 \tag{8}
\]

These formulas specify finite-dimensional Gaussian integrals, not
unknown arm probabilities. Their covariance matrices are determined
by (5), or by subtracting modes zero and one from stationary RPW
jet covariances. Rotating the point rotates \((A,B)\) orthogonally;
\(U\) is invariant. Hence these densities depend only on \(r,v\).

Here are the Jacobian factors. Conditional on \(Y=v\),
\(\nabla Y=(\nabla h-v\nabla w)/w\). Hence the joint density of
\((Y,\nabla Y)\) at \((v,0)\) is \(w^3\) times that in (7).
At a critical point,

\[
 D^2Y=(D^2h-vD^2w)/w.
\]

The absolute determinant contributes \(w^{-2}\), leaving \(w\).
On a circle \(w\) is constant. The joint density of \((Y,Y_s)\)
has factor \(w^2\), and \(|Y_{ss}|=|h_{ss}|/w\), again leaving
\(w\). In particular there is no additional radial derivative of
\(w\) in (8).

Weighted one-point Kac–Rice, with mark \(U\), now gives the expected
number of all stratified critical points of \(Y\) whose values lie
in an interval \(I\), under (6):

\[
 \int_I\left[2\pi\int_R^S r k_2(r,v)\,dr
               +2\pi Rk_1(R,v)+2\pi Sk_1(S,v)\right]dv.        \tag{9}
\]

The mark can first be truncated and then increased to \(U\).
The Gaussian conditional moments below show local finiteness.
Both boundary components are included. There are no corners.

## 3. Nondegeneracy and the large-radius estimate

Use the free jet coordinates

\[
 Z=(h,h_r,h_\tau,X,Z_2),\quad
 X=(h_{rr}-h_{\tau\tau})/2,\quad Z_2=h_{r\tau}.
\]

Here Hessian subscripts denote Cartesian directional derivatives,
so \(h_{\tau\tau}\) differs from \(h_{ss}\). The Helmholtz
equation gives \(h_{rr}+h_{\tau\tau}=-h\); hence these five
coordinates determine the whole two-jet.

The stationary RPW has covariance

\[
 D=\operatorname{diag}(1,1/2,1/2,1/8,1/8)                    \tag{10}
\]

in these coordinates. This follows by integrating the spectral
monomials \(1,\cos\vartheta,\sin\vartheta,
\cos(2\vartheta)/2,\sin(2\vartheta)/2\). Signs from differentiation
do not change the diagonal entries, and orthogonality makes the
off-diagonal entries zero.

The field \(h\) removes exactly the independent zeroth and two first
Fourier coefficients from a stationary RPW. Their jet coefficient
vectors have every component \(O(r^{-1/2})\), uniformly in angle,
for \(r\geq1\). The same is true of the coefficient vectors of
\(A,B\), the retained second mode. To check derivatives, differentiate
\(J_n(r)\cos n\theta\) and \(J_n(r)\sin n\theta\) through order
two for \(n=0,1,2\): each term is a fixed-order Bessel derivative
times a bounded power of \(1/r\). The recurrence relations and
fixed-order asymptotics in DLMF 10.6 and 10.17 give the claimed bound.
It follows that

\[
 \operatorname{Cov}(Z)=D+O(r^{-1}),\quad
 \operatorname{Cov}((A,B),Z)=O(r^{-1/2}),\quad
 \operatorname{Cov}((A,B))=I_2.                              \tag{11}
\]

All matrix norms here are equivalent finite-dimensional norms.
Thus the full covariance of \((A,B,Z)\) tends to the positive
definite matrix \(I_2\oplus D\). Choose \(R_0\) so that this
covariance is uniformly positive definite for \(r\geq R_0\), and
also \(1/2\leq w\leq3/2\) there. The same asymptotics give

\[
 w=1+O(r^{-1/2}),\quad
 |\nabla w|+\|D^2w\|=O(r^{-1/2}).                           \tag{12}
\]

In particular all Gaussian densities in (7)–(8) are nondegenerate.
Conditional means and covariances are obtained by the regression
formulas

\[
 m=\Sigma_{21}\Sigma_{11}^{-1}z,\qquad
 C=\Sigma_{22}-\Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}.         \tag{13}
\]

For the interior, condition on \((h,h_r,h_\tau)\); the remaining
coordinates are \((A,B,X,Z_2)\). For the boundary, condition on
\((h,h_\tau)\); the remaining coordinates are \((A,B,h_r,X,Z_2)\).
The Schur complements in (13) stay in a compact subset of the positive
definite matrices. Uniformly for \(|v|\leq1\), their means,
covariances and density factors differ from their stationary limiting
ones by \(O(r^{-1/2})\).

For clarity, conditional-moment continuity has a quantitative bound.
On such a compact set the Cholesky factor is Lipschitz: its recursive
formulas use sums, division by positive diagonal entries bounded away
from zero, and square roots of positive pivots bounded away from zero.
Couple two conditional vectors as \(m+LN\) and \(m'+L'N\), with
the same fixed-dimensional standard normal \(N\). Their difference
is bounded by \(C\varepsilon(1+|N|)\) if parameters differ by
\(\varepsilon\). For matrices of size two,

\[
 ||\det H|-|\det H'||\leq C\|H-H'\|(\|H\|+\|H'\|).
\]

The corresponding absolute-value inequality is immediate in dimension
one. Multiplying by \(U=(A^2+B^2)/2\) and also bounding the change
in \(U\), each difference is at most
\(C\varepsilon(1+|N|)^4\). Gaussian moments are finite, so the
expectations differ by \(O(\varepsilon)\). The deterministic
curvature term in (8) is \(O(1/r)\) times a Gaussian coordinate and
satisfies the same bound. These arguments prove that the densities
in (7)–(8) converge at the rate in (3).

It remains to identify the limits. There \((A,B)\) is independent
of the local jet, with \(\mathbb E U=1\). Conditional on value
\(v\), the stationary Hessian is

\[
 \begin{pmatrix}-v/2+X&Z_2\\Z_2&-v/2-X\end{pmatrix},
 \qquad X,Z_2\text{ independent }N(0,1/8).
\]

Writing \(4(X^2+Z_2^2)\) as an exponential variable gives

\[
 \mathbb E|v^2/4-X^2-Z_2^2|
          =(v^2-1+2e^{-v^2})/4.
\]

The value-gradient density is \(\phi(v)/\pi\). Their product is
\(\alpha(v)\). On a straight boundary the conditional second
derivative is \(N(-v/2,1/8)\), whose absolute mean is
\(e^{-v^2}/(2\sqrt\pi)+v\operatorname{erf}(v)/2\).
Multiplication by \(\phi(v)/\sqrt\pi\) gives \(\beta(v)\).
This proves (3), including its constants.

Here is the sharper estimate (3a). Write \(\varepsilon=r^{-1/2}\).
The covariance of the local free jet differs from (10) by
\(O(\varepsilon^2)\); its cross-covariance with \((A,B)\) is
\(O(\varepsilon)\). Under the interior conditioning in (7), the
conditional mean of \((X,Z_2)\) is \(O(\varepsilon^2)\), its
covariance is \(I_2/8+O(\varepsilon^2)\), the mean of \((A,B)\)
is \(O(\varepsilon)\), its covariance is
\(I_2+O(\varepsilon^2)\), and the remaining cross-covariance is
\(O(\varepsilon)\). These statements follow directly from (13):
the stationary covariances of \((X,Z_2)\) with the value and gradient
are zero, while the conditioning targets \((vw,v\nabla w)\) are
uniformly bounded. The identical orders hold under the boundary
conditioning for the relevant local coordinates.

An additional regression shows why the tilt has no linear effect.
Let \(T\) denote the unconditioned local coordinates remaining after
either set of constraints. Their covariance is uniformly invertible.
Conditional on \(T\) as well, the mean of \((A,B)\) has size at
most \(C\varepsilon(1+|T|)\), and its covariance is
\(I_2+O(\varepsilon^2)\). Consequently

\[
 \big|\mathbb E[U\mid T,\text{constraints}]-1\big|
      \leq C\varepsilon^2(1+|T|^2).                         \tag{20}
\]

The determinants and absolute derivatives in (7)–(8) have at most
quadratic growth in these coordinates, with bounded deterministic
coefficients. Gaussian moments therefore show that replacing \(U\)
by one changes either conditional moment by \(O(\varepsilon^2)\).

For the interior determinant there is also an exact trace cancellation:

\[
 \operatorname{tr}(D^2h-vD^2w)
       =-vw-v\Delta w=-v,\qquad \Delta w=J_0=1-w.           \tag{21}
\]

Its traceless part is an isotropic \(N(0,I_2/8)\) vector, up to a
covariance error \(O(\varepsilon^2)\) and a mean shift
\(O(\varepsilon)\). Changing the covariance first costs
\(O(\varepsilon^2)\), by the coupling estimate already proved.
For the mean, the function

\[
 D_v(m)=\mathbb E\big|v^2/4-|N+m|^2\big|,
 \qquad N\sim N(0,I_2/8),
\]

is even in \(m\). It has uniformly bounded second derivatives for
\(|v|\leq1\) and \(|m|\leq1\): write it as the integral of
\(|v^2/4-|z|^2|\) against the Gaussian density at \(z-m\), and
differentiate that density twice. The derivatives are bounded by an
integrable polynomial times a Gaussian, uniformly on these compact
parameter ranges. Taylor's formula, evenness and bounded second
derivatives give \(D_v(m)=D_v(0)+O(|m|^2)\). Increasing \(R_0\)
if necessary makes this applicable to the small shifts above.
Together with (20)–(21), the conditional moment in (7) is

\[
 (v^2-1+2e^{-v^2})/4+O(r^{-1}).
\]

The density in (7) is
\(\phi(vw)/\pi+O(r^{-1})\). Indeed the covariance error is
\(O(r^{-1})\), and the stationary gradient density at
\(v\nabla w\) differs from its density at zero by \(O(r^{-1})\).
Thus, uniformly for \(|v|\leq1\),

\[
 k_2(r,v)=w\frac{\phi(vw)}{\phi(v)}\alpha(v)+O(r^{-1}).       \tag{22}
\]

Put \(j=J_0(r)=O(r^{-1/2})\). Taylor expansion on the compact
level range gives
\((1-j)\phi(v(1-j))/\phi(v)=1+(v^2-1)j+O(j^2)\).
This proves the first formula in (3a).

For the boundary, under \(h=vw,h_\tau=0\), the mean of \(h_r\)
and of \(X\) is \(O(r^{-1})\), since both have stationary
covariance zero with the conditioned coordinates. Hence
\(h_{ss}=-h/2-X-h_r/r\) has mean \(-vw/2+O(r^{-1})\) and
variance \(1/8+O(r^{-1})\). The absolute-normal expectation is
locally Lipschitz in mean and variance when variance is bounded away
from zero, by coupling. Using (20), the conditional moment in (8)
is therefore \(B(vw)+O(r^{-1})\), where
\(B(z)=e^{-z^2}/(2\sqrt\pi)+z\operatorname{erf}(z)/2\).
The joint density in (8) is
\(\phi(vw)/\sqrt\pi+O(r^{-1})\), so

\[
 k_1(r,v)=w\beta(vw)+O(r^{-1}).                             \tag{23}
\]

Taylor expansion of the smooth function \(\beta\) proves the
second formula in (3a). This also explains why a first-order bound
on the cross-covariance alone would overestimate the local error.

The positive-definite free-jet covariance also supplies the needed
genericity on compact annuli in this range. One direct justification
is finite-parameter transversality. At each point the coefficient
vectors span the full free jet, hence in particular the value and
first derivatives. Choose finitely many Fourier coefficients spanning
these evaluations on a neighborhood of each point, then use a finite
cover of the compact annulus. Condition on all other coefficients.
The selected finite Gaussian vector has a smooth density. Parametric
transversality implies that the interior gradient and boundary
tangential derivatives have transverse zeros almost surely; the full
gradient has no zero on either boundary; and a fixed value is regular
on each stratum. This argument applies after dividing by the positive
smooth function \(w\). Nondegenerate zeros are isolated, and no
accumulation can occur in the compact annulus or on its boundary.
Thus the critical counts are finite almost surely. Absolute continuity
(6) preserves all these probability-one facts. These properties justify
the ordinary marked Kac–Rice formulas and the deformation below.

## 4. Topology and comparison of own-height arms

For any smooth function on a neighborhood of the closed annulus, if
an interval \([a,b]\) contains no stratified critical value, there is
a homeomorphism preserving the two boundary circles that carries its
superlevel set at \(a\) to that at \(b\), and also carries the strict
sublevel sets. Here is the construction needed for the arm event.

On the compact level strip use \(\nabla Y/|\nabla Y|^2\) in the
interior, and \(\tau/(\tau\cdot\nabla Y)\) near each boundary.
A partition of unity patches these into a smooth field \(V\) with
\(dY(V)=1\), tangent to each boundary on that boundary. Compactness
gives a slightly enlarged interval with the same nonvanishing
properties. Multiply \(V\) by a smooth function \(\chi(Y)\), equal
to one on \([a,b]\) and supported in the enlarged interval, and
extend by zero. Its flow preserves both boundaries and satisfies
\(dY/ds=\chi(Y)\). The scalar flow in the value is strictly increasing,
and its time-\((b-a)\) map carries value \(a\) to value \(b\).
It therefore carries both strict sign sets at one level to the
corresponding sets at the other. The flow preserves orientation and
cyclic order. It carries any four paths witnessing one arm event to
four paths witnessing the other. Consequently

\[
 \mathbf1_{\mathcal A(Y,a)\,\triangle\,\mathcal A(Y,b)}
 \leq \#\{\text{stratified critical points of }Y
                           \text{ with values in }[a,b]\}.    \tag{14}
\]

Fixed-level endpoints have probability zero of being critical, so
endpoint conventions do not affect the expectation. Applying (9) to
(14) bounds the change of the arm event under the zero-height Palm law.

Finally put \(H_t=F_t-tJ_0\). At every point of the annulus,

\[
 F_t-t=H_t-tw=w(H_t/w-t).                                    \tag{15}
\]

Since \(w>0\), the own-height arm event is precisely
\(\mathcal A(H_t/w,t)\). Apply the residual total variation bound
from Section 1 to this specified event at this specified \(t\):

\[
 |p_*(t;R,S)-\mathbb P_0^*\{\mathcal A(Y,t;R,S)\}|
       \leq\delta(t^2).                                    \tag{16}
\]

At zero, the corresponding probability is exactly \(p_*(0;R,S)\).
The triangle inequality, (14), and (9) prove (2). This argument does
not suppose that the alternating-arm event is monotone in the level.

To integrate the sharper expansion, use
\((rJ_1(r))'=rJ_0(r)\). The integrated first-order interior term is
exactly

\[
 2\pi(v^2-1)\alpha(v)[SJ_1(S)-RJ_1(R)].                     \tag{24}
\]

It is bounded by \(C(\sqrt R+\sqrt S)\), uniformly for
\(|v|\leq1\). The \(O(r^{-1})\) interior remainder integrates
to at most \(C(S-R)\). On each circle the leading \(J_0\) error
in (3a), multiplied by its length, is bounded by \(C\sqrt r\);
the remaining \(O(r^{-1})\) error contributes a bounded constant.
These estimates give (4). For fixed \(\lambda\), all terms in (4) tend to
zero when \(|t_R|R^2\to0\), because \(\alpha,\beta\) are bounded
on \([-1,1]\) and \(\delta(t_R^2)\leq t_R^2/e\).

## 5. Independent zero-level formulas for checking the densities

The exact densities at \(v=0\) admit a useful audit without sampling.
For (7) condition on \(h=h_r=h_\tau=0\), and let \(C\) be the
conditional covariance of \((A,B,X,Z_2)\). Then

\[
 E_2=\tfrac12(C_{AA}+C_{BB})(C_{XX}+C_{Z_2Z_2})
       +C_{AX}^2+C_{BX}^2+C_{AZ_2}^2+C_{BZ_2}^2             \tag{17}
\]

is exactly \(\mathbb E[U|\det D^2h|\mid h=\nabla h=0]\),
since the trace is zero and \(|\det D^2h|=X^2+Z_2^2\).
Formula (17) follows by expanding and using
\(\mathbb E[A^2X^2]=C_{AA}C_{XX}+2C_{AX}^2\).
Thus \(k_2(r,0)=w p_{(h,\nabla h)}(0)E_2\).

For (8), condition on \(h=h_\tau=0\), put \(V=-X-h_r/r\),
and use conditional covariances in the following expression:

\[
 E_1=\tfrac12\sqrt{2\operatorname{Var}(V)/\pi}
 \left[\operatorname{Var}(A)+\operatorname{Var}(B)
   +\frac{\operatorname{Cov}(A,V)^2+
          \operatorname{Cov}(B,V)^2}{\operatorname{Var}(V)}\right].
                                                               \tag{18}
\]

This equals \(\mathbb E[U|V|]\). Indeed regress \(A,B\) on \(V\)
and use \(\mathbb E|V|^3=2\operatorname{Var}(V)\mathbb E|V|\).
Hence \(k_1(r,0)=w p_{(h,h_\tau)}(0)E_1\). These formulas retain
the correlations of the tilt with the distant jet.

In the independent stationary limit, (17) gives \(E_2=1/4\) and
(18) gives \(E_1=1/(2\sqrt\pi)\). Therefore

\[
 \alpha(0)=1/(4\pi\sqrt{2\pi}),\qquad
 \beta(0)=1/(2\pi\sqrt{2\pi}).                              \tag{19}
\]

## Scope and sources

The new conclusion is the quantitative own-height comparison (2),
with explicit finite-dimensional densities and the uniform estimate
(3). It supplies a finite-scale radial-level stability estimate and
retains the area cost of counting all critical points. Formula (3a)
and the oscillatory integral (24) sharpen the error to \(O(|t|R)\)
on fixed-aspect annuli. It does not improve the sufficient
\(o(R^{-2})\) level window. There is no RSW,
arm exponent, or conformal-limit conclusion. The annulus stays away
from the distinguished saddle; estimates uniform down to radius zero
are not claimed. No literature priority is asserted.

The standard Fourier representation is discussed in Dmitry Beliaev,
*Gaussian fields and percolation*, [arXiv:2207.13448](https://arxiv.org/abs/2207.13448),
Section 2.1. Stephen Muirhead, Alejandro Rivera and Hugo Vanneuville,
with an appendix by Laurin Köhler-Schindler, *The phase transition for
planar Gaussian percolation models without FKG*,
[arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3), is used to
check the literature baseline and the preceding reports. The new
annular deformation argument is written out above. Bessel derivative
and asymptotic inputs are [DLMF 10.6](https://dlmf.nist.gov/10.6) and
[DLMF 10.17](https://dlmf.nist.gov/10.17). All these sources were opened.
