# Round 420 nineteenth persistent prefixes convert to bounded-gap prefix-pair profiles

Round 420 converts the nineteenth persistent-prefix profiles left by Round
419 into bounded-gap prefix-pair profiles at the same current marker depth.

Round 419 left, for every finite \(i,j\), the persistent-prefix contribution
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  =
  \mathfrak P^{G\to H,{\rm rad,tan,pre,out,per,short}}_
  {Q,\lambda_i,\sigma_i,\beta_i,j,
   4K_i^{\rm gap,br,recbr,\ldots,recbr,ch},L_i}
\]
under coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}.
\]
It also retained the adjacent nineteenth return-spread family
\[
  R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
  =
  X^{\rm rad,ret,spr}_{j,
    8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}}.
\]

For each finite \(i\), set
\[
  \Theta_i=\theta_{\lambda_i,\sigma_i,\beta_i}
\]
and define the current bounded-gap budget by
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\Theta_i}
    K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  \right\rceil+1 .
\]
The \(B_i\)-superscript is at the same current bridge-record marker depth as
the persistent-prefix profile, while the gap scale is the Round 419 source
scale.

The local conversion lemma is the ordered persistent-prefix ladder followed
by the bounded-successor-gap reduction:
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
The bounded-gap prefix-pair profile uses scale
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and cutoff \(B_i^{\rm br,recbr,\ldots,recbr,ch}\).  Thus the persistent
prefix obstruction is replaced by a bounded-gap successor-pair obstruction;
no return-spread, bridge-return, or long-run term is created by this local
step.

Substitution into the Round 419 finite ladder replaces
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  \Bigl(
    P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
    +
    R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
    +
    R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j+1}
  \Bigr)
\]
by
\[
  D_i^{\rm rec,br,recbr,\ldots,recbr,ch}
  \Bigl(
    P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j}
    +
    R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j}
    +
    R^{\rm spr,recbr,\ldots,recbr,ch}_{i,j+1}
  \Bigr).
\]

The exact carry-forward invariants are:

* the coefficient \(D_i^{\rm rec,br,recbr,\ldots,recbr,ch}\) is unchanged;
* the long-run coefficient
  \(A_i^{\rm long,br,recbr,\ldots,recbr,ch}\) is unchanged from Round 418;
* the adjacent nineteenth return-spread family from Round 419 is retained at
  radius \(8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}\);
* the nineteenth bridge-return spread family from Round 417 is retained;
* the eighteenth bridge-return and adjacent return-spread families,
  seventeenth retained spread families, older retained families, enlarged
  spread-return profiles, exact-level return terms, and all previously fixed
  finite cutoffs are retained.

The radial-tail and subdivision criteria now use the nineteenth bounded-gap
prefix-pair formulation together with the retained adjacent return-spread and
bridge-return profiles.  The next unresolved issue is to decompose this
bounded-gap prefix-pair family into a finite family of fixed-gap prefix-pair
profiles at the same current marker depth.
