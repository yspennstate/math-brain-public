# Round 294

Round 294 sharpens the short exact-start exception set from Round 293.

The new corollary is
```tex
\begin{corollary}[Threshold-tight short exact-start exceptions]
\label{cor:threshold-tight-short-exact-start-exceptions}
```
Instead of keeping every child of total length at most \(4\), it keeps only
the increments
\[
  \mathcal E_r
  =
  \left\{
    h\in\{1,\ldots,B_r\}:
    \ell_r+h\le
    \frac{\theta_{\lambda,\sigma,\beta}}{4K_{r+1}}L_H
  \right\}.
\]
Every child outside \(\mathcal E_r\) is absorbed by the prefix-record
outward-spread profile using the exact-start-to-record-spread lemma from
Round 293.

Because the large-window branch has
\[
  K_{r+1}\ge\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H ,
\]
one has \(\mathcal E_r\subseteq\mathcal S_r\), where
\(\mathcal S_r=\{h:\ell_r+h\le4\}\).  Hence \(|\mathcal E_r|\le2\).
The sharper threshold also gives:

- \(\mathcal E_r=\varnothing\) if
  \[
    K_{r+1}>
    \frac{\theta_{\lambda,\sigma,\beta}}{12}L_H ;
  \]
- a length-four exception can occur only at exact saturation
  \[
    K_{r+1}=
    \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H ;
  \]
- all exceptions occur in the narrow window
  \[
    \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H
    \le K_{r+1}
    \le
    \frac{\theta_{\lambda,\sigma,\beta}}{12}L_H .
  \]

The exceptional exact-start coefficient remains at most \(10W_{\beta,p}\),
and the prefix-record coefficient remains at most \(5W_{\beta,p}^2\), so the
large-window cost is still subexponential on the \(L_H\) scale.
