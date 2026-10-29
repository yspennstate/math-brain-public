# Planar first-passage percolation: the block-chaos route to sublinear variance (9-22 Aug 2026)

The working files of a two-week attempt on the variance of the passage time in planar lattice
first-passage percolation, the question whether Var(T(0, n e_1)) is O(n^{1-eps}) and, beyond it,
whether the fluctuation exponent is chi = 1/3. Neither is settled here. What the files do contain is
a set of refereed partial results and two errata to a recent preprint.

`VERIFIED_CLAIMS_LEDGER.md` lists every assertion with its status (PROVED, CORRECTLY DEDUCED,
REFEREED, MEASURED, HEURISTIC, WITHDRAWN, OPEN) and the file that carries it. The main entries:

- A lattice version of the block-chaos engine inequality, Var <= kappa A2 + sqrt(A4 Pbar) on Z^2,
  with a conditional halving step Var(X_Mn) <= (1/2) M Var(X_n) under hypotheses (M1), (M2), (CH)
  (`problem/MG2B_framework_lemma_draft.md`).
- The occupation lemma: the number of geodesic edges in a box is at most (b/a) times its diameter,
  tight at a = b (`problem/CRUX_iteration_arithmetic.md`, section 5).
- Theorem A: hypotheses H1-H4 with (M1)-(M3) and (CH) give Var(X_n) = O(n^{1-eps}).
- Two errata to arXiv 2604.01214: the printed bound E[G^2] >= 2E[H^2] is false as stated, and display
  (14) carries a factor-2 inconsistency whose endpoint survives through the sharp inequality.
- The wall: with today's unconditional inputs the chaos strength the route needs falls short by about
  n^2 / log^4 n (`problem/CRUX9_wall_referee_20260812.md` and the W2 report).
- Envelope-variance pinning (alpha = chi exactly within the hypothesis set), the splitting lemma for
  the one-wall deficit, and the corner route with its conditional threshold alpha > 1/3.

Referee reports sit next to the drafts they judge (`REFEREE*_report.md`, `*_REFEREE_*.md`) with
their check scripts and outputs. Script output files are named in the text where a scratch file was
used; the seeds are given, so each run can be repeated.

A later campaign on a related problem is in
`results/open-problems/probability_1000/sharp_rademacher_campaign_2026_08_18`.
