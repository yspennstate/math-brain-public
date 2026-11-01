# Round 250

Round 250 splits short outward-prefix spread into short prefix-record spread
and return-generating non-record spread.

For \(K,L\ge1\), define \(P^{\rm pre,rec,sh}_{j,K,L}\) by requiring many
levels \(u\in A_{j,p}\) with a short \((-1,+1)\)-crossing run \([a,b]\)
before the endpoint sphere, where the run is the first visit to level \(u\):
\[
  d(x,v_t)\ne u\ (0\le t<a),\qquad
  b<\tau_x^{\rm end}(\gamma),\qquad b-a\le L,
\]
and the level remains linearly below the endpoint:
\[
  e_x(\gamma)-u>\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H.
\]
If \(P^{\rm pre,out,sh}_{j,K,L}\) holds but
\(P^{\rm pre,rec,sh}_{j,2K,L}\) fails, then linearly many counted levels have
a short prefix outward run that is not the first visit to that level.  For
such a level, the path visited level \(u\) before the run and then returned
to \(u-1\) just before entering the run, producing an inward level-\(u\)
token.  The token-to-return lemma gives
\[
  P^{\rm pre,out,sh}_{j,K,L}
  \le
  P^{\rm pre,rec,sh}_{j,2K,L}
  +
  X^{\rm spr}_{j,2K}.
\]

In the finite ladder, \(K=32M_i\), so the residual is replaced by
\[
  P^{\rm pre,rec,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,64M_i,L_i}^{
    G\to H,{\rm rad,tan,pre,out,rec,short}}.
\]
The added return term is absorbed by the enlarged \(256M_i\) spread-return
profile, changing the coefficients to \(6\) for the current slab and \(4\)
for the next slab.

The current route to \(p_c(G)<p_{2\to2}(G)\) depends on finite-defect bins,
near-tail bins, a terminal far tail, short prefix-record spread, long
tangential runs, enlarged spread exterior returns, and ordinary exact-level
exterior returns.
