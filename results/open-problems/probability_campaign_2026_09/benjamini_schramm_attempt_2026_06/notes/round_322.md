# Round 322

Round 322 absorbs the bridge-record-record-record inward-free bridge family
from Round 321 into a deeper prefix-record profile, at the cost of another
finite long-run contribution.

Round 321 left the inward-free bridge-record-record-record family
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,
    2K_i^{\rm gap,br,recbr,recbr,ch},L_i,h}.
\]
Applying the inward-free-bridge chain-or-long-run reduction with
\[
  K=2K_i^{\rm gap,br,recbr,recbr,ch}
\]
gives
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,out,per,stair,loc,chain}_{j,
    2K_i^{\rm gap,br,recbr,recbr,ch},L_i,h+1}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Since \(h+1\ge2\), the locally short staircase-chain-to-prefix-record
reduction bounds the chain term by
\[
  P^{\rm pre,rec,br,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,2K_i^{\rm gap,br,recbr,recbr,ch},L_i}.
\]
Thus
\[
  P^{\rm pre,br,free,recbr,recbr,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,rec,br,recbr,recbr,recbr,ch}_{i,j}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]

Substitution into the Round 321 ladder replaces
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  \sum_{h=1}^{B_i^{\rm br,recbr,recbr,ch}}
  P^{\rm pre,br,free,recbr,recbr,recbr,ch}_{i,j,h}
\]
by
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
    B_i^{\rm br,recbr,recbr,ch}
  P^{\rm pre,rec,br,recbr,recbr,recbr,ch}_{i,j}
\]
and adds the same coefficient to the long-run term.  The new long-run
coefficient is
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
    B_i^{\rm br,recbr,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}
  +2B_i^{\rm ch}
  +3.
\]
All bridge-record-record-record bridge-return, adjacent return-spread,
bridge-record-record bridge-return, bridge-record bridge-return,
chain-depth bridge-return, staircase/local bridge, enlarged spread-return,
and exact-level return terms are retained.

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the deeper bridge-record-record-record prefix-record profile
\(P^{\rm pre,rec,br,recbr,recbr,recbr,ch}_{i,j}\), likely to be split into a
persistent prefix profile plus adjacent return-spread terms, paralleling the
Round 317 record split.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
