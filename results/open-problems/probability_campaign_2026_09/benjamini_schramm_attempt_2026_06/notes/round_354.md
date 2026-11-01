# Round 354

Round 354 converts the ninth persistent prefix profile left by Round 353 into
a bounded-gap prefix-pair profile.

Round 353 left the persistent family
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  =
  P^{\rm pre,out,per}_{j,
    4K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch},L_i}.
\]
The ordered-ladder and bounded-successor reductions give
\[
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
Here
\[
\begin{aligned}
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  &=
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  \right\rceil+1,
\end{aligned}
\]
and the bounded-gap pair profile uses cutoff
\[
  8K_i^{\rm gap,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
\]
and successor-gap bound
\[
  B_i^{\rm br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}.
\]

Substitution into the Round 353 finite ladder replaces
\[
  D_i^{\rm rec,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}
  P^{\rm pre,per,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
by the same coefficient times
\[
  P^{\rm pre,pair,br,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}.
\]
The adjacent return-spread family
\[
  R^{\rm spr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,recbr,ch}_{i,j}
\]
from Round 353 is retained, as are the eighth bridge-return family, older
return-spread and bridge-return families, long-run profiles, exact-level
return profiles, and all existing fixed finite coefficients.

The matching radial-tail and subdivision criteria have been added.  The next
obstruction is the ninth bounded-gap prefix-pair profile, which should next be
split by the actual successor gap, paralleling Round 349.

No external literature refresh was performed in this round; the Round 339
source-checked status remains the latest external status.
