---
name: fei23_two_path_reserve_reduced_to_log_moment_lemma_2026_11_09
description: "[PROVISIONAL] No (FEI23): two-path reserve reduced to log-moment lemma M<=1 (gives 5) or truncation CT (gives pi^2/2); proved one path; coupling open"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T05:08:36+04:00
  status: provisional
  evidence: "workers/FEI23/REPORT.md PROOF.md; rerun rc 0 identical certificates; frontier T021 f6f26c23df"
---

Is the two-path reserve inequality (FEI22 eq. 19) proved at small influence? No (FEI23, 9 Nov). It is reduced to one named lemma that is still open. Do not cite it as a proof of 5, of pi^2/2, or of FEI.

Write xi = W H^2 / i for the derivative-sector masses and tau = max(1, |G/H|) for the clipped ratios, where G, H and W are the root's exact sector coefficients. With M = sum xi ln tau there is an exact identity, 5i - Delta = i[2(1 - M) + R] with R >= 0. So the log-moment lemma LM, M <= 1, gives the constant 5. A stronger truncation lemma CT, sum xi min(tau, z) <= 1 + ln z for every z >= 1, gives pi^2/2 through the positive kernel -2 ln(1 - z^-2), with the empty-sector clipping loss written out. CT implies LM. Refuting either one alone does not refute Delta <= 5i.

CT is proved for a single selector path, by a piecewise staircase potential, and for independent-cofactor multiplexers; the second case covers the pure-AND side. The missing step is a coupled potential for two arbitrary staircases. The one-path potential does not carry over to the tensor product.

Finite evidence: 4,564 root pairs (the full FEI22 grid of 4,050, 512 frozen random dyadic pairs in both polarities, and 2 optimized witnesses), 1,215 of them below FEI22's threshold for 5. All pass CT and LM at every real z. The deficit is concave between exact breakpoints, so 12,666 breakpoint checks cover each pair. A bounded two-gate search made 29,904 evaluations and found no CT violation. Guards that caught errors: (x AND a) AND (x AND b) passes, but adding the one-path increments fails; pointwise Pareto tail domination is false for AND(7/8) followed by OR(1/8), while CT still holds there.

I reran it in a copy laid out like the fleet tree. certify_truncation.py, independent_audit.py and final_audit.py all gave rc 0, and the certificates are byte-identical (only timing fields differ). I also checked T = 2 ln 2 - (9/8) ln 3 = 0.1503555363682672.

Next: build a coupled staircase potential for LM or CT. The numerics in [[fei24_two_path_small_influence_no_counterexample_sup_pi2_over_2_2026_11_09]] point to pi^2/2; [[fei19_reserve_floor_pi2_over_2_2026_11_09]] is the lower bound.

Pushed to 06_math_research/frontier/T021/fei23_two_path_reserve_reduced_to_log_moment_lemma_2026_11_09 (f6f26c23df). GRID_CERTIFICATES.json (over 1.9 MB) stays local in workers/FEI23 for the offload sweep.

