# G0007: second attempt — complete new arguments

2026-10-11. Verdict: PARTIAL. These are author-derived arguments, not independently refereed. The previous continuity results survive the audit below. The original derivative assertions remain unresolved. The countermodel in Section 2 is deliberately a different measure, not a counterexample to the contact-process question.

## 1. Approaches and the exact gap

The two new approaches, chosen before pursuing them, are recorded in SECOND_ATTEMPT.md:

1. Compare changing the infection parameter with independent thinning/enhancement of the stationary configuration, using Broman--Steif. Try to obtain a linear lower bound near the healthy transition.
2. Use the stationary generator on finite all-healthy sets, rather than a spatial Markov approximation, to derive the healthy-cluster hierarchy and its degree moments.

The first approach leads to a proved obstruction; the second produces exact identities and improved healthy-threshold bounds. Neither settles derivatives.

For clarity, the missing healthy assertion is not merely continuity. With c=lambda_p^c and critical nonpercolation already established, differentiability at c is equivalent to theta_H(c-h)=o(h), and its derivative would be zero. Continuous differentiability additionally requires differentiability on a left neighborhood and convergence of that derivative to zero. On the infected side, a bound theta_I(c_I+h)>=a*h for a>0 would already rule out differentiability at c_I; no such contact-process bound is proved here.

### Audit of the earlier continuity argument

The finite-window coupling and reciprocal-cluster-size continuity arguments were reread in full. In particular, the reciprocal of the truncated root-cluster size differs from the full reciprocal by at most 1/(R+1), uniformly over configurations. The infinite-cluster indicator was never declared continuous.

The surgery argument was checked for its most dangerous quantifier: inserted times have a joint Lebesgue density conditional on the original sample. The Campbell--Mecke null-set identity permits this sample-dependent density and countably many finite coordinate lists. Infection is sent along a finite path after its last original incident mark; all internal vertices are recovered afterward, so only the chosen site's final state changes. The finite-bridge and unique-cluster projection transports, and the use of a fixed deterministic ball to join three clusters, were checked separately. No mathematical error was found in these steps. No uniform insertion constant is asserted for the contact process.

The old Lean process handle is unavailable and no output was captured from it. Thus MarkovObstruction.lean remains NOT kernel-checked in our records. The analytic continuity proof is not a Lean formalization.

## 2. Approach A: a complete countermodel to the noise-criticality inference

Broman and Steif, *Dynamical stability of percolation for some interacting particle systems and epsilon-movability*, Ann. Probab. 34(2) (2006), 539--576, DOI 10.1214/009117905000000602, arXiv:math/0605641, Theorem 1.11, PDF p. 7, proves that for a bounded-degree graph and 0<lambda_1<lambda_2,

    nu_lambda_1 <= (nu_lambda_2)^(-,epsilon)

for some epsilon>0, where the right side independently deletes occupied sites with probability epsilon. Complementing gives

    H_lambda_1 >= (H_lambda_2)^(+,epsilon)

for healthy laws H. This is the actual direction. Taking lambda_2=c and lambda_1=c-h does not prove that independent enhancement of H_c percolates for arbitrarily small epsilon. The following construction shows that even substantially stronger qualitative hypotheses and a linear noise comparison do not imply that missing fact.

### 2.1 Construction on T_3

Put independent Bernoulli bond marks with parameter r=3/4 on every edge of the 3-regular tree. Conditional on the resulting bond clusters, assign to each cluster an independent Uniform[0,1] label V_C. There are countably many clusters; one may enumerate them using a fixed enumeration of vertices. The conditional iid law is independent of that enumeration.

For -1/10<=t<=1/10, set s=t_+=max(t,0), and declare a cluster selected when V_C<=s. Let S_t(v) denote its selected indicator. Independently assign Uniform[0,1] variables U_v to vertices and put

    a(t)=1/10+t/10,  b(t)=3/4+t/10,
    p_t(v)=a(t)+(13/20) S_t(v),
    eta_t(v)=1{U_v<=p_t(v)}.

Write mu_t for this occupied-site law and theta(t) for its root infinite-component probability. This law is NOT stationary for the contact process.

### 2.2 Invariance, mixing, finite energy, association

Invariance follows directly: bond marks are iid, cluster labels are conditionally iid in an enumeration-independent manner, and vertex noise is iid. Every part of the distribution is unchanged by an automorphism of the tree.

Here is a precise mixing argument. For finite sets F,G, their internal bond-cluster partitions are determined by the edge marks in their finite convex hulls. When those hulls are disjoint, those edge marks are independent. A cluster label can be shared between F and G only if a vertex of F and a vertex of G belong to the same bond cluster. For a fixed pair x,y this has probability r^dist(x,y), because a tree has a unique path. Therefore the probability of any shared label is at most

    sum_(x in F,y in G) r^dist(x,y).

Conditional on the bonds, replace any labels shared with F by fresh iid labels for the clusters meeting G. This changes the spins in G only on the shared-label event. The modified G vector has the same marginal law and is independent of the F vector: each vector's cluster partition uses only its own hull edges, and its labels and vertex noise are now independent. The displayed bound thus controls the dependence of all bounded cylinder events on the two sets, up to an inessential factor two. It tends to zero when the sets are moved apart. Approximation of general events by cylinders proves ergodicity under automorphisms.

For finite energy, U_v is independent of the hidden field and of every other vertex's observation. Hence

    mu_t(eta(v)=1 | all other observed spins)
       = E[p_t(v) | all other observed spins].

All p_t(v) lie in [9/100,19/25]. The same uniform bounds therefore hold almost surely for the conditional probability. In particular both insertion and deletion tolerance hold with uniform constants. Infinite all-occupied and all-empty configurations have probability zero, since conditional on the hidden field all vertices have independent occupation probabilities bounded away from both endpoints.

The hidden field S_t has a useful exact finite-dimensional description. For s>0 choose a root of a finite connected subtree. The root has law Bernoulli(s), and a child has conditional probability

    P(S(child)=1 | S(parent)=i)=r*i+(1-r)*s.

Indeed an open bond copies the parent cluster label, whereas a closed bond starts a fresh label. Thus the transition matrix is

    P = [[1-(1-r)s, (1-r)s],
         [(1-r)(1-s), r+(1-r)s]].

Its determinant is r>0; Bernoulli(s) is stationary and reversible. The rooted representation agrees with the cluster-label construction on every finite subtree. It generates all hidden spins as increasing functions of independent uniform innovations, because the child probability increases with the parent spin. Each observation is also an increasing function of the hidden spin and its own independent noise. Harris association of independent variables therefore proves positive association of mu_t. For s=0 this is just iid site percolation.

In fact mu_t is downward FKG, which is also available for upper invariant contact-process measures. To prove this without importing a marginal lattice-condition theorem, condition finitely many observations to zero and include those vertices and the support of the events being tested in one finite connected subtree. The posterior hidden law is the same tree Markov weight multiplied at each conditioned vertex by the positive factor 1-a(t) or 1-b(t). Compute subtree partition functions Z_child(0),Z_child(1) from the leaves upward. Conditional on a parent spin, the posterior child transition is proportional to

    P(parent,child) Z_child(child).

Its determinant has the same positive sign as det(P), since multiplication of columns by positive numbers and normalization of rows preserve that sign. A binary stochastic matrix with nonnegative determinant has increasing child probability in the parent spin. The posterior root has some Bernoulli law, and all descendants can again be generated by monotone independent innovations. Unconditioned observations retain their independent increasing channels. Association follows for the conditioned observed law. This applies to every finite set of zero observations and every pair of cylinder events; approximation extends it to arbitrary increasing events. Thus mu_t is downward FKG.

### 2.3 Monotonicity and quantitative noise comparisons

Use the same bonds, cluster labels and U_v for every t. Selected indicators are increasing, and a(t),b(t) both increase with slope 1/10. This gives monotonicity. For a finite F and t>u, the union bound and the uniform threshold construction give

    P(eta_t|F != eta_u|F) <= |F| (3/4)(t-u),

because the conditional probability gap is (t-u)/10 plus (13/20) times the change in a selected label, whose probability is at most t-u. Weak continuity follows.

More strongly, let epsilon=(t-u)/10. Conditional on the coupled hidden fields, p_t(v)>=p_u(v)+epsilon. Since 0<=p_u,p_t<=1,

    p_t(v)(1-epsilon) >= p_t(v)-epsilon >= p_u(v),
    p_u(v)+epsilon(1-p_u(v)) <= p_u(v)+epsilon <= p_t(v).

The independently thinned mu_t has conditional product probabilities p_t(v)(1-epsilon), and the independently enhanced mu_u has probabilities p_u(v)+epsilon(1-p_u(v)). Coordinatewise product couplings conditional on the hidden fields therefore prove BOTH

    mu_u <= (mu_t)^(-,epsilon),
    (mu_u)^(+,epsilon) <= mu_t.

These are comparisons of the correct independently perturbed laws, not merely a correlated resampling. NoiseComparison.lean isolates the two scalar inequalities; its check status is recorded separately.

### 2.4 Criticality, a linear onset, and finite endpoint susceptibility

For t<=0 no cluster is selected. The occupied law is iid with density a(t)<=1/10<1/2, so theta(t)=0 on T_3.

For t>0 the root's bond cluster is selected with probability t, independently of the bond configuration and vertex noise. Restricted to this cluster, occupied paths have independent bond probability r and occupied-site probability b(t). Conditional on an occupied root, descendant survival u obeys

    u=1-(1-r*b(t)*u)^2,
    Theta_internal=b(t)[1-(1-r*b(t)*u)^3].

This is the usual Binomial(2,r*b(t)) offspring computation; a vertex must be occupied and the edge to it open. At b=3/4, z=r*b=9/16, u=(2z-1)/z^2=32/81 and

    Theta_internal=(3/4)[1-(7/9)^3]=193/486.

Since b(t)>=3/4, monotonicity gives theta(t)>=(193/486)t.

An upper bound is also needed to exclude a hidden jump and to quantify the onset. Let xi_t(v)=1{U_v<=a(t)} be the iid baseline process and C its root cluster, with |C|=0 if the root is closed. Baseline percolation is strictly subcritical, uniformly in this t interval. If the final root has an infinite occupied component, either the root was baseline closed and belongs to a selected cluster, or a path from its finite baseline cluster must leave through a vertex of a selected cluster. Thus a selected vertex lies in

    A={o} union C union its vertex boundary.

On a 3-regular tree, |A|<=1+4|C|. Conditional on bonds and baseline noise, each vertex's cluster is selected with probability t; the labels remain independent of the baseline noise, and a union bound works even if vertices share labels. Therefore

    theta(t) <= t E|A| <= t[1+4 chi(a(t))],
    chi(a)=E|C|=a+3a^2/(1-2a).

For a<=11/100, 1+4chi(a)<=1057/650<2. Consequently

    (193/486)t <= theta(t) <= 2t,  0<t<=1/10.

The threshold is exactly t=0, the transition is continuous, and theta is not differentiable there: its left derivative is zero and its right difference quotients are bounded below by 193/486. No assertion of a right derivative limit is needed.

Yet mu_0 is iid density 1/10. Its susceptibility is 11/80, finite. Independent enhancement with probability epsilon changes its density to 1/10+(9/10)epsilon, so its enhancement threshold is

    epsilon_c=(1/2-1/10)/(9/10)=4/9>0.

This is the promised obstruction. Setting H_lambda=mu_(1-lambda) on a neighborhood of lambda=1 gives a decreasing, invariant, ergodic, downward-FKG, uniformly finite-energy healthy family, with quantitative noise comparisons, whose healthy percolation transition has a kink, even though the endpoint is strictly subcritical for small independent enhancement.

It is NOT a contact-process counterexample. It lacks contact-process stationarity and duality. Its finite cylinder probabilities are generally not differentiable across t=0 because of t_+; this is another limitation if stronger local smoothness is established for the contact process. The construction does show that parameter/noise comparisons and the listed qualitative properties cannot supply the missing identification. For additional perspective its covariance at distance n is exactly

    (13/20)^2 s(1-s) r^n.

Thus exponential spatial mixing by itself is insufficient: on T_3 the sphere size grows like 2^n, and 2r>1. No uniform summability follows.

### 2.5 Conditional reduction that survives

If, for the ACTUAL critical healthy law H_c, one could prove both epsilon(h)>=k*h in the Broman--Steif comparison and

    P_(H_c^(+,epsilon))(o in an infinite component) >= A*epsilon

for all small epsilon, then theta_H(c-h)>=A*k*h. This would disprove differentiability at c, hence disprove continuous differentiability. The proof is just monotonicity in the displayed domination. Neither enhancement criticality at epsilon=0 nor the indicated sharpness estimate has been proved for H_c. The countermodel disproves their inference from the qualitative comparisons, even when a linear noise rate is already given. A general Bernoulli sharpness theorem cannot be applied to dependent H_c without additional hypotheses.

## 3. Approach B: exact contact-process identities and new bounds

Let lambda>lambda_1, q=rho(lambda), h=1-q, and Z(A)=nu_lambda(all vertices of finite A are healthy). Both q,h are positive. For F_A=1{all A healthy}, stationarity gives E L F_A=0. This is legitimate for a cylinder function: its changing rates are bounded by |A|(1+lambda*d), so differentiation of its expectation at time zero is dominated.

A recovery enters the event exactly when x in A is its sole infected vertex, of probability Z(A\{x})-Z(A). An infection arrow leaves it only from a vertex y outside A into an adjacent x in A, of probability Z(A)-Z(A union {y}). Internal infection arrows cannot act when all A is healthy. Hence the exact hierarchy is

    sum_(x in A)[Z(A\{x})-Z(A)]
     =lambda sum_(x in A,y~x,y outside A)[Z(A)-Z(A union {y})].       (3.1)

For a connected A of size n the number of boundary edges is dn-2(n-1). Shape matters in the terms involving one extra vertex or a removed internal vertex.

### 3.1 Pair, triple, and conditional degree variance

Write P2 for the all-healthy edge probability and P3 for the all-healthy three-vertex path probability. Every boundary extension of an edge has the latter shape. Singleton and edge stationarity give

    q=lambda*d*(h-P2),
    2(h-P2)=2lambda(d-1)(P2-P3).

Thus

    P2=h-q/(lambda*d),
    P3=h-q/(lambda*d)-q/[lambda^2*d*(d-1)].                 (3.2)

Let D be the number of healthy neighbors conditioned on a healthy root, with mean m. Summing one-neighbor and ordered two-neighbor indicators gives

    m=d*P2/h,
    E[D(D-1)]=d(d-1)*P3/h.

Substitute (3.2), using q/(lambda*h)=d-m, to obtain

    Var(D)=(d-m)(m-1/lambda).                               (3.3)

For two distinct neighbors y,z the same computation gives

    Cov(1{y healthy},1{z healthy} | o healthy)
      =(d-m)[lambda(d-1)m-d]/[lambda*d^2*(d-1)].             (3.4)

These computations use no spatial Markov assumption. SymPy checked the algebra independently in second_symbolic_checks.json; the generator derivation is the proof.

### 3.2 Downward FKG produces a density and degree bound

Liggett--Steif, *Stochastic domination: the contact process, Ising models and FKG measures*, Ann. Inst. H. Poincare Probab. Statist. 42(2) (2006), 223--243, arXiv:math/0504530, equation (5), PDF p. 7, explicitly recalls downward FKG for the contact process on a general graph, citing van den Berg--Haggstrom--Kahn. Its definition is conditional association after fixing any finite set to zero (Definition 1.1).

Apply it with the root fixed healthy. The two decreasing healthy-neighbor indicators in (3.4) have nonnegative covariance. Since d-m=q/(lambda*h)>0, all denominators are positive, and

    m>=d/[lambda(d-1)],
    h>=1/[lambda*d-1/(d-1)].                               (3.5)

For the second inequality, insert m=d-q/(lambda*h), multiply by the positive quantity lambda*h, and use q=1-h. This gives h[lambda*d-1/(d-1)]>=1 directly. Since h>0, the bracket is positive, so division is legitimate without any external lower bound on lambda_1. This bound improves the simpler h>=1/(lambda*d) obtained from (3.3) and nonnegative variance.

### 3.3 Healthy percolation for lambda<=d/[2(d-1)]

Put L_d=d/[2(d-1)]. For lambda<=lambda_1 all vertices are healthy under the upper invariant measure, using extinction at lambda_1. Suppose lambda>lambda_1 and all healthy clusters were finite. Proposition 5.1 and Remark 5.2 of the source, proved out in ATTEMPT.md Section 3, then give

    m=2-2 E[1/|C_o^H| | o healthy]<2.                     (3.6)

The expectation is strictly positive because its random variable is positive almost surely when the healthy root cluster is finite. Conversely (3.5) gives m>=d/[lambda(d-1)]>=2 for lambda<=L_d. This contradiction proves healthy percolation for all lambda<=L_d, including equality. Root percolation is positive whenever any infinite healthy cluster occurs, by invariance and countability.

The previously established absence of a critical healthy cluster now gives

    lambda_p^c(T_d)>d/[2(d-1)]  for every d>=3.              (3.7)

The strict inequality uses that previous critical result explicitly. Without it the present percolation-at-L_d argument yields the non-strict threshold inequality. For d=3,4,5 the new explicit bounds are respectively 3/4, 2/3, and 5/8. These improve the source's displayed numerical lower bounds at low degree; no priority claim is made.

### 3.4 Explicit positive improvements for d=4,5

For d=4 or 5 write L=L_d and define the following exact rational constants:

    U=L+1/100,
    q0=1-1/[L(d-2)],
    K=q0^d/[2(2d(1+U)+1)],
    delta=L*K/2,  lambda*=L+delta,
    tau=1/[2d(1+U)].

Direct rational arithmetic, recorded in second_threshold_bounds.json, verifies q0>0 and 0<delta<1/100. Source Lemma 4.1 on its rooted subtree, and monotonicity on adding edges to obtain T_d, imply q(lambda*)>=q0. This is the survival lower bound 1-1/[lambda(d-2)], with lambda*>=L.

We need a quantitative probability that a healthy root is isolated. Sample the stationary process at time -tau. Ordinary association gives probability at least q(lambda*)^d>=q0^d that all d neighbors are infected. During (-tau,0), require no neighbor recovery, no infection arrow directed into the root, and at least one root recovery. These future marks are independent of the initial configuration and of one another. Neighbor infections persist; the root is healthy at zero; no restriction on other arrows is needed. Thus, writing p_iso for this final isolated-healthy-root probability,

    p_iso>=q0^d exp[-d(1+lambda*)tau](1-exp[-tau]).

Since lambda*<U, d(1+lambda*)tau<=1/2. The elementary inequalities exp(-x)>=1-x and exp(tau)>=1+tau yield

    p_iso>=q0^d*(1/2)*tau/(1+tau)=K.                       (3.8)

The invariant-tree branching excess for healthy sites is

    B_H/h=m-2+2 E[1/|C_o^H| | o healthy]
         >=m-2+2p_iso/h
         >=2L/lambda*-2+2K.

Here (3.5) and h<=1 were used. With delta=L*K/2 and lambda*=L+delta,

    2L/lambda*-2+2K=2K-L*K/lambda*>=K>0.

Positive branching excess implies an infinite healthy cluster. Combining with critical healthy nonpercolation proves

    lambda_p^c(T_4)>2/3+25/553472,
    lambda_p^c(T_5)>5/8+16807/84321000.                    (3.9)

All constants are exact; the numerical values are approximately 0.66671184 and 0.62519932. These are strict rigorous threshold bounds, not estimates of the actual thresholds and not derivative estimates. The isolated-site argument is a stationary finite-time probability event, not a simulation of finite-volume metastability.

### 3.5 Where the hierarchy stops

Apply (3.1) to a three-vertex path. Let Z02 be the healthy probability for its two endpoints (a disconnected pair at distance two), P4 for a four-vertex path, and S4 for the four-vertex three-leaf star. Endpoint removals leave an edge, center removal leaves the disconnected pair; boundary extensions at endpoints or center give different shapes. Therefore

    2P2+Z02-3P3
      =lambda[(3d-4)P3-2(d-1)P4-(d-2)S4].                 (3.10)

This single identity does not determine the three new correlations. Factoring Z02, identifying P4 with S4, or assigning a Binomial offspring law to the healthy root degree would be unjustified. Differentiating (3.2), if q is differentiable, determines two local derivatives from q and q'; it does not control the infinite cluster derivative. A closed, quantitative large-radius hierarchy or an appropriate response estimate is still needed.

## 4. Checks and exact remaining gap

The new finite/algebraic checks are separate from the proofs:

- second_symbolic_checks.json: both conditional moment/covariance formulas simplify exactly.
- second_countermodel_checks.json: exact rational noise comparisons, reversibility and determinants, internal survival 193/486, endpoint enhancement 4/9, susceptibility 11/80, and upper slope constant 1057/650.
- second_fkg_checks.json: the finite four-vertex hidden-star law sums to one and passes all 256 log-supermodularity pair checks. This is a sanity check; the posterior-tree argument above proves conditional association.
- second_threshold_bounds.json: exact rational constants and positive branching-excess margins for d=4,5.
- NoiseComparison.lean: only the two scalar thinning/enhancement inequalities are formalized, with minimal tactic import, no sorry and no native_decide. The shared checker obtained a slot after 1,516 seconds and began running; unless an exit-zero result is captured, no kernel verification is claimed.

The second attempt does not close either derivative clause. The quantitative noise route needs an ACTUAL contact-process critical-enhancement theorem and a sharpness/slope estimate for that dependent law. The hierarchy route needs uniform control of disconnected and multiple-shape correlations as the radius grows. The new threshold bounds locate the healthy transition more tightly but give no modulus for theta_H(c-h) at that unknown threshold. They cannot be substituted for an exponent or differentiability theorem.

Overall conclusion: retain the proved threshold continuities; add the exact healthy moments, density and threshold bounds, and the proved countermodel to the abstract noise inference; leave both source derivative assertions unresolved. VERDICT: PARTIAL.
