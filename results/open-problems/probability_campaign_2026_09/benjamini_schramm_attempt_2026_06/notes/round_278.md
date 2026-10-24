# Round 278

Round 278 isolates the bridge-free part of the residual-width one-step
amplification.

The new corollary is

```tex
\begin{corollary}[Bridge-free residual descent near the slab top]
\label{cor:bridge-free-residual-descent-near-slab-top}
```

If the residual cutoff satisfies
\[
  B^{\rm res}_{K,\ell,p}\le \ell,
\]
then the residual-width one-step amplification has no confined
staircase-chain bridge residuals:
\[
  P^{\rm chain}_{j,K,L,\ell}
  \le
  \sum_{h=1}^{B^{\rm res}_{K,\ell,p}}
  P^{\rm chain}_{j,K^{\rm res}_{K,\ell,p},L,\ell+h}.
\]

Every displayed chain term strictly descends in residual start width:
\[
  R_{\ell+h,p}
  =
  \max\{R_{\ell,p}-h,0\}
  \le
  \max\{R_{\ell,p}-1,0\}.
\]
Thus once the chain length is close enough to the slab top, the one-step
move is both bridge-free and moves the chain closer to the start-count
vanishing threshold.

A sufficient condition for bridge-free descent is
\[
  R_{\ell,p}\le
  \frac{\theta_{\lambda,\sigma,\beta}(\ell-1)}{16K}L_H .
\]
Equivalently, in the near-top notation \(R_{\ell,p}\le C L_H/K\), it is
enough that
\[
  C\le \frac{\theta_{\lambda,\sigma,\beta}(\ell-1)}{16}.
\]

This still does not close the proof.  The new result identifies a clean
bridge-free descent regime, but the unresolved step remains how to enter
that regime from fixed initial chain lengths without losing the available
counting range.

No external literature refresh was performed in this round; the Round 276
source check remains the latest external status.
