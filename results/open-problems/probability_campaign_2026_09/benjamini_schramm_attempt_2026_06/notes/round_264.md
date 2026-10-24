# Round 264

Round 264 upgrades the packaged one-step staircase-chain amplification into
a finite-depth iteration statement.

Starting from a locally short staircase-chain profile with length
\(\ell\ge2\) and depth \(K_0=K\), choose finite cutoffs
\[
  B_r\ge
  B_{\lambda,\sigma,\beta,K_{r-1}}
  =
  \left\lceil
    \frac{16K_{r-1}\beta}{\theta_{\lambda,\sigma,\beta}}
  \right\rceil+1,
  \qquad
  K_r=2K_{r-1}B_r .
\]
Let \(\mathcal A_r(\ell)\) encode all possible length histories obtained by
replacing a length \(a\) with one of \(a+1,\ldots,2a\).  The new corollary
proves that after any fixed \(n\),
\[
  P^{\rm chain}_{j,K_0,L,\ell}
  \le
  \sum_{\mathbf a\in\mathcal A_n(\ell)}
    P^{\rm chain}_{j,K_n,L,a_n}
  +
  \sum_{r=1}^n
  \sum_{\mathbf a\in\mathcal A_{r-1}(\ell)}
  \sum_{h=a_{r-1}+1}^{B_r}
    P^{\rm chainbr}_{j,K_r,L,a_{r-1},h}.
\]

The multiplicities in \(\mathcal A_r(\ell)\) are intentional: they record
all paths through the repeated one-step inequalities.  This does not remove
the terminal chain residual, but it makes arbitrary finite chain
amplification available without writing a new bespoke finite ladder each
time.

No external open-status search was refreshed in this round.
