# Round 273

Round 273 splits the ordinary bridge residuals left by Rounds 271--272 into
an inward-free bridge residual and an existing spread exterior-return
residual.

The new bridge definition is

```tex
\begin{definition}[Inward-free confined fixed-gap bridge profiles]
\label{def:inward-free-confined-fixed-gap-bridge-profiles}
```

It records confined fixed-gap bridge witnesses for which the radial distance
never decreases between the end of the lower record run and the start of the
upper record run:
\[
  d(x,v_{t+1})\ge d(x,v_t)\qquad(b\le t<a').
\]

The new split is

```tex
\begin{corollary}[Confined bridges are inward-free or returning]
\label{cor:confined-bridges-inward-free-or-returning}
```

For fixed gap \(h\),
\[
  P^{\rm bridge}_{j,K,L,h}
  \le
  P^{\rm bridge,free}_{j,2K,L,h}
  +
  X^{\rm ret,spr}_{j,\,2K\max\{h-1,1\}}.
\]

Reason: if more than half of the counted bridge starts have inward-free
witnesses, the first term holds.  Otherwise, each remaining start has an
inward token at an intermediate level \(w\in(u,u+h)\).  The standard inward
token lemma gives an exterior return through \(w\).  For fixed \(w\), at most
\(\max\{h-1,1\}\) lower starts \(u\) can satisfy \(u<w<u+h\), so the returns
spread over enough distinct levels.

The split is then pushed through the Round 272 truncated finite chain
amplification:
\[
\begin{aligned}
  P^{\rm chain}_{j,K,L,\ell}
  \le&
  \sum_{a\in I_n(\ell)}P^{\rm chain}_{j,K_n,L,a}
\\
  &+
  \sum_{r=1}^n
  \sum_g
  P^{\rm bridge,free}_{j,2K_r,L,g}
  +
  \sum_{r=1}^n
  \sum_g
  X^{\rm ret,spr}_{j,2K_r(g-1)},
\end{aligned}
\]
where the \(g\)-range is the slab-truncated range from Round 272:
\[
  2\le g\le B_r-\ell-r+2,\qquad
  g<W_{\beta,p}-\theta_{\lambda,\sigma,\beta}L_H/(4K_r).
\]

This leaves inward-free confined bridges as the genuinely new bridge object.
All bridge witnesses with radial backtracking are absorbed into the existing
spread-return profile family.

No external literature refresh was performed in this round; the Round 270
status remains the latest source-checked external status.
