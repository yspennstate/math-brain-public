# FOREST handoff — account01/B01 — Cocks version reconciliation

Outcome: **ESSENTIAL_STEP_APPLIED**. Candidate `FOREST-KN-COCKS-REDUCTION-v2`. Parent target **not promoted** because the required two independent end-to-end reviews of v2 are not yet present. Context: `WITHOUT_VERIFIED_BRAIN`.

Named OTHER-account result consumed and answered: `account02/B02`, run `B02-20260922T013646Z-forest-r12`, especially `cocks_scope_correction.md`. I also consumed the later `account01/B03` source-gate refutation handoff. Both correctly identify that the **2005 Semple–Welsh working-paper** converse uses rational approximation and parallel copies and is only class-level. The new source check shows that this is not the final published dependency.

## Decisive source chronology

1. The **2005 working paper** states Proposition 2.1 as a class-level equivalence and proves the converse by replacing each edge by an integer number of parallel copies. This cannot establish `unit pNC on one fixed G => weighted pNC on M(G)`.
2. The **final 2008 Semple–Welsh paper changed Proposition 2.1**: it now states only the easy direction `all graphic matroids independence-correlated => Conjecture 1.1 for all graphs`. Proposition 3.5 proves weighted minor closure and explicitly notes that this alone does not show the unit-good graph class is minor-closed.
3. The **final published note** then records a later Cocks result in fixed-graph form: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated, settling their fixed-graph Question (3).
4. Cocks's published 2008 abstract says his paper extends Semple–Welsh, proves equivalences with correlated graphic matroids, and answers their open questions. Oxley's later text states the weaker class-level iff but does not contradict the fixed-graph theorem.

Thus the B02/B03 objection exposes an obsolete/pre-Cocks proof mechanism, but it does not refute the stronger graph-local theorem explicitly attributed to Cocks in the final peer-reviewed source. No accessible source found here states that the final attribution is false.

## Restored all-graphs chain

The lead exact Hermite theorem gives unit pNC for every `K_n`. Apply the published fixed-graph Cocks theorem to obtain that `M(K_n)` is independence correlated for all positive weights. By Semple–Welsh Proposition 3.5, every deletion minor is independence correlated. Every finite simple `G` on `n` vertices is obtained from `K_n` by deleting its nonedges, so `M(G)` is independence correlated; specialize all surviving weights to `1` to obtain the source uniform-all-forests pair inequality.

No contraction/minimal-counterexample argument is needed for this chain.

## Exact lead theorem audit retained

I independently re-expanded the Hermite reduction: with `s=k He_{k-1}(n+1)/He_k(n+1)`, the harder disjoint gap is proportional to

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`.

At the proved lower bound `L_n=(n-4)(n-1)(n+4)/(n+1)^3`,

`(n+1)^6 G_n(L_n)=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`,

whose shift `n=t+6` has coefficients

`2,142,3147,33233,187651,551661,666396`, all positive. Exact brute enumeration matched `K_3,...,K_6`, including disjoint gaps `6,210,13052` for `K_4,K_5,K_6`.

## Promotion gate

Do **not** auto-promote this to truth. The existing B02 audit passed the complete-graph mathematics but its global review predates this version-history reconciliation. A reviewer should now check exactly four items: Hermite theorem; final-vs-working-paper Semple–Welsh chronology; final fixed-graph Cocks attribution; Proposition 3.5 + deletion from `K_n`. Two independent existing-worker end-to-end PASS reviews are still required by owner control.

Canonical immutable scientific report:
`proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B01/20260922T010823Z-b01-forest-auto11/report.md`

Exact audit code/output are beside that report as `hermite_chain_audit.py` and `hermite_chain_audit.out`.
