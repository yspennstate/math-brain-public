# Round 267

Round 267 sharpens the finite-stage chain bookkeeping.

The finite-depth chain-amplification corollary used length histories
\(\mathbf a\in\mathcal A_n(\ell)\).  Those histories are useful for induction
but introduce artificial multiplicities: many histories can terminate at the
same chain length.  The new multiplicity-free corollary works directly with
the distinct reachable length interval
\[
  I_r(\ell)=\{\ell+r,\ell+r+1,\ldots,2^r\ell\}.
\]
For fixed \(n\),
\[
  P^{\rm chain}_{j,K_0,L,\ell}
  \le
  \sum_{a\in I_n(\ell)}P^{\rm chain}_{j,K_n,L,a}
  +
  \sum_{r=1}^n
  \sum_{a\in I_{r-1}(\ell)}
  \sum_{h=a+1}^{B_r}P^{\rm chainbr}_{j,K_r,L,a,h}.
\]

The round also adds the simple support lemma that a locally short chain of
length \(\ell\) cannot fit inside one slab once
\[
  \ell>W_{\beta,p}.
\]
Thus terminal chain residuals are automatically zero above the slab width.
Since \(W_{\beta,p}\asymp L_H\), fixed-depth amplification cannot by itself
remove all terminal chains; the remaining obstruction is to control the
accumulated bridge families under a depth growing like \(L_H\), or to find a
sharper amplification mechanism.

No external open-status search was refreshed in this round.
