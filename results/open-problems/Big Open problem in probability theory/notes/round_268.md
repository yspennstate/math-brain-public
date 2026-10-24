# Round 268

Round 268 audits the counting range behind the one-step chain amplification.

The bounded-successor-gap step starts with
\[
  N_\star>\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H
\]
chain-start levels in one slab.  The proof loses at most
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{16K}L_H
\]
successor gaps to gaps larger than
\[
  B_{\lambda,\sigma,\beta,K}
  =
  \left\lceil
    \frac{16K\beta}{\theta_{\lambda,\sigma,\beta}}
  \right\rceil+1.
\]
It therefore forces more than
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{8K}L_H
\]
bounded successor gaps only while
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{16K}L_H>1.
\]

This matters for the Round 267 slab-width cutoff.  Although terminal chains
vanish when their length exceeds \(W_{\beta,p}\asymp L_H\), the recursive
chain-amplification depth parameter grows as
\[
  K_r=2K_{r-1}B_r,\qquad
  B_r\gtrsim K_{r-1}.
\]
Thus a naive choice of depth \(n\asymp W_{\beta,p}\) exits the range in which
the current counting argument guarantees successor pairs.  The next proof
work must either keep the effective \(K_r\) below this range, find additional
successor-pair mass after \(K_r\) is large, or amplify chain length with a
smaller depth-parameter loss.

No external open-status search was refreshed in this round.
