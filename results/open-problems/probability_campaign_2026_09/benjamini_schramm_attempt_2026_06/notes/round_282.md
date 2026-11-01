# Round 282

Round 282 refines the bridge-active side of the Round 281 first-obstruction
dichotomy.

The new corollary is

```tex
\begin{corollary}[First bridge-active obstruction projects to ordinary bridges]
\label{cor:first-bridge-active-obstruction-projects-to-ordinary-bridges}
```

At the first obstruction index \(r_*\), if the counting range still holds,
\[
  K_{r_*}<
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H,
\]
then the obstruction must be bridge-active:
\[
  B_{r_*}>\ell_{r_*}.
\]
The residual-width one-step amplification at
\((K_{r_*},\ell_{r_*})\) is then bounded by longer chain profiles plus
ordinary confined bridge profiles:
\[
\begin{aligned}
  P^{\rm chain}_{j,K_{r_*},L,\ell_{r_*}}
  \le&
  \sum_{h=1}^{\ell_{r_*}}
  P^{\rm chain}_{j,K_{r_*+1},L,\ell_{r_*}+h}
\\
  &+
  \sum_{g=2}^{B_{r_*}-\ell_{r_*}+1}
  P^{\rm bridge}_{j,K_{r_*+1},L,g}.
\end{aligned}
\]
This uses the existing projection from confined staircase-chain bridges to
ordinary confined fixed-gap bridges, with \(g=h-\ell_{r_*}+1\).

The bridge-active condition also forces the quantitative lower bound
\[
  R_{\ell_{r_*},p}>
  \frac{\theta_{\lambda,\sigma,\beta}(\ell_{r_*}-1)}
       {16K_{r_*}}L_H.
\]
Thus the bridge branch in the first-obstruction alternative is not a new
object: it is an ordinary confined-bridge packet appearing exactly when the
current residual width remains too large for bridge-free descent.

No external literature refresh was performed in this round; the Round 276
source check remains the latest external status.
