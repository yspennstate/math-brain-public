# Round 419 nineteenth prefix records split into persistent prefixes

Round 419 applies the short prefix-record persistent/returning split to the
nineteenth prefix-record profiles left by Round 418.

Round 418 left, for every finite \(i,j\), the prefix-record family
\[
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  =
  \mathfrak P^{G\to H,{\rm rad,tan,pre,out,rec,short}}_
  {Q,\lambda_i,\sigma_i,\beta_i,j,
   2K_i^{\rm gap,br,recbr,\ldots,recbr,ch},L_i}
\]
under coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  =
  D_i^{\rm rec,br,recbr,\ldots,ch}
  B_i^{\rm br,recbr,\ldots,recbr,ch}.
\]
It also retained the nineteenth bridge-return spread family and updated the
long-run coefficient to
\[
  A_i^{\rm long,br,recbr,\ldots,recbr,ch}
  =
  A_i^{\rm long,br,recbr,\ldots,ch}
  +
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]

Apply the short prefix-record persistent/returning split with
\[
  K=2K_i^{\rm gap,br,recbr,\ldots,recbr,ch}.
\]
For every finite \(i,j\),
\[
\begin{aligned}
  P^{\rm pre,rec,br,recbr,\ldots,recbr,ch}_{i,j}
  \le&\;
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
\\
  &+
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
  +
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j+1}.
\end{aligned}
\]
The resulting persistent-prefix profile is
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  =
  \mathfrak P^{G\to H,{\rm rad,tan,pre,out,per,short}}_
  {Q,\lambda_i,\sigma_i,\beta_i,j,
   4K_i^{\rm gap,br,recbr,\ldots,recbr,ch},L_i},
\]
and the adjacent return-spread family is placed at the doubled return scale
\[
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,
    8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}}.
\]
Thus the persistent-prefix profile keeps the nineteenth bridge-record
marker depth, while the new adjacent return-spread family is the next
adjacent return layer at that depth.

Substitution into the Round 418 finite ladder replaces the nineteenth
prefix-record contribution under the unchanged coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
\]
by
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  \Bigl(
    P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
    +
    R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
    +
    R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j+1}
  \Bigr).
\]
No new finite multiplicative loss is introduced, and the long-run
coefficient
\[
  A_i^{\rm long,br,recbr,\ldots,recbr,ch}
\]
is unchanged from Round 418.

The nineteenth bridge-return spread family from Round 417, adjacent
nineteenth return-spread family, eighteenth bridge-return and adjacent
return-spread families, seventeenth retained spread families, older retained
families, enlarged spread-return profiles, exact-level return terms, and all
finite cutoffs are retained.

The radial-tail and subdivision criteria now use the resulting
persistent-prefix formulation together with the new adjacent return-spread
family and the retained nineteenth bridge-return spread profiles.  The next
internal issue is to convert the resulting persistent-prefix profiles into
bounded-gap prefix-pair profiles.
