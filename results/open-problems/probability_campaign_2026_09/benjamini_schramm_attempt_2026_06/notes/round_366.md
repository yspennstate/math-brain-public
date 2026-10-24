# Round 366

Round 366 converts the eleventh persistent-prefix family from Round 365 into
a bounded-gap prefix-pair family.

Round 365 left
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
at persistent cutoff
\[
  4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
The ordered-ladder and bounded-successor reductions give
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
The new successor-gap cutoff is
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  \right\rceil+1,
\]
and the pair profile uses cutoff
\[
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 365 finite ladder replaces the eleventh
persistent-prefix sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the bounded-gap prefix-pair sum.  The eleventh adjacent return-spread
family, tenth bridge-return spread family, adjacent tenth return-spread
family, older return-spread and bridge-return families, and long-run terms
are retained.

The radial-tail and subdivision criteria now use the eleventh bounded-gap
prefix-pair family.  The next internal move is to split this bounded-gap
family by the actual successor gap, paralleling Round 361.

No external literature refresh was performed in this round; the Round 339
source-checked status remains the latest external status.
