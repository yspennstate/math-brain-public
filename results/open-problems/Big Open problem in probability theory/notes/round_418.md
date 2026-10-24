# Round 418 nineteenth inward-free bridges absorb into records

Round 418 absorbs the nineteenth inward-free bridge profiles from Round 417
into prefix-record profiles, retaining the nineteenth bridge-return spread
family and updating the long-run coefficient.

Round 417 left, for every finite \(i,j,h\) with
\[
  1\le h\le B_i^{\rm br,recbr,\ldots,recbr,ch},
\]
the confined-bridge input inequality
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  +
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]
Both child profiles are evaluated at the doubled fixed-gap scale
\[
  2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},
\]
with the bridge-return spread radius
\[
  2K_i^{\rm gap,br,recbr,\ldots,recbr,ch}\max\{h-1,1\}.
\]

Define the nineteenth prefix-record profile at this same doubled scale by
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  =
  \mathfrak P^{G\to H,{\rm rad,tan,pre,out,rec,short}}_
  {Q,\lambda_i,\sigma_i,\beta_i,j,
   2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},L_i}.
\]

For each finite \(i,j,h\), the inward-free bridge chain/long-run alternative
gives
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,stair,loc,chain}_{i,j,h+1}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}.
\]
Since \(h+1\ge2\), the locally short staircase-chain-to-prefix-record
reduction, at threshold
\(2K_i^{\rm gap,br,recbr,\ldots,recbr,ch}\), bounds the chain term by
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
Therefore
\[
  P^{\rm pre,br,free,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j},
\]
and the Round 417 input inequality becomes
\[
  P^{\rm pre,br,recbr,\ldots,recbr,ch}_{i,j,h}
  \le
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  +
  W_{\beta_i,p}T^{\rm long}_{i,j}
  +
  R^{\rm spr,br,recbr,\ldots,recbr,ch}_{i,j,h}.
\]

Substitution into the Round 417 finite ladder replaces the finite
inward-free bridge sum, under the source coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch},
\]
by the nineteenth prefix-record sum with coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,\ldots,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
Here the coefficient on the left has one more \({\rm recbr}\) marker than
the source coefficient.  The long-run coefficient is updated by
\[
  A_i^{\rm long,br,recbr,\ldots,recbr,ch}
  =
  A_i^{\rm long,br,recbr,\ldots,ch}
  +
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]

The nineteenth bridge-return spread family from Round 417, adjacent
nineteenth return-spread family, eighteenth bridge-return and adjacent
return-spread families, seventeenth retained spread families, older retained
families, enlarged spread-return profiles, exact-level return terms, and all
finite cutoffs are retained.

The radial-tail and subdivision criteria now use the nineteenth
prefix-record profiles, the retained nineteenth bridge-return spread
profiles, and the updated long-run coefficient.  The next internal issue is
to split the nineteenth prefix-record profiles into persistent-prefix
profiles plus adjacent return-spread profiles.
