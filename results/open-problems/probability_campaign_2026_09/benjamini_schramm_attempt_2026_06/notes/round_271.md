# Round 271

Round 271 attacks the third option left by Rounds 269--270: direct handling of
the accumulated chain-bridge packets.

The first new manuscript corollary is

```tex
\begin{corollary}[Staircase-chain bridges project to ordinary bridges]
\label{cor:staircase-chain-bridges-project-to-ordinary-bridges}
```

If a confined staircase-chain bridge has lower-chain length \(\ell\) and
fixed gap \(h\ge\ell+1\), then the last lower-chain run at level
\[
  U=u+\ell-1
\]
and the first upper-chain run at level
\[
  U+(h-\ell+1)=u+h
\]
form an ordinary confined fixed-gap bridge.  The shift \(u\mapsto U\) is
injective and stays inside the slab because the lower chain already requires
all levels \(u,\ldots,u+\ell-1\) to belong to \(A_{j,p}\).  Hence
\[
  P^{\rm stair,loc,chain,bridge}_{j,K,L,\ell,h}
  \le
  P^{\rm bridge}_{j,K,L,h-\ell+1}.
\]

The second new manuscript corollary is

```tex
\begin{corollary}[Multiplicity-free chain amplification with ordinary bridges]
\label{cor:multiplicity-free-chain-amplification-with-ordinary-bridges}
```

Combining the projection with the multiplicity-free finite chain amplification
gives
\[
\begin{aligned}
  P^{\rm chain}_{j,K,L,\ell}
  \le&
  \sum_{a\in I_n(\ell)}P^{\rm chain}_{j,K_n,L,a}
\\
  &+
  \sum_{r=1}^n
  \sum_{g=2}^{B_r-\ell-r+2}
  P^{\rm bridge}_{j,K_r,L,g}.
\end{aligned}
\]

This removes the accumulated staircase-chain bridge profiles as a separate
residual family.  The remaining obstruction is now sharper: for growing depth,
one needs terminal-chain exhaustion plus exponent control for ordinary
confined bridges with the stage-dependent depth parameters \(K_r\) and gap
ranges \(2\le g\le B_r-\ell-r+2\).

No external literature refresh was performed in this round; the Round 270
status remains the latest source-checked external status.
