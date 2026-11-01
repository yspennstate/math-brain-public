# G0012 research record

Target: for each epsilon>0 there is C(epsilon) such that on every finite simple undirected n-vertex graph with minimum degree at least three, every length-k random non-backtracking walk (NBW), from every prescribed directed first edge, is simple with probability <epsilon whenever k>C(epsilon)sqrt(n). Length counts edges, so simplicity requires k+1 distinct vertices. Confirmed verbatim in Dozier, arXiv:2608.26321v1, Conjecture 1.5, PDF p.2.

## Source and earlier work checked, 2026-10-11

Dozier Theorem 1.1 has a constant depending on fixed regular degree d. Bencs et al., arXiv:2608.09729v1, Theorem 1, assumes fixed maximum degree and proves O_Delta(sqrt(n) log n) expected collision time; Theorem 2 treats fixed-degree spectral expanders. Neither settles the target. Bencs et al. Question 4 asks for universal O(sqrt(n)) expected collision time on the full simple-graph class. Their multigraph counterexample is outside our hypotheses.

Read-only brain recalls (topic and mistakes), math-store query, intake G0012-A001, and origin/master records operations/claims/G0012.md and the R01 September 17 handoff were consulted. The intake's proposed degree-ratio Jacobian in reversal is incorrect: the product of local uniform derangements is invariant under inversion at any degrees. The prior R01 biregular theorem and its global-averaging correction were also read. We do not claim those earlier results as new discoveries. The result developed below handles arbitrary bounded degree ratio, and we do not assert novelty.

## Partial theorem being checked

Write delta=min_v d(v), Delta=max_v d(v), a=delta-2, b=Delta-2, R=b/a>=1. The proposed estimate is

    P_delta0(simple through k edges) <= 800 n R^2/k^2

whenever k^2>=784 n R^2. In particular a constant degree ratio (even with unbounded degrees, no regularity, no bipartiteness, and many degree changes) gives the conjectured scale. This remains a restriction: R can diverge arbitrarily in the source class. Full proof and hostile checks follow.

The complete proof is in bounded_ratio_proof.md, Sections 1-4. It uses raw global deviation counts, a simple-interior excursion reversal involution, and conditional heat-bath resampling. It does not assume a per-plan returning-deviation bound. Sections 5-6 give the expected-time corollary and exact remaining gap.

## Exact computations and hostile checks

finite_checks.py enumerated 208,037 product plans across 15 connected graph-atlas graphs on 4-6 vertices (including irregular degree profiles), from one prescribed edge per graph. For every k=2,...,n-1, exact rational killed-NBW dynamic programming on (previous vertex,current vertex,visited bitmask) agreed with the simple-plan counting fraction. It checked the global raw bad-count lower bound for L=1,2 and the heat-bath incoming bound for every generated target. Runtime reported by the program was 62.35 seconds; no Monte Carlo was used. The original cap was 120,000 plans per graph, with a 150-second deadline; the saved script's cap was subsequently tightened to 60,000 (all 15 tested graphs already lie below 60,000). Largest tested graph-plan space was 59,049; jobs used small bounded graph data. Raw results: finite_results.json.

Derangements were enumerated at d=3,...,7; counts were 2,9,44,265,1854 and each fixed non-backtracking image had fiber size 1,3,11,53,309 respectively. This tests the completion-count input, not a proof at arbitrary d; the arbitrary-d symmetry argument is in proof Section 1.

reversal_checks.py tested the full excursion inversion and reversal twice, on 416 middle-returning simple-interior cases over all 256 cubic cube plans, using (k,L)=(4,4),(5,3). It confirmed the base path is unchanged, the reversed departure is admissible, the excursion is exactly reversed, at least one member collides, and double inversion restores the original plan. Raw results: reversal_results.json.

Important limits: small graph values do not satisfy the large-k theorem's threshold, so they test its nontrivial local combinatorial ingredients rather than numerically certify the asymptotic theorem. The crude global bad-count inequality can be vacuous on these small instances; the explicit 416 reversal tests and target-by-target heat-bath sums give stronger direct checks of those ingredients.

### A proved obstruction to naive vertex packing

The cube has edges 01,03,04,12,17,23,26,35,45,47,56,67. Specify local derangements by cycles:

| Vertex | Neighbor permutation cycle |
|---|---|
| 0 | (1 3 4) |
| 1 | (0 2 7) |
| 2 | (1 3 6) |
| 3 | (0 2 5) |
| 4 | (0 5 7) |
| 5 | (3 4 6) |
| 6 | (2 5 7) |
| 7 | (1 6 4) |

The base path starting with 01 is 0,1,2,3. Change departure at vertex 1 to 7: the length-two excursion is 1,7,6 because pi_7(1)=6. Change departure at vertex 2 to 6 instead: the excursion is 2,6,5 because pi_6(2)=5. Both walks are simple up to the end of these excursions, and neither excursion returns to the base path. Their external directed edges are disjoint, but they share external vertex 6. All specified maps are derangements of exactly the displayed neighbor sets. This is a complete counterexample to the auxiliary assertion that non-returning deviation segments must be vertex-disjoint; it is NOT a counterexample to G0012. Replacing directed-edge packing by vertex packing without an additional overlap argument is invalid.

### Referee checklist

1. Variable-degree plan measure: uniform product counting and pathwise transition identity are proved in Section 1; exact enumeration agrees.
2. Directed-edge disjointness: unique predecessor under a bijection, with departure identified as first backward base hit; only non-returning segments are counted. Vertex disjointness is false as shown above.
3. Excursion reversal: performed only on excursions with distinct interior vertices; omitted ones already collide. This avoids relying on a reversal claim for potentially repeated interiors. The pairing is global over S.
4. Changed permutation completions: simplicity up to a given time cannot depend on unused departure entries, since their first reuse entails an already-detected vertex collision.
5. Incoming sources: first target collision pins the departure to a window; before collision every candidate vertex is distinct. Counting all possible source local maps only overestimates sources. Fiber counts cancel exactly.
6. Window and degree constants: delta>=3 implies a>=1; Delta<=3b and Delta-1<=2b; n>=4 and the threshold gives k>=56R. The ceil estimates use k<n, R>=1.
7. Full conjecture: no uniform-in-R conclusion follows. The partial theorem is not presented as a solution or as new literature.

## Lean verification scope

The final Lean command exited 0: all declarations in HeatBath.lean were kernel-checked, with no sorry or native_decide. The full graph theorem remains a written mathematical proof rather than a Lean formalization.

HeatBath.lean formalizes the degree-four derangement and fixed-image fiber counts using decide +kernel, plus the algebraic double-count/window/final-constant steps. It imports only specific Mathlib modules. It does not formalize the graph trajectory or excursion-reversal proof. Initial runs caught a missing real-number import and misuse of mul_nonneg's proof argument; those errors were fixed before any Lean result was called checked. Final compiler outcome is retained in lean_check.txt.

## Exact reduction to the expected-time question

The full source conjecture is equivalent to a universal O(sqrt(n)) expected first-collision bound, whether starting from any prescribed directed edge or from any vertex with uniform first step. This is an elementary reduction, not a solution.

Suppose the full conjecture holds and choose its constant C for epsilon=1/2. Set q=floor(C sqrt(n))+2 and h=q-1. For a prescribed-edge walk let tau be its first vertex-collision time. Conditional on any collision-free prefix through time rh+1, the future only depends on the current directed edge. Its next q-edge block, including that current edge as its first edge, is internally simple with probability at most 1/2. Global survival of the prefix extended through (r+1)h+1 implies that internal simplicity. Therefore P(tau>rh+1)<=2^(-r) by induction. Splitting the tail sum into intervals k=rh+1,...,(r+1)h gives E(tau)<=1+2h<=2C sqrt(n)+3. All conditioning here is on the full prefix, not on a claimed stationary distribution.

Conversely a uniform directed-edge expectation bound E(tau)<=M sqrt(n) gives P(tau>k)<=M sqrt(n)/k by Markov's inequality, exactly the source conclusion with C=M/epsilon.

A uniform directed-edge expectation bound implies the same vertex-start bound by averaging over the first neighbor. For the converse, assume the uniform-first-step walk from every vertex v has first-collision expectation at most M sqrt(n). Given edge (u,v), generate a vertex-start walk from v conditional on its first neighbor not being u, an event of probability (d(v)-1)/d(v)>=2/3. Prepending u gives exactly the prescribed-edge NBW law. The prepended walk can only collide earlier than one plus the original vertex-start collision time. Its expected collision time is consequently at most 1+(3/2)M sqrt(n). Thus Bencs et al. Question 4 is equivalent, up to constants, to the full G0012 statement on connected simple graphs; disconnected graphs follow by applying bounds to the starting component, whose vertex count is at most n.
