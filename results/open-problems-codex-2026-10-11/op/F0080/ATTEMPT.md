# F0080 ? answered in the literature

Date: 2026-10-11. This is a literature resolution, not a claim of a new theorem.

## Exact source statement and hypotheses

Lyons?Peres?Schramm, Question 6.13, source PDF p. 27:

> Given a finitely generated group ?, does the expected degree of a vertex in the FMSF of a Cayley graph of ? depend on which Cayley graph is used? As discussed in the proof of Corollary 3.24, the analogous result is true for the FSF.

The forest uses independent continuous edge labels and the finite-cycle deletion rule. Vertex transitivity makes the expected degree independent of the vertex. The question is about varying the Cayley graph, not the vertex or the label distribution. Infinite locally finite Cayley graphs are the principal setting; finite groups are handled separately below. The supplied statement matches the fetched source exactly.

## Published answer and scope

Andreas Thom's *The expected degree of minimal spanning forests*, Theorem 1, proves for a vertex-transitive graph G of degree d and simple-random-walk spectral radius ?:

    1/(4?) ? 1/4 ? ?_FMSF(G) ? d.

Corollary 2 proves that for every finitely generated nonamenable group the FMSF expected degree is unbounded over finite symmetric generating multisets. The paragraph immediately after the corollary expressly says that it answers LPS Question 6.13.

The multiset distinction matters: replacing a generating set by all words of length k with multiplicities creates parallel edges and is not automatically an ordinary simple Cayley graph. The companion paper *A remark about the spectral radius* removes this issue. Its Theorem 1 gives, for each finitely generated nonamenable group and every ?>0, a finite symmetric generating SET S with ?(S)<?. Its Corollary 9 explicitly states:

> Let ? be a finitely generated non-amenable group. Then the expected degree of FMSF(?,S) is unbounded when S varies among finite symmetric generating sets. In particular, the expected degree of FMSF(?,S) depends on S ...

Thus the question is fully answered even for ordinary generating sets, without appealing only to multigraphs.

## Complete deduction of dependence from the cited theorems

Fix any finitely generated nonamenable group ? and any finite symmetric generating set S0. Put d0=|S0|. Every realized FMSF is a subgraph of its Cayley graph, so its degree at the identity is at most d0, and consequently ?(S0)?d0.

Choose ?<1/(4d0+1). By the spectral-radius theorem there is a finite symmetric generating set S with ?(S)<?. By the FMSF lower bound,

    ?(S) ? 1/(4?(S)) ? 1/4 > d0 ? ?(S0).

This supplies two Cayley graphs of the SAME group with rigorously different expected FMSF degrees. More generally, taking ?<1/(4M+1) proves ?(S)>M for any M>0. All the deep inputs here are published theorems, not conjectures.

If an identity element occurs in S, it can be removed without increasing the spectral radius. Indeed, writing m(S)=pI+(1?p)m(T), T=S\{1}, positivity of the random-walk kernel gives ||m(S)||=p+(1?p)||m(T)||. To justify this norm identity, for a self-adjoint operator with nonnegative matrix entries, |<Af,f>|?<A|f|,|f|>, so its norm equals the supremum of its positive Rayleigh quotients; adding pI then gives the displayed formula. Hence ||m(T)||?||m(S)||. T still generates ? and is symmetric. There are no multiplicities, so its Cayley graph is loopless and has no parallel edges. In any event Corollary 9 already states the ordinary-set conclusion.

For a concrete group choice, ?=F2 with its standard four-element symmetric generating set has Cayley graph a 4-regular tree. There are no finite cycles, so no edge is deleted and ?=4. Applying the two cited theorems with ?<1/17 produces an ordinary generating set of F2 with ?>4. This is an existence counterexample supported by published theorems; no explicit list of the second generating set is asserted.

## Boundary cases

For infinite amenable groups there is no dependence: LPS's proof of Corollary 3.24 states that FMSF=WMSF in the amenable case and that their expected degrees are 2. This is a cited result, not an inference from nonamenability alone.

For a finite group of size N, continuous iid labels are pairwise distinct almost surely. The finite-cycle rule yields the unique minimum spanning tree. For completeness it is connected: if it had two components, the least-label edge across a component cut could not have been removed, since every alternate path across that cut contains a strictly larger edge. It is acyclic by the cycle deletion rule. Every finite tree on N vertices has N?1 edges, so the sum of its degrees is 2(N?1). Cayley automorphisms preserve the iid-label law, hence every vertex has the same expected degree; averaging gives 2?2/N for every generating set. For N=1 it is 0. This also explains why the supplied infinite-group FSF formula should not be applied without qualification to finite groups.

## Referee checks and remaining gap

- Exact source and locator checked in the fetched PDF (Question 6.13, PDF p. 27).
- Lower bound checked in the full Thom PDF (Theorem 1); its proof uses a union bound over simple cycles with the random-walk path-count bound, not any independence between cycle events.
- Nonamenability assumption checked: it is required for arbitrarily small spectral radius; the answer is not claimed for amenable groups.
- Multisets versus sets checked explicitly using the SECOND primary source: Corollary 9, PDF p. 5. This eliminates the principal scope failure.
- Strict inequality checked algebraically: ?<1/(4d0+1) implies 1/(4?)?1/4>d0.
- Expected degree and number of components are different quantities; nothing about connectivity is inferred here.
- Publication identity and Combinatorica metadata checked against Crossref; Semantic Scholar source citations independently contain the resolving paper.
- OpenAlex was rate-limited; no successful result is claimed for that service.

Remaining mathematical gap: NONE for Question 6.13. No original research attempt, numerical experiment, or Lean check is needed after the literature-resolution branch instructed by the user. The published inputs are cited rather than represented as newly formalized or independently proved in full here.
