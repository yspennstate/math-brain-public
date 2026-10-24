# Round 311

Round 311 pushes the bridge-record prefix-record profile from Round 310
through the persistent-or-return split.

Round 310 left the profile
\[
  P^{\rm pre,rec,br,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,2K_i^{\rm gap,br,ch},L_i}.
\]
The generic short prefix-record split gives
\[
  P^{\rm pre,out,rec}_{j,K,L}
  \le
  P^{\rm pre,out,per}_{j,2K,L}
  +
  X^{\rm rad,ret,spr}_{j,4K}
  +
  X^{\rm rad,ret,spr}_{j+1,4K}.
\]
With \(K=2K_i^{\rm gap,br,ch}\), this becomes
\[
  P^{\rm pre,rec,br,recbr,ch}_{i,j}
  \le
  P^{\rm pre,per,br,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,ch}_{i,j+1},
\]
where
\[
  P^{\rm pre,per,br,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,br,ch},L_i}
\]
and
\[
  R^{\rm spr,recbr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,8K_i^{\rm gap,br,ch}}.
\]

Substitution into the Round 310 ladder replaces
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  P^{\rm pre,rec,br,recbr,ch}_{i,j}
\]
by
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  P^{\rm pre,per,br,recbr,ch}_{i,j}
  +
  2B_i^{\rm ch}B_i^{\rm br,ch}
  \bigl(
    R^{\rm spr,recbr,recbr,ch}_{i,j}
    +
    R^{\rm spr,recbr,recbr,ch}_{i,j+1}
  \bigr).
\]
All other Round 310 terms, including the bridge-record bridge-return spread
terms and the long-run coefficient
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}+2B_i^{\rm ch}+3,
\]
are unchanged.

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the bridge-record persistent prefix profile
\(P^{\rm pre,per,br,recbr,ch}_{i,j}\), together with the new adjacent
return-spread family \(R^{\rm spr,recbr,recbr,ch}\) and the earlier
bridge-record return-spread families.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
