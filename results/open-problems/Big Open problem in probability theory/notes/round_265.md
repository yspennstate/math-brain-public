# Round 265

Round 265 applies the finite-depth chain-amplification corollary at the
finite-ladder level.

The raw staircase-chain/bridge ladder has only two chain residuals in each
tail bin:
\[
  P^{\rm chain}_{i,j,3},
  \qquad
  P^{\rm chain}_{i,j,4}.
\]
For a fixed finite depth \(n\), the new finite-stage ladder chooses
\[
  K_{i,0}^{\rm ch}=512M_iB_iC_i,
  \qquad
  B_{i,r}^{\rm ch}\ge
    B_{\lambda_i,\sigma_i,\beta_i,K_{i,r-1}^{\rm ch}},
  \qquad
  K_{i,r}^{\rm ch}=2K_{i,r-1}^{\rm ch}B_{i,r}^{\rm ch}.
\]
It replaces each raw \(q=3,4\) chain profile by:

1. terminal chains indexed by
   \(\mathcal A_n(q)\), with depth \(K_{i,n}^{\rm ch}\);
2. all confined chain bridges accumulated at intermediate stages
   \(1\le r\le n\).

The remaining finite-ladder families are unchanged: terminal far tail,
confined locally short staircase bridges, confined fixed-gap bridges, long
tangential runs, spread-return profiles, and exact-level returns.

This generalizes the previous one-off second-stage ladder without deleting
that concrete instance.

No external open-status search was refreshed in this round.
