# Round 231

Round 231 localizes the level-congested inward slab term to exact levels.

For \(u,K\ge1\), define \(\mathcal X_{u,K}(x,\gamma)\) to be the property
that \(\gamma\) contains more than \(K\) exterior return subpaths through
level \(u\): each starts at level \(u-1\), immediately exits to level \(u\),
stays outside \(B_{u-1}(x)\) in its interior, and then returns from level
\(u\) to level \(u-1\).  The open time intervals are disjoint.

The exact-level exterior-return profile is
\[
  \mathfrak X_{Q,\lambda,\sigma,\beta,j,K}^{G\to H,{\rm rad,ret}},
\]
obtained by taking the worst level \(u\) in the slab \(A_{j,p}\).

The new localization bound is
\[
  \mathfrak V_{Q,\lambda,\sigma,\beta,j,K}^{G\to H,{\rm rad,in,con}}
  \le
  W_{\beta,p}\,
  \mathfrak X_{Q,\lambda,\sigma,\beta,j,K}^{G\to H,{\rm rad,ret}}.
\]
Since \(\log W_{\beta,p}=o(L_H)\), this polynomial loss does not change the
logarithmic exponent criteria.

The tokenized ladder can therefore replace the congested inward slab
obligation by exact-level exterior-return estimates.  The remaining localized
pieces are terminal far tail, horizontal-heavy slabs, spread-inward slabs, and
exact-level exterior returns.
