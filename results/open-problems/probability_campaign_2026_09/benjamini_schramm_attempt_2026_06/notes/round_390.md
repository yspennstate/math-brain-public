# Round 390

Round 390 converts the fifteenth persistent-prefix family from Round 389 into
a fifteenth bounded-gap prefix-pair family.

Round 389 left
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
\]
with fourteen \({\rm recbr}\) markers and cutoff
\[
  4K_i^{\rm gap,br,recbr,\ldots,recbr,ch}.
\]
Set
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  \right\rceil+1,
\]
where the \(B_i\)-superscript has fourteen \({\rm recbr}\) markers and the
gap cutoff has thirteen.  The ordered-ladder conversion followed by the
bounded-successor reduction gives
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
The prefix-pair profile uses cutoff
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and the new \(B_i\)-budget.

Substitution into the Round 389 finite ladder replaces the persistent-prefix
term under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
\]
by the fifteenth bounded-gap prefix-pair term.  The adjacent fifteenth
return-spread family, the fourteenth bridge-return and adjacent return-spread
families, older retained spread families, and the long-run coefficient are
unchanged.

The radial-tail and subdivision criteria now use the fifteenth bounded-gap
prefix-pair family.  The next internal move is to decompose this bounded-gap
family into fixed-gap profiles, paralleling the previous fixed-gap reduction.

No external literature refresh was performed in this round; the targeted
post-Round 382 source check remains the latest external status recorded by
this project.
