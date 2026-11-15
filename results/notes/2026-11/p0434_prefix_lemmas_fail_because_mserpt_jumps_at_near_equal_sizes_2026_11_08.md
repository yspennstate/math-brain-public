---
name: p0434_prefix_lemmas_fail_because_mserpt_jumps_at_near_equal_sizes_2026_11_08
description: "P0434 8 Nov: the size-cut and valley prefix lemmas for T_MS <= 2Q_G+R_G are false; two near-equal sizes make M-SERPT jump 1.1 pct while Gittins stays continuous"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:53:35-05:00
  status: verified
  evidence: "~/codex_fleet/runs/own_p0434/near_law.out, near_jump.out, theta_hunt.out (8 Nov 03:5x); pushed to research-repo codex-fleet"
---

Law s (1, 1.00922, 338.27, 468.80), p (0.458, 0.532, 8.89e-3, 8.72e-4), rho 0.5: valley 0 = classes {0,1}, D/(2Q_G+R_G) = (-3.8e-3, +4.75e-3, -0.172, -0.017), so the first-valley prefix is +9.5e-4 > 0, while the whole-law ratio is 0.812. Stable for gaps 1e-1 to 1e-4 and rho 0.1 to 0.99 (codex_fleet/runs/own_p0434/near_law.out). Cause (near_jump.out): T_G 6.41928 merged and at gap 1e-6, T_MS 6.41986 merged vs 6.49231 split, all in R_MS. At age 1 the survivors' mean remaining is set by the big classes, so M-SERPT's running-max rank climbs and jobs one gap from done wait behind new work. Random draws (2,700 + 600 laws) never found it; a near-equal-size family in theta_hunt.py did on its first pass. Lesson: a lemma checked only on random laws can miss degenerate families where a policy is discontinuous; hunt them on purpose before building a proof on the lemma. Any class-by-class or valley-by-valley induction in size order fails; large classes must pay. Supersedes the prefix-lemma plan in [[p0434_heavy_traffic_reduces_to_a_staircase_hull_inequality_2026_11_08]] as a proof route.
