# Addendum — sharpened light-cone constant

This addendum sharpens Theorem 5.1 of the run report; it does not change its hypotheses or the fact that the full QFORM conjecture remains open.

Keep the notation of `QFORM-RANK3-LIGHTCONE-CANONICAL-v1`: `beta=||A_{\bar i,i}||_2`, `r=||d_0||_2`, and

\[
|\lambda_1\lambda_2\lambda_3|=|\gamma|(\beta^2+r^2).
\]

Let

\[
s=(\beta^2+r^2)^{1/2},\qquad L=\|A\|_{op}.
\]

In the canonical orthogonal coordinates, the column corresponding to `U` contains the entries `beta`, `c`, `delta`, and the vector `d_0`. Hence its Euclidean norm is at least `s`, so

\[
L\ge s.
\]

Because `A` has exact rank three and all three nonzero eigenvalues satisfy `|lambda_j|>=1`, their product obeys

\[
|\lambda_1\lambda_2\lambda_3|\ge L.
\]

Therefore

\[
|\gamma|s^2\ge s,
\qquad\text{hence}\qquad
|\gamma|s\ge1.
\]

With `R=max(beta,r)`, we have `R>=s/sqrt(2)`, and therefore

\[
\boxed{|\gamma|R\ge2^{-1/2}.}
\]

If `R=beta`, the physical-singleton channel of `QFORM-CROSS-SQUARE-MOVING-CENTER-v1` gives

\[
\|p_Q\|_\infty
\le 8\,2^{1/4}|\beta\gamma|^{-1/2}
\le8\sqrt2.
\]

If `R=r`, the three-bank channel gives

\[
\|p_Q\|_\infty
\le8\sqrt2\,|r\gamma|^{-1/2}
\le8\,2^{3/4}.
\]

Thus Theorem 5.1 may be strengthened to

\[
\boxed{
\|p_Q\|_\infty\le8\,2^{3/4}<13.455.
}
\]

The density is continuous by the moving-center theorem, and every interval `I` obeys

\[
\Pr\{Q\in I\}\le8\,2^{3/4}|I|.
\]

This sharpening uses only the exact-rank-three target spectral lower bound and the canonical pseudodeterminant identity; no additional probabilistic assumption is introduced.