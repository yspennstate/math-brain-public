# Round 290

Round 290 sharpens the exact-start localization cost from slab width to
residual start width.

The strengthened corollary is still

```tex
\begin{corollary}[Few-start chains localize to exact starts]
\label{cor:few-start-chains-localize-to-exact-starts}
```

but it now uses
\[
  R_{\ell,p}=\max\{W_{\beta,p}-\ell+1,0\}
\]
instead of \(W_{\beta,p}\).  A length-\(\ell\) chain start must satisfy
\[
  u,u+1,\ldots,u+\ell-1\in A_{j,p}\cap\mathbb N,
\]
so there are at most \(R_{\ell,p}\) possible exact starts in the slab.
Thus
\[
  P^{\rm chain,qstart}_{j,K,L,\ell,q}
  \le
  R_{\ell,p}\,
  P^{\rm chain,exact}_{j,K,L,\ell}.
\]

The large-window exact-start reduction is now
\[
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le
  \sum_{h=1}^{B_r}
  5R_{\ell_r+h,p}\,
  P^{\rm chain,exact}_{j,K_{r+1},L,\ell_r+h},
\]
with
\[
  R_{\ell_r+h,p}=\max\{R_{\ell_r,p}-h,0\}.
\]
The expanded cost is bounded by
\[
  5\sum_{h=1}^{B_r}R_{\ell_r+h,p}\le 5W_{\beta,p}^2,
\]
so it is still subexponential, but it now records the residual-width drop
across the child family rather than paying the full slab-width cost for
every child.

No external literature refresh was performed in this round; the Round 285
source check remains the latest external status.
