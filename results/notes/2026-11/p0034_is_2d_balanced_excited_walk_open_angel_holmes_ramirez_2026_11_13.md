---
name: p0034_is_2d_balanced_excited_walk_open_angel_holmes_ramirez_2026_11_13
description: "[PROVISIONAL] P0034 (Lyons-Peres Q2.27, horizontal-new vertical-old walk on Z^2, rank 1 of the 200) is the 2D balanced excited random walk with axes swapped; still open: Angel-Holmes-Ramirez AoP 2023 prove a 0-1 law and range bounds, recurrence only conjectured"
metadata:
  type: project
status: provisional
---
P0034 on the 200 list (Lyons-Peres Question 2.27: step horizontally after a first visit, vertically after a repeat visit, is the walk recurrent on Z^2) is, after a 90 degree rotation, the balanced excited random walk (BERW) of Benjamini-Kozma-Schapira: vertical step on the first departure from a site, horizontal afterwards.

Literature as of 13 Nov 2026 (two web searches, abstracts read, papers not read in full):
- O. Angel, M. Holmes, A. F. Ramirez, Balanced excited random walk in two dimensions, Ann. Probab. 51(4) (2023), doi 10.1214/23-AOP1622, arXiv 2110.15889. Theorem 1.1: the set of sites visited infinitely often is a.s. empty or all of Z^2 (0-1 law); upper and lower range bounds. They CONJECTURE recurrence. So the problem is open.
- Benjamini-Kozma-Schapira: transience of the analogous model in Z^4 (Peres-Popov-Sousi: d>=3).
- S. Qin, arXiv 2609.30045 (Sep 2026): recurrence and range (pi n / log n) for M(2,1,2) - horizontal on first departure, planar SRW step afterwards. A different model: the later steps are not purely vertical. A method lead, not a solution.
- Horizontal-vertical walks with random resampled labels (AIHP 59(2), doi 10.1214/22-AIHP1277): recurrence for resampling probability in (1/3,1].

Our only attempt (6 Sep, codex_20h, P0034-A001: both coordinates martingales, E|X_n|^2 = n) did not cite AHR 2023. Any write-up on P0034 must cite AHR 2023, BKS, Peres-Popov-Sousi and Qin 2026.

**How to apply:** before attempting P0034, read AHR 2023 sections on the range bounds and Qin 2609.30045's recurrence argument; the honest target is either recurrence (the open conjecture) or a sharper range bound. Related: [[a_problem_is_not_open_until_the_literature_says_so]].

Update 13 Nov 12:48 (Qin abstract read): Qin 2609.30045 proves M(2,1,2) recurrent with range pi n/log n, and more generally recurrence when the total positive and negative cookie strengths per vertex are bounded by A, B with A+B < 1 + 1/(2 pi + 1). P0034 is outside that theorem: every later step is purely vertical, so the deviation from planar SRW never runs out (unbounded total strength per vertex). Qin's method would need a new idea to reach P0034; not a short route. Rated: leave P0034 unless a new idea appears.
