# Round 274

Round 274 removes the inward-free bridge family as an independent residual.

The new local reduction is

```tex
\begin{corollary}[Inward-free bridges are chains or long runs]
\label{cor:inward-free-bridges-are-chains-or-long-runs}
```

An inward-free confined bridge of gap \(h\) is radially nondecreasing between
the lower record run and the upper record run.  Hence it passes through each
intermediate level \(u+1,\ldots,u+h-1\) in order.  The intermediate level
runs are record and persistent, and they are consecutive.  Therefore either
all intermediate runs have length at most \(L\), giving a locally short
staircase chain of length \(h+1\), or some intermediate level has a long
tangential run.  In profile form,
\[
  P^{\rm bridge,free}_{j,K,L,h}
  \le
  P^{\rm chain}_{j,K,L,h+1}
  +
  W_{\beta,p}T^{\rm long}_{j,L}.
\]

Pushing this through the Round 273 finite chain amplification gives

```tex
\begin{corollary}[Finite chain amplification with chain-only bridge residuals]
\label{cor:finite-chain-amplification-with-chain-only-bridge-residuals}
```

The bridge residuals are now replaced by:

- terminal amplified chain profiles \(P^{\rm chain}_{j,K_n,L,a}\),
- additional slab-truncated chain profiles \(P^{\rm chain}_{j,2K_r,L,g+1}\),
- spread-return profiles \(X^{\rm ret,spr}_{j,2K_r(g-1)}\),
- and a long-run term with coefficient \(nW_{\beta,p}^2\).

For fixed \(n\), the factor \(nW_{\beta,p}^2\) is exponent-negligible because
\(\log W_{\beta,p}=o(L_H)\).  The direct bridge route has therefore been
converted into a chain-and-return route.  The remaining obstruction is to
control the new p-dependent family of chain profiles with lengths
\[
  3\le g+1\le W_{\beta,p}
\]
and parameters \(2K_r\), together with the already-existing return profiles.

No external literature refresh was performed in this round; the Round 270
status remains the latest source-checked external status.
