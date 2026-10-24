# Round 407

Round 407 splits the seventeenth prefix-record profiles left by Round 406
into persistent-prefix profiles plus a new adjacent return-spread family.

The input profile is
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
Applying the short prefix-record persistent/returning split with
\[
  K=2K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j+1}.
\end{aligned}
\]
The persistent-prefix cutoff is \(4K_i^{\rm gap,br,\ldots,ch}\), and the
new adjacent return-spread cutoff is \(8K_i^{\rm gap,br,\ldots,ch}\).

Substitution into the Round 406 finite ladder replaces the seventeenth
prefix-record term by the seventeenth persistent-prefix term and the two
adjacent eighteenth return-spread terms under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}.
\]
No long-run coefficient changes in this split.  The seventeenth
bridge-return spread family, adjacent seventeenth return-spread family,
sixteenth retained spread families, fifteenth retained spread families,
older retained spread families, enlarged spread-return profiles, exact-level
return terms, and long-run profiles are retained.

The radial-tail and subdivision criteria now use the eighteenth persistent
formulation.  The next internal move is to convert this persistent-prefix
family into a bounded-gap prefix-pair family.

External status was refreshed during this round using targeted searches over
recent arXiv/primary preprint records.  I found partial-result papers for
hyperbolic, nonunimodular, and related regimes, but no primary source claiming
a proof of the general nonamenable quasi-transitive \(p_c<p_u\) problem or
the stronger \(p_c<p_{2\to2}\) target.
