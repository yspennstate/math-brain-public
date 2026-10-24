# Round 403

Round 403 splits the bounded-gap prefix-pair family from Round 402 into a
finite family of fixed-gap profiles.

Round 402 left
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
\]
with cutoff
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and finite budget
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
Define the fixed-gap scale
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
Here the new fixed-gap scale has the same bridge-record marker depth as the
bounded-gap profile and \(B_i\)-budget, while the inherited cutoff has one
fewer marker.

Applying the bounded-gap-to-fixed-gap reduction gives
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 402 finite ladder replaces the bounded-gap
prefix-pair term under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
\]
by the finite fixed-gap sum.  The adjacent seventeenth return-spread family,
sixteenth bridge-return spread family, adjacent sixteenth return-spread
family, fifteenth retained spread families, older retained spread families,
enlarged spread-return profiles, exact-level return terms, and the long-run
coefficient are unchanged.

The radial-tail and subdivision criteria now use the seventeenth fixed-gap
profiles while retaining the seventeenth adjacent return-spread hypotheses.
The next internal move is to project these fixed-gap profiles to confined
bridge profiles.

No external literature refresh was performed in this round; the targeted
Round 399 source check remains the latest external status recorded by this
project.
