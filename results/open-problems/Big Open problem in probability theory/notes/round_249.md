# Round 249

Round 249 splits the short endpoint-prefix residual into an outward-through
part and a return-generating part.

For \(K,L\ge1\), define \(P^{\rm pre,out,sh}_{j,K,L}\) by requiring many
levels \(u\in A_{j,p}\) with a short \((-1,+1)\)-crossing run \([a,b]\)
before the first hit of the endpoint sphere:
\[
  b<\tau_x^{\rm end}(\gamma),\qquad b-a\le L,\qquad
  e_x(\gamma)-u>\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H.
\]
If \(P^{\rm pre,sh}_{j,K,L}\) holds but
\(P^{\rm pre,out,sh}_{j,2K,L}\) fails, then linearly many counted levels have
a short prefix run that is not of type \((-1,+1)\).  After discarding the
possible initial level \(u=0\), each such run has either an inward exit at
level \(u\) or an inward entry at level \(u+1\).  The existing token-to-return
lemma gives a spread exterior return at level \(u\) or \(u+1\).

The resulting profile split is
\[
  P^{\rm pre,sh}_{j,K,L}
  \le
  P^{\rm pre,out,sh}_{j,2K,L}
  +
  X^{\rm spr}_{j,16K}
  +
  X^{\rm spr}_{j+1,16K}.
\]

In the finite ladder, \(K=16M_i\), so \(P^{\rm pre,sh}_{i,j}\) is replaced by
\[
  P^{\rm pre,out,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,32M_i,L_i}^{
    G\to H,{\rm rad,tan,pre,out,short}},
\]
and the spread-return threshold is enlarged to \(256M_i\).  The spread-return
coefficients become \(5\) for the current slab and \(4\) for the next slab.

The current route to \(p_c(G)<p_{2\to2}(G)\) depends on finite-defect bins,
near-tail bins, a terminal far tail, short outward-prefix spread, long
tangential runs, enlarged spread exterior returns, and ordinary exact-level
exterior returns.
