VERDICT: PASS (correct and complete)

Independent audit of E0101, 12 October 2026

Claim reviewed and scope

I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md in the claimant's directory without modifying them. Locations below refer to ATTEMPT.md line numbers in that copy.

The principal claim (lines 13?21, 85?86; CLAIMS.jsonl item 2) is this: Let P be a transient irreducible Markov chain on a countable state space S, with compact metrizable Martin compactification K. Let the offspring distribution be spatially constant, independent in the standard BRW construction, with finite mean m>1 and E[N log N]<infinity. For a countable basis (V_i) of the boundary topology assume, for every i and every xi in V_i,

    liminf_{x in S, x -> xi} P_x(X_infinity in V_i) > 0.             (R)

Then, for each starting state, almost surely supp W equals the set L of boundary accumulation points of the particle positions. The quantifiers in (R) permit the positive constant and neighborhood to depend on both xi and i. The probability-one assertion is obtained using countably many basis sets and reciprocal-integer thresholds, not by intersecting uncountably many events.

The subsidiary claims are: the inclusion supp W subset L without (R); Dirichlet regularity implies (R); equality for simple random walk on every (q+1)-regular tree, q>=2; equality for symmetric finite-support generating random walks on non-elementary word-hyperbolic groups with spectral radius below one; and a counterexample if the source's L log L assumption is removed.

I independently downloaded https://arxiv.org/pdf/2205.15287 and checked Theorem 1.1 on PDF page 2 and Problem 4.2 on page 9. The problem says exactly: "Give conditions under which the support of W coincides almost surely with the set of accumulation points of B." It does not demand necessary and sufficient conditions. Page 9 explicitly gives a lamplighter counterexample to universal equality and singles out hyperbolic groups as an expected positive class. Thus the sufficient criterion, together with its non-vacuous tree and hyperbolic-group applications, answers the stated question. This is not a special case being misrepresented as a universal equality theorem.

Issues found

No failed step, missing material hypothesis, or substantive gap was found in the stated sufficient-condition result or its applications. No repair is required for this verdict. The limitations below are limits of the established result, not additional theorems.

Detailed proof audit

1. Definition of accumulation and the unconditional inclusion (lines 11, 24).

Each generation is finite almost surely because the offspring law takes finite integer values and has finite mean. A boundary-convergent sequence of positions cannot be confined to finitely many generations, since that would confine it to a finite subset of the discrete state space. Thus the definition using generations tending to infinity agrees with boundary accumulation of the entire particle trace.

For a K-open U, Portmanteau for the nonnegative finite measures m^{-n} B_n gives liminf m^{-n} B_n(U)>=W(U). If xi belongs to supp W, the right side is positive for every neighborhood U of xi. Such a neighborhood is therefore visited at all sufficiently large generations. Nested metric balls of radii tending to zero permit choosing increasing generations and positions tending to xi. The boundary is closed, and the source theorem places W there, so no state-space support point is inadvertently included. Extinction gives zero W and empty L. The inclusion is valid pathwise on the weak-convergence event.

2. Uniform positive success probability (lines 26?28).

For a one-particle descendant process let Y=W_x(V) and Z=W_x(K). Weak convergence tested against the constant function 1 identifies Z with the usual Galton?Watson martingale limit. Its law is independent of x, E Z=1 by Kesten?Stigum under L log L, and 0<=Y<=Z. The source expectation identity applies to every Borel V, not just continuity sets, and gives E_x Y=h_V(x).

Choose a positive finite cutoff K_c with E[Z 1_{Z>K_c}]<c/2. Splitting according to Z<=K_c and Z>K_c gives

    E_x Y <= K_c P_x(Y>0) + E[Z 1_{Z>K_c}].

If h_V(x)>=c this implies P_x(Y>0)>=c/(2K_c)>0. This deduction uses a common integrable total-mass law; it does not smuggle in a second moment, a bound uniform in all boundary points, or positive mass on any individual end. The actual process guarantees consistency of the lower bound with probability at most one. Empty or impossible threshold cases are harmless.

I re-derived this inequality directly and checked 891 dominated finite rational-law examples independently. These tests only check finite examples of the algebra; integrability supplies the infinite-law tail choice in the proof.

3. Descendant decomposition and conditional product (lines 30?34).

At fixed n and t>=0 there is the exact finite-measure identity

    m^{-(n+t)} B_{n+t} = m^{-n} sum_{|u|=n} m^{-t} B^u_t.

The source theorem applies conditionally to each actual birth state. Countably many possible particle labels permit simultaneous existence of the descendant weak limits. Since the generation-n sum is finite, passage to weak limits proves W=m^{-n} sum W^u as an identity of measures, not just convergence of their evaluations on selected sets.

Consequently W(V)=0 if and only if every generation-n descendant measure gives V zero mass. Conditional on the history through the birth of generation n, these descendant processes are independent with their respective one-particle laws. The claimed product formula follows, including the empty-generation convention. Revealing descendants' reproduction in this filtration would invalidate that independence; the filtration described and used in the proof is the usual history through generation n, so no such additional revelation is needed or used. If a generation contains one particle with h_V>=c, the product is at most 1-p_c.

4. Infinitely many visits and zero limiting mass (line 36).

A={W(V)=0} is measurable in the full genealogical history: W is the almost-sure weak limit of measurable random finite measures, and evaluation on a Borel set is measurable. Levy's upward theorem gives P(A|F_n)->1_A almost surely. On A, convergence to 1 forbids infinitely many n for which P(A|F_n)<=1-p_c. It therefore forbids infinitely many generations with a particle at a state satisfying h_V>=c. This requires no independence between successive visits, no selection of a stopping line, and no assumption that the repeatedly encountered particles have disjoint ancestry.

The probability-one intersection over all (i,j), with V=V_i and c=1/j, is countable and valid. Finite generations also ensure that infinitely many particles along an accumulating sequence force unbounded generations.

5. Reverse inclusion and arbitrary random accumulation points (line 38).

If xi in L is outside supp W, some K-open U containing xi has W(U)=0. A deterministic basis set V_i can be selected with xi in V_i subset U intersect boundary. It is Borel in K, and W(V_i)=0. Assumption (R) supplies a K-neighborhood O and a positive threshold, which can be decreased to 1/j, on which h_{V_i}>=1/j for states in S. The accumulating sequence enters O at unbounded generations, contradicting item 4. Selection of xi after observing the process does not introduce an uncountable exceptional-set gap. Together with item 1 this proves the advertised equality.

Applications and boundary cases

Regular tree (lines 52?71).

I independently checked the finite radial hitting formula

    f_L(r)=(q^{-r}-q^{-L})/(1-q^{-L})

and its recurrence (q+1)f_L(r)=f_L(r-1)+q f_L(r+1). Exact Fraction arithmetic passed all 3,045 interior checks for q=2,...,8 and L=2,...,30, and both endpoints in all 203 parameter pairs. The finite-exit argument, maximum principle, and monotone limiting hitting event justify the formula beyond those tests: P_x(hit a)=q^{-d(x,a)}.

The return probability from a after departing is 1/q, yielding G(a,a)=q/(q-1) and G(x,y)=q^{-d(x,y)}q/(q-1). Hence the stated Martin kernel q^{2(x|y)_o-|x|} is correct. Transience at each vertex, countability, and finite balls imply almost-sure convergence to an end. Finite branching gives compactness of the end compactification; kernel limits distinguish ends and account for every sequence escaping finite balls, establishing the claimed Martin/end topology identification.

For x in the forward subtree of v, an exit outside C_v requires hitting its parent. The hitting formula gives exactly the claimed lower bound 1-q^{-(d(x,v)+1)} for h_{C_v}(x). Boundary convergence to a point of C_v forces d(x,v)->infinity, so (R) follows. No argument here imposes a restriction on m relative to the local-survival threshold.

Hyperbolic groups and Dirichlet regularity (lines 73?80).

I independently downloaded https://arxiv.org/pdf/2205.13615v2. Proposition 3.19 on PDF page 18 identifies Dirichlet regularity with weak concentration of the hitting distributions at boundary points. Proposition 3.38 on page 24 gives the quoted result for the end, hyperbolic and Floyd compactifications under quasi-transitivity and absence of a globally fixed boundary point. Page 25, item (ii), recalls the Martin/hyperbolic identification when the graph is hyperbolic and the bounded-range chain has spectral radius below one. The definitions on pages 22?23 match the hypotheses being used.

The claimant's Cayley-graph walk is locally finite, bounded range and uniformly irreducible. Left translations act transitively and preserve P. A non-elementary hyperbolic group's boundary is infinite and has no global fixed point for the full group action. Irreducibility follows from generating support; spectral radius below one gives transience. These are the required boundary-theory inputs for the stated class. I checked their cited statements and applicability, rather than supplying new proofs of Ancona's theory.

For the last implication, compact metrizability yields a continuous boundary function phi valued in [0,1], equal to 1 at xi and zero outside V. Its bounded continuous harmonic extension f satisfies f(x)=E_x phi(X_infinity) by the martingale and boundary convergence argument. Thus h_V(x)>=f(x)->1 as x->xi. This proves (R) for every boundary-open V. The corollary is correctly supported by existing boundary theory plus the audited probability argument.

Dropping the moment assumption (line 89).

The explicit offspring distribution is normalized because A=sum_{k>=3} 1/[k^2(log k)^2] is finite and positive. Its mean is finite by convergence of sum 1/[k(log k)^2], and is strictly greater than 2. Its logarithmic moment diverges by divergence of sum 1/[k log k]. All particles have at least two children, so survival is certain. Kesten?Stigum, expressly stated on source page 2, gives normalized total mass tending to zero. On the compactification this forces weak convergence to the zero measure. The always-first-child genealogical ray has the ordinary simple-random-walk law and converges to an end, so L is nonempty almost surely. This is a correct counterexample outside, and only outside, the source's moment assumptions.

Literature checks and the apparent competing claim

I performed fresh arXiv API searches, saved as arxiv_search.xml and arxiv_precise.xml, and inspected relevant returned titles. A broader single-word search, saved as arxiv_targeted.xml, was noisy and is not evidence of comprehensive coverage. Two fresh OpenAlex requests (a topical search and a valid source DOI filter) returned HTTP 429; no successful OpenAlex coverage is claimed.

I additionally fetched abstracts of arXiv:2308.03711v5, 2502.07633v2 and 2409.01346v3, saved in related_abstracts.xml. Their stated topics are survival/persistence and Martin boundaries, empirical displacement limit theorems, and multifractal limit sets, respectively. These abstracts do not state the support-equality theorem. An abstract inspection cannot rule out an unadvertised result in the full text.

I independently downloaded and examined Woess, https://arxiv.org/pdf/2405.07301, PDF page 26, and Geldbach, https://arxiv.org/pdf/2509.06730, PDF pages 3?4 and 11. Woess's note does indeed attribute a topological-support dimension theorem and strict support inclusion to Geldbach. Geldbach's Theorem 1.1 instead states the dimension of the measure. Corollary 3.2 bounds that dimension using a countable union of typical-particle accumulation sets with full measure. Passing to the closure of such a union can increase dimension; this is not an upper bound on the topological support's dimension. The claimant correctly identifies the distinction at line 83. I do not resolve the Brownian model's support question here, but the inspected statements do not provide a proved counterexample to the discrete theorem being audited.

The literature check found no verified earlier theorem settling the exact claimed criterion, and no verified counterexample under its assumptions. This bounded check establishes neither novelty nor exhaustive absence of earlier solutions. SOLVED_IN_LITERATURE is not the claimant's verdict and is not warranted by this audit.

What is proved and what is not

The sufficient criterion (R), its Dirichlet-regularity consequence, and the specified tree and hyperbolic-group corollaries are proved. The unconditional inclusion and the outside-hypotheses counterexample are also correct. Necessary conditions, arbitrary irregular Martin boundaries, a classification of all chains, and the fine dimension or singularity properties of W are not proved or claimed.

I did not rerun or rely on the claimant's Lean artifact: the relevant algebra was checked independently, and the substantive measure/martingale/topology proof was audited mathematically. Independent exact-check counts are recorded in exact_checks.txt. All downloaded PDFs, extracted texts, search responses and this report were written only in the designated audit directory. The claimant's files were read only.
