# Proof attempt before experiments: rare controls and quadratic coupling

Goal: address a genuine dependency excluded from the previous jointly-independent-clause theorem. Introduce a fresh affine gate b(z)=1{z=0} on c>=4 bits and set G_c f=1-b(z)(1-f(y)). All monomials of the inherited Boolean phase now share the same gate. Prove a constant-independent-of-depth closure after arbitrary quadratic twisting and surjective affine changes, rather than assert unrestricted FEI.

Proposed exact formulas, to prove and test:
- p=2^-c, d=1-E f. Let I_lin(f) minimize sum_v alpha_f(v) over bases, without output-character folding. Then M(G_c f)=p[I_lin(f)+c d] for c>=2.
- H(G_c f)=p H(f)+2c(2pd-p^2d^2)+eta((1-pd)^2)-p eta((1-d)^2)+(p-p^2)eta(d^2), eta(t)=-t log2 t.
- Bound the final three terms by (1+2/ln2)pd. This implies preservation of H<=C M whenever C>=4+(1+2/ln2)/c.
- For ANY Boolean g with negative density delta<=1/8, prove M(g(-1)^Q)>=M(g)+(1/2-4delta)rank(B_Q), alongside the previously proved entropy increase <=rank(B_Q). If delta<=1/16 and C>=4, quadratic twisting preserves H<=C M.

Together, C=17/4+1/(2ln2)<5 should be retained under arbitrarily many independent four-bit controls, arbitrary quadratic twists at each controlled stage, disjoint products, and surjective affine changes/characters, starting from the proved constant-four seed class. The gate bits must be fresh; replacing them by dependent old variables is NOT covered.

Need distinguish the archived S05 conjunction-surplus work: that was a local L/(C+Q) bridge on disjoint factors, not the proposed exact affine-minimum identity plus non-disjoint quadratic coupling. Credit standard conjunction composition and old rank/coset lemmas. No full FEI bound or novelty certificate follows merely from this proposal.

Also examine tensor-amplified gated arbitrary f: the restricted test family stays FEI-hard when the ungated f is unconstrained, so density alone cannot close the global gap.
