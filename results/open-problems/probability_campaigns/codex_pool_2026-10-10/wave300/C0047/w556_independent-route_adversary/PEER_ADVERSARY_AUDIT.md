# Adversary audit of w555's core route

2026-10-10. Source: ~/brain_workers/w555/PROOFS.md, L1-L5 and attempted extension. My operator route and S1/S2 derivations were saved before reading this file. This is a mathematical adversary audit, not a served-model or formal-check receipt.

Verdict: KEEP SCOPED SPECIAL CASE AND OBSTRUCTION; NO GENERAL C0047 PROOF.

L1 supplies exactly the independence its product needs: deterministic, pairwise edge-disjoint cutsets, each blocking every x-y path. The opening event for each cutset uses only its own product-measure coordinates. The size-bound inequality has the correct direction for p in [0,1].

L2 uses vertex transitivity to obtain a common strictly positive infinite-cluster membership probability, and Harris association rather than an asserted independence of membership events. Its conclusion p_u=1 includes the connected infinite graph at p=1. My independent S1 finite-set witness confirms the same uniqueness lower-bound mechanism without cutsets.

L3 correctly reduces to inclusion-minimal x-y cuts. Minimality forces exactly two components and every reduced cut edge between them. Local finiteness makes the one-end argument legitimate after deleting the cut endpoints. The finite side has at most K/h_E vertices, so all reduced cuts draw nonempty disjoint subsets from a fixed finite collection of edges around x or y. The displayed bound is conservative but valid. It rules out this exact separator hypothesis on one-ended nonamenable Cayley graphs.

L4's quotient is a tree of m-cycles for the specified simple graph C_2*C_m, m>=3. A descendant entry uses the parent bridge; all remaining bridge variables and that cycle's internal variables are fresh. Its nonroot offspring distribution therefore is Binomial(X-1,p), not merely a positive conditional mean. The root instead has Binomial(X,p) possible exits; it supplies finitely many seeds and has a positive chance to supply one when p>0, so this difference preserves the critical criterion. The two cycle arcs are edge-disjoint and inclusion-exclusion gives the stated expectation. The nondegenerate bounded offspring distribution justifies extinction at mean one. The bridges prevent the surviving descendants from remerging in the ambient graph, which is the crucial geometric premise.

L5 correctly uses adjacency A=dP, and bounds a union over simple paths before replacing the count with all walks. It never assigns p^n to repeated-edge walks. This normalization correction belongs to w555's lane; I do not claim it as a new computation of my own.

The hardest extension step is still missing, as w555 explicitly records: fresh branching in an embedded or explored subtree does not prevent ambient mergers. A valid general extension needs either fresh separator events that block every remaining ambient path, or an independently derived quantitative nonmerger estimate at a parameter above the original graph's p_c. Nonamenability alone has not supplied either premise here. L3 excludes the uniformly bounded deterministic-cut version on the one-ended class.

No fatal flaw was found in the stated L1-L5 scope. The convention comparison with Kozakova's multiple-edge model is not needed for the simple-graph proof and remains a separately sourced inference. The label "right coset g<C_m>" in L4 should read "left coset"; the defined set and geometry are unambiguous, so this is terminology rather than a proof gap.

NEXT: w557 checks the special case independently; any attempt to extend L4 must replace the tree-of-blocks nonmerger premise with a proved statement on the original fixed Cayley graph.
