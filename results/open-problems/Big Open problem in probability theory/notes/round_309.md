# Round 309

Round 309 splits the bridge-record confined fixed-gap bridge profile into an
inward-free bridge profile and a bridge-return spread profile.

Round 308 left the confined bridge-record family
\[
  P^{\rm pre,br,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,K_i^{\rm gap,br,ch},L_i,h}.
\]
Applying the existing confined-bridge inward-free-or-returning dichotomy gives
\[
  P^{\rm pre,br,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,free,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,2K_i^{\rm gap,br,ch},L_i,h}
\]
and
\[
  R^{\rm spr,br,recbr,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,2K_i^{\rm gap,br,ch}\max\{h-1,1\}}.
\]

Substitution into the Round 308 ladder replaces
\[
  2B_i^{\rm ch}
  \sum_{h=1}^{B_i^{\rm br,ch}}
  P^{\rm pre,br,recbr,ch}_{i,j,h}
\]
by
\[
  2B_i^{\rm ch}
  \sum_{h=1}^{B_i^{\rm br,ch}}
  \Bigl(
    P^{\rm pre,br,free,recbr,ch}_{i,j,h}
    +
    R^{\rm spr,br,recbr,ch}_{i,j,h}
  \Bigr).
\]

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the bridge-record inward-free bridge family
\(P^{\rm pre,br,free,recbr,ch}_{i,j,h}\), together with the new
bridge-record bridge-return spread profiles and the earlier bridge-record
spread-return profiles.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
