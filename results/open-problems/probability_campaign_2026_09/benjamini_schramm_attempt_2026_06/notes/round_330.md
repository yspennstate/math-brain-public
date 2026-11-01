# Round 330

Round 330 converts the bridge-record-record-record-record persistent prefix
profile from Round 329 into a bounded-gap
bridge-record-record-record-record-record prefix-pair profile.

Round 329 left
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i}.
\]
Applying the persistent-prefix ordered-ladder reduction and then the
bounded-successor-gap reduction with
\[
  K=4K_i^{\rm gap,br,recbr,recbr,recbr,ch}
\]
gives
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,ch}_{i,j},
\]
where
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,recbr,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,recbr,recbr,ch}}
\]
and
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64K_i^{\rm gap,br,recbr,recbr,recbr,ch}\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1 .
\]

Substitution into the Round 329 finite ladder replaces
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,ch}
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
by the same coefficient times
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
The new adjacent return-spread family
\(R^{\rm spr,recbr,recbr,recbr,recbr,recbr,ch}\), all older return-spread and
bridge-return families, and the long-run coefficient from Round 328 are
unchanged.

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the bounded-gap bridge-record-record-record-record-record
prefix-pair family
\(P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,ch}_{i,j}\), which should next
be split by the actual successor gap, paralleling Round 325.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
