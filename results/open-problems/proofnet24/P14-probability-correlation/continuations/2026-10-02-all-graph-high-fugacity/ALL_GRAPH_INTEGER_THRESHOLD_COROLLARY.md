# An explicit integer-conductance high-fugacity threshold

Research consequence, 2 October 2026. This corollary uses the complete
internally audited [all-graph high-fugacity theorem](ALL_GRAPH_HIGH_FUGACITY_PROOF.md).
The additional arithmetic argument was independently checked by the
heat/entropy analyst. Priority and external peer review remain unverified.

Let G have m>=2 edges and positive integer conductances c_g. For distinct
marked edges e,f set

\[
 P_{ef}=\prod_{g\ne e,f}(1+c_g).
\]

Then the forest Rayleigh polynomial is nonnegative whenever

\[
 \boxed{\lambda\ge 1+2P_{ef}^2.}
\]

For every marked pair on a common cycle it is strictly positive throughout
this range. For different graphic-matroid components it is identically zero.
One may use the larger graph-wide bound
\(1+2\prod_g(1+c_g)^2\) without specifying a pair. For the unweighted
graph the pair bound is uniform over all pairs and simplifies to

\[
 \boxed{\lambda\ge 1+2\,4^{m-2}.}
\]

This is a crude sufficient threshold, not an optimal estimate and not a
statement at every positive fugacity.

## Proof

Multi-affinity gives
\(Z=A+z_eB+z_fC+z_ez_fD\), where each of A,B,C,D is a sum over a subset
of the unmarked edge subsets, with nonnegative coefficient one. Thus
\(R_{ef}=BC-AD\), independent of the marked activities. Specialize only
the unmarked activities to \(\lambda c_g\), obtaining
\(R(\lambda)=\sum_{j=0}^d a_j\lambda^j\) with integer coefficients.

At unmarked activity c, each of A(c),B(c),C(c),D(c) is at most P_ef,
because the generating sum over every unmarked edge subset is exactly
\(P_{ef}\). Nonnegative coefficients and convolution therefore give

\[
 \sum_j|a_j|\le B(c)C(c)+A(c)D(c)\le2P_{ef}^2.
\]

If R is zero the claim is immediate. Otherwise the complete all-graph
theorem says that its highest nonzero coefficient a_d is positive.
Integrality gives a_d>=1. If d=0 it is already strictly positive. If
d>=1 and lambda>=1+2P_ef^2, then lambda>=1 and

\[
 \begin{aligned}
 R(\lambda)&\ge a_d\lambda^d-
                  \sum_{j<d}|a_j|\lambda^{d-1}\\
 &\ge\lambda^{d-1}(\lambda-2P_{ef}^2)>0.
 \end{aligned}
\]

This proves the bound. The graph-wide and unweighted simplifications follow
from P_ef<=product_g(1+c_g) and P_ef=2^(m-2) when every c_g=1.

For positive rational conductances, choose a positive integer D such that
c'_g=D c_g are integers. Activities lambda c equal (lambda/D)c'. Thus
an explicit sufficient original scale is
\(\lambda\ge D[1+2\prod_{g\ne e,f}(1+D c_g)^2]\).
The bound can be enormous; arbitrary real conductances remain covered by
the main qualitative theorem.
