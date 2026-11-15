# A renewal sandwich for a Gaussian-smoothed two-dimensional SHE

Let

\[
 R_s(x)=\frac{1}{4\pi s}\exp\!\left(-\frac{|x|^2}{4s}\right),\qquad s>0,
\]

and let \(W_s\) be a centered Gaussian noise with covariance
\(\mathbb E[W_s(dt,x)W_s(dt,y)]=R_s(x-y)dt\).
Consider the Itô equation on \(\mathbb R^2\)

\[
 dZ=\tfrac12\Delta Z\,dt+bZ\,W_s(dt,x),\qquad Z(0,x)=1,
 \qquad b\ne0.
 \tag{1}
\]

The covariance is smooth and bounded. In particular, the usual mild solution exists with finite second moments on bounded time intervals. Set \(g=b^2\) and \(M(t)=\mathbb E[Z(t,0)^2]\). Define \(x_g>0\) as the unique solution of

\[
 \frac{g}{4\pi}\Phi(x_g)=1,
 \qquad
 \Phi(x)=\int_0^\infty\frac{e^{-v}}{v+x}\,dv
         =e^x E_1(x),
 \quad E_1(x)=\int_x^\infty\frac{e^{-v}}v\,dv.
 \tag{2}
\]

**Proposition.** The limit

\[
 \gamma(b,s)=\lim_{t\to\infty}\frac{\log M(t)}t
\]

exists, and

\[
 \boxed{\quad \frac{x_g}{2s}\le\gamma(b,s)\le\frac{x_g}{s}.\quad}
 \tag{3}
\]

More precisely, define

\[
 k_a(u)=\frac{g}{4\pi(u+a)},\qquad
 F_a(t)=1+\sum_{n\ge1}\int_{\substack{u_i>0\\u_1+\cdots+u_n<t}}
                  \prod_{i=1}^n k_a(u_i)\,du_1\cdots du_n.
 \tag{4}
\]

For every \(t\ge0\),

\[
 F_{2s}(t)\le M(t)\le F_s(t).
 \tag{5}
\]

Consequently,

\[
 \lim_{b\to0}b^2\log\big(s\gamma(b,s)\big)=-4\pi.
 \tag{6}
\]

Here \(s\) is fixed. The sign of \(b\) does not matter.

## 1. The second moment as a Brownian functional

For completeness, the second moment closure can be obtained directly from Itô multiplication. If \(U(t,x,y)=\mathbb E[Z(t,x)Z(t,y)]\), the two diffusion terms are \(\tfrac12(\Delta_x+\Delta_y)U\), and the quadratic covariation contributes \(gR_s(x-y)U\). The initial condition is \(U(0,x,y)=1\). Boundedness of \(R_s\) permits the convergent Duhamel expansion and identifies the unique bounded solution on each finite time interval. Equivalently, the Feynman–Kac formula gives

\[
 U(t,x,y)=\mathbb E_{x,y}\exp\!\left(g\int_0^t R_s(B_u^1-B_u^2)\,du\right),
 \tag{7}
\]

where the two independent Brownian motions have generator \(\tfrac12\Delta\).
Their difference \(D\) has generator \(\Delta\) and covariance \(2uI_2\). Thus

\[
 M(t)=\mathbb E_0\exp\!\left(g\int_0^tR_s(D_u)\,du\right).
 \tag{8}
\]

There is no self-interaction term in (7): equation (1) is interpreted in the Itô sense. Also
\(1\le M(t)\le\exp(gR_s(0)t)\).

## 2. Gaussian products at ordered times

For \(n\ge1\), let \(0<t_1<\cdots<t_n\) and put \(u_i=t_i-t_{i-1}\), with \(t_0=0\). Write

\[
 A_n(u_1,\ldots,u_n)=\mathbb E_0\prod_{i=1}^n R_s(D_{t_i}).
\]

After weighting by the first \(i-1\) factors and normalizing, suppose that the position has Gaussian law \(N(0,v_{i-1}I_2)\). Initially \(v_0=0\). Brownian propagation across the next gap gives covariance
\(w_i I_2\), where \(w_i=v_{i-1}+2u_i\).
Multiplication by \(R_s\), which is the density of \(N(0,2sI_2)\), has normalizing constant

\[
 c_i=\int_{\mathbb R^2}\frac{e^{-|z|^2/(2w_i)}}{2\pi w_i}
                         \frac{e^{-|z|^2/(4s)}}{4\pi s}\,dz
     =\frac{1}{2\pi(w_i+2s)}.
 \tag{9}
\]

The normalized product has covariance

\[
 v_i I_2,\qquad v_i=\frac{2s\,w_i}{w_i+2s}.
 \tag{10}
\]

Hence \(0\le v_i<2s\) at every stage, and

\[
 A_n=\prod_{i=1}^n c_i,\qquad
 \prod_{i=1}^n\frac1{4\pi(u_i+2s)}
 \le A_n\le
 \prod_{i=1}^n\frac1{4\pi(u_i+s)}.
 \tag{11}
\]

All integration steps are finite Gaussian integrals; the normalization at each stage is conditional on the previous weights, not on an unweighted Brownian distribution.

Expand the exponential in (8). For each path, the factor \(1/n!\) in the exponential series cancels the \(n!\) orderings of the integration cube. Nonnegativity permits termwise integration. Changing ordered times to gaps and applying (11) proves (5). The series converge locally uniformly, since the \(n\)-th term is bounded by \((g t/(4\pi s))^n/n!\).

## 3. Scalar renewal growth

The definition (4) implies the Volterra equation

\[
 F_a(t)=1+\int_0^t k_a(u)F_a(t-u)\,du.
 \tag{12}
\]

Its kernel has Laplace transform

\[
 L_a(r)=\int_0^\infty e^{-ru}k_a(u)\,du
       =\frac{g}{4\pi}\Phi(ar),\qquad r>0.
 \tag{13}
\]

The substitution \(v=ru\) gives the last equality. This transform is continuous and strictly decreasing, tends to infinity as \(r\downarrow0\), and tends to zero as \(r\uparrow\infty\). The first limit follows by monotone convergence from \(\int_0^\infty (u+a)^{-1}du=\infty\). The last follows from \(L_a(r)\le g/(4\pi ar)\). Thus its unique root \(L_a(r_a)=1\) is \(r_a=x_g/a\).

To prove that \(r_a\) is the exponential rate without a renewal limit theorem, first take \(r>r_a\), so \(L_a(r)<1\). In each term of (4), insert \(e^{r\sum_i u_i}\le e^{rt}\). Extend the integral to all positive gaps after multiplying its kernel by \(e^{-ru}\). This gives

\[
 F_a(t)\le \frac{e^{rt}}{1-L_a(r)}.
 \tag{14}
\]

Next take \(0<r<r_a\). Choose \(T<\infty\) with
\(\int_0^T e^{-ru}k_a(u)du\ge1\), possible since \(L_a(r)>1\).
Set \(w(t)=e^{-rT}e^{rt}\). Then

\[
 w(t)-(k_a*w)(t)
 =e^{r(t-T)}\left(1-\int_0^t e^{-ru}k_a(u)du\right)\le1.
 \tag{15}
\]

For \(t\le T\), both factors on the right are at most 1, and the second is allowed to be negative. For \(t\ge T\), the second factor is nonpositive. Thus \(w\le1+k_a*w\).
Iterate this inequality \(N\) times. The partial renewal series is at most \(F_a\), while the remaining convolution \(k_a^{*N}*w\) tends to zero on every bounded time interval: it is bounded there by
\(\sup_{v\le t}w(v)\,[g t/(4\pi a)]^N/N!\).
Consequently \(w(t)\le F_a(t)\). Combining this with (14), taking logarithms and then \(r\uparrow r_a\) or \(r\downarrow r_a\), proves

\[
 \lim_{t\to\infty}t^{-1}\log F_a(t)=r_a.
 \tag{16}
\]

Equations (5) and (16) already give (3) with lower and upper limits in place of \(\gamma\).

## 4. Existence of the second-moment rate

Let
\(u(t,z)=\mathbb E_z\exp(g\int_0^t R_s(D_v)dv)\).
The Gaussian calculation above also proves \(u(t,z)\le u(t,0)\). Indeed, start at a deterministic nonzero \(z\). At each weighting step the predicted Gaussian has some mean \(m_i\) and covariance \(w_iI_2\). Its normalizing constant is

\[
 c_i\exp\!\left(-\frac{|m_i|^2}{2(w_i+2s)}\right)\le c_i.
 \tag{17}
\]

The covariance recursion is unchanged by the mean. Therefore every ordered product expectation starting at \(z\) is at most its counterpart starting at zero. Sum its nonnegative expansion to obtain the assertion.

By the Markov property,

\[
 M(t+q)=\mathbb E_0\left[e^{g\int_0^t R_s(D_v)dv}u(q,D_t)\right]
       \le M(t)M(q).
 \tag{18}
\]

Thus \(f(t)=\log M(t)\) is subadditive and \(0\le f(t)\le gR_s(0)t\). Fix \(T>0\) and write \(t=nT+r\), \(0\le r<T\). Then
\(f(t)\le n f(T)+gR_s(0)T\), whence
\(\limsup_{t\to\infty} f(t)/t\le f(T)/T\).
Taking the infimum over \(T>0\), and using
\(f(t)/t\ge\inf_{T>0}f(T)/T\), proves existence of the limit. This completes (3).

## 5. Weak-coupling scale and diffusion normalization

As \(x\downarrow0\), split the integral in (2) at 1:

\[
 \Phi(x)=\int_0^1\frac{dv}{v+x}
       +\int_0^1\frac{e^{-v}-1}{v+x}\,dv
       +\int_1^\infty\frac{e^{-v}}{v+x}\,dv
       =\log(1/x)+O(1).
 \tag{19}
\]

The absolute value of the middle integral is at most 1, since \(1-e^{-v}\le v\); the last is at most \(e^{-1}\). Equation (2) implies \(x_g\downarrow0\) and
\(g\log x_g=-4\pi+O(g)\). From (3),
\(\log(s\gamma)=\log x_g+O(1)\), proving (6).

For an equation with diffusion coefficient \(d>0\), namely \(dZ=d\Delta Z\,dt+bZ\,W_s(dt,x)\), put \(\tau=2dt\). The equation in time \(\tau\) has diffusion coefficient \(1/2\) and noise coefficient \(b/\sqrt{2d}\). Therefore

\[
 \gamma_d(b,s)=2d\,\gamma\!\left(\frac{b}{\sqrt{2d}},s\right),\qquad
 \frac{d}{s}x_{b^2/(2d)}\le\gamma_d(b,s)\le\frac{2d}{s}x_{b^2/(2d)}.
 \tag{20}
\]

In particular \(\lim_{b\to0} b^2\log(s\gamma_d(b,s))=-8\pi d\).
For the prompt's diffusion coefficient \(d=1\), \(Z\) with \(b=\lambda\) corresponds by Itô's formula to

\[
 h(t,x)=\lambda^{-1}\log Z(t,x)+\tfrac12\lambda R_s(0)t,
\]

which solves the spatially smoothed KPZ equation in the prompt, with flat initial condition. The added deterministic height does not affect its variance. The estimates above concern \(Z^2\), not \(\operatorname{Var}(\log Z)\).

## 6. Independent Gaussian identities

The constants in (11) can also be checked without sequential conditioning. Let \(C_{ij}=\min(t_i,t_j)\). One coordinate of \((D_{t_1},\ldots,D_{t_n})\) is a centered Gaussian vector with covariance \(2C\). Integrating its density against \(\exp(-|z|^2/(4s))\) gives
\(\det(I+C/s)^{-1/2}\): combine the two quadratic forms in the Gaussian integral and divide the resulting normalizing determinant by that of the original density. The two coordinates are independent, so

\[
 A_n=(4\pi s)^{-n}\det(I+C/s)^{-1}.
 \tag{21}
\]

For two gaps \(u,v>0\), \(C=\left(\begin{smallmatrix}u&u\\u&u+v\end{smallmatrix}\right)\), and therefore

\[
 A_2(u,v)=\frac1{(4\pi)^2(s^2+2su+sv+uv)}.
 \tag{22}
\]

This also follows by substituting \(v_1=2su/(s+u)\) into (9). For one gap, \(A_1(u)=1/[4\pi(s+u)]\), and hence the first term after 1 in the expansion of \(M(t)\) is exactly
\(g(4\pi)^{-1}\log(1+t/s)\). In particular, \(M'(0)=g/(4\pi s)=gR_s(0)\), also obtained directly from (8).

## Scope

The result is an explicit estimate for one fixed mollifier and flat initial data. Second-moment intermittency in dimension two is established background; see Le Chen and Kunwoo Kim, *Nonlinear stochastic heat equation driven by spatially colored noise: moments and intermittency*, [arXiv:1510.06046](https://arxiv.org/abs/1510.06046), introduction and Theorem 1.3. No novelty beyond the earlier T090 report is asserted for the general phenomenon. The proof here supplies the finite-time scalar sandwich and its constants directly.

Neither (3) nor (6) determines the variance, roughness exponent, or limiting law of the centered height. A positive exponential growth rate of an exponential moment can be caused by rare heights. In particular, \(\gamma^{-1}\) is a second-moment time scale; it has not been proved to be a crossover time for typical KPZ height fluctuations.
