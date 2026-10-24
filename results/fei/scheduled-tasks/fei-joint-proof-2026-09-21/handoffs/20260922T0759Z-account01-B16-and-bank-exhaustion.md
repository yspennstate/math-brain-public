# account01/B16 FEI handoff — uniform AND-bank repair is exhausted

**Status:** `ESSENTIAL_STEP_APPLIED / SAME-CENTRE_UNIFORM-AND-BANK_REPAIR_REFUTED`; full FEI remains **OPEN / NOT PROVED**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Source-bound scientific report: `proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T0743Z-and-bank-exhaustion/REPORT.md` in private `yspennstate/math-open-problems`.

Consumed exact peers:
- account03/B12 `20260922T061544Z-biased-prime-candidate-refutation`: the composition-prime 18-input gate at `(3/8,1/2,...,1/2)` gives `D_{Gamma^dagger}<-0.0176114`, so `LIMIT-PRIME-GATE-LIFT-v1` is refuted.
- account02/B17 `20260922T071234Z-and-slack-rigidity`: a same-centre repair must spend AND slack; its previous finite chain only forced `K>0.2528769`, leaving the guaranteed bank `A=0.258204856` narrowly viable.

New exact theorem. For every symmetric perturbation `psi` with `psi(1/2)=0` satisfying

`q psi(p)+p psi(q)-psi(pq) >= -K p q (1-p)(1-q)` for all `p,q`,

the prime-witness repair functional obeys

`(57/256) psi(3/8)-psi(967/2048) <= kappa K`,

with exact

`kappa = 792001822391570453 / 11721234856636579840 = 0.06756982793012956...`.

Proof: a 35-term positive rational combination of actual AND inequalities telescopes *exactly* to the witness functional; the standard-library Fraction checker contains all pairs and multipliers. No continuity, boundedness, finite-grid extrapolation, or floating-point sign decision is used.

Since the exact witness deficit is `>0.0176114`, any such repair needs

`K > 0.2606400007146834... > 0.258204856 = A`.

Therefore the entire **uniform guaranteed** AND bank above the certified `0.01` read-once lift is insufficient for a same-centre repair. A viable same-centre replacement must exploit detailed nonuniform AND slack beyond `A M(p,q)` at some charged points (or else change the centre/base potential). This strengthens the peer's `>97.93%` result to `>100.943%` of the guaranteed bank.

Do not interpret this as a refutation of FEI or of every same-centre potential. The next exact target is the actual nonuniform AND-slack ledger for these 35 pairs, coupled to the prime witness constraint.
