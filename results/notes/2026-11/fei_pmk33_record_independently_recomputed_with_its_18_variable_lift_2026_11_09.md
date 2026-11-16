---
name: fei_pmk33_record_independently_recomputed_with_its_18_variable_lift_2026_11_09
description: "[VERIFIED] FEI record PM(K33) 6.5218457109 re-checked from scratch: counts, score and the gadget lift (18-var brute force) all agree; caveat: the score is H/(I-1), plain H/I is 3.32"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T05:29:27+02:00
  status: provisional
  evidence: ""
---

Rank 10 independent check, an agent, 9 Nov 2026, of the FEI loop's record (an agent; memory [[fei_pmk33_exact_because_level4_is_9_plus_9_equals_d_2026_11_09]]). Three scripts, none sharing the loop's code (its fano_19as.py mk(m) and gadget.py were read only for the definitions), in the private brain repository: 12_cognitive_architecture/top10_7_10_agent/:
- rank10_check_pmk33_counts_1109.py: |O| 247, majority 265, d 18, level table 0:34 1:63 2:72 3:78 4:18, top level 9 (|Z|=4) + 9 (|Z|=5); the loop's level (zeros alone in their row or column) equals sensitivity computed directly from f on all 265 points.
- rank10_check_pmk33_score_1109.py: direct character sums (no fast transform), own S selection and Kuhn matching: score 6.5218457109 to 10 digits; S = the 18 level-4 cells (exact, no tie-break); Parseval 0.96484375 = (N-d)/N; matching p 9, s1 0.
- rank10_check_pmk33_lift_1109.py: built the lifted Boolean function (9 grid variables + one fresh coin per matched pair = 18 variables, 262,144 points): balanced, H 6.7766053090, I 2.0390625, equal to the closed-form p/s1 terms to 1e-9.
Caveat (a flag, not a verdict): lean_score is H/(I-1). The lifted function's plain H/I is 3.3234. Whatever step turns H/(I-1) into an FEI lower bound (composition or a limit) was not checked here.
Scar: the workstation's default python finds numpy only without -s (user site); python -s gives ModuleNotFoundError.
Update 9 Nov 06:1x, the composition step (closes the caveat above): for balanced g, H(g o g) = H(g) + I(g) H(g) and I(g o g) = I(g)^2, so the k-fold composition has H_k/I_k = H(1+...+I^(k-1))/I^k -> H/(I-1) when I > 1. rank10_check_composition_1109.py builds g o g by brute force (Maj3 on 9 variables; three random balanced 4-bit g on 16 variables) and matches both identities exactly. With the lift's H and I the ratio is 6.52184 at k 20 and 6.5218457109 at k 40. So 6.5218 is a valid FEI lower bound by composition. Posted to the board review file, commit 90a8c47 on the private task board main.
Scar (posting to the board): the board publisher commits to main about once a minute, so a git fetch + push loop on this slow workstation lost three races in a row. The GitHub contents API (GET the file's sha, then PUT one file) landed on the second try, because it only conflicts with an edit to the same file. Script: put_board_file.py, and a copy beside the check files.
