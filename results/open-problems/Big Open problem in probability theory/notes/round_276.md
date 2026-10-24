# Round 276

Round 276 sharpens the successor-gap count by using the residual width
available to chain starts.

The new lemma is

```tex
\begin{lemma}[Residual-width successor-gap count for chains]
\label{lem:residual-width-successor-gap-count-for-chains}
```

For a locally short chain of length \(\ell\), not every level in the heavy
slab can be a chain start.  The start \(u\) must satisfy
\[
  u,u+1,\ldots,u+\ell-1\in A_{j,p}\cap\mathbb N.
\]
Thus the available start width is
\[
  R_{\ell,p}=\max\{W_{\beta,p}-\ell+1,0\},
\]
not the whole slab width \(W_{\beta,p}\).  The successor-gap cutoff can
therefore be replaced by
\[
  B^{\rm res}_{K,\ell,p}
  =
  \left\lceil
    \frac{16K R_{\ell,p}}{\theta_{\lambda,\sigma,\beta}L_H}
  \right\rceil+1.
\]
As long as the counting range
\(\theta_{\lambda,\sigma,\beta}L_H/(16K)>1\) holds, a chain profile with
parameters \((K,L,\ell)\) implies a bounded-gap chain-pair profile with
parameters \((2K,L,\ell,B^{\rm res}_{K,\ell,p})\).

The near-top corollary is

```tex
\begin{corollary}[Near-top chains have bounded residual successor cutoffs]
\label{cor:near-top-chains-have-bounded-residual-successor-cutoffs}
```

If \(R_{\ell,p}\le C L_H/K\), then the residual cutoff is bounded by the
constant
\[
  B_C=
  \left\lceil
    \frac{16C}{\theta_{\lambda,\sigma,\beta}}
  \right\rceil+1,
\]
independent of \(p\).  This identifies a useful near-top regime: once the
chain length is within \(O(L_H/K)\) of exhausting the slab, the successor step
has bounded gap cost.

This does not yet close the proof.  The missing step is still a mechanism
that drives a fixed initial chain length into that near-top regime without
the existing rapidly growing \(K\)-loss.

External status was refreshed this round.  The current search found no
announced proof of the full Benjamini--Schramm non-uniqueness conjecture for
all nonamenable quasi-transitive graphs, nor of the stronger general target
\(p_c(G)<p_{2\to2}(G)\).  The visible recent sources remain partial or
adjacent.
