# Round 312

Round 312 converts the bridge-record persistent prefix profile from
Round 311 into a bounded-gap bridge-record-record prefix-pair profile.

Round 311 left
\[
  P^{\rm pre,per,br,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,br,ch},L_i}.
\]
Applying the ordered-ladder lemma and then the bounded-successor-gap lemma
with \(K=4K_i^{\rm gap,br,ch}\) gives
\[
  P^{\rm pre,per,br,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,ch}_{i,j},
\]
where
\[
  P^{\rm pre,pair,br,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,8K_i^{\rm gap,br,ch},L_i,
    B_i^{\rm br,recbr,ch}}
\]
and
\[
  B_i^{\rm br,recbr,ch}
  =
  \left\lceil
    \frac{64K_i^{\rm gap,br,ch}\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1 .
\]

Substitution into the Round 311 ladder replaces
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  P^{\rm pre,per,br,recbr,ch}_{i,j}
\]
by
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}
  P^{\rm pre,pair,br,recbr,ch}_{i,j}.
\]
The new return-spread family
\(R^{\rm spr,recbr,recbr,ch}\), the bridge-record bridge-return terms, the
older bridge-record spread-return terms, and the long-run coefficient
\[
  2B_i^{\rm ch}B_i^{\rm br,ch}+2B_i^{\rm ch}+3
\]
are unchanged.

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the bounded-gap bridge-record-record prefix-pair family
\(P^{\rm pre,pair,br,recbr,ch}_{i,j}\), which should next be split by the
actual successor gap, in parallel with Rounds 301 and 307.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
