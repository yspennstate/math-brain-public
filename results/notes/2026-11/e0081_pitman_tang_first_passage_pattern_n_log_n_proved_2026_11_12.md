---
name: e0081_pitman_tang_first_passage_pattern_n_log_n_proved_2026_11_12
description: "[PROVISIONAL] Pitman-Tang first-passage pattern waiting time: order n log n proved (Peres conjecture) via record-time range bound; referee E0081AR pending"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T23:05:45+02:00
  status: verified
  evidence: ""
---

Pitman-Tang (arXiv 1411.0041) asked for the order of the expected waiting time E T_n until a simple random walk shows a
first-passage window of length n (net drop lambda sqrt n, endpoint the strict minimum of the window). Known: n to n^{5/4};
Peres conjectured n log n (Tang 2017 thesis Conj. 2.5.2).

Codex run E0081A (12 Nov) proves c n log n <= E T_n <= C n log n, and I checked every lemma by hand.
- Upper bound: the chance of a hit among the n/2 windows starting in [0, n/2] is at most C/log n. Split the walk into
  first half X, an independent middle increment B, and the continuation Y. A hit forces B into the set
  {X_s - Y_s : s a strict descending record of Y} shifted by a constant. That set has expected size <= sqrt n / log n:
  record times number about sqrt n, but by strong Markov at the first visit to each value z the walk revisits z on
  records G_L ~ log L/(2 pi) more times. B's point masses are <= C/sqrt n, so the hit probability is <= C/log n.
- Lower bound: given one hit with word w, a later hit at shift s needs w(s) < 0 and has conditional chance
  f_s(-w(s)) <= C/s, so the expected number of hits after the first is O(log n): first-success gives >= c/log n.
- Then the union over blocks of starting times gives the lower bound on E T_n, and independent blocks of length 3n/2
  give the upper bound.
Method worth reusing: range of a difference walk sampled at record times = (number of visits)/(return potential).

Open: the source's Table 1 (about 1.8 n) disagrees with the run's simulation (4.16 n at n=100, lambda=-1); convention
unresolved. Hard Codex referee E0081AR launched on worker machine 1, 13 Nov 01:04 +04. Archive: brain
06_math_research/referee_reports/2026-11-12/E0081A/. A paper waits for the referee and a literature search.



Update 13 Nov: refereed MINOR by an independent Codex referee (E0081AR, brain 06_math_research/referee_reports/2026-11-12/E0081AR). Lemmas 2-6 and the deduction hold. Fixes: (4) needs k integer; endpoint rounding (n=1000, lambda=-1 gives a=32); the source Table 1 values all sit below the exact lower bound 1/f_n(a), so that table is wrong (ending-time convention (2.4), cause otherwise unknown); credit source (2.21) for the overlap count; file paths. Paper handed to an agent (mesh topic referee/e0081). Ledger row in probability_1000_intake_E_20260908.

13 Nov (workstation 23:57): paper public at github.com/yspennstate/first-passage-pattern-waiting-time, HEAD e4c5ae2 (an agent, 7 pages, the five referee fixes applied; n=1000 row rerun at a=32: 4946.3, se 28.0). Ledger row public_commit e4c5ae2, current_status solved_paper_public (brain 267ea803). Zenodo and ResearchGate wait for the W43 audit after 17 Nov 01:00.
