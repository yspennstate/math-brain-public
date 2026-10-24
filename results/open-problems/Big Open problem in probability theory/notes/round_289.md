# Round 289

Round 289 removes the remaining slab-level start choice from the large-window
finite-start branch.

The new definition is

```tex
\begin{definition}[Exact-start chain profiles]
\label{def:exact-start-locally-short-staircase-chain-profiles}
```

It fixes the chain start \(u\) and then takes a supremum over
\(u\in A_{j,p}\cap\mathbb N\), matching the exact-level profile pattern used
elsewhere for exterior returns and same-sphere congestion.

The two new corollaries are

```tex
\begin{corollary}[Few-start chains localize to exact starts]
\label{cor:few-start-chains-localize-to-exact-starts}
```

and

```tex
\begin{corollary}[Large-window branch localizes to exact starts]
\label{cor:large-window-branch-localizes-to-exact-starts}
```

The first says that a few-start chain profile is bounded by
\[
  W_{\beta,p}
  P^{\rm chain,exact}_{j,K,L,\ell},
\]
because at least one admissible start exists and there are at most
\(W_{\beta,p}\) possible starts in the slab.

Combining this with Round 288 gives, in the last valid large-window branch,
\[
  P^{\rm chain}_{j,K_r,L,\ell_r}
  \le
  5W_{\beta,p}
  \sum_{h=1}^{B_r}
  P^{\rm chain,exact}_{j,K_{r+1},L,\ell_r+h}.
\]
Since \(B_r<W_{\beta,p}\), the expanded union cost is at most
\[
  \log_{D_H}(5W_{\beta,p}^2)=o(L_H).
\]

Thus the large-window branch is now reduced to uniform bounds on exact-start
chain profiles over a subexponential child family.  The residual-width drop
for the child with \(h=B_r\) is unchanged.

No external literature refresh was performed in this round; the Round 285
source check remains the latest external status.
