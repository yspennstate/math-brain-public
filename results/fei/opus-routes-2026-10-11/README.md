# FEI supplementary obligations: Opus workflow (claude-51330238, 11 Oct 2026)

Set up on 11 Oct 2026 to support a team of Codex agents working on the full Fourier entropy-influence conjecture,
with every result and idea saved to the brain; this workflow ran up to 20 Opus agents beside them.

Split agreed with claude-2d8060eb (mesh msg-a05dccebae): it runs the 100 Codex agents on account 5, the B01-B20 streams and 20 Opus stream leads, and syncs their runs to math-open-problems. This workflow takes the supplementary obligations of research_pushes/2026-10-11-full-fei-100-agents/CAMPAIGN.md, each with an attacker and an independent referee, then a synthesis. claude-51330238 also owns all brain ingestion (FEI node tree, memories, math-brain store).

One folder per route: NOTES.md (all working, proofs, failed attempts with witnesses), CLAIMS.json, code/, data/, REFEREE.md. SYNTHESIS.md at the end. Full FEI remains OPEN unless a complete proof passes the campaign's independent review (B18, B19, B20).

NEXT 06:1x 12 Oct (claude-51330238): report for his 04:06 ask opened in Chrome, Downloads/fei_progress_report_2026-10-12.html
(built by scratchpad build_report.py from fei_stats.py counts). Referees: A2, U, BT confirmed (BT referee adds the anti-diagonal
tribes no-go for level-wise Gibbs references); SEL referee working; W attack still running (no referee yet); R, S, L, K lost at
00:29 to the network drop (relaunch is his call; Claude week ~80 pct, cap 85). When wf_39311c05-db6 ends: read SYNTHESIS.md and
the SEL/W referees, file memories, steer 2d8060eb (B20 route 1: Booleanity at |S| >= 1). Mesh: msg-3d23b7c732 to 2d8060eb
(fei100_sync fails on math-open-problems, fix suggested, no reply yet); msg-6a2b6fdf5c to 322bc92e (live FEI trees excluded from
save-then-delete - agreed 03:00Z; release them when the campaign or this workflow ends). Ingest loop pid 103860 keeps pushing hourly.
NEXT 06:5x 12 Oct: report corrected (W read-once half is O'Donnell-Tan composition + Theorem A; U novelty unchecked) and reopened in
Chrome. Memories filed: the_fei_sync_lost_every_push_to_one_file_commits_2026_10_12, an_fei_class_listed_as_new_was_read_once_2026_10_12.
Steering sent to 2d8060eb: msg-820e93ddbd (novelty pass, BT no-go for route 3, A2=A032, PP_q review), plus a note on two fei100.py copies.
His 05:53 order (verified in his prompt log): keep working on his tasks for 15 h (to ~20:53). Machine at 95 pct commit / <1 GB free at
06:4x: launch nothing large. Waiting on wf_39311c05-db6 (W attack, SEL referee, then SYNTHESIS) - its notification wakes me.
NEXT 16:39 12 Oct (claude-6bb7036b-s07, recovery stream): SYNTHESIS.md written (all routes, equivalent forms, the shared
obstruction, next targets). L2-level-two/ added (CLAIMS.json, NOTES.md, NEXT_s07.md): explicit per-level constants,
localization below half the log-influence, the gap reduction, obstructions O1-O5 and the tribes one-block witness.
NEXT 17:4x 12 Oct (claude-6bb7036b-s07): L2 sections 5b-5c. Read-once AND/OR/parity formulas: one integer, the height at
which S - i first reaches the branch of i, is an exact witness (L2-R2); a 43-function brute-force bench finds a scale-and-count
profile exact on every structured family but one, and X009 forces any witness bound to be paid on average over coordinates
(L2-GW-E). L2/CLAIMS.json now marks every self-checked proof CANDIDATE until another agent's adversarial pass.
NEXT 18:2x 12 Oct (claude-6bb7036b-s07): L2 section 5d, pivotal faces. P(A_i and A_j) = P(i, j in S), and Harper's
inequality on pivotal sets bounds the trivial witness cost of any set of coordinates by a spectral second moment (Proposition P3,
L2-PF; standard facts, not claimed new, and nothing is priced below the trivial cost). An unpredictable coordinate need not have a
subcube pivotal set (L2-PF-E). check_levels.py full run: 70,253 functions, 0 violations of eleven checks (L2 NOTES section 7).
NEXT 18:5x 12 Oct (claude-6bb7036b-s07): L2 section 5e, blocks with signed-character fibers (Lemma B, L2-SB): if every fiber
of F over an address block is a signed character, the data block costs sum_Y B_t <= H(S_Y) <= 2 I_X, sharp on AND powers, so
selectors, however many and however unpredictable, are never the obstruction on that class; the open part is the address
part, which is as hard as FEI. Elementary, not claimed new; code/selector_block.py and a second path code/audit_selector_block.py
(278,440 cases, no violation).
NEXT 19:0x 12 Oct (claude-6bb7036b-s07): Corollary K in L2 section 5e (L2-SB-K): if every monomial of the GF(2) polynomial
of f uses at most one variable per block of a K-block partition, then H <= 2(K - 1) I. K = 2 is the elementary quadratic case;
K >= 3 not searched in the literature, not claimed new. code/block_partite.py and code/audit_block_partite.py.
It does not reach tribes, AND/OR trees, balls or majority: their polynomials put every pair of coordinates in one
monomial, so K = n (code/partite_reach.py).
