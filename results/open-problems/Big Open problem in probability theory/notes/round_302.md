# Round 302

Round 302 projects the fixed-gap chain-depth prefix-pair obstruction into a
confined-bridge profile.

Round 301 left the chain-depth term as
\[
  P^{\rm pre,gap,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,gap}_{j,K_i^{\rm gap,ch},L_i,h},
  \qquad
  1\le h\le B_i^{\rm ch}.
\]
Applying the existing fixed-gap-pair-to-confined-bridge reduction with the
same parameters \((\lambda_i,\sigma_i,\beta_i,K_i^{\rm gap,ch},L_i)\) gives
\[
  P^{\rm pre,gap,ch}_{i,j,h}
  \le
  P^{\rm pre,br,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,K_i^{\rm gap,ch},L_i,h}.
\]

Substitution into the fixed-gap persistent chain-absorbed ladder gives
\[
\begin{aligned}
  Y_{\lambda_0}^{\rm rad}
  \le&
  Y_{\lambda_N}^{\rm rad}
  +2\sum_{i,j}\sum_{h=1}^{B_i^{\rm ch}}
    P^{\rm pre,br,ch}_{i,j,h}
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

The matching radial-tail and subdivision criteria have been added.  The next
local obstruction is to split these chain-depth confined bridges into
inward-free and returning alternatives.
