# Correction addendum — fleet04/B19 finite-carrier curved rank-two terminal

This immutable addendum corrects the malformed TeX serialization in REPORT.md at scientific commit bc051c30b5fefa64e93f96bc4cae12c03b426d6a. The original file is retained unchanged for provenance. Its mathematical intent is replaced by the literal formulas below.

Run: 20260924T091538Z-fleet04-B19-QFORM-r5  
Status: ESSENTIAL_STEP_APPLIED / NEW_TERMINAL_NODE / FULL_QFORM_OPEN  
Newest Claude source checked: b0cbc2233369b6a3f366cf569d425f485f123e1c  
Completed fleet01/B19 source used: 879ad8a0be00493b8a826558a993a45a6070f162  
Corrected fleet01/B18 source used: 43beacb57eba0134d9b4b4cf8b7843a4f119049c

## 1. Fleet01/B19 input and exact threshold application

For a nonzero literal scalar pivot \(a=A_{ii}\), let \(S\) be its exact Schur complement. Then

\[
s_2(S)\ge s_3(A)\ge 1.
\]

Define the Schur tetrad energy

\[
W_2(S)=
\sum_{\substack{|I|=|J|=2\\ I\cap J=\varnothing}}
\det S[I,J]^2.
\]

The completed aggregate receiver gives

\[
\|p_Q\|_\infty
\le
8\sqrt2\,e^{1/4}|a|^{-1/2}W_2(S)^{-1/8}.
\tag{1.1}
\]

At the live thresholds

\[
|a|\ge 2^{-12},
\qquad
W_2(S)\ge 2^{-32},
\]

equation (1.1) yields

\[
\boxed{
\|p_Q\|_\infty
\le
8\sqrt2\,e^{1/4}(2^{-12})^{-1/2}(2^{-32})^{-1/8}
<14{,}876.
}
\tag{1.2}
\]

This keeps all same-bank curvature, affine terms, signs, and additional spectrum.

At \(W_2(S)=0\), the rigidity conclusion is

\[
S=\Delta+R,
\qquad
\operatorname{rank}R\le2,
\]

with \(\Delta\) a physical diagonal matrix. If \(\|\Delta\|_{\mathrm{op}}<1/2\), the spectral target forces \(R\) to have rank two with both nonzero singular values \(>1/2\). The fleet01/B19 theorem then either pays the diffuse branch by

\[
\|p_Q\|_\infty
<
17.449\,|a|^{-1/2},
\tag{1.3}
\]

or localizes the remaining obstruction to at most six literal coordinates.

## 2. Corrected finite-carrier curved rank-two terminal

Let \(I,J,\{w\}\) be disjoint sets of literal original coordinates. Suppose the retained coefficient packet is

\[
A_R=
\begin{pmatrix}
0&B&0\\
B^\top&C&h\\
0&h^\top&a
\end{pmatrix},
\qquad
R=I\sqcup J\sqcup\{w\},
\tag{2.1}
\]

where \(C=C^\top\) and \(h\) are arbitrary, \(a\ne0\), and \(B\) has singular values

\[
\sigma_1\ge\sigma_2>0.
\]

All coefficients involving outside coordinates may be arbitrary.

### Theorem — QFORM-FINITECARRIER-CURVED-R2-TERMINAL-v1

The full ambient quadratic form has a density and

\[
\boxed{
\|p_{X^\top AX}\|_\infty
\le
\min\left\{
\frac{2\sqrt\pi}{\sqrt{\sigma_1\sigma_2}},
\frac{4\sqrt2}{\sqrt{|a|\sigma_1}}
\right\}.
}
\tag{2.2}
\]

### Proof

Condition only on the outside original coordinates. The retained polynomial becomes

\[
2X_I^\top B X_J+\alpha^\top X_I+G(X_J)
+aX_w^2+\rho(X_J)X_w+c,
\tag{2.3}
\]

where \(G\) contains the entire \(J\)-bank curvature \(X_J^\top C X_J\), while \(\rho\) contains the genuine \(J\)-\(w\) coupling and conditioned outside-\(w\) couplings. Hence every conditioning weight is retained.

Apply the corrected fleet01/B18 one-sided-curvature theorem with \(j=2\). Since the two-dimensional unit-ball volume is \(v_2=\pi\),

\[
C_2(B)
=
\frac{2}{1}v_2^{1/2}(\sigma_1\sigma_2)^{-1/2}
=
\frac{2\sqrt\pi}{\sqrt{\sigma_1\sigma_2}}.
\tag{2.4}
\]

Its private-square branch gives the second term in (2.2). Both estimates are uniform in the conditioned outside values, so averaging proves (2.2). No rotated independence is used.

At

\[
\sigma_1\sigma_2\ge2^{-12},
\]

the theorem gives

\[
\boxed{
\|p_Q\|_\infty
\le128\sqrt\pi
=226.874\ldots .
}
\tag{2.5}
\]

At the alternative gate

\[
|a|\sigma_1\ge2^{-12},
\]

it gives

\[
\boxed{
\|p_Q\|_\infty
\le256\sqrt2
<362.039.
}
\tag{2.6}
\]

The exact zeros in the \(I\)-\(I\) and \(I\)-\(w\) blocks are hypotheses, not perturbative conveniences. Small nonzero replacements are not discarded.

## 3. Noncircular insertion and remaining leaves

The endpoint \(W_2(S)=0\), \(\|\Delta\|_{\mathrm{op}}<1/2\) first invokes the exact diagonal-plus-rank-two rigidity theorem. Its diffuse branch ends at (1.3); its nondiffuse branch localizes to at most six literal coordinates. Only after that localization is Theorem (2.2) invoked, and only when the finite carrier exposes the exact packet (2.1). Thus no node relies on a downstream conclusion.

The still-open leaves are:

- quantitative \(0<W_2(S)<2^{-32}\) stability without a strong-triangle witness;
- genuinely tiny or zero scalar pivots requiring a hub-star/third-resource compiler;
- finite carriers lacking the exact zero-self-side geometry (2.1);
- the shared-bank convex/two-sheet collar.

The full QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED. No full-candidate review is requested because these leaves remain.
