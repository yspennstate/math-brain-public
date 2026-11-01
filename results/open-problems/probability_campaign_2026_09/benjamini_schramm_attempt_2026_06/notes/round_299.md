# Round 299

Round 299 applies the existing short prefix-record
persistent-or-returning split to the chain-depth prefix-record profile that
appeared in Round 298.

Set
\[
  K_i^{\rm ch}=512M_iB_iC_i .
\]
The Round 298 finite ladder contains the term
\[
  2P^{\rm pre,rec,ch}_{i,j},
  \qquad
  P^{\rm pre,rec,ch}_{i,j}
  =
  P^{\rm pre,out,rec}_{j,K_i^{\rm ch},L_i}.
\]
By the prefix-record split,
\[
  P^{\rm pre,rec,ch}_{i,j}
  \le
  P^{\rm pre,per,ch}_{i,j}
  +
  R^{\rm spr,ch}_{i,j}
  +
  R^{\rm spr,ch}_{i,j+1},
\]
where
\[
  P^{\rm pre,per,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,2K_i^{\rm ch},L_i},
  \qquad
  R^{\rm spr,ch}_{i,j}
  =
  X^{\rm ret,spr}_{j,4K_i^{\rm ch}} .
\]

Substitution gives a persistent chain-absorbed finite ladder:
\[
\begin{aligned}
  Y_{\lambda_0}^{\rm rad}
  \le&
  Y_{\lambda_N}^{\rm rad}
  +2\sum_{i,j}P^{\rm pre,per,ch}_{i,j}
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
downstream route no longer needs a direct exponent hypothesis on
\(P^{\rm pre,rec,ch}\).  The next remaining chain-depth obstruction is the
persistent-prefix profile \(P^{\rm pre,per,ch}\), together with the larger
threshold spread-return profile \(R^{\rm spr,ch}\).
