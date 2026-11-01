# P0043 referee packet — w437, 2026-10-10

## Source and parent status

Lyons–Peres, *Probability on Trees and Networks*, Conjecture 8.15 states: “If G is any quasi-transitive graph with p_c(G) < 1, then theta(p_c(G)) = 0.” The restriction p_c<1 is essential. The 2026-09-24 OpenAI preprint's Theorem 1.1 claims exactly the bond version for infinite connected locally finite quasi-transitive graphs. This changes P0043 from a safely open target to a **claimed solution requiring full referee certification**. The public comparator Lean file contains `sorry`; the separate `OAI/Probability/CriticalPercolation/Main.lean` solution module states the target theorem without a local `sorry`. I have not compiled or closed its import/axiom chain. No full parent-problem KEEP is issued here.

## Peer verdicts

**w435-L1 KEEP (auxiliary lemma).** Couple the critical configuration with independent Bernoulli r thinning. Each resulting edge is iid Bernoulli(p_c r), strictly below p_c for rational r<1. Therefore its probability of any infinite component is zero; integrating the conditional thinning probability and intersecting countably many rational r gives quenched threshold one for every infinite critical component. This relies only on the definition of p_c and conditional expectation; it does not settle whether such components exist.

**w435-L2 KEEP (auxiliary lemma).** For the normalized open-prefix mass Y_n, E Y_n=1 and E Y_n²=E_{mu×mu} r^{-k_n}≤I_r, since two n-edge prefixes have 2n-k_n distinct edges. Cauchy–Schwarz gives P(Y_n>0)≥1/I_r. Local finiteness and nested open-prefix events give an infinite path. This is an independent reproduction of the load-bearing second moment; no multiplication of conditional row probabilities is used.

**w435-L3 KEEP (method obstruction).** Tonelli gives E K=Σ_e a_e² and r^{-K}≥1+(r^{-1}-1)K. Signed expected ray traversals form unit flow f with |f_e|≤a_e. For each finite cut D_j, (Σ_D f_e)^2=1≤|D_j|Σ_D f_e². Disjoint cuts sum. On the square lattice the L1-ball cuts have 8j+4 edges, so Σ_j(8j+4)^{-1}=∞; the same upper bound on cut size holds for any subgraph that supports a ray. This is an obstruction to the ray-energy route, not to P0043.

**w435-L4 KEEP (special-case counterexample).** The generation size is 2^{n+floor(sqrt n)}. For p<1/2 its open-level expectation tends to zero. For the uniform ray measure, P(K≥n)=2^{-n-floor(sqrt n)} and E 2^K=1+(1/2)Σ_{k≥1}(2k+1)2^{-k}=7/2, giving critical root survival at least 2/7 by L2. The root is the unique degree-4 vertex; its fixed distance levels yield infinitely many orbits. Quasi-transitivity is absent.

**w435-G1 DROP as a proposed proof step.** Finite intersection energy for a hypothetical critical component is not derived. L3 shows no universal form can hold in recurrent square-lattice subgraphs. The L1 fragility result is fully compatible with critical survival on the non-quasi-transitive tree in L4. Hardest remaining gap for this route: a valid component-energy construction under suitable structural hypotheses, plus a separate recurrent case.

**w435-L5 KEEP (correction to C0084-A001).** For the d-regular tree, d≥3, p_c=1/(d-1). The number of depth-n vertices is d(d-1)^{n-1}; each is root-connected with probability p_c^n, so its expected open count is d/(d-1) at every n≥1. Tonelli yields infinite susceptibility at criticality, although critical Bin(d-1,1/(d-1)) Galton–Watson branches die out almost surely. The prior C0084-A001 row says the exponential-growth argument “show[s] that the susceptibility is finite at p_c in a spherically-averaged sense”; Hutchcroft's actual Theorem 6 assumes p<p_c. This is a source-backed correction of an inference, not a new general proof.

**w436-C0 KEEP (boundary case).** On Z every fixed ray has probability p^n of n consecutive open edges, so no infinite cluster for p<1 by countability; at p=1 all edges open. Hence p_c=1 and the excluded boundary can percolate.

**w436-C1 KEEP (special-case counterexample).** Write m(n)=1+floor(log2 n), M_n=E_{1/2}Z_n=4^{m(n)}. The conditional second-moment identity for independent offspring edges gives E Z_n²/M_n²=1+(1/2)Σ_{j≤n}1/M_j. The exact block sum is Σ_{k≥0}2^k/4^{k+1}=1/2, so the ratio is ≤5/4 and P(Z_n>0)≥4/5. Nested events and local finiteness give survival. For p<1/2, E_p Z_n≤4n²(2p)^n→0; the same argument from each vertex rules out all infinite clusters, hence p_c=1/2. The root has unique degree 8 and all its distance levels are distinct orbits, so the example lies outside P0043. This checks w436's hardest recurrence directly.

**w436-C2 KEEP (noninheritance counterexample).** On the C1 host tree, two independently sampled uniform-child rays share their first n edges with probability 1/(2^n 4^{m(n)}). Thus I_{1/2}=1+(1/2)Σ_n4^{-m(n)}=5/4. Critical root survival is ≥4/5, yet L1 gives quenched p_c(C)=1 for each surviving component; L2 then forbids finite I_r on such a component for every r<1. This independently checks the distinction between host energy and component energy.

**w436-C3 KEEP with source-status qualification.** The paper's Theorem 1.1 states the full target and the comparator challenge has `sorry`. The comparator is a statement stub: a distinct solution module, `OAI/Probability/CriticalPercolation/Main.lean`, states the target theorem with an actual proof body and no local `sorry`. Its imported closure and axioms remain unchecked here. The proper status is claimed solved, independently unverified; neither the old open label nor a fully certified solution is justified by this packet.

**w436-E1 FIX (relation kind).** The from card says “the root survives at criticality with probability at least 4/5” on the dyadic tree. The to card says the proposed host-to-component energy implication “is false without an additional structural premise.” The example supports that falsity, so the relation should be `proves`, not `refutes`. This is a semantic edge correction; both endpoint statements are supported.

**w436-E2 KEEP (relation).** The from card says surviving components “admit no ray measure with finite I_r for r<1”; the to card says “almost surely every infinite open component C ... has quenched bond threshold p_c(C)=1.” The first uses the second plus the checked open-prefix criterion, so `depends_on` is appropriate.

**w436-E3 KEEP (relation).** The from card says its dyadic tree “is not quasi-transitive”; the existing P0043 card asks about “G [that] is quasi-transitive and p_c(G)<1.” `semantic_association` accurately marks a boundary example, without asserting a counterexample to P0043.

## Independent check of the public preprint's delicate step

The preprint's Proposition 9.3 uses a conditional failure bound, not independence of site outcomes. If at each tested site the failure probability conditional on its full prior history is at most δ, then for any fixed finite set S, P(all S are tested and fail)≤δ^{|S|}: order their test slots, note that earlier specified failures and current tested status are measurable before the next test, and apply the tower property inductively. This validates the particular passage from (59) to (60), provided the paper's fresh-corridor conditional law and geometric separation hypotheses hold. I have **not** independently established Proposition 9.2, Lemma 9.1, or the nilpotent quotient construction; those are the outstanding load-bearing pieces before a parent KEEP.

## NEXT

Check Proposition 9.2's deterministic contact shell and its use of the joint-gluing inequality under the actual revealed sigma-field; request independent review of any new lemma before promotion.
