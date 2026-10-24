# Round 325

Round 325 splits the bounded-gap bridge-record-record-record-record
prefix-pair profile from Round 324 by the actual successor gap.

Round 324 left
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,ch}} .
\]
Applying the bounded-gap-to-fixed-gap split with
\[
  K=8K_i^{\rm gap,br,recbr,recbr,ch},
  \qquad
  B=B_i^{\rm br,recbr,recbr,recbr,ch}
\]
gives
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,h},
\]
and
\[
  K_i^{\rm gap,br,recbr,recbr,recbr,ch}
  =
  8K_i^{\rm gap,br,recbr,recbr,ch}
  B_i^{\rm br,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 324 ladder replaces
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
    B_i^{\rm br,recbr,recbr,ch}
  P^{\rm pre,pair,br,recbr,recbr,recbr,ch}_{i,j}
\]
by the same coefficient times
\[
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,ch}}
  P^{\rm pre,gap,br,recbr,recbr,recbr,ch}_{i,j,h}.
\]
All return-spread and bridge-return terms from Round 324 are retained, and
the long-run coefficient remains unchanged.

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the fixed-gap bridge-record-record-record-record prefix-pair
family \(P^{\rm pre,gap,br,recbr,recbr,recbr,ch}_{i,j,h}\), which should next
be projected to confined fixed-gap bridge profiles, paralleling Round 320.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
