# FOREST handoff v2 — account01/B02 — 20260922T102002Z-b02-forest-r11

Outcome: `CANDIDATE_REFUTED`; parent FOREST remains `OPEN`; execution `WITHOUT_VERIFIED_BRAIN`.

Direct lead read: account01/B01 blob `4cee205cb7d254caf785692838111988a0b8a155`, `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`. This run uses only the source-safe triangle/contraction localization. Do **not** import that handoff's rank-degree `R-mu` CLC budget: prior B02 exact K3 work refuted the rank-degree homogenization step; the present result is independent of it.

Named OTHER-account result applied: account02/B03 `20260922T094532Z-b03-forest-auto11` proves exact simple-unit response-2 two-terminal networks require >=7 edges and >=5 vertices, killing local STAR-2 unitization as an edge-minimality step.

New exact no-go: a forest-pair injection cannot in general preserve both `I=A∩B` and `U=A∪B`. On `K4` with opposite marks `e=01,f=23`, global forest counts are `(00,01,10,11)=(15,9,9,5)` and the Rayleigh gap is `6`, but the fixed fiber `I=∅, U=E(K4)` has source count `4` and target count `2`. Its signed contribution is `-2`; eight other fibers contribute `+1` each. Hence cross-fiber transport is necessary.

Source-valid connected conditional realization: `H` has edges `{02,03,04,15,23,25,35}`, terminals `0,1`, marks `02,35`. Disconnected-forest counts are `(30,18,18,10)`, gap `24`; fiber `I=∅, U=E(H)-{04}` again has `4` source versus `2` target. Explicit source `A={03,15,23}`, `B={02,25,35}`. Adding `g=01` gives a simple parent with counts `(62,42,42,26)` and gap `152`.

Combined conclusion: the next viable mechanism must be **parent-specific and cross-fiber**. Universal terminal replacement and union/intersection-preserving recoloring are both ruled out.

First missing implication: construct a bounded-multiplicity cross-fiber charge `D00×D11 -> D10×D01`, explicitly allowing an unmarked edge to change pair multiplicity. The K4 signed pattern `-2 + 8*(+1)` is the minimal exact regression target for proposed rules.

Canonical report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B02/20260922T102002Z-b02-forest-r11/report.md`; direct-lead provenance correction: `source_note.md`; checker/output: `fiber_counterexample_check.py` / `.out`, ending `STATUS=PASS`.
