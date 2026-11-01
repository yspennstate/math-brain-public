# Round 031 log

## Goal

Test a richer finite-type percolation lower process for
\(T_3\square\mathbb Z\), retaining finite vertical subsets rather than only
one contiguous interval.

## Finite-subset lower process

Added `scripts/subset_branching_scan.py`.  A type is a non-empty subset of
\(\{0,\ldots,W\}\) containing \(0\), representing a reached child-fiber subset
up to vertical translation and with span at most \(W\).  Given a parent type,
horizontal seeds are sampled on the retained sites and vertical percolation
expands them inside the child line.  The lower process keeps the reached
subset of span at most \(W\) with largest cardinality, using a deterministic
tie-break.

The retained type is always a subset of the actual reached child set, so this
is a legitimate finite-type lower-process diagnostic.  It preserves separated
heights that the one-interval process discards.

Floating thresholds for the unweighted finite-subset process:

\[
\begin{array}{c|c|c}
W & \#\text{types} & p_W\\
\hline
2 & 4 & 0.316714332031\\
3 & 8 & 0.304788514903\\
4 & 16 & 0.299989501051\\
5 & 32 & 0.297859216380\\
6 & 64 & 0.296860517956\\
7 & 128 & 0.296377903218
\end{array}
\]

For \(W=8\), full bisection was too slow, but fixed-\(p\) probes give
\[
  p_8\in(0.2961,0.2962),
\]
with
\[
  \rho_{\rm lower}(0.2961)=0.999809303920,\qquad
  \rho_{\rm lower}(0.2962)=1.000276892970.
\]

This is a substantial improvement over the one-interval family, which
saturates near \(0.302827\), but it still does not beat the current
decorated-strip certificate
\[
  p_c(T_3\square\mathbb Z)<5909/20000=0.29545.
\]

## Weighted selector

Added `scripts/subset_branching_weighted_scan.py`.  For a positive test vector
\(v\), the retained child type is chosen to maximize \(v_T\) among all reached
subsets \(T\) of span at most \(W\).  If
\[
  2\,\mathbb E[\max_T v_T]>v_S
\]
for every parent type \(S\), the selector defined by \(v\) gives a concrete
finite-type lower process with spectral radius greater than one.

At \(W=7\), the weighted selector gives:

\[
\begin{array}{c|c}
p & \min_S 2\mathbb E[\max_T v_T]/v_S\\
\hline
0.29545 & 0.995691051183\\
0.2960 & 0.998245903598\\
0.2962 & 0.999175273922\\
0.2964 & 1.000104820600
\end{array}
\]

Thus the weighted selector does not materially improve the finite-subset
threshold at this size.

## Consequence

Finite-subset branching is a better non-oriented comparison than the
one-interval process, but the current implementation still stalls around
\(p\approx0.2961\), above the decorated-strip bound and far above the
\(0.274159516989\) threshold needed for the current finite-length SAW
certificate.  The remaining \(T_3\square\mathbb Z\) case still needs a new
operator-side estimate or a lower process retaining more global fiber
information.
