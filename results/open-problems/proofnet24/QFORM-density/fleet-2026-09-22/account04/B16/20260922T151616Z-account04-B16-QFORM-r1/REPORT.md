# account04/B16 — conditional heavy-Rayleigh projection–product theorem

Run: 20260922T151616Z-account04-B16-QFORM-r1  
Programme: QFORM-DENSITY-3EIG-20260922, owner revision 2026-09-22.5  
Classification: ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN  
Execution: WITHOUT_VERIFIED_BRAIN

## 1. Theorem

Let \(X_1,\ldots,X_n\) be independent real random variables with densities \(0\le f_i\le1\), and let \(A\) be any real symmetric matrix. Suppose that for some original-coordinate set \(R\), the physical principal block
\[
B=A_{RR}=U\Lambda U^\top
\]
has rank exactly three, with \(U^\top U=I_3\) and invertible real symmetric \(\Lambda\).

Choose \(i\in R\). Write \(u_k\) for row \(k\) of \(U\), and set
\[
c=\|u_i\|_2^2>0,\qquad e=u_i/\sqrt c,\qquad P=I-ee^\top,\qquad a=e^\top\Lambda e.
\]
Assume
\[
a\ne0,\qquad \|Pu_k\|_2^2\le\frac12\quad(k\in R,\ k\ne i).
\]
Then the full quadratic form \(Q=X^\top AX\), with arbitrary couplings between \(R\) and \(R^c\) and an arbitrary quadratic form on \(R^c\), has an essentially bounded density satisfying
\[
\boxed{\|p_Q\|_\infty\le
4\sqrt{2e}\,c^{-1/2}|a|^{-1/4}|\det\Lambda|^{-1/4}.}
\tag{1}
\]
Since \(d=B_{ii}=ca\), equivalently
\[
\boxed{\|p_Q\|_\infty\le
4\sqrt{2e}\,(c|d||\det\Lambda|)^{-1/4}.}
\tag{2}
\]
If the three nonzero eigenvalues of \(B\) have modulus at least one, \(c>1/2\), and \(|B_{ii}|\ge1/4\), then
\[
\boxed{\|p_Q\|_\infty\le2^{13/4}\sqrt e<15.69.}
\tag{3}
\]
If \(i\) is the unique row of \(U\) with leverage \(>1/2\), the transverse hypothesis is automatic. All signatures and repeated eigenvalues are allowed. The theorem proves essential boundedness; continuity is not claimed.

Name: QFORM-CONDITIONAL-HEAVY-RAYLEIGH-HALF-v1.

## 2. Peer result actually applied

The assigned partner account01/B16 proved QFORM-RANK3-HEAVY-RAYLEIGH-HALF-v1 at

yspennstate/math-open-problems@4d35dc77fb399e31aa4f3525c8fed83808a86572

path

proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260922T123944Z-B16-qform/REPORT.md.

Its core analytic estimate is the rank-two diffuse half-order bound
\[
\operatorname*{ess\,sup}_s\mathbb E|s-W^\top S W|^{-1/2}
\le4\sqrt{2e}\,|\det S|^{-1/4}.
\tag{4}
\]
The new step is to show that (4) is uniform after arbitrary outside conditioning, because the induced perturbation of the residual is linear in each remaining original coordinate. This applies the partner result to the full conditional density inequality rather than merely citing it.

The phase-stability input is also consistent with account01/B08's QFORM-DIFFUSE-SEPARABLE-PHASE-v1, commit fce159beaecf924a3e500dc7865ae61f8b35c932.

## 3. Rank-two estimate with coordinate-linear phases

Let \(V\in\mathbb R^{m\times2}\) have \(V^\top V=I_2\), with rows \(v_k\) satisfying \(\|v_k\|^2\le1/2\). Let \(Y_k\) be independent with densities bounded by one, put \(W=V^\top Y\), let \(S\) be invertible symmetric \(2\times2\), and let \(\beta_k\in\mathbb R\). Define
\[
T=W^\top S W+\sum_k\beta_kY_k.
\]
Then
\[
\boxed{\operatorname*{ess\,sup}_s\mathbb E|s-T|^{-1/2}
\le4\sqrt{2e}\,|\det S|^{-1/4}.}
\tag{5}
\]

Fix Fourier time \(\tau\) and absorb the linear term into
\[
a_{k,\tau}(x)=f_k(x)e^{i\tau\beta_kx}.
\]
Its modulus is \(f_k\), so every one-dimensional norm used by sharp Hausdorff--Young is unchanged. The geometric rank-one Brascamp--Lieb calculation in the partner theorem therefore gives, uniformly in \(\tau\) and all \(\beta_k\),
\[
\|\widehat\mu_\tau\|_{L^1(\mathbb R^2)}\le(2\pi)^2e,
\tag{6}
\]
where \(\mu_\tau\) is the resulting complex pushforward to \(W\).

Gaussian-regularized Fourier inversion and the two-dimensional Fresnel integral give
\[
|\phi_T(\tau)|\le
\min\left(1,\frac{\pi e}{|\tau|\,|\det S|^{1/2}}\right).
\tag{7}
\]
No scalar pointwise van-der-Corput bound is used. Put \(K=\pi e|\det S|^{-1/2}\). The Riesz identity
\[
\widehat{|x|^{-1/2}}(\tau)=\sqrt{2\pi}\,|\tau|^{-1/2}
\]
and
\[
\int_{\mathbb R}|\tau|^{-1/2}\min(1,K/|\tau|)\,d\tau=8\sqrt K
\]
give (5), with Gaussian regularization providing the distributional justification and (7) the absolute domination.

## 4. Arbitrary outside couplings

Condition on all outside variables \(X_{R^c}=y\). The conditional form in \(x=X_R\) is
\[
x^\top Bx+\ell(y)^\top x+\kappa(y),
\tag{8}
\]
and the coordinates inside \(R\) remain independent with their original density caps.

Write
\[
U^\top x=\sqrt c\,e\,x_i+Z,\qquad z_0=e^\top Z,\qquad W=PZ,
\]
and in \(\mathbb Re\oplus e^\perp\) write
\[
\Lambda=\begin{pmatrix}a&b^\top\\ b&C\end{pmatrix}.
\]
The \(x_i\)-terms are
\[
ac\,x_i^2+\left(2\sqrt c(az_0+b^\top W)+\ell_i\right)x_i.
\]
Completing this original-coordinate square gives exactly
\[
Q\mid X_{R^c}=y
=ac\,[x_i+\theta_y(X_{R\setminus\{i\}})]^2
+W^\top S W+\sum_{k\ne i}\beta_{k,y}X_k+\gamma_y,
\tag{9}
\]
where
\[
S=C-\frac{bb^\top}{a},\qquad \det S=\frac{\det\Lambda}{a}.
\tag{10}
\]
Indeed, subtracting the completed square cancels the \(z_0^2\) and \(z_0W\) terms; the outside-induced term leaves only a linear combination of the remaining original coordinates. No transformed-coordinate conditional density cap is assumed.

The transverse rows \(Pu_k\), \(k\ne i\), form a Parseval frame on \(e^\perp\):
\[
\sum_{k\ne i}(Pu_k)(Pu_k)^\top=P.
\]
Thus (5) applies to the residual in (9), uniformly in \(y\).

For fixed \(X_{R\setminus\{i\}}\) and \(y\), the square pushforward of the original physical variable \(X_i\) has density bounded by
\[
|ac|^{-1/2}|t-T_y|^{-1/2}.
\tag{11}
\]
There are at most two roots; the two density values sum to at most two and cancel the derivative factor two. Averaging (11), using (5), and then (10), gives
\[
\begin{aligned}
\|p_{Q\mid y}\|_\infty
&\le4\sqrt{2e}|ac|^{-1/2}|\det S|^{-1/4}\\
&=4\sqrt{2e}c^{-1/2}|a|^{-1/4}|\det\Lambda|^{-1/4}.
\end{aligned}
\]
This bound is independent of \(y\). Mixing over \(X_{R^c}\) proves (1) and absolute continuity of the full law.

Since \(d=ca\), (2) follows. Under \(c>1/2\), \(|d|\ge1/4\), and \(|\det\Lambda|\ge1\),
\[
(c|d||\det\Lambda|)^{-1/4}\le(1/8)^{-1/4}=2^{3/4},
\]
which proves (3).

## 5. Scope and remaining implication

The theorem permits arbitrary ambient dimension, arbitrary outside quadratic terms, arbitrary outside couplings, every signature of the rank-three block, and arbitrary cap-one input densities without moments or support regularity.

It does not assert that every matrix with three large eigenvalues contains such a physical principal block. That structural extraction remains false for several naive fixed-minor formulations in the live correction inbox.

The first remaining conditional-block interface is QFORM-CONDITIONAL-HEAVY-ISOTROPIC-OR-MULTIHEAVY-v1: handle either \(a=e^\top\Lambda e=0\) or very small, where the pivot is mainly bilinear, or a transverse Parseval row with leverage \(>1/2\). Any solution must retain original-coordinate product structure.

After that, a separate full-target debt remains: extract a controlled physical block or aggregate from an arbitrary full matrix having only three selected large eigenvalues and an arbitrary coupled spectral complement.

## 6. Integrity

The proof uses no uniform scalar quadratic-phase decay, no independence after spectral rotation, no fiber supremum, no fixed-minor extraction theorem, and no conditional cap for an aggregate. It adds no moment, Gaussian, log-concavity, compact-support, connected-support, or sign hypothesis.

Status: ESSENTIAL_STEP_APPLIED. The stated branch theorem is proved. The full conjecture remains open.
