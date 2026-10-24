SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B05, 2026-09-23T03:13:19Z.

# B05 — rough ruled-surface interval theorem and a kappa-free two-sheet receiver

Run: `20260923T031319Z-account04-B05-rough-ruled-r1`.

Status: **PROVED SUPPORTING THEOREMS / FULL QFORM OPEN**.

The target remains the unrestricted cap-one product-law conjecture. Continuity is separate. This note proves the rough-input form of the new one-sheet estimate without evaluating an arbitrary density on a quadratic surface, and applies the completed account01/B05 theorem to an actual two-sheet inequality. It does not call the half-line estimate a full rank-three theorem.

## 1. Smooth coarea identity and Jacobian

Let
\[
q(z)=\lambda_1z_1^2+\lambda_2z_2^2-\mu z_3^2,\qquad
\lambda_1,\lambda_2,\mu>0,
\]
and let \(g\) be a smooth probability density on \(\mathbb R^3\). Use
\[
z_1=\frac{\rho\cos\theta}{\sqrt{\lambda_1}},\quad
z_2=\frac{\rho\sin\theta}{\sqrt{\lambda_2}},\quad
z_3=\frac{w}{\sqrt\mu}.
\]
Then
\[
dz=\frac{\rho}{\sqrt{\lambda_1\lambda_2\mu}}\,d\rho\,d\theta\,dw,
\qquad q(z)=\rho^2-w^2.
\]
For every bounded interval \(I\), Tonelli and \(y=\rho^2-w^2\), \(dy=2\rho\,d\rho\), give
\[
\begin{aligned}
\Pr\{q(Z)\in I\}
&=\frac1{2\sqrt{\lambda_1\lambda_2\mu}}
 \int_I\int_{\{w^2+y>0\}}\int_0^{2\pi}\\
&\quad g\!\left(
 \frac{\sqrt{w^2+y}\cos\theta}{\sqrt{\lambda_1}},
 \frac{\sqrt{w^2+y}\sin\theta}{\sqrt{\lambda_2}},
 \frac w{\sqrt\mu}\right)\,d\theta\,dw\,dy.
\end{aligned}
\tag{1.1}
\]
Thus the polar Jacobian \(\rho\) cancels the level Jacobian in \(dy=2\rho\,d\rho\). Equation (1.1) is an equality of nonnegative interval integrals and does not require a pointwise version of a rough surface trace.

For \(y>0\), the completed ruled estimate in the current Claude package bounds the smooth product-law trace by
\[
C_+(\lambda)
=(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
\left(\frac{\sin^2\theta}{\lambda_1}
+\frac{\cos^2\theta}{\lambda_2}
+\frac1\mu\right)^{-1/2}d\theta
\le \frac{\pi\sqrt2}{s},
\tag{1.2}
\]
where \(s=\min(\lambda_1,\lambda_2,\mu)\).

## 2. Rough-product interval transfer

### Theorem 2.1 — `QFORM-ROUGH-RULED-ONE-SHEET-INTERVAL-v1`

Let independent \(X_i\) have measurable probability densities \(0\le f_i\le1\). For orthonormal \(r_1,r_2,r_3\), put
\[
Q=\lambda_1\langle r_1,X\rangle^2+
  \lambda_2\langle r_2,X\rangle^2-
  \mu\langle r_3,X\rangle^2.
\]
For every interval \(J\subset[0,\infty)\),
\[
\boxed{\Pr\{Q\in J\}\le C_+(\lambda)|J|
\le \frac{\pi\sqrt2}{s}|J|.}
\tag{2.1}
\]

#### Proof

Let \(f_{i,\varepsilon}=f_i*\eta_\varepsilon\), with \(\eta_\varepsilon\) a smooth probability mollifier. Convolution preserves total mass and the cap \(f_{i,\varepsilon}\le1\). Couple \(X_{i,\varepsilon}=X_i+\varepsilon Z_i\) with independent smooth noises. Then \(Q(X_\varepsilon)\to Q(X)\) in probability.

For every open interval \(G\Subset(0,\infty)\), the smooth ruled theorem and (1.1) give
\[
\Pr\{Q(X_\varepsilon)\in G\}\le C_+(\lambda)|G|.
\]
Portmanteau for the open set \(G\) yields
\[
\Pr\{Q(X)\in G\}\le\liminf_{\varepsilon\downarrow0}
\Pr\{Q(X_\varepsilon)\in G\}\le C_+(\lambda)|G|.
\]
Enlarge a closed interval \(J\Subset(0,\infty)\) by \(\delta\) and let \(\delta\downarrow0\). At the endpoint \(0\), the nonzero polynomial \(Q\) has a Lebesgue-null zero set, hence \(\Pr(Q=0)=0\); apply the preceding estimate to \((0,b+\delta)\). This proves (2.1). The proof passes interval probabilities, not pointwise values of a rough trace. QED.

## 3. Two-sheet side: actual account01/B05 receiver

For \(y=-\alpha<0\), the same substitution yields the two-sheet trace
\[
H_g(\alpha)=\frac1{2\sqrt{\lambda_1\lambda_2\mu}}
\sum_{\sigma=\pm1}\int_0^{2\pi}\int_{\sqrt\alpha}^{\infty}
g\!\left(
 \frac{\sqrt{w^2-\alpha}\cos\theta}{\sqrt{\lambda_1}},
 \frac{\sqrt{w^2-\alpha}\sin\theta}{\sqrt{\lambda_2}},
 \frac{\sigma w}{\sqrt\mu}\right)\,dw\,d\theta,
\tag{3.1}
\]
with
\[
\Pr\{-\beta<Q<-\alpha\}=\int_\alpha^\beta H_g(u)\,du.
\tag{3.2}
\]
An arbitrary joint density cap cannot bound (3.1); product provenance must be spent.

The newest completed account01/B05 theorem says that for three genuinely independent scalars with caps \(L_1,L_2,L_3\), any invertible symmetric \(3\times3\) quadratic core \(M\), and arbitrary affine terms,
\[
\boxed{
\|p_Q\|_\infty
\le C_3(L_1L_2L_3)^{2/3}|\det M|^{-1/3},
\qquad C_3=8\sqrt2\,3^{3/4}<25.8.
}
\tag{3.3}
\]

Apply (3.3) in the one-rank-two/two-rank-one aggregate packet. Let
\[
\mathfrak m=\sum_{i\in G_1,j\in G_2,k\in G_3}|\det A_{ijk}|>0
\]
and let \(u\) be the unit physical Schur direction in the first bank. Keep one physical coordinate \(X_i\) and the two normalized scalar-bank variables \(Y,Z\), conditioning on every other original variable. These retained variables are independent with caps \(1,\sqrt2,\sqrt2\), and their exact quadratic-core determinant is
\[
|\det M_i|=\mathfrak m\,u_i^2.
\tag{3.4}
\]
Therefore
\[
\Pr\{Q\in I\mid\text{conditioning}\}
\le 8\,2^{7/6}3^{3/4}
(\mathfrak m u_i^2)^{-1/3}|I|.
\tag{3.5}
\]
If \(\max_i u_i^2\ge\eta\), averaging gives the full-line, hence two-sheet, estimate
\[
\boxed{\Pr\{Q\in I\}<41(\mathfrak m\eta)^{-1/3}|I|.}
\tag{3.6}
\]
There is no factor involving \(\det B\), \(\sigma_{\min}(B)\), or \(\|B\|_{\rm op}\).

Complementary account01/B05 receivers are
\[
\|p_Q\|_\infty\le256(\mathfrak m\|B\|_{\rm op})^{-1/4}
\tag{3.7}
\]
for an invertible scalar pair \(B\), and
\[
\|p_Q\|_\infty\le16\mathfrak m^{-1/3}
\tag{3.8}
\]
at exact rank one. Equations (3.6)–(3.8) are genuine convex/two-sheet payments in their stated product-provenance packet, not fiber-supremum estimates.

## 4. Remaining gap

The one-sheet side is now a rigorous rough-input interval theorem. In the aggregate two-sheet packet, scalar-pair condition-number degeneration, exact rank one, and the double-zero regime with a heavy physical Schur coordinate are paid.

The first unpaid local implication is `QFORM-DOUBLEZERO-DIFFUSE-SCHUR-GROUPING-v1`: \(\mathfrak m\) stays bounded below, \(\|B\|_{\rm op}\to0\), and
\[
\max_i u_i^2\to0,\qquad \sum_i u_i^2=1.
\]
One must spend the total Schur mass before paying the local reciprocal factor \((u_i^2)^{-1/3}\). The orthogonal first-bank aggregate remains correlated with \(u\cdot X_{G_1}\) and enters scalar-pair translations, so it cannot be conditioned away while retaining a density cap.

The unrestricted conjecture also requires a structural reduction placing every three-large-eigenvalue matrix in a paid packet. Neither issue is solved here. Continuity is not claimed.

## 5. Source pins

- Claude ruled-surface package beginning at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, with later corrections retained.
- account01/B05 r25 report blob `0bed6a6426109541a9664c70b1acb27a9166528a`, audit commit `3e8704eead81b6fef2d305978ec89abb307d899a`.
- account02/B05 rough-transfer checkpoint blob `f0be659bbc113dbf7c203f6a42d4791c4d7e6d32`.

No post-rotation independence, arbitrary-joint coarea estimate, pointwise rough trace evaluation, conditional-cap substitution, moment/support assumption, or perturbative deletion is used. Status remains `WITHOUT_VERIFIED_BRAIN`.
