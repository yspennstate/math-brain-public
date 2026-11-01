# Round 287

Round 287 refines the last valid large-window branch of the Round 284 normal
form.

The new corollary is

```tex
\begin{corollary}[Large-window branch has subexponential child cost]
\label{cor:large-window-branch-has-subexponential-child-cost}
```

If the normal form lands in the last valid large-window step at index \(r\),
then
\[
  B_r\le \ell_r<W_{\beta,p}.
\]
Thus the bridge-free child sum contains at most \(W_{\beta,p}\) profiles, and
\[
  \frac{\log_{D_H} W_{\beta,p}}{L_H}\to0
  \qquad(p\uparrow\pc(H)).
\]
Consequently a uniform logarithmic exponent bound over the child profiles
\[
  P^{\rm chain}_{j,K_{r+1},L,\ell_r+h},
  \qquad 1\le h\le B_r,
\]
implies the same exponent bound for the parent profile
\[
  P^{\rm chain}_{j,K_r,L,\ell_r}.
\]
The largest child still has the residual-width drop from the normal form:
\[
  R_{\ell_r+B_r,p}
  \le
  \max\left\{
    R_{\ell_r,p}
    -
    \frac{\theta_{\lambda,\sigma,\beta}}{32K_r}L_H,
    0
  \right\}.
\]

No external literature refresh was performed in this round; the Round 285
source check remains the latest external status.
