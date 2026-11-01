# Round 286

Round 286 refines the ordinary bridge-packet branch of the Round 284 normal
form.

The new corollary is

```tex
\begin{corollary}[Bridge-packet branch has truncated return form]
\label{cor:bridge-packet-branch-has-truncated-return-form}
```

If the wide-residual normal form lands in the ordinary bridge-packet
alternative at index \(r\), define the truncated gap set
\[
  \mathcal G_r
  =
  \left\{
    2\le g\le B_r-\ell_r+1:
    g<
    W_{\beta,p}
    -
    \frac{\theta_{\lambda,\sigma,\beta}}{4K_{r+1}}L_H
  \right\}.
\]
Then the local chain profile at \((K_r,\ell_r)\) is bounded by longer chain
children, inward-free confined bridge profiles, and spread-return profiles:
\[
\begin{aligned}
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le&
  \sum_{h=1}^{\ell_r}
  P^{\rm chain}_{j,K_{r+1},L,\ell_r+h}
\\
  &+
  \sum_{g\in\mathcal G_r}
  P^{\rm bridge,free}_{j,2K_{r+1},L,g}
  +
  \sum_{g\in\mathcal G_r}
  X^{\rm ret,spr}_{j,2K_{r+1}(g-1)}.
\end{aligned}
\]

The proof uses the existing large-gap vanishing lemma to delete ordinary
bridge gaps at or above the slab-start cutoff, then applies the existing
confined-bridge split into inward-free bridges or spread returns.

No external literature refresh was performed in this round; the Round 285
source check remains the latest external status.
