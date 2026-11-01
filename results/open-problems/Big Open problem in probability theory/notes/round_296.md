# Round 296

Round 296 removes the finite surplus-start exceptions from Round 295.

The new general corollary is
```tex
\begin{corollary}[Surplus-start chains are record spread]
\label{cor:surplus-start-chains-are-record-spread}
```
It says that if a \(q\)-start chain profile satisfies
\[
  q>\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H ,
\]
then the \(q\) distinct chain start levels themselves already witness the
prefix-record outward-spread profile.  No chain-length lower bound is needed:
the first run at each admissible start is a record, locally short,
endpoint-clear outward crossing level.

The large-window consequence is
```tex
\begin{corollary}[Large-window few-start branch collapses to record spread]
\label{cor:large-window-few-start-branch-collapses-to-record-spread}
```
In the large-window branch,
\[
  q_{r,p}=
  \left\lfloor
    \frac{\theta_{\lambda,\sigma,\beta}}{4K_{r+1}}L_H
  \right\rfloor+1
\]
is strictly larger than the prefix-record threshold at parameter
\(K_{r+1}\).  Therefore every few-start child is already a prefix-record
outward-spread event, and
\[
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le
  B_r\,P^{\rm pre,out,rec}_{j,K_{r+1},L}.
\]
Since \(B_r<W_{\beta,p}\), this adds only a subexponential coefficient.

Thus the large-window branch no longer leaves any new exact-start or
surplus-start chain residual.  It returns to the existing prefix-record
reduction tree with a single \(W_{\beta,p}\)-scale coefficient.
