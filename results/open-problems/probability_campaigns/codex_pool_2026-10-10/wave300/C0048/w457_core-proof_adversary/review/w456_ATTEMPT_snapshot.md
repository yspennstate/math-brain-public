# C0048: exact cluster cumulants and the missing uniform potential

Author w456, 2026-10-10. Mathematical claims below are author-proved finite-volume or conditional results, pending w458's independent review. They do not solve C0048 and carry no novelty claim. Exact target and normalization: STATEMENT.md.

## Prior work and scope

C0048-A001 (2026-09-07 attempts.jsonl, line 38) tried improved reflection-positive contour counting. It recorded no result: contour entropy was uncontrolled at q=3,d=3, and the planar six-vertex transfer-matrix argument had no justified higher-dimensional replacement. Its numerical descriptions and constants are not certified here. The high-dimensional Biskup--Chayes theorem has an explicit sufficiently-large-dimension scope, not all d>=3. This packet takes the disjoint field-cumulant / uniform-potential lane.

Recall timed out after the instructed 60 seconds. The named perceptron scar is used as a warning that conditional or missing inputs must stay visible, and that source checks are not proofs. No conditional probabilities are multiplied without a conditional independence argument.

## L1. Exact second, third and fourth field cumulants (finite graphs)

Let G=(V,E) be any nonempty finite graph, N=|V|, integer q>=2, and beta>=0. Use FREE boundary, zero external field and weight exp(beta sum_e 1{sigma_x=sigma_y}). Let X=sum_x (1{sigma_x=1}-1/q), S_j(omega)=sum_{FK clusters C}|C|^j, and

P_G(h)=N^{-1} log E_mu[exp(h X)].

Expectations and variance of S_j below use the zero-field FREE FK law with p=1-exp(-beta). Put

a2=(q-1)/q^2,
a3=(q-1)(q-2)/q^3,
a4=(q-1)(q^2-6q+6)/q^4.

Then exactly

P_G''(0)=a2 E[S_2]/N,
P_G'''(0)=a3 E[S_3]/N,
P_G''''(0)=(a4 E[S_4]+3 a2^2 Var(S_2))/N.

Proof. Expand each edge factor as 1+(exp(beta)-1)1{same colour}. Conditional on the resulting FK edges, each cluster receives an independent uniform colour. A centered cluster-colour indicator Y has E[Y]=0, kappa_2(Y)=a2, kappa_3(Y)=a3 and kappa_4(Y)=a4. Conditional on omega, X=sum_C |C|Y_C. Therefore E[X^2|omega]=a2 S_2 and E[X^3|omega]=a3 S_3. Also E[X^4|omega]=a4 S_4+3 a2^2 S_2^2. Unconditionally E[X]=0, so kappa_4(X)=E[X^4]-3 E[X^2]^2=a4 E[S_4]+3 a2^2 Var(S_2). Derivatives of log moment generating functions are cumulants; divide by N. This proves all three identities. Conditional cluster-colour independence is legitimate; independence of the random cluster sizes is neither assumed nor true.

The fourth-order variance term cannot be dropped. It is nonnegative and can change the sign of the quartic pressure coefficient. For q=3, a4=-2/27 while 3a2^2=4/27. A formula retaining only a4 E[S_4]/N omits a genuine contribution, not a harmless notation choice.

## L2. A rigorous obstruction to a bare cubic argument

For q>2, P_G'''(0)>0 on every nonempty finite graph at every beta>=0 because S_3>=N and a3>0. Thus this sign alone has no dimension-sensitive information. At beta=0 the infinite-volume pressure is real analytic for every real h:

P_0(h)=log((exp((1-1/q)h)+(q-1)exp(-h/q))/q),

with P_0'''(0)=a3>0 and magnetization tending continuously to zero as h tends to zero. More directly, the planar q=3 Potts model has the same positive finite-volume cubic sign and a rigorously continuous thermal transition (Duminil-Copin--Sidoravicius--Tassion, arXiv:1505.04159). A dimension-sensitive control of a thermodynamic potential or its remainder is necessary.

## L3. Finite-volume Legendre coefficients and an explicit remainder obstruction

Write A=P_G''(0)>0 and B=P_G'''(0). The Legendre transform I_G(m)=sup_h{hm-P_G(h)} for the centered spin density m has, near m=0,

I_G(m)=m^2/(2A)-B m^3/(6A^3)+O(m^4).

Proof. Analyticity and A>0 give a local inverse to m=P_G'(h)=A h+B h^2/2+O(h^3). Its expansion is h=m/A-B m^2/(2A^3)+O(m^3). Since I_G'(m)=h and I_G(0)=0, integration proves the formula. The constant and neighborhood hidden in O(m^4) may depend on G and beta; no uniformity is asserted.

An exact moment inequality gives E[S_3]/N >= (E[S_2]/N)^2: configuration-wise Cauchy--Schwarz gives S_2^2 <= S_3 S_1=N S_3, and Jensen completes the expectation step. Consequently

B/(6A^3) >= q(q-2)/(6(q-1) A).

This lower bound tends to zero if susceptibility A diverges. It does not supply a positive uniform cubic coefficient.

More quantitatively, suppose for some r0,b,C>0, I_G(m)<=m^2/(2A)-b m^3+C m^4 throughout 0<=m<=r0. Since I_G>=0, for every r in (0,r0], 1/(2A)>=b r-C r^2. With r=min(r0,b/(2C)), this bounds A above by 1/[2(b r-C r^2)]. In particular, if r0>=b/(2C), then A<=2C/b^2. Thus a sequence with A tending to infinity cannot have BOTH a fixed positive cubic lower coefficient and a fixed quartic upper remainder on a fixed neighborhood. This is a proved incompatibility, not an estimate of critical susceptibility.

## L4. Quantitative cubic exclusion lemma

Let r0>0, b>0 and C>=0. Let F be differentiable on [0,r0], with

F(m)=a m^2-b_t m^3+R(m), b_t>=b,
|R(m)|<=C m^4 and |R'(m)|<=4C m^3.

If 0<m<r0, F'(m)=0, and F(m)<=F(0)=0, then m>=b/(6C) when C>0. Equivalently, no such point exists with 0<m<min(r0,b/(6C)). For C=0 there is no such interior point.

Proof. Stationarity yields a=(3/2)b_t m-R'(m)/(2m). Substitute into F to obtain F(m)=(b_t/2)m^3+R(m)-(m/2)R'(m) >= (b/2)m^3-3C m^4. This is strictly positive for 0<m<b/(6C), contradicting F(m)<=0. No assumption on the sign or limit of a is needed.

## L5. Conditional bridge to the full Potts target, including the critical endpoint

Fix q>=3,d>=3. Suppose there are delta,r0,b>0 and C>=0 such that for every beta in (beta_c,beta_c+delta), the normalized monochromatic-boundary magnetization M(beta) has the following property: if 0<M(beta)<r0, there exists a differentiable scalar potential F_beta on [0,r0] satisfying all hypotheses of L4, with the SAME r0,b,C, and F_beta'(M(beta))=0 and F_beta(M(beta))<=F_beta(0)=0. Then, since M(beta)>0 for beta>beta_c, L4 implies M(beta)>=eta, where eta=min(r0,b/(6C)) for C>0 and eta=r0 for C=0.

The critical endpoint is not a limit-exchange assumption. Let M_n(beta) be the corresponding finite-box magnetization. FK boundary comparison gives M_n decreasing in n; each M_n is continuous in beta. Therefore M(beta)=inf_n M_n(beta) is upper semicontinuous. FK parameter monotonicity gives M(beta) nondecreasing in beta. For beta_k decreasing to beta_c, upper semicontinuity gives M(beta_c)>=limsup_k M(beta_k), while monotonicity gives the reverse inequality. Hence M(beta_c)=lim_{beta down to beta_c}M(beta)>=eta>0, proving C0048 CONDITIONALLY on the displayed potential input.

For completeness, boundary comparison used here follows from the FK domain Markov property: conditioning edges outside a smaller box induces a partition of its boundary vertices; the fully wired partition dominates every such induced partition for q>=1. Increasing-volume and increasing-p comparison then follow by the standard increasing coupling. No estimate of its rate is used.

## Hardest missing lemma: uniform scalar-potential input SP(q,d)

Prove the uniformly controlled potentials required in L5 for the ACTUAL nearest-neighbour Potts Gibbs magnetization, for each fixed q>=3,d>=3, including q=d=3. This includes the physical minimum/stationarity link and a positive cubic coefficient with a volume- and temperature-uniform C1 quartic remainder. None of these bulk controls follows from L1's finite-volume expansion.

Attempt at SP. The independent-colour entropy along a one-preferred-colour density is

J_q(m)=[(1+(q-1)m)/q]log(1+(q-1)m)+[(q-1)(1-m)/q]log(1-m).

Its cubic expansion is J_q(m)=(q-1)m^2/2-(q-1)(q-2)m^3/6+R_q(m). On [0,r0] with r0<1, J_q''''(m)<=K=2(q-1)/q*((q-1)^3+(1-r0)^(-3)); Taylor's integral remainder gives |R_q(m)|<=K m^4/24 and |R_q'(m)|<=K m^3/6. Thus a scalar mean-field potential J_q(m)-lambda m^2 satisfies L4 with b=(q-1)(q-2)/6 and C=K/24. For q=3 and r0=1/2 this gives b=1/3,C=8/9, and exclusion threshold 1/16. This is a proved scalar mean-field SPECIAL CASE only.

The attempt fails at replacing the nearest-neighbour model's constrained free energy by J_q(m)-lambda m^2 plus a uniform C1 quartic correction. Spatial correlations contribute, and the exact fourth cumulant includes Var(S_2). Moreover, the full thermodynamic Legendre potential is convex and may have a flat coexistence segment; it cannot be silently identified with a nonconvex mean-field branch. The second/third cluster moment inequality in L3 supplies no uniform b. This is the single unresolved input SP(q,d); it is not renamed a proof of C0048.

NEXT: Independently verify L1--L5 and the mean-field constants; then derive or refute SP(q,d) by controlling the spatial-correlation contribution to the constrained potential, with q=d=3 as the first missing case.
