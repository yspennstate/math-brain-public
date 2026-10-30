# Source-exact transfer audit for the grouped Fourier estimate

Run: 20260924T181359Z-fleet04-B18-crosspaper-transfer-r1

Verdict: **PASS for the grouped Fourier and no-pivot branch.** The complete nine-eigenvalue theorem remains a candidate pending independent reconstruction of its pivot branches.

## Pinned mathematical sources

- Main candidate:
  proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex,
  commit eeb752c8943536541b34b42b8bf48e924f4d3d2f,
  blob 19fb119877426b640b2c0dae19ec2f78a399fe11,
  SHA-256 bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3.
  The relevant self-contained chain is lines 400--526.

- Separate reconstruction:
  proofnet24/QFORM-density/nine-eigenvalues-paper-2026-09-24/paper.tex,
  commit d3b12e27,
  blob 823201f05363fcc60c38cce0feb5abb636f081d7.
  The corresponding chain is lines 276--417.

- Separate reconstruction audit:
  blob af65f076e2c6c63a493c4f87f1d070b5f974a98a.

## Which literature results are actual proof dependencies?

The papers cite the geometric Brascamp--Lieb theorem of Ball and Barthe and identify the heat-flow tradition of Carlen--Lieb--Loss and Bennett--Carbery--Christ--Tao. They also discuss projection-density work of Rudelson--Vershynin and Livshyts--Paouris--Pivovarov.

For this candidate, however, those citations are contextual rather than hidden black-box dependencies:

1. The geometric Brascamp--Lieb inequality used here is reproved by heat flow in both manuscripts.
2. The cap-one projection-density bound
   \[
   \|p_{U^TX}\|_\infty\le e^{d/2}
   \]
   is derived directly from that reproved inequality.
3. The scalar Fourier-power estimate
   \[
   \int_{\mathbb R}|\widehat f(t)|^p\,dt
   \le\frac{2\pi\sqrt{2e}}{\sqrt p},\qquad p\ge2,
   \]
   is then derived from Plancherel, Fourier inversion, and the same projection bound.
4. The grouped Fourier theorem is proved from those ingredients, weighted Hölder, Gram determinants, and an elementary entropy inequality.

Thus the no-pivot branch does not silently require a sharper external projection theorem or independence after rotation.

## Transfer of the grouped estimate

Let \(h\) be the number of promoted physical hub rows, \(m\) the residual diffuse order, and \(q=h+m\). Candidate A proves

\[
 |\phi_Q(t)|
 \le
 B_{h,m}|t|^{-q/2},
\]

with

\[
 B_{h,m}
 =
 \pi^{q/2}2^{m/4}e^{(h+2m)/4}
 \omega(m)^{1/4}
 S^{-1/2}Z^{-1/4},
 \qquad
 \omega(m)=\frac{m^m}{m!}.
\]

In Reconstruction B, \(S^2=\Theta(H)\) and

\[
 Z=\frac{\Theta_q(H)}{\Theta(H)}.
\]

Consequently

\[
\begin{aligned}
 B_{h,m}^2
 &=
 \pi^q2^{m/2}e^{(h+2m)/2}
 \omega(m)^{1/2}S^{-1}Z^{-1/2}\\
 &=
 \pi^qe^{q/2}(2e)^{m/2}
 \omega(m)^{1/2}\Theta_q(H)^{-1/2}.
\end{aligned}
\]

This is exactly Reconstruction B's Lemma 4.3. The powers of \(2,\pi,e\), the entropy factor, the Fourier exponent, and both determinant factors agree identically.

Both manuscripts promote only literal original coordinates. After \(h\) promotions,

\[
 \Theta_q(H)>2^{-h}E_q(M).
\]

The mollified \(L^2\) estimate is uniform before passing to the limit. Neither proof takes a worst conditional-density supremum, and neither assumes that projected coordinates are independent.

## Application to the live no-pivot branch

For \(q=3\), both reconstructions give

\[
 C_3=3\sqrt2\,e\,(9/2)^{1/6}
 =14.818337662843\ldots.
\]

Under the no-pivot spectral branch,

\[
 V_3(A)\ge\left(\frac4{625}\right)^3,
 \qquad
 E_3(A_{I,J})\ge4^{-3}V_3(A)
 \ge\frac1{625^3}.
\]

Therefore

\[
 E_3(A_{I,J})^{-1/6}\le25
\]

and hence

\[
 \boxed{
 \|p_Q\|_\infty
 \le25C_3
 =370.458441571075\ldots<375.}
\]

This is a genuine application to the surviving matrix, not merely a comparison of theorem statements.

## Formalization boundary

The second package's AUDIT.md correctly records that Fourier inversion, geometric Brascamp--Lieb, the projection consequence, and Theorem 4.1 are not formalized in Lean. Finite entropy and constant sublemmas are formalized. The present PASS is therefore a mathematical source comparison and reconstruction, not a Lean certificate of the analytic theorem.

## Scope and remaining obligation

This transfer independently corroborates the grouped Fourier/heavy-row/no-pivot branch and finds no disagreement between the two papers there. It does not independently certify the diagonal-pivot or two-coordinate-pivot branches. It therefore does not yet supply the second complete end-to-end review required for the \(s_9\), constant-\(400\) theorem, and it says nothing new about \(s_8\) or the unrestricted three-eigenvalue conjecture.
