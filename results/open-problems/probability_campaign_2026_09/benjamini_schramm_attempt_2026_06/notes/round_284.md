# Round 284

Round 284 packages the first-obstruction analysis into a single normal-form
corollary.

The new corollary is

```tex
\begin{corollary}[Wide residual first-obstruction normal form]
\label{cor:wide-residual-first-obstruction-normal-form}
```

For a wide residual entry,
\[
  R=R_{\ell,p}\ge1,\qquad
  4^{R-1}K\ge
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
\]
the unit residual branch satisfies one of three alternatives:

1. Initial saturation:
\[
  K\ge \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H.
\]

2. Ordinary bridge packet: for some \(r<R\),
\[
  K_r<\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
  \qquad B_r>\ell_r,
\]
and the chain profile at \((K_r,\ell_r)\) is bounded by longer chain
profiles plus ordinary confined bridge profiles.

3. Last valid large-window step: for some \(r<R-1\),
\[
  K_r<\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
  \qquad B_r\le\ell_r,\qquad
  K_{r+1}\ge \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
\]
and the bridge-free successor window obeys
\[
  B_r\ge
  \frac{\theta_{\lambda,\sigma,\beta}}{32K_r}L_H.
\]

This packages Rounds 281--283 into a single citation target.  Wide residual
entries now reduce to initial loss of the counting range, an ordinary
confined-bridge packet, or the last bridge-free large-window step before
counting saturation.

No external literature refresh was performed in this round; the Round 276
source check remains the latest external status.
