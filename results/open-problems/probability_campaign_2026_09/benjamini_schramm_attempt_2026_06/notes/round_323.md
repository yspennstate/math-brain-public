# Round 323

Round 323 splits the bridge-record-record-record prefix-record profile from
Round 322 into a persistent prefix profile plus adjacent return-spread terms.

Round 322 left the prefix-record family
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,2K_i^{\rm gap,br,recbr,recbr,ch},L_i}.
\]
Applying the short prefix-record persistent-or-returning split with
\[
  K=2K_i^{\rm gap,br,recbr,recbr,ch}
\]
gives
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,per,br,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\]
Here
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,br,recbr,recbr,ch},L_i}
\]
and
\[
  R^{\rm spr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,8K_i^{\rm gap,br,recbr,recbr,ch}}.
\]

Substitution into the Round 322 ladder replaces
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
    B_i^{\rm br,recbr,recbr,ch}
  P^{\rm pre,rec,br,recbr,recbr,recbr,ch}_{i,j}
\]
by the same coefficient times
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,recbr,recbr,recbr,ch}_{i,j+1}.
\]
The long-run coefficient is unchanged:
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
    B_i^{\rm br,recbr,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}
  +2B_i^{\rm ch}
  +3.
\]
All bridge-record-record-record bridge-return, older adjacent return-spread,
bridge-record-record bridge-return, bridge-record bridge-return, chain-depth
bridge-return, staircase/local bridge, enlarged spread-return, and exact-level
return terms are retained.

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the persistent bridge-record-record-record prefix profile
\(P^{\rm pre,per,br,recbr,recbr,recbr,ch}_{i,j}\), likely to be converted to
a bounded-gap prefix-pair profile, paralleling the Round 318 step.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
