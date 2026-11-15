# Referee report on PAPER.tex

Overall verdict: **GAP**

I found no counterexample to the main theorem. The cost-time construction handles the dependence of accepted edges correctly, and the return-process argument establishes the required survival continuity under a finite mean, including the zero-survival and critical cases. The numerical checks agree with the stated Erlang tree.

As submitted, two proof details need to be supplied: a sufficient Markov state for the sprinkling absorption argument, and the extension of full-graph local convergence to deterministic budget arrays. Both have short repairs without strengthening the theorem. There is also a false explanatory claim about uniqueness of fixed points and an omitted common-law qualification in the continuous-cost wording. These are distinguished from a false main theorem throughout this report.

All locations are source line numbers in the unchanged PAPER.tex. Verdicts marked GAP solely for unavailable external-source verification are explicitly identified as such; they are not assertions that the cited result is false. No browsing, outside agents, pushes, or writes outside this folder were used.

## Required corrections and their mathematical scope

1. **Sprinkling state, line 169.** Quote: “the set of edges that have arrived after t evolves as a continuous-time Markov chain ... Make absorbing the states in which an edge between A and B has been accepted”. The arrived-edge set is a Markov state, but historical acceptance is not determined by that set. For example, with all three vertices initially active and budgets one, let A={u}, B={v}. After edges uv and uw have arrived, uv was accepted if it arrived first and was rejected if uw arrived first. The unordered arrived set is the same. The same situation can be embedded with spare active slots in larger original components. Use state (arrived-edge set, accepted-cross-edge flag), with the flag updated from the pre-arrival active counts, or retain the ordered arrival history. This is still a finite-state chain. From every transient state on the cover event, at least a²n²/4 active cross pairs have unseen clocks, each with rate 1/n. Summing its forward equations gives exactly the claimed inequality q′≤−a²nq/4. The exponential bound and partition union bound then follow. The accepted edges themselves are never asserted independent.

2. **Deterministic arrays, lines 340 and 369.** Quote: “the local convergence of G_n to Er(P) [Theorem 2.1] gives ...”. The source supplied here proves marked local convergence only at a fixed cutoff, for both random budgets and arrays. It does not explicitly establish the full-graph version for arrays or state an array version of the cited theorem. I cannot check that external theorem's exact scope without its text. A self-contained extension is provided below. No uniform integrability of the array and no convergence of its empirical means is needed.

3. **Fixed-point claim, line 334.** Quote: “rule out any fixed point other than e”. This is WRONG: the function identically equal to one is always a fixed point, and differs from e in the assumed positive-survival regime. The proof actually identifies e_* by proving that it is uniformly bounded below one on K. Replace the sentence by uniqueness among fixed points with that additional bound, or simply state that the argument identifies this particular limiting fixed point. The displayed proof is not invalidated by the sentence.

4. **Cost-law qualification, abstract and lines 40/81.** Quote: “any other law of independent continuous costs”. The distributional invariance requires identically distributed costs with one common continuous CDF, so that one common increasing transformation preserves all comparisons. For K3 with all budgets one, independent C12 uniform on (0,1) and C13,C23 uniform on (2,3) always keep edge 12, unlike the iid model. The precisely specified rate-1/n exponential model is fine. Add “identically distributed” to the broad wording.

## Ordered verdict tables

The following tables cover the named statements, displayed formulas, and proof steps in the order requested. Historical assertions that cannot be authenticated from the provided source are separated from the internal mathematics.

### 1. Introduction and cost time

| Location / statement or proof step | Verdict | Reason |
|---|---|---|
| Abstract, line 33, “independent continuous costs”; line 40 and Remark rem:costs, line 81 | GAP | Rank invariance needs one common continuous law, or a common increasing transformation of all edge costs. Independent, differently distributed costs do not suffice. The actual exponential model in line 40 is unambiguous. For example on K3 with all budgets 1, put C12 uniform on (0,1) and the other costs uniform on (2,3): edge 12 is always kept, unlike the iid model. |
| Line 40, exact finite model | CORRECT | Exponential rate 1/n means mean n; costs have no ties almost surely; min(D_i,n−1) resolves oversized budgets. All costs and budgets are independent. |
| Lines 43–45, definition of rho | CORRECT | Standard survival probability; precise construction checked below. |
| Lines 42, 46, historical/local-limit and upper-bound attributions | GAP | External source contents cannot be verified under the no-browsing rule; internal derivation of the needed local limit is supplied below. Attribution audit deferred to step 8. |
| thm:main, lines 48–54 and its convergence display | GAP | No counterexample found; the proof needs the local repairs described above. Deterministic arrays must have positive integer entries. |
| Line 56, P=delta_1 | CORRECT | Maximum degree one gives a matching, and the local tree has at most one edge, so rho=0. |
| Lines 58–67, proof roadmap and lower-bound display | CORRECT | Subject to the later lemmas, this accurately distinguishes cost-time addition from changing an already assigned cost rank. |
| Lines 71–75, d_i and F_k display | CORRECT | F_k counts vertices in components of size at least k. |
| Line 78, H_n(t), p_n, activity, acceptance rule, monotonicity | CORRECT | Activity uses ALL arrivals, including rejected edges. If an edge has cost s, only costs below s affect its rank. Adding later, more expensive edges cannot evict it. Thus G_n(t)=G_n restricted to costs ≤t is increasing and is a subgraph of G_n. Deleting costs above t cannot create extra edges of cost ≤t. This would fail for arbitrary edge deletion followed by reranking, which is not the construction used here. |
| Line 78, changing one budget | CORRECT | Only that vertex's outgoing preference decisions change; other endpoints' ranks do not depend on acceptances. |
| rem:costs, probability integral transform | CORRECT | For iid costs with one common continuous CDF, PIT gives iid uniforms and the common transformation gives rate-1/n exponentials. CDF flat portions do not create ties almost surely. The omitted common-law qualification is the gap recorded above. |
| Line 85, marked local convergence of H_n(t), exploration bounds and conditional density | CORRECT | Fixed-radius exploration is tight using sum_{j≤r}t^j; collisions cost O(M²/n). Conditional cost density is e^(−x/n)/(np_n). Deterministic marks sampled without replacement converge jointly to iid P under weak empirical convergence; no empirical mean bound is needed at a fixed cutoff. At t=0 take the trivial empty-graph limit separately. |
| Line 87, radius r+1 determines G_n(t) radius r and active labels | CORRECT | All incident edges at an inspected vertex needed for a rank or activity test have cost ≤t and are visible one H-layer further. Ties are a null discontinuity. |
| Lines 87–94, non-root type law mu, Gamma(D), root Gamma(D+1), h and h_t displays | CORRECT | Dth OTHER arrival is Gamma(D), with D−1 iid uniform earlier slots. Parent acceptance is y<x. At the root use the (D+1)st arrival and D earlier slots. Child types are fresh before acceptance, which then biases the types of kept children through h. h_t=min(t,x,z)/x is the correct joint acceptance/cutoff probability. |
| Lines 95–99, rho_t, p_t,k, coupling | CORRECT | Edge cutoff gives an increasing coupled family and rho_t≤rho. Increasing union alone does not prove convergence of survival probabilities; later sections must supply that step. |
| lem:conc-t, lines 103–105 | CORRECT | The proof below gives convergence for fixed t,k, with the deterministic-array assumptions stated. |
| Line 108, at most five changed graph edges per cost resampling | CORRECT | A valid loose upper bound (at most three suffice); cutoff cannot alter other endpoints' ranks. Exact maximum checked in step 7. |
| Line 108, one-edge sensitivity 2(k−1) | CORRECT | Merge/split calculation is right. “The smaller size if exactly one is” means the component of size <k. |
| Lines 108–111, rare change and conditional Efron–Stein display | CORRECT | Both resampled costs >t implies no change. Union bound gives change probability ≤2t/n. Independent edge-cost coordinates and finite bounded F_k justify Efron–Stein, yielding ≤50t(k−1)²n. |
| Lines 112–115, budget sensitivity, second Efron–Stein, total variance display | CORRECT | The conditional expectation g changes by ≤2(k−1)t per budget coordinate, independently of budget size. Independent iid budget coordinates suffice; no second budget moment is required. Constant is 2t²(k−1)²n before division by n². |
| Line 116, expectation and local event | CORRECT | Component size ≥k is determined within radius k−1. Its expectation converges to p_t,k; the variance bound gives the stated probability convergence. |

### 2. Active vertices and covering

| Location / statement or proof step | Verdict | Reason |
|---|---|---|
| Line 121, active labels | CORRECT | Needs the underlying Poisson costs, including rejected ones, rather than the retained tree alone. The preceding marked H-limit supplies them. |
| lem:active, lines 123–125 | CORRECT | Assumes P(D≥2)>0 as in the theorem; if rho_t=0 the implication is vacuous. |
| Line 128, fresh child variables and a_t=P(D≥2)e^(−t)>0 | CORRECT | Reveal candidate type/slots only at its test; the parent slot cost and all prior candidates are independent of these variables. Retained-child types would not have law mu, so this pre-acceptance reveal convention matters. |
| Lines 129–131, integral equal to e^(−t) | CORRECT | Substitute w=z−t and integrate the Gamma(k) density. This is exactly the event of no OTHER Poisson arrivals by t. |
| Line 132, forced acceptance and activity | CORRECT | z>t≥y guarantees acceptance; D≥2 and exactly one incident arrival by t guarantee activity. |
| Line 132, adaptive testing bound (1−a_t)^N and N→infinity | CORRECT | Whether the next test occurs is predictable before its child is revealed. Infinite locally finite tree requires infinitely many tests. The repeated conditional bound proves the assertion without incorrectly conditioning fresh variables on survival. |
| Line 135, coverage definition and C_R,B display in prose | CORRECT | All vertices of the witnessing path, including endpoints, have H-degree ≤B. In that induced graph a radius-R ball has ≤1+B+…+B^R vertices. H-radius R+1 determines coverage and labels. |
| lem:cover, lines 137–142 and probability display | CORRECT | Statement gives one simultaneous event for every union, not a union bound over components. |
| Line 145, choose R,B and then k0 | CORRECT | On an infinite component the root has a finite path to an active vertex; H-degrees on that path are finite. Monotone exhaustion in R,B gives the first probability bound. The tail of finite total progeny gives the second. |
| Line 145, probability <eta*zeta/8 for size≥k and uncovered | CORRECT | Split into infinite and finite components; k≥k0 only improves the finite tail. |
| Line 145, “Both events are determined by a ball of bounded radius” | CORRECT | Read as the events {\|T(t)\|≥k} and {root not covered}, the two events in the conjunction immediately before it. Infinite-size events earlier in the paragraph are not local; the antecedent could be made explicit. |
| Line 145, expected fraction/local convergence and Markov bound | CORRECT | For each fixed k the conjunction is local. Markov at eta*n/2 gives zeta/4+o(1), without needing a concentration inequality. |
| Line 147, deterministic covering count | CORRECT | Covered vertices in U can be assigned only to active vertices in U, since U is a union of components. At most C_R,B assignments per active vertex. |
| Line 150, interpretation | GAP | The intended assertion for an individual component of size merely k is correct, but the unqualified sentence is too broad: a single component of size at least eta*n is itself an admissible union. |

### 3. Sprinkling

| Location / statement or proof step | Verdict | Reason |
|---|---|---|
| prop:lower-t, lines 154–156 | CORRECT | The quantitative argument establishes it, with the minor Markov-state repair recorded below. No independence of kept edges is required. |
| Line 159, parameter order | CORRECT | a is fixed before delta=a/4 and k is chosen after a,delta; log(2)/k<delta*a²/8 is attainable. |
| Line 159, sigma-field F_t and conditional independence | CORRECT | F_t contains all budgets, identities and exact costs of arrivals ≤t, including the information that every other edge exceeds t. Independence of original exponential coordinates implies independent rate-1/n residual clocks conditional on F_t. The G_n(t) components and cover event are F_t-measurable. |
| Lines 161–164, conditional Chernoff display | CORRECT | Conditional number of eligible edges is fixed and ≤n²/2; each window probability ≤delta/n. E[2^N\|F_t]≤exp(delta*n/2), giving the displayed exponent by exponential Markov. |
| Line 165, few arrivals and remaining activity | CORRECT | A window arrival can deactivate at most its two endpoints; each side retains ≥an−2delta*n=an/2 active vertices. |
| Line 167, fixed partition, stopping time and unseen active pairs | CORRECT | Activity only decreases. An edge joining currently active vertices in distinct original components could not have arrived earlier: it would have been accepted then. Before the stopping time there are ≥a²n²/4 unseen active pairs, whose current residual clocks each have rate 1/n. |
| Line 169, “the set of edges that have arrived ... [is a] Markov chain ... Make absorbing the states in which an edge ... has been accepted” | GAP | The unordered arrived-edge set is a Markov state, but whether a cross edge WAS ACCEPTED need not be a function of that set: acceptance depends on arrival order. Augment the finite state by the accepted-cross-edge flag (or retain the ordered arrival history). With this explicit repair the absorption event and generator calculation are valid. This is a local presentation gap, not a counterexample to the proposition. |
| Lines 169–172, absorption rate, differential inequality and exponential display | CORRECT | In the augmented finite-state chain, before absorption ≥a²n²/4 eligible pairs each ring at rate 1/n. Summing the forward equations gives q'≤−(a²n/4)q. No-cross-acceptance plus N≤delta*n is precisely nonabsorption. |
| Line 174, partition count and union bound | CORRECT | Conditional on F_t there are ≤2^(n/k) fixed partitions. Sum the no-cross-and-few-arrivals probabilities; count the exceptional many-arrivals event once. The chosen k leaves a strictly negative exponential rate. |
| Line 176, blocks and deterministic mass argument | CORRECT | Under S≥3eta*n, absence of a block ≥S−eta*n yields a partition with each side ≥eta*n, contradicting the event. This even proves a stronger bound than S−3eta*n; for S<3eta*n the stated bound is trivial. |
| Lines 178–181, concentration and displayed failure bound | CORRECT | Fixed k gives S/n→p_t,k≥rho_t; combine cover failure ≤zeta/4 with the two exponential errors. |
| Line 182, arbitrary zeta and eta=epsilon/4 | CORRECT | Parameters may depend on zeta because the final failure event depends only on eta,t. Its limsup is bounded by every positive zeta/4. |
| Window edges versus old accepted edges, throughout | CORRECT | Window costs exceed t and cannot change ranks of older edges. Activity counts arrivals, not current degree in the kept graph. The proof handles the dependence of kept edges by conditional residual clocks and a rate bound; it never assumes independent acceptance indicators. |

### 4. Compact return process

| Location / statement or proof step | Verdict | Reason |
|---|---|---|
| Lines 189–192, potential and finite-mean display | CORRECT | Integrating the Gamma(m+1) density gives integral m dmu=E[D]−1<infinity. m is a potential bound, not the actual number of retained children. |
| Line 193, reduction to rho>0 | CORRECT | If rho=0, rho_t=0 for all t by domination. Positive survival implies some positive mu-mass of fertile types. |
| Lines 196–200, S_M,K,theta display and compact choice | CORRECT | Finite discrete union of closed positive-threshold intervals is compact. Exhaust it by M increasing, c_- decreasing, c_+ increasing; dominated convergence with integrable m gives theta→0. K excludes sterile types, which contribute zero to theta. |
| lem:outside, lines 202–204 | CORRECT | Bound includes the initial vertex and all first-hit K vertices as terminal vertices. |
| Line 207, outside-potential contraction, induction and sum | CORRECT | h≤1 gives expected outside potential ≤m' theta. Generation-j outside potential ≤m theta^j controls all generation-(j+1) vertices. Sum gives 1+m/(1−theta), so finite expectation implies almost sure finiteness. |
| Line 210, definition and branching property | CORRECT | A K-parent has finitely many slots; apply lem:outside to each outside child. Stop before revealing the future reproduction of K-hits; conditional on their types the descendant families are independent. |
| Lines 213–217, Q_j path integral and interpretation | CORRECT | Each intermediate vertex contributes its potential r_i, with successive acceptance factors h. Integrating nonnegative quantities is justified by Tonelli. |
| Lines 217–220, Q_j≤theta^j and eq:Qbounds | CORRECT | Drop h-factors and integrate products r_i over K-complements. On K, min(x,z)/x≥c_-/c_+, so the stated lower and geometric upper bounds hold. |
| Line 221, endpoint Lipschitz bounds, Q continuity | CORRECT | First-variable derivative bound is ≤1/c_- on the compact interval; the last h-factor is either identically 1 or has slope ≤1/c_-. Integration gives theta^j times the endpoint bound, summable over j. |
| Lines 224–227, alpha, pi and change of measure | CORRECT | On K, 1/alpha=x/m≤c_+. Multiplying by alpha(u) converts mu_K to pi exactly. |
| Lines 228–232, x Q_j symmetric path display and reversal | CORRECT | Product of min factors is invariant under reversal and intermediate measure product is unchanged. Intermediate m=0 terms vanish; no division by zero is needed. Uniform convergence follows from the geometric bound. |
| Lines 233–236, A, Hilbert–Schmidt, self-adjointness and F_min | CORRECT | K has finite pi measure and bounded continuous symmetric F. Thus A is compact self-adjoint on L²(pi). F=m Q r/z≥c_-/c_+² and is bounded above, so it is strictly positivity improving. |
| lem:eigen, lines 238–240 | CORRECT | Existence, continuity and strictly positive uniform bounds follow by the compact self-adjoint spectral theorem, as shown next. |
| Line 243, attained norm eigenvector and absolute-value argument | CORRECT | For nonzero compact self-adjoint A, an eigenvalue attains the operator norm in absolute value. Nonnegative kernel gives <A\|f\|,\|f\|>≥\|<Af,f>\|=\|\|A\|\|. Equality in the Rayleigh bound puts \|f\| in the +lambda eigenspace. Real eigenvectors may be chosen. |
| Line 243, continuous version and everywhere positivity/equation | CORRECT | Bounded continuous kernel on finite-measure compact K maps L² into continuous functions. Uniform F_min gives positive lower bound; full support of pi and continuity promote the L² equation to every point. No Krein–Rutman invocation or unproved irreducibility hypothesis is needed. The spectral theorem itself is not bibliographically cited. |
| lem:return(a), lines 251, 258 | CORRECT | gamma>0 because Gamma thresholds have positive density near zero. Each independent slot is rejected with probability ≥gamma/2; all ≤M slots rejected has probability ≥(gamma/2)^M. |
| lem:return(b), lines 252, 260 | CORRECT | Conditional branching gives extinction next step with probability ≥q0^L on 1≤Z_j≤L. Successive stopping-generation bound rules out infinitely many such visits on survival. Countable intersection over L gives Z_j→infinity. |
| lem:return(c), lines 253, 262 | CORRECT | Eigenfunction-weighted expected population is lambda^j v(s). If lambda≤1, positive v_min bounds E Z_j uniformly; Fatou precludes liminf Z_j=infinity with positive probability, as required by (b). This includes critical lambda=1 without a second moment assumption. |
| cor:lambda, lines 265–270 | CORRECT | Every stopped outside family is finite almost surely, simultaneously over countably many vertices. Infinite full progeny is equivalent to survival of at least one return process reached at the finite initial K-frontier. If all K-types die (lambda≤1), so does the full tree, contradicting rho>0. |

### 5. Survival continuity

| Location / statement or proof step | Verdict | Reason |
|---|---|---|
| prop:bounded, lines 279–281 | CORRECT | Uniform finite cutoff t0 is constructed for all s in K. The positive survival probability need not be uniform for the stated result. |
| Line 284, larger compact L and truncated return process | CORRECT | Stop on K; retain only paths with ≤N intermediate types all in L\K. Reproduction families from distinct K-vertices remain conditionally independent given types. |
| Lines 284–287, error bound epsilon_L,N | CORRECT | Long paths sum to theta^(N+1)/(1−theta). Union over one excluded intermediate vertex gives j theta^(j−1) tau; sum is tau/(1−theta)². The expression at theta=0 is understood through the geometric series (the j=1 term remains tau). |
| Lines 288–291, A_L,N v comparison display | CORRECT | Missing mean kernel ≤m epsilon, mu(K)≤1 and v≤v_max give the error M epsilon v_max. Divide by positive v_min to express the error as a multiple of v. |
| Line 292, choose L,N; self-adjointness, norm>1 and w | CORRECT | First N and L can make both error terms as small as needed. Path reversal preserves each restriction. The direct term Q0 keeps a uniformly positive kernel, so the already proved spectral argument applies and gives a uniformly bounded positive eigenfunction. |
| Line 294, bounded family size N0 and martingale definition | CORRECT | At most M' slots per intermediate/source vertex and depth N+1 give the deterministic bound sum_{j=1}^{N+1}(M')^j, even counting rejected/excluded candidate tests. Stop before exposing descendants of return children. The filtration reveals types but not their future reproduction. |
| Lines 294–299, conditional variance and squared martingale-increment displays | CORRECT | Independent families, each total weight ≤N0*w_max, yield variance ≤Z_j(N0*w_max)². Use Z_j≤X_j/w_min and E X_j=lambda_L,N^j w(s) to obtain the second displayed bound. |
| Line 300, summability, L² convergence and survival | CORRECT | Square-integrable martingale increments are orthogonal and summable since lambda_L,N>1. Their L² limit retains mean w(s)>0; extinction makes the martingale eventually zero. Thus survival has positive probability from every K-type. |
| Line 302, embedding into cost-cutoff tree | CORRECT | Every source along a retained path has threshold ≤c'_+; its edge cost is ≤that threshold. Concatenated paths therefore lie in the t0=c'_+ tree. Infinite return progeny gives infinitely many distinct full-tree vertices. |
| Lines 306–310, monotone extinction coupling, eq:gen and fixed-point limit | CORRECT | Conditional independence of the m slots gives the power m. h_t(1−e_t) increases pointwise and is bounded by 1; dominated (or monotone) convergence in the finite measure mu justifies the integral limit, for each finite m,x. Increasing union alone is not used to infer survival. |
| prop:cont, lines 312–314 | CORRECT | The proof identifies the relevant limiting fixed point rather than assuming fixed-point uniqueness. |
| Lines 317–320, J>0 and uniform gap from one on K | CORRECT | e_*≤e_t0<1 everywhere on K and mu(K)>0, so J>0. h≥c_-/c_+ and m≥1 give e_*≤(1−(c_-/c_+)J)^m≤1−c. |
| Line 321, iteration to first K-frontier and bounded convergence | CORRECT | Stopped outside families are finite almost surely, including the family of finitely many initial slots when s is in K. Thus the residual frontier disappears in finite random depth; products in [0,1] converge and are bounded. |
| Lines 322–325, return fixed-point identity, generation iteration and identification | CORRECT | The uniform bound e_*≤1−c on K makes the generation product tend to 0 on return survival (Z_j→infinity) and to 1 on extinction. Bounded convergence identifies e_* with return extinction, hence full-tree extinction. For outside types use their a.s. finite first-hit frontier and the same identity for e. |
| Lines 327–331, root formula and final exchange of limits | CORRECT | Root has D slots conditional on threshold Gamma(D+1). First apply dominated convergence to mu inside the bracket; then to the joint probability law of finite D and y. Bounds by 1 suffice; no higher moments are required for these exchanges. |
| rho=0 and criticality (lines 193, 262, 275, 338) | CORRECT | If rho=0, 0≤rho_t≤rho makes survival convergence immediate; no supercriticality argument is needed. Critical return norm ≤1 gives extinction by lem:return(c). If rho>0, cor:lambda forces norm>1, enabling the bounded subprocess even arbitrarily close to criticality. |
| Line 334, “rule out any fixed point other than e” | WRONG | The constant function 1 is always a fixed point of eq:gen. In the current rho>0 regime it differs from e. Correct statement: uniqueness among fixed points uniformly bounded below 1 on K (or the identification of this particular e_* using its bound (319)). The proof uses that extra bound and is not invalidated by this overstatement. |

### 6. Assembly, concentration and upper bound

| Location / statement or proof step | Verdict | Reason |
|---|---|---|
| Line 338, lower bound with fixed t then n→infinity | CORRECT | For each u>0 choose finite t from prop:cont and then apply prop:lower-t. No interchange of the n,t limits occurs. If rho=0 the lower bound is automatic. |
| Line 338, upper bound and probability convergence | CORRECT | Apply prop:upper for each u. The deterministic-array local-limit omission in its proof is recorded below. |
| Line 338, probability convergence implies L¹ | CORRECT | For X_n=L1/n in [0,1], E\|X_n−rho\|≤epsilon+P(\|X_n−rho\|>epsilon); take n→infinity, then epsilon→0. |
| Line 340, array assembly and no convergence of empirical means | CORRECT | Fixed-cutoff marked convergence uses only empirical weak convergence; return/continuity concern P alone. Concentration below uses tightness, not an array mean limit. The unproved full-local-limit extension in the upper-bound invocation should be supplied. |
| lem:conc, lines 346–348 | CORRECT | Conditional and budget variance estimates below prove the stated L² convergence. |
| Line 351, four-edge graph sensitivity and 8(k−1) F_k sensitivity | CORRECT | Valid loose bounds; at most three distinct graph edges actually change (the moved edge and at most one boundary alternative at each endpoint). |
| Line 351, change probability ≤2(d_i+d_j)/(n−1) | CORRECT | If moved edge is unpreferred at both endpoints at both costs, no list changes. Each endpoint rank is uniform under iid costs conditional on budgets; union over the four preference events gives the bound. No independence between these four events is assumed. |
| Lines 351–354, Efron–Stein display and summation identity | CORRECT | Independent cost coordinates, bounded F_k, the sensitivity and rare-change bound give 64(k−1)² sum_i d_i. The union-bound probability may exceed 1 but is still a valid upper bound. |
| Line 355, deterministic variance vanishes using weak convergence | CORRECT | Since d_i≤n, split sum d_i/n²≤B/n+#(d_i>B)/n. On positive integers, the bounded tail indicator has convergence under weak empirical laws. First n→infinity, then B→infinity uses only tightness of P. Empirical means can diverge. |
| Line 357, iid conditional variance expectation | CORRECT | sum min(D_i,n−1)≤sum D_i gives the finite-mean bound. |
| Line 357, budget-coordinate sensitivity min(X,n) | CORRECT | Changing D_i changes only its own list, by at most \|D_i−D_i'\| entries after clipping; use the one-edge F_k bound and the absolute range [0,n]. g is bounded, so Efron–Stein applies even without E D². |
| Lines 358–361, total variance display and dominated convergence | CORRECT | Dividing the budget Efron–Stein sum by n² gives E[min(X,n)²]/(2n). min(X,n)²/n≤X, E X<infinity, and it tends pointwise to zero. Both terms vanish. |
| prop:upper, lines 364–366 | CORRECT | Follows from expected local component sizes and lem:conc. |
| Line 369, p_k decreases to rho | CORRECT | Decreasing events {\|Er\|≥k} intersect in {\|Er\|=infinity}. |
| Line 369, full-graph local convergence, random budgets | GAP | This is explicitly attributed to EWT Theorem 2.1; the external theorem's exact hypotheses cannot be checked without its text. The paper's own Section sec:time proves only the fixed-cost version. Internal Poisson/rank exploration supports the claimed full local limit. |
| Line 369, same full-graph local convergence for deterministic arrays | GAP | Quote: “the local convergence of G_n to Er(P) [Theorem 2.1] gives ...”. The source supplied here does not establish that the cited iid-budget theorem covers deterministic triangular arrays. Section sec:time only proves fixed-cutoff local convergence. Supply the short extension to full graphs, or derive the needed expectation limit by a truncation argument. This is a proof omission, not evidence that uniform integrability of array means is necessary. |
| Line 369, concentration, L1≤max(k−1,F_k), choice of k | CORRECT | For fixed k, mean convergence plus lem:conc gives F_k/n→p_k. Then choose k with p_k<rho+u/2 and n large with (k−1)/n<rho+u. |


## Deterministic-array extension: why no empirical-mean hypothesis is missing

Here is a repair of the upper-bound invocation, independently of the cited theorem's possible scope. Fix an integer B, let W_n={i:d_i>B}, and compare the original graph with the graph in which every budget is clipped at B, using the same costs. The low-low kept edges are identical: changing a high vertex's budget changes only preferences at that vertex. Delete W_n and all incident edges from both graphs, leaving isolated placeholders; the resulting graphs agree.

If b is the number of kept low-high edges, deletion changes F_k by at most |W_n|+(k−1)b. Any affected low-only component that had size at least k still contributes after deletion. An affected smaller low-only component has at most k−1 vertices and must touch W_n, so charge it to an incident boundary edge. The removed high vertices contribute at most |W_n|. This bound is also valid for k=1.

For either graph, a low vertex i can prefer at most B neighbors; the uniformity of edge ranks gives

    E[b | d] ≤ B n |W_n|/(n−1).

Consequently the expected difference in F_k/n between the original and clipped graphs has limit superior at most

    2 [1+(k−1)B] P(D>B).

Weak convergence of the array's empirical laws gives |W_n|/n→P(D>B) for each integer B. Finite mean of P gives B P(D>B)→0, so the last bound vanishes as B→infinity. This uses no bound on the array's empirical means.

For fixed B, full local convergence of the clipped graph follows by bounded-budget Poisson exploration. At each inspected vertex expose its first B+1 incident order statistics and the endpoints needed to test reciprocal preference. A fixed retained radius requires only a bounded number of candidate inspections depending on B and that radius. The order statistics are tight; candidate endpoints are asymptotically uniform; collisions vanish. Weak empirical convergence gives the clipped budget marks. The limit is Er(P∧B). In a common Poisson weighted tree, any fixed exploration of Er(P) inspects finitely many vertices with finite budgets almost surely. For all sufficiently large B those inspected budgets are unchanged, so Er(P∧B) converges locally to Er(P). This proves the expected F_k limit by first n→infinity, then B→infinity. Lemma lem:conc completes the upper bound.

The concentration proof itself requires even less for arrays: sum_i d_i/n²≤B/n+#{d_i>B}/n, which vanishes by taking n→infinity and then B→infinity. For example, an array with floor(sqrt(n)) budgets n−2 and all other budgets 3 converges weakly to delta_3 while its empirical mean diverges. Neither that example nor similar sparse large budgets defeats these estimates.

## 7(a). Exhaustive sensitivity checks

These checks are independent code, not the paper's repository code. K4 is used for the preference check, as allowed in the question. Budgets above n−1 are equivalent to n−1, so budgets 1,2,3 exhaust the positive effective budgets on K4.

| k | Maximum change in F_k, all simple graphs on 5 vertices | Claimed bound 2(k−1) | Verdict |
|---|---:|---:|---|
| 1 | 0 | 0 | CORRECT |
| 2 | 2 | 2 | CORRECT |
| 3 | 4 | 4 | CORRECT |
| 4 | 5 | 6 | CORRECT |
| 5 | 5 | 8 | CORRECT |
| 6 | 0 | 10 | CORRECT |


There were 1,024 graphs, 10,240 directed edge toggles, and 61,440 comparisons including k=1,...,6. For k>5 every F_k is zero, so the remaining k are automatic.

| Preference-graph check | Exhaustive coverage | Exact maximum changed kept edges | Paper bound | Verdict |
|---|---|---:|---:|---|
| Full graph | 720 orders, 81 budget arrays, every moved edge and old/new insertion rank; 2,099,520 comparisons | 3 | 4 | CORRECT |
| Fixed-cutoff graph | Same coverage, every cutoff interval and feasible side of cutoff for moved edge; 17,146,080 comparisons | 3 | 5 | CORRECT |

A maximum-three witness, with vertices numbered 0,...,3: budgets (1,1,2,1). Old cost order is 01,02,03,12,13,23; new order is 02,03,12,01,13,23. Only edge 01 moves. The kept set changes from {01} to {02,12}. Full witness details are in sensitivity.json.

There is also a general reason for the improved bound: changing one edge's cost can change, at each endpoint, only that edge and one boundary alternative in the preferred set. Across both endpoints the union consists of at most three edges. A cutoff can additionally change the cost eligibility only of the moved edge, which is already in that union. The paper's weaker bounds are therefore valid for every n, not just for the exhaustive cases.

Command:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 sensitivity.py
```

## 7(b). Graph simulation and Erlang-tree Monte Carlo

Each graph row uses 30 independent replicates and the sample standard error of their mean. Each undirected edge gets one common iid Uniform(0,1) cost, mirrored at its two endpoints; the common transformation to exponential costs preserves its graph exactly. Preferred lists are computed by partial sorting; only mutual preferences are retained. A separate chronological implementation using all arrivals agreed with direct rank lists on 1,000 random K8 checks.

| Budget law | n | Mean L1/n | Standard error | Across-replicate SD |
|---|---:|---:|---:|---:|
| D=2 | 500 | 0.031867 | 0.001376 | 0.007537 |
| D=3 | 500 | 0.887267 | 0.004278 | 0.023433 |
| P(1)=0.6, P(5)=0.4 | 500 | 0.306733 | 0.020276 | 0.111058 |
| D=2 | 2000 | 0.009600 | 0.000293 | 0.001605 |
| D=3 | 2000 | 0.884750 | 0.002088 | 0.011438 |
| P(1)=0.6, P(5)=0.4 | 2000 | 0.300083 | 0.011878 | 0.065059 |


The tree Monte Carlo follows the source literally: root budget D has threshold Gamma(D+1) and D uniform slots; a fresh non-root candidate has D~P, threshold Gamma(D), and D−1 potential slots. Accept a candidate when its threshold exceeds the parent's slot cost. Reproduction families are independent conditional on types. Sterile children can immediately be discarded when testing infinitude.

Each row uses 20,000 independent trees. Stop a tree on extinction, reaching the specified number of fertile vertices in its current frontier, or generation 200. A cap hit is a survival proxy and can occur in a large finite tree; no exact simulation can certify an infinite tree. Every run here died or hit the cap before generation 200, so no unresolved depth-limit cases remained. The cap comparison and separate quadrature check address, but do not rigorously bound, this censoring bias.

| Budget law | Fertile-frontier cap | Cap hits / 20,000 | Alive at depth limit | rho proxy | Binomial SE |
|---|---:|---:|---:|---:|---:|
| D=2 | 64 | 0 | 0 | 0.000000 | — |
| D=3 | 64 | 17698 | 0 | 0.884900 | 0.002257 |
| P(1)=0.6, P(5)=0.4 | 64 | 6410 | 0 | 0.320500 | 0.003300 |
| D=2 | 256 | 0 | 0 | 0.000000 | — |
| D=3 | 256 | 17699 | 0 | 0.884950 | 0.002256 |
| P(1)=0.6, P(5)=0.4 | 256 | 6512 | 0 | 0.325600 | 0.003313 |


With zero cap/depth successes in 20,000 trials, the one-sided 95% upper confidence limit for that event's probability is 1−0.05^(1/20000)=0.0001498. Constant budget 2 also has zero survival analytically: each non-root has at most one child. If its threshold x≥1, rejection has probability at least (1/2)P(Gamma(2)≤1/2)>0. If x<1, with probability P(Gamma(2)∈[1,2])>0 its child is accepted and has threshold at least 1, giving the same rejection chance one step later. This supplies a uniform two-step chance of termination. The root has only two such lines.

For an independent numerical check of the root/child conventions, I solved the generating equation from zero extinction on [0,60], using composite trapezoids. If gamma_d is the Gamma(d) density, set

    f(z) = sum_d P(d) gamma_d(z) (1−e_d(z)),
    b(x) = (1/x) integral_0^x z f(z) dz + integral_x^infinity f(z) dz,
    e_d(x) = (1−b(x))^(d−1),
    rho = 1 − sum_d P(d) integral_0^infinity gamma_(d+1)(x) (1−b(x))^d dx.

Iteration stopped when the maximum fixed-point change was below 1e−12. These quadrature values are cross-checks, not rigorous error-certified enclosures.

| Budget law | rho, grid 0.005 | rho, grid 0.0025 | Absolute grid difference |
|---|---:|---:|---:|
| D=2 | 0.0000000000 | 0.0000000000 | 2.4e-12 |
| D=3 | 0.8855735734 | 0.8855735018 | 7.2e-08 |
| P(1)=0.6, P(5)=0.4 | 0.3232665412 | 0.3232657156 | 8.3e-07 |


Numerical verdict: **CORRECT as a consistency check**. For D=3, graph and tree values agree closely. For the mixture, the n=2000 graph mean 0.30008 is below the quadrature value 0.32327 by about 1.95 graph standard errors. Its 30-replicate range is 0.154 to 0.4005. That difference is reported rather than suppressed; this sample does not establish a mismatch. For D=2, the largest-component fraction decreases from about 0.032 to 0.0096, consistent with zero limit. These experiments neither prove the theorem nor establish rates of convergence.

Commands (run serially):

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 experiment.py graph --reps 30
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 experiment.py tree --trials 20000 --batch 500 --depth 200
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 experiment.py quadrature
```

Default master seed: 4522026; per-law, per-n and per-cap seed offsets are explicit in experiment.py. Raw graph replicates are in graph_trials.csv, tree batches in tree_batches.csv, and numerical summaries in graph_summary.json, tree_summary.json, quadrature_summary.json. Each row or batch was saved immediately, and each completed result was appended to LOG.md.

| Run | Elapsed seconds | Recorded peak RSS |
|---|---:|---:|
| Exhaustive sensitivity | 3.01 | Not separately recorded; small enumeration table |
| Graph simulations | 5.47 | 250,118,144 bytes |
| Tree Monte Carlo | 2.24 | 77,365,248 bytes |
| Quadrature | 0.10 | 31,408,128 bytes |

Each numerical script has a 270-second alarm. Computations ran one at a time with no workers. The scripts attempted to lower priority; the macOS sandbox denied priority changes, so they continued as a single bounded process. The first sensitivity launches failed immediately on this priority-setting restriction; the final code catches the error. No run approached the 1 GB memory limit or the five-minute time limit.

### 8. Attribution and novelty (memory only)

| Location / statement | Verdict | Reason |
|---|---|---|
| Lines 40, 408–409, La–Kabkab constant-budget attribution | GAP | The mutual cheapest-neighbor construction is consistent with my recollection of the bilateral preference model. I cannot verify the precise original model, bibliographic details or priority from memory alone. It must not be conflated with greedy degree-constrained b-matching, which counts accepted edges rather than all rank arrivals. |
| Lines 42, 46, 411–412, EWT account | GAP | The supplied account is consistent with my memory of the Erlang weighted tree/local-limit work. I cannot independently authenticate the exact theorem/corollary/question numbers, all hypotheses, or the quoted open-question status without the cited text. The paper's own type construction passes the independent simulations. |
| Claim of new reverse inequality | GAP | I cannot name with confidence a prior paper proving the stated equality for this exact model and all these budget laws, or a general theorem whose verified hypotheses immediately give it. This is NOT a literature search or a certificate of novelty. Known broad giant-from-local-limit criteria still require an almost-local connectivity/coalescence hypothesis; the present sprinkling proof supplies such work. |
| Sprinkling citations, Section sec:sprinkle | CORRECT | The argument is given directly; no external sprinkling theorem is actually invoked. No sprinkling theorem number is cited. The Markov-state repair remains necessary for the formulation in line 169. |
| Alon–Spencer citation | GAP | There is no Alon–Spencer reference in this source, at point of use or in the bibliography. “AS” means Aldous–Steele. Efron–Stein and Chernoff are named but have no source/theorem numbers (lines 108,112,161,351,357). They are standard and used correctly. |
| van der Hofstad, line 46 and refs vdH/vdHbook | CORRECT | The introductory description is consistent with my recollection. Both citations lack theorem numbers. They are contextual, not a load-bearing invoked theorem in this proof. Exact source content/edition/publication status cannot be checked here. |
| Spectral theorem, line 243 | CORRECT | Standard compact self-adjoint spectral theorem; assumptions are verified internally. No external theorem number is given. |

## Typos and unclear wording noticed

No definite spelling or LaTeX syntax error was found by reading. I did not compile the source. The following wording needs correction or clarification; the first, seventh and tenth items include issues discussed above.

| Location | Wording / issue | Suggested clarification |
|---|---|---|
| Abstract line 33; lines 40,81 | “independent continuous costs” / “any other law” | Say iid costs with a common continuous law. |
| thm:main line 53 | Deterministic array's entry domain is implicit | State positive integer entries, with the given cap; the cap is relevant only for sufficiently large n. |
| Lines 78,85,103,138,155 | “t<infinity” leaves nonnegativity implicit; density 1/t in line 85 excludes t=0 | Specify 0≤t<infinity and handle t=0 as the empty graph. |
| Line 108 | “by the smaller size if exactly one is [at least k]” | Say by the size of the component with fewer than k vertices. The calculation itself is correct. |
| Line 145 | “Both events” has a potentially misleading antecedent after references to infinite components | Name {\|T(t)\|≥k} and {root not covered}; the infinite-size event is not local. |
| Line 150 | “says nothing about ... any single component” | Qualify as a component of size merely k. A component of size ≥eta*n is an admissible union and receives a bound. |
| Line 169 | Arrived-edge set treated as if it determines historical acceptance | Add the acceptance flag or ordered arrival history to the state. |
| Line 176 | Stated S−3eta*n block bound followed by argument for S−eta*n | The argument is valid and stronger for S≥3eta*n; say so explicitly or streamline the constants. |
| Lines 340,369 | Array extension of full local convergence is implicit | Include the bounded-budget extension and tail comparison given above, or state the exact applicable cited result. |
| Line 334 | “any fixed point other than e” | False without the gap-below-one condition; the all-one function is always a fixed point. |
| Line 344 | “no moment beyond the weak convergence of the budgets” | Distinguish empirical array laws from the random budget law; the supplied iid concentration proof does use finite E D, while array concentration uses only tightness. |

## What remains unverified

The exact statements and hypotheses of EWT Theorem 2.1, Corollary 2.2 and Section 4 question 3; the original La–Kabkab model and Dabirian–Subramanian connectivity result; precise bibliographic details; and the absence of a prior proof of the reverse inequality cannot be checked from memory alone. I know no prior result I can confidently identify as settling this exact theorem, including its deterministic-array version. That is not an assertion of novelty. The b-matching comparison must distinguish mutual rank preferences from algorithms that count accepted edges toward capacity.

There is no Alon–Spencer reference in the supplied source: AS denotes Aldous–Steele. Chernoff and Efron–Stein are used correctly but have no source/theorem-number citations. Van der Hofstad is cited for context without a theorem number; its almost-local criterion is not invoked to discharge an unproved hypothesis here. The sprinkling and compact-kernel arguments are supplied directly rather than borrowed through a numbered external theorem.

The external code repository, any published PDF, grant/funding declarations, and claims about prior internal AI audits were not independently inspected. Finite-tree Monte Carlo has censoring bias and sampling uncertainty; the quadrature is not certified. No conclusion about general infinite-mean laws is drawn. No counterexample to the stated finite-mean main theorem was found.

PAPER.tex SHA-256 at audit completion: fe88a75a4f04f91692e5c1cb263562b072e8b53c360847613e57e8c2b04dd73e. PAPER.tex was not edited.

Task: “You are refereeing a mathematical paper that is already public but has had no outside audit.” First explicitly recorded audit clock: 12 November 2026, 04:11:25 +04 (Asia/Tbilisi); the prompt itself supplied no clock timestamp.

Overall verdict: **GAP**
