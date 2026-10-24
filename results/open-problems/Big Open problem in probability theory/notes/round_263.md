# Round 263

Round 263 packages the repeated staircase-chain iteration into a reusable
one-step amplification corollary.

For any fixed locally short chain length \(\ell\ge2\) and depth parameter
\(K\), define
\[
  B_{\lambda,\sigma,\beta,K}
  =
  \left\lceil
    \frac{16K\beta}{\theta_{\lambda,\sigma,\beta}}
  \right\rceil+1.
\]
The new corollary combines:

1. bounded successor gaps for chain starts,
2. pigeonholing to a fixed gap,
3. gluing overlapping/abutting gaps \(1\le h\le\ell\),
4. confining separated gaps \(h\ge\ell+1\).

It gives the one-step implication
\[
  P^{\rm chain}_{j,K,L,\ell}
  \le
  \sum_{h=1}^{\ell}P^{\rm chain}_{j,\widetilde K,L,\ell+h}
  +
  \sum_{h=\ell+1}^{\widetilde B}
  P^{\rm chainbr}_{j,\widetilde K,L,\ell,h}
\]
for any \(\widetilde B\ge B_{\lambda,\sigma,\beta,K}\), with
\(\widetilde K=2K\widetilde B\).

The Round 262 finite-ladder proof now cites this packaged step directly.
The live residual family is unchanged from Round 262, but future chain
amplification steps can now be written without reassembling the three local
corollaries.

No external open-status search was refreshed in this round.
