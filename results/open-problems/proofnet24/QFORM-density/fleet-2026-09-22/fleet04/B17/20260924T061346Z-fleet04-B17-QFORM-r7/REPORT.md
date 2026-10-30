# fleet04/B17 r7 — fold-aligned near-singular witness is uniformly bounded

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Run: \`20260924T061346Z-fleet04-B17-QFORM-r7\`  
Status: \`ESSENTIAL_STEP_APPLIED / ANALYTIC STRESS FAMILY BOUNDED / FULL TARGET OPEN\`

The full universal conjecture is not proved or disproved here. This report changes the witness mechanism from separated symmetric-unimodal banks to a shared-bank, exactly fold-aligned, near-singular physical pair. The calculation is analytic; no histogram, moment assumption, support enlargement, or independence after rotation is used.

## 1. Source-pinned motivation

The Claude baseline is \`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837\`; the later hub continuation \`c4c23b784395630c094ba299a50712209921d1ae\` is numerical evidence only and is not used as a theorem.

The completed fleet01/B17 theorem is \`QFORM B17 — arbitrary cap-one singleton plus two distinct symmetric-unimodal rank-one banks\`, path

\`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/QFORM-B17-20260923T060424Z-r15/REPORT.md\`.

It gives the actual inequality
\[
 \|p_Q\|_\infty\le C_{\rm sep}
 =3.8172923460947289\ldots<3\sqrt2
\tag{1.1}
\]
for the separated singleton-plus-two-rank-one-bank architecture. Thus a new adversarial test must leave that architecture. The family below does so by putting the fold-aligning correction on the same original-coordinate bank as a rank-two cross interaction.

The exact degenerate curved receivers motivating this test are fleet01/B06 r48,
\`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260924T060138Z-fleet01-B06-QFORM-r48/REPORT.md\`.
Their rank-one estimate contains an apparent inverse square root of the nonzero physical eigenvalue. The question is whether that loss is real after the full product weight is retained.

## 2. The fold-aligned target family

Let
\[
 X,Y,U,V\stackrel{\rm independent}{\sim}{\rm Unif}[-1/2,1/2],
\]
so all four input densities are normalized and bounded by one. For \(0<\theta\le1\), set
\[
 Q_\theta
 =\theta X^2+2XU+\theta^{-1}U^2+2YV.
\tag{2.1}
\]

The coefficient matrix in the original coordinate order \((X,Y,U,V)\) is
\[
 A_\theta=
 \begin{pmatrix}
 \theta&0&1&0\\
 0&0&0&1\\
 1&0&\theta^{-1}&0\\
 0&1&0&0
 \end{pmatrix}.
\tag{2.2}
\]

After merely permuting coordinates, not rotating the input law, this is the direct sum
\[
 \begin{pmatrix}\theta&1\\1&\theta^{-1}\end{pmatrix}
 \oplus
 \begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The first block has determinant zero and trace \(\theta+\theta^{-1}\); the second has eigenvalues \(1,-1\). Therefore
\[
 \boxed{\operatorname{spec}_{\ne0}(A_\theta)
 =\{\theta+\theta^{-1},1,-1\}.}
\tag{2.3}
\]
Every member of the family satisfies the original target hypothesis with three absolute eigenvalues at least one.

Completing the square gives the exact fold alignment
\[
 Q_\theta=S_\theta^2+T,\qquad
 S_\theta=\sqrt\theta\,X+\theta^{-1/2}U,\qquad
 T=2YV,
\tag{2.4}
\]
and \(S_\theta\) is independent of \(T\).

## 3. Exact component densities

Because \(\theta^{-1/2}U\) is uniform on an interval of length \(\theta^{-1/2}\), with density \(\sqrt\theta\), convolution with the probability density of \(\sqrt\theta X\) gives
\[
 \boxed{\|p_{S_\theta}\|_\infty\le\sqrt\theta.}
\tag{3.1}
\]
The law is symmetric. Hence the density of \(W_\theta=S_\theta^2\) satisfies, for \(w>0\),
\[
 p_{W_\theta}(w)
 =\frac{p_{S_\theta}(\sqrt w)+p_{S_\theta}(-\sqrt w)}{2\sqrt w}
 \le\frac{\sqrt\theta}{\sqrt w}.
\tag{3.2}
\]

A direct product calculation gives
\[
 p_T(t)=
 \log\frac1{2|t|}\,
 \mathbf 1_{\{0<|t|<1/2\}}.
\tag{3.3}
\]
Indeed \(YV\) has density \(2\log(1/(4|z|))\) on \(|z|<1/4\), and \(T=2YV\).

Define
\[
 f(w)=w^{-1/2}\mathbf1_{\{w>0\}},\qquad
 k(t)=\log\frac1{2|t|}\mathbf1_{\{0<|t|<1/2\}}.
\]
Then
\[
 p_{Q_\theta}(q)
 \le\sqrt\theta\int_0^\infty f(w)k(q-w)\,dw.
\tag{3.4}
\]

## 4. Uniform convolution estimate

If \(q\le1\) and the integrand in (3.4) is nonzero, then \(0<w<3/2\). Hölder with exponents \(3/2\) and \(3\) gives
\[
 \int_0^\infty f(w)k(q-w)\,dw
 \le
 \|w^{-1/2}\mathbf1_{(0,3/2)}\|_{3/2}\|k\|_3.
\tag{4.1}
\]
The two norms are explicit:
\[
 \int_0^{3/2}w^{-3/4}\,dw=4(3/2)^{1/4},
\tag{4.2}
\]
and, using \(u=2t\),
\[
 \int_{-1/2}^{1/2}
 \left(\log\frac1{2|t|}\right)^3dt
 =\int_0^1(-\log u)^3du=6.
\tag{4.3}
\]
Consequently the right side of (4.1) is
\[
 [4(3/2)^{1/4}]^{2/3}6^{1/3}=2\sqrt6.
\tag{4.4}
\]

If \(q>1\), nonzero integrand forces \(w>q-1/2>q/2\), whence
\[
 \int_0^\infty f(w)k(q-w)\,dw
 \le\sqrt{\frac2q}\int_{\mathbb R}k(t)\,dt
 \le\sqrt2,
\tag{4.5}
\]
because \(\int k=1\).

Combining (3.4), (4.4), (4.5), and \(\sqrt\theta\le1\) proves
\[
 \boxed{\|p_{Q_\theta}\|_\infty\le2\sqrt6
 =4.898979485566356\ldots}
\qquad(0<\theta\le1).
\tag{4.6}
\]

## 5. Consequence for the live proof strategy

The family (2.1) was designed to maximize the feared mechanism:

- the literal physical pair is rank one;
- its nonzero eigenvalue tends to zero in the \(X\)-coordinate description;
- the same-bank term \(\theta^{-1}U^2\) exactly aligns the conditional fold;
- the remaining physical cross interaction has a logarithmic product singularity.

Nevertheless the full product weight yields the uniform bound (4.6). Thus the \(\theta^{-1/2}\) loss in a worst conditional parabolic estimate is not, by itself, evidence for a counterexample. Aggregate curvature must be integrated before inversion.

This does not establish a general near-singular receiver: the proof uses the exact rank-one square identity and the explicit uniform laws. It rules out this analytic adversarial family only. The remaining witness search must introduce fragmentation/asymmetry in the shared bank or a nonseparable spectral tail while retaining an exact lower-bound certificate.

Continuity is separate from the target claim and is not used in the conclusion.
