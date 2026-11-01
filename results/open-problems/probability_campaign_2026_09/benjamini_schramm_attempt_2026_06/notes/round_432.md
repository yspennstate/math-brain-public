# Round 432 density loss in the chain-antichain split

Round 432 audits the quantitative strength of the Round 430 reduction.  The
chain-disjoint split is structurally useful, but by itself it does not
preserve a linear-density obstruction in either branch.

Let
\[
  N=\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H.
\]
For a parameter \(a\ge2\), the split gives either a nested chain of length
\(a\), or at least \(N/(a-1)\) pairwise disjoint exterior-return intervals.
These two lower bounds cannot both be linear in \(L_H\) by a single choice of
\(a\):

* if \(a\) is fixed, the disjoint branch has linear size, but the chain branch
  asks only for a fixed-size nested chain;
* if \(a\) is proportional to \(L_H\), the chain branch has linear size, but
  the disjoint branch may have only \(O(1)\) intervals;
* the balanced choice \(a\simeq\sqrt N\) guarantees only \(O(\sqrt{L_H})\)
  witnesses in either branch.

Thus the chain-antichain dichotomy alone cannot yield a logarithmic-exponent
saving of order \(L_H\).  Any proof must add a genuine estimate for at least
one of the branches:

1. a nested-chain estimate strong enough even when the guaranteed chain length
   is fixed or sublinear, perhaps because nesting forces large radial span or
   scarce annular geometry;
2. a disjoint-excursion estimate strong enough when the guaranteed disjoint
   family is linear, while separately controlling the fixed-chain exceptional
   branch;
3. a strengthened structural dichotomy that preserves positive density in
   one branch, for example "linear nested span" versus "linear disjoint
   returns."

The last formulation is the most promising deterministic target.  A nested
chain through return levels
\[
  u_1<\cdots<u_a
\]
has radial span \(u_a-u_1\).  A fixed-length chain with large span may still
be expensive: the outer return interval must contain an excursion reaching
far above its entry level before returning below it.  Therefore the next
target should track not just chain length, but chain span.  A useful
replacement profile would split spread returns into:

* nested chains with span at least \(\eta L_H\);
* many disjoint exterior returns;
* residual laminar forests whose chains all have small span.

The residual case is the new combinatorial obstacle: one must show it still
contains enough disjoint returns, or else identify an additional geometric
feature that was not captured by ordinary laminar height.
