SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B14, 2026-09-24T10:16:06Z.
attacking: recycle the active translation bank as a conditioning environment while retaining three literal cap-one anchors.

# Anchor recycling with arbitrary dense translation-bank curvature

Programme: QFORM-DENSITY-3EIG-20260922. Status: NEW TARGET-VALID CHAMBER / FULL QFORM OPEN. Execution: WITHOUT_VERIFIED_BRAIN.

## 1. The theorem

Let \(A=(A_1,A_2,A_3)\) have independent real coordinates with densities bounded by one. Let \(T\in\mathbb R^m\) consist of any further independent cap-one original coordinates, independent of \(A\). Put
\[
B_*=I_3-\frac23{\bf1}{\bf1}^T,
\qquad \operatorname{spec}(B_*)=\{1,1,-1\}.
\]
For arbitrary real matrices
\[
L,C\in\mathbb R^{3\times m}
\]
and arbitrary symmetric \(D\in\mathbb R^{m\times m}\), define the generally dependent translated active vector
\[
S=A+LT
\]
and the quadratic form
\[
Q=S^TB_*S+2S^TCT+T^TDT.
\tag{1.1}
\]
Then
\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}\le6\sqrt\pi.
}
\tag{1.2}
\]
Equivalently,
\[
\boxed{
\Pr(Q\in I)\le6\sqrt\pi\,|I|
}
\tag{1.3}
\]
for every interval \(I\).

The matrices \(L,C,D\) are unrestricted. In particular:

- all three entries of \(S\) may share every coordinate of \(T\), so the \(S_r\) need not be independent;
- \(D\) gives arbitrary dense, signed self-coupling inside the translation bank;
- \(C\) gives arbitrary dense coupling between the translated active variables and that same bank;
- the laws may have fragmented or unbounded support and need no moments;
- no independence after rotation is asserted.

This is an essential-density statement. Continuity is separate.

## 2. Proof: expand before conditioning

A direct application of an independent-\(S_r\) theorem would be invalid because the common \(LT\) makes the coordinates of \(S\) dependent. Instead expand (1.1) in the literal anchors:
\[
\begin{aligned}
Q
&=A^TB_*A
 +2A^T(B_*L+C)T\\
&\quad
 +T^T\!\left(
 L^TB_*L+L^TC+C^TL+D
 \right)T.
\end{aligned}
\tag{2.1}
\]
Condition on the original translation bank \(T=t\). The three literal anchors remain independent with density caps at most one, and the conditional polynomial is
\[
A^TB_*A+b(t)^TA+c(t),
\tag{2.2}
\]
where
\[
b(t)=2(B_*L+C)t
\]
and \(c(t)\) is an arbitrary measurable scalar field.

The completed affine reflection compiler used in fleet01/B14, with its current source at
\[
\texttt{c922f454adab32b0966d19d2e32794c6bbf8173d},
\]
gives uniformly in every affine field
\[
\Pr\!\left(A^TB_*A+b(t)^TA+c(t)\in I\mid T=t\right)
\le6\sqrt\pi\,|I|.
\tag{2.3}
\]
Integrating (2.3) in \(t\) proves (1.3), hence (1.2).

The important point is provenance: \(T\) is not declared independent of \(S=A+LT\). It is independent only of the literal anchors \(A\), which are the variables left active after (2.1).

## 3. Exact spectral verification

In the original coordinates \((A,T)\), the matrix of \(Q\) is
\[
\mathcal A=
\begin{pmatrix}
B_* & B_*L+C\\
L^TB_*+C^T &
L^TB_*L+L^TC+C^TL+D
\end{pmatrix}.
\tag{3.1}
\]
Its principal compression to the three anchor coordinates is exactly \(B_*\). Therefore Cauchy interlacing gives
\[
\lambda_2(\mathcal A)\ge1,
\qquad
\lambda_{\min}(\mathcal A)\le-1.
\tag{3.2}
\]
Thus \(\mathcal A\) has at least two positive eigenvalues at least one and at least one negative eigenvalue of modulus at least one. Every form in (1.1) lies inside the owner's exact full-target class, for every choice of \(L,C,D\).

This is an actual final-matrix spectral gate. It does not rely on a rank-three component whose spectrum could be canceled by a diagonal or dense perturbation.

## 4. Zero-tax finite or countable localization

Let \((q_j)_j\) be any finite or countable soft positive localization of the full translation-bank law:
\[
0\le q_j(t)\le1,\qquad \sum_jq_j(t)=1.
\]
Let \(m_j=\mathbb E q_j(T)\). Applying (2.3) to the unnormalised parameter measure \(q_j(t)\,d\mu_T(t)\) gives
\[
\boxed{
\Pr(Q\in I;\,j)
\le6\sqrt\pi\,m_j|I|.
}
\tag{4.1}
\]
Summing over \(j\) returns (1.3) exactly. Hence arbitrary distant fragments, remote combs, unbounded cells, and countably many pieces incur no localization tax.

This is the concrete finite-mixture reduction requested in the B14 assignment. It does not assume an interval extremizer. It uses positivity and the mass-linear affine reflection compiler.

The newest fleet01/B14 anchor-convolution theorem gives the same mass proportionality when a translated scalar is first represented as an untouched cap-controlled anchor convolved with a localized additive bank. The present theorem advances that result by allowing the three translated scalars to share the same bank and become dependent: one expands to the literal anchors before invoking the compiler.

## 5. Arbitrary measurable translation fields

Linearity of \(LT\) is not essential to the analytic step. Let \(\ell:\Omega\to\mathbb R^3\), \(r:\Omega\to\mathbb R^3\), and \(h:\Omega\to\mathbb R\) be arbitrary measurable functions of an independent environment \(T\). Then
\[
Q=(A+\ell(T))^TB_*(A+\ell(T))
 +r(T)^T(A+\ell(T))+h(T)
\tag{5.1}
\]
also obeys
\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}\le6\sqrt\pi.}
\tag{5.2}
\]
Indeed, conditioning on \(T\) again leaves \(A^TB_*A\) plus an arbitrary affine field. Formula (1.1) is the homogeneous quadratic-form specialization that also certifies the three-large-eigenvalue target.

## 6. What this resolves and what it does not

The theorem removes a genuine dependence obstruction in the anchor chamber:

- shared translations do not have to preserve independence of the translated active scalars;
- arbitrary dense quadratic curvature in the entire translation bank remains inside \(c(T)\);
- all kernel leakage into the anchor directions remains explicitly in \(b(T)\);
- fragmented and unbounded supports require no truncation or moment argument.

The unrestricted conjecture remains open because a general symmetric matrix with \(s_3(A)\ge1\) need not contain a literal three-coordinate principal reflection block \(B_*\), nor an equivalent product-preserving anchor representation. The first unpaid structural implication is to extract such an anchored block, or force another already-paid physical-fiber, pivot-crossing, grouped-bank, ridge, or Schur exit.

## 7. Source pins

- Owner/control revision: 2026-09-22.15 from fresh math-research-brain main.
- Current continuation: QFORM-CLAUDE-LATEST-20260922T225732Z.
- Newest completed fleet01/B14 anchor-convolution localization: math-open-problems commit c922f454adab32b0966d19d2e32794c6bbf8173d.
- Its designated affine reflection compiler: fleet02/B14 commit cd7154f14613325003b6346235701b8f067856a1.
- Previous fleet04/B14 scaled Schur localization: commit deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513.
- Previous fleet04/B14 atomless-boundary regularity: commit 10e3c2c60076516744368c00a83bb2f27c908298.

Repository publication is not native learned-memory ingestion. Unexposed model and thinking metadata remain UNKNOWN.
