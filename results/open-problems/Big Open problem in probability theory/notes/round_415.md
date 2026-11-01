# Round 415

Round 415 splits the nineteenth bounded-gap prefix-pair profiles from Round
414 into a finite family of fixed-gap prefix-pair profiles.

Round 414 left the bounded-gap prefix-pair family
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
\]
at scale
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
with cutoff \(B_i^{\rm br,recbr,\ldots,recbr,ch}\).  Define the fixed
successor-gap scale by
\[
  K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
Applying the bounded-gap pair fixed-gap reduction gives, for every finite
\(i,j\),
\[
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,\ldots,recbr,ch}}
  P^{\rm pre,gap,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 414 finite ladder replaces only the nineteenth
bounded-gap prefix-pair contribution by this finite fixed-gap sum.  The
coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
\]
and the long-run coefficient are unchanged.  The adjacent nineteenth
return-spread family, eighteenth bridge-return and adjacent return-spread
families, seventeenth retained spread families, older retained families,
enlarged spread-return profiles, exact-level return terms, and all finite
cutoffs are retained.

The radial-tail and subdivision criteria now use the nineteenth fixed-gap
prefix-pair formulation.  The next internal move is to project these
fixed-gap prefix-pair profiles to confined bridge profiles.

External status was refreshed during this round using targeted arXiv queries.
The search again found partial-result regimes and no primary-source claim
resolving the general nonamenable quasi-transitive \(p_c<p_u\) problem or the
stronger \(p_c<p_{2\to2}\) target.
