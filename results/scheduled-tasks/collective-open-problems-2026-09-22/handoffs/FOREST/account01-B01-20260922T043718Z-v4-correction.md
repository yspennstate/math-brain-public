# FOREST B01 handoff — fixed-Cocks bridge withdrawn

Run `20260922T043718Z-b01-forest-auto11`; outcome `CANDIDATE_REFUTED` **as written** for `FOREST-KN-COCKS-RECONCILED-v3`; parent FOREST remains open. Context `WITHOUT_VERIFIED_BRAIN`.

Canonical report: `yspennstate/math-open-problems/proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B01/20260922T043718Z-b01-forest-auto11/report.md`, creation commit `9fd91a5bd97a99ba6cf6dc3582d66d53c40faea1`.

## Decisive correction

The final Semple--Welsh Note literally says Cocks proved a fixed-graph upgrade `unit pNC on G => M(G) independence correlated`, but this reading is not source-secure. Erickson's 2008 thesis explicitly says the theorem published independently by Cocks is the **global** statement `all graphs I-negatively correlated => all graphs I-Rayleigh`, and its Corollary 5.2.3 proves exactly that through graphic substitutions. Oxley's 2011 *Matroid Theory* likewise credits Cocks with the class equivalence: graphic matroids are independence-correlated iff the unit conjecture holds for **all graphs**.

There is a strong consistency check: Stark proved unit pNC for `K_N` for all sufficiently large `N`. If the literal fixed-graph upgrade held in the strength used by v3, then Stark + weighted minor closure would immediately imply unit pNC for every finite simple graph by embedding an arbitrary graph into a sufficiently large complete graph and deleting nonedges. Current sources still list the all-graphs problem as open. Therefore the fixed-graph sentence cannot carry the lead proof fail-closed without the primary Cocks proof body or a new independent derivation.

## Exact replacement equivalence

For marked `e,f` in `K_n`, the following are equivalent:

1. every finite simple graph is unit forest pNC;
2. `Delta_{K_n}(e,f;y)>=0` for every `n,e,f` and every positive assignment to the unmarked edges;
3. every simple path-bundle expansion of every `K_n`, keeping `e,f` literal and replacing each unmarked edge `g` by `k_g` internally-disjoint length-`a_g>=2` paths, is unit pNC for the marked pair.

`1=>3` is immediate. `3=>2` is account04/B03's exact identity `Delta_H=C^2 Delta_K(q)` with `q_g=k_g/(2^{a_g}-1)` and density/continuity. `2=>1` sends nonedge weights to `epsilon->0+` in a complete supergraph. Thus "weighted K_n" is already equivalent to the whole target, not a small globalization lemma.

## Named peers applied

- account02/B02 correction blob `733d840093ca109d38f4e336d228ae1ddedf77c0`: vindicated on the scope issue.
- account04/B03 report blob `8812d4c9be5debaec40c02c2b13779bba8b62fae`: simple path-bundle identity supplies the exact replacement equivalence.
- fresh account04/B01 r13 two-cut algebra remains useful only up to its invocation of the same disputed fixed-graph Cocks step; its unconditional 3-connected conclusion is not accepted yet.

Preserve the exact complete-graph Hermite theorem and Semple--Welsh weighted minor closure. Withdraw prior v3 `FULL_PROOF_CANDIDATE` status pending primary-proof reconciliation or a genuinely new all-graphs argument. Do not count the two earlier v3 reviews as independent validation of this corrected source scope because both inherited the same fixed-graph interpretation.
