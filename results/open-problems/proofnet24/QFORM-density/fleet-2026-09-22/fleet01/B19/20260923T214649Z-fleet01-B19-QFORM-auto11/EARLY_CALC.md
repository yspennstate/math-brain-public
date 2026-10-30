# Early substantive calculation — common-plane Schur mismatch

Run: `20260923T214649Z-fleet01-B19-QFORM-auto11`  
Status: supporting derivation; unrestricted QFORM remains open.

Use the exact no-coloop endpoint from fleet02/B19 r36. After conditioning the already-separated original coordinates, the conditional quadratic polynomial is

\[
q(x,y)=x^TBx+2x^TMy+y^T(\Delta+M^TKM)y+a^Tx+b^Ty+c,
\]
where `x` consists of two literal original hub coordinates, `y` is the remaining original-coordinate product bank, `B=B^T` is `2x2`, `M` is `2xm` of rank two, `K=K^T`, and `Delta` is diagonal. Put

\[
G=MM^T,\qquad S=\sqrt{\det G},\qquad
\ell_i=m_i^TG^{-1}m_i.
\]

Assume for this calculation that `B` is invertible indefinite and `max_i ell_i<=1/2`. Set

\[
L:=K-B^{-1}.
\]

Completing the *physical* hub pair gives, with `h(y)=My+a/2`,

\[
q=(x+B^{-1}h(y))^TB(x+B^{-1}h(y))+R(y),
\]
where the quadratic matrix of the remainder is exactly

\[
\Delta+M^TLM.
\]
The affine and constant corrections are retained.

If `det L !=0`, then `M^TLM` has rank two, its range is exactly `range(M^T)`, hence the coordinate leverage of its orthonormal eigenframe is exactly `ell_i`. Its two nonzero eigenvalues `lambda_1,lambda_2` obey

\[
|\lambda_1\lambda_2|
=|\det(LMM^T)|
=|\det L|\,\det(MM^T)
=|\det L|S^2.
\]
Thus the completed Fresnel--Brascamp--Lieb theorem for diagonal plus spread rank two gives

\[
|\phi_R(t)|\le \min\left(1,\frac{4\pi}{|t|\sqrt{|\det L|S^2}}\right).
\]
Using

\[
|u|^{-1/2}=\sqrt{2/\pi}\int_0^\infty t^{-1/2}\cos(tu)\,dt
\]
(and truncation/monotone passage), the preceding characteristic-function estimate yields uniformly in the target shift `s`

\[
\sup_s E|R-s|^{-1/2}
\le 8\sqrt2\,(|\det L|S^2)^{-1/4}.
\]
Consequently

\[
\sup_s P(|R-s|<\rho)
\le 8\sqrt2\,(|\det L|S^2)^{-1/4}\sqrt\rho.
\]

The completed physical indefinite-pair logarithmic transducer, with
`D_B=|det B|` and `kappa=sigma_min(B)`, then gives the actual density payment

\[
\boxed{
\|p_q\|_\infty
\le16\,2^{1/4}(D_B\kappa)^{-1/4}
        (|\det(K-B^{-1})|S^2)^{-1/8}.
}
\]
Equivalently,

\[
\|p_q\|_\infty
\le16\,2^{1/4}(D_B\kappa)^{-1/4}
S^{-1/4}|\det(K-B^{-1})|^{-1/8}.
\]

This proof uses only original-coordinate conditioning; no rotated random variables are asserted independent. It retains arbitrary diagonal twists, arbitrary affine terms, and all signs of `K-B^{-1}`. The degenerate case `det(K-B^{-1})=0` is *not* paid by this inequality and is the structural residue to analyze next. Continuity is not claimed from the pair-log transducer.
