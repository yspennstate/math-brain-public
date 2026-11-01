# Round 251

Round 251 splits short prefix-record spread into persistent prefix-record
spread and return-generating nonpersistent spread.

For \(K,L\ge1\), define \(P^{\rm pre,per,sh}_{j,K,L}\) by requiring many
levels \(u\in A_{j,p}\) with a short record \((-1,+1)\)-crossing run
\([a,b]\) before the endpoint sphere such that the path stays above level
\(u\) after the run until the first endpoint-sphere hit:
\[
  d(x,v_t)>u\qquad(b<t\le\tau_x^{\rm end}(\gamma)).
\]
The run is still short and deep:
\[
  b<\tau_x^{\rm end}(\gamma),\qquad b-a\le L,\qquad
  e_x(\gamma)-u>\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H.
\]

If \(P^{\rm pre,rec,sh}_{j,K,L}\) holds but
\(P^{\rm pre,per,sh}_{j,2K,L}\) fails, then linearly many counted record
levels return to level \(u\) before the endpoint-sphere hit.  Since the
record run exits to \(u+1\), the first return to \(u\) is an inward
level-\(u+1\) token.  The token-to-return lemma gives
\[
  P^{\rm pre,rec,sh}_{j,K,L}
  \le
  P^{\rm pre,per,sh}_{j,2K,L}
  +
  X^{\rm spr}_{j,4K}
  +
  X^{\rm spr}_{j+1,4K}.
\]

In the finite ladder, \(K=64M_i\), so the residual becomes
\[
  P^{\rm pre,per,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,128M_i,L_i}^{
    G\to H,{\rm rad,tan,pre,out,per,short}}.
\]
The return terms are exactly at the already enlarged \(256M_i\) threshold,
changing spread-return coefficients to \(7\) for the current slab and \(5\)
for the next slab.

The current route to \(p_c(G)<p_{2\to2}(G)\) depends on finite-defect bins,
near-tail bins, a terminal far tail, short persistent-prefix spread, long
tangential runs, enlarged spread exterior returns, and ordinary exact-level
exterior returns.
