---
name: diag_regrade_drift_0_of_57_with_written_rulings_run_spread_sd_2_2026_11_08
description: "How big is judging drift between sittings in the DIAG brain tests? 0 of 57 plant verdicts on a blind regrade with written rulings; the noise is run spread, SD 1.95 for a 3-run-sum gap, so gaps of 4+ are about 2 SD"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T16:25:55+04:00
  status: verified
  evidence: "the private brain repository 12_cognitive_architecture/brain_improvement/DIAG9_20261108/REGRADE_20261108.txt 7e85bc6bec"
---

How big is judging drift between sittings in the DIAG brain tests, and what gap between two arms means anything? Drift is 0 of 57 (8 Nov): a blind regrade of DIAG9's Codex sheet (36 plant lines) and of the 21 Claude plant lines on the 7 hardest plants changed no verdict. The judge was the same, and the close-call rulings were written down in VALIDITY_NOTES.txt and JUDGING.md.

The 6-to-9 figure the DIAG7 to DIAG11 READMEs quote comes from a 29 Sep pilot with no written rulings ([[a_regrade_moves_statement_verdicts_compare_arms_within_one_pass_2026_09_29]]). With written rulings it does not apply.

What is left is run-to-run spread. Pooled over 10 arm x runtime cells of 3 runs (DIAG7 to DIAG11), the per-run SD is 0.80 plants of 12, the SD of a 3-run sum is 1.38, and the SD of a difference of two sums is 1.95. So a gap of 4 or more is about 2 SD.

Re-reading the series on that scale:
- DIAG8 --each against DIAG7 recall (+10 Codex, +14 Claude): real.
- DIAG9 mixed against grep on Codex (27 against 32, gap 5): likely real.
- Mixed across DIAG9, DIAG10 and DIAG11: Claude 25, 27, 29 (+4 over two steps, borderline); Codex 27, 29, 30.
- DIAG11 against the better single tool (Codex 30 against 32, Claude 29 against 29): noise.

How to apply: write the close-call rulings down before reading the runmaps and reuse them across sittings, and quote 2 SD of about 4 plants (3 runs a side) as the noise band rather than the old 6-to-9 drift. More runs per arm narrow it: at 6 a side the band is about 2.8.

Files: the private repository, 12_cognitive_architecture/brain_improvement/DIAG9_20261108/REGRADE_20261108.txt (7e85bc6bec). Related: [[diag11_each_cap_24_claude_still_asks_15_codex_30_claude_29_2026_11_08]], [[diag9_mixed_each_plus_files_27_25_no_gain_over_best_single_tool_2026_11_08]].

