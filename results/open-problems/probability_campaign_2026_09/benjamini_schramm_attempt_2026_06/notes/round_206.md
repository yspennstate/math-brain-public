# Round 206

Round 206 adds a guardrail for the long-excess tail from Round 204.

The raw bounded-degree self-avoiding path count gives, for \(n+k\ge1\),
\[
  \mathfrak N_{n,k}^{\rm saw,sph}
  \le
  \Delta(\Delta-1)^{n+k-1}.
\]
If this were inserted into the \(q\)-weighted long-excess tail, summation over
\(k\) would require
\[
  q(\Delta-1)<1.
\]
That is incompatible with the criterion, because \(q>p_c\) and the standard
tree-counting susceptibility bound gives
\[
  p_c\ge\frac1{\Delta-1}.
\]

So the remaining long-excess tail cannot be a pure maximum-degree estimate.
It has to use fixed exact spheres, endpoint constraints, averaging over
\(S_n(x)\), or additional graph geometry.
