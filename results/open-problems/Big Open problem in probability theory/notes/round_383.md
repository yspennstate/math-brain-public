# Round 383

Round 383 splits the thirteenth prefix-record family from Round 382 into a
persistent-prefix family and a new adjacent return-spread family.

Round 382 left
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
with cutoff
\[
  2K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]
Applying the short-prefix-record persistent/return split gives
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\end{aligned}
\]
The persistent-prefix cutoff is
\[
  4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
and the adjacent return-spread cutoff is
\[
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 382 finite ladder replaces the thirteenth
prefix-record contribution under the fixed coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
by the persistent-prefix term and the two adjacent fourteenth return-spread
terms.  The long-run coefficient is unchanged.  The thirteenth bridge-return
spread family, adjacent thirteenth return-spread family, twelfth bridge-return
spread family, adjacent twelfth return-spread family, all older return-spread
and bridge-return families, and exact-level terms are retained.

The radial-tail and subdivision criteria now use the persistent-prefix family
and the fourteenth adjacent return-spread family.  The next internal move is to
replace the persistent-prefix family by a bounded-gap prefix-pair family,
paralleling the previous bounded-gap reduction.

No external literature refresh was performed in this round; the targeted
post-Round 382 source check remains the latest external status recorded by
this project.
