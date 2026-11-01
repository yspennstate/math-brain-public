# Round 279

Round 279 iterates the bridge-free residual descent under explicit hypotheses.

The new corollary is

```tex
\begin{corollary}[Finite bridge-free residual descent iteration]
\label{cor:finite-bridge-free-residual-descent-iteration}
```

Starting from \((K,\ell)\), it builds a finite descent tree.  At a node
\(\mathbf h\), the current parameters are \(K(\mathbf h)\) and
\(\ell(\mathbf h)\), and the residual cutoff is
\[
  B(\mathbf h)=B^{\rm res}_{K(\mathbf h),\ell(\mathbf h),p}.
\]
If, at every node up to depth \(m-1\),
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{16K(\mathbf h)}L_H>1,
  \qquad
  B(\mathbf h)\le \ell(\mathbf h),
\]
then the bridge-free descent corollary can be applied at every node.  This
gives
\[
  P^{\rm chain}_{j,K,L,\ell}
  \le
  \sum_{\mathbf h\in\mathcal H_m}
  P^{\rm chain}_{j,K(\mathbf h),L,\ell(\mathbf h)}.
\]

The residual start width decreases by at least one at each descent step:
\[
  R_{\ell(\mathbf h),p}\le \max\{R_{\ell,p}-m,0\}
  \qquad(\mathbf h\in\mathcal H_m).
\]
Therefore, if the bridge-free hypotheses persist until
\[
  m\ge R_{\ell,p},
\]
then every terminal chain profile vanishes by the long-chain start-count
cutoff, and the initial chain profile is zero.

This is a conditional exhaustion theorem.  It does not solve the main
problem, because the manuscript still lacks a proof that the bridge-free
hypotheses persist from the fixed small chain lengths arising in the earlier
far-tail reductions.

No external literature refresh was performed in this round; the Round 276
source check remains the latest external status.
