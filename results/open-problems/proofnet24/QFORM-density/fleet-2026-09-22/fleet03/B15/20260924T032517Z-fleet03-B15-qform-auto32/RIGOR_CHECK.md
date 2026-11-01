# Rigor check — fleet03/B15 auto32

This note checks the three algebra/calculus points on which `QFORM-SUBMASS-SQRT-C0-v1` most directly depends. It does not change the theorem statement.

## 1. Border-rank-one determinant

In the low-complement-rank case write

\[
C=\sigma vv^T,
\qquad
B=\begin{pmatrix}
a&b_k&b_l\\
b_k&\sigma v_k^2&\sigma v_kv_l\\
b_l&\sigma v_kv_l&\sigma v_l^2
\end{pmatrix}.
\]

Direct expansion gives

\[
\det B=-\sigma(b_kv_l-b_lv_k)^2.
\]

Hence `b` not proportional to `v` produces an invertible physical triple. At least one of `v_k,v_l` is nonzero, so the triple has an unscaled nonzero diagonal available for the rank-three principal-block theorem.

Under scaling of the distinguished coordinate by `m`,

\[
B_m=\operatorname{diag}(m,1,1)B\operatorname{diag}(m,1,1),
\]

so

\[
\det B_m=m^2\det B
\]

while the chosen unscaled diagonal is unchanged. Therefore the source bound

\[
128(|B_{ii}|\,|\det B_m|)^{-1/4}
\]

has exactly the loss `m^{-1/2}`.

## 2. Schur complement scaling

If a nonsingular physical pair `D` avoids the distinguished coordinate, write the full matrix as

\[
A=\begin{pmatrix}D&B\\B^T&C\end{pmatrix},
\qquad
S=C-B^TD^{-1}B.
\]

The coordinate scaling acts only on the remainder block by a diagonal `E_m`, hence

\[
A_m=\begin{pmatrix}D&BE_m\\E_mB^T&E_mCE_m\end{pmatrix}
\]

and therefore

\[
S_m=E_mCE_m-E_mB^TD^{-1}BE_m=E_mSE_m.
\]

For `0<m<=1`, every diagonal coefficient is multiplied by `1` or `m^2`, while every off-diagonal coefficient is multiplied by `1` or `m`. With the auto27 definition of `eta`, this implies

\[
\eta(S_m)\ge m^2\eta(S).
\]

Consequently the auto27 fourth-root Schur certificate loses at most `m^{-1/2}`.

## 3. Sharpness integral

For the exact target

\[
Q=2XY+Z^2,
\qquad
A=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},
\]

let `Y,Z` be uniform on `[0,1]`. The positive marginal difference `1_[0,m]` gives the subdensity of `W=2XY`

\[
r_+(w)=\frac12\log\frac{2m}{w},\qquad0<w<2m.
\]

Since `Z^2` has density `(2\sqrt s)^{-1}` on `(0,1)`, for `m<=1/2`,

\[
(r_+*h)(2m)
=\frac14\int_0^{2m}\log\frac{2m}{w}(2m-w)^{-1/2}\,dw.
\]

With `w=2mu`, this equals

\[
\frac{\sqrt{2m}}4\int_0^1\log(1/u)(1-u)^{-1/2}\,du.
\]

Differentiating the beta integral `B(a,1/2)` at `a=1` gives

\[
\int_0^1\log(1/u)(1-u)^{-1/2}\,du=4(1-\log2),
\]

so the value is

\[
\sqrt{2m}(1-\log2).
\]

For the negative marginal difference `1_[2,2+m]`, throughout `0<w<2m`,

\[
r_-(w)=\frac12\int_2^{2+m}\frac{dx}{x}
=\frac12\log(1+m/2).
\]

Convolving at `2m` gives exactly

\[
\frac12\log(1+m/2)\sqrt{2m}.
\]

Thus the density difference at `t=2m` is exactly

\[
\sqrt{2m}\left(1-\log2-\frac12\log(1+m/2)\right).
\]

Since the input `L^1` distance is `\delta=2m`, this is asymptotic to `(1-\log2)\sqrt\delta`; the exponent `1/2` is therefore sharp.
