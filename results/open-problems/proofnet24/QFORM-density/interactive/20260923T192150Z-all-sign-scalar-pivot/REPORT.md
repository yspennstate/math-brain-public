# All-sign, all-rank scalar-pivot exit from the two-eigenvalue potential theorem

**Status:** Proved scoped corollary of two already assembled analytic estimates. This does not settle matrices lacking a quantitative original-coordinate pivot. It works for arbitrary rank, inertia, independent cap-one coordinate laws, and arbitrary affine terms.

## Theorem

Let A be any real symmetric matrix with s_3(A)>=sigma>0. Let X_i be independent with Lebesgue probability densities at most one. If some ORIGINAL coordinate i has nonzero diagonal entry a=A_ii, then for every b,c the random variable
\[
Q=X^{\mathsf T}AX+b^{\mathsf T}X+c
\]
has a density satisfying
\[
\|p_Q\|_\infty
\le \frac{C_*}{\sqrt{|a|\sigma}},\qquad
C_*:=1+44(10^{-15})^{-1/2}
=1.391402171\ldots\times10^9. \tag{1}
\]
Thus if s_3(A)>=1 and |a|>=delta>0, then \|p_Q\|_\infty<=C_*/sqrt(delta). No semidefinite or minority-sign assumption is made.

## The unconditional two-eigenvalue half-potential input

For any symmetric M with s_2(M)>=1 and arbitrary affine terms, write
\[
{\cal H}(R)=\sup_s\mathbb E\bigl[
 |R-s|^{-1/2}\mathbf1_{\{|R-s|\le1\}}\bigr].
\]
The assembled manuscript proves:

* If M has no c_*=10^{-15} pivot, Theorem lower:two of lower_levels.tex gives H(R)<=10^6.
* If M has a c_* pivot, Lemma pivot-half of structure.tex gives H(R)<=44 c_*^{-1/2}. A c-pivot is either an ORIGINAL diagonal of magnitude at least c or an ORIGINAL principal two-coordinate determinant of magnitude at least c.

These are exhaustive and neither requires a sign or rank restriction. Therefore
\[
\sup_s\mathbb E|R-s|^{-1/2}
\le 1+{\cal H}(R)
\le C_* \quad\hbox{if }s_2(M)\ge1. \tag{2}
\]
For s_2(M)>=sigma>0, apply (2) to R/sigma to get
\[
\sup_s\mathbb E|R-s|^{-1/2}\le C_*/\sqrt\sigma. \tag{3}
\]
Arbitrary affine coefficients scale along with the quadratic matrix and are allowed by both source theorems.

## Proof of (1)

Move i to the first coordinate and write
\[
A=\begin{pmatrix}a&v^{\mathsf T}\\v&D\end{pmatrix},
\qquad
S=D-\frac{vv^{\mathsf T}}a.
\]
The exact rank-one decomposition is
\[
A=
\frac1a\binom{a}{v}\begin{pmatrix}a&v^{\mathsf T}\end{pmatrix}
+
\begin{pmatrix}0&0\\0&S\end{pmatrix}. \tag{4}
\]
The first summand has rank one. The singular-value rank-one perturbation inequality, or its minmax proof, gives
\[
s_2(S)\ge s_3(A)\ge\sigma. \tag{5}
\]
Equation (5) holds for arbitrary signs and singular S, without treating spectral coordinates as independent.

Complete the square only in the original coordinate X_i:
\[
Q=a(X_i-m(X_{-i}))^2+R(X_{-i}),
\]
where m is affine and the quadratic coefficient matrix of R is S. Conditional on X_{-i}, each of the at most two inverse roots contributes at most 1/(2sqrt{|a|}\sqrt{|y-R|}) to the density of Q at y. Therefore for every nonnegative Borel h,
\[
\mathbb E h(Q)
\le |a|^{-1/2}
\mathbb E\int_{\mathbb R}h(y)|y-R|^{-1/2}\,dy. \tag{6}
\]
The variables X_{-i} remain independent cap-one original coordinates, and R may have any induced affine term. Apply (3) to R using (5), then Tonelli in (6), obtaining p_Q(y)<=C_*/sqrt{|a|sigma} almost everywhere. This proves (1).

## Source audit and exact limit

The numerical branches in lower_levels.tex were rechecked: at its comparable-eigenvalue threshold, rho_A=3/(64*10002) and nu_A=rho_A^2/2=1.09819349...e-11, the row test leaves 1.19628698...e-11; its discriminant bound is below 462,000 and its balanced Fourier half-potential bound is below 8,000. At the dominant-eigenvalue threshold K>10^4, the signed 2-by-2 compression has determinant mu_1 mu_2+s^2; the proof bounds s^2<0.0039 K, so opposite signs cannot cancel its determinant. The residual crossing and volume marginal calculations give Z_2>=1 and row inclusion probabilities below 0.6, hence H(R)<129. The proof accommodates arbitrary extra eigenvalues through the norm-one spectral remainder after normalization. The c_*-pivot and no-pivot cases cover all matrices without a hidden law assumption.

Full source proofs: proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/lower_levels.tex, Theorem lower:two, and structure.tex, Lemma pivot-half. This report is a combination and an explicit all-sign scalar-pivot statement, not a new proof of those two long source theorems.

The dependence on a cannot be suppressed by (4): a zero-curvature physical hub has a=0, while s_3(A) can still equal one. In that case the hub discriminant L^2+a(s-R) is merely L^2 and its quadratic matrix has rank one, so the present half-potential path cannot see a transverse square. The unrestricted indefinite no-pivot case remains OPEN.
