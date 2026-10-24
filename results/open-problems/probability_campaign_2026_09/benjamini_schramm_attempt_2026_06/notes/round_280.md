# Round 280

Round 280 records the depth obstruction for the conditional bridge-free
residual descent iteration.

The new lemma is

```tex
\begin{lemma}[Bridge-free residual exhaustion has logarithmic depth obstruction]
\label{lem:bridge-free-residual-exhaustion-logarithmic-obstruction}
```

If the finite bridge-free residual descent hypotheses persist long enough to
exhaust the initial residual width \(R_{\ell,p}\), then necessarily
\[
  4^{R_{\ell,p}-1}K
  <
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H.
\]
Equivalently,
\[
  R_{\ell,p}
  <
  1+
  \log_4\!\left(
    \frac{\theta_{\lambda,\sigma,\beta}L_H}{16K}
  \right).
\]

The proof follows the all-ones branch of the descent tree.  As long as the
residual width is positive, the residual cutoff satisfies
\[
  B^{\rm res}_{K(\mathbf h),\ell(\mathbf h),p}\ge2,
\]
so the depth parameter grows by at least a factor \(4\) at each step:
\[
  K(\mathbf h\frown1)\ge4K(\mathbf h).
\]
At depth \(R_{\ell,p}-1\), the all-ones branch still has positive residual
width, and the counting-range hypothesis forces
\[
  K(\mathbf 1_{R_{\ell,p}-1})
  <
  \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H.
\]
Combining these two facts gives the obstruction.

This shows that the present bridge-free descent recursion can only certify
residual exhaustion once the entry residual width is already \(O(\log L_H)\).
The remaining problem is therefore sharper: either enter the descent tree
with logarithmic residual width and controlled \(K\), or replace the current
\(K\)-growth mechanism.

No external literature refresh was performed in this round; the Round 276
source check remains the latest external status.
