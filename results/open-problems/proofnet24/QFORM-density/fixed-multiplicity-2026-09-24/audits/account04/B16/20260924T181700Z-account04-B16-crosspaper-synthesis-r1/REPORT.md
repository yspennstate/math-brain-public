# B16 independent cross-paper synthesis: grouped Fourier endpoint

Status: **SCOPED AUDIT PASSED; NOT AN END-TO-END CERTIFICATION.**

## Pinned inputs

- Current objective: \`QFORM-FIXED-MULTIPLICITY-AUDIT-20260924\`, brain commit \`194c09609c2ce750efaa9634a0849b5a27ff651c\`.
- Candidate A: \`fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex\`, commit \`eeb752c8943536541b34b42b8bf48e924f4d3d2f\`, blob \`19fb119877426b640b2c0dae19ec2f78a399fe11\`.
- Independent reconstruction B: \`nine-eigenvalues-paper-2026-09-24/paper.tex\`, commit \`d3b12e27\`, blob \`823201f05363fcc60c38cce0feb5abb636f081d7\`.
- Detailed precursor audit: account04/B20 commit \`095406a7ce674ea11af6bf2f452dfa03854d479b\`.

## Exact comparison of the grouped Fourier constants

Let \(h\) be the number of promoted physical hubs, \(m\) the residual diffuse order, and \(q=h+m\). Candidate A obtains
\[
 B_{h,m}
 =\pi^{q/2}2^{m/4}e^{(h+2m)/4}\omega(m)^{1/4}
   S^{-1/2}Z^{-1/4}.
\]
Reconstruction B obtains
\[
 |\phi_Q(t)|^2
 \le
 \pi^q e^{q/2}(2e)^{m/2}\omega(m)^{1/2}
 \Theta_q(H)^{-1/2}|t|^{-q}.
\]
Their geometric quantities satisfy
\[
 S^2=\Theta(H),\qquad Z=\frac{\Theta_q(H)}{\Theta(H)}.
\]
Consequently
\[
 S^{-1}Z^{-1/2}=\Theta_q(H)^{-1/2}
\]
and, using \(q=h+m\),
\[
 B_{h,m}^2
 =
 \pi^q 2^{m/2}e^{(h+2m)/2}\omega(m)^{1/2}
 \Theta_q(H)^{-1/2}
 =
 \pi^q e^{q/2}(2e)^{m/2}\omega(m)^{1/2}
 \Theta_q(H)^{-1/2}.
\]
Thus the two independently written proofs agree exactly, including every factor of \(2,\pi,e\), the entropy factor, hub determinant, residual volume, and the decay exponent. This is a literal identity, not merely agreement up to a universal constant.

Both arguments promote only original input coordinates. Independence is invoked only for the original product law; no orthogonal change of variables is interpreted as preserving independence. The mollified \(L^2\) estimate is uniform before the limiting step.

## Application to the live no-pivot branch

The \(s_9(A)\ge1\) no-pivot reduction supplies
\[
 V_3\ge\left(\frac4{625}\right)^3.
\]
The random-cut identity gives
\[
 E_3(M)\ge4^{-3}V_3\ge\frac1{625^3},
 \qquad E_3(M)^{-1/6}\le25.
\]
The common grouped Fourier endpoint therefore yields
\[
 \|p_Q\|_\infty
 \le25C_3
 =25\cdot3\sqrt2\,e\left(\frac92\right)^{1/6}
 =370.458441571075\ldots<375.
\]
The promoted cases \(h=0,1,2,3\) have endpoint constants
\[
 14.818337662843,\quad
 10.957714649270208,\quad
 8.263535690265833,\quad
 6.9949319447913725,
\]
so the unpromoted case is the worst one.

## Sharp limitation of this mechanism

At total order \(q=2\), the exact endpoint constant is
\[
 C_2=8\sqrt e\,2^{-1/8}=12.095072570796486\ldots,
\]
but the Fourier decay is only
\[
 |\phi_Q(t)|\lesssim |t|^{-q/2}=|t|^{-1}.
\]
Absolute inversion then diverges logarithmically. Heavy-row promotion changes the constant but preserves \(q=h+m\); therefore no optimization of the admissible weights or promotion thresholds can turn this order-two mechanism into a density bound.

This is a method obstruction, not a counterexample to the three-eigenvalue conjecture. Lowering the certified spectral threshold below nine requires a genuinely new shared-coordinate receiver, not a better constant in the same grouped-Fourier estimate.

## Proof graph and remaining audit gates

The checked chain is
\[
 \text{product cap}
 \Longrightarrow
 \text{geometric Brascamp--Lieb projection cap}
 \Longrightarrow
 \text{scalar Fourier powers}
 \Longrightarrow
 \text{grouped physical-coordinate decay}
 \Longrightarrow
 \text{heavy-row promotion}
 \Longrightarrow
 E_3(M)^{-1/6}\le25
 \Longrightarrow
 \|p_Q\|_\infty<375.
\]

The following branches of the \(400K^2/s\) candidate were **not** reconstructed in this audit:

1. the diagonal scalar-pivot branch;
2. the definite physical-pair branch;
3. the indefinite physical-pair branch;
4. the final end-to-end maximum over all branches.

Accordingly this report supplies an independent audit of the no-pivot component and an exact explanation of why the same mechanism stops at order two. It is not the second complete end-to-end review requested for certification.

The accompanying reconstruction audit also records that the Brascamp--Lieb, projection, Fourier-inversion, and grouped-decay steps are not all formalized in Lean; formal certificates cover only selected finite entropy and constant computations. No formal-verification claim is made here.
