# Round 234

Round 234 splits the remaining horizontal-heavy slab obstruction by exact
radial level.

For \(u,K\ge0\), define
\[
  \mathcal Z_{u,K}(x,\gamma):\quad H_x(\gamma;\{u\})>K.
\]
For \(K\ge1\), define the horizontal spread property
\[
  \mathcal Z^{\rm spr}_{j,K,p}(x,\gamma):
  \#\{u\in A_{j,p}\cap\mathbb N:H_x(\gamma;\{u\})>0\}
  >
  \frac{\theta_{\lambda,\sigma,\beta}}{2K}L_H .
\]
Then
\[
  \mathfrak V_{Q,\lambda,\sigma,\beta,j}^{G\to H,{\rm rad,hor}}
  \le
  \mathfrak Z_{Q,\lambda,\sigma,\beta,j,K}^{G\to H,{\rm rad,hor,spr}}
  +
  W_{\beta,p}
  \mathfrak Z_{Q,\lambda,\sigma,\beta,j,K}^{G\to H,{\rm rad,hor,lev}}.
\]

Combining this with Round 233 gives a fully localized ladder:
terminal far tail plus same-sphere spread, exact-level same-sphere congestion,
spread exterior returns, and exact-level repeated exterior returns.  The only
new multiplicative losses are slab-width factors \(W_{\beta_i,p}\), which are
exponent-negligible.
