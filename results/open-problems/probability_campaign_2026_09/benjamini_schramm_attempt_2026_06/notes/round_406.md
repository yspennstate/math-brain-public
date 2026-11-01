# Round 406

Round 406 absorbs the seventeenth inward-free bridge profiles from Round 405
into prefix-record profiles.

Round 405 left the finite inward-free family
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h},
  \qquad
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
The inward-free bridge reduction gives, for each finite \(i,j,h\),
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,stair,loc,chain}_{i,j,h+1}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Since \(h+1\ge2\), the locally short staircase-chain profile is absorbed by
the prefix-record profile
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}.
\]

The finite \(h\)-multiplicity is folded into a new coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
where the left-hand coefficient has one more record marker than the
right-hand one.  The same multiplicity is added to the long-run coefficient:
\[
  A_i^{\rm long,br,recbr,\ldots,recbr,ch}
  =
  A_i^{\rm long,br,recbr,\ldots,recbr,ch}
  +
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]

Substitution into the Round 405 finite ladder replaces the inward-free bridge
sum by the new prefix-record sum.  The seventeenth bridge-return spread
family, adjacent seventeenth return-spread family, sixteenth retained spread
families, fifteenth retained spread families, older retained spread families,
enlarged spread-return profiles, and exact-level return terms are unchanged.

The radial-tail and subdivision criteria now use the seventeenth prefix-record
profiles while retaining the seventeenth bridge-return and adjacent
return-spread hypotheses.  The next internal move is to split these
prefix-record profiles into persistent prefix profiles plus adjacent
return-spread profiles, starting the next persistent/bounded-gap/fixed-gap
cycle.

No external literature refresh was performed in this round; the targeted
Round 399 source check remains the latest external status recorded by this
project.
