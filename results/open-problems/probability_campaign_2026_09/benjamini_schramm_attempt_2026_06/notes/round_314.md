# Round 314

Round 314 projects the fixed-gap bridge-record-record prefix-pair profiles
from Round 313 to confined fixed-gap bridge profiles.

Round 313 left the finite fixed-gap family
\[
  P^{\rm pre,gap,br,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,K_i^{\rm gap,br,recbr,ch},L_i,h},
  \qquad
  1\le h\le B_i^{\rm br,recbr,ch}.
\]
The generic fixed-gap-pairs-have-confined-bridges reduction gives
\[
  P^{\rm pre,gap,br,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,K_i^{\rm gap,br,recbr,ch},L_i,h}.
\]

Substitution into the Round 313 ladder replaces
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  \sum_{h=1}^{B_i^{\rm br,recbr,ch}}
  P^{\rm pre,gap,br,recbr,ch}_{i,j,h}
\]
by
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  \sum_{h=1}^{B_i^{\rm br,recbr,ch}}
  P^{\rm pre,br,recbr,recbr,ch}_{i,j,h}.
\]
All return-spread and bridge-return terms from Round 313 are retained, and
the long-run coefficient remains
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}+2B_i^{\rm ch}+3.
\]

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the bridge-record-record confined bridge family
\(P^{\rm pre,br,recbr,recbr,ch}_{i,j,h}\), together with the new and older
bridge-record return-spread families.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
