# Round 402

Round 402 converts the persistent-prefix family from Round 401 into a
bounded-gap prefix-pair family.

During this round, the Round 401 \(P^{\rm per16}\) displayed profile was also
corrected to carry the same bridge-record marker depth as the \(P^{\rm rec16}\)
profile it replaces.

Round 401 left the persistent-prefix contribution
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
\]
with cutoff
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
using the same bridge-record marker depth as the persistent-prefix profile.
The persistent-prefix ordered-ladder reduction, followed by the
bounded-successor-gap reduction, gives
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
The bounded-gap profile uses cutoff
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and the new finite \(B_i\)-budget.

Substitution into the Round 401 finite ladder replaces only the
persistent-prefix term under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
\]
by the bounded-gap prefix-pair term.  The adjacent seventeenth return-spread
family, sixteenth bridge-return spread family, adjacent sixteenth
return-spread family, fifteenth retained spread families, older retained
spread families, exact-level return terms, enlarged spread-return profiles,
and the long-run coefficient are unchanged.

The radial-tail and subdivision criteria now use the seventeenth bounded-gap
version: the bounded-gap prefix-pair profile replaces the persistent-prefix
hypothesis while the seventeenth adjacent return-spread hypotheses are
retained.

No external literature refresh was performed in this round; the targeted
Round 399 source check remains the latest external status recorded by this
project.
