# FOREST B01 source/history closure addendum

This addendum is part of the immutable run record for `FOREST-KN-COCKS-RECONCILED-v3`; it supplements, and does not rewrite, canonical report blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`.

## Recovered P0001 / R02 dependencies

`operations/claims/P0001.md` fixes the exact outside target as Grimmett's 2022 Conjecture 4.2: uniform over all acyclic edge subsets of an arbitrary finite simple graph, prove pairwise negative correlation of distinct edge indicators. Its bounded source check records Grimmett--Winkler's finite verification and the 2026 Tang--Zhang complete-graph partial result; it explicitly warns that this is not a worldwide novelty certificate.

The recovered R02 run `runs/R02/20260918T0024Z_8c7d1e52.md` proves only a prior partial structural theorem: p-NC for graphs whose every nontrivial 2-connected block has cyclomatic number at most 6. It does so through Huang simplification, a minimum-degree/excess reduction, and an exact certificate on the 19 connected simple cubic graphs on 10 vertices. R02 explicitly leaves arbitrary finite graphs open. This result is compatible with, but not needed by, the present complete-graph/Cocks/minor chain; it is preserved as independent historical evidence rather than rederived.

## Current-source check performed in this run

A bounded 22 September 2026 literature search still surfaced the original Grimmett--Winkler conjecture, Semple--Welsh/Cocks, and partial newer results such as Tang--Zhang's March 2026 work on complete-graph spanning-subgraph families. No search miss is being used as a novelty claim. Priority/novelty remain unverified and require ordinary literature/expert review before external announcement.

## Source-exact comparison now used

The final Semple--Welsh paper states Proposition 3.5 (independence-correlated matroids are minor-closed) and, in its post-submission Note, records Cocks's stronger fixed-graph theorem: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. That later theorem is distinct from the older working-paper class-level parallel-copy mechanism criticized by fleet02/B02.

Hence the live end-to-end chain remains:

`all K_n unit p-NC (exact Hermite proof)`
`=> Cocks fixed-graph weighted independence correlation for M(K_n)`
`=> Semple--Welsh minor closure`
`=> arbitrary finite simple G by deleting nonedges from K_n`
`=> unit weights give the required uniform-forest inequality`.

This addendum does not change the internal classification: `FULL_PROOF_CANDIDATE`, with the same two independent existing-worker review passes and the same caution that the original Cocks full text was not directly read in this run.
