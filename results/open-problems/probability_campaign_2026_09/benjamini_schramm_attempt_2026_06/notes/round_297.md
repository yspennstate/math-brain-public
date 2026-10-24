# Round 297

Round 297 absorbs the remaining chain sums in the wide-residual normal form.

The new general corollary is
```tex
\begin{corollary}[Locally short staircase chains are prefix-record spread]
\label{cor:locally-short-staircase-chains-are-prefix-record-spread}
```
It observes that every ordinary locally short staircase-chain profile already
has more than
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H
\]
admissible start levels.  The first run at each admissible start is a
prefix-record outward crossing run.  Hence
\[
  P^{\rm chain}_{j,K,L,\ell}
  \le
  P^{\rm pre,out,rec}_{j,K,L}.
\]

The packaged consequence is
```tex
\begin{corollary}[Wide residual normal form with chain branches absorbed]
\label{cor:wide-residual-normal-form-with-chain-branches-absorbed}
```
For a wide residual entry, one of three alternatives now holds:

1. initial counting saturation;
2. a reduced bridge packet,
   \[
   P^{\rm chain}_{j,K_r,L,\ell_r}
   \le
   \ell_r P^{\rm pre,out,rec}_{j,K_{r+1},L}
   +
   \sum_{g\in\mathcal G_r}P^{\rm bridge,free}_{j,2K_{r+1},L,g}
   +
   \sum_{g\in\mathcal G_r}X^{\rm ret,spr}_{j,2K_{r+1}(g-1)};
   \]
3. a reduced large-window packet,
   \[
   P^{\rm chain}_{j,K_r,L,\ell_r}
   \le
   B_r P^{\rm pre,out,rec}_{j,K_{r+1},L}.
   \]

The coefficients and index sets are subexponential: \(\ell_r\le W_{\beta,p}\),
\(B_r<W_{\beta,p}\), and \(|\mathcal G_r|\le W_{\beta,p}\).

Thus, outside initial counting saturation, the wide-residual normal form now
reduces to prefix-record outward-spread, inward-free bridge, and spread-return
profiles.  The large-window branch no longer contributes a new chain residual,
and the bridge branch no longer leaves its chain-child sum unreduced.
