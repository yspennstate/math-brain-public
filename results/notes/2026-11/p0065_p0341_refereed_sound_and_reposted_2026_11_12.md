---
name: p0065_p0341_refereed_sound_and_reposted_2026_11_12
description: "P0341 occupation sums and P0065 harmonic dimension: Codex referee SOUND, fixes applied, re-posted 12 Nov"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T15:51:57+02:00
  status: verified
  evidence: "public commits f9e64f3 and b5bd8d7; ledger 92b692b4, 459d4388; brain d2420a01"
---

Two posted papers came back from blind GPT-6.1 referee passes (Codex on Mac mini 1, normal speed, one process, no outside documents) on 12 Nov 2026 and were re-posted the same afternoon.

P0341, harmonic-descent-occupation-sums (https://github.com/yspennstate/harmonic-descent-occupation-sums, commit f9e64f3): every numbered result SOUND. The referee checked every lemma in exact fractions on finite grids, Corollary 3.2 in 60-digit arithmetic at seven admissible points, the whole table, and derived the BCM bound quoted in Remark 2.6 itself. Its six fixes were presentational: the introduction's window-sum heuristic said "about (6/pi^2) 2^-j log n" where the fixed-j limit is (6/pi^2)(-log(1-2^-j)) log n (j=1 gives log 2, not 1/2); "for j>=2" at the block separation N_j/2 > N_{j-1}; notation rows split (epsilon/M, c/eta) and extended (p, f, B, theta, x, lambda_j). With seven new rows the notation table no longer fit on one page (Overfull vbox 80pt while output active); it is now a longtable.

P0065, harmonic-dimension-small-bias (https://github.com/yspennstate/harmonic-dimension-small-bias, commit b5bd8d7): SOUND, one wording error (the density of the tilted measure is E[W|T]/E[W]). The revision also states the pool estimator in full (seeds 1000-1005 coupled across lambda, +- = sd/sqrt 6), explains the 0.0018 gap between difference quotients and d_0' by curvature (about 0.01 m d_0''; d_0'' about 0.052 for the geometric law accounts for 0.0010 of it), puts Crossref-checked DOIs on all twelve references, and adds a notation appendix with one symbol per meaning (vertex x->v, ray eta vs increments theta_j, T'->tilde T, K->tilde N).

Ledger rows on open-problems-repo master: 92b692b4 (P0341), 459d4388 (P0065). Reports, referee scripts and the Codex log: brain 06_math_research/referee_reports/2026-11-12/P0065 and /P0341 (d2420a01).

What to carry: a referee SOUND verdict still leaves presentational fixes, and a fix that adds notation rows can push a tabular past the page; read the log for "Overfull \vbox ... while \output is active" after any appendix change. pw1k lint flags `\big|_{x=0}` (an evaluation bar, correct) and E_n[Z] as "[n] undefined"; both are false positives.

