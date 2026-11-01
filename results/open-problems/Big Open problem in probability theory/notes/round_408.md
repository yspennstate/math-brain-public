# Round 408

Round 408 converts the eighteenth persistent-prefix family from Round 407
into bounded-gap prefix-pair profiles.

The input profile is
\[
  P^{\rm pre,per,br,recbr,\ldots,recbr,ch}_{i,j}.
\]
First apply the ordered persistent-prefix ladder reduction with
\[
  K=4K_i^{\rm gap,br,recbr,\ldots,recbr,ch}.
\]
Then apply the bounded-successor-gap reduction.  Since the latter doubles
the cutoff, the bounded-gap profile uses
\[
  8K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
\]
and a fixed successor-gap range
\[
  B_i^{\rm br,recbr,\ldots,recbr,ch}
  =
  \left\lceil
    \frac{64\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}\,
    K_i^{\rm gap,br,recbr,\ldots,recbr,ch}
  \right\rceil+1.
\]

Substitution into the Round 407 finite ladder replaces the persistent-prefix
term
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
  \sum_j P_{i,j}^{\rm per17}
\]
by
\[
  D_i^{\rm rec,br,recbr,\ldots,ch}
  \sum_j P_{i,j}^{\rm pair18}.
\]
No long-run coefficient changes and no new nonconstant multiplicative loss
is introduced.  The adjacent eighteenth return-spread family, the
seventeenth bridge-return and adjacent return-spread families, all older
retained spread families, enlarged spread-return profiles, exact-level return
terms, and long-run profiles are retained.

The radial-tail and subdivision criteria now use the eighteenth bounded-gap
formulation.  The next internal move is to split this bounded-gap prefix-pair
family into a finite sum over fixed successor gaps.

External status was refreshed during this round using targeted arXiv queries.
The search again found only partial-result regimes and no primary-source
claim resolving the general nonamenable quasi-transitive \(p_c<p_u\) problem
or the stronger \(p_c<p_{2\to2}\) target.
