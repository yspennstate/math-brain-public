# An independent rank-one square bank with an arbitrary-rank Schur residual

23 September 2026. This is a scoped receiver derived from the assembled manuscript's arbitrary-rank two-eigenvalue half-power potential. It does not yield a structural reduction for all three-eigenvalue matrices.

## Theorem

Let \(X=(X_S,X_T)\) have independent original coordinates, each with a probability density bounded by one. Let \(u\in\mathbb R^S\) be a unit vector, \(\lambda\ne0\), \(v\in\mathbb R^T\), and \(D=D^\mathsf T\) be an arbitrary real \(|T|\)-by-\(|T|\) matrix. Suppose the quadratic matrix has the exact block form
\[
A=\begin{pmatrix}
\lambda uu^\mathsf T&uv^\mathsf T\\
vu^\mathsf T&D
\end{pmatrix}. \tag{1}
\]
If \(s_3(A)\ge\sigma>0\), then, for every affine vector of the form
\[
b=(\beta u,b_T)
\]
and every constant \(c\), the quadratic polynomial
\[
Q=X^\mathsf TAX+b^\mathsf TX+c
\]
has a density with
\[
\boxed{\quad
\|p_Q\|_\infty\le
{\sqrt2\,C_*\over\sqrt{|\lambda|\sigma}},
\qquad
C_*=1+44\cdot10^{7.5}.
\quad} \tag{2}
\]
There is no restriction on the signs, rank, norm or spectrum of \(D\), or on \(b_T\). In particular, a physical hub's self square and all its couplings are allowed if the hub lies in \(T\).

The affine restriction \(b_S=\beta u\) is needed for this exact square-conditioning proof. An affine direction supported on bank coordinates orthogonal to \(u\) depends on variables correlated with \(u^\mathsf TX_S\); conditioning on that direction does not retain a uniform density cap for the square variable.

## Proof

Put \(W=u^\mathsf TX_S\) and \(Y=X_T\). The one-dimensional bounded-density projection theorem gives \(\|p_W\|_\infty\le\sqrt2\), and \(W\) is independent of \(Y\). Completing the square yields
\[
Q=\lambda\left(W+{v^\mathsf TY+\beta/2\over\lambda}\right)^2
  +R(Y),
\]
where
\[
R(Y)=Y^\mathsf T\left(D-{vv^\mathsf T\over\lambda}\right)Y
 +(b_T-\beta v/\lambda)^\mathsf TY+c-\beta^2/(4\lambda). \tag{3}
\]
The nonzero eigenvalues of \(A\) are those of the reduced matrix
\[
C=\begin{pmatrix}\lambda&v^\mathsf T\\v&D\end{pmatrix};
\]
all directions in the \(S\)-bank perpendicular to \(u\) are zero quadratic directions. Thus \(s_3(C)\ge\sigma\). The spectral-count lemma for a nonsingular one-by-one Schur pivot shows that
\[
s_2\left(D-{vv^\mathsf T\over\lambda}\right)\ge\sigma. \tag{4}
\]

For a scalar variable of density at most \(M\), the translated square \(\lambda(W+a)^2\) has conditional density at \(z\) at most
\(M\,|z|^{-1/2}/\sqrt{|\lambda|}\). This follows by summing the two inverse branches of the square map. Applying it conditionally on \(Y\) gives
\[
p_Q(s)\le{\sqrt2\over\sqrt{|\lambda|}}
             \mathbb E|s-R(Y)|^{-1/2}. \tag{5}
\]
The assembled manuscript's lower-level estimates imply, for any real symmetric \(M\) with \(s_2(M)\ge\sigma\) and any original-coordinate affine term,
\[
\sup_s\mathbb E|Y^\mathsf TMY+d^\mathsf TY-s|^{-1/2}
\le C_*/\sqrt\sigma. \tag{6}
\]
For completeness, after scaling to \(\sigma=1\), if \(M\) has no \(10^{-15}\)-pivot, lower_levels.tex Theorem lower:two bounds the truncated half-power potential by \(10^6\). If there is such a diagonal or principal-pair pivot, structure.tex Lemma pivot-half bounds it by \(44(10^{-15})^{-1/2}\). The contribution from \(|Q-s|>1\) is at most one. The assertions are uniform in affine terms and arbitrary remaining spectrum. Equations (4)–(6) prove (2). A bound on interval probabilities follows first, so no pointwise-density version is needed in the argument.

When the Schur residual in (3) has exact rank two, rank_two.tex Theorem rt:half replaces the large \(C_*\) by the determinant bound \(68\,|\det\Lambda_2|^{-1/4}\), including arbitrary affine terms.

## Why this does not settle the unrestricted problem

The exact block condition (1) says that all within-bank quadratic dependence is through the one scalar \(W\), and all bank-to-remainder crossing rows are aligned with \(u\). A general dense three-eigenvalue matrix need not have any large independent bank of this form. An explicit exact-rank-three example with \(s_3=1\), all principal pairs nonsingular, and singleton diagonals tending to zero appears in the companion two-bank report:
https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T200935Z-two-bank-chirp-factorization/REPORT.md .
That example is covered by a different two-bank receiver, which illustrates that the exact square-bank condition is a sufficient analytic certificate rather than a necessary structure.
