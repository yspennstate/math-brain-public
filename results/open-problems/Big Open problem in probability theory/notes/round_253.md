# Round 253

Round 253 narrows the ordered prefix-ladder residual to a bounded-gap
successor-pair residual.

If an ordered ladder has levels
\[
  u_1<\cdots<u_N\subset A_{j,p},
\]
then the total successor gap is at most the slab width:
\[
  \sum_{q=1}^{N-1}(u_{q+1}-u_q)\le W_{\beta,p}.
\]
For
\[
  B_{\lambda,\sigma,\beta,K}
  =
  \left\lceil
    \frac{16K\beta}{\theta_{\lambda,\sigma,\beta}}
  \right\rceil+1,
\]
only fewer than \(\theta_{\lambda,\sigma,\beta}L_H/(16K)\) successor gaps can
be larger than \(B_{\lambda,\sigma,\beta,K}\), once \(p\) is close enough to
\(\pc(H)\).  Therefore
\[
  P^{\rm pre,lad,sh}_{j,K,L}
  \le
  P^{\rm pre,pair,sh}_{j,2K,L,B_{\lambda,\sigma,\beta,K}}.
\]

In the finite ladder, \(K=128M_i\), so the residual becomes
\[
  P^{\rm pre,pair,sh}_{i,j}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,256M_i,L_i,B_i}^{
    G\to H,{\rm rad,tan,pre,out,per,pair,short}},
\]
where
\[
  B_i=
  \left\lceil
    \frac{2048M_i\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1.
\]
The spread-return coefficients remain \(7\) for the current slab and \(5\) for
the next slab.

The current route to \(p_c(G)<p_{2\to2}(G)\) depends on finite-defect bins,
near-tail bins, a terminal far tail, bounded-gap short persistent prefix
pairs, long tangential runs, enlarged spread exterior returns, and ordinary
exact-level exterior returns.
