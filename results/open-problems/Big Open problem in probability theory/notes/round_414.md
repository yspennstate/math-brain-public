# Round 414

Round 414 converts the nineteenth persistent-prefix profiles from Round 413
into bounded-gap prefix-pair profiles.

Round 413 left the persistent-prefix family
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
\]
at scale
\[
  4K_i^{\rm gap,br,recbr,\ldots,recbr,ch}.
\]
For each finite \(i\), set
\[
  \Theta_i=\theta_{\lambda_i,\sigma_i,\beta_i}
\]
and define the bounded-gap cutoff
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\Theta_i}
    K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  \right\rceil+1 .
\]
The ordered-ladder and bounded-successor-gap reductions give
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}
  \le
  P^{\rm pre,pair,br,recbr,\ldots,recbr,ch}_{i,j},
\]
where the bounded-gap prefix-pair profile uses scale
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and cutoff \(B_i^{\rm br,recbr,\ldots,recbr,ch}\).

Substitution into the Round 413 finite ladder replaces only the nineteenth
persistent-prefix contribution by the nineteenth bounded-gap prefix-pair
contribution.  The coefficient
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
\]
and the long-run coefficient are unchanged.  The adjacent nineteenth
return-spread family, eighteenth bridge-return and adjacent return-spread
families, seventeenth retained spread families, older retained families,
enlarged spread-return profiles, exact-level return terms, and all finite
cutoffs are retained.

The radial-tail and subdivision criteria now use the nineteenth bounded-gap
prefix-pair formulation.  The next internal move is to split this bounded-gap
prefix-pair family into finite fixed-gap prefix-pair profiles.

External status was refreshed during this round using targeted arXiv queries.
The search again found partial-result regimes and no primary-source claim
resolving the general nonamenable quasi-transitive \(p_c<p_u\) problem or the
stronger \(p_c<p_{2\to2}\) target.
