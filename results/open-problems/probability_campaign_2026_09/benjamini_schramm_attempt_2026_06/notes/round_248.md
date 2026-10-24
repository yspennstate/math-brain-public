# Round 248

Round 248 splits the endpoint-prefix deep horizontal spread residual into an
already-listed long-run part and a genuinely short-run part.

For \(K,L\ge1\), define \(P^{\rm pre,sh}_{j,K,L}\) by requiring many levels
\(u\in A_{j,p}\) with a tangential run \([a,b]\) satisfying
\[
  b<\tau_x^{\rm end}(\gamma),\qquad b-a\le L,\qquad
  e_x(\gamma)-u>\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H.
\]
If \(P^{\rm pre}_{j,K}\) holds but \(P^{\rm pre,sh}_{j,K,L}\) fails, then at
least one endpoint-prefix counted level has a witnessing tangential run of
length \(>L\).  Taking the union bound over the slab gives
\[
  P^{\rm pre}_{j,K}
  \le
  W_{\beta,p}T^{\rm long}_{j,L}
  +
  P^{\rm pre,sh}_{j,K,L}.
\]

In the finite ladder this replaces \(P^{\rm pre}_{i,j}\) by
\[
  P^{\rm pre,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,16M_i,L_i}^{
    G\to H,{\rm rad,tan,pre,deep,short}},
\]
and doubles the existing \(W_{\beta_i,p}T_{i,j}^{\rm long}\) contribution.
The logarithmic criteria are unchanged because the factor \(2\) is fixed and
\(\log_{D_H}W_{\beta_i,p}=o(L_H)\).

The current route to \(p_c(G)<p_{2\to2}(G)\) depends on finite-defect bins,
near-tail bins, a terminal far tail, short endpoint-prefix deep horizontal
spread, long tangential runs, spread exterior returns, and ordinary
exact-level exterior returns.
