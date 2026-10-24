# Round 318

Round 318 converts the bridge-record-record persistent prefix profile from
Round 317 into a bounded-gap bridge-record-record-record prefix-pair profile.

Round 317 left
\[
  P^{\rm pre,per,br,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,br,recbr,ch},L_i}.
\]
Applying the persistent-prefix ordered-ladder reduction and then the
bounded-successor-gap reduction with \(K=4K_i^{\rm gap,br,recbr,ch}\) gives
\[
  P^{\rm pre,per,br,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,ch}_{i,j},
\]
where
\[
  P^{\rm pre,pair,br,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,
    8K_i^{\rm gap,br,recbr,ch},L_i,
    B_i^{\rm br,recbr,recbr,ch}}
\]
and
\[
  B_i^{\rm br,recbr,recbr,ch}
  =
  \left\lceil
    \frac{64K_i^{\rm gap,br,recbr,ch}\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1 .
\]

Substitution into the Round 317 ladder replaces
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  P^{\rm pre,per,br,recbr,recbr,ch}_{i,j}
\]
by
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  P^{\rm pre,pair,br,recbr,recbr,ch}_{i,j}.
\]
The new return-spread family \(R^{\rm spr,recbr,recbr,recbr,ch}\), the
bridge-record-record bridge-return terms, the older bridge-record and
chain-depth return-spread terms, and the long-run coefficient
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}B_i^{\rm br,recbr,ch}
  +2B_i^{\rm ch}B_i^{\rm br,ch}
  +2B_i^{\rm ch}
  +3
\]
are unchanged.

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the bounded-gap bridge-record-record-record prefix-pair family
\(P^{\rm pre,pair,br,recbr,recbr,ch}_{i,j}\), which should next be split by
the actual successor gap, in parallel with Rounds 301, 307, and 313.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
