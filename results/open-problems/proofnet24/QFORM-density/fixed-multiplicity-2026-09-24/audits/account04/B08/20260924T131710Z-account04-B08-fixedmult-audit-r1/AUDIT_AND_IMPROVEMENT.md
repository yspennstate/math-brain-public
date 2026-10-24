# account04/B08 independent fixed-multiplicity audit and constant improvement

Run: \`20260924T131710Z-account04-B08-fixedmult-audit-r1\`  
Objective: \`QFORM-FIXED-MULTIPLICITY-AUDIT-20260924\`

## Source pin and scope

I audited the 790-line candidate
\`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex\`
at blob \`183ccd294763214e6a707e8d4749ff9a8cf7006d\`, SHA-256
\`9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69b89591a4107e785340f65e69\`.

Correction: the repeated SHA-256 above has an accidental duplicated suffix. The canonical source pin used throughout this audit is

\`9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69\`.

The theorem audited is the fixed-multiplicity statement
\[
s_{17}(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10000\,K^2/s
\]
for arbitrary dimension, arbitrary real symmetric \(A\), arbitrary affine terms, and independent real coordinate laws with density caps \(K\). This is not the unrestricted three-eigenvalue conjecture.

## Verdict

**PASS.** I found no mathematical gap or false statement in an independent end-to-end read. The product-Fourier determinant receiver, the diffuse/original-coordinate crossing construction, the finite-dimensional interpolation step, every pivot branch, and the final scaling all retain their stated hypotheses. No rotation of the input product measure is used.

The advertised reproducibility package is now present on fresh master. I checked that \`verify.py\` pins the same manuscript SHA-256 and that \`checks.json\` records PASS with 534 exact interpolation seeds, 18 exact volume-sampling cases, 9 strict cases, exact diagonal-dominance slack \(297/2800\), 240 Schur threshold diagnostics, and 30 graph-weight diagnostics. These computations supplement but do not replace the written proof.

## Independent end-to-end checks

- Fourier inversion, Gaussian regularization, Plancherel, and the Riesz negative-half-moment identity have the correct \(2\pi\) normalizations.
- The projection-density theorem is applied only through deterministic changes of variables in integrals. It never asserts independence after an orthogonal rotation.
- Decoupling is performed in the original coordinate product law. The independent differences \(D_j=X_j-X'_j\) retain density cap one.
- In the graph Brascamp--Lieb step,
  \[
  H=\alpha I+a^2M^TM,\quad
  c_j=\alpha e_j^TH^{-1}e_j,\quad
  d_i=a^2m_i^TH^{-1}m_i
  \]
  form the required rank-one frame, with
  \[
  \theta=\sum_i d_i=\sum_j(1-c_j).
  \]
  The \(d_i\)-powers cancel, the \(c_j\)-entropy factor is at most \(e^{\theta/2}\), and \(\sqrt\alpha=2\pi e\) cancels the scalar Fourier constants. Taking fourth roots gives exactly
  \[
  |\phi_Z(t)|
  \le
  \det\!\left(I+\frac{t^2M^TM}{\pi^2e^2}\right)^{-1/8}.
  \]
- Cauchy--Binet gives the stated \(Z_k(M)\). Retaining the \(k\)-th coefficient produces the exponent \(k/4\); \(k=5\) gives an integrable characteristic-function envelope, while \(k=3\) gives the weighted negative-half-moment receiver. The manuscript does not conflate these endpoints.
- The square, definite-pair, and hyperbolic-pair formulas are conditional domination statements, not false conditional-density suprema. Dependence of the hyperbolic critical value on the conditioned variables is handled through nonnegative test functions and Tonelli.
- The nonsymmetric interpolation matrix has the two distinct ranks actually used: global rank at most \(3r\) and outside-seed rank at most \(r\). The exact strict-diagonal-dominance gap is
  \[
  \frac{371}{400}-\frac{23}{28}=\frac{297}{2800}>0.
  \]
- The main proof's branch constants and the rescaling \(Y=KX\), \(\widetilde Q=(K^2/s)Q\) are correct.

## Certified improvement: \(10000\) can be replaced by \(4340\)

The same proof, without changing any hypothesis, yields
\[
\boxed{\ \|p_Q\|_\infty<4340\,K^2/s.\ }
\]

### 1. Quarter-power coefficient

The exact coefficient in the Gaussian small-ball calculation is
\[
C_*=2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8).
\]
Elementary rational estimates give
\[
\Gamma(3/8)<\frac{73}{24},\qquad
2^{5/8}<\frac{25}{16},\qquad
\pi^{-1/4}<\frac45,\qquad
e^{3/8}<\frac32,
\]
hence
\[
C_*<\frac{365}{64}.
\]
For completeness: \(\Gamma(3/8)\le8/3+e^{-1}<73/24\);
\(32\cdot16^8<25^8\);
\(\pi>3>(5/4)^4\); and \(e<11/4\) implies
\(e^3<(3/2)^8\).

The sixth Taylor polynomial at \(7/4\) gives
\[
e^{7/4}>
\frac{16933657}{2949120}
>
\frac{365}{64},
\]
so layer cake improves the logarithmic potential constant to
\[
L_0'=4+4\log(365/64)<11.
\]

### 2. Exact far-region kernel coefficient

The proof of the elementary kernel lemma already establishes
\[
J(d)\le 8+2\sqrt2\,\log_+(1/|d|),
\]
because its far-region integral is
\(2\sqrt2\log_+(1/(2|d|))\); replacing \(2\sqrt2\) by \(3\) was only a rounding.

Therefore the scalar-pivot truncated half-potential is
\[
H(Q)
\le10\bigl(8+2\sqrt2\,L_0'\bigr)
<10(8+33)=410.
\]

### 3. The actual bottleneck is the indefinite-pair half-potential

The definite-pair branch remains below \(160\). In the indefinite-pair branch,
\[
H(Q)\le10(32+4\log16)+4/e.
\]
The rational bounds
\[
\log16<\frac{2773}{1000},
\qquad
\frac4e<\frac{184}{125}
\]
give
\[
H(Q)<\frac{54049}{125}=432.392<433.
\]
The first inequality is certified by the degree-ten Taylor polynomial:
\[
\sum_{j=0}^{10}\frac{(2773/1000)^j}{j!}-16
=
\frac{15125627502992708519531771781388649}
{3628800000000000000000000000000000000}>0.
\]
The second follows from
\(\sum_{j=0}^{6}1/j!=1957/720>125/46\).

Consequently every pivot with \(s_2(A)\ge1\) has \(H(Q)<433\).
The no-pivot \(s_9\) branch is already below \(200\), so the full half-potential in the nine-direction receiver is
\[
\sup_a\mathbb E|Q-a|^{-1/2}<434.
\]
A scalar pivot in the main \(s_{17}\) theorem therefore gives
\[
\|p_Q\|_\infty<10\cdot434=4340.
\]
The remaining main branches are smaller: the no-pivot branch is below \(2400\), the definite-pair branch below \(40\), and the indefinite-pair density branch is below \(199\) after \(L_0'<11\). Scaling restores \(4340K^2/s\).

## Finite method-barrier witness

For a diagonal crossing matrix
\[
M=\operatorname{diag}(\sigma_1,\ldots,\sigma_k),
\]
the determinant receiver is exactly
\[
\prod_{j=1}^k
\left(1+\frac{t^2\sigma_j^2}{\pi^2e^2}\right)^{-1/8},
\]
and
\[
Z_r(M)=\sum_{j_1<\cdots<j_r}
\sigma_{j_1}^2\cdots\sigma_{j_r}^2.
\]
Thus the \(k/4\) exponent obtained by retaining the top determinant coefficient is exact for this receiver. At \(k=4\) it is only \(|t|^{-1}\), which is not integrable. This is a concrete finite witness that the present unweighted Fourier endpoint alone cannot lower the unconditional multiplicity threshold; an additional structural or oscillatory input would be required.

## Status

The fixed-multiplicity theorem survives this independent review and admits the certified constant \(4340K^2/s\). The unrestricted three-eigenvalue conjecture remains open.
