# Round 232

Round 232 folds the exact-level exterior-return localization back into the
finite far-tail ladder.

For each ladder level \(i\) and slab \(j\), write
\[
  X_{i,j}^{\rm ret}
  =
  \mathfrak X_{Q,\lambda_i,\sigma_i,\beta_i,j,K_i}^{G\to H,{\rm rad,ret}}.
\]
Combining the tokenized ladder with Round 231 gives
\[
\begin{aligned}
  \mathfrak Y_{\lambda_0}
  \le
  \mathfrak Y_{\lambda_N}
  &+
  \sum_{i,j}\mathfrak V_{i,j}^{\rm hor}
  +
  \sum_{i,j}\mathfrak V_{i,j,K_i}^{\rm in,spr}
  +
  \sum_{i,j} W_{\beta_i,p}X_{i,j}^{\rm ret}.
\end{aligned}
\]
The factors \(W_{\beta_i,p}=O(L_H)\) are exponent-negligible.

Thus the current finite far-tail endpoint is terminal far tail plus three
localized obligations: horizontal-heavy slab estimates, spread-inward slab
estimates, and exact-level exterior-return estimates.  The level-congested
slab profile no longer appears as a separate primitive target.
