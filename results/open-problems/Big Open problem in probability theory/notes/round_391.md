# Round 391

Round 391 decomposes the fifteenth bounded-gap prefix-pair family from
Round 390 into a finite sum of fixed-gap profiles.

Round 390 left
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
\]
with fourteen \({\rm recbr}\) markers, cutoff
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
where the new \(K_i\)- and \(B_i\)-superscripts have fourteen
\({\rm recbr}\) markers, while the inherited gap scale has thirteen.
The bounded-gap-to-fixed-gap reduction gives
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 390 finite ladder replaces the bounded-gap
prefix-pair term under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
\]
by the finite fixed-gap sum.  The adjacent fifteenth return-spread family,
the fourteenth bridge-return and adjacent return-spread families, older
retained spread families, and the long-run coefficient are unchanged.

The radial-tail and subdivision criteria now use the fifteenth fixed-gap
profiles.  The next internal move is to project these fixed-gap profiles to
confined fixed-gap bridge profiles, paralleling the previous confined-bridge
projection.

No external literature refresh was performed in this round; the targeted
post-Round 382 source check remains the latest external status recorded by
this project.
