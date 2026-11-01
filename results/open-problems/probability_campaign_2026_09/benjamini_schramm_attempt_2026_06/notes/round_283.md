# Round 283

Round 283 refines the counting-saturation side of the Round 281
first-obstruction dichotomy.

The new corollary is

```tex
\begin{corollary}[First counting saturation has a last large bridge-free step]
\label{cor:first-counting-saturation-has-last-large-bridge-free-step}
```

Let
\[
  T_{\lambda,\sigma,\beta,p}
  =
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H.
\]
If the first obstruction index \(r_*\) satisfies
\[
  K_{r_*}\ge T_{\lambda,\sigma,\beta,p},
\]
then either \(r_*=0\), so the initial chain profile is already outside the
successor-counting range, or the predecessor \(r_0=r_*-1\) is still valid:
\[
  K_{r_0}<T_{\lambda,\sigma,\beta,p},
  \qquad
  B_{r_0}\le\ell_{r_0}.
\]
In the latter case the predecessor step is bridge-free:
\[
  P^{\rm chain}_{j,K_{r_0},L,\ell_{r_0}}
  \le
  \sum_{h=1}^{B_{r_0}}
  P^{\rm chain}_{j,K_{r_*},L,\ell_{r_0}+h}.
\]
Since \(K_{r_*}=2K_{r_0}B_{r_0}\), counting saturation gives
\[
  B_{r_0}
  \ge
  \frac{\theta_{\lambda,\sigma,\beta}}{32K_{r_0}}L_H.
\]
Thus a non-initial counting-saturation obstruction is not abrupt: it is
preceded by a bridge-free one-step packet with an \(L_H/K_{r_0}\)-scale
successor window.  The largest increment in that packet reduces residual
width by at least this amount, up to truncation at zero.

No external literature refresh was performed in this round; the Round 276
source check remains the latest external status.
