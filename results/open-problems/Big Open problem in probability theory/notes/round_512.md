# Round 512 leg collapse and record-envelope decomposition

Round 511 counts a reversal bubble as two single atoms.  This needs
justification, because a leg of a reversal may itself be a monotone trace
with many subdivisions.  The missing point is that monotone legs can be
collapsed without increasing weight in the low-branching residual regime.

At \(z=M_q^{-1}\), \(q=2,\ldots,6\), and \(C=2\), we have
\[
  Cc_q(z)=2qz^2w_*^2\le0.32<1.
\]
Consider a monotone leg of total height length \(L\).

* If the leg has no child atom, then maximal compression forces it to be one
  vertical atom, with weight \(z^L\).
* If the leg has \(m\ge1\) child atoms, its color factor is at most
  \((Cc_q(z))^m\le Cc_q(z)\).  Collapsing the whole leg to one child atom of
  height length \(L\) gives weight \(Cc_q(z)z^L\), no smaller than the
  original color-weighted length contribution.

Thus every monotone leg can be replaced by a single vertical or child atom
without decreasing the majorant weight.  If two collapsed legs form a
reversal bubble, the no-consecutive-vertical rule still guarantees that at
least one of them is a child atom: if both legs were pure vertical, the
original trace would contain two consecutive vertical runs with opposite
directions, contradicting maximal root-column compression.

This supplies the missing interpretation of the Round 511 inventory
\[
  D_q(z)=
  \left(\frac{z}{1-z}\right)^2
  \bigl((1+Cc_q(z))^2-1\bigr).
\]
It is not counting arbitrary subdivided legs directly; it counts the
collapsed image of those legs.

The remaining combinatorial map should be a record-envelope decomposition.
Assume the endpoint is to the right.  Follow the height trace and keep its
running record maximum.  The monotone skeleton is the sequence of record
increments.  Whenever the trace leaves the current record level and later
returns to or crosses that level, cut out the intervening segment as a
reversal bubble.  If the return occurs by a child jump that crosses over the
record level to a new record height, insert the record level as a virtual cut:
the original child jump of length \(a+b\) is split into a child return of
length \(a\) and a forward atom of length \(b\), preserving the \(z\)-length
factor and not increasing the child color factor.

After all such cuts, the trace is represented by:

1. a monotone record skeleton, controlled by Round 508; and
2. an ordered sequence of collapsed neutral reversal bubbles, controlled by
   the geometric factor from Round 511.

What remains to make this a proof is to formalize the record-envelope cuts
for packet families sharing one root column and to check that inserted
virtual cuts do not violate the adjacent-gap matching constraints.  Since
the construction only adds cuts to child jumps, not to vertical root-column
intervals, the hard-core vertical matching should be preserved or weakened,
not strengthened.
