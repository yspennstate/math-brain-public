SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B03, 2026-09-23T18:30:12Z.
attacking: a dependence-safe fractional-potential compiler for the exact sum/difference variables, followed by the first still-unpaid exponent endpoint.

# B03 r2 — dependent sum/difference fractional-budget compiler

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Assignment: \`Decoupled time integral\`  
Classification: **SUPPORTING_THEOREM PROVED / PARTNER RESULT APPLIED / ENDPOINT OBSTRUCTION IDENTIFIED / FULL TARGET OPEN**  
Execution: \`WITHOUT_VERIFIED_BRAIN\`.

The unrestricted conjecture remains open. Continuity is separate and is not claimed here.

## 1. Scope and corrections retained

Let \(X_1,\ldots,X_k\) be independent real random variables with probability densities bounded by one, and let \(X'\) be an independent copy. Put
\[
U_i=X_i-X_i',\qquad V_i=X_i+X_i'.
\]
The vectors \(U\) and \(V\) are generally dependent. I do not condition on one and assign a cap-one density to the other; that interface is refuted by \`QFORM-UV-CONDITIONAL-CAP-FALSE\`.

What is true is:
- the coordinates of \(U\) are mutually independent and each has density \(f_i*\widetilde f_i\le1\);
- the coordinates of \(V\) are mutually independent and each has density \(f_i*f_i\le1\);
- no independence between \(U\) and \(V\) is asserted or used.

The arbitrary-joint coarea bound, post-rotation independence, and law-uniform pointwise quadratic decay are not used.

## 2. Partner theorem actually applied

The completed partner result is account01/B03 r18:
\[
\texttt{proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/account01-B03-20260922T224814Z-r18/REPORT.md}.
\]
For independent cap-one \(Y_1,Y_2\), an invertible symmetric physical pair
\[
P=\begin{pmatrix}a&b\\b&c\end{pmatrix},\qquad D=|\det P|,
\]
and arbitrary affine terms, write \(m=\max(|a|,|c|)\). Uniformly in the translation \(s\), its theorem gives
\[
H_{1/2}(P):=\sup_s\mathbb E|Y^TPY+\ell^TY+d-s|^{-1/2}\le {\cal B}(P), \tag{2.1}
\]
where always
\[
{\cal B}(P)\le128D^{-1/4}, \tag{2.2}
\]
and, when \(m>0\),
\[
{\cal B}(P)\le8m^{-1/2}\left[3+2\log_+\!\left(\frac{2\sqrt2\,m}{\sqrt D}\right)\right]. \tag{2.3}
\]
Thus \({\cal B}(P)\) denotes the minimum of (2.2) and (2.3) when both are available.

## 3. Exact dependent Hölder lemma

For arbitrary nonnegative measurable \(F,G\) and conjugate exponents \(p,q\),
\[
\mathbb E[F(U)G(V)]
\le \bigl(\mathbb EF(U)^p\bigr)^{1/p}
   \bigl(\mathbb EG(V)^q\bigr)^{1/q}. \tag{3.1}
\]
This is Hölder on the actual joint law of \((U,V)\). No product replacement occurs.

Because the marginal densities of \(U\) and \(V\) are products of cap-one one-dimensional densities, also
\[
\mathbb E[F(U)G(V)]\le \|F\|_{L^p(\mathbb R^k)}\|G\|_{L^q(\mathbb R^k)} \tag{3.2}
\]
whenever the displayed norms are finite.

## 4. Dependent sum/difference fractional-budget theorem

Take invertible symmetric physical pairs \(P_-,P_+\) on two coordinates and arbitrary affine data:
\[
R_-(U)=U^TP_-U+\ell_-^TU+d_-,\qquad
R_+(V)=V^TP_+V+\ell_+^TV+d_+.
\]

**Theorem (\`QFORM-DEPENDENT-SUMDIFF-FRACTIONAL-BUDGET-v1\`).**
For every \(0\le\theta\le1\) and every \(s,t\in\mathbb R\),
\[
\boxed{
\mathbb E\!\left[
|R_-(U)-s|^{-\theta/2}
|R_+(V)-t|^{-(1-\theta)/2}
\right]
\le {\cal B}(P_-)^\theta{\cal B}(P_+)^{1-\theta}.
} \tag{4.1}
\]
In particular,
\[
\boxed{
\sup_{s,t}\mathbb E
|R_-(U)-s|^{-1/4}|R_+(V)-t|^{-1/4}
\le \sqrt{{\cal B}(P_-){\cal B}(P_+)}.
} \tag{4.2}
\]

**Proof.** For \(0<\theta<1\), apply (3.1) with \(p=1/\theta\), \(q=1/(1-\theta)\) to
\[
F=|R_--s|^{-\theta/2},\qquad G=|R_+-t|^{-(1-\theta)/2}.
\]
Then \(F^p=|R_--s|^{-1/2}\) and \(G^q=|R_+-t|^{-1/2}\). The \(U\)-coordinates are independent with densities at most one, so (2.1) applies to \(R_-(U)\); separately it applies to the marginal vector \(V\). This proves (4.1). The endpoints follow from (2.1), and \(\theta=1/2\) gives (4.2). \(\square\)

This is a genuine joint estimate on dependent sum/difference variables, not a product of marginal expectations.

## 5. Concrete target-level inequality from account01/B03

After conditioning on outside coordinates, suppose the active original-coordinate polynomial is
\[
Q=Y^TPY+\ell^TY+dZ^2+2eZ+c,
\]
where \(Y_1,Y_2,Z\) remain independent cap-one variables, \(P\) is invertible, and \(d\ne0\). Completing the square in \(Z\), the density \(g\) of \(dZ^2+2eZ\) obeys
\[
g(w)\le |d|^{-1/2}|w-w_0|^{-1/2}
\]
for almost every \(w\). Conditioning on \(Y\) and applying (2.1) gives
\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le |d|^{-1/2}{\cal B}(P)
\le128\,|d|^{-1/2}|\det P|^{-1/4}.
} \tag{5.1}
\]
All conditioning-generated affine terms are retained. Hence an actual principal block \(P\oplus[d]\), with both eigenvalues of \(P\) and \(d\) of modulus at least one, gives
\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}\le128.} \tag{5.2}
\]
This is an actual physical spectral gate, not a rank-three component plus an uncontrolled cancelling diagonal.

## 6. First remaining endpoint

Theorem (4.1) distributes a total singularity budget \(1/2\). It does not produce the \(1/2+1/2\) product. Applying Cauchy to that stronger product would require
\[
\mathbb E|R_\pm-r|^{-1},
\]
which is false in general. For cap-one inputs positive near zero and \(P=I_2\), the law of \(Y_1^2+Y_2^2\) has positive density at its lower endpoint, and the full Riesz integral diverges logarithmically. The missing half power cannot come from another formal Hölder step.

Thus (4.1) closes the dependency-safe \(1/4+1/4\) estimate after a balanced two-sided fractional split. The remaining B03 implication is to obtain the additional half power needed for an \(L^1\)-time estimate from genuine oscillatory cancellation or a third source-coordinate receiver. Marginal half-Riesz credit alone cannot supply it.

## 7. Status and sources

- Proved: exact joint fractional-budget estimate (4.1), preserving dependence of sums and differences.
- Applied: account01/B03 at the concrete density inequality (5.1).
- Not proved: a universal \(L^1\) Fourier bound for every three-large-eigenvalue matrix.
- Full QFORM conjecture: open.
- Continuity: not claimed.

Sources:
- Brain controls: fresh main and \`QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z\`.
- Required Claude base: \`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837\`.
- Current continuation checked: \`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md\`.
- Partner: account01/B03 r18 cited above.
