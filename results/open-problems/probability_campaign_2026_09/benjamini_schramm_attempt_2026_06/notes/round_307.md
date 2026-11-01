# Round 307

Round 307 splits the bounded-gap bridge-record prefix-pair profile by the
actual gap.

The Round 306 profile is
\[
  P^{\rm pre,pair,br,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,8K_i^{\rm gap,ch},L_i,B_i^{\rm br,ch}} .
\]
Applying the existing bounded-gap-to-fixed-gap split with
\[
  K=8K_i^{\rm gap,ch},\qquad B=B_i^{\rm br,ch}
\]
gives
\[
  P^{\rm pre,pair,br,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,ch}}
  P^{\rm pre,gap,br,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,gap,br,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,K_i^{\rm gap,br,ch},L_i,h},
  \qquad
  K_i^{\rm gap,br,ch}
  =
  8K_i^{\rm gap,ch}B_i^{\rm br,ch}.
\]

Substitution into the Round 306 ladder replaces
\[
  2B_i^{\rm ch}P^{\rm pre,pair,br,ch}_{i,j}
\]
by
\[
  2B_i^{\rm ch}
  \sum_{h=1}^{B_i^{\rm br,ch}}
  P^{\rm pre,gap,br,ch}_{i,j,h}.
\]

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the fixed-gap bridge-record prefix-pair family
\(P^{\rm pre,gap,br,ch}_{i,j,h}\), together with the bridge-record
spread-return and bridge-return spread profiles.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
