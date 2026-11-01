# Every exact rank-three physical spectral coloop

**Status:** Complete proof of the exact rank-three physical-spectral-coloop branch. The full dimension-independent conjecture still includes matrices with no physical coordinate in the three-dimensional spectral range, especially the overlapping small-leakage negative-target configuration.

## Theorem

Let \(X_i\) be independent real original-coordinate variables, each with a probability density at most one. Let a symmetric matrix \(A\) have **exact rank three** and \(s_3(A)\ge1\). If some original-coordinate basis vector \(e_h\) belongs to \(\operatorname{range}(A)\), then \(X^\top A X\) has a density bounded by an absolute constant independent of ambient dimension, the law, the target, and spectral signs.

For affine \(b^\top X+c\), the argument below proves the same result when \(b\in\operatorname{range}(A)\). The \(|A_{hh}|>1/4\) branch alone allows arbitrary affine \(b\); the small-diagonal branch does not cover a null-direction affine component.

## Small physical diagonal

If \(|a|:=|A_{hh}|\le1/4\), apply the proved all-target physical-coloop theorem *Exact rank-three physical coloop with a small hub diagonal*. It isolates an independent original hub \(H=X_h\), an orthonormal planar projection \((L,V)\) of the independent remaining originals with planar density cap at most two, and an exact three-dimensional spectral matrix. The theorem bounds the density uniformly, even for arbitrary joint planar light densities under that cap. Its proof explicitly treats the hub square \(aH^2\) and both signs of the transverse square.

## Substantial physical diagonal

If \(|a|>1/4\), complete the square in the **original coordinate** \(H=X_h\):
\[
 X^\top A X+b^\top X+c
 =a(H-m(Y))^2+Q_S(Y)+\ell(Y)+c',
 \qquad S=A_{\bar h,\bar h}-A_{\bar h,h}A_{h,\bar h}/a,
\]
where \(Y=(X_i)_{i\ne h}\) and \(m,\ell\) depend on the affine terms. Conditional on \(Y\), the hub density cap gives
\[
 p_Q(s)\le |a|^{-1/2}\,
   \mathbb E|s-Q_S(Y)-\ell(Y)-c'|^{-1/2}.
 \tag{1}
\]
The spectral-count lemma for coordinate Schur complements gives \(N_S(1)\ge N_A(1)-1=2\). The archived *lower_levels.tex* Theorem `lower:two` proves a truncated half-Riesz bound \(\mathcal H(Q_S+\ell)\le10^6\) if there is no \(c_*=10^{-15}\) original-coordinate pivot. The archived *structure.tex* Lemma `pivot-half` proves \(\mathcal H(Q_S+\ell)\le44c_*^{-1/2}\) if there is such a pivot. Both statements allow arbitrary affine terms and use independent original coordinates. Therefore, without invoking the unproved third-level no-pivot conjecture,
\[
 \sup_t\mathbb E\left[|Q_S+\ell-t|^{-1/2};
                       |Q_S+\ell-t|\le1\right]
 \le G_2:=\max\{10^6,44\cdot10^{15/2}\}.
\]
The contribution of \(|Q_S+\ell-t|>1\) is at most one. Since \(|a|^{-1/2}<2\), (1) yields \(\|p_Q\|_\infty\le2(1+G_2)\), uniformly in arbitrary \(b\).

This proves the theorem by the two diagonal regimes. The explicit constant in the substantial-diagonal branch is intentionally large; only its independence of dimension, signs, laws, and target matters here.
