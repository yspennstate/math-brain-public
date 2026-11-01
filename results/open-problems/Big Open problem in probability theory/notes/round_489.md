# Round 489 vertical-run entropy in the stack-charge lemma

Round 489 corrects an incompleteness in the Round 488 stack-charge lemma.

The tree stack is not the only source of entropy.  The line-height trace can
also have exponentially many possibilities, because a path may change its
vertical direction after moving to a fresh tree vertex.  Such a direction
change does not by itself violate self-avoidance.

For a path with \(a\) tree-coordinate steps and \(b\) line-coordinate steps,
decompose the line moves into maximal monotone vertical runs.  Since a
vertical direction change at the same tree vertex would revisit a vertex,
each change of vertical direction must be separated by at least one tree
step.  Hence the number \(r\) of vertical runs satisfies
\[
  r\le a+1.
\]
For fixed \(r\), the number of possible run lengths and signs is at most
\[
  2^r\binom{b-1}{r-1}.
\]
Thus a crude count of line-height traces is
\[
  \sum_{r\le a+1}2^r\binom{b-1}{r-1},
\]
which is exponential for many linear regimes of \(a,b\).  It cannot simply be
buried in the \(e^{o(n)}\) term of Round 488.

Consequently, the stack-charge lemma must be strengthened.  The right target
is not:

> tree push-pop schedules are subexponentially determined by the interleaving
> and line-height trace.

The right target is a joint encoding:

> after endpoint \(L^2\) averaging, the combined choices of tree stack
> schedule, vertical run decomposition, and line-height trace for annular
> exterior SAWs with \(a\) tree steps and \(b\) line steps are bounded by
> \(e^{o(n)}\binom na q^{a/2}\).

The exterior condition and the fixed annular boundary should be used here.
They impose an excursion constraint on the excess
\[
  e=d_T(o,v)+|z|-u\ge0
\]
and force the final excess to return to \(0\).  The portal lower-bound
families are exactly examples where this excursion constraint permits
substantial, but still controlled, vertical-run entropy.

Therefore the Round 487 upper strategy remains:
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\le\sqrt q+1,
\]
but the missing lemma is now sharper: prove a joint stack/run excursion
bound, not a tree-stack bound with the line trace treated as negligible.
