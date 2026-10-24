# Round 275

Round 275 adds the chain analogue of the fixed-gap bridge start-count cutoff.

The new cutoff is

```tex
\begin{lemma}[Long chains do not have enough slab starts]
\label{lem:long-chains-do-not-have-enough-slab-starts}
```

A locally short staircase chain of length \(\ell\) inside one heavy slab must
start at a level \(u\) such that
\[
  u,u+1,\ldots,u+\ell-1
\]
all lie in the slab.  Thus there are at most
\[
  \max\{W_{\beta,p}-\ell+1,0\}
\]
possible starts.  The chain profile requires strictly more than
\(\theta_{\lambda,\sigma,\beta}L_H/(4K)\) counted starts, so the profile is
zero whenever
\[
  W_{\beta,p}-\ell+1
  \le
  \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H.
\]
In particular, chain lengths \(\ell>W_{\beta,p}\) cannot occur inside one
slab.

This cutoff is pushed through the Round 274 bridge-free finite chain
reduction in

```tex
\begin{corollary}[Start-count truncation of bridge-free finite chains]
\label{cor:start-count-truncation-bridge-free-finite-chains}
```

The terminal amplified chain sum is restricted to
\[
  a<
  W_{\beta,p}+1-\frac{\theta_{\lambda,\sigma,\beta}}{4K_n}L_H.
\]
The bridge-derived chain residuals already have their slab-count truncation
from the bridge gap cutoff:
\[
  2\le g\le B_r-\ell-r+2,\qquad
  g<W_{\beta,p}-\frac{\theta_{\lambda,\sigma,\beta}}{4K_r}L_H.
\]
Thus the top
\(\theta_{\lambda,\sigma,\beta}L_H/(4K_n)\) portion of terminal chain lengths
does not contribute to the bridge-free finite chain reduction.

No external literature refresh was performed in this round; the Round 270
status remains the latest source-checked external status.
