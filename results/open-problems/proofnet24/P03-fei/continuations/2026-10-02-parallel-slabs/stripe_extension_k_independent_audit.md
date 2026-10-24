# Independent audit: parallel slabs and separated crossings

2 October 2026. I read the entire [stripe_extension_parallel_slabs_candidate.md](stripe_extension_parallel_slabs_candidate.md).

**Verdict:** the parallel-slab proof passes. The separated-crossing proof passes under **strict** separation greater than twice the largest weight. The candidate's nonstrict equality claim has an exact endpoint gap; the influence-additivity identity can fail at equality. This is a proof obstruction at the stated boundary, not a counterexample to FEI itself.

## 1. Exact equality-boundary obstruction

Take largest weight w=1, remaining weights 1/2,1/2, and

\[
 f(z,x,y)=1-2\mathbf1\{-1<z+(x+y)/2<1\}.
\]

The two crossing points are -1 and 1, exactly 2w apart. Let the associated upward crossing indicators be h_1=\mathbf1\{\text{score}>-1\} and h_2=\mathbf1\{\text{score}\ge1\}; these endpoint conventions produce the stated open exceptional interval.

For the remaining score s=(x+y)/2, its values -1,0,1 have probabilities 1/4,1/2,1/4. At s=0 both crossing halfspaces pivot, but their effects cancel in f. Exact counts give

\[
 I_z(f)=1/2,\qquad I_z(h_1)=I_z(h_2)=3/4.
\]

Thus the candidate identity \alpha=\sum_r\alpha_r is false, and the signed pivotal intervals overlap at an atom even though their centers are exactly 2w apart. The exact four-row certificate is [stripe_endpoint_equality_counterexample.json](stripe_endpoint_equality_counterexample.json).

Excluding endpoint ties while preserving this Boolean function forces the lower crossing slightly above -1 and the upper crossing slightly below 1: its score-0 values must stay exceptional and its score-\pm1 values must stay outside. Their new distance is strictly less than 2w. Hence a generic no-tie perturbation cannot preserve the candidate's nonstrict separation requirement.

A sufficient repair is to assume successive crossing distances are **strictly greater** than 2max_i|w_i|. Alternatively one must explicitly assume a representation with no attained-score ties and compatible disjoint pivotal intervals. The unrestricted two-crossing slab theorem is unaffected, because it is free to perturb into its narrow branch.

## 2. Narrow interval and disjoint-branch lemma

For a Boolean split f=A+zB, A^2+B^2=1. If the two exceptional branch supports are disjoint and the outside output is +1, then A=1-|B|. Let \alpha=\mathbb EB^2 and \beta=\mathbb EB. At degree zero the pair masses are (1-\alpha)^2 and \beta^2, with |\beta|\le\alpha. The nonempty pair mass is at most 2\alpha.

For \alpha<1/2, the zero-pair entropy is at most

\[
 \beta^2\log_2(1/\beta^2)+\beta^2\log_2e
 \le2\alpha^2\log_2(1/\alpha)+\alpha^2\log_2e<2\alpha.
\]

Here x\log(1/x) is increasing up to x=1/e, and \beta^2\le\alpha^2<1/4. For \alpha\ge1/2, conditional binary entropy is at most 1\le2\alpha. Combining with the exact split inequality \Delta H\le2\mathcal C gives \Delta H\le8\alpha. No monotonicity or LTF geometry is needed beyond the constant-background identity.

For an interval narrower than 2w, a pair of scores s-w,s+w cannot both lie inside it, so the branch supports are disjoint. Endpoints cause no difficulty under strict narrowness. The complement is handled by an output sign change.

## 3. Signed union under repaired strict separation

Assume crossing distances are greater than 2w. After a sufficiently small endpoint-preserving no-tie perturbation they still have this property, because the finite collection has a positive separation margin. Each coordinate edge of length 2w crosses at most one crossing. Thus

\[
 B=\sum_r\epsilon_rB_r,\quad |B|=\sum_rB_r,\quad
 \alpha=\mathbb EB^2=\sum_r\alpha_r.
\]

Redundant or constant crossings can be removed. Any remaining crossing gives a nonconstant halfspace; its largest-weight influence \alpha_r is positive by the established halfspace influence estimate.

With R=\sum_j a_j^2/w^2, the interval concentration/resampling argument gives

\[
 \operatorname{Stab}_\rho(B)
 \le\mathbb E|B(X)||B(Y)|
 \le\alpha\min\{1,6m/\sqrt{(1-\rho)R}\}.
\]

The relative \alpha factor is legitimate: the good/bad mask event depends only on the independently drawn mask. For the good mask, sum the m interval concentration estimates; for the bad mask, use one. The signed spectrum has nonnegative \rho-stability for \rho\ge0 by its Fourier expansion. Uniform hypercontractivity applies to signed B because |B| is an indicator, yielding \operatorname{Stab}_{1/2}(B)\le\alpha^{4/3}.

For Q_S=\widehat B(S)^2/\alpha these estimates imply the claimed low-degree bound at M=\max\{1,R,\ln(1/\alpha)\}. If R=0, omit the R bound; if \ln(1/\alpha)=0, use M\ge1 and the trivial bound. The zero atom satisfies Q_0=(\mathbb EB)^2/\alpha\le\alpha, rather than equality. These are exactly the hypotheses required by the generalized dyadic argument.

## 4. Density normalization and common KL scale

For each crossing halfspace, let p_r be its minority density and L_r=\ln(1/p_r). The physical influence convention is the same for its indicator and its \{-1,1\} version. The Keller--Klein bound uses total input-weight norm \sqrt{w^2+\sum a_j^2}; hence its normalized largest weight is 1/\sqrt{R+1}. It gives

\[
 \alpha_r\ge c p_r\min\{1,\sqrt{L_r/(R+1)}\},
 \qquad \alpha_r\le2p_r.
\]

There is no reversal of the second inequality: a pivotal edge spends probability \alpha_r/2 at its minority endpoint. Thus L_r\le\ln(2/\alpha_r).

If the stripe function changes under noise, at least one crossing halfspace changes. Union-bounding their established noise estimates gives

\[
 P(K\ge u)\le\frac{A_0}{\sqrt u}\sum_r p_r\sqrt{L_r}.
\]

For u<1, the full nonconstant spectral mass is \operatorname{Var}(f)\le4\sum p_r, from independent noise at rate 1/2, and the pair nonconstant mass is no larger. The stated A_0 easily dominates this regime. No relative small-set noise bound for an interval is asserted.

The common-scale conversion is correct:

\[
 p_r\sqrt{L_r}\le c^{-1}\alpha_r\max\{\sqrt{R+1},\sqrt{L_r}\}
 \le c^{-1}\alpha_r(\sqrt{R+1}+\sqrt{L_r}).
\]

With \lambda_r=\alpha_r/\alpha, weighted Cauchy--Schwarz and Shannon entropy at most \ln m give

\[
 \sum_r\lambda_r\sqrt{L_r}
 \le\sqrt{\ln(2/\alpha)+\sum_r\lambda_r\ln(1/\lambda_r)}
 \le\sqrt{\ln(2m/\alpha)}.
\]

Therefore the pair tail uses the same M as the signed slab spectrum, with the candidate's \Gamma_m. A very remote crossing does not improperly force a maximum bias scale. Every factor of two in the union and input normalization agrees with the completed halfspace proof.

## 5. KL, zero atoms, and induction

The candidate's generalized dyadic calculation has the right sign and constants. The star mass is q_*\le\alpha; replacing it by \alpha weakens the lower bound because \log(1/\alpha)\ge0. The missing baseline is at most \alpha\log(1/\alpha), uniformly bounded. KL data processing lower-bounds the uncoarsened divergence. Pointwise P_S\ge\widehat B(S)^2=\alpha Q_S rules out a positive Q mass with a zero P denominator. The signed coefficients require no further modification.

The spectral inclusion contribution is the exact \alpha[\log(1/\alpha)-D(Q\|P)]; the complementary contribution is at most \alpha\log_2e. Consequently \Delta H\le C_m\alpha. Scalar, constant, and zero remaining-weight cases are handled without defining Q at \alpha=0. Take m\ge1; the m=0 class consists only of constants.

Under strict separation, restriction translates all crossing points by the same amount and can only decrease the largest remaining weight. The positive separation margin remains. If fewer crossings remain after omitting out-of-range ones, all estimates retain the upper bound m. The class is therefore restriction-closed, and the exact influence split gives the claimed dimension induction.

For two arbitrary crossings, move endpoint conventions into gaps in the full finite score set and avoid the finitely many width-equality hyperplanes. This is permitted without a separation constraint. A narrow representation uses Section 2; a wide one is strictly separated and uses the signed proof with m=2. All restrictions remain interval functions, so the universal slab constant is valid for every endpoint convention, including the equality example in Section 1. Infinite endpoints reduce to one-crossing LTFs or constants.

## Verdict

**Parallel-slab theorem: analytic PASS.**

**Strictly separated m-crossing theorem: analytic PASS.**

**Nonstrict equality version with arbitrary endpoint conventions: exact proof gap.** The repair must be stated in the final theorem rather than hidden in a perturbation argument. No other algebraic or induction gap was found. The result does not cover three or more arbitrary nearby crossings, unrestricted Boolean FEI, or biased input-product laws.
