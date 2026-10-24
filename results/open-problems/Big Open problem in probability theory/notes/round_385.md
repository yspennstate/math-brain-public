# Round 385

Round 385 decomposes the fourteenth bounded-gap prefix-pair family from
Round 384 into a finite sum of fixed-gap profiles.

Round 384 left
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
with cutoff
\[
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
and height budget
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
Define the fixed-gap scale
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The bounded-gap-to-fixed-gap reduction gives
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 384 finite ladder replaces the bounded-gap
prefix-pair term under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the finite fixed-gap sum.  The adjacent fourteenth return-spread family,
thirteenth bridge-return spread family, adjacent thirteenth return-spread
family, twelfth bridge-return spread family, adjacent twelfth return-spread
family, all older return-spread and bridge-return families, and long-run
terms are retained.  No coefficient changes in this round.

The radial-tail and subdivision criteria now use the fourteenth fixed-gap
profiles.  The next internal move is to project these fixed-gap profiles to
confined fixed-gap bridge profiles, paralleling the previous confined-bridge
projection.

No external literature refresh was performed in this round; the targeted
post-Round 382 source check remains the latest external status recorded by
this project.
