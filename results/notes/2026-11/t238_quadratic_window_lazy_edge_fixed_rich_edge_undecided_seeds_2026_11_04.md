---
name: t238_quadratic_window_lazy_edge_fixed_rich_edge_undecided_seeds_2026_11_04
description: "T238 lazy-rich window (quadratic surrogate): lazy edge fixed in c across d; rich edge not shown fixed (share rises with d, seed sd shrinks); d=8 seeds fail to recover the teacher; README quoted picked seeds"
metadata:
  type: project
  created: 2026-11-04
  created_at: 2026-11-04T13:32:42+02:00
  status: verified
  evidence: "29 runs of window.py (11 source + 18 here), rank10_t238_tab.json; board 99b7e51"
---

T238 (top-400, lazy-to-rich window) second pass, research-repo 11e238fa, reviewed 4 Nov 2026 by an agent with 18 extra seeds of the source's own window.py (29 runs pooled, d = 8-32, n = d^2/4, c = 1e-3, 1e-2, 0.1).

- The lazy edge of the quadratic-surrogate window is fixed at c of order 0.1 for every d; that part holds across seeds.
- The rich side is NOT shown fixed: mean share at c = 1e-3 rises 0.59 -> 0.91 from d = 8 to 32 (slope +0.18 se 0.065 per doubling; +0.11 se 0.053 without d = 8). Seed sd shrinks 0.35 -> 0.02, so "seed spread as large as any trend" is only true at small d.
- At d = 8 (n = 2d) some seeds never recover the rank-one teacher at any c; the share then reads "lazy" for a reason unrelated to c. Small-d runs of this surrogate are confounded by identifiability, not window position.
- The README's "rich side better with d" numbers were picked seeds (seed 2 at d = 8 and 16); the claim survives in the median (rank correlation -0.39, p 0.04).
- Lesson for reviewing any seed-variance correction: re-run the source's script on more seeds, normalise every run the same way, and check whether the spread itself shrinks with the size parameter - a shrinking spread turns "noise as large as the trend" into a trend.

Row stays OPEN; the bridge from the matrix flow to the catalog's ReLU row is missing. Review: brain repo 12_cognitive_architecture/top10_7_10_agent/rank10_T238_review.md; board brain-tasks-board 99b7e51.


Update 4 Nov 15:4x (five more seeds: d = 24 seeds 5-6, d = 32 seeds 2-4; 34 runs): the rich edge is no longer undecided. Without d = 8 the share slope at c = 1e-3 is +0.108 per doubling (se 0.035, 3.1 se) and +0.108 (0.047) at 1e-2; d = 24 and 32 cells read 0.88 sd 0.02 and 0.91 sd 0.01 at c = 1e-3. So: lazy edge fixed in c = alpha/d, rich edge drifts to larger c as d grows. Caveat: all four d = 32, c = 1e-3 runs stopped at the step cap with train 2.9e-10 to 1.1e-9 (target 1e-10). Review addendum in rank10_T238_review.md.
