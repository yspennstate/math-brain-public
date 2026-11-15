# An explicit small-target basin and a finite-step-size probability bound

Consider the fully trainable two-layer linear network

\[
f_{a,W}(x)=a^TWx,\qquad L_b(a,W)=\tfrac12\|W^Ta-b\|^2,
\]

where \(a\in\mathbb R^m\), \(W\in\mathbb R^{m\times d}\), \(d\geq1\) and \(m\geq d+1\). This is the population square loss for isotropic Gaussian inputs and labels \(b^Tx\). It is also the full-batch square loss on \(x_j=\sqrt d\,e_j\), with labels \(\sqrt d\,b_j\), averaged over \(j\). Both layers are updated simultaneously with step \(\eta>0\).

Put

\[
A=\sqrt\eta\,a,\quad U=\sqrt\eta\,W,\quad y=\eta b,
\quad v=U^TA,\quad r=v-y.
\]

The scaled update is

\[
A^+=A-Ur,\qquad U^+=U-Ar^T. \tag{1}
\]

Write

\[
Z=[A\ U],\quad G=Z^TZ,\quad q=\|A\|^2,\quad C=U^TU,
\quad c=\lambda_{\max}(C),\quad H=C+qI_d.
\]

All parameter norms below are Euclidean, equivalently Frobenius norms of \(Z\).

## 1. Deterministic theorem

Fix \(0<\delta\leq1/4\), and suppose

\[
q_0+c_0\leq2-4\delta,\qquad c_0\leq1-2\delta,
\qquad D:=\det G_0>0. \tag{2}
\]

Define the explicit constants

\[
M=d+2,\qquad \rho=(1-\delta)^2,\qquad
\chi=\exp\!\left(-\frac4{\delta(2-\delta)}\right),
\qquad \mu=\frac{\chi D}{M^d},\qquad \kappa=\delta\mu. \tag{3}
\]

If

\[
\boxed{\quad \|y\|\leq\frac{\delta^2\chi}{8M^d}\det G_0
=\frac{\delta\kappa}{8},\quad} \tag{4}
\]

then (1) converges to a full-column-rank global minimizer. More precisely,

\[
\begin{split}
\|r_t\|&\leq(1-\kappa)^t\|r_0\|,\\
G_t&\succeq\mu I_{d+1},\\
2\mu\leq\lambda_{\min}(H_\infty)
&\leq\lambda_{\max}(H_\infty)
\leq2-\tfrac72\delta,\\
\|Z_t-Z_\infty\|_F
&\leq\frac{\sqrt M\,\|r_0\|}{\kappa}(1-\kappa)^t.
\end{split} \tag{5}
\]

In original coordinates the endpoint sharpness therefore satisfies

\[
\eta\lambda_{\max}(\nabla^2L_b(a_\infty,W_\infty))
\leq2-\tfrac72\delta. \tag{6}
\]

The constants are conservative. The result gives an explicit target threshold rather than an initialization-dependent existence assertion.

### Exact identities

Set \(\beta=\|y\|\). Expanding (1), using \(U^TA=v=r+y\), gives

\[
\begin{split}
q^+&=q-r^T(2I-C)r-2y^Tr,\\
C^+&=C-(2-q)rr^T-ry^T-yr^T,\\
r^+&=[I-H+(v^Tr)I]r. 
\end{split} \tag{7}
\]

For the last identity,

\[
(U^T-rA^T)(A-Ur)-y
=v-Cr-qr+r(A^TUr)-y,
\]

and \(A^TUr=v^Tr\). Define

\[
K(r)=\begin{pmatrix}0&r^T\\r&0\end{pmatrix}.
\]

Then \(Z^+=Z(I-K(r))\). The nonzero eigenvalues of \(K(r)\) are \(\|r\|\) and \(-\|r\|\), with the evident interpretation at \(r=0\). Thus

\[
\det G^+=\det G\,(1-\|r\|^2)^2. \tag{8}
\]

### Preliminary bounds on the constants

Since \(G_0\) is positive definite, so is \(C_0\). Its block determinant is

\[
D=\det C_0\,(q_0-v_0^TC_0^{-1}v_0)
\leq q_0\det C_0<2,
\]

because \(c_0<1\) and \(q_0<2\). Also
\(\delta(2-\delta)\leq7/16\), so \(\chi\leq e^{-64/7}<1/4\).
Consequently

\[
0<\mu<1/2,\qquad0<\kappa<\delta/2<1,
\qquad\beta\leq\delta\kappa/8<\delta/2. \tag{9}
\]

### Bootstrap

Let

\[
B_t=2\beta\sum_{j<t}\|r_j\|.
\]

We prove by induction, for every finite \(t\),

\[
\begin{gathered}
B_t\leq\delta/4,\qquad
q_t\leq q_0+B_t,\qquad C_t\preceq C_0+B_tI,\\
\det G_t\geq\chi D,\qquad
\|r_j\|\leq(1-\kappa)^j\|r_0\|\quad(0\leq j\leq t).
\end{gathered} \tag{10}
\]

At time zero these statements hold. In the induction step it suffices initially to use the weaker bound \(B_t\leq\delta/2\). Equations (2) and (10) imply

\[
c_t\leq1-\delta,\qquad
q_t+c_t\leq2-3\delta,\qquad q_t<2,
\qquad\operatorname{tr}G_t=q_t+\operatorname{tr}C_t<M. \tag{11}
\]

If the eigenvalues of \(G_t\) are positive and have sum less than \(M\), then

\[
\det G_t\leq\lambda_{\min}(G_t)M^d.
\]

Thus the determinant bound in (10) gives \(G_t\succeq\mu I\). Principal submatrices give \(q_t\geq\mu\), \(C_t\succeq\mu I\), and

\[
\lambda_{\min}(H_t)\geq2\mu. \tag{12}
\]

For clarity, positivity is automatic at the base step and follows from the strictly positive determinant bound at each later step, since every \(G_t\) is a Gram matrix.

By Cauchy--Schwarz and the arithmetic-geometric mean inequality,

\[
\|v_t\|^2\leq q_tc_t,
\qquad\|v_t\|\leq(q_t+c_t)/2\leq1-3\delta/2<1.
\]

In particular \(\|r_t\|\leq1-\delta\) by (9), so \(\|r_t\|^2\leq\rho<1\). Put \(a_t=\lambda_{\min}(H_t)\) and \(\omega_t=v_t^Tr_t\). Since \(r_t=v_t-y\),

\[
-\beta\leq\omega_t\leq q_tc_t+\beta
\leq(1-\delta)a_t+\beta. \tag{13}
\]

The last inequality uses \(q_t\leq a_t\) and \(c_t\leq1-\delta\). Every eigenvalue of the symmetric residual multiplier in (7) is at most

\[
1-a_t+\omega_t
\leq1-\delta a_t+\beta
\leq1-2\delta\mu+\beta\leq1-\kappa.
\]

It is at least

\[
1-(q_t+c_t)+\omega_t
\geq-1+3\delta-\beta\geq-1+2\delta\geq-1+\kappa.
\]

Here \(\beta\leq\kappa\) and \(\beta\leq\delta\) follow from (9). Therefore

\[
\|r_{t+1}\|\leq(1-\kappa)\|r_t\|. \tag{14}
\]

Initially \(\|r_0\|\leq1-2\delta+\beta<1\). The geometric bounds now proved through the current step give

\[
\sum_{j=0}^t\|r_j\|\leq\frac{\|r_0\|}{\kappa}<\frac1\kappa,
\qquad B_{t+1}\leq\frac{2\beta}{\kappa}\leq\delta/4. \tag{15}
\]

In (7), \(2I-C_t\succeq(1+\delta)I\) and \(2-q_t>0\). Also
\(\|r_ty^T+yr_t^T\|\leq2\beta\|r_t\|\).
Summing the first two identities of (7) yields

\[
\begin{split}
q_{t+1}&\leq q_0+B_{t+1}-(1+\delta)
\sum_{j=0}^t\|r_j\|^2,\\
C_{t+1}&\preceq C_0+B_{t+1}I.
\end{split} \tag{16}
\]

Since \(q_{t+1}\geq0\), this also proves

\[
\sum_{j=0}^t\|r_j\|^2
\leq\frac{q_0+B_{t+1}}{1+\delta}<2. \tag{17}
\]

For \(0\leq x\leq\rho\), integration gives
\(\log(1-x)\geq-x/(1-\rho)\). Applying (8) and (17),

\[
\det G_{t+1}
=D\prod_{j=0}^t(1-\|r_j\|^2)^2
\geq D\exp\!\left[-\frac2{1-\rho}
\sum_{j=0}^t\|r_j\|^2\right]
\geq\chi D. \tag{18}
\]

This proves every induction assertion at time \(t+1\). The proof uses no convergence assumption and no interchange of a pointwise target threshold with a probability limit.

### Convergence and endpoint sharpness

The exact parameter step satisfies

\[
\|Z_{t+1}-Z_t\|_F^2=r_t^TC_tr_t+q_t\|r_t\|^2
\leq M\|r_t\|^2. \tag{19}
\]

Equations (14) and (19) make the increments summable and give the tail bound in (5). The limit has residual zero and is a global minimizer. Passing to the limit in \(G_t\succeq\mu I\) proves full column rank. By (15)--(16),

\[
q_\infty+\lambda_{\max}(C_\infty)
\leq q_0+c_0+2B_\infty
\leq2-4\delta+\delta/2=2-7\delta/2.
\]

At zero residual the original parameter Hessian is \(J^TJ\), with
\(J(\alpha,V)=W^T\alpha+V^Ta\). Direct composition gives
\(JJ^T=W^TW+\|a\|^2I=\eta^{-1}H\). The positive eigenvalues of \(J^TJ\) and \(JJ^T\) agree, as follows by applying \(J\) or \(J^T\) to their positive-eigenvalue eigenvectors. This proves (5)--(6).

## 2. Gaussian probability bound at every positive step size

Let all entries of \(Z_0\) be independent \(N(0,\tau^2)\). Equivalently, all original parameters have variance \(\tau^2/\eta\). Put \(n=d+1\), and define the spectral event

\[
\mathcal B_\delta=\{q_0+c_0\leq2-4\delta,\ c_0\leq1-2\delta\}.
\]

Let \(F_\eta\) be failure to converge in parameter space to a full-column-rank global minimizer satisfying (6). For every
\(0<p<(m-d)/2\), define

\[
K_\delta=\frac{8(d+2)^d}{\delta^2\chi},\qquad
\mathcal M_p=(2\tau^2)^{-np}
\prod_{j=1}^n
\frac{\Gamma((m-j+1)/2-p)}{\Gamma((m-j+1)/2)}. \tag{20}
\]

Then, at every \(\eta>0\),

\[
\boxed{\quad
\mathbb P(F_\eta\cap\mathcal B_\delta)
\leq\mathcal M_p(K_\delta\eta\|b\|)^p,
\qquad
\mathbb P(F_\eta)
\leq\min\{1,\mathbb P(\mathcal B_\delta^c)
+\mathcal M_p(K_\delta\eta\|b\|)^p\}.
\quad} \tag{21}
\]

Any event requiring convergence to a global minimum with
\( |\eta\lambda_{\max}-2|\leq w\), for \(w<7\delta/2\), is contained in \(F_\eta\). Additional edge-residence conditions can only decrease its probability.

These events are measurable: convergence is a countable Cauchy condition on continuous finite iterates, and rank, loss and Hessian at the limit are measurable by continuity.

To prove (21), orthogonalize the \(n\) Gaussian columns of \(Z_0\) in order. The squared length of column \(j\) perpendicular to the span of its predecessors, divided by \(\tau^2\), has a chi-square law with \(\nu_j=m-j+1\) degrees of freedom. Conditional on all previous columns this law is constant: project an independent isotropic Gaussian onto the \(\nu_j\)-dimensional orthogonal complement and rotate an orthonormal basis. Therefore these squared lengths \(\tau^2X_j\) are independent. They are positive almost surely, and Gram-Schmidt gives

\[
D=\det G_0=\tau^{2n}\prod_{j=1}^nX_j. \tag{22}
\]

The chi-square density is
\(x^{\nu/2-1}e^{-x/2}/(2^{\nu/2}\Gamma(\nu/2))\) for \(x>0\), obtained by integrating the isotropic Gaussian density in polar coordinates. Integrating \(x^{-p}\) against it gives

\[
\mathbb E X_j^{-p}=2^{-p}
\frac{\Gamma(\nu_j/2-p)}{\Gamma(\nu_j/2)}
\quad\text{when }p<\nu_j/2.
\]

Thus \(\mathbb E D^{-p}=\mathcal M_p\). Outside \(\{D<K_\delta\eta\|b\|\}\), the deterministic theorem applies on \(\mathcal B_\delta\). Markov's inequality applied to \(D^{-p}\) proves (21). When \(b=0\), the failure event on \(\mathcal B_\delta\) is null directly, and (21) has zero perturbation term.

### An elementary bound for the spectral complement

For \(u>0\), put

\[
T_m(u)=\begin{cases}
\exp[-\frac m2(u-1-\log u)],&u>1,\\
1,&0<u\leq1.
\end{cases}
\]

If \(X\) is chi-square with \(m\) degrees of freedom, its Gaussian integral gives
\(\mathbb E e^{tX}=(1-2t)^{-m/2}\). Markov's inequality at
\(t=(1-1/u)/2\) proves \(\mathbb P(X>m u)\leq T_m(u)\) for \(u>1\); the remaining bound is trivial.

Let \(r_\delta=1-2\delta\). Since \(q_0,c_0\leq r_\delta\) imply \(\mathcal B_\delta\), for every \(0<\epsilon<1\),

\[
\mathbb P(\mathcal B_\delta^c)
\leq T_m\!\left(\frac{r_\delta}{m\tau^2}\right)
+(1+2/\epsilon)^d
T_m\!\left(\frac{(1-\epsilon)^2r_\delta}{m\tau^2}\right).
\tag{23}
\]

Here is a proof of the net factor. A maximal set of points on the unit sphere separated by more than \(\epsilon\) is an \(\epsilon\)-net. Disjoint balls of radius \(\epsilon/2\) around its points lie in the ball of radius \(1+\epsilon/2\), so volume comparison bounds its size by \((1+2/\epsilon)^d\). For any matrix \(U\), approximation by the net gives

\[
(1-\epsilon)\|U\|_{\rm op}\leq\max_{x\text{ in net}}\|Ux\|.
\]

For each fixed unit vector \(x\), the entries of \(U_0x\) are independent \(N(0,\tau^2)\). Apply the chi-square bound and a union bound. The first term of (23) bounds \(q_0>r_\delta\), proving the formula.

### Concrete specialization

Take \(m=16\), \(d=8\), \(\tau^2=1/288\), \(\delta=1/16\), and \(\epsilon=1/32\). Then

\[
\chi=e^{-1024/31},\qquad K_\delta=204{,}800{,}000{,}000\,e^{1024/31},
\qquad 2-7\delta/2=57/32.
\]

The coefficient in \(K_\delta\) is \(8\cdot10^8\cdot256\).
The admissible exponent \(p=3\) gives

\[
\mathcal M_3=
\frac{288^{27}}{\displaystyle\prod_{\nu=8}^{16}(\nu-2)(\nu-4)(\nu-6)}.
\tag{24}
\]

This follows either from (20) or three applications of \(\Gamma(z+1)=z\Gamma(z)\) in each factor. Equations (21), (23) and (24) give a fully explicit bound at finite \(\eta\), with a perturbation term proportional to \((\eta\|b\|)^3\).

For these choices, rational Taylor bounds on the exponential certify

\[
\mathbb P(\mathcal B_{1/16}^c)<9.568\times10^{-25},
\qquad \mathcal M_3K_{1/16}^3<1.127\times10^{120}.
\]

Consequently, for every fixed target \(b\),

\[
\boxed{\quad\eta\|b\|\leq10^{-48}
\quad\Longrightarrow\quad
\mathbb P(F_\eta)<2.1\times10^{-24}.\quad} \tag{25}
\]

The same bound applies to convergence to an endpoint in any relative sharpness window \( |\eta\lambda_{\max}-2|\leq w<7/32\). This numerical step-size range is a sufficient range, not an estimated transition scale.

For the numerical certification, if \(x>0\) is rational and \(N+2>x\), then

\[
\sum_{j=0}^N\frac{x^j}{j!}\leq e^x
\leq\sum_{j=0}^N\frac{x^j}{j!}
+\frac{x^{N+1}}{(N+1)!}\frac1{1-x/(N+2)}.
\]

The upper bound follows by bounding successive ratios in the remaining positive tail. With \(m/2=8\), each Chernoff term is exactly \(u^8e^{-8(u-1)}\), and the cubic coefficient is a rational number times \(e^{3072/31}\). Taking \(N=\lceil2x\rceil+120\) for each exponential and comparing rational numbers proves the displayed decimal upper bounds without floating-point exponentiation.

## 3. Scope and an initially supercritical example

Conditions (2) hold at \(\delta=1/16\) for the following full-rank example with \(m=16,d=8\):

\[
A_0=e_1,\qquad U_{0,1}=\tfrac45e_1+\tfrac1{10}e_2,
\qquad U_{0,j}=\tfrac1{10}e_{j+1}\quad(2\leq j\leq8).
\]

Indeed \(q_0=1\), \(c_0=13/20\), and \(q_0+c_0=33/20<7/4\), while \(c_0<7/8\). At zero target, the simultaneous parameter direction \(\dot A=e_1\), \(\dot U_{11}=1\), with other entries zero, has squared norm 2 and Hessian Rayleigh quotient

\[
\frac{(9/5)^2+2(4/5)}2=121/50>2.
\]

For nonzero scaled target \(y\), the same quotient is \(121/50-y_1\), so it remains above 2 for all targets allowed by (4). This follows either by differentiating the loss along that line or by the Hessian quadratic form \(\|J\dot Z\|^2+2\dot A^T\dot U r\). Strict inequalities persist on an open neighborhood. The theorem therefore does not require initial Hessian sharpness below \(2/\eta\).

The new result is an explicit nonzero-target threshold and its finite-\(\eta\) probability consequence on the region (2). It does not quantify the zero-target endpoint gap over the whole round-5 rectangle, classify the complementary starts, or prove sustained edge residence or nonmonotone loss. The coefficient in the probability bound is large, so the displayed sufficient step-size range can be very small. No novelty claim against the complete matrix-factorization literature is made.
