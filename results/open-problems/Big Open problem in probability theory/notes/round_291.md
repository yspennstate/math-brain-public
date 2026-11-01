# Round 291

Round 291 extracts a low-residual tail from the residual-weighted exact-start
large-window branch.

The new corollary is

```tex
\begin{corollary}[Large-window exact-start branch has a low-residual tail]
\label{cor:large-window-exact-start-branch-has-low-residual-tail}
```

Set
\[
  t_r=\left\lceil \frac{B_r}{2}\right\rceil .
\]
Starting from the Round 290 exact-start reduction, split the child sum into
the prefix \(1\le h<t_r\) and the tail \(t_r\le h\le B_r\).  The tail has
uniform residual factor
\[
  R_{\ell_r+h,p}\le \max\{R_{\ell_r,p}-t_r,0\}.
\]
Since the large-window branch has
\[
  B_r\ge
  \frac{\theta_{\lambda,\sigma,\beta}}{32K_r}L_H,
\]
the tail children all satisfy
\[
  R_{\ell_r+h,p}
  \le
  \max\left\{
    R_{\ell_r,p}
    -
    \frac{\theta_{\lambda,\sigma,\beta}}{64K_r}L_H,
    0
  \right\}.
\]

Thus the exact-start branch now separates into a prefix packet and a tail
packet where every child has an explicit \(L_H/K_r\)-scale residual drop.
The total expanded cost remains at most \(5W_{\beta,p}^2\), hence
subexponential.

No external literature refresh was performed in this round; the Round 285
source check remains the latest external status.
