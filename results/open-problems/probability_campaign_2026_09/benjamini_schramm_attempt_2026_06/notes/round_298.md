# Round 298

Round 298 pushes the Round 297 chain-to-record observation into the older
finite far-tail and radial criteria.

The old staircase-chain/bridge finite ladder contains the two raw locally
short chain terms
\[
  P^{\rm pre,stair,loc,chain,sh}_{i,j,3}
  +
  P^{\rm pre,stair,loc,chain,sh}_{i,j,4}
\]
at depth \(512M_iB_iC_i\).  By
Corollary~\ref{cor:locally-short-staircase-chains-are-prefix-record-spread},
each is bounded by the prefix-record outward-spread profile at that same
depth:
\[
  P^{\rm pre,stair,loc,chain,sh}_{i,j,q}
  \le
  P^{\rm pre,rec,ch}_{i,j},
  \qquad q=3,4.
\]

The new finite-ladder statement is
\[
\begin{aligned}
  Y_{\lambda_0}^{\rm rad}
  \le&
  Y_{\lambda_N}^{\rm rad}
  +2\sum_{i,j}P^{\rm pre,rec,ch}_{i,j}
  +\sum_{i,j}\sum_{h=3}^{C_i}
    P^{\rm pre,stair,loc,brdg,sh}_{i,j,h}
\\
  &+
  \sum_{i,j}\sum_{h=2}^{B_i}P^{\rm pre,br,sh}_{i,j,h}
  +\text{long-run, spread-return, and exact-return terms}.
\end{aligned}
\]

The matching radial-tail and subdivision criteria have also been added.
This removes the raw \(q=3,4\) locally short staircase-chain profiles from
the downstream hypotheses and replaces them by a prefix-record profile at a
larger fixed depth parameter.  That is an older profile type, so the next
natural move is to run the existing prefix-record splitting tree at this
larger depth, or prove the needed exponent bound directly for that family.
