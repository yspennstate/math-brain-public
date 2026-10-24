# Round 305

Round 305 pushes the bridge-depth prefix-record profile through the standard
persistent-or-return split.

Round 304 left
\[
  P^{\rm pre,rec,br,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,2K_i^{\rm gap,ch},L_i}.
\]
Applying the short prefix-record split with \(K=2K_i^{\rm gap,ch}\) gives
\[
  P^{\rm pre,rec,br,ch}_{i,j}
  \le
  P^{\rm pre,per,br,ch}_{i,j}
  +
  R^{\rm spr,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,ch}_{i,j+1},
\]
where
\[
  P^{\rm pre,per,br,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,ch},L_i}
\]
and
\[
  R^{\rm spr,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,8K_i^{\rm gap,ch}}.
\]

Substitution into the Round 304 ladder replaces
\[
  2B_i^{\rm ch}P^{\rm pre,rec,br,ch}_{i,j}
\]
by
\[
  2B_i^{\rm ch}P^{\rm pre,per,br,ch}_{i,j}
  +
  2B_i^{\rm ch}
  \bigl(
    R^{\rm spr,recbr,ch}_{i,j}
    +R^{\rm spr,recbr,ch}_{i,j+1}
  \bigr).
\]

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the persistent bridge-record profile
\(P^{\rm pre,per,br,ch}_{i,j}\), plus the bridge-record spread-return terms
and the Round 303 bridge-return spread terms.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
