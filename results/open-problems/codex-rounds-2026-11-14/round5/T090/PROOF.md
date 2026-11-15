# First correction to the Gaussian second-moment rate

Let

\[
 V_s(x)=\frac{1}{4\pi s}\exp\!\left(-\frac{|x|^2}{4s}\right),
 \qquad s>0,
\]

and consider the flat-initial-data Itô equation

\[
 dZ=\tfrac12\Delta Z\,dt+bZ\,W_s(dt,x),\qquad Z(0,x)=1,
 \qquad \mathbb E[W_s(dt,x)W_s(dt,y)]=V_s(x-y)dt.
 \tag{1}
\]

Write \(g=b^2\), let \(\gamma_{\rm E}\) denote Euler's constant, and define

\[
 D=\operatorname{Li}_2(1/4):=\sum_{n=1}^{\infty}\frac{4^{-n}}{n^2}.
 \tag{2}
\]

**Theorem.** The second-moment rate exists, and as \(b\to0\), \(b\ne0\),

\[
 \boxed{
 \gamma(b,s):=\lim_{t\to\infty}\frac1t\log\mathbb E[Z(t,0)^2]
 =\frac{e^{-\gamma_{\rm E}}}{2s}e^{-4\pi/b^2}
 \left(1+\frac{D}{4\pi}b^2+O(b^4)\right).}
 \tag{3}
\]

There are constants \(C,g_0>0\), independent of \(s>0\), such that the absolute value of the remainder in parentheses is at most \(Cb^4\) when \(0<b^2<g_0\). If \(x_g>0\) is the unique root of

\[
 \frac{g}{4\pi}e^{x_g}E_1(x_g)=1,
 \qquad E_1(x)=\int_x^\infty\frac{e^{-u}}u\,du,
 \tag{4}
\]

then

\[
 \frac{\gamma(b,s)}{x_{b^2}/(2s)}
 =1+\frac{D}{4\pi}b^2+O(b^4).
 \tag{5}
\]

The correction \(D/(4\pi)\) is strictly positive. The statement concerns an annealed second moment.

## 1. Spectral reduction and its normalization

Itô multiplication in (1) gives

\[
 \partial_t\mathbb E[Z(t,x)Z(t,y)]
 =\tfrac12(\Delta_x+\Delta_y)\mathbb E[Z(t,x)Z(t,y)]
 +gV_s(x-y)\mathbb E[Z(t,x)Z(t,y)].
\]

The coefficient \(gV_s\) is bounded. Its Duhamel series converges on bounded time intervals and agrees term by term with the bounded-potential Feynman–Kac series. The difference of the two Brownian motions has generator \(\Delta\). Thus, for \(H=\Delta+gV_s\) on \(L^2(\mathbb R^2)\), with domain \(H^2(\mathbb R^2)\),

\[
 M_s(t):=\mathbb E[Z(t,0)^2]
 =\mathbb E_0\exp\!\left(g\int_0^t V_s(D_u)du\right)
 =(e^{tH}1)(0),
 \tag{6}
\]

where \(D\) has generator \(\Delta\). The semigroup acts on bounded functions by the last expectation even though \(1\notin L^2\). Since the potential is real and bounded, \(H\) is self-adjoint on the stated domain. If \(T_t=e^{tH}\) and \(p_t(x)=(4\pi t)^{-1}e^{-|x|^2/(4t)}\), its kernel satisfies

\[
 0<k_t(x,y)\le e^{g\|V_s\|_\infty t}p_t(x-y).
 \tag{7}
\]

This follows by bounding each potential factor in the Duhamel expansion and convolving the heat kernels.

Put \(v=\sqrt{V_s}\). Then \(\|v\|_2=1\). Define

\[
 K_E=v(E-\Delta)^{-1}v,\qquad
 Pf=\langle v,f\rangle v,\qquad Q=I-P,\qquad
 \ell(E)=-\frac{\log E}{4\pi}.
 \tag{8}
\]

Multiplication by \(v\) is bounded; the same notation denotes that multiplication and the function. The free resolvent kernel is

\[
 G_E(r)=\int_0^\infty e^{-Et}p_t(r)dt
 =\frac1{4\pi}J(Er^2/4),\qquad
 J(a)=\int_0^\infty e^{-u-a/u}\frac{du}{u}.
 \tag{9}
\]

For \(z=\sqrt a\), substituting \(u=a/w\) in the part below \(z\) gives
\(J(a)=2\int_z^\infty e^{-u-a/u}du/u\). Since \(1-e^{-a/u}\le a/u\),

\[
 |J(a)-2E_1(z)|\le2a\int_z^\infty u^{-2}du=2\sqrt a.
\]

Differentiating, and matching the constant at zero using
\(\int_0^\infty e^{-u}\log u\,du=-\gamma_{\rm E}\), gives

\[
 E_1(z)=-\gamma_{\rm E}-\log z+
 \int_0^z\frac{1-e^{-u}}u\,du.
\]

The last integral is between zero and \(z\). Consequently

\[
 |J(a)+\log a+2\gamma_{\rm E}|\le4\sqrt a\qquad(a>0).
\]

Substitution in (9) proves the global decomposition

\[
 K_E=\ell(E)P+A+B_E,
 \tag{10}
\]

where

\[
 A(x,y)=\frac{v(x)v(y)}{2\pi}
    (\log2-\gamma_{\rm E}-\log|x-y|),
 \qquad
 |B_E(x,y)|\le\frac{\sqrt E}{2\pi}v(x)v(y)|x-y|.
 \tag{11}
\]

The logarithmic singularity is square integrable against two Gaussian densities: near zero its radial integral is bounded by a constant times \(\int_0^1r(1+|\log r|^2)dr\), and the tail is Gaussian. Hence \(A\) is Hilbert–Schmidt. Independent random variables \(X,Y\) with density \(V_s\) satisfy \(\mathbb E|X-Y|^2=8s\), so

\[
 \|B_E\|^2\le\|B_E\|_{\rm HS}^2
 \le\frac{2s}{\pi^2}E.
 \tag{12}
\]

Thus \(K_E\) is compact. No compact-support hypothesis is needed.

For completeness, its top eigenvalue \(\mu(E)=\|K_E\|\) is continuous and strictly decreasing on \((0,\infty)\). Positivity as a quadratic form follows from the positive Fourier multiplier \((E+|k|^2)^{-1}\). The resolvent identity proves norm continuity. For \(E_1<E_2\), its quadratic-form difference at nonzero \(f\) is

\[
 (E_2-E_1)\langle vf,
 (E_1-\Delta)^{-1}(E_2-\Delta)^{-1}vf\rangle>0,
\]

because \(v>0\) and the multiplier in the inner product is strictly positive. Testing at a top eigenvector at \(E_2\) proves strict decrease. From (10), \(\mu(E)\to\infty\) as \(E\downarrow0\); also \(\mu(E)\le\|V_s\|_\infty/E\to0\) as \(E\to\infty\). There is therefore a unique \(E=E(g,s)>0\) such that

\[
 \mu(E)=1/g.
 \tag{13}
\]

This crossing is the top of the spectrum of \(H\). Indeed, with \(S=(E-\Delta)^{1/2}\),
\(\|vS^{-1}\|^2=\|v(E-\Delta)^{-1}v\|=\mu(E)\), using the equal norms of \(C^*C\) and \(CC^*\). For \(f\in H^1\),

\[
 \langle f,(E-H)f\rangle
 =\|Sf\|_2^2-g\|vf\|_2^2\ge0.
\]

To see that this upper bound is attained, choose a nonnegative top eigenvector \(f\) of \(K_E\). Such a choice is possible since its strictly positive kernel implies that replacing an eigenvector by its absolute value cannot decrease the Rayleigh quotient. Set \(\psi=(E-\Delta)^{-1}(vf)\). Equation (13) gives \(v\psi=f/g\), and hence \(H\psi=E\psi\). The resolvent maps \(L^2\) into \(H^2\). Fourier Cauchy–Schwarz, using \(\int_{\mathbb R^2}(1+|k|^2)^{-2}dk<\infty\), shows that \(\psi\) is bounded and continuous. The positive convolution kernel gives \(\psi(0)>0\), so

\[
 M_s(t)\ge e^{Et}\frac{\psi(0)}{\|\psi\|_\infty}.
 \tag{14}
\]

For the reverse bound, the Duhamel series gives

\[
 T_t1=1+g\int_0^t T_uV_s\,du.
\]

For \(u\le1\), the integrand evaluated at zero is at most
\(e^{g\|V_s\|_\infty}\|V_s\|_\infty\). For \(u\ge1\), (7), Cauchy–Schwarz, and the spectral upper bound give

\[
 |(T_uV_s)(0)|
 \le e^{g\|V_s\|_\infty}\|p_1\|_2
       e^{E(u-1)}\|V_s\|_2.
\]

Both \(L^2\) norms are finite. Integration yields \(M_s(t)\le C_{g,s}e^{Et}\) for \(t\ge1\). Together with (14), this proves

\[
 \gamma(b,s)=E(g,s).
 \tag{15}
\]

## 2. Retaining the next block term

Fix \(s\). Write \(D_E=A+B_E\), and let \(C_s\) bound \(\|D_E\|\) for sufficiently small \(E\). The variational principle gives
\(\ell-C_s\le\mu(E)\le\ell+C_s\). When \(\ell>3C_s\), a top eigenvector can be written \(\alpha v+w\), with \(w\perp v\) and \(\alpha\ne0\). Otherwise its eigenvalue would have magnitude at most \(C_s\). Projecting the eigenvalue equation onto \(Q\) gives

\[
 w=\alpha R_E QD_Ev,
 \qquad R_E=(\mu(E)I_Q-QD_EQ)^{-1},
 \qquad \|R_E\|\le(\ell-2C_s)^{-1}.
\]

Projecting onto \(v\) gives the exact scalar equation

\[
 \mu(E)=\ell+\langle v,D_Ev\rangle
    +\langle QD_Ev,R_EQD_Ev\rangle.
 \tag{16}
\]

In the following inverse estimate all operators act on \(QL^2\):

\[
 R_E-\ell^{-1}I_Q
 =\ell^{-1}R_E\big((\ell-\mu(E))I_Q+QD_EQ\big).
\]

Its norm is at most \(2C_s/[\ell(\ell-2C_s)]=O_s(\ell^{-2})\). Define

\[
 a_s=\langle v,Av\rangle,\qquad c_s=\|QAv\|_2^2.
 \tag{17}
\]

By (12), \(\langle v,D_Ev\rangle=a_s+O_s(\sqrt E)\), and
\(QD_Ev=QAv+O_s(\sqrt E)\) in \(L^2\). Inserting these estimates in (16) proves

\[
 \mu(E)=\ell+a_s+\frac{c_s}{\ell}
            +O_s(\ell^{-2})+O_s(\sqrt E).
 \tag{18}
\]

As \(g\downarrow0\), the crossing \(E(g,s)\) tends to zero: at any fixed \(\eta>0\), eventually \(g\mu(\eta)<1\), so the unique crossing lies below \(\eta\). The bound \(|\mu(E)-\ell|\le C_s\) then gives
\(\ell=1/g+O_s(1)\) at the crossing. In particular
\(\sqrt E=O_s(e^{-2\pi/g})\). This is \(O_s(g^N)\) for every fixed \(N\), and \(1/\ell=g+O_s(g^2)\). Therefore (18) becomes

\[
 \frac1g=\ell+a_s+c_sg+O_s(g^2),
 \qquad
 \log E=-\frac{4\pi}{g}+4\pi a_s+4\pi c_sg+O_s(g^2).
 \tag{19}
\]

There is a second algebraic check on the sign and coefficient in (19). At the crossing, \(g\|D_E\|<1\) for small \(g\). The eigenvector equation \(K_Ef=f/g\) gives
\(f=g\ell\langle v,f\rangle(I-gD_E)^{-1}v\). Its projection onto \(v\), whose coefficient is nonzero, gives

\[
 \ell=\frac{1}{g\langle v,(I-gD_E)^{-1}v\rangle}.
\]

The norm-convergent Neumann series and (12) give
\(\langle v,(I-gD_E)^{-1}v\rangle
=1+ga_s+g^2\langle v,A^2v\rangle+O_s(g^3)\);
the exponentially small terms involving \(B_E\) are absorbed at this order. Taking the reciprocal yields
\(\ell=1/g-a_s+g(a_s^2-\langle v,A^2v\rangle)+O_s(g^2)\).
Since \(\langle v,A^2v\rangle-a_s^2=\|QAv\|^2=c_s\), this again gives \(\ell=1/g-a_s-c_sg+O_s(g^2)\).

## 3. The Gaussian coefficients

For independent \(X,Y\) with density \(V_s\), the random variable
\(|X-Y|^2/(8s)\) is unit exponential. It follows that

\[
 \mathbb E\log|X-Y|=\tfrac12(\log(8s)-\gamma_{\rm E}),
 \qquad
 a_s=-\frac{\log(2s)+\gamma_{\rm E}}{4\pi}.
 \tag{20}
\]

To calculate \(c_s\), put

\[
 L_s(x)=\int_{\mathbb R^2}V_s(y)\log|x-y|dy.
\]

Since \(Av(x)=v(x)[\log2-\gamma_{\rm E}-L_s(x)]/(2\pi)\), subtraction of its projection onto \(v\) gives

\[
 c_s=\frac{1}{4\pi^2}\operatorname{Var}(L_s(X)).
 \tag{21}
\]

For radii \(r\ne q\), the angular mean of \(\log|r-qe^{i\theta}|\) is \(\log\max(r,q)\): factor out the larger radius and take the real part of the absolutely convergent series for \(\log(1-ze^{i\theta})\), whose nonconstant terms have angular mean zero. Equal radii have measure zero under the Gaussian radial laws and do not affect the integral.

Let \(u=|x|^2/(4s)\), and let \(U\) be unit exponential. The preceding angular identity gives

\[
 L_s(x)=\tfrac12\log(4s)+\tfrac12\mathbb E\log\max(u,U).
\]

For \(u>0\), differentiation of the split integral for the last expectation gives derivative \((1-e^{-u})/u\); its value at zero is \(-\gamma_{\rm E}\). Thus, defining

\[
 \operatorname{Ein}(u)=\int_0^u\frac{1-e^{-z}}z\,dz
 =\int_0^1\frac{1-e^{-tu}}t\,dt,
\]

with the continuous integrand at zero, one obtains

\[
 L_s(x)=\frac{\log(4s)-\gamma_{\rm E}+\operatorname{Ein}(u)}2.
 \tag{22}
\]

All expectations below exist: \(0\le\operatorname{Ein}(u)\le u\), and \(U\) has finite moments. Tonelli's theorem gives

\[
 \mathbb E\operatorname{Ein}(U)
 =\int_0^1\frac{1-(1+t)^{-1}}t\,dt=\log2.
 \tag{23}
\]

For fixed \(t,q\ge0\), the covariance of \(1-e^{-tU}\) and \(1-e^{-qU}\) is

\[
 \frac1{1+t+q}-\frac1{(1+t)(1+q)}
 =\frac{tq}{(1+t+q)(1+t)(1+q)}.
\]

The variance of the integral defining Ein can be expanded under the two parameter integrals. One justification is to note that \((1-e^{-tU})/t\le U\), so all products are dominated by \(U^2\); Fubini applies. Subtracting the product of the means then yields

\[
 \operatorname{Var}(\operatorname{Ein}(U))
 =\int_0^1\int_0^1
       \frac{dt\,dq}{(1+t+q)(1+t)(1+q)}.
 \tag{24}
\]

Set \(x=t/(1+t)\), \(y=q/(1+q)\). The square maps to \([0,1/2]^2\),
\(dt\,dq=dx\,dy/[(1-x)^2(1-y)^2]\), and the denominator becomes
\((1-xy)/[(1-x)^2(1-y)^2]\). Hence

\[
 \operatorname{Var}(\operatorname{Ein}(U))
 =\int_0^{1/2}\int_0^{1/2}\frac{dx\,dy}{1-xy}
 =\sum_{n=0}^\infty\frac{(1/2)^{2n+2}}{(n+1)^2}=D.
 \tag{25}
\]

The series can be integrated term by term by monotone convergence, or by uniform convergence since \(xy\le1/4\). Equations (21) and (22) therefore give the scale-independent value

\[
 \boxed{c_s=\frac{D}{16\pi^2}.}
 \tag{26}
\]

Substituting (20) and (26) in (19), then using (15), gives

\[
 \log\gamma(b,s)
 =-\frac{4\pi}{g}-\log(2s)-\gamma_{\rm E}
       +\frac{D}{4\pi}g+O_s(g^2).
 \tag{27}
\]

For fixed \(s\), exponentiation gives (3), since
\(e^{Cg+O(g^2)}=1+Cg+O(g^2)\).

## 4. Independent series check of the variance

The variance in (25) can also be recovered by an orthogonal expansion. Define polynomials \(L_n\) by

\[
 \sum_{n=0}^\infty L_n(u)z^n
 =\frac{1}{1-z}\exp\!\left(-\frac{uz}{1-z}\right).
 \tag{28}
\]

For sufficiently small \(|z|,|w|\), integrating the product of these generating functions against \(e^{-u}du\) gives

\[
 \int_0^\infty e^{-u}
 \frac{e^{-uz/(1-z)}}{1-z}
 \frac{e^{-uw/(1-w)}}{1-w}\,du
 =\frac1{1-zw}.
\]

Differentiation under the integral near zero is justified by an integrable exponential bound. Comparing coefficients proves
\(\int_0^\infty e^{-u}L_n(u)L_m(u)du=\delta_{nm}\).

For fixed \(u\ge0\), integrate (28) after subtracting its constant term and dividing by \(z\), from zero to \(1/2\). The power series is uniformly convergent on this interval because its radius is at least one. This gives

\[
 H(u):=\sum_{n=1}^\infty\frac{L_n(u)}{n2^n}
 =\int_0^{1/2}
 \left[\frac{1}{1-z}e^{-uz/(1-z)}-1\right]\frac{dz}{z}.
\]

The integrand has a removable singularity at zero. Differentiating with respect to \(u\), and substituting \(t=z/(1-z)\), gives

\[
 H'(u)=-\int_0^{1/2}\frac{e^{-uz/(1-z)}}{(1-z)^2}dz
 =-\int_0^1e^{-ut}dt=-\frac{1-e^{-u}}u.
\]

Also \(L_n(0)=1\), so \(H(0)=\sum_{n\ge1}(n2^n)^{-1}=\log2\). Therefore
\(H(u)=\log2-\operatorname{Ein}(u)\).

By orthonormality, the partial sums defining \(H\) are Cauchy in \(L^2(e^{-u}du)\), since \(\sum(n^24^n)^{-1}<\infty\). Their pointwise limit just computed agrees almost everywhere with that \(L^2\) limit: an \(L^2\)-convergent sequence has an almost-everywhere convergent subsequence, obtained, for example, by choosing successive norm errors summable and applying Markov's inequality. Taking the squared \(L^2\) norm yields

\[
 \int_0^\infty e^{-u}(\operatorname{Ein}(u)-\log2)^2du
 =\sum_{n=1}^\infty\frac1{n^24^n}=D,
\]

independently confirming the covariance calculation.

## 5. Scaling and the renewal endpoint

Brownian scaling in (6), using \(V_s(\sqrt s\,x)=s^{-1}V_1(x)\), gives

\[
 M_s(t)=M_1(t/s),\qquad \gamma(b,s)=s^{-1}\gamma(b,1).
 \tag{29}
\]

Apply the already established estimate at \(s=1\) and this exact identity. The relative remainder in (3) is then bounded by the same constants for every \(s>0\), including when \(s\) varies with \(b\).

The identity
\(e^xE_1(x)=\int_0^\infty e^{-u}(u+x)^{-1}du\) shows that the left side of (4) is continuous and strictly decreasing in \(x\), with limits infinity and zero. Its positive root tends to zero with \(g\). The expansion derived after (9) gives

\[
 e^xE_1(x)=-\log x-\gamma_{\rm E}
              +O(x(1+|\log x|)).
\]

It first implies \(-\log x_g=4\pi/g+O(1)\), because its error tends to zero as \(x_g\to0\). Substituting that bound into its error then gives

\[
 \log x_g=-\frac{4\pi}{g}-\gamma_{\rm E}
                 +O(g^{-1}e^{-4\pi/g}).
\]

The error is smaller than every fixed positive power of \(g\). Thus division of (3) by \(x_g/(2s)\) proves (5), with the same scale-uniform error. In particular,

\[
 \lim_{b\to0}\frac1{b^2}
 \left(\frac{\gamma(b,s)}{x_{b^2}/(2s)}-1\right)
 =\frac{D}{4\pi}>0.
 \tag{30}
\]

For a general SHE diffusion coefficient \(d>0\), time change by \(2d\) gives
\(\gamma_d(b,s)=2d\,\gamma(b/\sqrt{2d},s)\). Consequently

\[
 \gamma_d(b,s)=\frac{d e^{-\gamma_{\rm E}}}{s}e^{-8\pi d/b^2}
 \left(1+\frac{D}{8\pi d}b^2
              +O\!\left((b^2/d)^2\right)\right).
 \tag{31}
\]

For the prompt's diffusion coefficient \(d=1\), both the exponential constant \(8\pi\) and the relative correction \(D/(8\pi)\) follow. Negative \(b\) gives the same rate because only \(g=b^2\) enters (6). At \(b=0\), \(Z=1\) and the rate is zero. The singular covariance limit \(s=0\) is excluded.

## Scope

Neither a height-variance exponent nor a roughness exponent follows from this annealed moment expansion. It also does not give a non-Gaussian fixed-coupling height limit. These conclusions require information about centered \(\log Z\) that is absent here.
