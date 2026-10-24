# Probability candidates and current evidence

Date: 2026-09-30. Bounded literature and repository search; no claim to exhaustive novelty clearance. This separates famous long-term targets from the lower-profile source problem that presently offers the strongest verifiable completion route.

## Ranking for this research continuation

1. **Hasebe–Ueda Problem 3.11: best immediate rigorous deliverable, lower-profile than FEI.** Does a non-Dirac probability measure preserve unimodality under free convolution with every unimodal probability measure? [Primary paper, Section 3.3](https://arxiv.org/html/1710.08240). The September 14 campaign summary is stale: September 16 reports R08 C005/C006 contain a full arbitrary-law candidate. This continuation reconstructs and audits it, repairs two analytic exposition gaps, and improves its fixed witness to (1/32)δ0+(31/32)U(0,1). See FREE_UNIMODALITY_RECONSTRUCTION.md. A complete proof reconstruction is substantially more promising than starting a famous conjecture from scratch, but must not be presented as newly discovering the already-recorded classification. Searches of exact terminology and the authors' later primary papers did not locate a published additive classification; that absence is not proof of novelty.

2. **Friedgut–Kalai Fourier entropy–influence: highest-priority famous target with a large relevant repository base.** For every Boolean f on every uniform finite cube, is there one finite universal C such that H(f̂²)≤CΣ_S|S|f̂(S)²? Entropy is in bits. [González–MacManus–Pereyra, 2026](https://arxiv.org/abs/2606.00246) continues to pose the unrestricted statement. The repo has substantial restricted-class theorems, exact counterexamples to shortcuts, and hereditary/restriction reductions, but no finite unrestricted C. The strongest next step is a genuine universal payment or decomposition theorem, not another finite enumeration or a renamed remainder equivalent to FEI.

3. **Benjamini–Schramm nonuniqueness: famous probability target, lower immediate tractability.** For an infinite connected locally finite quasi-transitive nonamenable graph G, prove p_c(G)<p_u(G). [Chatterjee et al., September 2026, Section 3.2](https://arxiv.org/html/2609.11845v1) explicitly records the missing general direction of the original 1996 conjecture. The existing [June repository attempt](https://github.com/yspennstate/math-open-problems/blob/master/probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/README.md) targets the stronger operator inequality p_c<p_{2→2}; its reductions do not establish it. No full proof is produced in this continuation. A usable target must retain nonamenability and quasi-transitivity throughout; arbitrary-graph examples or local tube estimates do not supply the needed global operator control.

4. **Janson Problem 18.40: reserve target with a concrete failed-proof lesson.** In weighted random allocations with m/n→λ>ν=0, can the largest box satisfy Y_(1)/n→0 in probability along the full sequence? [Primary source, Problem 18.40](https://arxiv.org/html/1112.0510). The [repository review](https://github.com/yspennstate/math-open-problems/blob/master/probability_campaign_2026_09/REVIEW_B.md) invalidated an attempted universal concentration argument because it ignored mixing entropy; the stronger statement that all balls occupy one box fails for dense weights such as w_k=k!. That failure does not settle the source's weaker question. This pass does not claim a repaired full proof, and its later-literature check is less comprehensive than the selected free-unimodality audit.

## FEI: concrete full-scope attempt and exact stopping point

The [existing erasure correction](https://github.com/yspennstate/math-open-problems/blob/master/research_pushes/2026-09-18-sidorenko-fei-ising/FEI.md) must remain in the active dependency set. If B(f)=Σ_i H(S_i|S_-i), the claim H(f)≤B(f)+(2/ln2)I(f) is false. What survives is a universal implication: B(g)≤K I(g) for **every** Boolean g implies FEI with K+2/ln2. Restrictions of the current f matter; a pointwise B(f) cannot replace a hereditary bound.

The 265-variable parity-lifted addressing example has H=16, I=11/2, B=0. It contradicts the pointwise shortcut since ln2>56/81>11/16. Systematic coding of tensor powers further preserves arbitrary H/I ratios asymptotically while forcing every fixed-size spectral erasure entropy to vanish. Thus sparse spectral adjacency cannot be used as a universal certificate that a leaf is easy.

The [minor-child allocation theorem](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/P03-fei/runs/2026-09-20/2026-09-20T05-32-22%2B0300__fei-minor-child-allocation.md) gives a sharper surviving route:

    B_i(f) ≤ (2+1/(sqrt(e)ln2)) min(Inf_i(f),1-Inf_i(f))
             + min(I(f_i^+),I(f_i^-)).

On a stopping restriction tree, the unbounded candidate payment is L_T=Σ_v w_v min(I(f_v^+),I(f_v^-)). A heavy spine pays this load exactly once at each stopped minor leaf, but recursive use adds 2 to the inherited leaf FEI constant. Therefore simply recursing to constant leaves does not close a dimension-free theorem: the constant accumulates with recursive minor-branch depth. This continuation rejects that tempting full-proof step. What is still needed is an amortization/decomposition bound or a different potential that prevents repeated charges. No such bound is established here.

## Fresh exact-scope prior-art alert for FEI

[Vladimir N. Potapov, *On the Fourier Entropy–Influence Conjecture for Boolean Plateaued Functions*, arXiv:2609.21563v1, 18 September 2026](https://arxiv.org/html/2609.21563v1), Theorem 2, states H(f)≤4I(f) for all plateaued Boolean functions. Its normalized Walsh coefficients, squared-coefficient entropy in bits, and total influence agree with the repository after replacing a {0,1}-valued f by (-1)^f. Its plateaued condition |W_f|∈{0,2^((s-n)/2)} is exactly |f̂|∈{0,2^-k} with s=n-2k.

Thus the repository's September 20 plateaued constant-four corollary cannot be claimed as newly first established without a priority comparison. This observation does not disprove that corollary, resolve full FEI, or automatically cover its sharper finite-k bound, weighted pairing theorem, or affine-minimum refinements. Those require separate statement-by-statement comparison.

## Exclusions and integrity

- Already-posted Kalai/percolation entropy results and the distinct Hasebe–Ueda Problem 3.3 are not counted as new open-problem solutions.
- The explicitly retired Aldous–Fill diameter route is not reopened.
- No schedule, fleet assignment, original proof, peer artifact, or owner control is changed.
- Numerical checks certify only their stated finite algebra. Analytic proof review, source matching, novelty, and publication remain different evidence dimensions.
