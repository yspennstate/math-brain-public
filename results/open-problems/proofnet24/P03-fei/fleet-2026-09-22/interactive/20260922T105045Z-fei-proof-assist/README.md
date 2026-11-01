# FEI proof assistance: five connected contributions

Date: 22 September 2026. Programme: **FEI-ALL-TEAM-20260922T095941Z**, control **2026-09-22.3**. This is an interactive research contribution, not an additional scheduled worker or a manufactured check-in.

**Full uniform-cube FEI remains open.** The target is a finite constant C independent of n and f such that H(f) <= C I(f) for every Boolean function on the uniform cube. The complete arguments below establish auxiliary results and scoped obstructions. They do not establish the remaining universal entropy payment.

## Results to use

| Contribution | Proved result | Remaining obligation |
|---|---|---|
| [Occurrence credit and phase](path_a/REPORT.md) | C_occ + P_phase is a nonnegative supermartingale under every uniform physical coordinate restriction. Expected increases of average child occurrence credit over any finite adaptive tree have one phase budget. An exact drift has six nonnegative terms. | Convert source-dependent drift or a state-dependent reserve into payment of the actual remaining entropy deficit. |
| [Physical entropy and phase refund](interference/REPORT.md) | The complete child-mixture information is paid by the phase correction. Explicit packet and influence-variation refunds telescope. A quadratic influence potential supplies an exact nonreusing variance conservation law. | Pay the conditional packet entropy, including its rare-event logarithm, on a genuine physical stopping tree. |
| [KL compression](rigidity/REPORT.md) | Preserve every singleton and use occupancy/amplitude bins on all higher levels. Fixed-width loss is at most kappa_q(I-1); level-adaptive bins lose at most (I-1)/q. Equal-influence spectra need O(q n log(n+1)) cells for the latter construction. | Prove a sufficient lower bound for the retained bin probabilities relative to their exact influence-matched reference. Small cell count does not prove this bound or polynomial computation. |
| [Multiscale reference](path_b/REPORT.md) | For disjoint iterates of a fixed balanced regular Boolean gate, one normalized hybrid reference recovers occurrence KL to additive epsilon I using O_g(1+log m+log(1/epsilon)) physical hierarchy levels. A quantitative necessity result explains the growing fine-scale cutoff. | Extend the source-valid hierarchy or its replacement to arbitrary composition-prime gates. |
| [Robust derivative structure](path_c/REPORT.md) | Mutual robust triggers form exact core cliques; one-way core masses increase by at least 16. Full ratio extremality yields linear physical child slack. On a trigger-independent selected family, terminality gives all capacitated Hall inequalities and a simultaneous fractional payment. | Pay query entropy and cover enough rows without reusing capacities across different families or states; handle the remaining singleton and nonrobust rows. |

Here C_occ means Var(f) times the KL divergence of the nonempty Fourier law from its occurrence-matched maximum-entropy law. P_phase is the existing sum of j(Inf_i), with j(t)=1-h_2(1/2+sqrt(t(1-t))). The reports define every normalization and endpoint case.

## A correction that should be consumed immediately

The proposed universal strengthened Bellman target D_Gamma - lambda C_occ >= 0 is false for **every fixed lambda > 0 and every finite potential center**. Recursive ternary majority gives a short exact obstruction: H=4(I-1), while C_occ >= (m-4)I+4 at depth m. Thus retaining a fixed positive fraction of that credit eventually demands more than any fixed-center balanced defect can supply.

The sparse one-point suspension gives a stronger simultaneous root-block obstruction, under the explicit additional assumption that the potential is valid on the AND/OR restriction children. Every nonempty physical root block then fails the proposed fixed-reserve local inequality for sufficiently large dimension.

This does not invalidate the signed Bellman identity, the proved supermartingale, lambda=0, state-dependent reserves, or FEI. The exact statements and two independent derivations of the positive credit bound are in [the occurrence-credit report](path_a/REPORT.md).

## Why the contributions fit together

The phase argument pays the Jensen-Shannon cost arising when actual child spectra are mixed. The occurrence-credit argument shows that this same cost bounds newly created dependence credit. Combining them gives a valid monotone quantity and an amortized budget without assuming the false monotonicity of occurrence credit alone.

The compression and hybrid-reference arguments retain high-level and rare-event information. They offer concrete alternatives to the refuted fixed-cardinality truncation and unweighted quadratic-energy routes. Their approximation errors are controlled; the universal lower bound needed to pay the FEI deficit is still missing.

The robust-clique argument supplies real child slack, and the Hall argument prevents double spending within a specified selected family. Their scope is deliberately explicit: a complement query can be expensive, and different families can share a capacity. These results are inputs to the stopping problem, not permission to discard those costs.

## Validation and provenance

Each report includes complete proofs and immutable links to the team results it uses. Adjacent checkers operate on genuine Boolean truth tables and exact integer Walsh data where applicable; entropy evaluations are numerical diagnostics, not universal computational proofs. The [independent reviews](reviews/) distinguish analytic review from executed checks. No formal proof-assistant verification or publication-level novelty determination is claimed.


## Prior work

The restriction and stopping-tree framework is part of the existing FEI literature, including González, MacManus and Pereyra, [Further evidence towards the Fourier Entropy-Influence conjecture](https://arxiv.org/abs/2606.00246), June 2026. The reports prove the additional accounting estimates they use and do not claim the underlying framework as new.

Potapov's September 2026 preprint [On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions](https://arxiv.org/abs/2609.21563) reports FEI for plateaued and partially bent classes. The flat-spectrum and exact-support observations here are not presented as new solutions of those classes. These references are a targeted overlap check, not a complete novelty search.
