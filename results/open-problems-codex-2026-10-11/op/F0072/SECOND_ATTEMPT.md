# F0072 second attempt — 2026-10-12

Reopened at the user's request. The remaining quantitative gap is a lower bound of order log M uniformly over EVERY site of a wall subbox B_M, including its faces, edges and corners, when the zero boundary is outside a larger B_N. Existing contact estimates control the average, and translated full-wall subdomains control only strict interior sites.

## Two approaches not pursued in the first attempt

1. **Reflection and pinning-hazard comparison.** For a reflected pair of wall subsets A,B meeting at a site o on the reflection plane, compare the contact density at o under A with that under A union B. If the normalized contact ratio for the union were bounded below by a fixed power of the ratio for A, repeated reflections could transfer the known full-wall central bound to a face or corner. Ferromagnetic reflection positivity, GHS-type diminishing influence inequalities, and pinning ratios are possible neighbouring tools. This is an approach, not a proved comparison. The first nontrivial finite lattice graph must be tested before relying on it.

2. **Coarea and exact subset recursion.** The identity |x-y|=the integral of level-crossing indicators decomposes the SOS energy into the edge boundaries of level sets. Within a sign/order sector, successive height gaps have independent exponential integrals with rates equal to cut sizes. Summing over sectors gives exact finite graph partition functions, contact densities, and first moments. This replaces the analytic problem by an explicit positive combinatorial ratio; it could reveal a monotonicity or isoperimetric inequality that controls wall-edge contacts.

I select approach 2 because its reduction can be proved completely, handles the unconstrained exterior without an incorrect sign assumption, and permits exact rational tests of approach 1. The computation is a referee check and a search for a structural inequality, not an extrapolated proof of an asymptotic statement.

## Plan and requested recall

Gap-specific brain queries were launched on: “entropic repulsion hard wall boundary subbox reflection positivity chessboard Velenik”; “absolute value FKG continuous SOS Lammers Lis”; and “convex gradient model conditional fluctuations hard wall Brascamp Lieb duplication”. Results will be saved in gap_recall_1.txt through gap_recall_3.txt. Recall outputs are hints only.

Next: prove the subset recursion with all grounding conventions explicit; obtain an exact wall-edge contact ratio; test a reflected three-site lattice domain and buffered small squares; isolate the needed combinatorial inequality if the asymptotic step remains out of reach.

## Exact finite-graph reduction (proved)

Let V be a finite set of free vertices in a grounded graph. Edges have unit weight; multiple edges to the ground are permitted. Every free component meets the ground. For S subset V let c(S) be the number of edges from S to its complement, including the ground, and put c(empty)=0. For nonempty S, c(S)>0. Define

    z(S) = integral_{[0,infinity)^S} exp(-H_S(x)) dx,

where all vertices outside S, INCLUDING V minus S, are fixed at zero. The original degrees remain fixed when S varies. In particular c(S)=sum_{v in S} deg(v)-2 times the number of edges within S. Let z(empty)=1. Then

    z(S) = (1/c(S)) sum_{v in S} z(S minus {v}).                 (R1)

Proof. Split the positive orthant according to its unique minimum-coordinate vertex v; ties form a measure-zero set. Write x_v=t and x_u=t+y_u for u in S minus {v}, with t,y>=0 and x_v's residual set to zero. Internal differences in S are unchanged. Every edge from S to its pinned complement contributes t plus its residual endpoint value. Hence H_S(x)=c(S)t+H_{S minus {v}}(y). The change of variables has Jacobian 1. Integrating t gives 1/c(S); summing over v proves (R1). Coercivity ensures all integrals are finite, and Tonelli justifies splitting and summation.

Let A subset V be the set of hard-wall sites, and define Z(A)=integral exp(-H(x)) 1_{x_A>=0} dx. Then

    Z(A) = sum_{S subset V, S contains A} z(S) z(V minus S).     (R2)

Proof. Outside a null set, S is the set of vertices with strictly positive height. All other heights are strictly negative. If u in S and v outside S, |x_u-x_v|=|x_u|+|x_v|. Thus each cross-sign edge separates into a ground edge for each of the two sign domains. The energy is H_S(x_S)+H_{V minus S}(-x_{V minus S}); its positive and negative integrals factor. The hard wall simply requires A subset S. This proves (R2); no sign assumption on the originally unconstrained exterior is made.

For i in A define

    n_i(A) = sum_{S subset V minus {i}, S contains A minus {i}}
                  z(S) z((V minus {i}) minus S).

The continuous contact density is exactly

    f_i^A(0) = n_i(A)/Z(A).                                   (R3)

Proof. Fix x_i=0 in the density. All incident edges become ground edges; the cut function for the remaining subsets stays the original c, since i is now a pinned complementary vertex. Apply the sign-sector factorization to the remaining coordinates with wall A minus {i}. Divide by the original Z(A). Continuity of the one-site density at zero from the allowed side follows from the bounded change in H when x_i changes, as in first-attempt Lemma 1.

For i in S let m_i(S)=integral x_i exp(-H_S(x)) dx, and put m_i(S)=0 when i is not in S. The same minimum-coordinate split proves

    m_i(S) = z(S)/c(S) + (1/c(S)) sum_{v in S minus {i}} m_i(S minus {v}).   (R4)

Indeed the contribution of t integrates to sum_v z(S minus {v})/c(S)^2=z(S)/c(S). The residual x_i contributes only when v differs from i, giving the second term. Consequently for every i in A,

    E_A x_i = [sum_{S contains A} m_i(S) z(V minus S)]/Z(A).    (R5)

These are exact formulas, not Gaussian approximations. On a unit-edge finite lattice graph all cuts are positive integers, so all z, m, Z and contact densities are rational numbers. They permit an O(|V| 2^|V|) partition-function computation and an O(|V|^2 2^|V|) computation of all first moments. These computations are only practical on small graphs here.

## A new structural consequence: attractive sign-set weights (proved)

The function z is log-supermodular:

    z(S union T) z(S intersection T) >= z(S) z(T).              (R6)

Proof by increasing one-vertex ratios. If v is not in S, integrating its height t gives

    z(S union {v})/z(S)
       = integral_0^infinity exp(-deg(v)t)
          E_{Q_S^+} exp(2 sum_{u in S adjacent v} min(x_u,t)) dt.

This identity follows from |x_u-t|=x_u+t-2min(x_u,t) for nonnegative values. If S subset T with v outside T, the positive, zero-boundary field on T restricted to S stochastically dominates the one on S: condition on T minus S and apply first-attempt Lemma 2 with nonnegative exterior values. The displayed integrand is an increasing function of each x_u, and extra neighbours of v in T contribute additional nonnegative terms. Therefore the ratio z(S union {v})/z(S) increases with S. Enumerate S minus T, add those vertices in the same order to S intersection T and to T, and multiply these ratio inequalities. The result is z(S)/z(S intersection T)<=z(S union T)/z(T), proving (R6).

For w(S)=z(S)z(V minus S), the same inequality applies to complements, so

    w(S union T) w(S intersection T) >= w(S) w(T).

Thus the exact sign-set distribution, proportional to w(S), satisfies the lattice condition of the finite Boolean FKG theorem. Here “attractive” means precisely this proved inequality. Positive association may be invoked from the standard finite FKG theorem, but no quantitative influence bound or wall-edge repulsion follows from that theorem alone. The hard wall restricts this law to S containing A. Conditional on S, positive and negative height fields are independent full-wall zero-boundary SOS fields on their respective sign domains.

## Exact energy distribution (proved)

For any wall set A, H under its Gibbs law has Gamma(|V|, rate 1) distribution. To prove this without an angular decomposition, put Z_A(beta)=integral exp(-beta H(x))1_{x_A>=0} dx. Homogeneity of H and of the wall cone gives Z_A(beta)=beta^(-|V|)Z_A(1) by x=y/beta. Therefore E_A exp(-s H)=Z_A(1+s)/Z_A(1)=(1+s)^(-|V|) for s>=0, the Laplace transform of that gamma density. Uniqueness of the Laplace transform gives the distribution; differentiation, justified by coercivity, gives E H=|V| and Var(H)=|V|. This verifies a global energy budget but does not prevent its concentration near the wall boundary, so it does not fill the pointwise gap.

## Hostile test: the proposed reflected pinning inequality is false

Take the three free lattice sites (-1,0),(0,0),(1,0) in Z^2; fix EVERY other lattice height at zero. Write the centre as x and the leaves as y,z. The genuine nearest-neighbour Hamiltonian is

    H(x,y,z)=2|x|+3|y|+3|z|+|x-y|+|x-z|.

The coefficients 2 and 3 count actual lattice edges to the zero exterior; they are not invented onsite potentials. Define C={centre}, A={centre,left}, B={centre,right}, U=A union B. Reflection in the vertical centre line exchanges A and B and fixes the grounded graph. The tempting transfer inequality was

    f_centre^U(0)/f_centre^C(0)
        >= [f_centre^A(0)/f_centre^C(0)]^2.                   (FALSE)

For x>=0 integrate a leaf. Splitting its integral at 0 and x gives

    F_free(x)=integral_R exp(-3|y|-|x-y|)dy
             =(3/4)exp(-x)-(1/4)exp(-3x),
    F_positive(x)=integral_0^infinity exp(-3y-|x-y|)dy
                 =(1/2)exp(-x)-(1/4)exp(-3x).

For example, the positive integral on [0,x] is exp(-x)(1-exp(-2x))/2, and on [x,infinity) it is exp(-3x)/4; the negative integral adds exp(-x)/4. Multiplying by exp(-2x) from the two central exterior edges and integrating x>=0 gives

    Z(C)=11/128, Z(A)=Z(B)=19/384, Z(U)=11/384.

These can also be verified directly by multiplying the two displayed exponential sums and using integral_0^infinity exp(-k x) dx=1/k. At x=0 the two leaf factors are F_free(0)=1/2 and F_positive(0)=1/4. Therefore

    f_centre^C(0)=32/11, f_centre^A(0)=f_centre^B(0)=48/19,
    f_centre^U(0)=24/11.

The normalized half-wall ratio is 33/38 and the union ratio is 3/4. But 3/4 < 1089/1444=(33/38)^2: after multiplying by positive denominators, 3*1444=4332 < 4*1089=4356. Their difference is 3/722. This is an exact counterexample to the displayed AUXILIARY reflection inequality, not to F0072. It does not rule out a different exponent, a volume-dependent prefactor, or a comparison tailored to buffered macroscopic cubes; none is proved here. Mere reflection symmetry and ferromagnetic attractiveness do not prove this particular comparison.

CoareaReflectionCorrect.lean is the corrected cross multiplication to be checked using decide +kernel; the analytical leaf integrations and Gibbs interpretation remain written proofs. The initial hand calculation used an incorrect coefficient in F_positive. The exact recursion assertion caught it before any conclusion was entered in CLAIMS.jsonl. The original ReflectionArithmetic.lean contains arithmetic for the superseded numbers and is NOT verification of this counterexample.

The direction of failure has a general explanation on graphs separated by the reflected root. Suppose the two reflected components are conditionally independent given x_o=t, and C imposes only x_o>=0. Let g be the normalized root density under C, and let q(t) be the positivity probability for one component given that root height. Reflection symmetry gives the same q for the other component. Multiplying g(t) by q(t) or q(t)^2 and renormalizing gives

    f_o^A(0)/f_o^C(0)=q(0)/E_g q,
    f_o^U(0)/f_o^C(0)=q(0)^2/E_g(q^2).

Jensen's inequality E(q^2)>=(E q)^2 gives the REVERSE of the proposed reflection inequality, strictly when q is not constant. The three-site domain is such a separator graph, and q(t)=F_positive(t)/F_free(t) is nonconstant. This explains the failure structurally. It is not an application of GHS to SOS and supplies no asymptotic counterexample to the source problem.

## A precise sign-buffer criterion for closing the original edge gap (proved reduction)

Let Q_A be the partial-wall measure in B_N, and let S be its positive sign set. Its law is exactly w(S)/Z(A) on S containing A, by (R2). Fix i in A and r>=1 for which D=i+B_{2r} lies in the ambient free box. On the event D subset S, condition on S. The positive height field has full-wall zero-boundary law on S. Condition further on its positive heights outside D; these are nonnegative, or pinned zero. First-attempt Lemma 2 compares the field in D with its zero-boundary full-wall law. First-attempt Proposition 3 then gives, for every h>=0,

    Q_A(phi_i<=h)
       <= Q_A(D not subset S) + (exp(2d h)-1)/(2r+1).          (SB)

This conditioning is legitimate because the negative height field factors off in (R2); it supplies ground edges rather than negative boundary heights to the positive field. Thus (SB) avoids the failed sign assumption of the original translated-domain argument.

If N-M>=delta M for a fixed delta>0, choose r=floor(M^alpha/3) with 0<alpha<1. Then D is in B_N for all i in B_M for sufficiently large M. A sufficient assertion for the desired uniform wall-edge lower bound is

    sup_{i in B_M} Q_{B_M}(i+B_{2r} not subset S) -> 0.        (GAP-SB)

For any a<alpha/(2d), substitution h=a log M in (SB) gives a bound equal to the left side of (GAP-SB) plus O(M^(2da-alpha)), which tends to zero. Combined with the existing upper bound this would establish order-log-M heights at EVERY wall site, including corners. For d=2 with M proportional to N, the existing upper bound is O(log M); for d>=3 it is already uniform in ambient N. Notice that GAP-SB is only a sufficient route, not a claimed necessary condition.

The new assertion is completely explicit in the combinatorial weights:

    Q_A(D subset S)=Z(A union D)/Z(A)
       = [sum_{S contains A union D} z(S)z(V minus S)]
          /[sum_{S contains A} z(S)z(V minus S)].

What has not been proved is that this ratio tends to 1 uniformly over wall-edge and corner i when r is a small power of M. The lattice condition (R6) gives monotonicity under adding constraints, but no rate or such geometric enlargement. The finite counterexample above blocks the simplest attempt to supply that rate by a reflected contact inequality. Isoperimetry of cut(S) alone also does not control the ratio: the positive recursion sums over all deletion orders, and the denominator includes the unconstrained negative domain's z(V minus S).

## Referee audit of the new reduction

* Grounding: c(S) always counts edges to all vertices outside S; its degree terms are NEVER recomputed as induced-graph degrees. Removing a pinned site changes which vertices are integrated, not the original degree count.
* Cross signs: an edge between positive and negative heights contributes the SUM of amplitudes, which is why the independent positive-domain laws have extra zero-boundary edges. Treating the conditional positive domain as the original model with random negative boundary would give the wrong kernel here.
* Coordinate ties and zeros: they have Lebesgue measure zero in partition functions. Contact densities use a separate (|V|-1)-dimensional pinned integral; one cannot infer them by inserting a zero-measure sign event into (R2).
* First moments: the minimum coordinate contributes a nonzero t term EVEN when the minimum vertex is i. This is the z(S)/c(S) term in (R4).
* Sign attractiveness: (R6) proves a Boolean lattice condition; it supplies no quantitative buffer probability. GAP-SB remains a conjectural estimate for the lattice geometry under consideration.
* Reflection counterexample: it is a valid finite Z^2 domain, but it disproves an auxiliary universal inequality only. It is not a counterexample to the macroscopic buffered-cube entropic-repulsion problem.
* Full-wall case N=M: a positive buffer about a wall-edge site would hit pinned zeros and is impossible. That case concerns bulk sites in the source and was already proved. GAP-SB is proposed only for walls with a macroscopic free buffer.
* No limit is inferred from the small exact computations below.

## Temperature check (proved)

For inverse temperature beta>0, positive-domain integrals satisfy z_beta(S)=beta^(-|S|)z_1(S), by height rescaling. Hence z_beta(S)z_beta(V minus S)=beta^(-|V|)w_1(S). The exact sign-set law, including the condition S contains A, is independent of beta. Heights rescale by beta^(-1), and contact densities by beta. Taking beta large therefore does not create a low-temperature parameter for this sign-buffer problem. Importing an integer-SOS low-temperature Peierls estimate on that basis would be unjustified.

## Computational verification completed so far

The corrected coarea_checks.py ran its substantive computation in 8.881 seconds and wrote coarea_checks.json. Its checks used exact fractions throughout, with floating point only for human-readable final values. It verified the three-site leaf integrations and contacts, exhaustively checked (R6) on all 64 subset pairs of that graph, checked contact sums against cut(A), checked equality for full walls, and checked reflection/square symmetry of the buffered model.

On the 3x3 zero-boundary square with reflected half-box walls, and baseline C the common central column, the normalized half-wall contact ratio was 129578024283533199/172861085963391392 = 0.7496078342986651. The union ratio was 15410438048373483/27933278569307944 = 0.5516874079115762, again strictly below the squared half ratio. This gives a second exact failure on an actual square, not just the three-site strip. It remains an auxiliary-inequality counterexample; its wall sets do not have the macroscopic buffer of the target.

On a buffered 4x4 square with a central 2x2 wall, each wall corner had the same contact density, about 0.9500772794308594, and mean about 0.5082231456381662. The exact rational values are in coarea_checks.json. The computation verifies that the formula handles free exterior heights and wall corners correctly; a single small square is not evidence for or against logarithmic asymptotics.

## Further exact probe and why the cut-size bound does not finish the argument

coarea_probe.py asked new questions of the 4x4 buffered model. It completed in 1.279 seconds with sampled peak RSS 34,152,448 bytes; it has a 180-second computation guard and an 800-MiB RSS guard. Conditional on the central 2x2 wall, a specified adjacent exterior site was positive with probability about 0.6619009091, the radius-one 3x3 positive buffer about a specified wall corner occurred with probability about 0.1686325648, and all 16 free vertices were positive with probability about 0.01573631260. Exact fractions are in coarea_probe.json. These finite values are diagnostic only; no asymptotic rate is inferred from them.

The same calculation shows that z(S) is not determined by |S| and c(S). In Z^2 a four-vertex path P and a four-vertex star T both have |S|=4, three internal edges and cut 10, but

    z(P)=19/1920, z(T)=13/1280, z(T)/z(P)=39/38.

Here is a complete hand check using (R1). For one site z=1/4; for an adjacent pair z=1/12 and for an isolated pair z=1/16. A three-site path has cut 8 and partition (2/12+1/16)/8=11/384. An edge plus an isolated site has partition (1/12+2/16)/10=1/48. Three isolated sites have partition 1/64. Removing a path endpoint leaves a three-site path, and removing one of its two interior vertices leaves an edge plus an isolated site, so z(P)=(2*11/384+2*1/48)/10=19/1920. Removing the star centre leaves three isolated sites, and removing a leaf leaves a three-site path, so z(T)=(1/64+3*11/384)/10=13/1280. This matches the exact subset computation. Thus replacing all deletion-order weights by a function of the current volume and perimeter loses real information, even on lattice subsets with the same volume and perimeter.

For completeness, crude bounds do not supply the missing buffer ratio. Since H_S(x)<=4 sum_{v in S} x_v for positive Z^2 heights, z(S)>=4^(-|S|). Conversely choose a spanning tree of the free vertices and their contracted ground, with |S| edges; deleting all other edges lowers H. Over all real heights the selected tree integral is 2^|S|, by using its edge increments as coordinates (triangular Jacobian 1). The positive orthant is a subset of that integration domain, so z(S)<=2^|S|. These bounds leave exponentially wide multiplicative uncertainty.

An isoperimetric refinement from (R1) is still inadequate. For a k-site Z^2 subset, let a,b be its numbers of occupied rows and columns. Then k<=ab and its cut is at least 2a+2b>=4 sqrt(k). Expanding (R1) into its k! deletion orders therefore gives z(S)<=k!/(4^k sqrt(k!))=sqrt(k!)/4^k. Each order visits one subset of each size 1,...,k, justifying the product of square-root factors. This factorial bound is eventually worse than the tree bound and cannot prove Z(A union D)/Z(A)->1. It is a checked dead end, rather than a claimed control of the geometric wall-edge ratio.

Attractiveness alone is also insufficient: in a graph of isolated free vertices each with q edges to ground, z(S)=q^(-|S|) and w(S)=q^(-|V|) is constant. Its sign sets are independent fair bits, even after conditioning A positive. The buffer ratio is exactly 2^(-|D minus A|), not a number tending to 1. This is a counterexample to using only the abstract lattice condition and rescaling identities; the graph is not the cubic-lattice box of F0072, so it is not a counterexample to that problem. The missing estimate must use the lattice geometry and sharper partition comparisons.

## Exact attractive pure-death-process representation (proved)

The coarea recursion has an additional probabilistic interpretation. For each nonempty positive domain S, define

    lambda_v(S)=z(S minus {v})/z(S), v in S.

By (R1), sum_{v in S} lambda_v(S)=c(S). Start a continuous-time pure-death chain from S. Wait an independent Exp(rate=c(S)) time, delete v with probability lambda_v(S)/c(S), and repeat until empty. Assign to vertex v its deletion time T_v. Then (T_v) has EXACTLY the positive zero-boundary SOS height distribution on S.

Proof. Fix an order v_1,...,v_k of deletions, let S_j be the surviving set before the jth deletion, and let tau_j be the consecutive holding times. The joint density of that order and these gaps is

    product_j [c(S_j) exp(-c(S_j)tau_j)
                   z(S_j minus {v_j})/(c(S_j)z(S_j))]
        = z(S)^(-1) exp(-sum_j c(S_j)tau_j),

because the z ratios telescope to z(empty)/z(S)=1/z(S). The map from gaps to ordered deletion times has Jacobian 1. On this ordering sector coarea gives H(T)=sum_j c(S_j)tau_j, so the displayed density is precisely the normalized Gibbs density. Summing over orders proves the representation.

This chain is attractive under inclusion of its initial sets. Indeed (R6)'s increasing one-vertex ratios give lambda_v(T)<=lambda_v(S) whenever S subset T and v in S. For a completely explicit coupling, on any finite ambient graph choose R at least the maximum of all these finitely many rates. Use a common rate-R Poisson clock and a common uniform random variable at each vertex. At its clock, remove v from a configuration K if it is present and the uniform value is at most lambda_v(K)/R. If the larger configuration removes a shared vertex, the smaller one removes it as well; removal of a vertex belonging only to the larger set cannot violate inclusion. Thus inclusion persists at every jump, and deletion times in the larger starting domain stochastically dominate the smaller domain's times. This gives a second proof of positive-domain height monotonicity.

One may take R equal to the maximum original vertex degree. Indeed increasing a single height from 0 to t changes H by at most deg(v)t. Integrating exp(-H) over t>=0 at fixed remaining coordinates therefore gives z(S)>=z(S minus {v})/deg(v). Hence lambda_v(S)<=deg(v). This bounds the proposed Poisson clock construction uniformly over all starting subsets of a fixed finite ambient graph; no explosion or unbounded-clock assumption is hidden in the representation.

The initial killing-rate identity also checks the contact formula directly:

    E_{S drawn from w(. | A subset S)} lambda_i(S)
      = [sum_{S contains A} z(S minus {i})z(V minus S)]/Z(A)
      = n_i(A)/Z(A)=f_i^A(0),

where the middle equality changes the summation variable to S minus {i}. Thus the earlier pinned-integral formula and the death-chain formula agree exactly.

For the PARTIAL wall the starting set S is random with law w(S)/Z(A), S containing A. The exact original quantity becomes

    Q_A(phi_i>h)=E_{S drawn from w(. | A subset S)} P_S(T_i>h), i in A.

Hence an equivalent form of the remaining gap is uniform survival of all wall sites up to time a log M in this chain with that conditioned initial distribution. Its total rate is the geometric cut c(S), but the individual rates lambda_v(S) are NONLOCAL partition ratios. Replacing them with the number of adjacent ground vertices, or treating the chain as standard Eden growth or the contact process, would be incorrect. No theorem about those other particle systems has been assumed to apply. The sign-buffer criterion is one sufficient route to survival, but need not be necessary.

## Current mathematical verdict

PARTIAL. The second attempt proves exact partition/contact/moment recursions, an attractive sign-set lattice condition, an attractive pure-death representation, gamma energy/rescaling identities, the sign-buffer-to-uniform-repulsion implication, and the exponential low-site-count bound below. It refutes a tempting reflected-contact lemma on two finite lattice geometries. It does NOT prove a quantitative buffer estimate or uniform pointwise edge survival estimate for macroscopic partial walls, and does NOT solve the broader interaction class. Existing full-wall and strict-inner-subbox logarithmic bounds remain valid. The precise unresolved quantities are the ratios Z(A union D)/Z(A) approaching 1 (sufficient), or the conditioned death-chain single-site survival probabilities above approaching 1 (equivalent).

## Stronger quantitative partial result: domination of the low-height count

Set q=2d, let A=B_M with side ell=2M+1, and let the ambient zero-boundary box be any B_N with N>=M. Put n=|A|=ell^d, b=c(A)=q ell^(d-1), and r=b/q=ell^(d-1). For h>=0 define

    K_h=number of i in A with phi_i<=h.

Then K_h is stochastically dominated by an immigration/pure-birth process Y_h starting at 0 with rate b+q k in state k. Its distribution is negative binomial with parameters r and p=exp(-q h):

    E exp(theta Y_h)=[p/(1-(1-p)exp(theta))]^r

for (1-p)exp(theta)<1. In particular

    E K_h <= r(exp(q h)-1),
    Q_A(K_h>=m) <= exp(-p m/2+r log 2)                       (COUNT)

for every positive integer m. A right side above 1 is simply a vacuous upper bound. This is a proved count bound, not a pointwise edge bound.

Proof of the rate comparison. Start the exact death chain from the random positive set S_0 drawn under the wall, so A subset S_0. At any later state S, the still-alive wall subset is U=A intersection S, and K=|A minus S|. The rate of a wall death is sum_{v in U} lambda_v(S). Integration by parts over the nonnegative coordinates in U of the positive-domain field Q_S^+ gives

    sum_{v in U} lambda_v(S)
      = E_{Q_S^+} sum_{v in U} partial_v H_S <= c(U).

Indeed lambda_v(S) is its contact density by the pinned-coordinate formula. The derivatives on edges within U cancel; every edge crossing U contributes at most 1, whether its other endpoint is in S or is a pinned ground vertex. All the slice integrals are legitimate by the same coercivity and bounded-derivative argument as first-attempt Lemma 1. Removing one vertex from U can increase c(U) by at most q, since its degree is q and at most q cut edges can be added. After K removals this yields c(U)<=b+qK. Thus the conditional instantaneous wall-death rate is at most b+qK, independently of all outside deaths and of the initial sign configuration.

An explicit Markov coupling avoids any independence assumption about these wall deaths. Couple (S,Y) with Y initially 0. A wall-vertex death S->S minus {v} occurs jointly with Y->Y+1 at rate lambda_v(S). An outside-vertex death changes S only, at its ordinary rate lambda_v(S). In addition, let Y increase alone at rate b+qY-sum_{v in A intersection S}lambda_v(S). Whenever Y>=K this extra rate is nonnegative by the preceding inequality. Every allowed jump preserves Y>=K. The S marginal is the correct death chain, and Y's total birth rate is exactly b+qY. The latter process is nonexplosive: stop it at level L, use its drift bound to get E Y_{h stopped}<=r(exp(qh)-1), and apply P(hit L by h)<=E Y_{h stopped}/L. As L tends to infinity this tends to zero at every finite h. The coupling is therefore well-defined, gives K_h<=Y_h at all finite times, and works for every initial S_0; mixing over the wall-conditioned initial set preserves the stochastic domination.

Proof of the birth law. Since r is a positive integer, Y+r is a Yule process with per-individual birth rate q and r initial ancestors. A single-ancestor Yule process has P(Z_h=k)=p(1-p)^(k-1), k>=1, p=exp(-qh). To verify this directly, differentiate the formula and check the forward equations P'_k=-qk P_k+q(k-1)P_{k-1}, with P_1(0)=1 and all other initial probabilities zero. The geometric probabilities sum to 1, and the nonexplosion argument above ensures the usual finite-level forward solution identifies the process. The r independent ancestral families give Y as a sum of r independent (geometric-minus-one) variables. Summing the geometric series proves the displayed exponential-moment formula and its mean. This use of independence is for the dominating Yule families, not the actual SOS sites or death rates.

For the tail, take theta=p/2. The elementary inequality exp(x)<=1/(1-x) for 0<=x<1 follows by termwise comparison of its positive power series with the geometric series. Hence

    1-(1-p)exp(p/2)
      >= 1-(1-p)/(1-p/2)=p/(2-p)>=p/2.

The moment formula is finite and at most 2^r. Markov's inequality gives (COUNT). For p=1, Y_0=0 and the same upper bound remains valid; no logarithm of 0 is needed.

Consequently, for every fixed eta>0 and 0<a<1/q, h=a log M and M>=2,

    Q_A(K_h>=ceil(eta |A|)) <= exp(-c_{d,eta} M^(d-q a))

for all sufficiently large M, uniformly in ambient N>=M. To check the exponent, p=M^(-qa), |A|=(2M+1)^d and r=(2M+1)^(d-1). The negative term -p eta |A|/2 has order -M^(d-qa), while r log 2 has order M^(d-1). Because qa<1, the former dominates and absorbs the latter into a smaller positive constant c. Thus a positive fraction of anomalously low wall sites has exponentially small probability, improving the previous polynomial Markov bound for that fraction.

This does not close F0072's selected-site quantifier: a fixed face, edge or corner site could belong to a surface-size exceptional set while the fraction of low sites is arbitrarily small. Taking m=1 in (COUNT) gives no useful uniform decay because r is large. The precise pointwise gap therefore remains, despite the new concentration result.

## Final verification and closure

The corrected CoareaReflectionCorrect.lean passed lake env lean (exit 0), using decide +kernel. Checked source SHA-256: 776269b8d0c7e0f469c5261e6390bc24480206edaf84bebab97bd2c0f74362be. This verifies the finite cross multiplication only. ReflectionArithmetic.lean and lean_second_check.json belong to the superseded numerical setup and are not cited as verification of the corrected Gibbs counterexample.

The death-chain uniformization checks passed all nine cases in 0.05244250001851469 seconds. Its three-site root marginal agreed with the independent leaf-integral CDF to maximum error 4.218847493575595e-15. On the 3x3 full-wall square all nine count-tail thresholds were compared with the negative-binomial bound at four levels; all passed. The Poisson truncation bounds are recorded in death_count_checks.json. These checks substantiate the finite implementation; the written coupling and geometric-family proof establish COUNT for all finite volumes.

Final STATE: DONE. VERDICT: PARTIAL. There is new exponential concentration for the fraction of low wall sites, but no proved uniform selected-site lower bound at partial-wall edges or corners. No counterexample to F0072 and no matching published solution is claimed.
