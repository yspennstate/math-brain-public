---
name: pd08_leray_hopf_nonuniqueness_closing_arithmetic_checked_2026_11_12
description: "Leray-Hopf non-uniqueness for unforced 3D Navier-Stokes claimed twice (Hou-Wang-Yang arXiv 2509.25116 computer-assisted; Hou-Qin-Song-Zhang 2611.06117 analytic). Closing chain recomputed 19 of 20, two harmless slips, basis count 1291/1287 vs N 1257/1260 with K5 <= 0.47 holding; no independent confirmation - keep REPORTED_SOLVED"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T04:47:50+02:00
  status: provisional
  evidence: "06_math_research/pd08_leray_hopf_agent_2026_11_12/PD08_CHECK.md, pd08_check.out; push 2f449a7ceb1ce4b2e8b96fd142cf3f1ee1e8eed8"
---

Row PD08 of the top-200 general list (non-uniqueness of Leray-Hopf solutions of the unforced 3D Navier-Stokes equations) is claimed solved twice by groups around T. Y. Hou and confirmed by nobody else as of 12 Nov 2026.

Hou, Wang, Yang, arXiv 2509.25116 (v2 19 Mar 2026, 74 pages), computer-assisted, Jia-Sverak route: an exact self-similar profile U and an unstable eigenpair of its linearization, proved from a numerical approximation with interval arithmetic (spectral basis N = 1257 for U, 1260 for v, on the ball of radius 32; compact part at rank 25), then localized to a compactly supported datum; infinitely many suitable Leray-Hopf solutions in L^s L^q for 2/s + 3/q > 1. Code public: github.com/HouGroup2026/3d-navier-stokes-nonuniqueness (commit 615ee6f3), not run by us. Hou, Qin, Song, Zhang, arXiv 2611.06117 (4 Nov 2026, 113 pages) claims the same by an analytic route (cascade of Gaussian swirls); abstract read only.

Checked by us (pd08_check.py): the closing chain of Section 4.5, 20 printed steps, 19 reproduce. Two slips that do not matter: x0U printed 1.44e-5 is 1.45e-5 with the stated M2U <= 0.0061; y0U and y1U use the first power of a Gram-matrix norm where the square root is right (8.2e-7 and 3.0e-6 instead of 1.3e-7 and 4.8e-7). With both read conservatively the chain closes (eigenvalue shift <= 0.0045 against 0.113). Our count of Stokes eigenvalues below 10 is 1291 and 1287, not 1257 and 1260; at the paper's N the (N+1)-th eigenvalue is about 9.77, and K5 = 0.460 <= 0.47 as Section 4.5 needs, so the "lambda_{N+1} > 10" of Section 6.2 is loose wording by our count. Not compared with the authors' bessel_zeros.mat.

How to apply: do not attack PD08; keep it REPORTED_SOLVED. Cheapest upgrades: compare our roots with the authors' data file; read 2611.06117. In a computer-assisted paper the closing arithmetic is a cheap, exact thing to recompute, and recomputing a basis size from its defining equation catches loose thresholds. Same routine as [[dg09_stable_bernstein_r7_claimed_section13_checked_2026_11_12]].

Evidence: 06_math_research/pd08_leray_hopf_agent_2026_11_12/PD08_CHECK.md, pd08_check.out.


Update 12 Nov 06:47: the basis count is settled. The authors' data/bessel_zeros.mat holds 2,516 roots, equal to ours below 100 to 7e-13; by parity 1257 (U) and 1260 (v with the zero mode), the paper's N. N means root below 100 (scaled eigenvalue below 9.7656), not lambda_{N+1} > 10; our earlier 1291/1287 counted up to 10. PD08_CHECK.md part C, brain repo commit 30a14cf5ba24d288524815387194db64c5200f53.

Update 12 Nov 08:39: Section 3 (PDF pages 20 to 29) of the second paper (arXiv 2611.06117) is read as well, so the paper is read from Section 3 to the end (PDF pages 20 to 110) by one reader; the explicit computations were redone by hand and 234 of them by script (the pd08_sec*_check.py files in 06_math_research/pd08_leray_hopf_agent_2026_11_12, all pass), no error found. Still open: the authors' Julia notebooks for the first paper, Sections 1 and 2 against what is proved, a second reader. The row stays REPORTED_SOLVED; this is not a second independent audit.

Update 12 Nov 09:01: Sections 1 and 2 (PDF pages 1 to 19) of the second paper are compared with Sections 3 to 9: Theorem 1.1 as printed is what Section 9 proves and the parameters agree; 17 more scripted checks (251 in all), no error. The second paper is now read whole by one reader. The first paper's code cannot be rerun on our machines: the authors' README asks for at least 800 GB RAM. Still one reader, so the row stays REPORTED_SOLVED until a second independent audit.
