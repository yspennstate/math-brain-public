# The second logarithmic correction for Gaussian covariance

Let

\[
 V_s(x)=\frac{e^{-|x|^2/(4s)}}{4\pi s},\quad s>0,\qquad g=b^2>0,
\]

and consider the flat-initial-data Itô equation on \(\mathbb R^2\)

\[
 dZ=\tfrac12\Delta Z\,dt+bZ\,W_s(dt,x),\quad Z(0,x)=1,
 \qquad \mathbb E[W_s(dt,x)W_s(dt,y)]=V_s(x-y)dt.
 \tag{1}
\]

All logarithms are natural. Write \(\gamma_{\rm E}\) for Euler's constant, and define

\[
 D=\sum_{n=1}^{\infty}\frac{4^{-n}}{n^2}=\operatorname{Li}_2(1/4),
 \qquad I_n=\int_0^{1/3}\frac{x^{n-1}}{1+x}\,dx,
 \qquad J=\sum_{n=1}^{\infty}\frac{I_n^2}{n}.
 \tag{2}
\]

**Theorem.** The rate \(\gamma(b,s)=\lim_{t\to\infty}t^{-1}\log\mathbb E[Z(t,0)^2]\) exists. As \(g\downarrow0\),

\[
 \boxed{\log\gamma(b,s)
 =-\frac{4\pi}{g}-\log(2s)-\gamma_{\rm E}
  +\frac{D}{4\pi}g+\frac{J}{16\pi^2}g^2+O(g^3).}
 \tag{3}
\]

The remainder is bounded in absolute value by \(Cg^3\) for \(0<g<g_0\), with \(C,g_0\) independent of \(s>0\). Equivalently,

\[
 \gamma(b,s)=\frac{e^{-\gamma_{\rm E}}}{2s}e^{-4\pi/b^2}
 \left[1+\frac{D}{4\pi}b^2
 +\frac{J+D^2/2}{16\pi^2}b^4+O(b^6)\right].
 \tag{4}
\]

In particular, the new logarithmic coefficient is strictly positive. Exact rational enclosures are

\[
 0.08383727095123180283<J<0.08383727095123180284,
 \tag{5}
\]
\[
 0.00053090572038263670<\frac{J}{16\pi^2}
                         <0.00053090572038263671.
 \tag{6}
\]

This is an annealed second-moment expansion. It makes no assertion about the variance or limiting law of \(\log Z\).

## 1. Spectral characterization

Itô multiplication gives

\[
 \partial_t\mathbb E[Z(t,x)Z(t,y)]
 =\tfrac12(\Delta_x+\Delta_y)\mathbb E[Z(t,x)Z(t,y)]
   +gV_s(x-y)\mathbb E[Z(t,x)Z(t,y)].
\]

Boundedness of \(V_s\) justifies the Duhamel series on each finite time interval. Its terms agree with the Feynman–Kac expansion, so the difference Brownian motion \(B\), whose generator is \(\Delta\), gives

\[
 M_s(t)=\mathbb E[Z(t,0)^2]
 =\mathbb E_0\exp\!\left(g\int_0^tV_s(B_u)du\right)
 =(T_t1)(0),\qquad T_t=e^{t\mathcal H},\quad \mathcal H=\Delta+gV_s.
 \tag{7}
\]

The operator \(\mathcal H\) is self-adjoint on \(H^2(\mathbb R^2)\), since the potential is bounded and real. Its positive kernel obeys

\[
 k_t(x,y)\le e^{g\|V_s\|_\infty t}p_t(x-y),\qquad
 p_t(z)=(4\pi t)^{-1}e^{-|z|^2/(4t)}.
 \tag{8}
\]

One obtains (8) by bounding each potential factor in the Duhamel series and convolving the heat kernels.

Put \(v=\sqrt{V_s}\), so \(\|v\|_2=1\), and let

\[
 K_E=v(E-\Delta)^{-1}v,\quad
 P=|v\rangle\langle v|,\quad Q=I-P,\quad
 \ell(E)=-\frac{\log E}{4\pi}.
\]

Here \(v\) also denotes multiplication. The free resolvent kernel is

\[
 G_E(r)=\frac{1}{4\pi}\int_0^\infty
                 e^{-u-Er^2/(4u)}\frac{du}{u}.
\]

For \(\mathcal J(a)=\int_0^\infty e^{-u-a/u}du/u\), substitution \(u=a/w\) below \(\sqrt a\) gives
\(\mathcal J(a)=2\int_{\sqrt a}^\infty e^{-u-a/u}du/u\).
Since \(1-e^{-a/u}\le a/u\), its difference from \(2E_1(\sqrt a)\) has absolute value at most \(2\sqrt a\). The identity

\[
 E_1(z)=-\gamma_{\rm E}-\log z+
                 \int_0^z\frac{1-e^{-u}}u\,du
\]

follows by differentiation and matching the constant at zero using
\(\int_0^\infty e^{-u}\log u\,du=-\gamma_{\rm E}\).
The last integral lies between zero and \(z\). Therefore
\(|\mathcal J(a)+\log a+2\gamma_{\rm E}|\le4\sqrt a\) for all \(a>0\). Consequently

\[
 K_E=\ell(E)P+A+B_E,
 \quad A(x,y)=\frac{v(x)v(y)}{2\pi}
            [\log2-\gamma_{\rm E}-\log|x-y|],
 \tag{9}
\]
\[
 |B_E(x,y)|\le\frac{\sqrt E}{2\pi}v(x)v(y)|x-y|,
 \qquad \|B_E\|\le\|B_E\|_{\rm HS}\le\frac{\sqrt{2sE}}\pi.
 \tag{10}
\]

For (10), independent \(X,Y\) with density \(V_s\) satisfy \(\mathbb E|X-Y|^2=8s\). Also \(A\) is Hilbert–Schmidt: its squared kernel is integrable near the diagonal because \(\int_0^1r\log^2r\,dr<\infty\), and integrable at infinity by Gaussian decay. Thus \(K_E\) is compact.

Let \(\mu(E)=\|K_E\|\), its top eigenvalue. Nonnegativity follows from the positive Fourier multiplier of the free resolvent. The resolvent identity gives norm continuity. For \(E_1<E_2\) and nonzero \(f\),

\[
 \langle f,(K_{E_1}-K_{E_2})f\rangle
 =(E_2-E_1)\langle vf,
 (E_1-\Delta)^{-1}(E_2-\Delta)^{-1}vf\rangle>0.
\]

The inequality follows in Fourier variables, since \(v>0\) and the multiplier is strictly positive. Testing a top eigenvector at \(E_2\) proves strict decrease of \(\mu\). Equations (9)–(10) imply \(\mu(E)\to\infty\) as \(E\downarrow0\), while \(\mu(E)\le\|V_s\|_\infty/E\to0\) as \(E\to\infty\). There is a unique \(E=E(g,s)>0\) such that

\[
 \mu(E)=1/g.
 \tag{11}
\]

This \(E\) is the top of the spectrum of \(\mathcal H\). Indeed, for \(S=(E-\Delta)^{1/2}\),
\(\|vS^{-1}\|^2=\|v(E-\Delta)^{-1}v\|=1/g\), using the equal norms of \(C^*C\) and \(CC^*\). Hence for \(f\in H^1\),

\[
 \langle f,(E-\mathcal H)f\rangle
 =\|Sf\|_2^2-g\|vf\|_2^2\ge0.
\]

The strictly positive kernel permits a nonnegative top eigenvector \(f\) of \(K_E\): replacing a maximizer by its absolute value cannot reduce the Rayleigh quotient. Set \(\psi=(E-\Delta)^{-1}(vf)\). Then \(v\psi=f/g\), so \(\mathcal H\psi=E\psi\). Resolvent smoothing puts \(\psi\) in \(H^2\); Fourier Cauchy–Schwarz and \(\int(1+|k|^2)^{-2}dk<\infty\) make it bounded and continuous. Its positive convolution formula gives \(\psi(0)>0\). Positivity then yields

\[
 M_s(t)\ge e^{Et}\psi(0)/\|\psi\|_\infty.
\]

For the reverse bound, Duhamel gives \(T_t1=1+g\int_0^tT_uV_s\,du\). For \(u\le1\) its integrand at zero is bounded by \(e^{g\|V_s\|_\infty}\|V_s\|_\infty\). For \(u\ge1\), (8) and the spectral upper bound give

\[
 |(T_uV_s)(0)|\le
 e^{g\|V_s\|_\infty}\|p_1\|_2e^{E(u-1)}\|V_s\|_2.
\]

Integration proves \(M_s(t)\le C_{g,s}e^{Et}\) for \(t\ge1\). Therefore

\[
 \gamma(b,s)=E(g,s).
 \tag{12}
\]

This handles the constant initial function without treating it as an \(L^2\) vector.

## 2. Expansion at the exact crossing

Fix \(s\). Write \(D_E=A+B_E\). For small \(E\), \(\|D_E\|\le C_s\), so the variational principle gives \(|\mu(E)-\ell(E)|\le C_s\). As \(g\downarrow0\), (11) forces \(E(g,s)\downarrow0\): for any fixed \(\eta>0\), eventually \(g\mu(\eta)<1\), and the crossing lies below \(\eta\). At that crossing,

\[
 \ell=1/g+O_s(1),\qquad \sqrt E=O_s(e^{-2\pi/g}).
 \tag{13}
\]

For \(\ell>3C_s\), write a top eigenvector as \(\alpha v+w\), \(w\perp v\). Its coefficient \(\alpha\) is nonzero, since an eigenvector in \(QL^2\) would have eigenvalue at most \(C_s\). Put

\[
 a_E=\langle v,D_Ev\rangle,\quad h_E=QD_Ev,\quad C_E=QD_EQ|_{QL^2}.
\]

Projection of the eigenvalue equation onto \(Q\) gives
\(w=\alpha(\mu-C_E)^{-1}h_E\); projection onto \(v\) gives

\[
 1/g=\ell+a_E+\langle h_E,(g^{-1}-C_E)^{-1}h_E\rangle.
 \tag{14}
\]

For small \(g\), \(g\|C_E\|<1/2\), and the norm-convergent series gives

\[
 (g^{-1}-C_E)^{-1}=gI+g^2C_E+O_s(g^3).
\]

The remainder norm is bounded by \(g^3\|C_E\|^2/(1-g\|C_E\|)\). Define

\[
 a_s=\langle v,Av\rangle,\quad h=QAv,\quad
 c=\|h\|^2,\quad d=\langle h,QAQh\rangle=\langle h,Ah\rangle.
\]

Equation (10) shows that \(a_E-a_s\), \(h_E-h\), and \(C_E-QAQ\) are \(O_s(\sqrt E)\) in their respective norms. Thus (14) and (13) imply

\[
 \ell=1/g-a_s-cg-dg^2+O_s(g^3),
\]
\[
 \log E=-4\pi/g+4\pi a_s+4\pi cg+4\pi dg^2+O_s(g^3).
 \tag{15}
\]

An independent scalar derivation checks the coefficient. From the rank-one equation,

\[
 \ell=\frac{1}{g\langle v,(I-gD_E)^{-1}v\rangle}.
\]

Let \(m_j=\langle v,A^jv\rangle\). The block matrix of \(A\) gives
\(m_1=a_s\), \(m_2=a_s^2+c\), and \(m_3=a_s^3+2a_sc+d\): the paths through its two blocks are respectively the constant block, the two paths with one excursion, and the path with one \(QAQ\) factor. Expanding the reciprocal of \(1+m_1g+m_2g^2+m_3g^3+O_s(g^4)\) yields

\[
 \ell=\frac1g-m_1+(m_1^2-m_2)g
       +(-m_1^3+2m_1m_2-m_3)g^2+O_s(g^3)
 =\frac1g-a_s-cg-dg^2+O_s(g^3).
\]

The replacement of \(D_E\) by \(A\) has exponentially small error by (13). In particular there is no surviving \(a_sc\) term at order \(g^2\).

## 3. Gaussian radial formulas and recheck of the first correction

If \(X,Y\) have density \(V_s\), then \(|X-Y|^2/(8s)\) is unit exponential. Therefore

\[
 a_s=\frac{\log2-\gamma_{\rm E}-\mathbb E\log|X-Y|}{2\pi}
     =-\frac{\log(2s)+\gamma_{\rm E}}{4\pi}.
 \tag{16}
\]

For radii \(r\ne q\), the angular average of \(\log|r-qe^{i\theta}|\) is \(\log\max(r,q)\). To verify it, factor out the larger radius and use the convergent power series for \(\log(1-z e^{i\theta})\); every nonconstant Fourier mode has zero average. Equal radii form a set of measure zero in the subsequent radial integrals.

Let \(u=|x|^2/(4s)\). Under \(V_s(x)dx\), \(u\) has density \(e^{-u}du\). Angular averaging gives

\[
 L_s(x):=\int V_s(y)\log|x-y|dy
 =\frac{\log(4s)-\gamma_{\rm E}+\operatorname{Ein}(u)}2,
 \quad \operatorname{Ein}(u)=\int_0^1\frac{1-e^{-tu}}t\,dt.
 \tag{17}
\]

Indeed the derivative of \(\mathbb E\log\max(u,U)\) is \((1-e^{-u})/u\), and its value at zero is \(\mathbb E\log U=-\gamma_{\rm E}\). This proves (17). Tonelli gives \(\mathbb E\operatorname{Ein}(U)=\int_0^1(1+t)^{-1}dt=\log2\). Define

\[
 H(u)=\log2-\operatorname{Ein}(u),\quad
 \int_0^\infty e^{-u}H(u)du=0.
\]

Since \((Av)/v=[\log2-\gamma_{\rm E}-L_s]/(2\pi)\), (16)–(17) imply

\[
 h(x)=\frac{v(x)}{4\pi}H(u).
 \tag{18}
\]

For completeness, the covariance of \(1-e^{-tU}\) and \(1-e^{-qU}\) is
\(tq/[(1+t+q)(1+t)(1+q)]\). Fubini is justified by \((1-e^{-tU})/t\le U\) and \(\mathbb EU^2<\infty\). Thus

\[
 \mathbb EH(U)^2=
 \int_0^1\int_0^1\frac{dt\,dq}{(1+t+q)(1+t)(1+q)}
 =\int_0^{1/2}\int_0^{1/2}\frac{dx\,dy}{1-xy}=D.
\]

The substitution is \(x=t/(1+t)\), \(y=q/(1+q)\); expanding the last integrand gives the positive series for \(D\). Hence

\[
 c=D/(16\pi^2).
 \tag{19}
\]

## 4. Evaluation of the next block term

Because \(h\) is radial, angular averaging in \(\langle h,Ah\rangle\) is legitimate. The averaged finite-part kernel, after removing its two factors of \(v\), is

\[
 \frac{-2\gamma_{\rm E}-\log s-\log\max(u,w)}{4\pi}.
\]

Equations (18) and the zero mean of \(H\) cancel both constant terms, giving

\[
 d=-\frac{1}{64\pi^3}\int_0^\infty\int_0^\infty
       e^{-u-w}H(u)H(w)\log\max(u,w)\,du\,dw.
 \tag{20}
\]

All integrals are absolute: \(|H(u)|\le\log2+u\), the logarithmic singularity is integrable at zero, and the weights are exponential at infinity.

Put \(F(t)=\int_0^t e^{-u}H(u)du\). Symmetry of the double integral in (20) shows that its numerator, including the minus sign, equals

\[
 -2\int_0^\infty F(t)F'(t)\log t\,dt
 =\int_0^\infty\frac{F(t)^2}{t}\,dt.
 \tag{21}
\]

For the integration by parts, \(F(t)=O(t)\) at zero. Its zero total integral and \(|H(u)|\le\log2+u\) give \(F(t)=O((1+t)e^{-t})\) at infinity. Thus \(F(t)^2\log t\) vanishes at both endpoints and the integral in (21) is finite.

The defining integral of Ein gives another formula for \(H\):

\[
 H(u)=\int_0^1\left(e^{-pu}-\frac1{1+p}\right)\frac{dp}{p}.
\]

The singularity at \(p=0\) is removable. Integration against \(e^{-u}\) from zero to \(t\) gives

\[
 F(t)=\int_0^1\frac{e^{-t}-e^{-(1+p)t}}{p(1+p)}\,dp>0
 \qquad(t>0).
 \tag{22}
\]

All exchanges on bounded \(t\) intervals follow from the removable singularity and a bounded integrand. In particular the coefficient in (20) is strictly positive.

Squaring (22), integrating with \(dt/t\), and applying Tonelli to nonnegative integrands gives

\[
 \int_0^\infty\frac{F(t)^2}t\,dt
 =\int_0^1\int_0^1\frac{1}{p(1+p)q(1+q)}
 \log\frac{(2+p)(2+q)}{2(2+p+q)}\,dp\,dq.
 \tag{23}
\]

To evaluate the inner time integral, expand its numerator as
\(e^{-2t}-e^{-(2+p)t}-e^{-(2+q)t}+e^{-(2+p+q)t}\).
The identity
\(\int_0^\infty(e^{-at}-e^{-bt})dt/t=\log(b/a)\)
follows by integrating \(\int_a^b e^{-rt}dr\) first in \(t\). Apply it to the two differences to obtain the logarithm in (23).

Now substitute \(x=p/(2+p)\), \(y=q/(2+q)\). Then
\(dp/[p(1+p)]=dx/[x(1+x)]\), and

\[
 \frac{(2+p)(2+q)}{2(2+p+q)}=\frac1{1-xy}.
\]

The square maps to \([0,1/3]^2\). Expanding \(-\log(1-xy)=\sum_{n\ge1}(xy)^n/n\), and using Tonelli once more, proves

\[
 \int_0^\infty\frac{F(t)^2}t\,dt
 =\int_0^{1/3}\int_0^{1/3}
       \frac{-\log(1-xy)}{xy(1+x)(1+y)}dxdy
 =\sum_{n=1}^\infty\frac{I_n^2}{n}=J.
 \tag{24}
\]

At \(xy=0\) the displayed integrand is defined by continuity. Combining (20)–(24) gives the explicit scale-independent value

\[
 \boxed{d=\langle h,QAQh\rangle=\frac{J}{64\pi^3}.}
 \tag{25}
\]

Equations (12), (15), (16), (19), and (25) prove (3) for fixed \(s\). Exponentiating gives (4), since the order-\(g^2\) term receives \(\tfrac12[D/(4\pi)]^2\) in addition to \(J/(16\pi^2)\).

## 5. Uniformity, normalization and certified decimals

Brownian scaling in (7), with \(V_s(\sqrt s\,x)=s^{-1}V_1(x)\), gives exactly

\[
 M_s(t)=M_1(t/s),\qquad \gamma(b,s)=s^{-1}\gamma(b,1).
 \tag{26}
\]

Apply (3)–(4) at \(s=1\) and then use (26). This proves the stated uniformity without requiring the intermediate operator bounds to be uniform in \(s\). For diffusion coefficient \(d_0>0\) in the SHE, time change gives

\[
 \gamma_{d_0}(b,s)=2d_0\gamma(b/\sqrt{2d_0},s).
\]

In (3), this replaces the leading constant by \(-8\pi d_0/b^2+\log(d_0/s)-\gamma_{\rm E}\), the order-\(b^2\) coefficient by \(D/(8\pi d_0)\), and the order-\(b^4\) coefficient by \(J/(64\pi^2d_0^2)\). At \(d_0=1/2\) these return (3).

Here are explicit finite-arithmetic certificates for (5)–(6). Since \(0<I_n\le3^{-n}/n\),

\[
 0<\sum_{n>N}\frac{I_n^2}{n}
 \le\frac{9^{-(N+1)}}{(N+1)^3(1-1/9)}.
 \tag{27}
\]

For any even \(K\), the alternating series for \(1/(1+x)\), integrated on \([0,1/3]\), gives

\[
 S_{n,K}:=\sum_{k=0}^{K-1}\frac{(-1)^k3^{-(n+k)}}{n+k}
 <I_n<S_{n,K}+\frac{3^{-(n+K)}}{n+K}.
 \tag{28}
\]

The lower bound is positive: adjacent terms pair to positive numbers. Square these two rational bounds, divide by \(n\), and sum for \(1\le n\le20\), with \(K=60\). Add (27) to the upper endpoint. This gives rational endpoints \(J_-,J_+\); exact integer comparison gives

\[
 \frac{8383727095123180283}{10^{20}}<J_-<J<J_+
 <\frac{8383727095123180284}{10^{20}}.
\]

For (6), enclose \(\pi\) using \(\pi=16\arctan(1/5)-4\arctan(1/239)\), with respectively 40 and 12 terms of the alternating arctangent series. The identity follows because \(\tan(4\arctan(1/5))=120/119\), and subtracting \(\arctan(1/239)\) gives tangent 1, at an angle in \((0,\pi/2)\). Alternating-series bounds then give rational \(\pi_-<\pi<\pi_+\). The rational interval
\([J_-/(16\pi_+^2),J_+/(16\pi_-^2)]\) lies strictly inside the endpoints in (6). The same calculation gives

\[
 0.00004224813485733012<d<0.00004224813485733013.
\]

The accompanying script performs these operations with exact fractions and rounds displayed endpoints outward by integer division. Its quadrature comparisons and zero-energy ODE output are separate floating-point diagnostics; they are not used in the proof.
