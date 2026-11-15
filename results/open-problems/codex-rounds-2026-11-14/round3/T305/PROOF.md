# Finite-step remainder drift for leapfrog

Let
\[
 \mathcal H(x,p)=V(x)+|p|^2/2,\qquad
 \rho(dx,dp)=\pi(dx)N(0,I)(dp),
\]
and let \(\Phi_T\) be its exact Hamiltonian flow. Write \(\Psi_h\) for
kick–drift–kick leapfrog, \(T=nh>0\), and
\[
 A(x,p)=\frac1{12}p^T\nabla^2V(x)p-\frac1{24}|\nabla V(x)|^2,
 \quad B_T=A-A\circ\Phi_T,
\]
\[
 \Delta_{h,T}=\mathcal H\circ\Psi_h^n-\mathcal H,
 \qquad R_{h,T}=\Delta_{h,T}-h^2B_T.
 \tag{1}
\]
All energy errors below are for the proposal before a Metropolis decision.

## 1. An identity on the full class

Suppose \(V\in C^2\) and \(mI\preceq\nabla^2V\preceq LI\), with
\(0<m\le L<\infty\). Then
\[
 E_\rho R_{h,T}
 =D_{\rm KL}((\Psi_h^n)_\#\rho\,\|\,\rho)\ge0.
 \tag{2}
\]
No restriction on \(h\) is needed in (2).

To prove this, put \(S=\Psi_h^n\). A kick
\((x,p)\mapsto(x,p-h\nabla V(x)/2)\) and a drift
\((x,p)\mapsto(x+hp,p)\) are invertible shears with Jacobian determinant
one. Thus \(S\) is a global volume-preserving diffeomorphism. If \(f\)
is the density of \(\rho\) and \(q\) the density of \(S_\#\rho\), then
\(q(Sz)=f(z)\). Consequently
\[
 \begin{aligned}
 D_{\rm KL}(S_\#\rho\,\|\,\rho)
 &=\int f(z)\log\frac{q(Sz)}{f(Sz)}\,dz\\
 &=E_\rho[\mathcal H(SZ)-\mathcal H(Z)].
 \end{aligned}
 \tag{3}
\]
These integrals are finite: the bounded Hessian implies linear growth of
the gradient, at most quadratic growth of \(V\), and finite second moments
under \(\rho\). Each fixed finite composition of the shears has at most
linear growth. Also \(|A(z)|\) has at most quadratic growth. The exact
flow preserves both volume and \(\mathcal H\), hence preserves \(\rho\).
It follows that \(E_\rho B_T=0\), proving (2). The same change of
variables also gives \(E_\rho e^{-\Delta_{h,T}}=1\).

In particular, subtracting the exact-flow leading coefficient cannot
remove the mean numerical energy error.

There is also an acceptance interpretation. Let
\(r(z)=(1-e^{-\Delta_{h,T}(z)})_+\) be the conditional rejection
probability. Then
\[
 E_\rho r
 =\|S_\#\rho-\rho\|_{\rm TV}
 \le\sqrt{\tfrac12 E_\rho R_{h,T}}.
 \tag{3a}
\]
Indeed
\[
 E_\rho r=\int(f(z)-f(Sz))_+dz
 =\|\rho-S^{-1}_\#\rho\|_{\rm TV}
 =\|S_\#\rho-\rho\|_{\rm TV}.
\]
The middle equality uses that \(f\circ S\) is a probability density;
the last uses invariance of total variation under an invertible map.
For the inequality, let \(B=\{q\ge f\}\), \(t=\int_Bq\), and
\(s=\int_Bf\). Then \(t-s=\|q-f\|_{\rm TV}\). Jensen's inequality on
\(B\) and its complement gives
\[
 D_{\rm KL}(q\|f)\ge
 t\log(t/s)+(1-t)\log((1-t)/(1-s))\ge2(t-s)^2.
\]
For the last inequality, the binary relative entropy, as a function of
\(t\), vanishes and has derivative zero at \(t=s\), while its second
derivative is \(1/[t(1-t)]\ge4\). Integrating this second derivative twice
proves the assertion; boundary cases follow by limits. Combine with (2).

This controls stationary average rejection. Transferring it by the warm
density bound alone incurs a factor \(M_0\), so it does not provide the
logarithmic warm-start dependence sought in T305.

## 2. A finite-step Gaussian theorem

Suppose now
\[
 V(x)=\tfrac12(x-x_*)^TK(x-x_*)+c,
 \qquad mI\preceq K\preceq LI.
\]
Let \(\lambda_1,\ldots,\lambda_d\) be the eigenvalues of \(K\), and
assume \(h\sqrt L\le1\). Define
\[
 a_i=\frac{h^2\lambda_i}{4},\quad r_i=\sqrt{1-a_i},\quad
 \phi_i=2n\arcsin(h\sqrt{\lambda_i}/2),\quad
 \tau_i=T\sqrt{\lambda_i},
\]
\[
 \mu_{h,T}=\sum_{i=1}^d
 \frac{h^4\lambda_i^2\sin^2\phi_i}{32(1-h^2\lambda_i/4)},
 \qquad b_{h,T}=\frac{h^4L^2(1+T\sqrt L)}8.
 \tag{4}
\]
Then
\[
 E_\rho R_{h,T}=\mu_{h,T},\qquad
 0\le\mu_{h,T}\le\frac{dh^4L^2}{24},\qquad
 \operatorname{Var}_\rho(R_{h,T})\le4d b_{h,T}^2.
 \tag{5}
\]
For any \(M_0\)-warm position law \(\nu\le M_0\pi\), independently
refreshed standard Gaussian momentum, and \(0<\delta<1\),
\[
 \Pr_{\nu\otimes N(0,I)}\left\{
 |R_{h,T}-\mu_{h,T}|>
 2b_{h,T}\sqrt{2ds}+2b_{h,T}s\right\}\le\delta,
 \quad s=\log(2M_0/\delta).
 \tag{6}
\]
Here \(\mu_{h,T}\) is the stationary mean, not necessarily the mean
under the warm law.

### Exact quadratic representation

Translate by \(x_*\) and diagonalize \(K\) orthogonally. Both integrators
and the Gaussian momentum respect this change of coordinates. For one
coordinate of precision \(\lambda\), use standardized variables
\(u=(y,p)^T=(\sqrt\lambda x,p)^T\). Under stationarity the \(2d\)
standardized variables are independent standard normals. Put
\(\eta=h\sqrt\lambda\), \(a=\eta^2/4\), \(r=\sqrt{1-a}\).
One leapfrog step is the matrix
\[
 C=\begin{pmatrix}1-\eta^2/2&\eta\\
 -\eta(1-\eta^2/4)&1-\eta^2/2\end{pmatrix}.
 \tag{7}
\]
For \(\theta=2\arcsin(\eta/2)\), one has
\(\cos\theta=1-\eta^2/2\) and \(\sin\theta=\eta r\).
Multiplication, using the angle addition identities, gives
\[
 C^n=\begin{pmatrix}\cos\phi&\sin\phi/r\\
 -r\sin\phi&\cos\phi\end{pmatrix},\qquad \phi=n\theta.
 \tag{8}
\]
This matrix preserves \(p^2+r^2y^2\). Since the physical energy is
\((y^2+p^2)/2\), its energy error is exactly
\[
 \Delta_{h,T}^{(\lambda)}=\frac a2(y_n^2-y^2).
 \tag{9}
\]
The exact flow rotates \(u\) by the angle \(\tau=T\sqrt\lambda\), so
\(y_T=y\cos\tau+p\sin\tau\). In these coordinates
\[
 A=\lambda(p^2/12-y^2/24).
\]
Exact conservation of \(p^2+y^2\) therefore gives
\[
 h^2(A(u)-A(\Phi_Tu))
 =\frac{h^2\lambda}{8}(y_T^2-y^2)=\frac a2(y_T^2-y^2).
 \tag{10}
\]
Subtracting (10) from (9) gives, without an asymptotic expansion,
\[
 R_{h,T}^{(\lambda)}=u^TE_\lambda u,\qquad
 E_\lambda=\frac a2(vv^T-ww^T),
 \tag{11}
\]
where column vectors \(v=(\cos\phi,\sin\phi/r)^T\) and
\(w=(\cos\tau,\sin\tau)^T\) are used. Thus
\[
 \operatorname{tr}E_\lambda
 =\frac a2(\cos^2\phi+\sin^2\phi/r^2-1)
 =\frac{a^2\sin^2\phi}{2(1-a)}.
 \tag{12}
\]
Adding (12) proves the mean formula in (5). Since \(a\le1/4\), it also
proves the bound on \(\mu_{h,T}\).

### Dimension-uniform matrix bounds

For \(0\le\eta\le1\), differentiation and integration give
\[
 \begin{aligned}
 0\le2\arcsin(\eta/2)-\eta
 &=\int_0^\eta\left((1-t^2/4)^{-1/2}-1\right)dt\\
 &\le\int_0^\eta\frac{t^2}{8(3/4)^{3/2}}dt
 =\frac{\eta^3}{24(3/4)^{3/2}}\le\frac{\eta^3}{12}.
 \end{aligned}
 \tag{13}
\]
The integrand inequality follows from the mean value theorem applied to
\((1-u)^{-1/2}\) on \([0,1/4]\). Therefore
\[
 |\phi-\tau|\le\frac{Th^2\lambda^{3/2}}{12}.
 \tag{14}
\]
Also \(1/r-1=a/[r(1+r)]\le a\), because
\(r\ge\sqrt3/2\). The distance between two unit vectors on the circle
is at most their angle difference, so
\[
 |v-w|\le a+|\phi-\tau|,\qquad |v|+|w|\le1/r+1\le5/2.
\]
Using
\(vv^T-ww^T=(v-w)v^T+w(v-w)^T\), one obtains
\[
 \begin{aligned}
 \|E_\lambda\|_{\rm op}
 &\le\frac{5a}{4}(a+|\phi-\tau|)\\
 &\le h^4\lambda^2\left(\frac5{64}
                         +\frac{5T\sqrt\lambda}{192}\right)
 \le b_{h,T}.
 \end{aligned}
 \tag{15}
\]
Let \(E\) be the block diagonal matrix with these \(d\) blocks. Then
\[
 \|E\|_{\rm op}\le b_{h,T},\qquad
 \|E\|_F^2\le2d b_{h,T}^2.
 \tag{16}
\]
For a standard Gaussian vector \(U\), Wick's fourth-moment formula gives
\(\operatorname{Var}(U^TEU)=2\|E\|_F^2\), proving the variance bound.

### Quadratic-form concentration and warmth

For completeness, diagonalize an arbitrary real symmetric matrix \(E\)
with eigenvalues \(e_j\), and let \(Z_j\) be independent standard normals.
Writing \(F=\|E\|_F\), \(b=\|E\|_{\rm op}\), direct Gaussian integration
and the logarithm series give, for \(2|t|b<1\),
\[
 \begin{aligned}
 \log E\exp\{t(U^TEU-\operatorname{tr}E)\}
 &=\sum_j\left[-te_j-\tfrac12\log(1-2te_j)\right]\\
 &\le\frac{t^2F^2}{1-2|t|b}.
 \end{aligned}
 \tag{17}
\]
Indeed each logarithm series after its linear term is bounded above by
\(t^2e_j^2\sum_{k\ge0}(2|t|b)^k\). For \(s>0\), choose
\(t=\sqrt s/(F+2b\sqrt s)\); substituting into Chernoff's bound at
\(2F\sqrt s+2bs\) gives exponent \(-s\). Use also \(-t\), obtaining
\[
 \Pr_\rho\{|R-\mu|>2F\sqrt s+2bs\}\le2e^{-s}.
 \tag{18}
\]
If \(F=0\), the remainder is identically zero and the assertion is
immediate. Combining (16) and (18), and bounding the warm phase-space
density by \(M_0\rho\), proves (6).

## 3. The nonvanishing remainder at the critical scale

Fix \(T>0\) with \(\sin T\ne0\). Consider standard Gaussian targets in
dimensions \(d_k\), with \(h_k=T/n_k\to0\) and
\(d_kh_k^4\to\ell^4\in(0,\infty)\). Then
\[
 R_{h_k,T}\longrightarrow\frac{\ell^4\sin^2T}{32}
 \quad\hbox{in }L^2(\rho_{d_k}).
 \tag{19}
\]
In fact (13) implies \(\phi_k\to T\), and (4) implies
\(\mu_{h_k,T}\to\ell^4\sin^2T/32\). Meanwhile (5) gives
\(\operatorname{Var}(R_{h_k,T})=O(d_kh_k^8)\to0\).
These two facts prove (19).

The same convergence holds in probability under any sequence of warm
position starts with \(\log M_{0,k}=o(d_k)\) and fresh Gaussian momentum.
For each fixed \(\delta>0\), the right side in (6) tends to zero:
\[
 h_k^4\sqrt{d_ks_k}
 =(d_kh_k^4)\sqrt{s_k/d_k}\to0,\qquad
 h_k^4s_k=(d_kh_k^4)s_k/d_k\to0.
\]
First take \(k\to\infty\) and then let \(\delta\downarrow0\).

Thus a general claim that the uncentered remainder in (1) is \(o(1)\)
at the critical step size would already fail when the Hessian is constant.
This does not imply poor acceptance. It identifies the necessary drift
scale \(dh^4\), alongside the centered Gaussian remainder scale
\(h^4\sqrt d\). At \(T\in\pi\mathbb Z\) the limit in (19) is zero;
the restriction on \(T\) is essential for a positive limit.

## 4. Scope

Equation (2) holds throughout the class in T305, and identifies the mean
remainder with the relative entropy of the numerical endpoint law. The
finite-step bounds (4)–(6) and the limit (19) are proved only for Gaussian
targets. They neither bound that entropy for nonquadratic potentials nor
control their centered remainders. The desired uniform operator-norm
theorem, proposal overlap, and a mixing argument remain open here.

The earlier leading-coefficient concentration remains valid. It bounds an
observable evaluated at two exactly stationary endpoints. Equations
(2) and (19) explain why this alone cannot account for the finite-step
energy error: the numerical endpoint law contributes a positive mean.
