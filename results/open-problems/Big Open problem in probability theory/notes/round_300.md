# Round 300

Round 300 converts the Round 299 chain-depth persistent-prefix family into a
bounded-gap chain-depth prefix-pair family.

Set
\[
  K_i^{\rm per,ch}=1024M_iB_iC_i .
\]
The existing ordered-ladder lemma applies at this depth:
\[
  P^{\rm pre,per,ch}_{i,j}
  \le
  P^{\rm pre,lad,ch}_{i,j}.
\]
The existing bounded-successor-gap lemma then gives
\[
  P^{\rm pre,lad,ch}_{i,j}
  \le
  P^{\rm pre,pair,ch}_{i,j},
\]
where
\[
  P^{\rm pre,pair,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,2048M_iB_iC_i,L_i,B_i^{\rm ch}}
\]
and
\[
  B_i^{\rm ch}
  =
  \left\lceil
    \frac{16384M_iB_iC_i\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1 .
\]

Substitution into the persistent chain-absorbed finite ladder gives
\[
\begin{aligned}
  Y_{\lambda_0}^{\rm rad}
  \le&
  Y_{\lambda_N}^{\rm rad}
  +2\sum_{i,j}P^{\rm pre,pair,ch}_{i,j}
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

The corresponding radial-tail and subdivision criteria have been added.
The downstream route no longer needs direct control of
\(P^{\rm pre,per,ch}\); it now needs bounded-gap chain-depth prefix-pair
control and the chain-depth spread-return profile.
