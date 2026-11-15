# Endpoint moments in the maximizing-zoom argument

The question is the moment-preservation step in OpenAI, *Metric-measure limits of subcritical FK and spanning-tree planar maps* (September 24, 2026), Proposition tree:prop:internal_norm_comparison. The relevant sources are [bootstrap.tex](sources/bootstrap.tex), [moments.tex](sources/moments.tex), and [certificates.tex](sources/certificates.tex). The statement below concerns interval costs; it does not prove the spatial certificate comparison or the planar-map limit.

## A uniform tail estimate

Let k be an integer at least two, and let 1/k < p < 1. Consider any collection of laws of nonnegative interval costs X_[a,b] with these properties:

1. Costs are stationary in time, and costs on finitely many intervals with disjoint interiors are independent.
2. For every finite partition a=t_0<...<t_m=b,
   X_[a,b] <= sum_i X_[t_(i-1),t_i] almost surely.
3. For each integer l>=0,
   ||X_[0,2^(-l)]||_k <= 2^(-lp).

The laws need not be the same from one member of the collection to another. Put

\[
\theta=\frac{kp-1}{k-1}>0,\qquad C=1+2^{kp-1}.
\]

Then every law in the collection satisfies, for R>=1,

\[
 \boxed{\quad
 \mathbb E\!\left[X_{[0,1]}^k
       {\bf1}_{\{X_{[0,1]}>R\}}\right]
 \le C R^{-\theta}.\quad}                                      \tag{1}
\]

Consequently these kth powers are uniformly integrable. In fact, for every 0<delta<theta,

\[
 \mathbb E X_{[0,1]}^{k+\delta}
 \le 1+\frac{\delta C}{\theta-\delta}.                           \tag{2}
\]

The constants are independent of the member of the collection.

### Proof

Write X=X_[0,1]. The l=0 assumption gives E X^k<=1. Choose any dyadic integer m=2^l and set

\[
 Y_i=X_{[(i-1)/m,i/m]},\qquad S=\sum_{i=1}^mY_i .
\]

Then X<=S and E Y_i^k<=m^(-kp). The variables Y_i are independent. Expand S^k into its pure part P=sum_i Y_i^k and its mixed part Q. Both parts are nonnegative, and

\[
 \mathbb E P\le m^{1-kp}.                                     \tag{3}
\]

For a mixed monomial H=product_i Y_i^(a_i), its positive integer exponents sum to k, and each is at most k-1. Set u=k/(k-1). Then ua_i<=k. Independence and the monotonicity of moments give

\[
 \mathbb E H^u
 =\prod_i\mathbb E Y_i^{ua_i}
 \le\prod_i(\mathbb E Y_i^k)^{ua_i/k}
 \le m^{-kpu},
 \qquad \|H\|_u\le m^{-kp}.                                   \tag{4}
\]

The sum of all multinomial coefficients in the expansion is m^k. The triangle inequality in L^u therefore yields

\[
 \|Q\|_u\le m^{k-kp}.                                         \tag{5}
\]

This also holds when m=1, since Q=0. Holder's inequality uses conjugate exponents u and k. Markov's inequality uses E X^k<=1. Thus

\[
\begin{aligned}
 \mathbb E[X^k{\bf1}_{\{X>R\}}]
 &\le \mathbb E[P{\bf1}_{\{X>R\}}]
      +\mathbb E[Q{\bf1}_{\{X>R\}}] \\
 &\le m^{1-kp}
      +m^{k-kp}\mathbb P[X>R]^{1/k}\\
 &\le m^{1-kp}+\frac{m^{k-kp}}{R}.                             \tag{6}
\end{aligned}
\]

Choose the largest dyadic m not exceeding R^(1/(k-1)). Then

\[
 \tfrac12 R^{1/(k-1)}<m\le R^{1/(k-1)}.
\]

Since 1-kp<0 and k-kp>0, the two terms in (6) satisfy

\[
 m^{1-kp}\le2^{kp-1}R^{-\theta},\qquad
 m^{k-kp}/R\le R^{-\theta}.                                   \tag{7}
\]

This proves (1), including 1<=R<2^(k-1), where m=1 is allowed.

For x>=0,

\[
 x^{k+\delta}\le x^k+
 \delta x^k\int_1^\infty t^{\delta-1}{\bf1}_{\{x>t\}}\,dt .
\]

For x>=1 there is equality; for x<1 the inequality follows from x^(k+delta)<=x^k. Tonelli's theorem, (1), and E X^k<=1 now give (2).

## Fixed dyadic enlargements and passage to a limit

Let L=2^M for a fixed nonnegative integer M. Subadditivity gives

\[
 X_{[0,L]}\le\sum_{j=0}^{L-1}X_{[j,j+1]} .
\]

By stationarity and the L^(k+delta) triangle inequality, (2) implies

\[
 \|X_{[0,L]}\|_{k+\delta}
 \le L\left(1+\frac{\delta C}{\theta-\delta}\right)^{1/(k+\delta)}.
                                                                    \tag{8}
\]

No independence between these unit costs is needed for this last inequality. In particular,

\[
 \mathbb E[X_{[0,L]}^k{\bf1}_{\{X_{[0,L]}>R\}}]
 \le \frac{L^{k+\delta}}{R^\delta}
       \left(1+\frac{\delta C}{\theta-\delta}\right).             \tag{9}
\]

This is uniform over the collection for each fixed L. By translation, it also applies on any translated interval of that length. Any nonnegative distance bounded by the corresponding internal endpoint cost has the same tail bound. In particular, one may compute the distance between these endpoints in a larger internal graph.

If a sequence of such unit endpoint variables converges in law to X_infinity, bounded continuous truncations x -> min(x^k,A), followed by (1), give

\[
 \mathbb E X_\infty^k=\lim_r\mathbb E X_r^k.                    \tag{10}
\]

For an enlargement use (9) in the same truncation argument. No exchange of an unbounded test function with weak convergence is required.

## Application to the preprint's maximizing zooms

In the notation of [bootstrap.tex](sources/bootstrap.tex), assume the rigid laws and their interval data exist as asserted. For each r, let

\[
 H_r=\sup_{i\ge0}2^{ip}q_{r,i}<\infty,
 \qquad 2^{i_rp}q_{r,i_r}>H_r/2 .
\]

Here H_r>0 by the lower-tip bound for a rigid law with C_r>0. With time unit v_r=2^(-i_r) and cost unit H_r v_r^p,

\[
 \widetilde q_{r,l}
 =\frac{q_{r,i_r+l}}{H_r\,2^{-i_rp}}
 \le2^{-lp},\qquad
 \tfrac12<\widetilde q_{r,0}\le1.                              \tag{11}
\]

The index i_r is chosen from deterministic moments of a law. It is not a random stopping time in the contour realization.

The spanning-tree parameters satisfy p=1/d_(sqrt(2))<1/2, s=p/2, and ks>8. Hence kp>16, so the hypothesis kp>1 above holds. This uses only the symbolic inequalities; no numerical value of d_(sqrt(2)) is needed.

The remaining probabilistic hypotheses have the following exact scope. At discrete resolution, internal costs on disjoint deterministic intervals are functions of disjoint independent walk increments. If a fixed finite vector of these costs converges jointly in law, its limiting coordinates are independent: for bounded continuous f_i,

\[
 \mathbb E\prod_i f_i(Y_i)
 =\lim_n\mathbb E\prod_i f_i(Y_{n,i})
 =\lim_n\prod_i\mathbb E f_i(Y_{n,i})
 =\prod_i\mathbb E f_i(Y_i).
\]

The same argument applies to a sequence of different continuum laws after deterministic zooms. Stationarity and finite-partition subadditivity also pass through the retained joint interval data; the latter is a closed inequality. These are unconditional statements. They assert no closure of conditional independence.

Subject to the existence and joint retention of the interval data asserted in the paper, (1) therefore proves uniform integrability for the entire family of maximizing zooms. If its unit endpoint variables have a weak limit, then (10) and (11) give

\[
 2^{-k}\le\mathbb E\widetilde X_\infty^k\le1.                  \tag{12}
\]

Equations (8)--(10) justify the corresponding moment passage on each fixed dyadic enlargement. Thus the maximizing-zoom argument does not lose its positive unit endpoint moment. The certificate compactness, spatial projection, local upper comparison, and interior lifting still require separate justification.

## Checks on the hypotheses and constants

There is a second derivation of uniform integrability that does not optimize a tail bound. Fix m first in (6), send R to infinity, and obtain a tail limsup at most m^(1-kp). Then send dyadic m to infinity. This proves uniform integrability because kp>1 and confirms the sign and the two limiting orders in (1).

Independence cannot be dropped. For integers r>=1, let B_r be Bernoulli with probability r^(-k), and set X_r([a,b])=(b-a)r B_r. These costs are stationary and exactly additive. Their dyadic norms equal 2^(-l), so they satisfy (11) for every p<1, while E X_r([0,1])^k=1 and X_r([0,1]) tends to zero in probability. The kth powers are not uniformly integrable. All pieces share B_r, so (4) fails. This example has consistent interval data; its failure is precisely the missing independence.

The strict threshold kp>1 is also necessary for this moment argument. Let N_lambda be a stationary Poisson process of rate lambda, and put

\[
 P_k(\lambda)=\mathbb E N_\lambda([0,1])^k
   =\sum_{j=1}^k S(k,j)\lambda^j,\qquad
 Z_\lambda([a,b])
   =N_\lambda([a,b])/P_k(\lambda)^{1/k},
\]

where S(k,j) are the Stirling numbers of the second kind. These interval costs are independent on disjoint interiors and additive. For 0<t<=1, positivity of the coefficients gives P_k(lambda t)<=t P_k(lambda). Thus the dyadic norms satisfy the bound with p=1/k and the unit kth moment is exactly one. As lambda decreases to zero, Z_lambda([0,1]) tends to zero in probability, since the probability of a nonzero value is at most lambda. Its kth powers are not uniformly integrable. This is a threshold example, not a model for the maps.

For the exponent in (7), balance the two powers before inserting the dyadic rounding: m^(1-kp)=m^(k-kp)/R is equivalent to R=m^(k-1). Substitution gives the same theta=(kp-1)/(k-1) as the direct exponent calculation. The factor 2^(kp-1) comes only from rounding down to a dyadic m. These identities and the two counterchecks are also checked in [audit.py](audit.py).

## What this leaves open

The proof of Proposition tree:prop:internal_norm_comparison still needs the passage from C_r/H_r -> 0 to zero local costs, followed by the interior lifting of those zero-cost certificates into the unit interval graph. These are spatial assertions in Proposition tree:prop:certificate_limit, Lemma tree:lem:chart_reconstruction and Lemma tree:lem:nonzero_local_cost of [certificates.tex](sources/certificates.tex). The present argument proves the analytic moment step conditional on the retained interval structure and does not certify these geometric assertions.

The earlier implication from a universal norm comparison and all-scale extraction to A_j=2^(pj+o(j)) remains valid. It remains conditional until its geometric inputs have been checked.

## Independent recheck of the earlier conditional exponent

Assume the earlier inputs: for every fixed positive integer m, every sequence j_r tending to infinity has a further subsequence on which A_(j_r+m)/A_(j_r) converges to a number in [R_0^(-1)2^(mp),R_0 2^(mp)], with a single finite R_0>=1 independent of m. Then, for each m, all sufficiently large j satisfy the same bounds with R_0 replaced by 2R_0. Otherwise extraction from a violating sequence contradicts its limit bound.

Put t_j=log_2(A_j)-pj and c=log_2(2R_0). Thus |t_(j+m)-t_j|<=c eventually, for every fixed m. Along each residue class modulo m, telescoping gives limsup |t_j|/j<=c/m; there are finitely many residues, so the same bound holds without restricting residues. Letting m tend to infinity gives log_2(A_j)/j -> p. This verifies the main deterministic implication in the earlier [PRIOR_PROOF.md](PRIOR_PROOF.md).

For the final scale, assume B_(2n)=n^(p+o(1)), the paper's asserted sphere subsequential limits make H_n/B_(2n) tight and bounded away from zero in probability, and the asserted full metric limit does the same for a_n H_n. If the deterministic a_n B_(2n) escaped to infinity along a subsequence, tightness of a_n H_n would fail. If it escaped to zero, a_n H_n would converge to zero in probability, contrary to noncollapse. Therefore a_n B_(2n) lies eventually between two positive constants, yielding a_n=n^(-p+o(1)). The sphere assertions themselves have not been proved here.
