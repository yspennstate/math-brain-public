# Exact checks for account04/B18 r5

Run: \`20260923T221534Z-account04-B18-QFORM-r5\`.

The proof uses only the following finite-dimensional identities.

1. Since \(B\) is symmetric and \(\ker B\) is orthogonal to \(\operatorname{range}(B)\),
   \[
   Be_0=B P_{\operatorname{range}(B)}e_0.
   \]
2. Under \(\max_j|\mu_j|\le L\),
   \[
   \|Be_0\|_2\le L\|P_{\operatorname{range}(B)}e_0\|_2=L\sqrt h.
   \]
3. Because \(B_{00}=0\), \(\|Be_0\|_2=\|g\|_2\). Therefore
   \[
   \max_i|g_i|\ge a\Longrightarrow a\le\|g\|_2\le L\sqrt h
   \Longrightarrow h\ge a^2/L^2.
   \]
4. Substitution into \(576^{1/3}s^{-1}h^{-1/3}\) gives
   \[
   576^{1/3}s^{-1}(a^2/L^2)^{-1/3}
   =576^{1/3}L^{2/3}s^{-1}a^{-2/3}.
   \]
5. At \(a=1/64\),
   \[
   a^{-2/3}=64^{2/3}=16,\qquad
   16\cdot576^{1/3}=133.1253646753219\ldots<133.126.
   \]

No determinant sign, post-rotation independence, or conditional density bound enters these checks.
