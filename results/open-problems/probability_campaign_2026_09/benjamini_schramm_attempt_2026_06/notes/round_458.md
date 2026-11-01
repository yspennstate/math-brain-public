# Round 458 the annular gap threshold is \(1/p_c\)

Round 458 calibrates the \(Q\)-parameter in the annular boundary exponent
target.

In the subdivision route, \(H=\operatorname{Sub}(G)\) and
\[
  Q=q^2,
  \qquad q>\pc(H).
\]
Since
\[
  \pc(H)^2=\pc(G),
\]
the parameter \(Q\) can be chosen arbitrarily close to \(\pc(G)\) from above.
Therefore the useful form of the annular boundary exponent condition is not
for one arbitrary \(Q\), but the strict gap
\[
  \Gamma_{\rm ann}(G)<\frac1{\pc(G)}.
\]
If this holds, choose \(Q\in(\pc(G),1)\) with
\[
  Q\Gamma_{\rm ann}(G)<1.
\]
Then Round 452 gives the uniform annular cut estimate.

This is the exact annular analogue of the global SAW operator-gap route
\[
  \gamma_{\rm SAW,2}(G)<\frac1{\pc(G)}.
\]
The annular version is weaker because it only tests killed exterior
boundary-to-boundary returns.  It is also better matched to the spread-return
profile: the obstruction is not arbitrary SAW propagation, but repeated
return from a ball boundary to the same ball boundary through the exterior.

The raw degree bound gives only
\[
  \Gamma_{\rm ann}(G)\le \Delta-1
\]
up to harmless constants, while the universal lower bound
\[
  \pc(G)\ge \frac1{\Delta-1}
\]
does not imply a strict annular gap.  Any proof of
\(\Gamma_{\rm ann}<1/\pc\) must therefore use more than bounded degree, just
as in the global SAW route.
