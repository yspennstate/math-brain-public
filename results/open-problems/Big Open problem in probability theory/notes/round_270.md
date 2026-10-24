# Round 270

Round 270 tests the first proposed escape from the Round 269 obstruction:
remove the fixed-gap pigeonhole loss and keep only the unavoidable successor
count loss.

The new manuscript lemma is

```tex
\begin{lemma}[Ideal doubled-count exhaustion has a constant obstruction]
\label{lem:ideal-doubling-loss-exhaustion-obstruction}
```

It considers the optimistic recursion \(K_r^{\rm id}=2^rK\), which is what
would remain if a lower-loss successor extraction avoided the current
\(K\mapsto KB\) fixed-gap pigeonhole.  If an ideal iteration both stays in the
successor-counting range
\[
  2^{r-1}K<\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H
\]
and reaches the slab cutoff
\[
  2^n\ell>W_{\beta,p},
\]
then necessarily
\[
  K\beta\le\frac{\theta_{\lambda,\sigma,\beta}}8\ell .
\]

The follow-up remark applies this diagnostic to the raw chain terms in the
finite far-tail ladder.  For \(q\in\{3,4\}\) and
\[
  K_{i,0}^{\rm ch}=512M_iB_iC_i,
\]
the ideal route would still need
\[
  512M_iB_iC_i\,\beta_i
  \le
  \frac{\theta_{\lambda_i,\sigma_i,\beta_i}}8q.
\]
This constant inequality is not supplied by the existing reductions.

Interpretation: simply replacing \(K\mapsto2KB\) by \(K\mapsto2K\) is not a
robust enough new ingredient.  A viable route must also improve the initial
depth-to-length ratio, restart the counted-start supply with a fresh ratio, or
estimate bridge packets directly.

External status was refreshed during this round.  The search found current
partial progress around the same conjectural landscape, including Hutchcroft's
\(L^2\) boundedness condition, Hutchcroft--Pan's threshold examples, and Li's
2026 planar-site/end-structure work, but no general solution of the
nonamenable quasi-transitive Bernoulli bond-percolation nonuniqueness
conjecture or of the stronger target \(p_c(G)<p_{2\to2}(G)\).
