# T238 moves on the obstruction

- 2026-10-16, literature (agent A): the window has to be a curve in (alpha, T); the one-step threshold (2205.01445) and the
  gamma field theory (2205.09653) are its two ends; heuristic window alpha ~ d^(ck) at n ~ d^k.
- 2026-10-31, result (agent B): target 2 for a quadratic student. With +- pairs the infinite-width dynamics close on the
  matrix flow P' = -(GP + PG), Q' = GQ + QG from c I, c proportional to alpha/d. Runs at d = 8-32, n = d^2/4
  (NOTE_quadratic_window.md, window.py, win_*.txt, win2_*.txt); the second pass withdrew the first pass's reading that the
  rich end moves down with d.
- 2026-11-04, audit (agent C): 34 runs with seed spread (AUDIT_agent_C.md). The lazy edge sits at c of order 0.1 at every
  d = 8-32. At fixed small c the share of the gap left grows with d (3.1 standard errors at c = 1e-3 without d = 8), so
  the rich edge drifts to larger c. At n = 2d (d = 8) some seeds never recover the teacher.
