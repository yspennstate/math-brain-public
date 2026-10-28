# QFORM additional-eigenvalue control: two-stage Schur transport

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-22T20:45:29Z.

attacking: exact original-coordinate transport of arbitrary added spectral directions through two successive Schur pivots, with a dependence-safe density consequence.

## Status

Supporting theorem. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. The result proves essential boundedness only in the quantitative scopes stated below; continuity is not claimed.


## 1. Exact one-pivot transport for an arbitrary finite-rank symmetric addition

Let

\[
M_0=\begin{pmatrix}a&b^T\\ b&C\end{pmatrix},\qquad a\ne0,
\]

and add an arbitrary symmetric perturbation written as

\[
H=U\Theta U^T,\qquad U=\begin{pmatrix}u^T\\W\end{pmatrix},\qquad \Theta=\Theta^T.
\]

No sign, size, rank, or invertibility assumption is imposed on \(\Theta\). Put

\[
M_1=M_0+H,\quad a_1=a+u^T\Theta u,
\]

and assume only \(a_1\ne0\). Write the two Schur complements

\[
S_0=C-\frac{bb^T}{a},\qquad
S_1=M_1/ a_1.
\]

Define

\[
D=W-\frac{bu^T}{a},\qquad
K_1=\Theta-\frac{\Theta uu^T\Theta}{a_1}.
\]

Then the exact identity is

\[
\boxed{S_1=S_0+D K_1D^T.}\tag{1}
\]

If \(\Theta\) is invertible this may equivalently be written

\[
K_1=(\Theta^{-1}+uu^T/a)^{-1},
\]

but (1) does not require invertibility.

### Proof

Use the baseline elimination congruence

\[
L=\begin{pmatrix}1&0\\-b/a&I\end{pmatrix}.
\]

Then

\[
LM_0L^T=\operatorname{diag}(a,S_0),\qquad
LU=\begin{pmatrix}u^T\\D\end{pmatrix}.
\]

Hence

\[
LM_1L^T=
\begin{pmatrix}
a+u^T\Theta u & u^T\Theta D^T\\
D\Theta u & S_0+D\Theta D^T
\end{pmatrix}.
\]

Taking the Schur complement of the top-left scalar gives exactly (1). Because the congruence is unit lower-triangular in the eliminated coordinate, this is the same physical-coordinate Schur complement as for \(M_1\). No rotated-coordinate probability statement enters.

## 2. Exact second-pivot transport

Now split, still in the original remaining physical coordinates,

\[
S_0=\begin{pmatrix}s&c^T\\c&T_0^{\rm raw}\end{pmatrix},\qquad
D=\begin{pmatrix}r^T\\Z\end{pmatrix},\qquad s\ne0.
\]

Let

\[
T_0=T_0^{\rm raw}-\frac{cc^T}{s},\qquad
s_1=s+r^TK_1r,
\]

and assume \(s_1\ne0\). Define

\[
E=Z-\frac{cr^T}{s},\qquad
K_2=K_1-\frac{K_1rr^TK_1}{s_1}.
\]

Then after eliminating the second physical pivot from \(S_1\), the residual is

\[
\boxed{T_1=T_0+E K_2E^T.}\tag{2}
\]

The proof is the same one-pivot identity applied to \(S_0+D K_1D^T\). Thus arbitrary added spectral directions remain a finite-rank symmetric update after each real-coordinate elimination; no independent-convolution replacement is needed.

For a three-coordinate core, \(T_0=t_0\) and \(T_1=t_1\) are scalars and

\[
\boxed{\det M_1=a_1s_1t_1.}\tag{3}
\]

In particular, every number and magnitude of added global eigendirections is compressed, on a chosen physical triple, into the three pivot/residual quantities \(a_1,s_1,t_1\). The possible failure is explicit pivot or final-curvature cancellation, not hidden dependence after rotation.

## 3. Rank-one specialization and exact resonance coefficients

For \(H=\tau vv^T\), write \(v=(u,w)\) at the first pivot and

\[
d=w-(u/a)b.
\]

Then (1) becomes

\[
S_1=S_0+\kappa_1dd^T,
\qquad
\boxed{\kappa_1=\frac{\tau a}{a+\tau u^2}}.
\]

Writing \(d=(r,z)\) at the second pivot and \(e=z-(r/s)c\), (2) becomes

\[
T_1=T_0+\kappa_2ee^T,
\]

with

\[
\boxed{\kappa_2=\frac{\kappa_1s}{s+\kappa_1r^2}
=\frac{\tau as}{as+\tau(u^2s+ar^2)}}.\tag{4}
\]

Also

\[
\boxed{(a+\tau u^2)(s+\kappa_1r^2)
=as+\tau(u^2s+ar^2).}\tag{5}
\]

Thus a single added eigen-direction remains rank one through both Schur steps. Large \(|\tau|\) does not itself force instability; instability occurs only when a physical pivot denominator approaches a genuine cancellation.

## 4. Quantitative residual-reserve certificate

For general finite-rank addition, if

\[
\sigma_{\min}(T_0)\ge L,
\qquad
\|E\|_{\rm op}^2\,\|K_2\|_{\rm op}\le\delta<L,
\]

then Weyl's inequality applied to (2) gives

\[
\boxed{\sigma_{\min}(T_1)\ge L-\delta.}\tag{6}
\]

For a physical three-coordinate core, suppose moreover

\[
|a_1|\ge\alpha>0,\qquad |s_1|\ge\beta>0,
\qquad |t_0|\ge L,\qquad |e^TK_2e|\le\delta<L.
\]

Then \(|t_1|\ge L-\delta\), and by (3)

\[
|a_1\det M_1|=|a_1^2s_1t_1|
\ge \alpha^2\beta(L-\delta).\tag{7}
\]

## 5. Actual application of the completed account04/B12 theorem

Dependency actually consumed: account04/B12 `QFORM mixed-norm shear compiler`, canonical report

`yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e:proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260922T192552Z-account04-B12-mixed-shear-r1/REPORT.md`.

That theorem states that if `(U,Z)` has joint density \(h\), then for every measurable \(\psi\),

\[
\|p_{U+\psi(Z)}\|_\infty
\le \int \operatorname*{ess\,sup}_u h(u,z)\,dz,
\]

without requiring independence of \(U\) and \(Z\).

Apply it to an original-coordinate split \(X=(Y,Z)\), where \(Y\) is the protected physical triple and

\[
Q=Y^TM_1Y+2Y^TBZ+Z^TCZ.
\]

For fixed \(Z=z\), the arbitrary affine term \(2Y^TBz\) is covered by the completed orientation-free rank-two affine half-Riesz estimate after the first physical square is completed. It gives the uniform conditional cap

\[
\sup_z\|p_{Y^TM_1Y+2Y^TBz\mid Z=z}\|_\infty
\le128|a_1\det M_1|^{-1/4}.
\]

Therefore the joint mixed norm is bounded by the same number (the \(Z\)-density integrates to one), and the account04/B12 shear compiler adds the entire dependent outside quadratic remainder \(Z^TCZ\) without convolution. Combining with (7),

\[
\boxed{
\|p_Q\|_\infty
\le128[\alpha^2\beta(L-\delta)]^{-1/4}.
}\tag{8}
\]

This is the promised dependence-safe additional-eigenvalue inequality.

## 6. Arbitrarily large same-sign spectral sea is free

There is a useful unlimited-magnitude corollary. Suppose \(M_0\) is positive definite. If \(\Theta\succeq0\), then \(a_1\ge a>0\) and

\[
K_1=\Theta^{1/2}
\left(I-\frac{qq^T}{a+\|q\|^2}\right)
\Theta^{1/2}\succeq0,
\qquad q=\Theta^{1/2}u.
\]

Hence \(S_1\succeq S_0\), so \(s_1\ge s>0\); applying the same argument again gives \(K_2\succeq0\) and \(T_1\succeq T_0\). Thus all LDL pivots on this physical triple are monotone under an arbitrary-rank, arbitrarily large PSD addition. Consequently

\[
\boxed{
\|p_Q\|_\infty
\le128(a\det M_0)^{-1/4}
}
\]

continues to hold after adding any PSD spectral sea to the triple, with arbitrary outside completion. Reflection gives the identical statement for a negative-definite core plus arbitrary NSD addition.

More generally, if \(\varepsilon M_0\succeq LI_3\), an arbitrary sign-compatible sea satisfies \(\varepsilon H_{\rm good}\succeq0\), and a remaining arbitrary-sign compression obeys \(\|H_{\rm bad}\|_{\rm op}\le\delta<L\), then

\[
\varepsilon(M_0+H_{\rm good}+H_{\rm bad})\succeq(L-\delta)I_3.
\]

Therefore a physical pivot has magnitude at least \(L-\delta\), the determinant has magnitude at least \((L-\delta)^3\), and the partner-compiled local inequality yields

\[
\boxed{\|p_Q\|_\infty\le\frac{128}{L-\delta}.}\tag{9}
\]

For a global spectral decomposition of the bad part, \(H_{\rm bad}=\sum_r\tau_rv_rv_r^T\), its compression to the protected physical triple \(I\) obeys

\[
\|P_IH_{\rm bad}P_I\|_{\rm op}
\le\sum_r|\tau_r|\,\|(v_r)_I\|_2^2.
\]

Hence even arbitrarily large opposite-sign eigenvalues are harmless when their weighted physical leverage on the protected core is small; arbitrarily large sign-compatible eigenvalues cost nothing at all.

## 7. What remains unpaid

This does **not** derive such a protected triple from the bare hypothesis of only three global eigenvalues with modulus at least one. The singleton-plus-two-banks family still shows why selecting one physical triple and paying reciprocal local curvature can lose a factor growing with dimension. The remaining global bridge must aggregate diffuse banks or find a secure two-pivot branch before local reciprocal costs are paid.

The exact transport identities sharpen that bridge: once a physical two-pivot core is selected, all extra spectrum is represented by the explicit Möbius updates `K1,K2`; no statement that 'extra eigenvalues automatically help' is needed. Mixed-sign cancellation is visible as a pivot/final-reserve resonance and must be routed to a different physical block or aggregate mechanism.

## 8. Computation check

A direct symbolic check verifies the rank-one formulas exactly. A separate 500-trial floating-point check of the general finite-rank identities gave maximum operator-norm residuals approximately `1.73e-13` for (1) and `6.46e-13` for (2). In 500 SPD-plus-PSD trials the smallest eigenvalues of both observed Schur increments were nonnegative up to numerical precision (minimum observed first increment `4.58e-10`, second `7.44e-4`). These computations are checks only; the proof above is algebraic.

## Scope ledger

- Exact target quantifiers preserved: yes, in every stated conditional theorem.
- Original-coordinate independence preserved: yes.
- Added eigenvalues: arbitrary rank/sign/magnitude in the exact transport identities; unlimited sign-compatible seas plus small arbitrary-sign compressed tail in (9).
- Rotated remainder treated as independent convolution: no.
- Refuted pointwise decay/fiber-sup shortcuts used: no.
- Partner applied to an equation: account04/B12 mixed-norm shear theorem, producing (8) and (9).
- Essential boundedness: proved in the stated scopes.
- Continuity: not proved by this result.
- Full QFORM: OPEN.
- Native brain receiver use: not established; `WITHOUT_VERIFIED_BRAIN`.
