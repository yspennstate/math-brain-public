# Round 306

Round 306 converts the bridge-record persistent-prefix profile into a
bounded-gap bridge-record prefix-pair profile.

Round 305 left
\[
  P^{\rm pre,per,br,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,4K_i^{\rm gap,ch},L_i}.
\]
Applying the ordered-ladder lemma and the bounded-successor-gap lemma gives
\[
  P^{\rm pre,per,br,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,ch}_{i,j},
\]
where
\[
  P^{\rm pre,pair,br,ch}_{i,j}
  =
  P^{\rm pre,out,per,pair}_{j,8K_i^{\rm gap,ch},L_i,B_i^{\rm br,ch}}
\]
and
\[
  B_i^{\rm br,ch}
  =
  \left\lceil
    \frac{64K_i^{\rm gap,ch}\beta_i}
         {\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1 .
\]

Substitution into the Round 305 ladder replaces
\[
  2B_i^{\rm ch}P^{\rm pre,per,br,ch}_{i,j}
\]
by
\[
  2B_i^{\rm ch}P^{\rm pre,pair,br,ch}_{i,j}.
\]

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the bounded-gap bridge-record prefix-pair family
\(P^{\rm pre,pair,br,ch}_{i,j}\), together with the bridge-record
spread-return and bridge-return spread profiles.

No external literature refresh was performed in this round; the Round 298
source-checked status remains the latest external status.
