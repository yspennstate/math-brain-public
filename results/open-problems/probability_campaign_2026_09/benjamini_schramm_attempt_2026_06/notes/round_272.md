# Round 272

Round 272 adds a deterministic support cutoff for ordinary confined
fixed-gap bridge profiles.

The new manuscript lemma is

```tex
\begin{lemma}[Large fixed gaps do not have enough slab starts]
\label{lem:large-fixed-gaps-do-not-have-enough-slab-starts}
```

For an ordinary bridge of fixed gap \(h\), counted starts \(u\) must satisfy
both \(u\in A_{j,p}\) and \(u+h\in A_{j,p}\).  A slab has at most
\(W_{\beta,p}\) integer levels, so there are at most
\[
  \max\{W_{\beta,p}-h,0\}
\]
possible lower starts.  Therefore the bridge property is empty whenever
\[
  W_{\beta,p}-h\le
  \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H.
\]
In particular, the bridge profile is zero for \(h\ge W_{\beta,p}\).

The new follow-up corollary is

```tex
\begin{corollary}[Ordinary-bridge truncation in finite chain amplification]
\label{cor:ordinary-bridge-truncation-in-finite-chain-amplification}
```

It refines the Round 271 ordinary-bridge amplification to
\[
\begin{aligned}
  P^{\rm chain}_{j,K,L,\ell}
  \le&
  \sum_{a\in I_n(\ell)}P^{\rm chain}_{j,K_n,L,a}
\\
  &+
  \sum_{r=1}^n
  \sum_{\substack{2\le g\le B_r-\ell-r+2\\
        g<W_{\beta,p}-\theta_{\lambda,\sigma,\beta}L_H/(4K_r)}}
  P^{\rm bridge}_{j,K_r,L,g}.
\end{aligned}
\]

This does not solve the bridge estimates, but it prevents the growing
cutoffs \(B_r\) from forcing genuinely new bridge gaps beyond the slab scale.
Any growing-depth bridge-control criterion may now be stated over
\(O(W_{\beta,p})=O(L_H)\) possible gaps at each stage, with a small additional
boundary exclusion when \(K_r\) is not too large.

No external literature refresh was performed in this round; the Round 270
status remains the latest source-checked external status.
