# Referee log

Task: “You are refereeing a mathematical paper that is already public but has had no outside audit.” Received in this run on 12 November 2026 (Asia/Tbilisi; exact prompt clock time unavailable). All locations refer to original PAPER.tex lines. PAPER.tex is read-only throughout. No browsing, agents, pushes, or writes outside this folder. External brain/mesh/checklist commands are not run because they write outside the folder; the current task's narrower rule controls. Verdicts concern the mathematics as written, and distinguish an incorrect sentence from an incorrect main theorem.

## 1. Introduction and cost time

| Location / statement or proof step | Verdict | Reason |
|---|---|---|
| Abstract, line 33, “independent continuous costs”; line 40 and Remark rem:costs, line 81 | GAP | Rank invariance needs one common continuous law, or a common increasing transformation of all edge costs. Independent, differently distributed costs do not suffice. The actual exponential model in line 40 is unambiguous. For example on K3 with all budgets 1, put C12 uniform on (0,1) and the other costs uniform on (2,3): edge 12 is always kept, unlike the iid model. |
| Line 40, exact finite model | CORRECT | Exponential rate 1/n means mean n; costs have no ties almost surely; min(D_i,n−1) resolves oversized budgets. All costs and budgets are independent. |
| Lines 43–45, definition of rho | CORRECT | Standard survival probability; precise construction checked below. |
| Lines 42, 46, historical/local-limit and upper-bound attributions | GAP | External source contents cannot be verified under the no-browsing rule; internal derivation of the needed local limit is supplied below. Attribution audit deferred to step 8. |
| thm:main, lines 48–54 and its convergence display | GAP | Statement is coherent; its mathematical validity is deferred until its proof is audited. Deterministic arrays must implicitly have positive integer entries. |
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

## 2. Active vertices and covering

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
| Line 145, “Both events are determined by a ball of bounded radius” | CORRECT | Read as the events {|T(t)|≥k} and {root not covered}, the two events in the conjunction immediately before it. Infinite-size events earlier in the paragraph are not local; the antecedent could be made explicit. |
| Line 145, expected fraction/local convergence and Markov bound | CORRECT | For each fixed k the conjunction is local. Markov at eta*n/2 gives zeta/4+o(1), without needing a concentration inequality. |
| Line 147, deterministic covering count | CORRECT | Covered vertices in U can be assigned only to active vertices in U, since U is a union of components. At most C_R,B assignments per active vertex. |
| Line 150, interpretation | CORRECT | The lemma supplies a lower bound only for unions of mass at least eta*n. It does not assert one for every large-in-k component. |

## 3. Sprinkling

| Location / statement or proof step | Verdict | Reason |
|---|---|---|
| prop:lower-t, lines 154–156 | CORRECT | The quantitative argument establishes it, with the minor Markov-state repair recorded below. No independence of kept edges is required. |
| Line 159, parameter order | CORRECT | a is fixed before delta=a/4 and k is chosen after a,delta; log(2)/k<delta*a²/8 is attainable. |
| Line 159, sigma-field F_t and conditional independence | CORRECT | F_t contains all budgets, identities and exact costs of arrivals ≤t, including the information that every other edge exceeds t. Independence of original exponential coordinates implies independent rate-1/n residual clocks conditional on F_t. The G_n(t) components and cover event are F_t-measurable. |
| Lines 161–164, conditional Chernoff display | CORRECT | Conditional number of eligible edges is fixed and ≤n²/2; each window probability ≤delta/n. E[2^N|F_t]≤exp(delta*n/2), giving the displayed exponent by exponential Markov. |
| Line 165, few arrivals and remaining activity | CORRECT | A window arrival can deactivate at most its two endpoints; each side retains ≥an−2delta*n=an/2 active vertices. |
| Line 167, fixed partition, stopping time and unseen active pairs | CORRECT | Activity only decreases. An edge joining currently active vertices in distinct original components could not have arrived earlier: it would have been accepted then. Before the stopping time there are ≥a²n²/4 unseen active pairs, whose current residual clocks each have rate 1/n. |
| Line 169, “the set of edges that have arrived ... [is a] Markov chain ... Make absorbing the states in which an edge ... has been accepted” | GAP | The unordered arrived-edge set is a Markov state, but whether a cross edge WAS ACCEPTED need not be a function of that set: acceptance depends on arrival order. Augment the finite state by the accepted-cross-edge flag (or retain the ordered arrival history). With this explicit repair the absorption event and generator calculation are valid. This is a local presentation gap, not a counterexample to the proposition. |
| Lines 169–172, absorption rate, differential inequality and exponential display | CORRECT | In the augmented finite-state chain, before absorption ≥a²n²/4 eligible pairs each ring at rate 1/n. Summing the forward equations gives q'≤−(a²n/4)q. No-cross-acceptance plus N≤delta*n is precisely nonabsorption. |
| Line 174, partition count and union bound | CORRECT | Conditional on F_t there are ≤2^(n/k) fixed partitions. Sum the no-cross-and-few-arrivals probabilities; count the exceptional many-arrivals event once. The chosen k leaves a strictly negative exponential rate. |
| Line 176, blocks and deterministic mass argument | CORRECT | Under S≥3eta*n, absence of a block ≥S−eta*n yields a partition with each side ≥eta*n, contradicting the event. This even proves a stronger bound than S−3eta*n; for S<3eta*n the stated bound is trivial. |
| Lines 178–181, concentration and displayed failure bound | CORRECT | Fixed k gives S/n→p_t,k≥rho_t; combine cover failure ≤zeta/4 with the two exponential errors. |
| Line 182, arbitrary zeta and eta=epsilon/4 | CORRECT | Parameters may depend on zeta because the final failure event depends only on eta,t. Its limsup is bounded by every positive zeta/4. |
| Window edges versus old accepted edges, throughout | CORRECT | Window costs exceed t and cannot change ranks of older edges. Activity counts arrivals, not current degree in the kept graph. The proof handles the dependence of kept edges by conditional residual clocks and a rate bound; it never assumes independent acceptance indicators. |

## 4. Compact return process

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
| Line 243, attained norm eigenvector and absolute-value argument | CORRECT | For nonzero compact self-adjoint A, an eigenvalue attains the operator norm in absolute value. Nonnegative kernel gives <A|f|,|f|>≥|<Af,f>|=||A||. Equality in the Rayleigh bound puts |f| in the +lambda eigenspace. Real eigenvectors may be chosen. |
| Line 243, continuous version and everywhere positivity/equation | CORRECT | Bounded continuous kernel on finite-measure compact K maps L² into continuous functions. Uniform F_min gives positive lower bound; full support of pi and continuity promote the L² equation to every point. No Krein–Rutman invocation or unproved irreducibility hypothesis is needed. The spectral theorem itself is not bibliographically cited. |
| lem:return(a), lines 251, 258 | CORRECT | gamma>0 because Gamma thresholds have positive density near zero. Each independent slot is rejected with probability ≥gamma/2; all ≤M slots rejected has probability ≥(gamma/2)^M. |
| lem:return(b), lines 252, 260 | CORRECT | Conditional branching gives extinction next step with probability ≥q0^L on 1≤Z_j≤L. Successive stopping-generation bound rules out infinitely many such visits on survival. Countable intersection over L gives Z_j→infinity. |
| lem:return(c), lines 253, 262 | CORRECT | Eigenfunction-weighted expected population is lambda^j v(s). If lambda≤1, positive v_min bounds E Z_j uniformly; Fatou precludes liminf Z_j=infinity with positive probability, as required by (b). This includes critical lambda=1 without a second moment assumption. |
| cor:lambda, lines 265–270 | CORRECT | Every stopped outside family is finite almost surely, simultaneously over countably many vertices. Infinite full progeny is equivalent to survival of at least one return process reached at the finite initial K-frontier. If all K-types die (lambda≤1), so does the full tree, contradicting rho>0. |

## 5. Survival continuity

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

## 6. Assembly, concentration and upper bound

| Location / statement or proof step | Verdict | Reason |
|---|---|---|
| Line 338, lower bound with fixed t then n→infinity | CORRECT | For each u>0 choose finite t from prop:cont and then apply prop:lower-t. No interchange of the n,t limits occurs. If rho=0 the lower bound is automatic. |
| Line 338, upper bound and probability convergence | CORRECT | Apply prop:upper for each u. The deterministic-array local-limit omission in its proof is recorded below. |
| Line 338, probability convergence implies L¹ | CORRECT | For X_n=L1/n in [0,1], E|X_n−rho|≤epsilon+P(|X_n−rho|>epsilon); take n→infinity, then epsilon→0. |
| Line 340, array assembly and no convergence of empirical means | CORRECT | Fixed-cutoff marked convergence uses only empirical weak convergence; return/continuity concern P alone. Concentration below uses tightness, not an array mean limit. The unproved full-local-limit extension in the upper-bound invocation should be supplied. |
| lem:conc, lines 346–348 | CORRECT | Conditional and budget variance estimates below prove the stated L² convergence. |
| Line 351, four-edge graph sensitivity and 8(k−1) F_k sensitivity | CORRECT | Valid loose bounds; at most three distinct graph edges actually change (the moved edge and at most one boundary alternative at each endpoint). |
| Line 351, change probability ≤2(d_i+d_j)/(n−1) | CORRECT | If moved edge is unpreferred at both endpoints at both costs, no list changes. Each endpoint rank is uniform under iid costs conditional on budgets; union over the four preference events gives the bound. No independence between these four events is assumed. |
| Lines 351–354, Efron–Stein display and summation identity | CORRECT | Independent cost coordinates, bounded F_k, the sensitivity and rare-change bound give 64(k−1)² sum_i d_i. The union-bound probability may exceed 1 but is still a valid upper bound. |
| Line 355, deterministic variance vanishes using weak convergence | CORRECT | Since d_i≤n, split sum d_i/n²≤B/n+#(d_i>B)/n. On positive integers, the bounded tail indicator has convergence under weak empirical laws. First n→infinity, then B→infinity uses only tightness of P. Empirical means can diverge. |
| Line 357, iid conditional variance expectation | CORRECT | sum min(D_i,n−1)≤sum D_i gives the finite-mean bound. |
| Line 357, budget-coordinate sensitivity min(X,n) | CORRECT | Changing D_i changes only its own list, by at most |D_i−D_i'| entries after clipping; use the one-edge F_k bound and the absolute range [0,n]. g is bounded, so Efron–Stein applies even without E D². |
| Lines 358–361, total variance display and dominated convergence | CORRECT | Dividing the budget Efron–Stein sum by n² gives E[min(X,n)²]/(2n). min(X,n)²/n≤X, E X<infinity, and it tends pointwise to zero. Both terms vanish. |
| prop:upper, lines 364–366 | CORRECT | Follows from expected local component sizes and lem:conc. |
| Line 369, p_k decreases to rho | CORRECT | Decreasing events {|Er|≥k} intersect in {|Er|=infinity}. |
| Line 369, full-graph local convergence, random budgets | GAP | This is explicitly attributed to EWT Theorem 2.1; the external theorem's exact hypotheses cannot be checked without its text. The paper's own Section sec:time proves only the fixed-cost version. Internal Poisson/rank exploration supports the claimed full local limit. |
| Line 369, same full-graph local convergence for deterministic arrays | GAP | Quote: “the local convergence of G_n to Er(P) [Theorem 2.1] gives ...”. The source supplied here does not establish that the cited iid-budget theorem covers deterministic triangular arrays. Section sec:time only proves fixed-cutoff local convergence. Supply the short extension to full graphs, or derive the needed expectation limit by a truncation argument. This is a proof omission, not evidence that uniform integrability of array means is necessary. |
| Line 369, concentration, L1≤max(k−1,F_k), choice of k | CORRECT | For fixed k, mean convergence plus lem:conc gives F_k/n→p_k. Then choose k with p_k<rho+u/2 and n large with (k−1)/n<rho+u. |

Independent repair of the deterministic-array local-limit omission: fix a budget threshold B and let W_n={i:d_i>B}. Remove W_n and its incident edges from the kept graph, retaining isolated vertex placeholders. The remaining low-low graph is unchanged if every high budget is replaced by B. Write b for the number of retained low-high edges. Deleting W_n can change F_k by at most |W_n|+(k−1)b: every affected low-only component previously had size <k and touches W_n, or it already contributed before deletion. Conditional on budgets, E b≤B n|W_n|/(n−1), by uniform neighbor ranks at each low vertex. Thus comparison to the all-budgets-clipped-at-B graph costs at most 2[|W_n|+(k−1)B n|W_n|/(n−1)] in expected F_k. Dividing by n, taking limsup_n, gives ≤2[1+(k−1)B]P(D>B). Finite mean of P implies B P(D>B)→0. For fixed B, full-graph local convergence follows by bounded-budget Poisson exploration: expose each visited vertex's first B+1 incident order statistics and their endpoints; their costs are tight, endpoints are asymptotically uniform, the number of candidates inspected to fixed retained radius is bounded by a constant depending on B,r, and collisions vanish. Empirical weak convergence gives the clipped marks. The clipped limit is Er(P∧B). Coupling through the Poisson weighted tree, any fixed exploration of Er(P) inspects finitely many vertices and finite budgets almost surely, so Er(P∧B) converges locally to Er(P). Hence the expected F_k limit follows by n→infinity followed by B→infinity. This supplies the upper bound for arrays with NO uniform integrability condition on the array. Only finite mean of the limit P is used in this particular repair.

Main theorem assessment after steps 1–6: no counterexample to thm:main found. The cost-time dependence issue is handled. Two short exposition repairs are needed (Markov state and array local-limit extension), the iid qualification should be explicit, and line 334 overstates fixed-point uniqueness. Numerical and attribution checks follow.

2026-11-12T04:17:10 — Step 7(a), simple-graph sensitivity: CORRECT. All 1,024 simple graphs on 5 vertices, all 10 toggles, all k=1,...,6 pass 2(k−1). Maxima: [0, 2, 4, 5, 5, 0].

2026-11-12T04:17:12 — Step 7(a), preference sensitivity: CORRECT. Exhaustive K4 orders, all positive effective budgets 1..3 and every moved edge/rank give exact maximum 3 changed kept edges. Exhaustive fixed-cutoff variants also give maximum 3. Paper bounds four and five are conservative, valid. Results in sensitivity.json.

2026-11-12T04:18:55 — Step 7(b), graph simulation completed: {"n": 500, "law": "constant2", "reps": 30, "mean": 0.031866666666666675, "sd": 0.007537187499478758, "se": 0.001376095871203491, "minimum": 0.02, "maximum": 0.052}. Numerical verdict pending tree comparison.

2026-11-12T04:18:55 — Step 7(b), graph simulation completed: {"n": 500, "law": "constant3", "reps": 30, "mean": 0.8872666666666668, "sd": 0.02343285835263623, "se": 0.0042782350355207365, "minimum": 0.844, "maximum": 0.928}. Numerical verdict pending tree comparison.

2026-11-12T04:18:55 — Step 7(b), graph simulation completed: {"n": 500, "law": "mixture1_5", "reps": 30, "mean": 0.30673333333333336, "sd": 0.111058211928617, "se": 0.020276362623164283, "minimum": 0.058, "maximum": 0.48}. Numerical verdict pending tree comparison.

2026-11-12T04:18:56 — Step 7(b), graph simulation completed: {"n": 2000, "law": "constant2", "reps": 30, "mean": 0.009600000000000001, "sd": 0.0016049492418657725, "se": 0.00029302230114023275, "minimum": 0.0075, "maximum": 0.013}. Numerical verdict pending tree comparison.

2026-11-12T04:18:58 — Step 7(b), graph simulation completed: {"n": 2000, "law": "constant3", "reps": 30, "mean": 0.88475, "sd": 0.011437800306967623, "se": 0.00208824707878856, "minimum": 0.8635, "maximum": 0.9075}. Numerical verdict pending tree comparison.

2026-11-12T04:19:00 — Step 7(b), graph simulation completed: {"n": 2000, "law": "mixture1_5", "reps": 30, "mean": 0.30008333333333326, "sd": 0.06505887033445479, "se": 0.01187807028266152, "minimum": 0.154, "maximum": 0.4005}. Numerical verdict pending tree comparison.

2026-11-12T04:19:09 — Step 7(b), Erlang-tree Monte Carlo completed: {"law": "constant2", "trials": 20000, "frontier_cap": 64, "max_depth": 200, "hit_cap": 0, "alive_at_depth": 0, "rho_proxy": 0.0, "binomial_se": 0.0, "zero_success_95_upper": 0.000149775396222962, "max_candidates_in_one_generation": 1000}. Cap hits are finite-run survival proxies, not a proof of infinitude.

2026-11-12T04:19:10 — Step 7(b), Erlang-tree Monte Carlo completed: {"law": "constant3", "trials": 20000, "frontier_cap": 64, "max_depth": 200, "hit_cap": 17698, "alive_at_depth": 0, "rho_proxy": 0.8849, "binomial_se": 0.0022566788650581187, "zero_success_95_upper": null, "max_candidates_in_one_generation": 26606}. Cap hits are finite-run survival proxies, not a proof of infinitude.

2026-11-12T04:19:10 — Step 7(b), Erlang-tree Monte Carlo completed: {"law": "mixture1_5", "trials": 20000, "frontier_cap": 64, "max_depth": 200, "hit_cap": 6410, "alive_at_depth": 0, "rho_proxy": 0.3205, "binomial_se": 0.0032998465873431146, "zero_success_95_upper": null, "max_candidates_in_one_generation": 17828}. Cap hits are finite-run survival proxies, not a proof of infinitude.

2026-11-12T04:19:10 — Step 7(b), Erlang-tree Monte Carlo completed: {"law": "constant2", "trials": 20000, "frontier_cap": 256, "max_depth": 200, "hit_cap": 0, "alive_at_depth": 0, "rho_proxy": 0.0, "binomial_se": 0.0, "zero_success_95_upper": 0.000149775396222962, "max_candidates_in_one_generation": 1000}. Cap hits are finite-run survival proxies, not a proof of infinitude.

2026-11-12T04:19:11 — Step 7(b), Erlang-tree Monte Carlo completed: {"law": "constant3", "trials": 20000, "frontier_cap": 256, "max_depth": 200, "hit_cap": 17699, "alive_at_depth": 0, "rho_proxy": 0.88495, "binomial_se": 0.0022562523961206114, "zero_success_95_upper": null, "max_candidates_in_one_generation": 101172}. Cap hits are finite-run survival proxies, not a proof of infinitude.

2026-11-12T04:19:12 — Step 7(b), Erlang-tree Monte Carlo completed: {"law": "mixture1_5", "trials": 20000, "frontier_cap": 256, "max_depth": 200, "hit_cap": 6512, "alive_at_depth": 0, "rho_proxy": 0.3256, "binomial_se": 0.0033134924173747553, "zero_success_95_upper": null, "max_candidates_in_one_generation": 68700}. Cap hits are finite-run survival proxies, not a proof of infinitude.

2026-11-12T04:19:21 — Step 7(b), independent generating-equation quadrature cross-check: {"law": "constant2", "dx": 0.005, "x_max": 60, "iterations": 75, "last_fixedpoint_error": 7.011058400507864e-13, "rho_quadrature": 4.346745186012413e-12}.

2026-11-12T04:19:21 — Step 7(b), independent generating-equation quadrature cross-check: {"law": "constant3", "dx": 0.005, "x_max": 60, "iterations": 41, "last_fixedpoint_error": 7.607248164731573e-13, "rho_quadrature": 0.8855735734323648}.

2026-11-12T04:19:21 — Step 7(b), independent generating-equation quadrature cross-check: {"law": "mixture1_5", "dx": 0.005, "x_max": 60, "iterations": 95, "last_fixedpoint_error": 8.816836150060681e-13, "rho_quadrature": 0.3232665411595447}.

2026-11-12T04:19:21 — Step 7(b), independent generating-equation quadrature cross-check: {"law": "constant2", "dx": 0.0025, "x_max": 60, "iterations": 75, "last_fixedpoint_error": 7.011058400507864e-13, "rho_quadrature": 1.9051427102567686e-12}.

2026-11-12T04:19:21 — Step 7(b), independent generating-equation quadrature cross-check: {"law": "constant3", "dx": 0.0025, "x_max": 60, "iterations": 41, "last_fixedpoint_error": 7.587819261800632e-13, "rho_quadrature": 0.8855735018030011}.

2026-11-12T04:19:21 — Step 7(b), independent generating-equation quadrature cross-check: {"law": "mixture1_5", "dx": 0.0025, "x_max": 60, "iterations": 95, "last_fixedpoint_error": 8.800737916203616e-13, "rho_quadrature": 0.323265715586998}.

Step 7(b) numerical verdict: CORRECT as a consistency check, not a proof. Graph simulations (30 independent replicates each) give mean L1/n: constant 2, n=500: 0.0318667 (SE 0.0013761), n=2000: 0.0096000 (SE 0.0002930); constant 3: 0.8872667 (SE 0.0042782), 0.8847500 (SE 0.0020882); mixture P(1)=0.6,P(5)=0.4: 0.3067333 (SE 0.0202764), 0.3000833 (SE 0.0118781). Tree Monte Carlo, 20,000 trials per law and frontier cap, gives rho proxies at cap 64 / 256: constant 2: 0 / 0; constant 3: 0.88490 / 0.88495; mixture: 0.32050 / 0.32560. Every unclassified tree died or hit its cap before depth 200; no depth-limit survivors remained. These are finite-frontier survival proxies, with possible finite-tree cap hits, not exact infinite-tree survival samples. No substantial graph/tree mismatch appears relative to sampling error and finite-size effects. The mixed-law n=2000 mean is about 1.95 graph standard errors below the quadrature limit, worth reporting rather than hiding, but does not establish an error.

Independent numerical cross-check: solve the non-root generating equation from the zero extinction function (the minimal fixed point), using composite trapezoids on x∈[0,60]. Grid spacings 0.005 / 0.0025 give rho: constant 2: 4.35e−12 / 1.91e−12 (numerical zero); constant 3: 0.8855735734 / 0.8855735018; mixture: 0.3232665412 / 0.3232657156. Monte Carlo is consistent with these numbers. This checks the root Gamma(D+1) convention independently against the child Gamma(D) convention. This quadrature is not a certified error bound.

Resource audit for step 7: sensitivity run 3.01 seconds; graph run 5.47 seconds, peak RSS 250,118,144 bytes; tree run 2.24 seconds, peak RSS 77,365,248 bytes; quadrature run 0.10 seconds, peak RSS 31,408,128 bytes. Each computation had an internal 270-second alarm and ran serially. Numerical thread environment variables were fixed at 1. Priority lowering was attempted but macOS sandbox denied it; no additional compute process was started to work around that denial. Initial sensitivity launches stopped immediately on priority-setting errors; the final script catches that permission failure.

## 8. Attribution and novelty (memory only)

| Location / statement | Verdict | Reason |
|---|---|---|
| Lines 40, 408–409, La–Kabkab constant-budget attribution | GAP | The mutual cheapest-neighbor construction is consistent with my recollection of the bilateral preference model. I cannot verify the precise original model, bibliographic details or priority from memory alone. It must not be conflated with greedy degree-constrained b-matching, which counts accepted edges rather than all rank arrivals. |
| Lines 42, 46, 411–412, EWT account | GAP | The supplied account is consistent with my memory of the Erlang weighted tree/local-limit work. I cannot independently authenticate the exact theorem/corollary/question numbers, all hypotheses, or the quoted open-question status without the cited text. The paper's own type construction passes the independent simulations. |
| Claim of new reverse inequality | GAP | I cannot name with confidence a prior paper proving the stated equality for this exact model and all these budget laws, or a general theorem whose verified hypotheses immediately give it. This is NOT a literature search or a certificate of novelty. Known broad giant-from-local-limit criteria still require an almost-local connectivity/coalescence hypothesis; the present sprinkling proof supplies such work. |
| Sprinkling citations, Section sec:sprinkle | CORRECT | The argument is given directly; no external sprinkling theorem is actually invoked. No sprinkling theorem number is cited. The Markov-state repair remains necessary for the formulation in line 169. |
| Alon–Spencer citation | GAP | There is no Alon–Spencer reference in this source, at point of use or in the bibliography. “AS” means Aldous–Steele. Efron–Stein and Chernoff are named but have no source/theorem numbers (lines 108,112,161,351,357). They are standard and used correctly. |
| van der Hofstad, line 46 and refs vdH/vdHbook | CORRECT | The introductory description is consistent with my recollection. Both citations lack theorem numbers. They are contextual, not a load-bearing invoked theorem in this proof. Exact source content/edition/publication status cannot be checked here. |
| Spectral theorem, line 243 | CORRECT | Standard compact self-adjoint spectral theorem; assumptions are verified internally. No external theorem number is given. |

Further wording audit: line 150 (“says nothing about the density ... in any single component”) is too broad literally: a single component of size at least eta*n IS an admissible union. The intended statement about an individual component of size merely k is correct. Revise my earlier interpretation-based CORRECT assessment to GAP for that sentence's unqualified wording. This does not affect lem:cover or sprinkling.

Overall verdict: GAP. The theorem's mathematics survives the independent checks, and explicit short repairs are available; as submitted the Markov-state formulation and deterministic-array full-local-limit invocation omit details, the common-cost-law qualification is unclear, and the fixed-point-uniqueness sentence is false. No counterexample to the main theorem found. Full report follows in REPORT.md.

Additional independent implementation check: CORRECT. On 1,000 random K8 instances, direct mutual rank lists exactly matched chronological acceptance with ALL arrivals counted. This explicitly checks the central accepted-versus-arrived distinction.

2026-11-12T04:28:09 — REPORT.md completed: full verdict tables, explicit repairs, exhaustive-check and simulation tables with commands, all wording issues noticed, citation limits and overall GAP verdict. Final audit checked every requested LaTeX label, Markdown table structure, 180 saved graph trials, 240 saved tree batches, six rows in each numerical summary, and unchanged PAPER.tex SHA-256. Task complete.
