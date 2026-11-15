# A one-minimum theorem for the isotropic Marchenko--Pastur risk profile

This result concerns an explicit spectral risk profile proposed in earlier T267 work as a surrogate for infinite-width ReLU random features. It does not establish that the nonlinear network has this limiting risk. In particular, no kernel approximation or uniform-in-time network limit is assumed as a proved result here.

## Statement

Fix an aspect ratio \(\gamma>0\), signal energy \(E\geq0\), noise variance \(s^2\geq0\), and ridge parameter \(c\geq0\). Set

\[
 \ell_- = \frac{(1-\sqrt\gamma)^2}{4\gamma},\qquad
 \ell_+ = \frac{(1+\sqrt\gamma)^2}{4\gamma},\qquad
 \alpha_0=(1-\gamma^{-1})_+.
\]

Define the scaled Marchenko--Pastur probability measure

\[
 \nu_\gamma(d\ell)=\alpha_0\delta_0(d\ell)
 +\frac{2}{\pi}\frac{\sqrt{(\ell_+-\ell)(\ell-\ell_-)}}{\ell}
 \mathbf1_{(\ell_-,\ell_+)}(\ell)\,d\ell.
 \tag{1}
\]

For \(t\geq0\), let

\[
 \mathcal R(t)=s^2+
 \int\left[
 E\left(\frac{c+\ell e^{-t(\ell+c)}}{\ell+c}\right)^2
 +\frac{s^2}{4}\frac{\ell}{(\ell+c)^2}
       (1-e^{-t(\ell+c)})^2
 \right]\nu_\gamma(d\ell).
 \tag{2}
\]

At \(\ell=0\), the signal integrand is defined to be \(E\), and the variance integrand to be zero, also when \(c=0\). This convention records an unlearned null direction.

**Theorem.**

1. If \(E>0\) and \(s^2/4\leq Ec\), then \(\mathcal R\) is strictly decreasing at every finite time.
2. If \(E>0\) and \(s^2/4>Ec\), then there is exactly one critical time \(t_*>0\). It is a strict, nondegenerate minimum: \(\mathcal R'<0\) before it, \(\mathcal R'>0\) after it, and \(\mathcal R''(t_*)>0\).
3. If \(E=0<s^2\), then \(\mathcal R'(t)>0\) for \(t>0\). If \(E=s^2=0\), the profile is constant.

Consequently this profile never has two strict local minima separated by a local maximum, for any positive aspect ratio. There is no assumption that its spectral interval and its doubled interval are disjoint.

## 1. Exact finite-sample origin of the profile

The following calculation identifies precisely the surrogate to which (2) applies. It is not an identity for a nonlinear network.

Let \(X\) be any fixed real \(n\times d\) design matrix. Put \(T=X^TX/(4d)\) and \(y=X\beta+\varepsilon\), where \(\beta\) and \(\varepsilon\) are independent, centered, with covariances \((E/d)I_d\) and \(s^2I_n\). Take an independent centered test input \(x\) with covariance \(I_d\) and an independent centered test noise of variance \(s^2\). If the design is random, take it independent of the teacher and training noise. Train

\[
 \dot\theta=-(T+cI)\theta+\frac{X^Ty}{4d},\qquad\theta(0)=0.
 \tag{3}
\]

This is gradient flow for \(\|X\theta-y\|^2/(8d)+c\|\theta\|^2/2\). Write
\(g_t(\ell)=(1-e^{-t(\ell+c)})/(\ell+c)\), with \(g_t(0)=t\) if \(c=0\). Solving each scalar equation in an orthonormal eigenbasis of \(T\) gives

\[
 \theta(t)=g_t(T)\left(T\beta+\frac{X^T\varepsilon}{4d}\right).
\]

In a direction with eigenvalue \(\ell\), the signal multiplier in \(\theta-\beta\) is

\[
 \ell g_t(\ell)-1
 =-\frac{c+\ell e^{-t(\ell+c)}}{\ell+c}.
\]

The covariance of \(X^T\varepsilon/(4d)\) is

\[
 \frac{s^2X^TX}{16d^2}=\frac{s^2}{4d}T.
\]

The signal-noise cross term vanishes by independence and centering. The test risk conditional on \(\theta,\beta\) is \(s^2+\|\theta-\beta\|^2\). Averaging over the training teacher and noise, conditional on \(X\), therefore gives exactly

\[
 s^2+\frac1d\sum_{j=1}^d
 \left[E\left(\frac{c+\ell_j e^{-t(\ell_j+c)}}{\ell_j+c}\right)^2
 +\frac{s^2}{4}\frac{\ell_j}{(\ell_j+c)^2}
 (1-e^{-t(\ell_j+c)})^2\right].
 \tag{4}
\]

Thus (2) is the exact spectral limit of (4) whenever the empirical eigenvalue measures converge weakly to (1) and remain in a common compact interval. For each fixed finite \(t\), the displayed integrands, with the stated extension at zero, are bounded and continuous on that interval. No exchange with \(t\to\infty\) is needed. The measure (1) is the usual scaled MP candidate when \(X\) has independent standard Gaussian entries and \(d/n\to\gamma\); a proof of the random matrix limit is not needed for, and is not part of, the theorem about (2).

## 2. Differentiate the risk

Set \(B=s^2/4\), \(A=B-Ec\), and \(k=\ell+c\). For \(\ell>0\), differentiating the two summands of (2) separately yields

\[
 \frac{d}{dt}\left[E\frac{(c+\ell e^{-kt})^2}{k^2}\right]
 =-\frac{2E\ell}{k}(ce^{-kt}+\ell e^{-2kt}),
\]

\[
 \frac{d}{dt}\left[B\frac{\ell}{k^2}(1-e^{-kt})^2\right]
 =\frac{2B\ell}{k}(e^{-kt}-e^{-2kt}).
\]

Their sum is

\[
 \mathcal R'(t)=2\int_{\ell>0}\frac{\ell}{\ell+c}
 \left[Ae^{-t(\ell+c)}-(E(\ell+c)+A)e^{-2t(\ell+c)}\right]
 \nu_\gamma(d\ell).
 \tag{5}
\]

The atom at zero contributes no derivative. At \(c=0\), the apparent singularity in the variance in (2) is removable for every finite \(t\):
\((1-e^{-t\ell})^2/\ell\leq t^2\ell\).
In (5), \(\ell/(\ell+c)\leq1\) and the other factors and all their time derivatives are bounded on any finite time interval. Differentiation under the integral follows by dominated convergence. The same argument gives two continuous time derivatives, including at \(t=0\).

If \(E>0\) and \(A\leq0\), the first coefficient in (5) is nonpositive and
\(E(\ell+c)+A=E\ell+B>0\) for every \(\ell>0\). The density in (1) has positive mass there. Hence \(\mathcal R'(t)<0\). This proves part 1.

If \(E=0\), (5) is
\(2B\int \ell/(\ell+c)(e^{-kt}-e^{-2kt})\,d\nu_\gamma\),
which is strictly positive for \(B>0,t>0\), and identically zero when \(B=0\). This proves part 3.

It remains to treat \(E>0,A>0\).

## 3. The signed rate density has exactly one change of sign

Set \(a=c+\ell_-\) and \(b=c+\ell_+\). Then \(0\leq a<b\). Multiplying the continuous density in (1) by \(\ell/(\ell+c)\), and changing variable from \(\ell\) to \(k=\ell+c\), gives

\[
 w(k)=\frac{2}{\pi}\frac{\sqrt{(b-k)(k-a)}}{k}
       \mathbf1_{(a,b)}(k).
 \tag{6}
\]

Extend \(w\) by zero outside that interval. If \(a=0\), this is integrable at zero, since it is proportional to \(k^{-1/2}\) there. Formula (5) becomes

\[
 F(t):=\tfrac12\mathcal R'(t)
 =\int e^{-kt}h(k)\,dk,
 \qquad
 h(k)=Aw(k)-\tfrac12(Ek/2+A)w(k/2).
 \tag{7}
\]

The factor \(1/2\) in the second term is the Jacobian from the substitution \(k=2u\). The support of the positive density in (7) is \([a,b]\); the negative density is supported on \([2a,2b]\).

If \(b\leq2a\), take any \(r\in[b,2a]\). Then \(h\geq0\) below \(r\), \(h\leq0\) above it, and each strict sign holds on an interval. A possible gap between supports does not affect this assertion.

Suppose instead that \(2a<b\). On the overlap \(2a<k<b\), divide the negative density by \(w(k)>0\). The quotient is

\[
 Q(k)=\frac{\tfrac12(Ek/2+A)w(k/2)}{w(k)}
 =(Ek/2+A)
 \sqrt{\frac{b-k/2}{b-k}\frac{k/2-a}{k-a}}.
 \tag{8}
\]

Both rational factors are positive on this interval. Their derivatives are

\[
 \frac{d}{dk}\frac{b-k/2}{b-k}=\frac{b}{2(b-k)^2}>0,
 \qquad
 \frac{d}{dk}\frac{k/2-a}{k-a}=\frac{a}{2(k-a)^2}\geq0.
 \tag{9}
\]

The factor \(Ek/2+A\) is positive and increasing. Thus \(Q\) is continuous and strictly increasing. At the lower endpoint,

\[
 \lim_{k\downarrow2a}Q(k)=0\quad(a>0),
 \qquad
 \lim_{k\downarrow0}Q(k)=A/\sqrt2\quad(a=0).
\]

Both limits are strictly below \(A\). At the upper endpoint \(Q(k)\to+\infty\): the first factor inside the square root diverges, and the second has a positive limit because \(b>2a\). There is consequently a unique \(r\in(2a,b)\) with \(Q(r)=A\). On the overlap, \(h(k)=w(k)(A-Q(k))\). On any positive-only part of the support, \(h>0\); on the negative-only part, \(h<0\). Therefore in this case also,

\[
 h(k)\geq0\ (k<r),\qquad h(k)\leq0\ (k>r),
 \tag{10}
\]

with strict signs on intervals of positive length on both sides of \(r\).

## 4. A signed Laplace transform with this sign pattern has one zero

Define \(G(t)=e^{rt}F(t)\). Since \(h\) is integrable with compact support, differentiation gives

\[
 G'(t)=\int(r-k)e^{(r-k)t}h(k)\,dk>0.
 \tag{11}
\]

Indeed, \((r-k)h(k)\) is nonnegative everywhere and positive on intervals of positive length. Thus \(G\) is strictly increasing, and \(F\) can have at most one zero.

At zero, (7), or equivalently (5), gives

\[
 F(0)=-E\int_a^b k w(k)\,dk<0.
 \tag{12}
\]

To verify that \(F\) eventually becomes positive, choose \(u<r\) such that
\(H=\int_{k\leq u}h(k)\,dk>0\). Such a choice is possible because \(h\) is strictly positive on an interval below \(r\). Let \(N=\int_{k>r}|h(k)|\,dk<\infty\). Discarding the remaining positive terms, for \(t\geq0\) we obtain

\[
 F(t)\geq H e^{-ut}-N e^{-rt}>0
 \quad\hbox{whenever }e^{(r-u)t}>N/H.
 \tag{13}
\]

Continuity, (12), (13), and strict increase of \(G\) imply exactly one zero \(t_*>0\), with the stated derivative signs. At that zero,
\(F'(t_*)=e^{-rt_*}G'(t_*)>0\), so \(\mathcal R''(t_*)=2F'(t_*)>0\). This proves part 2 and the theorem.

## 5. Independent algebraic checks and boundary cases

**A second derivation of (5).** In an eigenmode of (3), the signal error is
\(b_\ell(t)=-c/k-(\ell/k)e^{-kt}\). Its derivative is \(\ell e^{-kt}\), so
\(2E b_\ell b_\ell'=-2E\ell(c e^{-kt}+\ell e^{-2kt})/k\).
The noise multiplier is \(v_\ell(t)=(1-e^{-kt})/k\), with derivative \(e^{-kt}\) and forcing variance \(B\ell\) after the normalized trace is taken. Its squared-error derivative is
\(2B\ell v_\ell v_\ell'=2B\ell(e^{-kt}-e^{-2kt})/k\).
Adding them recovers (5) directly from the scalar ODE.

**Initial slope checked by a spectral moment.** The interval length is
\(\ell_+-\ell_-=1/\sqrt\gamma\). Substituting
\(\ell=(\ell_-+\ell_+)/2+((\ell_+-\ell_-)/2)\cos\theta\)
and using \(\int_0^\pi\sin^2\theta\,d\theta=\pi/2\) gives

\[
 \int\ell\,\nu_\gamma(d\ell)
 =\frac2\pi\int_{\ell_-}^{\ell_+}
      \sqrt{(\ell_+-\ell)(\ell-\ell_-)}\,d\ell
 =\frac{(\ell_+-\ell_-)^2}{4}=\frac1{4\gamma}.
\]

Hence (5) gives \(\mathcal R'(0)=-E/(2\gamma)\).
Independently, (3) gives \(\dot\theta(0)=T\beta+X^T\varepsilon/(4d)\); differentiating the test squared error and averaging gives
\(-2E\operatorname{tr}(T)/d\). This agrees with the preceding expression when the first spectral moment tends to \(1/(4\gamma)\). For standard Gaussian entries this expectation is already exactly \(-En/(2d)\) at finite size, since \(\mathbb E\|X\|_F^2=nd\).

**Density dilation checked without cancelling factors.** Directly from (6),
\(w(k/2)/w(k)=2\sqrt{(b-k/2)(k/2-a)/((b-k)(k-a))}\).
Multiplication by the substitution Jacobian \(1/2\) gives (8). Omitting this Jacobian would change the \(a=0\) lower endpoint and invalidate the sign argument.

**Critical aspect ratio and zero ridge.** If \(\gamma=1,c=0\), then \(a=0\). The rate density has an integrable inverse-square-root singularity; the lower limit in (8) is \(A/\sqrt2\), not zero. This case is included in the proof. When the long-time variance diverges, the theorem only concerns finite times and remains valid.

**Zero eigenvalues.** For \(\gamma>1\), the atom at zero contributes the constant \(E\alpha_0\) to the risk, with no contribution to (5). It cannot create an extremum. Treating a zero eigenvalue as a mode of rate \(c\) without its zero prefactor would be incorrect.

**Noiseless and zero-signal cases.** If \(s^2=0,E>0\), part 1 applies, including at \(c=0\). If \(E=0<s^2\), the minimum is at the boundary \(t=0\), not at an interior critical time.

**An arbitrary spectrum would invalidate the conclusion.** The MP density is essential. To check this, replace (1) by
\(\nu=(9999\delta_{100}+\delta_1)/10000\), and set \(c=0,E=1,s^2=4\). Formula (5) then gives

\[
 10000F(t)=9999(e^{-100t}-101e^{-200t})
                 +(e^{-t}-2e^{-2t}).
\]

At \(t=0\) this is negative. At \(t_1=(\log2)/10\), the first parentheses equal \(923/1048576\), and the second parentheses are at least \(-1\). Hence
\(10000F(t_1)\geq9999\cdot923/1048576-1>0\), since \(9999\cdot923=9229077>1048576\).
At \(t_2=(\log2)/2\), the first parentheses are less than \(2^{-50}\), and the second equal \(1/\sqrt2-1<-1/4\). Thus
\(10000F(t_2)<9999\cdot2^{-50}-1/4<0\).
At \(t_3=2\log2\), both parentheses are positive: the second equals \(1/8\), and the first is \(2^{-200}(1-101\cdot2^{-200})>0\).
The analytic risk therefore has a minimum, a maximum, and a second minimum on these successive intervals. This is only a check outside the theorem's hypotheses, not a nonlinear-network example. It shows why the sign argument cannot be applied to a general empirical eigenvalue measure.

## Scope for T267

For the value \(c=1/4-1/(2\pi)\) used in the earlier ReLU surrogate, the theorem removes the earlier extreme-aspect-ratio restriction completely. It proves the conjectured one-minimum property of that explicit curve. The proof also works at \(c=0\) and for every other \(c\geq0\).

This does not prove absence of double descent in nonlinear random features or in feature learning. The surrogate-to-network passage still requires a correct deterministic equivalent for the actual test risk, including constant and radial kernel terms and the initialization. Teacher/noise averaging in (4) must also be distinguished from risk for a realized training sample. Even convergence of risks and first derivatives on every compact time interval would not exclude small extrema whose times diverge with dimension. None of these missing implications is used in the theorem.
