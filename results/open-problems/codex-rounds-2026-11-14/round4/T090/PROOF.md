# Sharp weak-coupling prefactor for the Gaussian second moment

Let

\[
 V_s(x)=R_s(x)=\frac{1}{4\pi s}e^{-|x|^2/(4s)},\qquad s>0,
\]

and consider the flat-initial-data Itô equation on \(\mathbb R^2\)

\[
 dZ=\tfrac12\Delta Z\,dt+bZ\,W_s(dt,x),\quad Z(0,x)=1,
 \quad \mathbb E[W_s(dt,x)W_s(dt,y)]=R_s(x-y)dt.
 \tag{1}
\]

Write \(g=b^2>0\) and let \(\gamma_{\rm E}=0.57721\ldots\) denote Euler's constant. All logarithms are natural.

**Theorem.** The second-moment rate satisfies

\[
 \gamma(b,s):=\lim_{t\to\infty}\frac1t\log\mathbb E[Z(t,0)^2]
 =\frac{e^{-\gamma_{\rm E}}}{2s}\exp\!\left(-\frac{4\pi}{b^2}\right)
   \bigl(1+O(b^2)\bigr),\qquad b\to0.
 \tag{2}
\]

The error in the relative expression can be chosen independent of \(s>0\), by exact spatial scaling. If \(x_g\) is the positive root of

\[
 \frac{g}{4\pi}e^{x_g}E_1(x_g)=1,\qquad
 E_1(x)=\int_x^\infty\frac{e^{-u}}u\,du,
 \tag{3}
\]

then

\[
 \frac{\gamma(b,s)}{x_{b^2}/(2s)}=1+O(b^2)\longrightarrow1.
 \tag{4}
\]

This sharpens the lower endpoint of the preceding round's renewal sandwich. The theorem concerns an annealed exponential moment, not the variance of the height.

## 1. Reduction to a bounded-potential semigroup

Itô multiplication shows that \(U(t,x,y)=\mathbb E[Z(t,x)Z(t,y)]\) solves

\[
 \partial_t U=\tfrac12(\Delta_x+\Delta_y)U+gR_s(x-y)U,
 \qquad U(0,x,y)=1.
\]

Since \(R_s\) is bounded, the Duhamel series converges absolutely on each bounded time interval. It identifies this solution with the Feynman–Kac expression for two independent Brownian motions of generator \(\tfrac12\Delta\). Their difference has generator \(\Delta\), so

\[
 M(t):=\mathbb E[Z(t,0)^2]
 =\mathbb E_0\exp\!\left(g\int_0^tV_s(D_u)du\right).
 \tag{5}
\]

In particular, there is no self-interaction correction in (5); (1) is the Itô equation. Define on \(L^2(\mathbb R^2)\)

\[
 H=\Delta+gV_s,\qquad \operatorname{dom}H=H^2(\mathbb R^2),
 \qquad T_t=e^{tH}.
\]

Bounded real multiplication preserves self-adjointness on this domain. The semigroup also acts on bounded functions by Feynman–Kac. For its integral kernel,

\[
 0<k_t^g(x,y)\le e^{g\|V_s\|_\infty t}p_t(x-y),\qquad
 p_t(z)=\frac{e^{-|z|^2/(4t)}}{4\pi t}.
 \tag{6}
\]

For example, (6) follows by expanding the bounded potential and bounding each of its factors by \(g\|V_s\|_\infty\), then using the heat-kernel convolution identity. Also \(M(t)=(T_t1)(0)\).

## 2. A uniform free-resolvent decomposition

For \(E>0\), integration of the heat kernel gives the free resolvent kernel

\[
 G_E(r)=\int_0^\infty e^{-Et}p_t(r)dt
 =\frac1{4\pi}\int_0^\infty e^{-u-Er^2/(4u)}\frac{du}{u},\qquad r>0.
 \tag{7}
\]

Put \(J(a)=\int_0^\infty e^{-u-a/u}du/u\). With \(z=\sqrt a\), substitution \(u=a/w\) in the part below \(z\) gives

\[
 J(a)=2\int_z^\infty e^{-u-a/u}\frac{du}{u}.
\]

Since \(0\le1-e^{-a/u}\le a/u\),

\[
 |J(a)-2E_1(z)|\le2a\int_z^\infty\frac{du}{u^2}=2\sqrt a.
 \tag{8}
\]

The identity

\[
 E_1(z)=-\gamma_{\rm E}-\log z+
       \int_0^z\frac{1-e^{-u}}u\,du
 \tag{9}
\]

follows by differentiating the two sides and matching the constant at zero. That constant can also be obtained by integration by parts from
\(\int_0^\infty e^{-u}\log u\,du=-\gamma_{\rm E}\).
The last integral in (9) lies between zero and \(z\). Combining (8) and (9) proves

\[
 |J(a)+\log a+2\gamma_{\rm E}|\le4\sqrt a\quad(a>0).
 \tag{10}
\]

In particular the bound is global, including large separations \(r\). Substituting \(a=Er^2/4\) into (7) gives

\[
 G_E(r)=\frac{-\log E}{4\pi}
 +\frac{\log2-\gamma_{\rm E}-\log r}{2\pi}
 +\mathcal R_E(r),\qquad
 |\mathcal R_E(r)|\le\frac{\sqrt E\,r}{2\pi}.
 \tag{11}
\]

This derives both the logarithmic coefficient and the finite constant directly from the heat kernel.

Fix \(s>0\) temporarily and write \(V=V_s\), \(v=\sqrt V\). Since \(\int V=1\), \(\|v\|_2=1\). On \(L^2\) set

\[
 K_E=v(E-\Delta)^{-1}v,\quad
 P f=\langle v,f\rangle v,\quad
 \ell(E)=\frac{-\log E}{4\pi}.
\]

Here and below \(v\) also denotes multiplication when used next to an operator. Equation (11) yields

\[
 K_E=\ell(E)P+A+B_E,
 \tag{12}
\]

where the kernels are

\[
 A(x,y)=\frac{v(x)v(y)}{2\pi}
       (\log2-\gamma_{\rm E}-\log|x-y|),\qquad
 B_E(x,y)=v(x)\mathcal R_E(|x-y|)v(y).
\]

The operator \(A\) is Hilbert–Schmidt. Indeed its squared kernel integral is a constant multiple of an integral of \(1+\log^2|X-Y|\), where \(X,Y\) are independent with density \(V\). Their difference has Gaussian density \(R_{2s}\). Near zero the radial integral is bounded by a constant times \(\int_0^1r(1+\log^2r)dr<\infty\); at infinity the Gaussian density makes it finite. Moreover (11) gives the explicit bound

\[
 \|B_E\|^2\le\|B_E\|_{\rm HS}^2
 \le\frac{E}{4\pi^2}\iint V(x)V(y)|x-y|^2dxdy
 =\frac{2s}{\pi^2}E.
 \tag{13}
\]

Here each coordinate of \(X-Y\) has variance \(4s\), so its squared length has mean \(8s\). In particular, \(K_E\) is compact for every \(E>0\), and the noncompact support of the potential causes no omitted tail term.

## 3. The spectral threshold and the pointwise growth rate

The compact operator \(K_E\) is nonnegative and self-adjoint, since the free resolvent has those properties. Let \(\mu(E)=\|K_E\|\), its largest eigenvalue. It is positive, continuous for \(E>0\), and strictly decreasing. To see strict decrease, for \(E_1<E_2\) and nonzero \(f\), the resolvent identity gives

\[
 \langle f,(K_{E_1}-K_{E_2})f\rangle
 =(E_2-E_1)\left\langle vf,
 (E_1-\Delta)^{-1}(E_2-\Delta)^{-1}vf\right\rangle>0.
\]

The last inequality follows in Fourier variables, where the multiplier is strictly positive, and \(vf\ne0\) because \(v>0\). Apply this to a normalized top eigenvector at \(E_2\) to obtain \(\mu(E_1)>\mu(E_2)\). Norm continuity follows from the same resolvent identity and boundedness of multiplication by \(v\).

As \(E\to\infty\), \(\mu(E)\le\|V\|_\infty/E\to0\). As \(E\downarrow0\), (12) and the trial vector \(v\) give \(\mu(E)\to\infty\). Hence, for every \(g>0\), there is a unique \(E=E(g,s)>0\) such that

\[
 g\mu(E)=1.
 \tag{14}
\]

This \(E\) is the top of the spectrum of \(H\). Here is a quadratic-form verification. Write \(S=(E-\Delta)^{1/2}\). For \(f\in H^1\),

\[
 \langle f,(E-H)f\rangle
 =\|Sf\|_2^2-g\|vf\|_2^2.
\]

The squared norm of \(vS^{-1}\) is \(\|vS^{-2}v\|=\mu(E)\), by equality of the nonzero operator norms of \(C^*C\) and \(CC^*\), with \(C=vS^{-1}\). Thus (14) implies \(E-H\ge0\) as a form.

The kernel of \(K_E\) is strictly positive off the diagonal. A normalized top eigenvector may be chosen nonnegative: replacing it by its absolute value increases its Rayleigh quotient, which cannot exceed the top eigenvalue. Let \(f\ge0\) be such an eigenvector and set

\[
 \psi=(E-\Delta)^{-1}(vf).
\]

Then \(\psi>0\) and \(v\psi=f/g\), so
\((E-\Delta)\psi=vf=gV\psi\), that is, \(H\psi=E\psi\). The right-hand side defining \(\psi\) is in \(L^2\), and the free resolvent maps it into \(H^2\). The Fourier Cauchy–Schwarz estimate using \(\int_{\mathbb R^2}(1+|k|^2)^{-2}dk<\infty\) shows that \(\psi\) has a bounded continuous representative. Its convolution formula with \(G_E>0\) gives \(\psi(0)>0\). Thus \(E\) is an eigenvalue as well as an upper spectral bound.

The eigenfunction and positivity give a lower bound for (5):

\[
 M(t)=(T_t1)(0)
 \ge \frac{(T_t\psi)(0)}{\|\psi\|_\infty}
 =e^{Et}\frac{\psi(0)}{\|\psi\|_\infty}.
 \tag{15}
\]

For the upper bound use the other Duhamel identity, first justified by its convergent bounded-potential series:

\[
 T_t1=1+g\int_0^t T_uV\,du.
 \tag{16}
\]

Indeed, \(T_t-P_t=\int_0^t T_u(gV)P_{t-u}du\), and \(P_{t-u}1=1\). For \(0\le u\le1\), \((T_uV)(0)\le e^{g\|V\|_\infty}\|V\|_\infty\). For \(u\ge1\), (6), Cauchy–Schwarz, and the spectral bound imply

\[
 |(T_uV)(0)|
 \le\|k_1^g(0,\cdot)\|_2\,\|T_{u-1}V\|_2
 \le e^{g\|V\|_\infty}\|p_1\|_2 e^{E(u-1)}\|V\|_2.
\]

Both \(V\) and \(p_1\) belong to \(L^2\). Since \(E>0\), integrating (16) gives \(M(t)\le C_{g,s}e^{Et}\) for \(t\ge1\), with a finite constant independent of \(t\). Together with (15), this proves

\[
 \gamma(b,s)=E(g,s).
 \tag{17}
\]

This argument does not assume that the constant initial function belongs to \(L^2\).

## 4. Rank-one eigenvalue expansion

In (12) put \(D_E=A+B_E\) and \(Q=I-P\). For sufficiently small \(E\), \(\|D_E\|\le C_s\), while \(\ell=\ell(E)\to\infty\). The variational principle gives

\[
 \ell-C_s\le\mu(E)\le\ell+C_s.
\]

Choose \(E\) small enough that \(\ell>3C_s\). Decompose a normalized top eigenvector as \(f=\alpha v+w\), \(w\perp v\). We have \(\alpha\ne0\), since otherwise its eigenvalue would be at most \(C_s\). Projecting the eigenvalue equation onto \(Q\) gives

\[
 w=\alpha(\mu-QD_EQ)^{-1}QD_Ev,
\]

where the inverse has norm at most \((\ell-2C_s)^{-1}\). Projecting onto \(v\) and dividing by \(\alpha\) therefore gives

\[
 \mu(E)=\ell+\langle v,D_Ev\rangle
 +\langle QD_Ev,(\mu-QD_EQ)^{-1}QD_Ev\rangle.
\]

The last term has absolute value at most \(C_s^2/(\ell-2C_s)\). By (13),

\[
 \mu(E)=\frac{-\log E}{4\pi}+a_s+
 O_s\!\left(\frac1{|\log E|}\right),\qquad
 a_s=\langle v,Av\rangle.
 \tag{18}
\]

The \(O_s(\sqrt E)\) term from \(B_E\) is absorbed because \(\sqrt E\,|\log E|\to0\).

To compute \(a_s\), take independent \(X,Y\) with density \(R_s\). Their difference has density \(R_{2s}\), hence

\[
 U=\frac{|X-Y|^2}{8s}
 \quad\hbox{has density }e^{-u}\,1_{u>0}.
\]

The logarithm is integrable, and

\[
 \mathbb E\log|X-Y|
 =\tfrac12\log(8s)+\tfrac12\int_0^\infty e^{-u}\log u\,du
 =\tfrac12(\log(8s)-\gamma_{\rm E}).
\]

Consequently

\[
 a_s=\frac{\log2-\gamma_{\rm E}-\mathbb E\log|X-Y|}{2\pi}
 =-\frac{\log(2s)+\gamma_{\rm E}}{4\pi}.
 \tag{19}
\]

As \(g\downarrow0\), (14) forces \(E(g,s)\downarrow0\): for each fixed \(\eta>0\), \(g\mu(\eta)<1\) eventually, so the crossing lies below \(\eta\). Equations (14) and (18) first give \(\ell=1/g+O_s(1)\). Substituting this back into their error term then gives

\[
 \frac1g=\frac{-\log E}{4\pi}+a_s+O_s(g),
\]

and hence, using (19),

\[
 \log E=-\frac{4\pi}{g}-\log(2s)-\gamma_{\rm E}+O_s(g).
 \tag{20}
\]

Exponentiating and using (17) proves (2) for fixed \(s\).

## 5. Scaling, the renewal endpoint, and normalization

Brownian scaling and \(V_s(\sqrt s\,x)=s^{-1}V_1(x)\) give directly from (5)

\[
 M_s(t)=M_1(t/s),\qquad \gamma(b,s)=s^{-1}\gamma(b,1).
 \tag{21}
\]

Thus the relative error in (2) can be taken independent of \(s>0\).

For (3), the function \(e^xE_1(x)=\int_0^\infty e^{-u}/(u+x)du\) decreases continuously from infinity to zero, so the root is unique and tends to zero with \(g\). Formula (9) gives

\[
 e^xE_1(x)=-\log x-\gamma_{\rm E}
             +O\bigl(x(1+|\log x|)\bigr).
\]

At the root, this first implies \(-\log x_g=4\pi/g+O(1)\). The error term is consequently \(o(g)\), and substitution once more gives

\[
 x_g=e^{-\gamma_{\rm E}}e^{-4\pi/g}(1+o(g)).
\]

Combining with (2) proves (4). The earlier renewal lower bound additionally shows that the ratio in (4) is at least one at every \(g>0\).

For an SHE diffusion coefficient \(d>0\), the difference process has generator \(2d\Delta\). The time change \(\tau=2dt\) gives

\[
 \gamma_d(b,s)=2d\,\gamma\!\left(\frac{b}{\sqrt{2d}},s\right)
 =\frac{d e^{-\gamma_{\rm E}}}{s}
      e^{-8\pi d/b^2}\bigl(1+O(b^2/d)\bigr),
 \tag{22}
\]

for fixed \(d>0\). Thus the prompt's diffusion coefficient \(d=1\) has \(8\pi\), not \(4\pi\), in the exponent. In that normalization, with \(b=\lambda\),
\(h=\lambda^{-1}\log Z+\tfrac12\lambda R_s(0)t\) solves the stated smoothed KPZ equation. The deterministic term has no effect on its variance, but (22) estimates \(\mathbb E[Z^2]\), not that variance.

## 6. Independent check of the finite constant

There is a second calculation of (19). For fixed radii \(r,q\), averaging \(\log|r-qe^{i\theta}|\) over \(\theta\) gives \(\log\max(r,q)\). For \(r\ne q\), expand \(\log(1-ze^{i\theta})=-\sum_{n\ge1}z^ne^{in\theta}/n\), \(|z|<1\), and take real parts and the angular average. Equality of radii has probability zero under the Gaussian laws, so it does not affect the expectation.

If \(U=|X|^2/(4s)\), \(V'=|Y|^2/(4s)\), then \(U,V'\) are independent unit exponentials. Their maximum has density \(2e^{-u}(1-e^{-u})\), so angular averaging gives

\[
 \mathbb E\log|X-Y|=\tfrac12\log(4s)
 +\tfrac12\int_0^\infty2(e^{-u}-e^{-2u})\log u\,du.
\]

For \(c>0\), substitution \(w=cu\) yields
\(\int_0^\infty e^{-cu}\log u\,du=(-\gamma_{\rm E}-\log c)/c\).
The last display therefore equals
\(\tfrac12\log(4s)+\tfrac12(-\gamma_{\rm E}+\log2)
=\tfrac12(\log(8s)-\gamma_{\rm E})\), agreeing with (19).

## Scope and background

The logarithmic rank-one resolvent method is established spectral theory. Relevant background actually consulted is Jussi Behrndt, Petr Siegl, Nicolas Weber, *Revisiting the Weak Coupling Phenomenon for Two-Dimensional Schrödinger Operators*, [arXiv:2604.19284](https://arxiv.org/abs/2604.19284), and Sylwia Kondej, Vladimir Lotoreichik, *Weakly coupled bound state of 2D Schrödinger operator with potential-measure*, [arXiv:1402.3995](https://arxiv.org/abs/1402.3995). The latter's compact-support hypotheses are not invoked for the Gaussian potential. Equations (7)–(20) give the needed estimates directly.

The explicit Gaussian prefactor and comparison (4) are the advance relative to the preceding T090 report. No novelty claim in the wider spectral literature is made. No exponent for typical height fluctuations, roughness, or non-Gaussian fixed-coupling height limit follows from this result.
