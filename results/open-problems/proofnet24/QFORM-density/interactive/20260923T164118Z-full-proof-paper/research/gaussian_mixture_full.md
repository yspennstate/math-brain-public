# Full arbitrary-rank quadratic-form bound for Gaussian mixture product laws

**Status:** complete supporting theorem. Two independent calculations checked the determinant expansion, inverse-scale averaging, affine terms, and constants. The unrestricted QFORM problem for arbitrary cap-one densities remains OPEN. No literature-wide novelty claim is made.

## Statement

Let

\[
X_i=M_i+\sqrt{T_i}G_i,
\qquad 0<T_i<\infty\ \text{almost surely},
\]

where the pairs \((M_i,T_i)\) are independent across coordinates, and the standard normal variables \(G_i\) are independent of all mixture data and of one another. Assume

\[
\mathbb E T_i^{-1/2}\le\sqrt{2\pi}.
\]

For any real symmetric matrix \(A\), any affine coefficients \(b,c\), and any integer \(3\le k\le\operatorname{rank}A\), put

\[
Z_k=e_k(A^2)=\sum_{|I|=|J|=k}\det(A_{IJ})^2.
\]

Then \(Q=X^TAX+b^TX+c\) has a bounded continuous density with

\[
\|p_Q\|_\infty\le I_k Z_k^{-1/(2k)},
\quad I_k=\int_0^\infty(1+u^{2k})^{-1/4}\,du
=\frac1{2k}\mathrm B\left(\frac1{2k},\frac14-\frac1{2k}\right)
<\frac{k}{k-2}.
\]

For \(k=3\), \(I_3=2.942468198\ldots<3\). If \(s_3(A)\ge1\), then \(Z_3\ge1\), so the complete three-eigenvalue conjecture holds with constant below three **for this input class**, with no rank, sign, dimension, or affine restriction.

## Complete proof

Condition on all mixture variables. Write \(D=\operatorname{diag}(T_i)\), \(B=D^{1/2}AD^{1/2}\), and \(\ell=D^{1/2}(2AM+b)\). Conditional on those variables, the polynomial is \(G^TBG+\ell^TG+c'\). Orthogonal diagonalization is legitimate for the standard Gaussian vector. One-dimensional Gaussian integration gives

\[
|\varphi_{Q\mid M,D}(t)|
=\prod_j(1+4t^2\mu_j^2)^{-1/4}
\exp\left[-\sum_j\frac{t^2\beta_j^2}{2(1+4t^2\mu_j^2)}\right]
\le\det(I+4t^2B^2)^{-1/4},
\]

where \(\mu_j\) and \(\beta_j\) are the diagonalized quadratic and linear coefficients. The formula includes zero eigenvalues. Since all coefficients in the determinant expansion are nonnegative,

\[
|\varphi_{Q\mid M,D}(t)|\le[1+(2t)^{2k}W_k]^{-1/4},
\qquad W_k=e_k(B^2)>0.
\]

For \(k>2\), this is integrable. Fourier inversion, followed by \(u=2tW_k^{1/(2k)}\), yields

\[
\|p_{Q\mid M,D}\|_\infty
\le\frac{I_k}{2\pi}W_k^{-1/(2k)}.
\]

Now apply Cauchy–Binet to the random scaled matrix. With \(T_I=\prod_{i\in I}T_i\),

\[
W_k=\sum_{|I|=|J|=k}\det(A_{IJ})^2T_I T_J.
\]

The pairs of subsets are ordered and may overlap. Normalize the nonzero coefficients into probability weights \(w_{IJ}=\det(A_{IJ})^2/Z_k\), and let

\[
\alpha_i=\sum_{I,J}w_{IJ}
\bigl(\mathbf1_{\{i\in I\}}+\mathbf1_{\{i\in J\}}\bigr).
\]

Then \(0\le\alpha_i\le2\) and \(\sum_i\alpha_i=2k\). Weighted arithmetic–geometric mean gives

\[
W_k\ge Z_k\prod_iT_i^{\alpha_i}.
\]

Independence across coordinates and Jensen's inequality for the power \(\alpha_i/k\le2/k<1\) give

\[
\begin{aligned}
\mathbb E W_k^{-1/(2k)}
&\le Z_k^{-1/(2k)}\prod_i\mathbb E(T_i^{-1/2})^{\alpha_i/k}\\
&\le Z_k^{-1/(2k)}\prod_i(\mathbb E T_i^{-1/2})^{\alpha_i/k}\\
&\le 2\pi Z_k^{-1/(2k)}.
\end{aligned}
\]

This factor cancels the \(2\pi\) in Fourier inversion. It also bounds the expectation of the conditional Fourier \(L^1\) norm, so Tonelli and conditional expectation give an integrable unconditional characteristic function. Therefore the density has a continuous bounded version, not merely an almost-everywhere bound.

The beta integral follows by \(v=u^{2k}\), and

\[
I_k<\int_0^1 1\,du+\int_1^\infty u^{-k/2}\,du=\frac{k}{k-2}.
\]

Finally, \(Z_3\ge s_1(A)^2s_2(A)^2s_3(A)^2\ge1\) in the normalized conjecture. This proves the claim.

## Which original input laws are covered?

For a Gaussian scale mixture about a deterministic center \(m_i\),

\[
f_i(x)=\mathbb E[(2\pi T_i)^{-1/2}e^{-(x-m_i)^2/(2T_i)}].
\]

Its essential maximum is attained in the limit at the common center and equals \((2\pi)^{-1/2}\mathbb E T_i^{-1/2}\), by monotone convergence. Thus the original cap-one hypothesis is exactly the displayed inverse-scale condition. The theorem covers all independent centered Gaussian scale mixtures with cap-one densities, including arbitrarily small component variances and laws without finite ordinary moments. Translated centered Laplace laws are examples.

For random component centers, the inverse-scale condition is sufficient for a density cap but is stronger than the cap. Many narrow separated components can produce a cap-one final density while their average peak is arbitrarily large. Arbitrary rough densities cannot therefore be inserted into the proof by an unrestricted Gaussian-mixture approximation. This is an explicit remaining gap, not a resolved approximation step.

The theorem is separate from the adapted-hub result: the latter allows a more general conditional hub law, whereas the present theorem applies to arbitrary matrices but requires the mixture condition on every original coordinate.

## Relation to other inputs

The Gaussian characteristic-function identity and Cauchy–Binet formula are classical. The argument above supplies the full average over random variances. Related primary literature includes Aizenman–Peled–Schenker–Shamis–Sodin, *Matrix regularizing effects of Gaussian perturbations* (2017), and Herry–Malicet–Poly, *Regularity of laws via Dirichlet forms: application to quadratic forms in independent and identically distributed random variables* (2025). Their distinct assumptions and conclusions are discussed in the manuscript's literature section. A limited literature search is not evidence of novelty.
