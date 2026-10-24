# Round 409

Round 409 splits the eighteenth bounded-gap prefix-pair family from Round
408 into fixed-gap prefix-pair profiles.

The input profile is
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
For the bounded-gap range
\[
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
define the fixed-gap scale by
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
The bounded-gap-to-fixed-gap reduction gives
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 408 finite ladder replaces the bounded-gap term
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
  \sum_j P_{i,j}^{\rm pair18}
\]
by the finite fixed-gap sum
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
  \sum_j\sum_h P_{i,j,h}^{\rm gap18}.
\]
The added \(h\)-sum is finite and independent of \(p\).  The adjacent
eighteenth return-spread family, the seventeenth bridge-return and adjacent
return-spread families, all older retained spread families, enlarged
spread-return profiles, exact-level return terms, and long-run profiles are
retained.

The radial-tail and subdivision criteria now use the eighteenth fixed-gap
formulation.  The next internal move is to project these fixed-gap profiles
to confined bridge profiles.

External status was refreshed during this round using targeted arXiv queries.
The search again found only partial-result regimes and no primary-source
claim resolving the general nonamenable quasi-transitive \(p_c<p_u\) problem
or the stronger \(p_c<p_{2\to2}\) target.
