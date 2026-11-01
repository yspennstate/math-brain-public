# Round 252

Round 252 turns the short persistent-prefix residual into an ordered
endpoint-prefix ladder residual.

For \(K,L\ge1\), define \(P^{\rm pre,lad,sh}_{j,K,L}\) by requiring many
levels
\[
  u_1<\cdots<u_{N_\star}\in A_{j,p}
\]
with short persistent record \((-1,+1)\)-crossing runs
\([a_q,b_q]\) before the endpoint sphere, satisfying
\[
  b_q-a_q\le L,\qquad
  e_x(\gamma)-u_q>\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H,
\]
and with the runs chronologically ordered:
\[
  b_q<a_{q+1}\qquad(1\le q<N_\star).
\]

The deterministic ordering is forced by the record condition.  The run at
level \(u_q\) begins at the first visit to \(u_q\); to first reach
\(u_{q+1}>u_q\), the radial distance sequence must already have visited
\(u_q\), and it cannot be inside the level-\(u_q\) run when it is at level
\(u_{q+1}\).  Hence
\[
  P^{\rm pre,per,sh}_{j,K,L}
  \le
  P^{\rm pre,lad,sh}_{j,K,L}.
\]

The finite ladder therefore replaces
\[
  P^{\rm pre,per,sh}_{i,j}
\]
by
\[
  P^{\rm pre,lad,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,128M_i,L_i}^{
    G\to H,{\rm rad,tan,pre,out,per,lad,short}},
\]
with no coefficient changes: spread-return coefficients remain \(7\) for the
current slab and \(5\) for the next slab.

The current route to \(p_c(G)<p_{2\to2}(G)\) depends on finite-defect bins,
near-tail bins, a terminal far tail, ordered short persistent prefix ladders,
long tangential runs, enlarged spread exterior returns, and ordinary
exact-level exterior returns.
