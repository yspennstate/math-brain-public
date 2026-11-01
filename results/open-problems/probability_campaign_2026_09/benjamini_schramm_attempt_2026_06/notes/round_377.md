# Round 377

Round 377 splits the twelfth prefix-record family from Round 376 into a
persistent-prefix family plus adjacent return-spread profiles.

Round 376 left
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
Applying the short prefix-record spread/persistent-return split with
\[
  (\lambda,\sigma,\beta,K,L)
  =
  (\lambda_i,\sigma_i,\beta_i,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i)
\]
gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\end{aligned}
\]
The persistent cutoff is
\[
  4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
and the adjacent return-spread cutoff is
\[
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 376 finite ladder replaces the twelfth
prefix-record sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the thirteenth persistent-prefix sum plus two adjacent thirteenth
return-spread sums.  The twelfth bridge-return spread family, adjacent
twelfth return-spread family, eleventh bridge-return spread family, adjacent
eleventh return-spread family, older return-spread and bridge-return
families, and long-run terms are retained.

The radial-tail and subdivision criteria now use the thirteenth persistent
prefix family and the new thirteenth return-spread family.  The next
internal move is to convert the thirteenth persistent-prefix family into a
bounded-gap prefix-pair family, paralleling Round 372.

No external literature refresh was performed in this round; the Round 339
source-checked status remains the latest external status.
