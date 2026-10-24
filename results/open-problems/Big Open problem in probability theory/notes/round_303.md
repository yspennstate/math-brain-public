# Round 303

Round 303 splits the chain-depth confined fixed-gap bridge obstruction into
inward-free bridges and spread-return profiles.

Round 302 left the chain-depth bridge term
\[
  P^{\rm pre,br,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge}_{j,K_i^{\rm gap,ch},L_i,h},
  \qquad
  1\le h\le B_i^{\rm ch}.
\]
Applying the existing confined-bridge inward-free-or-return split with
\((\lambda_i,\sigma_i,\beta_i,K_i^{\rm gap,ch},L_i)\) gives
\[
  P^{\rm pre,br,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,ch}_{i,j,h}
  +
  R^{\rm spr,br,ch}_{i,j,h},
\]
where
\[
  P^{\rm pre,br,free,ch}_{i,j,h}
  =
  P^{\rm pre,out,per,bridge,free}_{j,2K_i^{\rm gap,ch},L_i,h}
\]
and
\[
  R^{\rm spr,br,ch}_{i,j,h}
  =
  X^{\rm rad,ret,spr}_{j,2K_i^{\rm gap,ch}\max\{h-1,1\}}.
\]

Substitution into the confined-bridge persistent chain-absorbed ladder gives
\[
\begin{aligned}
  Y_{\lambda_0}^{\rm rad}
  \le&
  Y_{\lambda_N}^{\rm rad}
  +2\sum_{i,j}\sum_{h=1}^{B_i^{\rm ch}}
    P^{\rm pre,br,free,ch}_{i,j,h}
  +2\sum_{i,j}\sum_{h=1}^{B_i^{\rm ch}}
    R^{\rm spr,br,ch}_{i,j,h}
\\
  &+
  2\sum_{i,j}
    \bigl(R^{\rm spr,ch}_{i,j}+R^{\rm spr,ch}_{i,j+1}\bigr)
  +
  \sum_{i,j}\sum_{h=3}^{C_i}
    P^{\rm pre,stair,loc,brdg,sh}_{i,j,h}
\\
  &+
  \sum_{i,j}\sum_{h=2}^{B_i}
    P^{\rm pre,br,sh}_{i,j,h}
  +
  \text{long-run, existing spread-return, and exact-return terms}.
\end{aligned}
\]

The matching radial-tail and subdivision criteria have been added.  The
remaining bridge-like chain-depth obstruction is the inward-free confined
bridge family; bridge witnesses with radial backtracking have been absorbed
into spread-return profiles.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
