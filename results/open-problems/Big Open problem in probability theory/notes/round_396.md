# Round 396

Round 396 converts the sixteenth persistent-prefix family from Round 395 into
a sixteenth bounded-gap prefix-pair family.

Round 395 left
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
\]
with fifteen \({\rm recbr}\) markers and cutoff
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
where the \(B_i\)-superscript has fifteen \({\rm recbr}\) markers and the
gap cutoff has fourteen.  The ordered-ladder conversion followed by the
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

Substitution into the Round 395 finite ladder replaces the persistent-prefix
term under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
\]
by the sixteenth bounded-gap prefix-pair term.  The adjacent sixteenth
return-spread family, fifteenth bridge-return spread family, adjacent
fifteenth return-spread family, older retained spread families, and the
long-run coefficient are unchanged.

The radial-tail and subdivision criteria now use the sixteenth bounded-gap
prefix-pair family while retaining the sixteenth adjacent return-spread
hypotheses.  The next internal move is to decompose this bounded-gap family
into fixed-gap profiles, paralleling the previous fixed-gap reduction.

No external literature refresh was performed in this round; the targeted
post-Round 382 source check remains the latest external status recorded by
this project.
