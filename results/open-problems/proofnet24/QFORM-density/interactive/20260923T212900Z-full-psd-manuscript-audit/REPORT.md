# Independent audit of the full semidefinite density theorem

**Status:** The published manuscript proof is sound under the stated hypotheses on this audit. This is an audit of a proved positive/negative semidefinite subcase, **not** a proof of the unrestricted mixed-sign conjecture.

## Source and statement

Source pinned at [manuscript/semidefinite.tex, Theorem sd:main](https://github.com/yspennstate/math-open-problems/blob/d6f59993e85da91da39942ae96d92481abbaf541/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/semidefinite.tex), blob SHA 2477f8adafb8219ef40be060ad8876ddcc2eed05. Supporting Fourier lemmas are in [manuscript/fourier.tex](https://github.com/yspennstate/math-open-problems/blob/d6f59993e85da91da39942ae96d92481abbaf541/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/fourier.tex).

If the original coordinates \(X_i\) are independent with densities at most one, \(A\succeq0\) has \(\lambda_3(A)>0\), and \(b,c\) are arbitrary, then \(Q=X^TAX+b^TX+c\) has an essentially bounded density with
\[
\|p_Q\|_\infty\le17100/\lambda_3(A).
\]
It covers **arbitrary rank** and affine components along \(\ker A\). Reflection gives the negative semidefinite case.

## Checks performed

1. **Physical positive pivot and spectral count.** For \(a=A_{ii}>0\), completion of the physical coordinate square gives \(Q=a(X_i-m(X_{-i}))^2+R(X_{-i})\). The Schur residual is PSD, its affine term is arbitrary, and its \((k-1)\)-st eigenvalue is at least \(\lambda_k(A)\). The latter follows from intersecting the top-\(k\) positive spectral subspace with the square-completion hyperplane. The conditional square kernel is at most \(a^{-1/2}|s-R|^{-1/2}\); the manuscript's square-root profile lemma composes it with concentration of \(R\).

2. **Three-level induction.** The manuscript first proves \(\alpha_1(Q)\le K_1=4\sqrt{128}\) under \(\lambda_1(A)\ge1\), then \(\alpha_2(Q)\le K_2=4\sqrt{600}\,K_1\) under \(\lambda_2(A)\ge1\), where \(\alpha_2\) is the \(u(1+\log(1/u))\) concentration norm. At level three, a diagonal \(a_{ii}\ge1/640\) leaves a PSD residual with \(\lambda_2\ge1\). The profile lemma yields
\[
\|p_Q\|_\infty
 \le3\sqrt{640}\sqrt{K_2(3+\log K_2)}
 =17061.1429\ldots<17100.
\]
The layer-cake bounds and logarithmic constants in these steps check out.

3. **Small-diagonal partition includes the full spectral tail.** Factor \(A=BB^T\) with \(B^TB=\Lambda\) containing **every nonzero eigenvalue**, not just the first three. Random signs define the two physical banks and \(N=\tfrac12\sum_i\eta_i b_ib_i^T\). The events \(\mathcal S,\mathcal E_1,\mathcal E_2\) control respectively the first-\(k\) cross singular value, the top-block Gram error, and the coupling to all remaining Gram coordinates. Their total failure probability is \((18k+64k^2)d/\theta\), below one for the manuscript's \(\gamma_1=128,\gamma_2=300,\gamma_3=640\). On the simultaneous event, \(s_k(A_{I,J})\ge\theta/4\), and the Gram/ridge comparison bounds every canonical \(k\)-minor row inclusion probability by \(64k d/\theta\le1/2\). I checked the singular-Gram limiting argument and the block matrix inequality used for the tail.

4. **Fourier volume receiver permits arbitrary affine terms and bank-local tails.** The source's decoupling lemma starts from \(Y=F(X_I)+2X_I^TMX_J+G(X_J)\), with arbitrary measurable \(F,G\). It squares the characteristic function using an independent copy of the \(J\) bank; the resulting independent difference densities have cap one. Cauchy-Binet and Gaussian Brascamp–Lieb give the weighted-minor determinant bound; scalar Hausdorff–Young applies because the row inclusion marginals are at most \(1/2\). For \(k=3\), Fourier inversion yields \(6\sqrt e\,Z_3^{-1/6}\le24\sqrt e/\theta\). For \(k=1,2\), the same receiver supplies the exact decay used by the concentration induction. Thus an affine term outside \(\operatorname{range}(A)\) remains inside arbitrary bank-local phases and is paid.

5. **Scaling and sign.** Apply the normalized proof to \(Q/\lambda_3(A)\); density scaling gives the stated denominator. The law of \(-Q\) handles NSD \(A\). No bound is asserted here for a general mixed-sign matrix.

## Remaining full-problem gap

The manuscript's separate absolute-spectral-spread theorem handles mixed-sign \(A\) when every diagonal entry of \(|A|\) is sufficiently small. The unrestricted mixed-sign case with a heavy spectral row remains open: a physical quadratic pivot can have small or zero scalar diagonal through cancellation of positive and negative spectral contributions. The PSD Schur concentration hierarchy therefore cannot be transplanted by replacing \(A\) with \(|A|\); doing so changes the quadratic form and its bank couplings.

This audit checked the algebra, constants, hypothesis flow, and the cited Fourier receiver in the manuscript. It was not a formal proof-assistant verification.
