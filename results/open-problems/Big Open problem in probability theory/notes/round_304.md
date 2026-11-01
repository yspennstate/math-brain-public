# Round 304

Round 304 absorbs the chain-depth inward-free confined bridge profiles into
prefix-record outward-spread profiles and long-run profiles.

Round 303 left the inward-free bridge term
\[
  P^{\rm pre,br,free,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,2K_i^{\rm gap,ch},L_i,h},
  \qquad
  1\le h\le B_i^{\rm ch}.
\]
The existing inward-free bridge reduction gives
\[
  P^{\rm pre,br,free,ch}_{i,j,h}
  \le
  P^{\rm pre,out,per,stair,loc,chain}_{j,2K_i^{\rm gap,ch},L_i,h+1}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Since \(h+1\ge2\), the locally short chain-to-record observation gives
\[
  P^{\rm pre,out,per,stair,loc,chain}_{j,2K_i^{\rm gap,ch},L_i,h+1}
  \le
  P^{\rm pre,rec,br,ch}_{i,j},
\]
where
\[
  P^{\rm pre,rec,br,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,2K_i^{\rm gap,ch},L_i}.
\]

Substituting into the Round 303 ladder replaces
\[
  2\sum_h P^{\rm pre,br,free,ch}_{i,j,h}
\]
by
\[
  2B_i^{\rm ch}P^{\rm pre,rec,br,ch}_{i,j}
  +
  2B_i^{\rm ch}W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Thus the total long-run coefficient becomes \(2B_i^{\rm ch}+3\).

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the bridge-depth prefix-record profile
\(P^{\rm pre,rec,br,ch}_{i,j}\), together with the bridge-return spread
profiles \(R^{\rm spr,br,ch}_{i,j,h}\) from Round 303.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
