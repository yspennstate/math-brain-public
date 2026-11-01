# Round 308

Round 308 projects the fixed-gap bridge-record prefix-pair profile to a
confined bridge profile.

Round 307 left the finite fixed-gap family
\[
  P^{\rm pre,gap,br,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,K_i^{\rm gap,br,ch},L_i,h},
  \qquad
  K_i^{\rm gap,br,ch}
  =
  8K_i^{\rm gap,ch}B_i^{\rm br,ch}.
\]
Applying the existing fixed-gap-pairs-have-confined-bridges reduction gives
\[
  P^{\rm pre,gap,br,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,K_i^{\rm gap,br,ch},L_i,h}.
\]

Substitution into the Round 307 ladder replaces
\[
  2B_i^{\rm ch}
  \sum_{h=1}^{B_i^{\rm br,ch}}
  P^{\rm pre,gap,br,ch}_{i,j,h}
\]
by
\[
  2B_i^{\rm ch}
  \sum_{h=1}^{B_i^{\rm br,ch}}
  P^{\rm pre,br,recbr,ch}_{i,j,h}.
\]

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the bridge-record confined bridge family
\(P^{\rm pre,br,recbr,ch}_{i,j,h}\), together with the bridge-record
spread-return and bridge-return spread profiles.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
