# Second serious attempt — C0159, 2026-10-11–12 (Jerusalem)

The gap from ATTEMPT.md is elimination of right jumps of two-point connectivity at the remaining parameters of general nonunimodular transitive graphs. Summably decreasing modular weights also prevent the heavy-cluster weighted theorem from giving finite contacts. The earlier work already covered scalar descendant recursions on grandparent graphs, arbitrary-radius sprinkling at continuity points, and finite-weight superlevels.

## Two approaches not used in the first attempt

1. **Connection-operator reduction.** Let T_p(u,v)=P_p(u connected to v), as an operator on ordinary counting-measure l2. Instead of scalar tree recursions or tilted mass transport, expand a sprinkled connection into edge-disjoint p-connected segments separated by new edges. The BK inequality may bound this expansion by a geometric operator series. If successful, it would prove right continuity, quantitative bounds, and thus repulsion at every p for which T_p is bounded. A neighbouring literature target is Hutchcroft's L2-boundedness condition and tilted susceptibility on nonunimodular graphs.

2. **Finite-interface partition recursion.** Replace a grandparent vertex by a finite transitive fiber, or take its Cartesian product with a finite connected graph. Descendant cones now have a finite multi-terminal interface. Record their connectivity partitions and derive a finite-dimensional recursion. A uniqueness or continuity theorem for its minimal fixed point would give a stronger graph family than the scalar recursion already proved. The danger is real: concavity of the scalar reliability map does not survive for a general partition distribution; multiple fixed points or discontinuous minimal solutions cannot be dismissed. This route requires a new uniqueness argument, rather than treating the old scalar proof as automatically extensible.

Approach 1 is more promising: it has an explicit operator convergence criterion and makes no unproved uniqueness claim. It is pursued below. Approach 2 is recorded as an unproved future lead.

## A. Quantitative right continuity from a bounded connection operator

Let G be a countable connected graph of maximum degree Delta<infinity. All edges have independent Bernoulli bond states. Write tau_p(u,v)=P_p(u connected to v), including tau_p(u,u)=1. Let A be its adjacency operator on counting-measure l2(V), with ||A||<=Delta, and suppose the nonnegative symmetric connection kernel T_p=(tau_p(u,v)) defines a bounded l2 operator of norm K. In particular K>=1. Fix p<1, q>p and t=(q-p)/(1-p). Suppose t Delta K<1.

Theorem A.1. Under these hypotheses T_q is bounded and

    ||T_q|| <= K/(1-t Delta K),
    0 <= tau_q(u,v)-tau_p(u,v)
       <= t Delta K^2/(1-t Delta K)          for every u,v.

In particular all two-point functions are right-continuous at p, and the full finite-radius cluster-repulsion statement holds almost surely at p by ATTEMPT.md Proposition 5.1. No transitivity or unimodularity is required for this criterion.

Proof. Sample independent edge families X~Bernoulli(p) and Y~Bernoulli(t), and let q-open mean X=1 or Y=1. If u connects to v at q but not at p, there is a finite simple q-open path with at least one X-closed edge. Split this path at its X-closed edges. Suppose they are the n distinct edges {a_i,b_i}, oriented along the path, i=1,...,n. The intervening path segments witness the connections

    u connected at p to a_1;
    b_i connected at p to a_(i+1), 1<=i<n;
    b_n connected at p to v.

These connection events occur disjointly in the BK sense, because the witnessing path segments have disjoint edge sets. Zero-length segments are allowed and use the empty witness; their connection probability is 1. Each of the n separator edges must have Y=1. The Y events are independent because the separator edges are distinct, and they are independent of the X disjoint-occurrence event. The requirement X=0 on separator edges can be dropped for an upper bound. The BK inequality for increasing events of independent bond percolation therefore bounds the probability for this ordered separator list by

    t^n tau_p(u,a_1) [product_{i=1}^{n-1} tau_p(b_i,a_(i+1))] tau_p(b_n,v).

BK here also holds for connection events in the infinite graph: truncate them to finite boxes, where ordinary finite-product BK applies, and increase the boxes. Any finite collection of finite witnesses lies in one box, so disjoint occurrence is recovered by that increasing union. Iteration of the two-event inequality gives the displayed multi-event bound.

Take the countable union over n and ordered lists of distinct separator edges. Enlarging the sum to all ordered adjacent vertex pairs, even lists with repeated edges, is legitimate: the probability estimate was used only on the original distinct lists, and the added summands are nonnegative. This distinction matters: t^n is not claimed to be the probability of repeated Y edges. The resulting bound is

    tau_q(u,v)-tau_p(u,v)
       <= sum_{n>=1} t^n [T_p (A T_p)^n](u,v).       (A.1)

All matrix-product entries in this expression agree with nonnegative multiple sums. For finitely many bounded nonnegative operators this follows by inserting finite-coordinate projections between them and taking their increasing limit. Those projections converge strongly to the identity; hence the finite-coordinate matrix products converge to the bounded-operator matrix entry. Thus there is no unproved interchange with a conditionally convergent series.

For each n, the operator norm of T_p(A T_p)^n is at most K(Delta K)^n. Its individual nonnegative entry is bounded by the same norm (test on unit coordinate vectors). Since t Delta K<1, the operator series

    S = sum_{n>=0} t^n T_p(A T_p)^n

converges in norm and has norm <=K/(1-t Delta K). Its entries are the corresponding nonnegative scalar series. Equation (A.1) gives the second asserted bound by summing the n>=1 geometric series. Together with the n=0 term it also gives entrywise 0<=T_q<=S.

This entrywise domination does imply boundedness on l2, even for signed inputs. For finitely supported f,g,

    |sum_{u,v} f(u) tau_q(u,v) g(v)|
       <= <|f|, S |g|>
       <= ||S|| ||f||_2 ||g||_2.

For finitely supported g, T_q g initially has well-defined coordinates. Applying this inequality to every finitely supported test f, or equivalently to its restriction on every finite vertex set, bounds ||T_q g||_2 by ||S||||g||_2. Extend from the dense finite-support subspace to a bounded operator. Its norm obeys the asserted bound. Let q decrease to p in the explicit difference bound: t decreases to zero and the right side tends to zero. Proposition 5.1 now applies. This proves Theorem A.1.

Corollary A.2. If

    p_(2->2) = sup{p in [0,1]: T_p is bounded on l2},

then every p<p_(2->2) satisfies finite-radius repulsion. Boundedness is downward closed because 0<=T_p<=T_r for p<=r, using the signed-input argument above. Thus every p below the supremum lies below some bounded parameter and is itself bounded. Theorem A.1 also shows openness to the right: a bounded T_p with p<1 forces boundedness at every q with q-p < (1-p)/(Delta K). Consequently, if p_(2->2)<1, T at that threshold cannot be bounded. This is a scope statement, not a proof that the threshold is a bad parameter for repulsion.

## B. Tilted susceptibility supplies the operator hypothesis

Suppose a closed group Gamma acts transitively on G and w is its positive Haar-stabilizer weight cocycle. Fix o, set h(x)=sqrt(w(x)), and define

    chi_(p,1/2) = sum_y tau_p(o,y) sqrt(w(y)/w(o)).

Lemma B.1. If this tilted susceptibility is finite, then ||T_p||_(2->2)<=chi_(p,1/2).

Proof. Simultaneous Gamma invariance of tau and the weight-ratio cocycle implies

    sum_y tau_p(x,y) h(y)/h(x) = chi_(p,1/2) =: M

for every x. For a finitely supported f, weighted Cauchy–Schwarz gives

    |(T_p f)(x)|^2
       <= [sum_y tau_p(x,y) h(y)/h(x)]
          [sum_y tau_p(x,y) h(x)/h(y) |f(y)|^2].

Sum over x, interchange the nonnegative sums, and use symmetry tau_p(x,y)=tau_p(y,x). The remaining inner sum at y is again M, so ||T_p f||_2^2<=M^2||f||_2^2. The density argument extends T_p and gives the bound. No assertion that h itself belongs to l2 is needed; it is a Schur-test weight, not a test vector. This completes the proof.

Thus every parameter where chi_(p,1/2)<infinity satisfies full finite-radius repulsion. Whether the literature supplies a nontrivial interval above p_c is checked below before claiming such an interval for general nonunimodular graphs.

### Literature-verified interval above criticality

Hutchcroft, arXiv:1711.02590v3, Section 1.3, PDF/printed p.8, defines p_t= sup{p: chi_(p,lambda)<infinity for some lambda} and states p_t=p_c(1/2). Theorem 1.8, PDF/printed p.9, states:

> Let G be a connected, locally finite graph and suppose that Gamma subset Aut(G) is transitive and nonunimodular. Then p_c(G) < p_c(G,Gamma,lambda) <= p_t(G,Gamma) for every lambda in (0,1).

The local PDF was fetched and the statement and definitions were inspected directly, not inferred from a brain card. Taking lambda=1/2 gives p_c<p_t. Monotonicity of the nonnegative tilted susceptibility shows chi_(p,1/2)<infinity for every p<p_t: for such p choose a finite-susceptibility parameter r>p from the definition of the supremum, and compare termwise. Thus Lemma B.1 and Theorem A.1 prove:

Normalization check: in the transitive case the paper's modular function is Delta(u,v)=|Gamma_v u|/|Gamma_u v| (general definition on PDF p.12). For the common stabilizer H=Gamma_u intersect Gamma_v, the numerator and denominator are respectively [Gamma_v:H] and [Gamma_u:H]. The ratio is m(Gamma_v)/m(Gamma_u)=w(v)/w(u), so its half-tilted susceptibility is exactly the quantity used in Lemma B.1; no reciprocal convention is silently assumed.

Corollary B.2. Every connected locally finite nonunimodular transitive graph exhibits full finite-radius Bernoulli bond cluster repulsion at every fixed p<p_t(G,Gamma), and more generally at every p<p_(2->2)(G). The interval (p_c,p_t) is nonempty, so this covers a genuine initial portion of the infinite-cluster regime on every such graph.

This is a reduction to a known theorem, not a new full result in print. The source also states p_t<=p_h and explicitly says both equality and strict inequality are possible. Therefore it is unjustified to replace p_t by p_h or claim that this treats every light-cluster parameter.

### Checking the brain's uniqueness obstruction

The math store returned a draft claim that bounded T_p excludes uniqueness. Here is its independent proof, also consistent with Hutchcroft arXiv:1904.05804v2, p.4.

If G is infinite and transitive and there is almost surely exactly one infinite cluster, then theta=P_p(o belongs to an infinite cluster)>0. Otherwise transitivity and the countable vertex union would make the probability of any infinite cluster zero. The Harris–FKG inequality for the increasing events {u belongs to an infinite cluster} and {v belongs to an infinite cluster} gives joint probability at least theta^2. To justify FKG for these events, use the decreasing approximations by connection to the boundary of a finite ball and pass to the limit in the finite-event inequality. Uniqueness makes that joint event imply u connected to v. Hence tau_p(u,v)>=theta^2 for every u,v. Its column is not in l2, so T_p is unbounded. In particular p_(2->2)<=p_u: if p_(2->2)>p_u, the definition of the infimum p_u supplies a unique-cluster parameter below p_(2->2), contradicting boundedness there. This validates the returned hint without assuming the draft's status proves it.

## C. A decisive limitation of this new criterion

Boundedness of T_p cannot be deduced merely from all clusters being light. Consider the grandparent graph H(b) already treated in ATTEMPT.md, b>=2. Its original (b+1)-regular tree T is a spanning subgraph. The unique original-tree path joining o to x has length d_T(o,x), so

    tau_p^H(o,x) >= p^{d_T(o,x)}.

The tree has (b+1)b^(n-1) vertices at distance n>=1 from o. Hence

    sum_x tau_p^H(o,x)^2
       >= 1 + (b+1) sum_{n>=1} b^(n-1) p^(2n).

For p>=1/sqrt(b) this series diverges, because its terms do not tend to zero. Then T_p^H delta_o is not in l2, so T_p^H is not bounded on l2. But every cluster is light for every p<1 by ATTEMPT.md Proposition 3.2, and repulsion holds for all p by Theorem 6.1. Taking, for example, b=2 and p=3/4 gives a concrete overlap where all clusters are light and the new operator hypothesis fails. Thus this sufficient condition is not necessary, and applying it indiscriminately to the light phase would be a mathematical error.

This obstruction occurs in an actual infinite-cluster nonuniqueness regime, rather than a vacuous regime of only finite clusters. Here is an independent verification. For 1/b<p<1 the descendant original-tree percolation in a fixed cone has positive survival probability delta. Its offspring generating function is f(s)=(1-p+ps)^b. It satisfies f(0)>0, f(1)=1 and f'(1)=bp>1, so for some s<1 close to 1 one has f(s)<s. The intermediate value theorem supplies a fixed point r<1; the extinction iterates f^n(0) are bounded by r, and therefore survival probability is at least 1-r>0.

There are countably infinitely many pairwise disjoint descendant cones with roots at the same height. Explicitly, for each ancestor parent^k(o), take a child branch different from the one leading to o, and descend k-1 additional steps; the resulting roots all have height h(o) and lie in disjoint branches. For each such cone require original-tree survival inside it and closure of its full b+2-edge grandparent boundary. This event has probability delta(1-p)^(b+2)>0. The determining edge sets for the different cones are disjoint: ancestor-step edges cannot join two incomparable descendant cones. Hence these events are independent. The probability that no event occurs in a tail is zero, by the finite-product bound, so infinitely many occur almost surely. Each occurring cone contains an infinite cluster that cannot leave it, producing infinitely many distinct infinite clusters. Thus every p in (1/b,1) has infinitely many infinite grandparent clusters, including the entire interval [1/sqrt(b),1) where the bubble and operator criteria fail.

For the explicit b=2,p=3/4 example, r=1/9 satisfies f(r)=r. Thus delta>=8/9, the four-edge boundary closes with probability 1/256, and the independent successful-cone event has probability at least 1/288. These rational identities were checked separately in gp_survival_check.json.

## D. A quantitative contact-count tail

Retain the hypotheses of Theorem A.1 at p: maximum degree Delta>=1 and bounded ||T_p||=K. The Delta=0 connected graph has only one vertex and no distinct clusters, so its contact count is identically zero. Fix u,v and R>=1, and let Z_R be |A_R(C_p(u),C_p(v))| on the event that the two clusters are distinct, and zero otherwise. This definition permits finite clusters as well as infinite ones. Let B_R=sup_x |B(x,R)|<infinity and L_R=(R+1)B_R. For an integer N>=1 set m=ceil(N/L_R).

Proposition D.1. Whenever m>(2 Delta K)^R,

    P_p(Z_R>=N) <= [2 Delta K^2/(1-exp(-1))] m^(-1/R).

In particular the distinct-cluster contact count has an O(N^(-1/R)) tail, and is finite almost surely. For R=1 this is O(1/N).

Proof. In a fixed configuration with Z_R>=N, choose N distinct contact starts and a length-at-most-R path from each into the other cluster, using fixed enumerations. Greedily retain vertex-disjoint paths. A retained path has at most R+1 vertices; all candidate paths meeting it have their starts in its R-neighborhood, of size at most (R+1)B_R=L_R. Thus one retained path eliminates at most L_R of the original contact starts. To eliminate all N requires at least ceil(N/L_R)=m retained paths. This also works if the entire contact set is infinite, since only N starts are used.

Choose t=m^(-1/R) and q=p+(1-p)t. The hypothesis makes t Delta K<1/2, in particular t<1 and q<1. Conditional on the p-configuration, each selected path becomes q-open with probability at least t^R=1/m, and these events are independent by edge disjointness. Hence the conditional probability that u and v merge at q is at least

    1-(1-1/m)^m >= 1-exp(-1).

The elementary inequality follows from 1-s<=exp(-s) for s in [0,1]. Since the roots were distinct at p, integrating this conditional bound and then applying Theorem A.1 gives

    (1-exp(-1)) P_p(Z_R>=N)
       <= tau_q(u,v)-tau_p(u,v)
       <= t Delta K^2/(1-t Delta K)
       <= 2 Delta K^2 t.

Substitute t=m^(-1/R) to obtain the claim. Since m tends to infinity with N, P(Z_R=infinity)=lim_N P(Z_R>=N)=0. Countable unions over u,v,R recover the repulsion assertion directly, without using an abstract continuity statement. This completes the proof.

The greedy constant is deliberately a crude valid upper bound; no independence among the p-clusters or among different candidate paths is asserted. Only the retained paths use independent fresh Y edges. The proof gives a tail for a *fixed rooted pair*, not a uniform simultaneous bound on the largest contact count among all cluster pairs. It is an actual quantitative consequence of the operator criterion and does not require finiteness of ordinary susceptibility.

The O(1/N) estimate at R=1 does not by itself imply a finite expected contact count. The following direct BK argument supplies that stronger conclusion by a different estimate.

## D2. Stronger refinement: finite bubble diagrams suffice directly

The previous operator work suggests checking its one-column consequence rather than assuming a bounded operator. This yields a sharper criterion and a simpler repulsion proof.

For a fixed vertex u write b_p(u)=sum_x tau_p(u,x)^2. This is the bubble diagram at u, not ordinary susceptibility. Let J_R(x,y)=1{d_G(x,y)<=R}. Its symmetric matrix has row and column sums at most B_R, so ||J_R||_(2->2)<=B_R. To verify the norm bound directly, for finite-support f weighted Cauchy–Schwarz gives

    sum_x |sum_y J_R(x,y)f(y)|^2
       <= B_R sum_x sum_y J_R(x,y)|f(y)|^2
       <= B_R^2 sum_y |f(y)|^2,

and density gives the bounded extension.

Theorem D.2. On a countable bounded-degree graph, if b_p(u),b_p(v)<infinity, the distinct-cluster contact count defined in D satisfies

    E_p Z_R(u,v) <= B_R sqrt(b_p(u)b_p(v)).

Consequently Z_R(u,v) is finite almost surely. If every two-point column is square-summable, the all-finite-radius cluster-repulsion assertion holds at p. If ||T_p||=K is bounded, the stronger estimate E Z_R<=B_R K^2 holds, and P(Z_R>=N)<=B_R K^2/N for every R.

Proof. For any x,y, on the event

    {u connected to x, v connected to y, C_p(u) distinct from C_p(v)},

there are finite open paths from u to x in C_p(u) and from v to y in C_p(v). Their vertex sets, hence their edge sets, are disjoint because the clusters are distinct. Thus this event is contained in the disjoint occurrence of {u connected to x} and {v connected to y}. BK gives its probability at most tau_p(u,x)tau_p(v,y). The assertion also covers zero-length paths, whose empty edge witnesses cause no problem.

Pointwise, each x counted by Z_R has at least one y in the other cluster within radius R. Therefore

    Z_R <= sum_{x,y} J_R(x,y)
                     1{u connected to x, v connected to y, C_p(u) distinct from C_p(v)}.

Tonelli and the preceding BK bound imply

    E Z_R <= sum_{x,y} tau_p(u,x) J_R(x,y) tau_p(v,y).

The two columns are l2 by hypothesis. Apply the J_R operator bound and Cauchy–Schwarz to get B_R sqrt(b_p(u)b_p(v)). The infinite scalar sum equals that inner product: finite nonnegative truncations increase to it, while the bounded J_R operator and convergence of l2 truncations justify the finite limit. A nonnegative extended random variable of finite expectation is finite almost surely. Apply the countable union over u,v,R if all columns satisfy the hypothesis. For bounded T_p, b_p(u)=||T_p delta_u||_2^2<=K^2. Markov's inequality then gives the stated O(1/N) bound. This proves the theorem.

No conditioning on the two clusters was used in BK; cluster distinctness only supplies disjoint witnesses for an event that is then bounded under the unconditional Bernoulli law. Applying an independence assertion to the two random clusters themselves would be wrong. A finite bubble diagram is used explicitly; merely having finite individual connection probabilities or light clusters does not make the displayed sum finite.

For a transitive graph b_p(u) is independent of u; call it b_p. Define p_bubble=sup{p:b_p<infinity}. Monotonicity makes b_p finite for every p<p_bubble, and D.2 also applies at the endpoint if its bubble diagram is finite (no right-openness of this condition is asserted). In particular

    p_c < p_t <= p_(2->2) <= p_bubble <= p_u

for the nonunimodular transitive graphs at issue. The first inequality is the verified Hutchcroft theorem; the next is Lemma B.1; the next follows because bounded T_p has l2 columns; the final one follows from the uniqueness obstruction. This strengthens the new parameter criterion to every p with finite bubble diagram and yields a finite expected contact bound. It still leaves the GP(2), p=3/4 example outside the criterion: its column square sum diverges, even though repulsion is true by the first attempt. No theorem identifying p_bubble with p_u is inferred.

## E. Independent checks performed

operator_checks.py computes exact two-point matrices at p=1/4 and q=1/3 by exhaustive enumeration on K4, C4, and P4 (64,16,8 edge configurations respectively at each parameter). It then independently inverts I-t A T_p over rational numbers and checks every entry of

    0 <= T_q-T_p <= T_p(I-t A T_p)^(-1)-T_p,

as well as the scalar geometric bound and the row-sum norm upper bound. No floating-point tolerance is used. A separate enumeration computes contact-count distributions for every rooted pair, for R=1,2 and N=1,...,4, and verifies 384 inequalities of the form

    P(Z_R>=N)[1-(1-t^R)^ceil(N/L_R)] <= tau_q(u,v)-tau_p(u,v).

All these checks passed. After the direct bubble refinement, the same independently computed contact distributions also verified 96 exact expected-contact/BK-sum/bubble-norm inequalities. The script also checks the repeated-edge warning exactly (t=1/9 differs from t^2=1/81), and computes growing exact l2-column lower bounds for GP(2), p=3/4, whose shell ratio is 9/8. Output is saved in operator_checks_output.json. These finite computations test plausible failure points; they do not replace the written infinite-graph proofs.

NeumannFinite.lean formalizes the finite Neumann remainder identity in an arbitrary ring and its scalar upper bound for real z in [0,1). It uses two specific Mathlib imports, no sorry, and no native_decide. Lean completed with exit code 0 and no diagnostics; the command and its precise scope are recorded in LEAN_CHECK.md. This formalization does not certify the BK, Schur, or percolation arguments.

## Referee checklist and remaining gap

Every connection path used in A.1 is finite and simple. BK is applied to p-open connection witnesses, not to events asserting specified edges closed. Repeated sprinkled edges are excluded before the independent t^n calculation. Their inclusion occurs only after the probability estimate, as extra nonnegative summands. All operator products are justified by strong finite-coordinate approximation, and matrix entrywise order is converted to l2 norm bounds using absolute values. The Schur weight may be unbounded, but each row ratio sum is finite under its hypothesis. No assertion of full percolation repulsion follows at parameters where the connection operator is unbounded. The grandparent example explicitly demonstrates this limitation.

The strongest new criterion is D.2: finite two-point bubble diagram implies repulsion at every finite radius and a finite expected contact bound, hence an O(1/N) tail for each fixed pair. This includes all p<p_(2->2) and therefore all p<p_t on nonunimodular transitive graphs. Combined with the first attempt, any possible failure must be at a nonunique parameter with an infinite bubble diagram, p>=p_bubble, in the countable set of two-point right jumps. At R=1, its infinitely many contacts would also have weights tending to zero (use the finite-weight result for heavy pairs or the light-neighborhood lemma otherwise). These are necessary conditions, not a contradiction. Proving that every nonunique parameter has finite bubble diagram is neither shown nor a viable necessary-condition replacement: the grandparent example refutes that idea. Approach 2 remains an unproved lead. No complete solution or counterexample to arbitrary-transitive C0159 is claimed.
