# Fixed finite test-input predictions for the selected two-input law

**Status: internally proved extension, conditional on the previously established joint initialization, macro compactness, and selected training law in ALL_INITIAL_LIMIT.md; independently audited in reviews/i03_test_predictions_review.md.** This concerns a fixed finite collection of deterministic test inputs evaluated along the same training run. Test inputs have no labels and do not enter GD. There is no claim uniform over an infinite input class, no generalization-risk theorem, and no pre-step tangent-Gram \(L^1/J_1\) limit.

Use the exact shallow two-training-input model and scales of ALL_INITIAL_LIMIT.md: \(X\in\mathbb R^{2\times d}\) has full row rank, \(G=XX^T\), \(0<\rho<1\), \(a=m^{1/\alpha}\), \(L=(\log m)^{1/\alpha}\), and \(h=\gamma/L\). Fix any finite deterministic matrix \(Z\in\mathbb R^{q\times d}\), with \(q\) fixed as width grows. Define
\[
g_{i,n}=(ZU_{i,n})_+,\qquad
f^*_{m,n}=\frac1{aL}\sum_{i=1}^m W_{i,n}g_{i,n},\qquad
K=ZX^TG^{-1}\in\mathbb R^{q\times2}. \tag{1}
\]
The positive part acts coordinatewise. Polygonally interpolate \(f^*_m\) at physical times \(nh\). Write \(r_m=y-f_m\) for the **training** residual. The test outputs have no feedback into this residual.

## Joint initial law

Stack the input matrices as \(A=\binom XZ\), without assuming that \(A\) has full row rank. For each original coordinate \(\ell\) and sign \(\pm\), put
\[
a_\ell^\pm=(\pm Ae_\ell)_+
 =\binom{x_\ell^\pm}{z_\ell^\pm},\qquad
x_\ell^\pm=(\pm Xe_\ell)_+,\quad
z_\ell^\pm=(\pm Ze_\ell)_+. \tag{2}
\]
Use the **same** signed-ray stable variables \(\xi_\ell^\pm,S_\ell^\pm\) and independent marked Poisson process \(N\) as in BOUNDARY_GRID.md. The stacked finite-ray initialization limit is
\[
\binom F{F_*}
 =\sum_{\ell,\pm}a_\ell^\pm\xi_\ell^\pm,\qquad
\begin{pmatrix}C&C_*^T\\C_*&C_{**}\end{pmatrix}
 =\sum_{\ell,\pm}S_\ell^\pm a_\ell^\pm(a_\ell^\pm)^T, \tag{3}
\]
where, in particular,
\[
C_*=\sum_{\ell,\pm}S_\ell^\pm z_\ell^\pm(x_\ell^\pm)^T
 \in\mathbb R^{q\times2}. \tag{4}
\]
Here \((F,C,N)\) are exactly the training primitives, while \(F_*,C_*\) record their joint test geometry. Thus
\[
(f_{m,0},f^*_{m,0},C_{m,0},C_{*,m,0},N_m)
\ \Rightarrow\ (F,F_*,C,C_*,N),\quad
C_{*,m,0}=a^{-2}\sum_i g_{i,0}h_{i,0}^T,\quad h_{i,n}=(XU_{i,n})_+. \tag{5}
\]
Here is the rank-free part of that finite-ray proof explicitly. With \(H_A(u)=(Au)_+\), \(\Psi_A(u)=\sum_{\ell,\pm}(\pm u_\ell)_+a_\ell^\pm\), and \(M_2(u)\) the second largest \(|u_\ell|\),
\[
\|H_A(u)-\Psi_A(u)\|\le c_A M_2(u),\quad
\left\|H_A(u)H_A(u)^T-
 \sum_{\ell,\pm}(\pm u_\ell)_+^2a_\ell^\pm(a_\ell^\pm)^T\right\|
\le c_A\sum_{\ell<j}|u_\ell u_j|. \tag{5a}
\]
The first bound follows by separating the largest original coordinate and using ReLU Lipschitzness; the second follows by expanding the outer products and bounding every cross-coordinate term. The \(\alpha\)-moment of \(M_2(U)\) is finite, so conditional stable summation makes the \(W\)-weighted first remainder divided by \(aL\) vanish: its conditional \(\alpha\)-scale to the power \(\alpha\) is bounded in mean by \(O(1/\log m)\). For the Gram remainder choose \(\alpha/2<s<\min(\alpha,1)\); subadditivity and finite \(s\)-moments give an \(O(m^{1-2s/\alpha})\) bound for its \(s\)-moment after division by \(a^2\). The remaining signed-coordinate ray and marked-\(W\) limits, including their joint independence and small-jump estimates, are precisely the scalar/category initialization theorem used in BOUNDARY_GRID.md. None of these steps requires rank of \(A\). Full row rank was used there only to obtain a density for the **training** \(F\) and positive-definite training \(C\); those properties remain available because \(X\) itself has full row rank. No density or nonsingularity of \((F,F_*)\) or the full block matrix is asserted.

## Exact finite-width projection and output identities

Every hidden-layer update belongs to the row span of \(X\):
\[
U_{i,n+1}-U_{i,n}
 =(\gamma/a)W_{i,n}X^TD(XU_{i,n})r_{m,n}.
\]
Consequently, at **every width and every step**, with \(v_{i,n}=XU_{i,n}\),
\[
ZU_{i,n}=K v_{i,n}+(Z-KX)U_{i,0}. \tag{6}
\]
For a retained marked endpoint with \((W_{i,0}/a,U_{i,0})\to(z,u)\), divide (6) by \(L\). The initial-mark offset tends to zero, uniformly in time, so if \(v_{i,n}/L\to q_{z,u}(t)\) along a macro subsequence, then
\[
ZU_{i,n}/L\to Kq_{z,u}(t),\qquad
g_{i,n}/L\to(Kq_{z,u}(t))_+ \tag{7}
\]
uniformly on each fixed physical horizon. This identity is the reason that a possibly out-of-training-span test input still has a selected endpoint path; the orthogonal initial component is \(O(1)\) for a retained atom and vanishes after division by \(L\).
The ReLU acts **after** the map \(K\): \((Kq)_+\) cannot generally be replaced by \(K(q)_+\), because rows of \(K\) may contain negative entries.

There is also an exact integration-by-parts identity, valid at every grid node. Since \(W_{i,n}-W_{i,0}=(\gamma/a)\sum_{j<n}r_{m,j}^Th_{i,j}\), set
\[
A_{*,m}(n,j)=a^{-2}\sum_i g_{i,n}h_{i,j}^T,\qquad
J_{m,n}=h\sum_{j<n}r_{m,j}.
\]
Then
\[
f^*_{m,n}-f^*_{m,0}
 =\frac1L\sum_i z_{i,0}(g_{i,n}-g_{i,0})
  +h\sum_{j<n}A_{*,m}(n,j)r_{m,j},
\qquad z_{i,0}=W_{i,0}/a. \tag{8}
\]
This uses the actual simultaneous GD iterates, including any gate crossing. No test tangent-kernel approximation has been inserted.

## Uniform test–train Gram freeze and cutoff removal

On the finite-horizon bootstrap localization of MACRO_COMPACTNESS.md, let \(R_{i,0}=(W_{i,0}^2+\|U_{i,0}\|^2)^{1/2}\), \(S_0=a^{-2}\sum_iR_{i,0}^2\), \(R_*\) be a localized bound for \(\sup_{n\le T/h}\|r_{m,n}\|\), and \(T<\infty\). Its row bound gives, simultaneously for every row \(i\),
\[
\sup_{n\le T/h}\|(W_{i,n},U_{i,n})-(W_{i,0},U_{i,0})\|
 \le\varepsilon_m R_{i,0},\qquad \varepsilon_m=O(L/a)\to0. \tag{9}
\]
ReLU Lipschitzness yields \(\|g_{i,n}-g_{i,0}\|\le\|Z\|\varepsilon_mR_{i,0}\) and \(\|h_{i,j}-h_{i,0}\|\le\|X\|\varepsilon_mR_{i,0}\); all features are bounded by a fixed multiple of \(R_{i,0}\). Expanding the two-factor difference and applying Cauchy–Schwarz therefore gives the **rectangular cross-time** estimate
\[
\sup_{n,j\le T/h}\|A_{*,m}(n,j)-C_{*,m,0}\|
 \le c_{X,Z}\varepsilon_m S_0=o_P(1). \tag{10}
\]
Its limiting matrix need not be symmetric. Since \(\sup_n\|r_{m,n}\|\) is localized and \(J_m\to I=\int r\) whenever \(r_m\to r\), the second term of (8) converges uniformly to \(C_*I(t)\).

The first term of (8) has the same uniform small-initial-output-weight control as the training endpoint term, with \(\|Z\|\|X\|\) in place of \(\|G\|\). For \(D_\varepsilon=\{i:|z_{i,0}|\le\varepsilon\}\), the exact hidden update gives
\[
\begin{aligned}
\sup_{n\le T/h}
\left\|\frac1L\sum_{i\in D_\varepsilon}
 z_{i,0}(g_{i,n}-g_{i,0})\right\|
&\le (T+h)\|Z\|\|X\|R_*
\sum_{i\in D_\varepsilon}|z_{i,0}|
  \sup_{j\le T/h}|W_{i,j}/a|\\
&\le (T+h)\|Z\|\|X\|R_*
\left(\sum_{i\in D_\varepsilon}z_{i,0}^2
      +\varepsilon_m S_0\right). \tag{11}
\end{aligned}
\]
The initial small-\(|z|\) square mass has \(\limsup_m\mathbb E\sum_{D_\varepsilon}z_{i,0}^2=O(\varepsilon^{2-\alpha})\). For a fixed \(\varepsilon\), retaining \(|z|<M,\|u\|<B\) leaves finitely many atoms; large \(|z|\) and large original marks are removed by their finite-intensity occurrence probabilities. By (7), each retained contribution converges uniformly to \(z(Kq_{z,u}(t))_+\), as its initial \(g_{i,0}/L\to0\). Every limiting endpoint satisfies \(\sup_{t\le T}\|q_{z,u}(t)\|\le |z|\|G\|\int_0^T\|r(s)\|ds\), so
\[
\sum_{(z,u)\in N}\sup_{t\le T}
  \|z(Kq_{z,u}(t))_+\|
\le \|K\|\|G\|
  \left(\int_0^T\|r(s)\|ds\right)\int z^2N(dz,du)<\infty. \tag{12}
\]
This establishes absolute uniform convergence of the limiting endpoint sum and permits removal of all cutoffs.

The same localized energy bound gives \(\sup_{n\le T/h}\|f^*_{m,n+1}-f^*_{m,n}\|\le h\,c_{X,Z,\gamma,T}R_*S_0(1+o(1))\) by splitting the one-step test-output increment into the \(g\)-change and \(W\)-change. Thus held and polygonal test paths have the same limit, and (8)–(12) give joint tightness and identification in \(C([0,T];\mathbb R^{2+q})\).

## General fixed-test limit and the four selected branches

For any selected training-subsequence limit with original marked endpoints \(q_{z,u}\), the test-output path is necessarily
\[
\boxed{\quad
f^*(t)=F_*+C_*I(t)
  +\int z\bigl(Kq_{z,u}(t)\bigr)_+N(dz,du),
\qquad I(t)=\int_0^t r(s)ds.\quad} \tag{13}
\]
The integral is an ordinary absolutely and uniformly convergent Poisson sum. The selected training theorem ALL_INITIAL_LIMIT.md makes \(r\) and every \(q_{z,u}\) a unique measurable function of \((F,C,N)\). Equations (5)–(13) therefore identify **every** joint subsequential test/training limit with the same path, proving
\[
(f_m,f_m^*,f_{m,0},f^*_{m,0},C_{m,0},C_{*,m,0},N_m)
\ \Rightarrow\
(y-r,f^*,F,F_*,C,C_*,N)
\]
with the first two coordinates in \(C([0,T];\mathbb R^{2+q})\), for every fixed finite \(Z\) and \(T\). Training initial residual axes have probability zero, so its four conditional branches combine without an extra hitting-time continuity claim.

The endpoint sum in (13) simplifies because each selected sign population shares one normalized path. All positive parts below act coordinatewise in \(\mathbb R^q\).

* If \(R_1,R_2>0\), let \(P_+\) and \(V\) be the any-active selected mass and inherited reflected endpoint of ALL_INITIAL_LIMIT.md (equivalently the one-capture path of ONE_CAPTURE.md). Then
  \[
  f^*(t)=F_*+C_*I(t)+P_+(KV(t))_+. \tag{14}
  \]
* If \(R_1,R_2<0\), use \(P_-\) and the reflected positive-sign-mirror endpoint \(\widetilde V\) driven by \(-r\). Every selected endpoint is \(|z|\widetilde V\) with \(z<0\), so
  \[
  f^*(t)=F_*+C_*I(t)-P_-(K\widetilde V(t))_+. \tag{15}
  \]
* If \(R_1<0<R_2\), let \(P_2,P_1\) be the frozen-grid orbit-selected positive- and negative-\(z\) masses of ALL_MIXED_LIMIT.md, and write \(v_+=(u,v)\), \(v_-=(v_-,u_-)\) in its original training-coordinate order. Then
  \[
  f^*(t)=F_*+C_*I(t)+P_2(Kv_+(t))_+-P_1(Kv_-(t))_+. \tag{16}
  \]
  The opposite mixed orientation is obtained by the exact training-coordinate permutation of ALL_INITIAL_LIMIT.md, applied to \(v_\pm\) before multiplication by the original \(K\). There is no new test-output selector.

As a consistency check, taking \(Z=X\) gives \(K=I_2\), \(F_*=F\), \(C_*=C\); (13) becomes the already proved training output identity \(f=y-r\). The present theorem is for fixed finite test rows only. It does not claim convergence uniformly over \(Z\), population prediction risk, a deep-network feature law, or a stronger topology for the binary pre-step tangent Gram.
