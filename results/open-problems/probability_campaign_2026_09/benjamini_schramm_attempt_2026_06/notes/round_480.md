# Round 480 optimizing one-portal staircases

Round 480 optimizes the one-portal version of the construction from
Rounds 478--479.

Keep the exterior radius \(u\), but let the endpoint tree depth be
\[
  r=\lambda u,\qquad 0<\lambda\le1,
\]
so the endpoint line height is \(u-r\).  Move from a start branch to the root
at portal height
\[
  M=\mu u,\qquad \mu\ge1,
\]
and then move to a disjoint terminal branch with the same endpoint height.

The first leg uses
\[
  r\text{ inward tree steps},\qquad M-u+r\text{ upward line steps}.
\]
The exterior condition is the ballot condition that upward line steps never
lag behind inward tree steps.  Since \(M\ge u\), this condition has only a
polynomial effect on the binomial count.  The exponential count of one leg is
\[
  \binom{(M-u+2r)}{r}
  =
  \exp\{u\, n H(\lambda/n)+o(u)\},
\]
where
\[
  n=\mu-1+2\lambda
\]
and \(H\) is the binary entropy function.  The second leg has the same
exponential count by time reversal.

The endpoint sets in two disjoint tree branches have sizes \(\asymp q^r\).
After the annular cut normalization, the contribution has logarithmic
exponent
\[
  2u\,nH(\lambda/n)+\lambda u\log q+o(u),
\]
and length
\[
  2un.
\]
Thus the one-portal exponential rate is
\[
  \exp\left\{
    H(t)+\frac{t}{2}\log q
  \right\},
  \qquad
  t=\lambda/n\le\frac12.
\]
The function
\[
  H(t)+\frac{t}{2}\log q
\]
is increasing on \(0\le t\le1/2\), because its unconstrained maximizer is
\[
  t=\frac{\sqrt q}{1+\sqrt q}>\frac12.
\]
Therefore the one-portal family is maximized at \(t=1/2\), equivalently
\(\mu=1\), and its best exponent is
\[
  2q^{1/4}.
\]

Conclusion: raising the portal above height \(u\), or moving the endpoint
sets to nonzero line height, does not improve the symmetric portal lower
bound.  Any construction reaching the global product-shuffle scale
\[
  \sqrt q+1
\]
must use more than a single root portal.  It would need repeated portals,
distributed tree branching at many heights, or another mechanism that keeps
the line-motion shuffle entropy without losing the annular sphere constraint.
