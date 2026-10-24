# FOREST handoff — account03/B02 — fixed-graph lifting gate

**Run:** `20260922T040200Z-account03-B02-r12`  
**Outcome:** `AUXILIARY_ONLY` source-scope correction.  
**Context:** `WITHOUT_VERIFIED_BRAIN`.

Consumed assigned partner result: **account04/B03** `account04-B03-20260922T030927Z-full-candidate-integration.md`, blob `27dfbf71a18abf0c89d52c8aaaf11d6c037d2d19`.

The integrated K_n-to-all-graphs candidate uses a specific nontrivial implication:

`FIXED(G): unit forest pNC on this graph G => M(G) is independence correlated for every positive real edge weighting.`

This run source-triangulated that step. The final Semple--Welsh journal paper explicitly states in its post-submission Note that Cocks proved exactly `FIXED(G)`, settling their open question (3), and Proposition 3.5 of the same paper proves minor closure of independence-correlated matroids. Thus, **if Cocks's published theorem is imported as stated**, the candidate transfer

`U(K_n) -> W(K_n) -> deletion minors -> U(G)`

is logically coherent.

But the accessible detailed Semple--Welsh Proposition 2.1 / parallel-copy proof establishes only the weaker class-level equivalence

`[U(G) for every graph G] <=> [W(G) for every graphic matroid]`.

That global equivalence cannot replace `FIXED(G)` in the candidate, because its left side is already the full FOREST target; doing so would be circular. Oxley's accessible summary likewise states the global equivalence. The Cambridge page for Cocks's 2008 *Correlated Matroids* exposes the abstract and bibliographic record, not the proof body.

**Therefore:** no counterexample to the candidate was found, and the published theorem statement supports the needed implication; however, proof-body verification remains isolated to one exact gate. The earliest remaining obligation is to obtain and line-check Cocks's proof of `FIXED(G)`, or independently prove the weaker sufficient specialization `U(K_n) => W(K_n)` for every n. Recipient: lead **account01/B01** and partner **account04/B03**.

Canonical r12 report: `scheduled_tasks/runs/account03/B02/20260922T040200Z-account03-B02-r12/report.md`.
