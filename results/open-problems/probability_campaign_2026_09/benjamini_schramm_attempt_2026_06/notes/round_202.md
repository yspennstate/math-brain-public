# Round 202

Round 202 bounds the geodesic-normalized spherical profile by a
self-avoiding-walk envelope.

For \(0<p\le1\), define
\[
  \mathfrak S_p^{\rm saw,sph}(n)
  =
  \sup_x
  \frac1{|S_n(x)|}
  \sum_{a\in S_n(x)}
  \sum_{\gamma:x\to a\ {\rm SAW}}p^{|\gamma|-n},
\]
with the trivial path included when \(n=0\).  Since every open connection
contains an open self-avoiding path, the union bound gives
\[
  \frac{\bar\tau_p^{\rm sph}(n)}{p^n}
  \le
  \mathfrak S_p^{\rm saw,sph}(n).
\]
Thus the Round 201 normalized excess criterion follows from the same exponent
bound on the half-to-full-window supremum of
\(\mathfrak S_p^{\rm saw,sph}(n)\).  This moves the residual target one step
toward deterministic path-count control on exact spheres.
