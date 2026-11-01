# Round 513 single-trace record-envelope lemma

Round 512 reduces the low-branching residual to a combinatorial encoding.
Here is the single-trace scalar version.

Fix \(q=2,\ldots,6\), \(z=M_q^{-1}\), \(C=2\), and
\[
  a=Cc_q(z)=2qz^2w_*^2<1.
\]
For the scalar model, an atom is a nonzero height increment \(\delta\) with
weight
\[
  z^{|\delta|}
\]
if it is vertical and
\[
  a z^{|\delta|}
\]
if it is a child atom.  The only local rule kept is that two vertical atoms
are not consecutive.

**Lemma target.**  Every scalar trace from \(0\) to \(S>0\) can be encoded by

1. a monotone increasing scalar trace from \(0\) to \(S\); and
2. an ordered list of neutral primitive bubbles,

with total encoding weight at least the original trace weight.  A primitive
bubble is a pair of opposite monotone legs with at least one child leg, and
has inventory
\[
  D_q(z)=\left(\frac{z}{1-z}\right)^2\bigl((1+a)^2-1\bigr).
\]

The encoding is allowed to use virtual cuts and need not itself be a valid
root trace word.  It is only a counting majorant.

The proposed proof is the standard record-envelope algorithm.

1. Read the height sequence from left to right and maintain the running
   maximum \(R\).
2. Whenever the next atom goes from \(R\) to a new height \(R'>R\), record a
   monotone skeleton increment.
3. Whenever the trace leaves \(R\) to a lower height, follow it until the
   first later atom whose endpoint is at least \(R\).  The intervening piece
   is an excursion below the record level.
4. If the last atom lands at \(R\), cut the excursion as a neutral bubble.
   If it lands at \(R'>R\), split that last atom at the virtual level \(R\):
   the part up to \(R\) closes a neutral bubble and the remaining part
   \(R\to R'\) is a monotone skeleton increment.

The split in step 4 does not increase weight.  A vertical atom cannot cross a
previously visited record level in a valid compressed trace, so a crossing
atom is necessarily a child atom.  Splitting a child atom of length \(u+v\)
into a child return of length \(u\) and a forward vertical or child atom of
length \(v\) preserves the \(z\)-length factor and does not increase the
color factor because \(a<1\).

Excursions below a record level may have internal reversals.  Apply the same
record-envelope algorithm recursively after reflecting that excursion.  The
depth-first list of all primitive bubbles gives an ordered bubble sequence.
Since each monotone leg of a primitive bubble can be collapsed by Round 512,
the total bubble contribution is bounded by the geometric factor
\[
  1+\frac{D_q(z)}{1-D_q(z)}=\frac{1}{1-D_q(z)}.
\]

This lemma would turn the numeric Round 511 check into a scalar proof for
one trace.  The remaining extension is to packets: apply the encoding to each
trace word in global order and check that shared root-column self-avoidance
and adjacent-gap vertical matching are not used in a way that increases the
majorant.  Since the encoding is already an overcount and virtual cuts are
inserted only into child atoms, the packet extension should preserve the
upper bound.
