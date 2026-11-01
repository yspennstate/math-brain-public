# Round 042 log

## Goal

Compare the new fiber-summed tree criterion with the Hutchcroft--Pan 2024
product/lamplighter theorem, and reset the next target accordingly.

## Source audit

The extracted source of Hutchcroft--Pan, `arXiv:2412.15895`, proves a stronger
result than the line-factor proposition in this draft.  Their theorem states
that if \(T\) is a regular tree and \(G\) is either \(T\times H\), with \(H\) an
infinite amenable Cayley graph, or the lamplighter graph over \(T\), then
\[
  p_{2\to2}(G)=p_u(G).
\]
They further identify this value with the nonunimodular tilted and heaviness
thresholds \(p_t\) and \(p_h\) for the natural end-fixing automorphism group.

Thus the \(T_d\square\mathbb Z\) identity obtained in Rounds 040--041 is not a
new product theorem.  It is still useful locally because it isolates a much
smaller operator mechanism: once a fiber-summed directional mass \(I_n(p)\)
decays faster than \((d-1)^{-n/2}\), Schur's test on fibers and the tree
spherical \(L^2\) bound give \(p\le p_{2\to2}\).

## Hutchcroft--Pan mechanism

Their proof uses a broader nonunimodular framework rather than Yamamoto's
one-dimensional fixed-direction exponent.  The key ingredients are:

- A relative characterization of \(p_u\) by finite intersections with the
  amenable fiber, using subgroup relativization and relative sharpness.
- Slab quantities \(P_p(n)\) and \(E_p(n)\) for connecting from the origin to a
  fiber at tree level \(-n\), with
  \[
    E_p(n)\le C_p P_p(n)\log(e/P_p(n))
  \]
  for \(p<p_u\), so probabilities and expected fiber mass share the same
  exponential rate.
- A backscattering argument.  For \(T\times H\), amenability of \(H\) enters
  through Kesten's subexponential return estimate for a branching random walk
  in the \(H\)-coordinate.  This proves the directional exponent is at least
  \(1/2\) throughout \(p<p_u\).
- A nonunimodular Hammersley--Welsh inequality bounding the tilted
  susceptibility by
  \[
    \chi_{p,1/2}
    \le
    \bigl(\mathbb E_p |K_o\cap[o]|\bigr)^2
    \exp\!\left[
      2\sum_{n\ge0}(k-1)^{-n/2}D_p(n)
    \right].
  \]
  Combined with the exponent bound, this gives \(\chi_{p,1/2}<\infty\) for
  every \(p<p_u\), hence \(p_u\le p_t\le p_{2\to2}\le p_u\).

## Consequence for this project

The immediate next target should not be another proof of the amenable-product
case.  The useful abstraction is to identify which parts of the
Hutchcroft--Pan mechanism survive outside exact tree products and lamplighter
graphs:

1. A quotient or height structure with a meaningful modular/tilted
   susceptibility.
2. Relative sharpness for intersections with an amenable or amenable-like
   normal subgroup/fiber.
3. A replacement for the backscattering step that forces the relevant
   transverse exponent to be at least \(1/2\).
4. A Hammersley--Welsh decomposition robust enough to bound an \(L^2\) or
   tilted two-point norm.

The fiber-summed criterion from Round 041 is the elementary operator endpoint
of this program, while Hutchcroft--Pan supplies a substantially stronger
nonunimodular route for product and lamplighter examples.
