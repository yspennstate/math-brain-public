# Round 254

Round 254 splits the bounded-gap prefix-pair residual into fixed-gap
prefix-pair residuals.

If \(P^{\rm pre,pair,sh}_{j,K,L,B}\) holds, every counted lower level \(u\)
has a partner \(u+h\) for at least one \(1\le h\le B\).  By pigeonholing over
this finite set of possible gaps,
\[
  P^{\rm pre,pair,sh}_{j,K,L,B}
  \le
  \sum_{h=1}^{B}P^{\rm pre,gap,sh}_{j,KB,L,h}.
\]
The threshold parameter is multiplied by \(B\), and the depth condition only
weakens.  Since \(B\) is fixed for each ladder parameter set, the finite sum
is exponent-negligible.

In the finite ladder, the residual is now
\[
  P^{\rm pre,gap,sh}_{i,j,h}
  =
  \mathfrak P_{Q,\lambda_i,\sigma_i,\beta_i,j,256M_iB_i,L_i,h}^{
    G\to H,{\rm rad,tan,pre,out,per,gap,short}},
  \qquad 1\le h\le B_i.
\]
The spread-return coefficients remain \(7\) for the current slab and \(5\) for
the next slab.

The current route to \(p_c(G)<p_{2\to2}(G)\) depends on finite-defect bins,
near-tail bins, a terminal far tail, fixed-gap short persistent prefix pairs,
long tangential runs, enlarged spread exterior returns, and ordinary
exact-level exterior returns.
