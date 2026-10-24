# Independent RF universality audit

**Status, 2026-10-24.** The spectral, generalized-invariance, independent-side-information, and ordinary-GD embedding steps in B03's finite-horizon route pass this audit. The clipping argument verifies the full WZF entrywise assumptions. The empirical rank-one overlaps can be frozen by the explicit stability argument below. The later addendum also verifies B01's cumulant formulas and state-covariance positive definiteness against Fan's primary equations, closing that fixed-horizon applicability issue without added algorithmic noise. Exact calibration and uniform time require the separate analytic and optimization results; no complete-original-problem or novelty claim is made here.

There is one normalization point to retain: WZF's padded singular-value law uses the **row dimension**. The feature-normalized law in B03 (8.9) has first moment \(rv\), but WZF's \(D\) satisfies \(\mathbb E D^2=v\).

## 1. Model and precise conclusion

Let \(p=d-1\), \(N/d\to\delta>0\), \(m/d\to\gamma>0\), and \(r_d=N/m\to r=\delta/\gamma\). Independently draw standard Gaussian matrices
\[
X\in\mathbb R^{N\times p},\qquad G\in\mathbb R^{m\times p},
\qquad E\in\mathbb R^{N\times m}.
\]
Set \(V=G/\sqrt d\), \(\phi=\tanh\), and
\[
A=\frac{\phi(XV^\top)}{\sqrt m},\qquad
A_{\mathrm G}=\frac{aXV^\top+\sqrt\nu E}{\sqrt m},
\quad a=\mathbb E[Z\phi(Z)]=\mathbb E\phi'(Z),
\quad v=\mathbb E\phi(Z)^2,\quad\nu=v-a^2>0.
\tag{1}
\]
The positivity follows because \(\tanh\) is not a linear function in Gaussian \(L^2\).

The matrix \(A\) satisfies WZF Proposition D.1(b2); its limiting diagonal distribution equals that of the bi-orthogonally invariant matrix \(A_{\mathrm G}\). This conclusion holds for an augmented matrix with any fixed positive proportional number of independent test rows. A deterministic training/test mask belongs to side information.

For almost-sure statements, construct the entire data-array sequence independently of the entire feature-array sequence, for example on the product of all per-dimension laws. This permits conditioning on the whole feature sequence. The final in-probability conclusions concern only the per-dimension distributions and do not depend on choosing this coupling.

## 2. Operator bounds and the complete concentration lemma

The standard Gaussian matrix norm bound gives deterministic \(C_X,C_G\) such that
\[
\mathbb P(\|X\|_{\rm op}>C_X\sqrt d)
+\mathbb P(\|G\|_{\rm op}>C_G\sqrt d)\le C e^{-cd}.
\tag{2}
\]
Here is also a direct bound for the nonlinear matrix. Conditional on \(V\), the rows \(h_i=\phi(Vx_i)\) are independent and centered because \(\phi\) is odd. For any unit vector \(b\), the function \(x\mapsto b^\top\phi(Vx)\) is \(\|V\|_{\rm op}\)-Lipschitz. Gaussian concentration and a product argument give a uniform sub-Gaussian bound for \(u^\top H b\) for unit \(u,b\), where \(H=\phi(XV^\top)\). Taking fixed \(1/4\)-nets of both spheres and choosing a sufficiently large threshold \(C\sqrt{N+m}\) yields
\[
\mathbb P(\|A\|_{\rm op}>C_A)\le C e^{-cd}.
\tag{3}
\]
All constants depend only on limiting dimension-ratio bounds. The Gaussian surrogate has the same type of bound by the triangle and product inequalities.

Let \(\mathcal P_L\) be Frobenius-metric projection onto the convex operator-norm ball of radius \(L\). It is 1-Lipschitz in Frobenius norm and commutes with left and right orthogonal maps. Define
\[
\bar X=\mathcal P_{C_X\sqrt d}(X),\quad
\bar G=\mathcal P_{C_G\sqrt d}(G),\quad
B=\mathcal P_{C_A}\left[\frac{\phi(\bar X\bar G^\top/\sqrt d)}{\sqrt m}\right].
\tag{4}
\]
By (2)–(3), \(B=A\) except on an exponentially unlikely event, hence eventually almost surely. All three clipping maps are necessary for the following short global concentration proof: merely controlling a derivative on a nonconvex likely set would not establish a global Lipschitz constant.

For two base inputs, the scalar Lipschitz property of \(\phi\), the product inequality, and nonexpansiveness give
\[
\begin{aligned}
\|B(X,G)-B(X',G')\|_F
&\le\frac{C_G\|X-X'\|_F+C_X\|G-G'\|_F}{\sqrt m}\\
&\le\frac C{\sqrt d}\|(X,G)-(X',G')\|_F.
\end{aligned}\tag{5}
\]
If \(\|B\|_{\rm op},\|B'\|_{\rm op}\le C_A\), telescoping products gives
\[
\begin{aligned}
\|(BB^\top)^k-(B'B'^\top)^k\|_F
&\le2k C_A^{2k-1}\|B-B'\|_F,\\
\|(B^\top B)^k-(B'^\top B')^k\|_F
&\le2k C_A^{2k-1}\|B-B'\|_F,\\
\|(BB^\top)^kB-(B'B'^\top)^kB'\|_F
&\le(2k+1)C_A^{2k}\|B-B'\|_F.
\end{aligned}\tag{6}
\]
Every scalar entry is therefore \(C_k/\sqrt d\)-Lipschitz in the independent standard Gaussian base variables.

Oddness of \(\phi\) and the equivariance of the clipping maps preserve signed-permutation invariance. Row sign flips force the means of offdiagonal entries of \((BB^\top)^k\) to vanish; column sign flips do the same for \((B^\top B)^k\). Every entry of \((BB^\top)^kB\) has zero mean. Row/column permutations make all diagonal expectations in each respective square block equal.

Gaussian concentration followed by a union bound gives
\[
\mathbb P\left(\max_{\text{all entries}}|F(B)-\mathbb EF(B)|>
d^{-1/2+\varepsilon}\right)
\le C_k d^2 e^{-c_kd^{2\varepsilon}}
\tag{7}
\]
for each one of the three matrix polynomials in (6). The probabilities are summable. The difference between a common diagonal expectation and the realized normalized trace is at most the maximal diagonal deviation. Choosing a smaller exponent first absorbs constants and dimension ratios. Consequently, for every fixed \(k\ge0\) and every \(\varepsilon>0\), almost surely eventually,
\[
\begin{gathered}
\max_i\left|((AA^\top)^k)_{ii}-\frac1N\operatorname{tr}(AA^\top)^k\right|
,\quad \max_{i\ne j}|((AA^\top)^k)_{ij}|
<m^{-1/2+\varepsilon},\\
\max_i\left|((A^\top A)^k)_{ii}-\frac1m\operatorname{tr}(A^\top A)^k\right|
,\quad \max_{i\ne j}|((A^\top A)^k)_{ij}|
<m^{-1/2+\varepsilon},\\
\max_{i,j}|((AA^\top)^kA)_{ij}|<m^{-1/2+\varepsilon}.
\end{gathered}\tag{8}
\]
The \(k=0\) square statements are immediate. Intersecting over countably many \(k\) and positive rational exponents gives the simultaneous assertion for all fixed \(k,\varepsilon\). These are exactly the required matrix-power entry bounds, with WZF's column dimension equal to our \(m\).

## 3. Conditional covariance and spectral law

Write the rows of \(V\) as \(f_j^\top\), and let
\[
q_j=\|f_j\|^2,\qquad
\rho_{jk}=\frac{f_j^\top f_k}{\sqrt{q_jq_k}},\qquad
\Sigma_V=\mathbb E_x[\phi(Vx)\phi(Vx)^\top].
\]
Gaussian norm and spherical inner-product tails, union bounds, and Borel–Cantelli imply
\[
\max_j|q_j-1|=O\left(\sqrt{\frac{\log d}{d}}\right),\quad
\max_{j\ne k}|\rho_{jk}|=O\left(\sqrt{\frac{\log d}{d}}\right),\quad
\|V\|_{\rm op}=O(1)
\tag{9}
\]
almost surely.

Expand \(g\mapsto\phi(\sqrt qg)\) in the orthonormal Gaussian Hermite basis, with coefficients \(c_\ell(q)\). Even coefficients vanish, and Gaussian integration by parts gives
\[
c_1(q)=\sqrt q A(q),\qquad A(q)=\mathbb E\phi'(\sqrt qZ).
\]
For \(j\ne k\), the bivariate Hermite formula and Cauchy–Schwarz give
\[
(\Sigma_V)_{jk}=A(q_j)A(q_k)f_j^\top f_k+R_{jk},
\qquad |R_{jk}|\le |\rho_{jk}|^3.
\tag{10}
\]
The last bound uses \(|\tanh|\le1\), so the squared Hermite coefficient sums are at most one. Therefore the offdiagonal remainder obeys
\[
\|R_{\rm off}\|_{\rm op}\le m\max_{j\ne k}|\rho_{jk}|^3
=O\left(\frac{(\log d)^{3/2}}{\sqrt d}\right)=o(1).
\tag{11}
\]
The diagonal remainder is exactly \(v(q_j)-q_jA(q_j)^2\), where \(v(q)=\mathbb E\phi(\sqrt qZ)^2\). The functions \(A,v\) are continuous near one. Thus (9), the bounded norm of \(V\), and (10)–(11) prove
\[
\left\|\Sigma_V-\left(a^2VV^\top+\nu I_m\right)\right\|_{\rm op}\to0
\quad\text{almost surely}.
\tag{12}
\]

Here is the exact external spectral-theorem application. In Louart–Liao–Couillet (LLC), take their Gaussian weight matrix to be our \(X\in\mathbb R^{N\times p}\), their deterministic input to be \(V^\top\in\mathbb R^{p\times m}\), their activation to be \(\tanh\), and their dimensions \((n,p,T)=(N,p,m)\). Conditional on a good whole sequence \(V\), all three dimensions are proportional and \(\|V\|_{\rm op}\) is bounded. The unused response matrix in their standing assumptions may be chosen zero. Their Theorem 2 gives a deterministic spectral equivalent depending on \(\Sigma_V\).

Apply the same theorem a second time with identity activation and input \(\Sigma_V^{1/2}\in\mathbb R^{m\times m}\). Its input norm is bounded by (12); its Gaussian matrix is \(Z\in\mathbb R^{N\times m}\). This proves that \(A^\top A\) and
\[
\frac1m\Sigma_V^{1/2}Z^\top Z\Sigma_V^{1/2}
\tag{13}
\]
have asymptotically the same empirical spectral law, almost surely conditional on \(V\).

Put \(C_V=a^2VV^\top+\nu I_m\). Couple the Gaussian row matrices using the same \(Z\). The square-root inequality gives
\[
\left\|\frac1{\sqrt m}Z\Sigma_V^{1/2}
-\frac1{\sqrt m}ZC_V^{1/2}\right\|_{\rm op}
\le\frac{\|Z\|_{\rm op}}{\sqrt m}
\|\Sigma_V-C_V\|_{\rm op}^{1/2}\to0.
\tag{14}
\]
Conditional on \(V\), \(A_{\mathrm G}\) has independent Gaussian rows with covariance \(C_V/m\). Fubini's theorem now transfers the conditional almost-sure matching to the joint model.

For completeness, no new random-matrix input beyond LLC is needed to establish that the limiting law is deterministic. Its identity-activation case with input \(I_p\), weight matrix \(G\in\mathbb R^{m\times p}\), supplies the usual Wishart law for \(GG^\top/d\), after converting between the two Gram matrices and using \(p/d\to1\). Denote that \(m\)-normalized limit by \(\mathrm{MP}_\gamma\), and let \(H\) be its image under \(x\mapsto\nu+a^2x\).

The feature-side law \(\mu_{\mathrm f}\) of \(A^\top A\) is determined by the following transform at \(-\zeta<0\):
\[
\delta_\zeta=\int\frac{t}{\zeta+rt/(1+\delta_\zeta)}\,dH(t),\qquad
m_{\mathrm f}(-\zeta)=\int\frac1{\zeta+rt/(1+\delta_\zeta)}\,dH(t).
\tag{15}
\]
The positive fixed point is unique: rewrite its equation as
\[
\frac{\delta}{1+\delta}
=\int\frac{t}{\zeta(1+\delta)+rt}\,dH(t).
\]
The left side increases strictly and the right side decreases strictly. At finite dimension, \(0\le\delta\le\sup t/\zeta\); this compact bound and uniform convergence of the integrals show continuity of the solution under weak convergence of bounded population laws. Hence the deterministic equivalents converge, and so do the empirical laws.

All matrix norms are eventually bounded by deterministic constants, so weak spectral convergence upgrades to convergence of every fixed moment, and therefore to the all-orders Wasserstein convergence needed in Proposition D.1.

### Row versus feature normalization

If \(\mu_{\mathrm r}\) is the \(N\)-normalized eigenvalue law of \(AA^\top\), then
\[
\mu_{\mathrm r}=\frac1r\mu_{\mathrm f}+\left(1-\frac1r\right)\delta_0.
\tag{16}
\]
The formula is an identity of signed expressions; its result is a probability measure even when \(r<1\), because the feature-side zero mass then cancels the negative term. WZF's \(D\) is the square root pushforward of \(\mu_{\mathrm r}\). In particular
\[
\mathbb E D^{2k}=\frac1r\int\lambda^k\,d\mu_{\mathrm f}(\lambda)\quad(k\ge1),
\qquad \mathbb E D^2=v>0.
\tag{17}
\]
This accounts for the factor \(r\) in WZF's initial covariance \(\Omega_1=rv\mathbb E U_1^2\).

## 4. Full diagonal distribution and exact independence

For fixed orthogonal \(O\in O(N)\), \(Q\in O(m)\), the joint Gaussian law of ((X,V,E)) is preserved by \((X,V,E)\mapsto(OX,QV,OEQ^\top)\). Thus \(A_{\mathrm G}\) is bi-orthogonally invariant. Its singular-value law is the one just obtained.

For \(A\), independently sample a matrix \(M\) with the same distribution, and independent uniform signed permutations \(\Pi_U,\Pi_V\). Since \(A\)'s law is signed-permutation invariant, \(\Pi_U M\Pi_V^\top\) has the same law as \(A\). Estimates (8) apply to \(M\). This is the independent-permutation representation in Proposition D.1(b2). That proposition and its Lemma D.2 extend the power estimates to the entire generated diagonal algebra and identify the same diagonal distribution as \(A_{\mathrm G}\). It would be invalid to skip this argument and infer the diagonal distribution from singular values alone.

For the teacher split, rotate a deterministic unit teacher to \(e_1\), and write full inputs and feature rows as
\[
\widetilde X_i=(z_i,x_i),\qquad
\widetilde W_j=(g_j/\sqrt d,f_j).
\]
The random vectors \(z\in\mathbb R^N\), \(g\in\mathbb R^m\), the perpendicular matrices \(X,V\), and the uniform random variables used to sample labels given \(z\) are mutually independent. Hence \(A\) is **exactly**, not asymptotically, independent of all of ((z,g,Y)). Additional test rows and a deterministic training mask preserve this fact. The low-rank term is
\[
\frac{a}{\sqrt{md}}zg^\top=\frac{s_d}{m}zg^\top,
\qquad s_d=a\sqrt{m/d}\to s=a\sqrt\gamma.
\tag{18}
\]
The side variable is \(g_j=\sqrt d\,\widetilde W_{j1}\sim N(0,1)\), not the vanishing coordinate \(\widetilde W_{j1}\).

The signed-permutation representation can also be chosen independently of this entire side-information vector. No labels or teacher coordinates have to be sign-flipped. The universality application is to the **unconditional** matrix \(A\); conditioning on \(V\) was only a spectral proof device.

One must not add the extensive perpendicular feature matrix \(V\) itself as independent side information: it is dependent on \(A\), and it is not finitely many coordinate-side vectors. The proportional test-row construction is the correct way to infer test-path laws within this argument.

The finite-dimensional side laws have exponential moments: they consist of Gaussian coordinates, bounded labels/residuals, deterministic binary masks, and any finitely many added Gaussian regularizers. Their empirical laws converge in every Wasserstein order by blockwise strong laws and Gaussian moment bounds. Polynomial density in \(L^2\) follows from exponential integrability: an \(L^2\) function orthogonal to all polynomials defines a finite signed measure whose Laplace transform is analytic near zero and has all derivatives zero; uniqueness of Fourier transforms then makes the function zero. This also works for the deterministic train/test mixture.

## 5. Causal ordinary-GD embedding and overlap freezing

Use \(B=A+(s/m)zg^\top\), row mask \(\chi\in\{0,1\}^N\), normalized weights \(w^0=0\), and fixed step parameter \(\lambda\). Ordinary full-batch logistic GD is
\[
\begin{aligned}
q_t^{(d)}&=m^{-1}g^\top w^t,\\
S^t&=Aw^t+s q_t^{(d)}z,\\
r^t&=\chi\odot[Y-\sigma(S^t)],\\
\rho_t^{(d)}&=N^{-1}z^\top r^t,\\
w^{t+1}&=w^t+\lambda[A^\top r^t+s r_d\rho_t^{(d)}g].
\end{aligned}\tag{19}
\]
Replacing dimension-dependent \(\lambda_d,s_d,r_d\) by their limits is harmless at fixed horizon, by the same stability estimate below.

Let \(q_t,\rho_t\) be the deterministic limits constructed recursively through AMP state evolution. Initialize \(R_1=\chi(Y-1/2)\), \(Q_0=0\), \(q_0=0\), and \(\rho_0=\mathbb E[Z_{\rm teacher}R_1]\). Write the AMP coordinates as
\[
\begin{aligned}
Z_t&=A^\top R_t-\sum_{h<t}b_{th}Q_h,\\
Q_t&=Q_{t-1}+\lambda\left[Z_t+\sum_{h<t}b_{th}Q_h
+sr\rho_{t-1}g\right],\\
Y_t^{\rm AMP}&=AQ_t-\sum_{h\le t}a_{th}R_h,\\
R_{t+1}&=\chi\odot\left[Y-\sigma\left(Y_t^{\rm AMP}
+\sum_{h\le t}a_{th}R_h+s q_tz\right)\right].
\end{aligned}\tag{20}
\]
The coefficients \(a,b\) must be the bi-orthogonally invariant AMP prescriptions, not zero. The added history terms cancel their Onsager subtractions **exactly**. Therefore (20) describes ordinary GD with the two rank-one overlaps frozen, and does not assume that unmodified GD is already AMP.

This recursive definition is causal. Before defining \(Q_t\), \(\rho_{t-1}\), the law of \(Z_{1:t}\), and \(b_{th}\) depend on already defined row functions. The resulting column function \(Q_t\) determines \(q_t=\mathbb E[gQ_t]\), the relevant derivatives, and \(a_{th}\). These determine \(R_{t+1}\) and then \(\rho_t=\mathbb E[Z_{\rm teacher}R_{t+1}]\). There is no same-step circular choice of an unknown empirical overlap.

Each \(Q_t\) is a linear function of Gaussian column history and \(g\). Each row function is bounded and Lipschitz in its AMP history, because sigmoid has bounded derivative and previous row functions are recursively Lipschitz. Off the actual binary mask/label support, extend masks and labels using bounded smooth clipping equal to the identity at 0 and 1; this preserves global Lipschitz constants uniformly over side arguments. The functions have polynomial growth.

Here is the independent proof that the frozen overlaps can be replaced by physical empirical overlaps. Let \((\bar w^t,\bar r^t)\) denote (20) after its exact cancellations, and assume its WZF joint \(W_2\) limits. These imply
\[
\varepsilon_{q,t}=\left|\frac{g^\top\bar w^t}{m}-q_t\right|\to0,
\qquad
\varepsilon_{\rho,t}=\left|\frac{z^\top\bar r^t}{N}-\rho_t\right|\to0.
\tag{21}
\]
Indeed the overlap test functions are continuous of at most quadratic growth, which joint \(W_2\) convergence controls. This step does not appeal to WZF Remark 2.23: that remark lists particular empirical AMP statistics and does not automatically cover arbitrary additional global overlaps.

Set
\[
e_t=\frac{\|w^t-\bar w^t\|}{\sqrt m},\quad
h_t=\frac{\|r^t-\bar r^t\|}{\sqrt N},\quad
G_m=\frac{\|g\|}{\sqrt m},\quad Z_N=\frac{\|z\|}{\sqrt N},
\quad C=\|A\|_{\rm op}.
\]
These side norms and \(C\) are eventually bounded. Cauchy–Schwarz and sigmoid's \(1/4\)-Lipschitz property give
\[
h_t\le\frac14\left[
\left(\frac C{\sqrt{r_d}}+|s| Z_NG_m\right)e_t
+|s| Z_N\varepsilon_{q,t}\right],
\tag{22}
\]
while subtracting the two weight updates gives
\[
e_{t+1}\le e_t+|\lambda|\left[
\left(C\sqrt{r_d}+|s|r_dG_mZ_N\right)h_t
+|s|r_dG_m\varepsilon_{\rho,t}\right].
\tag{23}
\]
Since \(e_0=0\), a fixed-horizon induction proves \(e_t,h_t\to0\) for every fixed \(t\). Perturbations in dimension ratios or in \(\lambda,s\) add terms bounded by their scalar differences times uniformly bounded normalized iterate/residual norms and therefore also vanish.

The same induction proves stability under added physical update/residual errors of normalized size \(O(\epsilon)\), with a finite constant depending on the fixed horizon. This is useful for B04's fresh-Gaussian regularization strategy: cancel Onsager terms first, compare the resulting physical recursions, and then let \(\epsilon\downarrow0\). It avoids needing uniform continuity of inverse covariance matrices or Onsager coefficients near a degenerate state.

## 6. Remaining boundaries and primary-source dependencies

The audit establishes the matrix hypotheses and the frozen-to-adaptive reduction. Nonsingularity of the finite state covariance matrices was initially a separate proof obligation. The addendum below verifies B01's direct solution of that obligation. Positive variance of the matrix spectrum alone would not suffice.

The appended test block must have a positive limiting fraction and zero training mask. Conditional on the trained model it supplies independent test observations; it avoids an unjustified identification of test covariance from training singular values alone. Passing from fixed-horizon dynamics to data-dependent unbounded stopping times, convergence to an MLE, or an optimum over all training times requires the separate uniform-time result.

Primary sources inspected directly:

* [Wang–Zhong–Fan, arXiv:2206.13037v5](https://arxiv.org/html/2206.13037v5): Proposition D.1(b2), its bounds (D.6), Lemma D.2, the row-padded convention (D.3), and Theorem 2.22. These supply the final generalized-invariance and AMP implications after their hypotheses are verified above. The theorem explicitly requires independent side information and nonsingular state covariances.
* [Louart–Liao–Couillet, arXiv:1702.05419v2](https://arxiv.org/pdf/1702.05419): Assumptions 1–3 and Theorem 2. The exact substitutions appear in Section 3. This is an empirical spectral theorem; the separate concentration proof in Section 2 is what enables the later dynamical application.

No novelty claim is made for the matrix lemma, the AMP embedding principle, or a complete solution of the original problem. The report is an independent hypothesis and proof audit of the proposed route.

## 7. Addendum: closed cumulants and nonsingular state evolution

I independently inspected Fan's primary [arXiv:2008.11892v5](https://arxiv.org/pdf/2008.11892), equations (5.9)–(5.13), and compared them with the file fullproof/b01_GD_state_evolution_check.md. Matrix order, transposition of the memory arrays, and the outer aspect-ratio factor all agree.

Here is the independent spectral algebra check. Write \(M(z)\) for the row-normalized moment series and \(M_H\) for the population-covariance moment series. Equation (15), expanded at infinity, gives
\[
rM(z)=M_H(rz(1+M(z))).
\]
The ordinary moment–\(R\) identity is
\[
M_H(w)=w(1+M_H(w))R_H^{\rm ord}(w(1+M_H(w))),
\quad
R_H^{\rm ord}(u)=\nu+\frac{a^2}{1-a^2\gamma u}.
\]
Set \(u=z(1+M)(1+rM)\). Substituting yields
\[
M=uR_H^{\rm ord}(ru)
=\nu u+\frac{a^2u}{1-a^2\delta u},
\qquad \delta=r\gamma=N/d.
\]
Thus the rectangular cumulants are
\[
\kappa_2=v,\qquad \kappa_{2k}=a^{2k}\delta^{k-1}\quad(k\ge2).
\]
As a normalization check, the second row spectral moment is
\[
\mathbb E D^4=(1+r)v^2+\delta a^4.
\]

Use B01's notation: \(\Delta=\mathbb E[RR^\top]\), \(\Gamma=\mathbb E[QQ^\top]\), strictly lower triangular row derivative matrix \(\Phi\), and lower triangular column derivative matrix \(\Psi\). Put \(h_0=a^2\delta\), \(K=\Psi\Phi\), \(L=\Phi\Psi\). Inserting the geometric cumulant sequence into Fan's two covariance sums gives
\[
\Sigma=\nu\Gamma+
a^2(I-h_0K)^{-1}
[\Gamma+h_0\Psi\Delta\Psi^\top](I-h_0K)^{-\top},
\]
\[
\Omega=r\nu\Delta+
ra^2(I-h_0L)^{-1}
[\Delta+h_0\Phi\Gamma\Phi^\top](I-h_0L)^{-\top}.
\]
These identities follow by grouping terms with a fixed sum of the left and right powers. Nilpotence makes every series finite, so no analytic convergence or small-step assumption is hidden. Both second terms are positive semidefinite congruences. Therefore
\[
\Omega\succeq r\nu\Delta,\qquad \Sigma\succeq\nu\Gamma.
\]

Initially \(\Delta_1=p/4>0\), where \(p\) is the positive training fraction. If \(\Delta_t\succ0\), then \(\Omega_t\succ0\). The column recursion is linear and has derivative matrix \(\Psi_t\) with diagonal entries \(\lambda>0\); it is invertible. Since its teacher coordinate is independent of the centered column Gaussian fields,
\[
\Gamma_t=\Psi_t\Omega_t\Psi_t^\top+q_{1:t}q_{1:t}^\top\succ0.
\]
Consequently \(\Sigma_t\succ0\). Conditional on the teacher, label, mask, and previous row Gaussian fields, the new row field has positive Gaussian innovation variance. On mask one, the new residual is a strictly monotone sigmoid function of that innovation, while every previous residual is already fixed. It cannot belong to their linear span almost surely. Hence \(\Delta_{t+1}\succ0\), completing induction.

This proves every state covariance required by WZF is nonsingular for every fixed positive step and every finite horizon. The earlier possible regularization strategy is unnecessary. All fixed-horizon conclusions remain subject to taking the dimension limit with the horizon held fixed; the separate uniform-time audit addresses the additional optimization argument.
