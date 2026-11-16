---
name: t180_prophet_secretary_hardness_paper_posted_2026_11_03
description: T180 posted 3 Nov: prophet secretary constant < 0.72294 (461-item instance, interval DP certificate), repo prophet-secretary-hardness
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T04:22:12+02:00
  status: verified
  evidence: "public repo github.com/yspennstate/prophet-secretary-hardness 96a0b92; code/check_output.txt interval run; code/continuum_output.txt"
---

T180 posted 3 Nov 2026 (papers loop a checklist task, 6th of the top 10 on my count): github.com/yspennstate/prophet-secretary-hardness, head 96a0b92, public. Title "A prophet secretary instance with ratio below 0.7230". Index card in math-brain-public papers/README.md (01996a9ddb). PAPER_CANDIDATES.md row 6 marked POSTED.

Result: the prophet secretary constant alpha < 0.72294. Instance I(400,30) (461 items): 400 prizes worth 1 w.p. 1e-9; 30 items worth 1.28233*kq w.p. 0.2065/30; 30 worth 1.38487*kq w.p. 0.17698/30; one sure item 0.823*kq (kq = 4e-7). The ratio V/E max lies in [0.722933460012600477658647124, ...127]: count DP (770,722 states) in mpmath.iv at 100 bits, 153 s. Prior best 0.7235 (Giambartolomei-Mallmann-Trenn-Saona arXiv:2304.04024, the same order-unaware setting); Bubna-Chiplunkar 0.7254; Correa-Saona-Ziliotto sqrt3-1; best algorithm 0.688 (Chen-Huang-Li-Tang arXiv:2411.01191).

Paper layout: Lemma 2.1 (random-order recursion), Lemma 2.2 (count reduction for identical groups), E max closed form, the interval proof (arithmetic ops and max have valid interval extensions; by induction every state is enclosed), checks as a remark (subset DP n=11,15; q=1e-12 moves the ratio 7e-8), and a size table (k 100..800: 0.72340, 0.72308, 0.72293, 0.72286). Section 4 is the many-prize ODE, labelled heuristic and numerical. My own code/continuum.py (u = time remaining, solve_ivp DOP853) reproduces all six continuum values: sqrt3-1 with no medium items; 0.72348603 at GMS's parameters; 0.72302401 one value minimised; 0.72275062 at the I(k,m) parameters; 0.72274261 two values minimised; 0.72268397 three values minimised. The minimising parameters are from an agent's Nelder-Mead; I did not re-run the minimisation.

Before release: build 0 Overfull, no ??; paper_release_guard ok; the voice check flags only the byline; the scan of the stage finds nothing but the byline. Back matter is the same as the T362 paper.

What would change it: an earlier public bound below 0.7230 for single-item random order (a search on 3 Nov found none after v6 of 2304.04024), or an error in the count reduction (cross-checked only at n = 11 and 15).

Related: [[t180_461_item_instance_certified_by_interval_dp_2026_11_03]], [[prophet_secretary_hardness_below_0_7235_two_value_cloud_2026_11_03]], [[t362_rr_constant_step_log_factor_paper_posted_2026_11_02]].

