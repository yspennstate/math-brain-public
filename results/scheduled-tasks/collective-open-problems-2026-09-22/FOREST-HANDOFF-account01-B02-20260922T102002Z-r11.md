# FOREST handoff — account01/B02 — 20260922T102002Z-b02-forest-r11

Outcome: `CANDIDATE_REFUTED`; parent FOREST remains `OPEN`; execution `WITHOUT_VERIFIED_BRAIN`.

Named OTHER-account result applied: account02/B03 `20260922T094532Z-b03-forest-auto11` proves exact simple-unit response-2 two-terminal networks require >=7 edges and >=5 vertices, killing local STAR-2 unitization as an edge-minimality step.

New exact no-go: a forest-pair injection cannot in general preserve both `I=A∩B` and `U=A∪B`. On `K4` with opposite marks `e=01,f=23`, global forest counts are `(00,01,10,11)=(15,9,9,5)` and the Rayleigh gap is `6`, but the fixed fiber `I=∅, U=E(K4)` has source count `|00×11|_fiber=4` and target count `|10×01|_fiber=2`. Its signed contribution is `-2`; eight other fibers contribute `+1` each. Therefore cross-fiber transport is mathematically necessary, not merely a tie-breaking issue.

Source-valid connected conditional realization: `H` on vertices `0,...,5` with edges `{02,03,04,15,23,25,35}`, terminals `u=0,v=1`, marks `e=02,f=35`. The terminals have no common neighbor. The `u-v`-disconnected forest counts are `(30,18,18,10)`, gap `24`; the fiber `I=∅, U=E(H)-{04}` is exactly the K4 obstruction after identifying `0~1`, again `4` source versus `2` target. Explicit source: `A={03,15,23}`, `B={02,25,35}`. Adding `g=01` gives a simple parent with forest counts `(62,42,42,26)` and gap `152`.

Combined with the account02/B03 local-unitizer lower bound, the viable mechanism is now sharply constrained: it must be **parent-specific and cross-fiber**. Universal terminal replacement and union/intersection-preserving recoloring are both ruled out.

First missing implication: construct a bounded-multiplicity cross-fiber charge `D00×D11 -> D10×D01` in the lead's relevant minimal-parent class, explicitly allowing an unmarked edge to change pair multiplicity. The K4 `-2 + 8*(+1)` decomposition is the smallest exact regression target for any proposed rule.

Canonical report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B02/20260922T102002Z-b02-forest-r11/report.md`.
Checker/output: `fiber_counterexample_check.py` / `.out`, ending `STATUS=PASS`.
