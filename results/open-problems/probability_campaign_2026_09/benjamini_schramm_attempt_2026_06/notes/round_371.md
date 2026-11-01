# Round 371

Round 371 splits the eleventh prefix-record family from Round 370 into a
persistent-prefix family plus adjacent return-spread profiles.

Round 370 left
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
Applying the short prefix-record spread/persistent-return split with
\[
  (\lambda,\sigma,\beta,K,L)
  =
  (\lambda_i,\sigma_i,\beta_i,
    2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i)
\]
gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\end{aligned}
\]
The persistent cutoff is
\[
  4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
and the adjacent return-spread cutoff is
\[
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 370 finite ladder replaces the eleventh
prefix-record sum under coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the twelfth persistent-prefix sum plus two adjacent twelfth return-spread
sums.  The eleventh bridge-return spread family, adjacent eleventh
return-spread family, tenth bridge-return spread family, adjacent tenth
return-spread family, older return-spread and bridge-return families, and
long-run terms are retained.

The radial-tail and subdivision criteria now use the twelfth persistent
prefix family and the new twelfth return-spread family.  The next internal
move is to convert the twelfth persistent-prefix family into a bounded-gap
prefix-pair family, paralleling Round 366.

No external literature refresh was performed in this round; the Round 339
source-checked status remains the latest external status.
