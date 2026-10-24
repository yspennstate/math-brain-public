# Round 327

Round 327 splits the bridge-record-record-record-record confined fixed-gap
bridge profile from Round 326 into an inward-free bridge profile plus a
bridge-return spread profile.

Round 326 left the confined bridge-record-record-record-record family
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,
    K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,h}.
\]
The confined-bridge inward-free-or-returning dichotomy gives
\[
  P^{\rm pre,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,recbr,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,h}
\]
and
\[
  R^{\rm spr,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,
    2K_i^{\rm gap,br,recbr,recbr,recbr,ch}\max\{h-1,1\}}.
\]

Substitution into the Round 326 ladder replaces
\[
  D_i^{\rm rec,br,recbr,recbr,ch}
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,ch}}
  P^{\rm pre,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
\]
by the same coefficient times
\[
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,recbr,ch}}
  \Bigl(
    P^{\rm pre,br,free,recbr,recbr,recbr,recbr,ch}_{i,j,h}
    +
    R^{\rm spr,br,recbr,recbr,recbr,recbr,ch}_{i,j,h}
  \Bigr).
\]
All earlier adjacent return-spread and bridge-return terms are retained, and
the long-run coefficient remains \(A_i^{\rm long,br,recbr,recbr,ch}\).

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the bridge-record-record-record-record inward-free bridge family
\(P^{\rm pre,br,free,recbr,recbr,recbr,recbr,ch}_{i,j,h}\), together with the
new bridge-record-record-record-record bridge-return spread profiles and the
earlier return-spread profiles.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
