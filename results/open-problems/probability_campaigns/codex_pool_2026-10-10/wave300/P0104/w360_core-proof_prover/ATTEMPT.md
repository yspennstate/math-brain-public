# P0104 core-proof checkpoint

## Scope

P0104 is the grouped intake record at Downloads/Probability_1000_20h_20260906/problems.jsonl:175, citing ADH Questions 13 and 15. The original source asks for a fluctuation exponent below 1/2 in dimensions >=2 under suitable edge-law conditions, its planar value 1/3, and positivity in a suitable dimension. In the checked arXiv v2 both questions are on PDF page 37, section 3.1; the intake's page 34/40 pointers were corrected. The source leaves the precise conditions and interpretation of variance scaling open. Current openness UNKNOWN. The selected precise model is undirected nearest-neighbour FPP on Z^2 with iid Uniform[1,2] edge times, endpoints 0 and n e_1, n >= 1. The proposed exponent is Var(T_n)=n^(2/3+o(1)); this has not been proved.

The prior attempt P0104-A001, attempts.jsonl:106, proves that O(n/log n) does not give chi<1/2: log(n/log n)/(2 log n) tends to 1/2. It explicitly claims no solution. The named H/I probe found no P0104 proof and the annotated Lean ranking is historical attempted_un, not a formal receipt. The two checked canonical-store campaign claims separate a verified abstract resampling engine from an unverified variance-comparison wall. The April 2026 primary paper arXiv:2604.01214 proves a polynomial variance improvement for a particular rotationally invariant Riemannian model, which does not apply to this iid lattice model. No novelty or retirement conclusion follows from this targeted check.

## Saved lemma C1: exact finite reduction

Let G_n be the induced nearest-neighbour graph on the vertices [-2n,2n]^2 intersect Z^2. Then T_n equals the minimum over the finitely many simple paths in G_n from 0 to n e_1, for every configuration of weights in [1,2]. In particular T_n is a bounded function of finitely many independent coordinates.

Proof. The direct horizontal path has n edges and cost at most 2n. Every path with more than 2n edges has cost greater than 2n. A path leaving the square must have at least 2n+1 edges before its first vertex outside it, so cannot improve the direct path. Removing a loop strictly decreases cost because every edge weight is at least 1. Thus a minimizing path can be chosen among the finite collection of simple paths in G_n. Conversely these are allowed lattice paths. Both minima agree. Also n <= T_n <= 2n.

This is an elementary special-case reduction, not a novel FPP theorem and not a solution of P0104. Independent review by w362 is pending.

## Single hardest remaining gap

Prove two-sided estimates at the n^(2/3) scale for the integral of the edge replacement-threshold covariance under independent coordinate resampling. The exact integral and its load-bearing hypotheses will be written next. No independence of different geodesic corridors is being assumed.

## Saved lemma C2: replacement thresholds and the uniform covariance kernel

Write each edge time as 1+U_e with U_e Uniform[0,1]. With all other coordinates fixed, let A_e be the minimum cost of a simple endpoint-to-endpoint path avoiding e and B_e the minimum cost of a simple path containing e with e's weight removed. A_e is finite in G_n; allow B_e=+infinity. Define a_e=clamp(A_e-B_e-1,0,1), with a_e=0 if B_e is infinite. Then for a constant c_e depending only on the other coordinates,

    T_n(U_e, U_-e) = c_e + min(U_e, a_e).

Proof. Minimize separately among avoiding and containing paths to get min(A_e,B_e+1+U_e). If A_e-B_e-1 is below 0 the function is constant; if above 1 it is affine throughout [0,1]; inside [0,1] it is B_e+1+min(U_e,a_e). These three cases give the displayed formula, including B_e infinite.

For one common independent U Uniform[0,1] define K(a,b)=Cov(min(U,a),min(U,b)). If m=min(a,b) and M=max(a,b), then

    K(a,b) = (m^2/2) (M - M^2/2 - m/3).

Proof. For a<=b, E min(U,a)=a-a^2/2 and E[min(U,a) min(U,b)]=ab-ab^2/2-a^3/6, by integrating over [0,a], [a,b], [b,1]. Subtract the product of the means. Symmetry gives the other ordering. Equivalently K(a,b)=integral_0^a integral_0^b [min(u,v)-uv] du dv. Its integrand is nonnegative. Hence K is coordinatewise increasing, K(a,a)=a^3/3-a^4/4, and K(a,b)>=K(eta,eta) whenever both thresholds are at least eta.

Independent derivation of the same polynomial was reported by w361. This is an exact special-case identity, not a novelty claim.

## Saved lemma C3: exact noise integral with its first-order floor

For 0<=rho<=1 let U_-e^rho independently retain each coordinate other than e with probability rho and otherwise replace it by a fresh Uniform[0,1]. The coordinate e is shared between the two environments when forming the conditional covariance. Define

    J_n(rho) = sum_e E K(a_e(U_-e), a_e(U_-e^rho)).

Then

    Var(T_n) = integral_0^1 J_n(rho) d rho
             = integral_0^infinity exp(-t) J_n(exp(-t)) dt.

Proof. For the finite coordinate set E_n let f=T_n-E T_n and use its Hoeffding decomposition f=sum_{nonempty S subset E_n} f_S. One direct definition is f_S=sum_{A subset S} (-1)^(|S|-|A|) E[f | U_A]. Product independence implies orthogonality, and each f_S has conditional mean zero in every coordinate in S. Let D_e f=f-E[f | U_-e]. Sharing e and resampling every other coordinate with retention rho gives

    E[D_e f(U) D_e f(U_e,U_-e^rho)]
       = sum_{S containing e} rho^(|S|-1) ||f_S||_2^2.

To verify this, expand both finite sums. Distinct subsets have an unpaired coordinate, whose conditional mean is zero. For equal subsets, every replaced coordinate in S other than e kills the term, while retaining all |S|-1 of them leaves its squared norm. Conditional covariance in U_e is exactly K. Thus

    J_n(rho) = sum_S |S| rho^(|S|-1) ||f_S||_2^2.

Integrate each finite monomial: integral_0^1 |S| rho^(|S|-1) d rho=1. Orthogonality proves the variance formula. Setting rho=exp(-t) produces the exp(-t) Jacobian.

The persistent first-order term is

    L_n=J_n(0)=sum_e ||f_{ {e} }||_2^2.

Write R_n(rho)=J_n(rho)-L_n. Its coefficients are nonnegative and it tends to zero at rho=0. The exact decomposition is Var(T_n)=L_n+integral_0^1 R_n(rho) d rho. A bound claiming that the full J_n(exp(-t)) decays to zero requires L_n=0, which has not been assumed. This incorporates w361's first-order-floor warning.

## Saved lemma C4: many robust replacement margins in continuous FPP

For n>=9 in this model,

    n/8192 <= J_n(1) <= 2n/3.

With eta=1/64, the expected number of edges whose off-edge threshold a_e is at least eta is between n/1024 and 128n. More concretely the expected number of edges on the unique geodesic whose replacement gap (best avoiding-path cost minus T_n) is at least 1/128 is at least n/2048.

Proof. The finite simple geodesic gamma has n<=|gamma|<=2n and is unique almost surely: distinct simple paths have distinct edge sets, so their cost difference is a nonconstant continuous linear combination of independent weights. Except at ties of measure zero, conditional on U_-e an edge belongs to gamma exactly when U_e<a_e. Consequently

    sum_e E a_e = E|gamma| <= 2n,
    sum_e E a_e^3 = 3 E sum_{e in gamma} U_e^2.

For a fixed simple path of length l, if sum U_e^2<=l/1024, at most l/4 of its edges can have U_e>=1/16. Thus at least 3l/4 coordinates satisfy U_e<1/16. Independence applies on this fixed path. A union over their subsets bounds the probability by 2^l (1/16)^(3l/4)=(1/4)^l. The number of simple paths of length l starting at 0 is at most 4*3^(l-1). A union bound over all l>=n therefore gives

    P(exists such a cheap simple path of length >=n)
      <= (16/3)(3/4)^n <= 1/2  for n>=9.

No conditional probabilities along a selected geodesic were multiplied. On the complement, sum_{e in gamma} U_e^2>n/1024, and hence sum_e E a_e^3>=3n/2048. The kernel obeys a^3/12<=K(a,a)<=a/3 on [0,1], proving the energy bounds.

The part of sum E a_e^3 contributed by a_e<eta is at most eta^2 sum E a_e<=n/2048. The rest is at least n/1024. Since a_e^3<=1, sum P(a_e>=eta)>=n/1024. The opposite bound uses eta*P(a_e>=eta)<=E a_e and sums to 128n.

Finally, given a_e>=eta, the event U_e<=a_e/2 has conditional probability a_e/2 and gives an avoiding-path gap at least a_e/2>=1/128. This remains valid when the unclamped threshold exceeds 1. Its expected count is (1/2)sum E[a_e 1_{a_e>=eta}], at least (1/2)sum E[a_e^3 1_{a_e>=eta}]>=n/2048. The bound also concerns full-lattice avoiding paths, not merely the finite box: any path leaving G_n costs at least 2n+1, while T_n<=2n. Such a path therefore has slack at least 1 and cannot destroy a finite-box slack bound of 1/128. The lemma stops at zero resampling; it proves no persistence window.

## Precise remaining input and a proved conditional route

The single hardest remaining input is a quantitative noise estimate at rate n^(-1/3), not marginal energy. A sufficient, unproved version is the following. For every 0<epsilon<1/3, suppose constants c,C>0, eta in (0,1], p>1, n_0 exist such that for n>=n_0:

1. L_n<=C n^(2/3+epsilon).
2. R_n(1-s)<=C n (1+s n^(1/3-epsilon))^(-p) for 0<=s<=1.
3. sum_e P(a_e(U_-e)>=eta, a_e(U_-e^(1-s))>=eta)>=c n for 0<=s<=n^(-1/3-epsilon).

Then the exact integral gives

    c K(eta,eta) n^(2/3-epsilon) <= Var(T_n)
      <= C(1+1/(p-1)) n^(2/3+epsilon).

The lower bound integrates the monotone kernel bound over the stated noise window. The upper bound integrates the remainder using x=s n^(1/3-epsilon) and integral_0^infinity (1+x)^(-p) dx=1/(p-1), then adds L_n. If these unproved hypotheses hold for every epsilon, the selected variance exponent equals 2/3. C4 establishes only the zero-noise marginal precursor to hypothesis 3; it supplies no positive polynomial noise window and does not establish 1 or 2.

The unweighted-overlap shortcut has a further obstruction: K(a,a)=a^3/3-a^4/4, while the conditional probability that the shared edge belongs to both paths with threshold a is a. Their ratio tends to zero as a decreases to zero. No distribution-free positive constant can lower-bound K by the bare overlap probability. Positive margins are necessary in this particular lower-bound route.

## Attempt at the hard input: a proved small window, far short of KPZ

Let N_n=|E_n|=8n(4n+1)=32n^2+8n. For eta=1/64 and n>=9 the coupled robust-threshold count satisfies

    Q_eta(s) >= (1-s)^(N_n-1) n/1024.

For each e use the event that none of its other N_n-1 coordinates were replaced. Its probability is (1-s)^(N_n-1), independent of the original environment, and on that event the two thresholds agree. Sum the lower bound from C4. This uses independence of the resampling flags, not independence of chosen geodesic edges.

In particular Q_eta(s)>=n/2048 for 0<=s<=1/[2(N_n-1)], since the union bound makes the no-replacement probability at least 1/2. This genuinely proves a positive window, but its scale is n^(-2), while the needed input is near n^(-1/3). Extending this event alone cannot close the gap: its probability tends to zero exponentially in n^(5/3) at the desired noise rate. The reduction therefore supplies only Var(T_n)>=K(eta,eta)n/[4096(N_n-1)], a weak finite-volume bound. It does not improve known lattice fluctuation results.

## Saved lemma C8: bound the first-order floor by independent overlap

Let p_e=P(e in gamma)=E a_e. Let gamma' be the geodesic in a wholly independent environment with the same endpoint pair. Then

    L_n <= (1/4) sum_e p_e^2 = (1/4) E|gamma intersect gamma'|.

Proof. The single-coordinate conditional mean g_e(u)=E[T_n | U_e=u] is nondecreasing by C2, and its range has length g_e(1)-g_e(0)=E a_e=p_e. A random variable Z in [A,B] has Var(Z)<= (B-A)^2/4: expand (Z-A)(B-Z)>=0, average, and bound (E Z-A)(B-E Z) by (B-A)^2/4. Apply this to g_e(U_e) and sum to obtain L_n=sum Var(g_e(U_e))<=sum p_e^2/4. Independence of the two whole environments gives P(e in gamma and gamma')=p_e^2; linearity of expectation gives the overlap identity. No within-geodesic independence is used.

The primary hypothesis check is now complete. Dembin--Elboim--Peled, On the influence of edges in first-passage percolation on Z^d (arXiv:2307.01162v2), equation (1.4) requires a weight law supported on [a,b] with b>a>0, absolutely continuous, with density at least alpha>0 almost everywhere on that interval. Uniform[1,2] satisfies this with a=1, b=2, alpha=1. Corollary 1.3, equation (1.9), at d=2 and beta=2 gives sum p_e^2<=C n^(2/3)(log n)^2 for n>=2. It requires no limit-shape curvature assumption. Therefore this selected model has

    L_n <= C n^(2/3)(log n)^2.

This is an application of a published theorem plus the self-contained range bridge above, not a new exponent theorem. It removes hypothesis 1 from the list of unproved inputs in the conditional route: log^2 n is absorbed by n^epsilon for every fixed epsilon>0. The single remaining hard lemma for this route consists of the centered-covariance upper envelope and the robust lower-persistence window stated as hypotheses 2 and 3. Both remain unproved.

NEXT: w362 audit C4 and the C8 published-theorem bridge, then prove the centered-covariance upper envelope and robust lower persistence near noise rate n^(-1/3).
