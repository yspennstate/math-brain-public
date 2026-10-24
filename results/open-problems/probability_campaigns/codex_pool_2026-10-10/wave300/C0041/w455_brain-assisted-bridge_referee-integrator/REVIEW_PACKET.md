# C0041 referee packet — w455 — 2026-10-10

## Verdict and source

**Parent: FIX status, not KEEP proof.** Original source: Drewitz--Ramirez, arXiv:1309.2589v1, Open Question 2.20. A September 23, 2026 OpenAI preprint now claims the exact implication with a stronger deterministic vector limit. Local PDF SHA-256: `8b305d1fbb11b2a62d76f7decbc45accf5d1c02362937d0af5c4108dd0cc1411`. Formalization manifest identifies `OAI.DirectionalTransience.directional_transience_implies_ballisticity` in `lean/OAI/Probability/Ballisticity/Main.lean`; the comparator template's `sorry` is not the implementation. I have not built the implementation or checked `#print axioms`, nor audited the decisive estimate (5). No solved declaration from this packet.

## Narrow review requests

- **w458:** Independently check L01 in ATTEMPT.md and CLAIMS.jsonl. In particular verify `Q(n true boundary)=P_0(T_n<T_-1)`, the generating-function limit, and the first raw cycle versus conditioned iid cycles. Return KEEP/FIX/DROP with a counterexample or proof step. Also verify P04's manifest correction.
- **w453, w454:** Their artifacts subsequently arrived. PEER_AUDITS.jsonl records stepwise verdicts on w453 L1/L2/L3 and w454 001/002. Every bound checks as stated within its narrower assumptions. Neither provides the needed spatial tail from C0041. w453's r+1 box estimate is strictly sharper than w454's 2r+1 version; keep one mechanism in the brain.
- **formal referee:** Build the actual Lean implementation, print trusted axioms for the named headline theorem, inspect any sorry/admit/axiom in imported Ballisticity files, and compare the actual MainStatement to C0041. The comparator template is not a proof receipt.
- **paper referee:** Check Proposition 2.2 (integrable spatial radius), Proposition 2.5 (estimate (5) to duration mean), and Sections 3-8 proving (5), especially adaptive conditioning of shared environments. This is the outstanding parent gap.

## Reproduction

`python -X utf8 pdf_probe.py openai_directional_ballisticity_2026.pdf pages 2 3 10 11` shows theorem, roadmap, (5), and reduction. `python -X utf8 target_card_probe.py` reads the store with SQLite `mode=ro` and writes target_card_receipt.json. `python -X utf8 bounded_recall.py` writes recall_receipt.json with the 60-second gate. SOURCE_STATUS.json and CLAIMS.jsonl carry scoped claims and evidence.

## Submission states

L01: author proof saved, independent review pending, no theorem promotion. Preprint status concept: draft prepared for math-brain inbox; integration and retrievability require separate checks. Parent C0041: claimed resolved in public preprint, independent mathematical and formal checks pending.
