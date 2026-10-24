# Round 315

Round 315 splits the bridge-record-record confined fixed-gap bridge profile
from Round 314 into an inward-free bridge profile plus a bridge-return spread
profile.

Round 314 left the confined bridge-record-record family
\[
  P^{\rm pre,br,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,K_i^{\rm gap,br,recbr,ch},L_i,h}.
\]
The confined-bridge inward-free-or-returning dichotomy gives
\[
  P^{\rm pre,br,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,free,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,2K_i^{\rm gap,br,recbr,ch},L_i,h}
\]
and
\[
  R^{\rm spr,br,recbr,recbr,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,
    2K_i^{\rm gap,br,recbr,ch}\max\{h-1,1\}}.
\]

Substitution into the Round 314 ladder replaces
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  \sum_{h=1}^{B_i^{\rm br,recbr,ch}}
  P^{\rm pre,br,recbr,recbr,ch}_{i,j,h}
\]
by
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  \sum_{h=1}^{B_i^{\rm br,recbr,ch}}
  \Bigl(
    P^{\rm pre,br,free,recbr,recbr,ch}_{i,j,h}
    +
    R^{\rm spr,br,recbr,recbr,ch}_{i,j,h}
  \Bigr).
\]
All earlier return-spread and bridge-return terms are retained, and the
long-run coefficient remains
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}+2B_i^{\rm ch}+3.
\]

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the bridge-record-record inward-free bridge family
\(P^{\rm pre,br,free,recbr,recbr,ch}_{i,j,h}\), together with the new
bridge-record-record bridge-return spread profiles and the earlier
bridge-record return-spread profiles.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
