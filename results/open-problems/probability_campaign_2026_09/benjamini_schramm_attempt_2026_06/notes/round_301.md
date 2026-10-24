# Round 301

Round 301 splits the bounded-gap chain-depth prefix-pair profile by the
actual gap.

The Round 300 profile is
\[
  P^{\rm pre,pair,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,2048M_iB_iC_i,L_i,B_i^{\rm ch}} .
\]
Applying the existing bounded-gap-to-fixed-gap split with
\[
  K=2048M_iB_iC_i,\qquad B=B_i^{\rm ch}
\]
gives
\[
  P^{\rm pre,pair,ch}_{i,j}
  \le
  \sum_{h=1}^{B_i^{\rm ch}}
  P^{\rm pre,gap,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,gap,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,K_i^{\rm gap,ch},L_i,h},
  \qquad
  K_i^{\rm gap,ch}=2048M_iB_iC_iB_i^{\rm ch}.
\]

Substitution into the bounded-gap persistent chain-absorbed ladder gives
\[
\begin{aligned}
  Y_{\lambda_0}^{\rm rad}
  \le&
  Y_{\lambda_N}^{\rm rad}
  +2\sum_{i,j}\sum_{h=1}^{B_i^{\rm ch}}
    P^{\rm pre,gap,ch}_{i,j,h}
  +2\sum_{i,j}
    \bigl(R^{\rm spr,ch}_{i,j}+R^{\rm spr,ch}_{i,j+1}\bigr)
\\
  &+
  \sum_{i,j}\sum_{h=3}^{C_i}
    P^{\rm pre,stair,loc,brdg,sh}_{i,j,h}
  +
  \sum_{i,j}\sum_{h=2}^{B_i}
    P^{\rm pre,br,sh}_{i,j,h}
\\
  &+
  \text{long-run, existing spread-return, and exact-return terms}.
\end{aligned}
\]

The matching radial-tail and subdivision criteria have been added.  The
remaining chain-depth prefix obstruction is now a finite fixed-gap family
instead of a bounded-gap family.
