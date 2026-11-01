# Round 397

Round 397 decomposes the sixteenth bounded-gap prefix-pair family from
Round 396 into a finite sum of fixed-gap profiles.

Round 396 left
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
\]
with fifteen \({\rm recbr}\) markers, cutoff
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
and height budget
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
Define the fixed-gap scale
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
where the new \(K_i\)- and \(B_i\)-superscripts have fifteen
\({\rm recbr}\) markers, while the inherited gap scale has fourteen.  The
bounded-gap-to-fixed-gap reduction gives
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 396 finite ladder replaces the bounded-gap
prefix-pair term under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
\]
by the finite fixed-gap sum.  The adjacent sixteenth return-spread family,
fifteenth bridge-return spread family, adjacent fifteenth return-spread
family, older retained spread families, and the long-run coefficient are
unchanged.

The radial-tail and subdivision criteria now use the sixteenth fixed-gap
profiles while retaining the sixteenth adjacent return-spread hypotheses.
The next internal move is to project these fixed-gap profiles to confined
fixed-gap bridge profiles, paralleling the previous confined-bridge
projection.

No external literature refresh was performed in this round; the targeted
post-Round 382 source check remains the latest external status recorded by
this project.
