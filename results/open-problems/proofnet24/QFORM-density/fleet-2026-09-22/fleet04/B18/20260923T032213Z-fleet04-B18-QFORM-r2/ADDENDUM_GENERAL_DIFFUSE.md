# Addendum — the equal split is unnecessary

The theorem in `REPORT.md` has a stronger source-valid form. The proof used the equal-split hypothesis only to deduce `||v_j||^2<=1/2`. No bank partition is otherwise needed by the full determinant-squared basis law.

## `QFORM-DIFFUSE-FRAME-FULL-BASIS-CAP-v1`

Retain the exact-rank-three Schur-isotropic form

\[
Q=(V^TX_{\rm res}+uX_0)^TD(V^TX_{\rm res}+uX_0),
\qquad V^TV=I_3,quad u^TDu=0.
\]

Assume only

\[
0<r:=||u||\le1,
\qquad \max_j||v_j||^2\le\frac12.
\tag{A.1}
\]

The original coordinates remain independent with density caps one, and the three nonzero eigenvalues of the physical matrix have modulus at least one. Then `Q` has a continuous density and, with

\[
\beta=\frac{r^2}{1+r^2},
\]

\[
\boxed{
||p_Q||_\infty
\le 3\exp\!\left(\frac{3-\beta}{3}\right)
(1-\beta)^{-(1-\beta)/3}
\le3e<8.155.
}
\tag{A.2}
\]

At `r=1`, the right side is `3e^(5/6)2^(1/6)=7.7482743348...`.

### Proof

Use the full determinant-squared volume law on the physical columns of `L=[u,V^T]`. Its score is

\[
Z=\det(LL^T)=\det(I+uu^T)=1+r^2.
\]

Its marginals are the leverage scores. The special marginal is `beta<=1/2`. For every residual row,

\[
p_j=v_j^T(I+uu^T)^{-1}v_j\le||v_j||^2\le1/2.
\]

Thus fleet01/B18's capped-basis theorem applies. The target spectrum gives

\[
|\det D|Z=|\operatorname{pdet}A|\ge1.
\]

Finally, `sum_j p_j=3` and `-(1-x)log(1-x)<=x` give exactly the factor computation in equations (4.3)--(4.7) of `REPORT.md`. Continuity is part of the capped-basis theorem. QED.

## Consequence for the live structural split

Every low-shear (`r<=1`) Schur-isotropic survivor is now paid unless it has a physical residual row with leverage `||v_j||^2>1/2`. Hence the first structural debt in this exact core is reduced to a genuine localized heavy-row alternative, plus the high-shear regime `r>1`. No exact balanced partition is required.

This does not absorb additional spectrum and does not assert post-rotation independence.
