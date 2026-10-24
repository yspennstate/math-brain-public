# Round 441 endpoint weights reduce to annular cut norms

Round 441 sharpens the endpoint-weight obstruction from Round 439.

Let \(A=A_{Q,u,\le L}^x\) be the truncated annular SAW transfer matrix on
\(S_{u-1}(x)\).  For nonnegative endpoint weights \(f,g\),
\[
  \langle f,Ag\rangle
  =
  \sum_{a,b} f(a)A(a,b)g(b).
\]
The right inverse object is not just the full average
\(\sum_{a,b}A(a,b)\), but the cut profile
\[
  A(U,V)=\sum_{a\in U}\sum_{b\in V}A(a,b),
  \qquad U,V\subseteq S_{u-1}(x).
\]

Indeed, decompose \(f\) and \(g\) into dyadic level sets
\[
  U_i=\{a:2^i\le f(a)<2^{i+1}\},
  \qquad
  V_j=\{b:2^j\le g(b)<2^{j+1}\}.
\]
Then
\[
  \langle f,Ag\rangle
  \le
  4\sum_{i,j}2^{i+j}A(U_i,V_j).
\]
Consequently, a large weighted annular transfer has an inverse explanation:
after discarding logarithmic bookkeeping, there are endpoint level sets
\(U,V\) for which the unweighted annular cut mass \(A(U,V)\) is large
relative to the level sizes and weights.

This suggests the correct endpoint-spread split.

1. If the dyadic endpoint weights have no large atoms and all annular cuts
   \(A(U,V)\) obey a useful estimate, then the marked-return contribution is
   controlled.
2. If some endpoint level is too large, then the skeleton has endpoint
   congestion at \(S_{u-1}(x)\).  This should become a separate exact-level
   endpoint-congestion profile.
3. If endpoint levels are acceptable but \(A(U,V)\) is large for some
   moderate-size \(U,V\), then the obstruction is no longer a path-counting
   issue.  It is a ball-annulus cut-energy obstruction between two boundary
   subsets.

Thus the annular target can be stated as a restricted cut-norm estimate:
for all relevant roots, levels, truncations, and boundary subsets,
\[
  A_{Q,u,\le L}^x(U,V)
\]
must be small enough, as a function of \(|U|\), \(|V|\), and \(L\), to beat
the endpoint-level entropy.  A full \(L^2\) bound implies such a cut estimate
by
\[
  A(U,V)\le \|A\|_{2\to2}\sqrt{|U||V|},
\]
but the cut formulation is weaker and better aligned with the actual
obstruction.

The next object is the boundary-energy form of this cut profile.
