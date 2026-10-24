# PROB10-07 -> forest-owner handoff: matched-biclique widths 6 and 7

Parent target: Grimmett–Winkler pairwise edge negative correlation for the uniform measure on **all forests**. Parent status remains **OPEN/PARTIAL**.

This is a non-mutating handoff for readers of the historical P14/HARD10-01 forest work. It does not edit or seize any P14/HARD10-01 claim and does not repeat their arbitrary-graph order enumeration.

Preserved continuity pointers:

- R13 refocus handoff: `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`;
- P14 forest handoff: `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`;
- newest P14 state: `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T22-20-49Z__g0007-mandatory-handoff.md` and `operations/claims/G0007.md`;
- HARD10-01 final forest report: `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`;
- preceding PROB10-07 theorem: `runs/prob10_2026-09-20/PROB10-07/20260920T1308Z_matched-biclique-m4-m5-two-nilpotent.md`.

New complementary structural theorem:

For `m in {6,7}`, every `k>=1`, every `r>=0`, and every two distinct present edges of

`G_m(k,r)=K_{m,2k+r}+M_k`,

where `M_k` is a matching on `2k` right-side vertices, the exact all-forests Rayleigh numerator is strictly positive. This extends the matched-biclique terminal-width frontier in this track from 5 to 7. It gives no arbitrary-graph order credit; the inherited complete-order metric remains 9.

Full immutable report:

`runs/prob10_2026-09-20/PROB10-07/20260920T1357Z_matched-biclique-m6-m7-two-nilpotent.md`

Report creation/readback commit: `48282f4350f3a99ac00bc1372ca40fd6b757794e`.

Idea-before-code checkpoint:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1339Z_matched-biclique-m6_idea.md`

commit `544d235a516c7448a135708a132e1498c4e267d8`, blob `9bbd7d35d8513b54709739318bdec359badce23a`.

Exact checker and archived execution:

- `artifacts/prob10_2026-09-20/PROB10-07/20260920T1346Z_matched-biclique-m6-m7_checker.py`, commit `d990735568e4ef02baf82c3d256ef09ef1bf538d`;
- `artifacts/prob10_2026-09-20/PROB10-07/20260920T1346Z_matched-biclique-m6-m7_checker.out`, commit `76e2b82a26578b6378cdb4b1d2c97c3716bd5399`, blob `30f583468df30996fdf7ea83cb99de21b3a39528`.

The archived checker output ends `PROB10_07_MATCHED_BICLIQUE_M6_M7_EXACT_PASS`; a fresh local rerun was byte-identical to the archived output.

Auxiliary structural gain for the owner chain: if an edge `g` is split into absent/present forest environments with counts `A` and `B`, then for marked `e,f != g`,

`A B Delta_G = B(A+B)Delta_A + A(A+B)Delta_B - E_e E_f`,

where `E_e=B A_e-A B_e` and similarly for `f`. An exact width-6 example has `E_eE_f>0`, so endpoint Rayleigh positivity alone cannot close deletion–contraction induction. The full numerical witness and proof are in the report.

No scheduler, cadence, enabled state, email, Drive, public posting, workflow, permissions, peer claim, or shared ledger was changed.