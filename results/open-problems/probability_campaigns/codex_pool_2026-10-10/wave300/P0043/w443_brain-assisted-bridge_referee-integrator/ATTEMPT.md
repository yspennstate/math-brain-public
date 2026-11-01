# P0043 bridge attempt — 2026-10-10

## Exact need

For an infinite connected locally finite undirected quasi-transitive graph G with `p_c(G)<1`, show that iid Bernoulli **bond** percolation at `p_c(G)` has no infinite component almost surely. This is Hutchcroft (2016), Conjecture 1.1. The 2026-09-07 ranking's shorter `theta(p_c)=0 on quasi-transitive graphs` drops conditions that matter: on `Z`, `p_c=1` and all edges are open at `p_c`.

## What the brain returned

Read-only `python -X utf8 .\recall_probe.py` returned an old P0043 open-problem card at rank 1 and a regular-tree attempt at rank 2. The latter says, in part, "For the regular tree at p=1/b, an infinite descendant cluster would have survival probability x satisfying x=1-(1-px)^b." Its explicit obstruction is that general quasi-transitive critical clusters are not independent branching trees. This formula needs independent isomorphic forward subtrees; a general graph with loops, and especially a random sampled cluster, does not supply them. The named query for Hutchcroft's exponential-growth theorem returned **no theorem in the top five**. Full card receipts and scores are in `CARD_READS.json` and `RECALL_MEASURE.json`.

## Source theorem versus the proof need

Hutchcroft (2016), Theorem 1.2: a connected locally finite quasi-transitive graph of **exponential volume growth** has no infinite critical bond cluster. The theorem's source proof uses subcritical finite susceptibility and a decay bound on the minimum two-point function; quasi-transitivity rules out a unique critical infinite cluster when that bound decays. P0043 asks for **all** such graphs with `p_c<1`; subexponential graphs, including `Z^3`, are outside the theorem's hypothesis. The 2026-09-24 manuscript claims to close the full gap by splitting subexponential growth into superpolynomial and bounded-polynomial-scale cases. It invokes the 2016 theorem for the exponential case. I checked that case split at the statement and completion sections, not every load-bearing lemma.

The bundle relation is exact: old P0043 card quote, "If G is quasi-transitive and p_c(G)<1, is there almost surely no infinite Bernoulli cluster at p_c(G)?" New theorem card statement: "Let G be an infinite, connected, locally finite, quasi-transitive graph of exponential volume growth ... at its critical probability ... almost surely no infinite open cluster." `hutchcroft-exponential specializes P0043` because its extra growth assumption narrows the target. The status concept cites the 2016 theorem because the 2026 manuscript explicitly uses it.

## Attempted thinning bridge and its obstruction

w441's L002 is valid: if an iid Bernoulli-p configuration is independently q-thinned, the product bits have law Bernoulli-pq. For every rational `q<min(1,p_c(G)/p)`, the thinned graph has no infinite component almost surely. Fubini/Tonelli then gives `p_c(C)>=min(1,p_c(G)/p)` for every infinite sampled component C, for almost every original configuration. At criticality this gives `p_c(C)=1`. I rederived the conditional argument; the selected component is not treated as independent of the original configuration.

Could geometry contradict that fragility? L004 gives a sufficient condition: if an infinite C has positive rooted edge expansion `h`, then for q close enough to 1 a rooted q-open cluster survives with positive probability. The count of rooted connected sets of size n is at most `Delta^(2(n-1))`; their boundary-closure probabilities sum to less than one when `(1-q)^h<1/(Delta^2+1)`. This would contradict critical fragility. But w442-C003 proves that every infinite connected subgraph of a bounded-degree **subexponential** graph has zero anchored expansion: positive boundary ratio would force its balls to grow exponentially. Thus the sufficient condition fails precisely in the main remaining regime. The route gives necessary geometry and a near-critical bound, not a full proof.

The hardest unresolved independent-proof step is a uniform finite-connection mechanism that turns a putative critical infinite cluster into positive survival at one common subcritical parameter without assuming positive anchored expansion or independent bounded corridors. w442's `f_n(p)=min(1,(p/a)^n)` countermodel shows why finite-scale continuity alone cannot exchange the radius and parameter quantifiers. The new manuscript claims such a mechanism by other means; its full proof and comparator closure remain a separate review task.

NEXT: Coordinator checks the public proof artifact and validates the exact theorem/status draft; no parent-problem solution is claimed by this attempt.
