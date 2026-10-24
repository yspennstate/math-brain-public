# FOREST handoff — account04/B02 — 20260922T070653Z

Outcome: `CANDIDATE_REFUTED` for `FOREST-FULL-RADIUS-TRANSFER-HALL-v1`, and more strongly for any residual injection constrained to preserve both coordinate union and intersection. Parent FOREST target remains `OPEN`.

Canonical report: repository `yspennstate/math-open-problems`, path `proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B02/20260922T070653Z-account04-B02-forest-exchange-v4/report.md`, Git blob `536a2157ede22dbddcafeb4f1b28b308ac8222ff`.

Exact checker blob: `6cd5d65b1880ab4015016eee9579dadbaa90e640`. Captured output blob: `6abc63f471bf1e87deed9780e325c77b1e1ca8a4`.

Named other-account result consumed: account01/B03 run `20260922T052013Z-b03-forest-r11-d011c5`, report blob `d975b5c7b4257aee81eb4ee136b0cccce64b5033`, especially its full-radius reconnection existence lemma and proposed Hall/fiber-capacity upgrade. Latest complete team-lead version consumed: account01/B01 run `20260922T050946Z-b01-forest-auto11`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`.

Core counterexample: take `G=K4`, `e=01`, `f=23`, so `G0=C4` has edges `{02,03,12,13}`. Exact residual counts are `|N|=15`, `|A|=|B|=9`, `|D|=5`, cells `(n00,n10,n01,n11,q)=(4,2,2,7,2)`, and Rayleigh gap `Delta=6>0`. Thus the source inequality is true here.

For each base edge `g`, the left pair `(E(G0)\{g},{g})` belongs to `(N\A)xD`. These four pairs all have union `E(G0)` and empty intersection. Under the **entire** support of target pairs preserving both union and intersection, they have only two neighbors, namely the two ordered opposite-edge matching partitions. Hence Hall fails `4 -> 2` despite positive Rayleigh slack.

Directly for partner-style one-way transfers `F'=F\S`, `H'=H union S`, even allowing arbitrary nonempty `S subseteq F` with no path/radius restriction, the two left states `({03,12,13},{02})` and `({02,03,12},{13})` have the same unique target `({03,12},{02,13})`. Thus full-radius pointwise reconnection cannot be upgraded to Hall while staying transfer-only.

Required next mechanism: any successful exact injection must sometimes change coordinate union or intersection. A broader external-edge cut/join support (remove `k` edges from `F`, add `k` not-necessarily-identical edges to `H`) has an exact `30/30` matching on this K4 diagnostic, but no universal Hall theorem is claimed. Increasing radius inside the old transfer support cannot work.

Execution context remained `WITHOUT_VERIFIED_BRAIN`; no installation/benchmark work or production/private-data action was performed.
