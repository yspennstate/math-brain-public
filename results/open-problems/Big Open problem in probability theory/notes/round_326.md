# Round 326

Round 326 projects the fixed-gap bridge-record-record-record-record
prefix-pair profile from Round 325 to a confined fixed-gap bridge profile.

Round 325 left
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,h}.
\]
Applying the fixed-gap pair-to-confined-bridge reduction with
\[
  (\lambda,\sigma,\beta,K,L)
  =
  (\lambda_i,\sigma_i,\beta_i,
    K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i)
\]
gives
\[
  P^{\rm pre,gap,br,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,recbr,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,h}.
\]

Substitution into the Round 325 ladder replaces the fixed-gap prefix-pair
family by the confined bridge family under the same inherited coefficient
\[
  D_i^{\rm rec,br,recbr,recbr,ch}
  =
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
    B_i^{\rm br,recbr,recbr,ch}.
\]
All return-spread and bridge-return terms from Round 325 are retained, and no
new variable multiplicative loss is introduced.

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the confined fixed-gap bridge family
\(P^{\rm pre,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}\), which should next be
split into an inward-free bridge profile plus a bridge-return spread profile,
paralleling the Round 321 inward-free bridge split.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
