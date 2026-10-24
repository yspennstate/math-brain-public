# G0007: continuity proved; derivative questions unresolved

Date: 2026-10-11. Status: author-derived proofs below, checked internally; no independent referee. The full problem is PARTIAL because the derivative assertions remain unproved. No novelty priority is claimed.

## 1. Exact statement and conventions

John Fernley and Emmanuel Jacob, *Percolation of the contact process on the regular tree*, arXiv:2609.09972v1, PDF pp. 2--5. T_d is the infinite d-regular tree, d >= 3. Recovery rate is 1, and each infected neighbor transmits at rate lambda. nu_lambda is the upper invariant measure; 1 denotes infected. Write

  theta_I(lambda) = nu_lambda(o lies in an infinite infected component),
  theta_H(lambda) = nu_lambda(o lies in an infinite healthy component),
  c_I = sup{lambda: theta_I(lambda)=0},
  c_H = inf{lambda: theta_H(lambda)=0}.

The source's Theorems 2.1 and 2.4 give lambda_1 < c_I,c_H < infinity for every d >= 3. Its p. 2 states that the weak survival probability rho(lambda) is continuous on the whole parameter line. The results below use that established continuity as an input, not as a new theorem proved here.

**Main partial result.** For every d >= 3,

  theta_I(c_I)=theta_H(c_H)=0,

and both theta_I and theta_H are continuous at their respective thresholds. Nothing below proves existence or continuity of their derivatives near the thresholds, or nonexistence/discontinuity of the infected derivative.

## 2. Finite-window continuity and the endpoint reduction

Use one graphical construction with rate-one recovery marks and infection marks on each directed edge carrying an extra rate coordinate. Keeping marks with rate coordinate <= lambda couples every infection rate monotonically. In the forward-survival representation in source p. 2, put X_lambda(v)=1 precisely if the contact process starting at v survives forever. The joint spatial law is nu_lambda, by time reversal and duality.

For mu <= lambda, X_mu(v) <= X_lambda(v), and

  P(X_mu(v) != X_lambda(v)) = rho(lambda)-rho(mu).

For any finite F and event E determined by F, a union bound therefore gives

  |nu_lambda(E)-nu_mu(E)| <= |F| |rho(lambda)-rho(mu)|.       (2.1)

Consequently every cylinder probability is continuous. On the compact countable product {0,1}^{V(T_d)}, this implies weak continuity: continuous functions are uniformly approximated by functions of finitely many coordinates.

Let E_n^I and E_n^H be the events that o has a monochromatic path to the sphere of radius n, including the color of o. These are cylinder events and decrease in n. Their intersection is the infinite-component event: an infinite connected locally finite cluster has vertices at every distance, and conversely paths to arbitrarily distant spheres make the cluster infinite. Thus

  theta_a(lambda) = inf_n nu_lambda(E_n^a), a in {I,H}.

An infimum of continuous functions is upper semicontinuous. Explicitly, if lambda_j -> lambda, then for each n,

  limsup_j theta_a(lambda_j) <= nu_lambda(E_n^a),

and take the infimum in n. theta_I is increasing and theta_H decreasing. Upper semicontinuity gives right-continuity of theta_I and left-continuity of theta_H. At either threshold, continuity is equivalent to zero critical infinite-component probability: the function is identically zero strictly on its nonpercolating side, and if its endpoint value is zero upper semicontinuity and nonnegativity give the full limit zero.

This reduction was already recorded in the September 17 research history and is reproved here.

## 3. An invariant-tree weak-limit lemma

All invariance here means invariance under the full automorphism group of T_d. For a site configuration eta, let p=E eta(o), D_o be the occupied degree at o (zero if o unoccupied), C_o its occupied cluster, and

  f(eta) = 1{o occupied}/|C_o|,

with 1/infinity=0. Let k_o be the number of infinite branches of C_o after o is removed, taking k_o=0 when o is unoccupied. Define

  B(mu) = E_mu D_o - 2 E_mu eta(o) + 2 E_mu f.

**Lemma 3.1 (branching-excess identity).** For any invariant site measure mu,

  B(mu) = E_mu[1{o occupied}(k_o-2)_+].                     (3.1)

Proof. We first justify the mass transport principle used here. For every nonnegative measurable equivariant transport m(u,v,eta), an automorphism interchanging o and v exists on the regular tree. Invariance gives E m(o,v)=E m(v,o). Sum over v and apply Tonelli. Expected mass sent equals expected mass received, with infinity permitted.

For adjacent occupied u,v, let n(u,v) be the size of the component on u's side after the edge uv is cut. Send one unit from u to v when n(u,v)>n(v,u), interpreting infinity > finite but not infinity > infinity. Set the diagonal mass at u to D_u minus the number of units sent along edges; all other masses are zero. Total outgoing mass is D_u. Each occupied finite tree has either one centroid vertex (all its incident branches strictly smaller than half its size), or one centroid edge (two equal halves). The received mass is 0 at a centroid vertex, 1 at each endpoint of a centroid edge, and 2 at every other vertex in a finite component. Indeed, away from the centroid there is one larger-side neighbor, giving one incoming unit and diagonal mass one; at a centroid vertex every neighbor is smaller, giving diagonal zero and no incoming units; at an endpoint of a centroid edge the equal-side neighbor gives diagonal one and no incoming units.

At a vertex of an infinite component with k>=2 infinite branches, edges to finite branches carry outgoing units, edges between infinite sides carry none, and diagonal mass is k; there are no incoming units. If k=1, the sole infinite-side neighbor sends one incoming unit, all finite-side neighbors receive outgoing units, and diagonal mass is one. Received mass is therefore max(k,2). Mass transport gives

  E D_o = 2p - 2P(o is a finite centroid vertex)
                 - P(o is a finite centroid-edge endpoint)
                 + E[1{o occupied}(k_o-2)_+].

To average the centroid defect, every vertex in a finite component of size n sends 2/n to the centroid vertex, or 1/n to each of the two centroid-edge endpoints. Its total outgoing mass is 2/n; incoming mass is two at a centroid vertex and one at each centroid-edge endpoint. Hence

  2 E f = 2P(o is a finite centroid vertex)
                   + P(o is a finite centroid-edge endpoint).

Combining proves (3.1). This reproduces and averages Proposition 5.1 and Remark 5.2 of the source; it requires no contact-process dynamics. QED.

**Lemma 3.2 (continuity of B).** B is continuous under weak convergence of invariant site measures.

Proof. D_o and eta(o) are bounded cylinder functions. The nonlocal function f is nonetheless bounded and continuous. More quantitatively, let f_R be the inverse size of the occupied root cluster in the induced ball B_R, or zero if o is unoccupied. This is a cylinder function. If that truncated cluster does not meet the sphere of radius R it equals the full cluster. Otherwise its size is at least R+1, and

  0 <= f_R-f <= 1/(R+1).

Thus f_R converges uniformly to f, which is continuous. All three expectations defining B are therefore weakly continuous. QED.

**Corollary 3.3.** A weak limit mu of invariant site measures having only finite occupied clusters has no occupied cluster with at least three ends, almost surely.

Proof. For each approximating measure (3.1) gives B=0. Lemma 3.2 gives B(mu)=0. Nonnegativity implies P(k_o>=3)=0, and by invariance and countability k_v<=2 for every vertex almost surely. A cluster in a tree having three distinct ends contains a vertex with three infinite branches: take rays for three distinct ends and their connecting subtree; the branching vertex of their three eventual tails lies in the cluster. Thus such a cluster is impossible. QED.

## 4. Finite Poisson insertions preserve null events

**Lemma 4.1.** In a family of independent positive-rate Poisson point processes on a bounded time interval, adjoining finitely many points with a joint Lebesgue density, possibly chosen using the original processes and any independent background, produces a law absolutely continuous with respect to the original joint law. The finite number of insertions and the finite set of coordinates used may depend measurably on the original sample, provided there are only countably many possible coordinate lists.

Proof. Fix a deterministic coordinate list j_1,...,j_m, with rates r_j>0; repeated coordinates are allowed. For any original-law null set N in the full space, the factorial Campbell-Mecke identity states

  E integral 1_N(Pi + sum_i delta_(j_i,t_i)) prod_i r_(j_i) dt_i
   = E[1_N(Pi) Z_(j_1,...,j_m)(Pi)] = 0,

where Z counts ordered tuples of distinct existing points with the specified coordinate list. Background variables remain unchanged in this formula. This identity can be proved without a limiting theorem: conditional on a coordinate's point count n, its times are iid uniform; inserting k labeled points changes n to n+k, and the Poisson factorial identity cancels the factor (n+k)!/n! from choosing ordered distinct points. Apply this for each coordinate and condition on the background. Counts are finite almost surely. The right side vanishes because N is null.

The nonnegative integrand on the left is consequently zero for almost every pair (original sample, time tuple). Multiplying it by any measurable insertion density depending on the original sample still gives zero. Rates are strictly positive, so the same conclusion holds with unweighted Lebesgue time measure. Restricting the original sample to any measurable subset also preserves zero. Finally partition into the countably many choices of finite coordinate list, number of inserted points, and the identity operation. This proves the assertion. Coincident times form a Lebesgue null set and cause no problem. QED.

For one extra uniform point on an interval J of length ell in a rate-one recovery process, the Radon-Nikodym derivative is N(J)/ell. No uniform bound on this derivative is asserted or needed.

## 5. Both one-site surgeries for stationary contact processes

**Lemma 5.1 (healthy insertion).** For any stationary contact-process measure pi on a connected locally finite graph with finite incident rates, resetting a finite set S to healthy has pushforward law absolutely continuous with respect to pi.

Proof. Sample xi_-1 with law pi independently of all Harris marks during (-1,0); the final state xi_0 also has law pi. There are finitely many infection arrows touching S in this interval. Let tau be the last such arrow time, or -1 if there is none. Almost surely tau<0. Insert one recovery at each x in S, at times having a joint Lebesgue density in (tau,0). Lemma 4.1 makes the modified joint law absolutely continuous with respect to the original one. No original infection arrow touches S after tau. Recoveries added after tau therefore cannot affect the state of any vertex outside S, and every vertex of S is healthy at time zero. The modified final state is exactly the original final state reset on S. Taking a measurable pushforward preserves absolute continuity. QED.

**Lemma 5.2 (infected insertion).** Suppose furthermore every graph edge transmits in both directions at a strictly positive rate and pi assigns probability zero to the all-healthy configuration. Resetting any one vertex o to infected has pushforward law absolutely continuous with respect to pi. By composing these maps, the same holds for any finite set.

Proof. Use the same stationary initial-state/future-mark representation. If xi_0(o)=1, do nothing. Otherwise choose a nearest vertex z with xi_0(z)=1, with any deterministic tie-breaking rule. Such a vertex exists at finite distance almost surely. Let z=v_0,v_1,...,v_m=o be a shortest path; m>=1. Every internal vertex v_i, 1<=i<m, is healthy in xi_0, by minimality of the distance. Write K for this finite path.

Let tau be the last original recovery mark at a vertex of K or infection arrow on any directed edge touching K during (-1,0), or -1 if none. Finitely many such marks exist, so tau<0. The original states on K are constant on (tau,0): z is infected and all the others are healthy. Choose 2m-1 ordered times with a joint density in (tau,0). At the first m times insert arrows v_(i-1) -> v_i in that order. At the remaining m-1 times insert a recovery at each internal vertex. Each inserted arrow belongs to a positive-rate Poisson process; each recovery belongs to a rate-one process.

After these operations z and o are infected and every internal vertex is restored to healthy. No original arrow touching K occurs after tau, no original recovery occurs there after tau, and no added arrow leaves K. Hence every outside vertex has exactly its original final state. The modified final configuration is exactly xi_0 with o set to infected.

The chosen path, its length, and its ordered coordinate list take countably many values. Although both path and tau depend on the original marks and initial state, conditional insertion times have a Lebesgue density. Lemma 4.1, including its sample-dependent clause, applies. The modified joint law, and hence the final reset-state law, is absolutely continuous with respect to the original law. Finally, if T_*pi << pi and U_*pi << pi, then U_*T_*pi << U_*pi << pi; thus finitely many single-site resets compose. QED.

The reset-map formulation is the one used below: if mu(N)=0, then mu{eta: reset_S(eta) in N}=0. This is nonuniform insertion tolerance. It is stronger than a full-support assertion but does not supply a uniform conditional-probability bound.

## 6. Thin infinite clusters cannot survive insertion tolerance

**Lemma 6.1.** An invariant site measure mu on T_d, d>=3, which is insertion tolerant on every finite set, assigns zero probability to the all-occupied configuration, and has no occupied clusters with three ends, has no infinite occupied cluster.

Proof. Let N be the number of infinite occupied clusters, possibly infinity. We first exclude 2<=N<infinity, using only invariance. Between two disjoint connected subsets of a tree there is a unique shortest bridge path. Existence follows by minimizing their integer distance. Uniqueness follows because two different bridges, together with the paths within the two connected subsets, would give a cycle. On the event 2<=N<infinity, form the union S of these bridge paths for every pair of infinite clusters. S is a finite nonempty automorphism-equivariant vertex set. Every vertex of the entire tree sends total mass one, divided equally among vertices of S; send no mass off this event. Each vertex of S receives infinite mass. If S is nonempty with positive probability, countability implies some vertex belongs to S with positive probability, and invariance implies the same for o. The expected received mass is then infinite, while sent mass is at most one, contradicting mass transport. Thus this event is null.

Next exclude a unique proper infinite cluster C. Each outside vertex has a unique nearest projection onto C, because C is connected in a tree. Send one unit from each outside vertex to this projection, gating the transport on N=1 and C proper. If x in C has an outside neighbor y, the entire half-tree beyond xy lies outside C: any occupied-cluster path back to C would have to cross y. This half-tree is infinite and every one of its vertices projects to x. Thus x receives infinite mass. A proper nonempty connected cluster has a boundary edge, so the preceding countability/invariance argument again makes expected received mass infinite if this event has positive probability. Sent mass is at most one. Hence N=1 implies the whole tree is occupied, which the hypothesis excludes.

If percolation remains possible, N=infinity has positive probability. The balls B_R(o) exhaust the tree. Therefore for some fixed finite R there is positive probability that B_R intersects at least three distinct infinite occupied clusters. Reset every site in this fixed ball to occupied. Each of those clusters has an infinite tail outside the ball, since removing a finite set from an infinite locally finite connected cluster leaves at least one infinite component. Filling the connected ball joins these tails. They yield three distinct ends: tails from originally distinct occupied clusters cannot be joined outside the ball, since that would make them one original cluster. The resulting occupied component consequently has at least three ends. This resulting configuration lies in a mu-null event by hypothesis. But insertion tolerance says its preimage under resetting B_R also has probability zero, contradicting the positive-probability event just found. All possibilities for positive N are excluded. QED.

**Theorem 6.2 (general weak-limit criterion).** If mu is a weak limit of invariant site measures with only finite occupied clusters, mu is insertion tolerant, and mu(all occupied)=0, then mu has only finite occupied clusters.

Proof. Apply Corollary 3.3 and Lemma 6.1. QED.

## 7. Application to both critical contact-process configurations

We must check the all-occupied exceptions and every hypothesis, rather than assume them.

The forward-survival representation of nu_lambda is an equivariant measurable function of independent Poisson labels on vertices and directed edges (each label may contain an entire time-axis process). This product field is ergodic under tree automorphisms. For completeness: approximate any invariant event A by an event E using finitely many label coordinates with error epsilon. Move those coordinates disjointly by an automorphism g; then E and gE are independent. Since gA=A,

  |P(A)-P(A)^2| <= 4 epsilon.

Let epsilon decrease to zero. Any invariant event has probability zero or one; the same holds for the equivariant factor nu_lambda.

For lambda>lambda_1, the infected marginal q=rho(lambda)>0. At any finite lambda,

  q <= lambda*d/(1+lambda*d) < 1,

because survival from a single infected vertex requires an outgoing infection arrow before its first recovery. Thus neither the all-healthy nor the all-infected configuration has positive nu_lambda probability: each is an invariant event, and probability one would contradict respectively q>0 or q<1.

At c_I and c_H the source gives lambda_1<c_I,c_H<infinity, so these exclusions apply. Lemma 5.2 gives insertion tolerance of infected configurations at c_I. Lemma 5.1 gives insertion tolerance of healthy configurations at c_H (regard healthy vertices as occupied).

Choose lambda_n<c_I increasing to c_I. By the threshold definition and monotonicity, their infected configurations have only finite clusters almost surely. Root nonpercolation implies absence of any infinite cluster by invariance and a countable union over vertices. Section 2 gives weak convergence to the infected configuration at c_I. Theorem 6.2 proves theta_I(c_I)=0.

Choose lambda_n>c_H decreasing to c_H. Their healthy configurations have only finite clusters almost surely, by the analogous threshold definition. Their laws converge weakly to the healthy configuration at c_H. Theorem 6.2 proves theta_H(c_H)=0.

Section 2 now gives continuity at both thresholds. Every argument applies separately for every d>=3, including degrees 3 and 4; no comparison with the strong-survival threshold lambda_2 is used. QED.

## 8. An independent obstruction to the spatial Markov ansatz

This additional result is not needed for Section 7.

Suppose a nontrivial invariant stationary contact-process configuration were a homogeneous tree-indexed Markov chain, meaning that neighbor subtrees are independent conditional on the root spin and use one common two-state transition matrix. Put q=P(root infected), R=q/(1-q), a=P(neighbor infected | root healthy), s=1-a, and t=P(neighbor healthy | root infected). Edge symmetry gives (1-q)a=qt, so t=a/R.

The generator equation for the all-healthy event on a singleton gives R=lambda*d*a. Thus a>0. Also s>0: if a=1, adjacent healthy pairs have probability zero but recovery of either endpoint of an infected-healthy pair creates such a pair at strictly positive rate, contradicting stationarity.

For any connected finite set A of size n, the probability all A is healthy under the Markov ansatz is (1-q)s^(n-1). If x in A has internal degree r_x, the probability x alone is infected within A, divided by that all-healthy probability, is

  R (t/s)^(r_x).

This follows by rooting the finite subtree at x: its r_x incident edges use transition probability t instead of s, and the root density uses q instead of 1-q. Given all A healthy, every boundary neighbor is infected with conditional probability a. There are dn-2(n-1) boundary edges. Stationarity of the all-healthy event therefore gives, with v=t/s,

  sum_(x in A) R v^(r_x) = lambda*a*[dn-2(n-1)].           (8.1)

For a singleton, edge, and three-vertex path respectively this gives

  R=lambda*a*d,
  d*v=d-1,
  d*(2v+v^2)=3d-4.

But the edge equation gives v=(d-1)/d, and substitution in the last left side yields 3d-4+1/d. Since d>0 this is a contradiction. Hence the nontrivial stationary contact-process field is not such a spatial Markov chain. The three-variable algebraic contradiction is isolated in MarkovObstruction.lean; its kernel-check status is recorded separately in CHECKS.md. This does not rule out richer path-history messages or infinite-dimensional cavity descriptions. QED.

## 9. Hostile review and computations

The two delicate steps are the sample-dependent Poisson augmentation (Lemma 4.1), and the final-time-only surgery (Lemma 5.2). The proof explicitly uses a joint density for inserted times, countably many finite path choices, and an interval after *all* original recoveries and incident arrows on the path. Adding deterministic-time marks would not justify absolute continuity. Forgetting the final internal recoveries would change the complement configuration and would not prove the reset-map statement. No uniform positive lower bound is used.

The weak-limit step uses the continuous reciprocal cluster-size observable, with the explicit uniform error <=1/(R+1). It does not assert continuity of infinite-component indicators. The merger uses a fixed deterministic ball on a positive-probability event, rather than selecting a random ball and assuming invariance of that selection. Unique proper and finitely-many-cluster cases are separately excluded. Both global constant configurations are separately checked at the source thresholds.

checks.py verifies the finite centroid transport on all 1,442 labeled trees of sizes 1 through 6, the branching-excess formula on 24 independent site-percolation cases (maximum discrepancy about 2.1e-14), and the Poisson one-point density on 76 count cases. These are sanity checks for identities, not numerical evidence replacing any proof or estimating contact-process critical exponents. Memory is far below 1 GB and runtime is seconds.

## 10. Precise remaining gap: derivatives

Set c=c_H. Since theta_H(lambda)=0 for lambda>=c and theta_H is continuous at c, differentiability at c would require and is equivalent to

  theta_H(c-h)=o(h) as h decreases to zero;

the derivative would then be zero. A continuous first derivative across c additionally requires differentiability on a left neighborhood and theta_H'(lambda)->0 from the left. Merely proving o(h) would not prove that stronger assertion.

Likewise theta_I is zero for lambda<=c_I. If a positive limit theta_I(c_I+h)/h exists, theta_I cannot be differentiable at c_I, since its left derivative is zero. No such positive slope, or other proof of failure of continuous differentiability, is supplied here.

Section 7 is qualitative. It supplies no scale-uniform bound on theta_a at distance h from the threshold, and the Poisson surgery costs depend on the chosen finite path and its available time interval. Replacing this dependence by an unproved uniform bound would be a gap. Neither the independent-percolation recursion nor the source's finite random-regular-graph simulation determines the needed derivatives of this dependent infinite-volume measure.

The remaining obligations are therefore: prove or disprove healthy continuous differentiability at c_H, and prove or disprove infected continuous differentiability at c_I. Both are still open in this attempt. The complete original problem is not marked SOLVED.
## 11. Independent surrogate: both transitions can have a kink

This section is a proved comparison-model calculation, NOT a counterexample for the contact process.

On T_d let independent infected-site density be p(lambda)=max(0,1-1/(lambda*d)) for lambda>0 (and p(0)=0). This is the elementary mean-field density surrogate; its healthy-site density is 1-p(lambda). Both colors are independent site percolation separately. Put b=d-1 and p_c=1/b. If u is descendant survival conditional on a vertex being occupied, independence gives

  u=1-(1-p*u)^b,
  Theta(p)=p*[1-(1-p*u)^d].

For p<=1/b the Binomial(b,p) offspring process dies out: its generating function is convex, lies above the diagonal when its mean is <=1, and has only the extinction fixed point 1 (at equality strict convexity supplies strict inequality away from 1). For p>1/b the unique positive solution u lies in (0,1]. It tends to zero as p decreases to p_c, since any positive limit would solve the critical equation, whose only solution is zero.

Divide the equation by u and expand the finite polynomial:

  0=bp-1-binomial(b,2)*p^2*u+O(u^2).

The derivative with respect to u at (p_c,0) is -binomial(b,2)*p_c^2=-(b-1)/(2b), nonzero. The implicit function theorem gives

  u = [2b^2/(b-1)]*(p-p_c)+O((p-p_c)^2),
  Theta(p) = [2d/(d-2)]*(p-p_c)+O((p-p_c)^2).

The surrogate thresholds and nonzero one-sided slopes are therefore

  c_I^mf=(d-1)/(d*(d-2)),
  c_H^mf=(d-1)/d,
  (Theta_I^mf)'(c_I^mf+)=[2d/(d-2)]/[d*(c_I^mf)^2],
  (Theta_H^mf)'(c_H^mf-)=-[2d/(d-2)]/[d*(c_H^mf)^2].

Both functions are continuous but not differentiable at the respective thresholds, since their derivatives on the zero side are zero. The ratio of the magnitudes of these one-sided slopes is exactly (d-2)^2. Thus even an independent smooth-density surrogate can exhibit a much flatter healthy curve while still having a healthy kink. The formula is a warning against reading continuous differentiability from a finite-resolution figure; it decides neither derivative of nu_lambda.

## 12. Why the qualitative method does not determine derivatives

Even within independent invariant insertion-tolerant tree measures, a smooth choice of the density parameter can yield either a kink or continuous differentiability. On a small neighborhood of c, choose healthy occupied density p_1(lambda)=p_c-(lambda-c) or p_3(lambda)=p_c-(lambda-c)^3. Both are decreasing smooth densities in (0,1). The Section 11 expansion gives Theta_1(lambda)=A(c-lambda)+O((c-lambda)^2) on lambda<c, so it has a kink. For p_3 it gives Theta_3(lambda)=A(c-lambda)^3+O((c-lambda)^6); the analytic supercritical branch has derivative tending to zero and the zero branch on lambda>=c gives a continuously differentiable transition. These are not contact-process laws. They demonstrate that weak continuity and insertion tolerance alone cannot settle the derivative assertions; additional rate-dependent contact-process information is essential.


## Second serious attempt completed, 2026-10-11

Two previously untried approaches were formulated in SECOND_ATTEMPT.md: parameter/noise comparison via Broman--Steif, and the exact all-healthy stationary generator hierarchy. Complete new proofs, hypotheses, limitations, and the audit of the earlier argument are in SECOND_PROOFS.md.

New proved contact-process results: exact all-healthy pair/triple identities, conditional healthy-degree variance and covariance, h>=1/[lambda*d-1/(d-1)], and lambda_p^c(T_d)>d/[2(d-1)] for d>=3. The denominator's positivity follows directly from h[lambda*d-1/(d-1)]>=1. The strict threshold conclusion uses the earlier author proof of critical healthy nonpercolation. Further exact bounds are lambda_p^c(T_4)>2/3+25/553472 and lambda_p^c(T_5)>5/8+16807/84321000. Their complete stationary isolated-site proof is in SECOND_PROOFS.md Section 3.4.

A different-model construction proves that invariant ergodicity, downward FKG, uniform finite energy, weak continuity and even linear independent-noise comparisons do not identify the enhancement threshold of a critical parameter law. This countermodel is NOT a contact-process counterexample. It has a continuous, nondifferentiable onset with finite endpoint susceptibility and positive independent-enhancement threshold. All its claims and the limitation concerning finite-cylinder differentiability are explicit in SECOND_PROOFS.md Section 2.

Remaining gap: for the actual contact-process healthy law, prove theta_H(c-h)=o(h), differentiability on a left neighborhood and derivative limit zero, or disprove one of these. For the infected law, establish a positive critical right slope or another obstruction to continuous differentiability. The hierarchy introduces disconnected correlations and multiple shapes already at four sites and supplies no uniform radius-response bound. No independent-enhancement criticality or sharpness theorem for the actual critical healthy law was proved. Threshold bounds do not settle either derivative assertion. Overall VERDICT remains PARTIAL; the earlier continuity proofs are retained.
