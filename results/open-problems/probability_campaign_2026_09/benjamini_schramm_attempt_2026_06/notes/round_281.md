# Round 281

Round 281 turns the logarithmic obstruction into a first-obstruction
alternative along the unit residual-descent branch.

The new corollary is

```tex
\begin{corollary}[Wide residual entry forces a first descent obstruction]
\label{cor:wide-residual-entry-forces-first-descent-obstruction}
```

Write \(R=R_{\ell,p}\), and suppose the residual entry is wider than the
logarithmic threshold:
\[
  4^{R-1}K
  \ge
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H.
\]
Along the all-ones branch define
\[
  \ell_r=\ell+r,\qquad K_0=K,\qquad
  B_r=B^{\rm res}_{K_r,\ell_r,p},\qquad
  K_{r+1}=2K_rB_r.
\]
Since \(R_{\ell_r,p}=R-r>0\) for \(0\le r\le R-1\), every \(B_r\ge2\), and
hence \(K_{R-1}\ge4^{R-1}K\).  Thus some first index
\(r_*<R\) must either leave the counted-start range,
\[
  K_{r_*}\ge
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
\]
or leave the bridge-free range,
\[
  B_{r_*}>\ell_{r_*}.
\]

Before \(r_*\), the bridge-free residual descent is valid along the unit
branch.  If the first obstruction is not counting saturation, then the
residual-width one-step amplification at \((K_{r_*},\ell_{r_*})\) has a
non-empty confined chain-bridge sum.  This converts the previous negative
obstruction into a concrete dichotomy: wide residual entries force either a
counting-range saturation node or a genuine bridge packet before residual
exhaustion.

No external literature refresh was performed in this round; the Round 276
source check remains the latest external status.
