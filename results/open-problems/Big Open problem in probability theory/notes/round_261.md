# Round 261

Round 261 iterates the successor-gap reduction from staircase pairs to
arbitrary locally short outward staircase chains.

For a fixed chain length \(\ell\ge2\), many chain starts in one slab imply
many bounded successor gaps.  Pigeonholing over the bounded gaps gives a
finite fixed-gap staircase-chain-pair family.

For a fixed-gap pair of \(\ell\)-chains:

\[
  1\le h\le \ell
\]
means the two chains overlap or abut.  Their record runs coincide on the
overlap, and the pair glues into one locally short chain of length
\[
  \ell+h.
\]

For
\[
  h\ge \ell+1,
\]
the connector from the last run of the lower chain to the first run of the
upper chain is confined:
\[
  u+\ell-1<d(x,v_t)<u+h.
\]

In the finite ladder this is applied to the previous \(q=3,4\) chain
residuals.  With
\[
  D_i=
  \left\lceil
    \frac{8192M_iB_iC_i\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+5,
  \qquad
  K_i^\sharp=1024M_iB_iC_iD_i,
\]
the live chain residual is replaced by longer chains of lengths \(4,\ldots,8\)
and confined fixed-gap staircase-chain bridges.

No external open-status search was refreshed in this round.
