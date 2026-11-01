# Round 269

Round 269 quantifies the obstruction identified in Round 268.

If a finite chain-amplification iteration remains inside the
successor-counting range at every step, then
\[
  K_{r-1}<\frac{\theta_{\lambda,\sigma,\beta}}{16}L_H
  \qquad(1\le r\le n).
\]
But the depth recursion also has the uniform lower bound
\[
  K_r=2K_{r-1}B_r\ge4K_{r-1}.
\]
Therefore
\[
  4^{n-1}K_0
  <
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H
\]
and all terminal lengths \(a\in I_n(\ell)\) satisfy
\[
  a\le2^n\ell
  \le
  \ell\sqrt{\frac{\theta_{\lambda,\sigma,\beta}}{4K_0}L_H}.
\]

Since \(W_{\beta,p}\asymp L_H\), these terminal lengths are still below the
slab width for all \(p\) sufficiently close to \(p_c(H)\).  Thus the
slab-width support cutoff cannot be reached by any iteration that remains
valid under the current successor-counting proof.

This confirms that the chain program needs a new ingredient: smaller
\(K\)-loss in successor extraction, a restart/renormalization of the counted
start lower bound after \(K_r\) grows, or a direct estimate for the accumulated
bridge residuals.

No external open-status search was refreshed in this round.
