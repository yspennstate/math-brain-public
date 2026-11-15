# The flat equal-mass semidiscrete-to-smoothing reduction

Let \(Q=[0,1]^2\), let \(T=\mathbb R^2/\mathbb Z^2\), and let \(\Omega\) be either space. Distances on \(Q\) are Euclidean, and distances on \(T\) are quotient distances. Write \(dx\) for uniform probability measure. Use the Neumann heat operator on \(Q\) and the periodic heat operator on \(T\), with convention \(P_t=\exp(t\Delta)\).

Let \(Y_1,\ldots,Y_n\) be independent uniform points and set

\[
\nu_n=\frac1n\sum_{i=1}^n\delta_{Y_i},\qquad
q_t\,dx=P_t\nu_n,\qquad
-\Delta f_t=q_t-1,\qquad \int_\Omega f_t\,dx=0.
\]

Put \(E_t=\int_\Omega|\nabla f_t|^2dx\) and

\[
F_\Omega(t)=\sum_{j>0}\frac{e^{-t\lambda_j}}{\lambda_j},
\]

where \(\lambda_j\) are the positive eigenvalues of the relevant Laplacian, counted with multiplicity.

**Theorem.** There are constants \(C_0,C_1\) such that, for \(n\ge2\), \(0<t\le1/2\), and \(nt\ge C_0\log(en)\),

\[
\begin{split}
n\,\mathbb E\big|W_{2,\Omega}^2(dx,\nu_n)
&-W_{2,\Omega}^2(q_tdx,\nu_n)-2\nu_n(f_t)+E_t\big|\\
&\le C_1\sqrt{\frac{\log(en)^3}{nt}}.
\end{split}
\tag{1}
\]

Consequently,

\[
n\,\mathbb E\left[W_{2,\Omega}^2(dx,\nu_n)
-W_{2,\Omega}^2(P_t\nu_n,\nu_n)\right]
=2F_\Omega(t)-F_\Omega(2t)
+O\!\left(\sqrt{\frac{\log(en)^3}{nt}}\right).
\tag{2}
\]

This is an independent derivation of the flat equal-mass case of Proposition 3.1 in Yunzong Xu, *Random matching between distinct distributions in two dimensions*, [arXiv:2610.40509v1](https://arxiv.org/html/2610.40509v1#S3.SS2). It uses a Jacobian map rather than the flow in that paper's Appendix B.1. No matching asymptotic theorem is assumed. The proof does not determine a finite next-order matching constant.

## 1. An action estimate

For a zero-mean function \(h\), let

\[
\|h\|_{-1}^2=\sum_{j>0}\frac{|\langle h,\psi_j\rangle|^2}{\lambda_j}.
\]

Here \(\psi_j\) is a real orthonormal eigenbasis in \(L^2(dx)\). Equivalently, this is \(\int|\nabla u|^2dx\) for \(-\Delta u=h\), with zero mean and Neumann boundary condition when appropriate. It is also the squared dual norm against functions whose Dirichlet energy is at most one. If \(h=\operatorname{div}R\) and \(R\) has zero normal flux, integration by parts therefore gives

\[
\|h\|_{-1}\le\|R\|_2.
\tag{3}
\]

If \(a,b\) are nonnegative probability densities and \(b\ge b_0>0\), then

\[
W_2^2(a\,dx,b\,dx)\le4b_0^{-1}\|a-b\|_{-1}^2.
\tag{4}
\]

Indeed, solve \(-\Delta u=a-b\). For \(0\le s<1\), put \(\theta(s)=1-(1-s)^2\), \(\rho_s=b+\theta(s)(a-b)\), and \(J_s=\theta'(s)\nabla u\). Then \(\partial_s\rho_s+\operatorname{div}J_s=0\), the flux is tangent to the boundary, and \(\rho_s\ge b_0(1-s)^2\). The action is bounded by

\[
\int_0^1\int\frac{|J_s|^2}{\rho_s}\,dx\,ds
\le b_0^{-1}\int_0^1\frac{\theta'(s)^2}{1-\theta(s)}\,ds
\int|\nabla u|^2dx
=4b_0^{-1}\|a-b\|_{-1}^2.
\]

The dynamic action upper bound for squared transport distance proves (4). Smooth approximation proves it for all density endpoints of finite indicated energy. All applications below have smooth densities, so no singular endpoint is needed in (4).

## 2. A deterministic change of source

Let \(f\) be smooth, with mean zero, periodic on \(T\), or with zero normal derivative on each face of \(Q\). Define

\[
v=\nabla f,\quad H=D^2f,\quad
\gamma=\sup_x\|H(x)\|_{\mathrm{op}}\le1/8,\quad
q=1-\Delta f,\quad E=\int|v|^2dx.
\]

For any probability measure \(\nu\), including atomic measures, write

\[
L=W_2^2(dx,\nu),\qquad D=W_2^2(qdx,\nu).
\]

We prove

\[
|L-D-2\nu(f)+E|\le C\gamma(L+E).
\tag{5}
\]

The constant is uniform in \(f\) and \(\nu\) subject to the stated assumptions.

### The Jacobian density and its discrepancy

Set \(S(x)=x-v(x)\). On the torus this means the induced map modulo \(\mathbb Z^2\). Its Jacobian determinant is

\[
\widehat q=\det(I-H)=1-\Delta f+\det H=q+\det H.
\tag{6}
\]

Since every eigenvalue of \(H\) lies in \([-\gamma,\gamma]\),

\[
q\ge1-2\gamma\ge3/4,\qquad
(1-\gamma)^2\le\widehat q\le(1+\gamma)^2.
\tag{7}
\]

The map is a diffeomorphism of the relevant space. For \(T\), lift \(f\) periodically to \(\mathbb R^2\). The function \(|x|^2/2-f(x)-y\cdot x\) is strictly convex and coercive for every \(y\), and hence has one minimizer, satisfying \(S(x)=y\). The positive definite derivative \(I-H\) gives a smooth inverse. The identity \(S(x+k)=S(x)+k\) then gives a diffeomorphism on the quotient.

For \(Q\), the Neumann condition and \(|f_{11}|\le\gamma\) imply

\[
|f_1(x)|\le\gamma\min(x_1,1-x_1),
\]

and the corresponding estimate holds for \(f_2\). Thus \(S(Q)\subset Q\), with each face preserved. If \(y\) is in the interior of \(Q\), minimize the strictly convex function \(|x|^2/2-f(x)-y\cdot x\) on \(Q\). At a lower coordinate face its derivative in the inward direction is \(-y_i<0\); at an upper face the derivative in the inward direction is \(-(1-y_i)<0\). A minimizer is therefore interior and satisfies \(S(x)=y\). Strict convexity gives injectivity. Compactness covers the target boundary by limits. The positive derivative gives the inverse up to each face. This proves the assertion for \(Q\), including corners.

Change of variables now gives

\[
S_\#(\widehat q\,dx)=dx,\qquad \int\widehat q\,dx=1.
\tag{8}
\]

In two dimensions define

\[
R=\frac12(\operatorname{cof}H)v.
\]

The rows of the symmetric matrix

\[
\operatorname{cof}H=
\begin{pmatrix}f_{22}&-f_{12}\\-f_{12}&f_{11}\end{pmatrix}
\]

have zero divergence, by equality of third derivatives. Direct differentiation gives

\[
\operatorname{div}R=\det H,\qquad |R|\le\frac\gamma2|v|.
\tag{9}
\]

The norm bound uses that the two eigenvalues of the cofactor matrix are the two eigenvalues of \(H\) in reverse order. At a vertical square face, \(f_1=f_{12}=0\): the second equality follows by tangential differentiation of the first. Consequently \(R_1=0\) there. The horizontal faces give \(R_2=0\). Thus \(R\) has zero normal flux on every face. On \(T\) it is periodic. Equations (3), (6), and (9) give

\[
\|\widehat q-q\|_{-1}\le\frac\gamma2\sqrt E,
\qquad
w:=W_2(\widehat qdx,qdx)\le C\gamma\sqrt E.
\tag{10}
\]

For the second inequality apply (4) with base density \(q\), using (7).

### The pointwise cost comparison, including the torus cut locus

Taylor's formula along a segment gives, for \(h=y-x\) in \(Q\),

\[
\left|f(y)-f(x)-v(x)\cdot h\right|\le\frac\gamma2|h|^2.
\]

Expanding \(|h+v(x)|^2\) therefore proves

\[
\begin{split}
(1-\gamma)d(x,y)^2+2(f(y)-f(x))+|v(x)|^2
&\le d(Sx,y)^2\\
&\le(1+\gamma)d(x,y)^2+2(f(y)-f(x))+|v(x)|^2.
\end{split}
\tag{11}
\]

For \(T\), choose arbitrary lifts of \(x,y\). Apply the same Taylor bound on \(\mathbb R^2\) to every \(h=y-x+k\), \(k\in\mathbb Z^2\). Periodicity makes \(f(y)-f(x)\) independent of \(k\). Both bounds are consequently valid before minimizing over \(k\). Since \(1\pm\gamma>0\), minimizing their terms \((1\pm\gamma)|h|^2\) gives (11) with the torus distances. This does not require a unique shortest lift or a small displacement.

### Taking infima and correcting the density

The map \((x,y)\mapsto(Sx,y)\) is a bijection between couplings of \((\widehat qdx,\nu)\) and couplings of \((dx,\nu)\). Write \(\widehat D=W_2^2(\widehat qdx,\nu)\). The integral of the separated term in (11) is the same for every such coupling:

\[
A_f=2\nu(f)-2\int f\widehat q\,dx+\int|v|^2\widehat q\,dx.
\]

Taking infima in (11) gives

\[
|L-\widehat D-A_f|\le\gamma\widehat D.
\tag{12}
\]

Integration by parts, using (6) and (9), gives

\[
\int f\widehat q\,dx
=\int f(1-\Delta f)\,dx+\int f\operatorname{div}R\,dx
=E-\int v\cdot R\,dx
=E+O(\gamma E).
\]

Also \(\widehat q=1+O(\gamma)\) pointwise by (7), so \(\int|v|^2\widehat q\,dx=E+O(\gamma E)\). It follows that

\[
A_f=2\nu(f)-E+O(\gamma E).
\tag{13}
\]

The triangle inequality gives \(|\sqrt{\widehat D}-\sqrt D|\le w\), hence

\[
|\widehat D-D|\le2w\sqrt D+w^2
\le C\gamma(D+E),\qquad \widehat D\le C(D+E).
\tag{14}
\]

To justify the first bound directly, use \(\sqrt{\widehat D}\le\sqrt D+w\) for one sign, and \(\sqrt{\widehat D}\ge\max(0,\sqrt D-w)\) for the other sign. Then apply (10), \(2\sqrt{DE}\le D+E\), and \(\gamma\le1\).

Finally (4), with base density 1 and \(q-1=-\Delta f\), gives \(W_2^2(qdx,dx)\le4E\). Therefore

\[
D\le2L+8E.
\tag{15}
\]

Combining (12)–(15) proves (5). No regularity of the target \(\nu\) has been used.

## 3. Explicit heat-potential estimates

On \(Q\) an orthonormal basis is

\[
\psi_{k,l}(x)=c_kc_l\cos(\pi kx_1)\cos(\pi lx_2),\qquad
c_0=1,\quad c_j=\sqrt2\ (j>0),
\]

with eigenvalues \(\pi^2(k^2+l^2)\), \(k,l\ge0\). On \(T\), Fourier modes have eigenvalues \(4\pi^2|k|^2\), \(k\in\mathbb Z^2\). Zero modes are excluded below. Define

\[
G_t(x,y)=\sum_{j>0}\frac{e^{-t\lambda_j}}{\lambda_j}\psi_j(x)\psi_j(y).
\tag{16}
\]

The corresponding real Fourier basis, or the complex Fourier basis with conjugates in the kernel, gives the same estimates. For \(t>0\) all series and their derivatives converge absolutely. Moreover

\[
f_t(x)=\frac1n\sum_i G_t(x,Y_i),\qquad
\int G_t(x,y)\,dy=0.
\tag{17}
\]

In each of the two spectra there are at most \(C r\) modes with integer frequency maximum \(r\ge1\), with \(c r^2\le\lambda\le C r^2\). Derivatives of order \(a\) of a basis function have supremum at most \(C_a r^a\). Thus

\[
\|G_t\|_\infty+F_\Omega(t)\le C\sum_{r\ge1}\frac{e^{-ct r^2}}r
\le C\log(e/t),\qquad 0<t\le1.
\tag{18}
\]

For the last step, split at \(r=t^{-1/2}\). The lower part is a harmonic sum. For the upper part, compare with \(\int_{t^{-1/2}}^\infty e^{-ct u^2}du/u\) and a bounded first term. The substituted integral has a fixed positive lower endpoint and is bounded uniformly in \(t\).

Similarly, summing \(r e^{-ct r^2}\) and \(r^2e^{-ct r^2}\), respectively, gives

\[
\|D_x^2G_t\|_\infty\le C/t,\qquad
\|D_x^3G_t\|_\infty\le Ct^{-3/2}.
\tag{19}
\]

These Gaussian sum bounds follow by comparison with their integrals after scaling \(u\mapsto\sqrt t\,u\). For any Hessian component, orthogonality in the \(y\) variable gives

\[
\begin{split}
\sup_x\int|\partial_{ab,x}G_t(x,y)|^2dy
&=\sup_x\sum_{j>0}\frac{e^{-2t\lambda_j}}{\lambda_j^2}
|\partial_{ab}\psi_j(x)|^2\\
&\le C\sum_{r\ge1}r e^{-ct r^2}\le C/t.
\end{split}
\tag{20}
\]

This argument proves the variance estimate directly; it does not square an absolute kernel envelope. The derivatives in (19) and (20) are ordinary derivatives up to square faces. Each cosine mode has zero normal derivative there, so \(f_t\) satisfies the boundary conditions of Section 2 exactly.

## 4. Hessian concentration

Write \(\ell_n=\log(en)\). Fix a large constant \(K\) and put

\[
\delta=K\sqrt{\frac{\ell_n}{nt}}.
\tag{21}
\]

After choosing \(K\), choose \(C_0\) in the theorem large enough that \(\delta\le1/8\). For fixed \(x\) and component \(a,b\), the variables \(\partial_{ab,x}G_t(x,Y_i)\) are independent and centered. Equations (19) and (20) bound their absolute value and variance by \(C/t\). Bernstein's inequality therefore gives

\[
\mathbb P\bigl(|\partial_{ab}f_t(x)|>u\bigr)
\le2\exp(-cntu^2),\qquad 0<u\le1.
\tag{22}
\]

Indeed, the usual denominator \(C/t+(C/t)u\) is at most \(C'/t\) in this range. Constants in (22) can absorb any fixed fraction of \(u\).

The third-derivative bound in (19), averaged as in (17), makes each Hessian component deterministically \(Ct^{-3/2}\)-Lipschitz. Take a net with spacing \(c\delta t^{3/2}\), using at most \(C\delta^{-2}t^{-3}\) points, including near the boundary. If all Hessian components on the net have absolute value at most \(\delta/4\), then, for sufficiently small fixed \(c\), they have absolute value at most \(\delta/2\) everywhere. The operator norm of a two by two matrix is at most twice its largest entry. A union bound consequently gives

\[
\mathbb P(\|D^2f_t\|_{\mathrm{op},\infty}>\delta)
\le C\delta^{-2}t^{-3}\exp(-cnt\delta^2).
\tag{23}
\]

Here \(nt\ge C_0\ell_n\) implies \(t\ge1/n\). Substitution of (21) bounds the prefactor by

\[
\delta^{-2}t^{-3}=\frac{n}{K^2\ell_n t^2}\le Cn^3.
\]

Taking \(K\) sufficiently large in (23) proves, uniformly in the theorem's time range,

\[
\mathbb P(\mathcal A^c)\le Cn^{-12},\qquad
\mathcal A=\{\|D^2f_t\|_{\mathrm{op},\infty}\le\delta\}.
\tag{24}
\]

## 5. Rough cost and exact spectral moments

Let \(a_j=\nu_n(\psi_j)\), with \(j>0\). Independence, zero mean, and \(L^2\) normalization give

\[
\mathbb E a_j^2=\frac1n.
\tag{25}
\]

The heat and Poisson expansions give the pathwise identities

\[
\nu_n(f_t)=\sum_{j>0}\frac{e^{-t\lambda_j}}{\lambda_j}a_j^2,
\qquad
E_t=\sum_{j>0}\frac{e^{-2t\lambda_j}}{\lambda_j}a_j^2.
\]

For the first identity, the series for \(f_t\) converges absolutely and uniformly, allowing evaluation at the sampled points even though it depends on those same points. The second is the Dirichlet energy identity. Taking expectations of these nonnegative series gives exactly

\[
n\mathbb E\nu_n(f_t)=F_\Omega(t),\qquad
n\mathbb E E_t=F_\Omega(2t).
\tag{26}
\]

These are unconditional identities; no restriction to \(\mathcal A\) is made.

We also need a rough cost estimate independent of the reduction. Set \(s=1/n\). Reflected or periodic Gaussian motion at heat time \(s\) couples each site to its smoothing at squared cost at most \(4s\). For the square, fold each coordinate of \(y+Z\) into \([0,1]\), with \(Z\) centered Gaussian of covariance \(2s I\). The folding map is 1-Lipschitz and fixes \(y\), so displacement squared is at most \(|Z|^2\). On the torus take the quotient instead. The expectation of \(|Z|^2\) is \(4s\) in both cases. Hence

\[
W_2^2(\nu_n,P_s\nu_n)\le4s.
\]

By (4), with base density 1,

\[
W_2^2(P_s\nu_n,dx)\le4\|q_s-1\|_{-1}^2.
\]

The triangle inequality, (25), and (18) therefore give

\[
\begin{split}
n\mathbb E L_n
&\le8ns+8n\mathbb E\|q_s-1\|_{-1}^2\\
&=8+8F_\Omega(2/n)\le C\ell_n,
\qquad L_n=W_2^2(dx,\nu_n).
\end{split}
\tag{27}
\]

Because \(t\ge1/n\), equations (18) and (26) also give \(n\mathbb E E_t\le C\ell_n\). Neither bound assumes the leading matching asymptotic.

## 6. The expected remainder

Let \(D_{n,t}=W_2^2(q_tdx,\nu_n)\) and

\[
\mathcal R_{n,t}=L_n-D_{n,t}-2\nu_n(f_t)+E_t.
\]

On \(\mathcal A\), (5) applies and gives \(|\mathcal R_{n,t}|\le C\delta(L_n+E_t)\). Using (27) and (26), with nonnegative upper bounds before any event restriction, yields

\[
n\mathbb E[|\mathcal R_{n,t}|1_{\mathcal A}]
\le C\delta\ell_n
=C\sqrt{\frac{\ell_n^3}{nt}}.
\tag{28}
\]

It remains to control the exceptional event. Both transport costs are bounded by the squared diameter. Equations (17) and (18) give \(\|f_t\|_\infty\le C\log(e/t)\le C\ell_n\). Moreover, since \(q_t\) is a probability density,

\[
E_t=\int f_t(q_t-1)\,dx\le2\|f_t\|_\infty.
\]

Thus \(|\mathcal R_{n,t}|\le C\ell_n\) deterministically. By (24),

\[
n\mathbb E[|\mathcal R_{n,t}|1_{\mathcal A^c}]
\le Cn^{-11}\ell_n
\le C\sqrt{\frac{\ell_n^3}{nt}}.
\tag{29}
\]

For the last inequality it suffices to use \(t\le1/2\), \(n\ge2\), and \(\ell_n\ge1\). Equations (28) and (29) prove (1). Taking expectations and using (26) proves (2), including the sign and coefficient of each spectral term.

## 7. Consequences and checks

At the subdivision time \(t=n^{-5/6}\), the error in (2) is

\[
O\bigl(n^{-1/12}\log(en)^{3/2}\bigr)=o(1).
\tag{30}
\]

The exponent follows both from \((nt)^{-1/2}=n^{-1/12}\) and from the good-event product \(\delta\ell_n=K n^{-1/12}\ell_n^{3/2}\).

The spectral definition of \(h_\Omega\) in round 3 implies, without any random-matching conclusion,

\[
2F_\Omega(t)-F_\Omega(2t)
=\frac{\log(2/t)}{4\pi}+h_\Omega+o(1).
\]

In particular, the \(\log2\) contribution has a plus sign. This also follows by differentiating: \(F'=-K_\Omega\), so the derivative of the spectral combination is \(-2K_\Omega(t)+2K_\Omega(2t)\), with leading term \(-1/(4\pi t)\). The exact moment calculation (26) is the primary normalization check; a finite orthogonal toy calculation in the supplied script tests it independently by exhaustive sample enumeration.

The determinant discrepancy can be checked in a second way. The two by two identity \(\operatorname{cof}H=(\operatorname{tr}H)I-H\) gives

\[
2R=(\Delta f)\nabla f-\nabla(|\nabla f|^2/2).
\]

Taking its divergence cancels the third derivatives and gives \(((\Delta f)^2-\operatorname{tr}(H^2))/2=\det H\). This confirms both the sign and the factor \(1/2\) in (9). For a mean-zero Neumann polynomial, the script checks this identity, zero boundary flux, total Jacobian mass, and both integration-by-parts terms by exact rational polynomial arithmetic.

The result verifies the reduction needed by round 4, including its quantitative error. Existence of the constant in the smoothing cost still requires the separate sample-size/time comparison and convergence argument. Those steps, and the evaluation of the universal equal-mass constant, are not proved here.
