# Round 367

Round 367 splits the eleventh bounded-gap prefix-pair profile from Round 366
by the actual successor gap.

Round 366 left
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}.
\]
Applying the bounded-gap-to-fixed-gap split with
\[
  K=8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
  \qquad
  B=B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
gives
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
Here
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
\]
and
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},
    L_i,h}.
\]

Substitution into the Round 366 ladder replaces
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
by the same coefficient times
\[
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j,h}.
\]
The eleventh adjacent return-spread family, tenth bridge-return spread
family, adjacent tenth return-spread family, all older return-spread and
bridge-return families, and the long-run coefficient remain unchanged.

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the eleventh fixed-gap prefix-pair family, which should next be
projected to confined fixed-gap bridge profiles, paralleling Round 362.

No external literature refresh was performed in this round; the Round 339
source-checked status remains the latest external status.
