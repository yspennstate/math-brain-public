# Round 292

Round 292 refines the single low-residual tail into dyadic residual layers.

The new corollary is

```tex
\begin{corollary}[Dyadic residual layers for the exact-start branch]
\label{cor:dyadic-residual-layers-exact-start-branch}
```

It defines
\[
  M_r=\max\{1,\lceil\log_2 B_r\rceil\},\qquad
  s_{r,0}=B_r+1,\qquad
  s_{r,m}=\left\lceil\frac{B_r}{2^m}\right\rceil .
\]
The intervals
\[
  I_{r,m}=\{s_{r,m},\ldots,s_{r,m-1}-1\}
\]
partition \(\{1,\ldots,B_r\}\).  The large-window exact-start branch is
bounded by
\[
  5\sum_{m=1}^{M_r}
  \max\{R_{\ell_r,p}-s_{r,m},0\}
  \sum_{h\in I_{r,m}}
  P^{\rm chain,exact}_{j,K_{r+1},L,\ell_r+h}.
\]

Every child in layer \(m\) has residual width at most
\[
  \max\left\{
    R_{\ell_r,p}
    -
    \frac{\theta_{\lambda,\sigma,\beta}}{2^{m+5}K_r}L_H,
    0
  \right\}.
\]
The expanded cost remains at most \(5W_{\beta,p}^2\), so the dyadic
decomposition does not add exponent loss.

No external literature refresh was performed in this round; the Round 285
source check remains the latest external status.
