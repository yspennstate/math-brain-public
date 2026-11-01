# Round 310

Round 310 absorbs the bridge-record inward-free bridge profiles into
prefix-record outward-spread profiles and long-run profiles.

Round 309 left the inward-free bridge term
\[
  P^{\rm pre,br,free,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,2K_i^{\rm gap,br,ch},L_i,h},
  \qquad
  1\le h\le B_i^{\rm br,ch}.
\]
The existing inward-free bridge reduction gives
\[
  P^{\rm pre,br,free,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,out,per,stair,loc,chain}_{j,2K_i^{\rm gap,br,ch},L_i,h+1}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Since \(h+1\ge2\), the locally short chain-to-record observation gives
\[
  P^{\rm pre,out,per,stair,loc,chain}_{j,2K_i^{\rm gap,br,ch},L_i,h+1}
  \le
  P^{\rm pre,rec,br,recbr,ch}_{i,j},
\]
where
\[
  P^{\rm pre,rec,br,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,2K_i^{\rm gap,br,ch},L_i}.
\]

Substituting into the Round 309 ladder replaces
\[
  2B_i^{\rm ch}
  \sum_{h=1}^{B_i^{\rm br,ch}}
  P^{\rm pre,br,free,recbr,ch}_{i,j,h}
\]
by
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  P^{\rm pre,rec,br,recbr,ch}_{i,j}
  +
  2B_i^{\rm ch}B_i^{\rm br,ch}
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Thus the total long-run coefficient becomes
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}+2B_i^{\rm ch}+3.
\]

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the bridge-record prefix-record profile
\(P^{\rm pre,rec,br,recbr,ch}_{i,j}\), together with the bridge-record
bridge-return and spread-return profiles.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
