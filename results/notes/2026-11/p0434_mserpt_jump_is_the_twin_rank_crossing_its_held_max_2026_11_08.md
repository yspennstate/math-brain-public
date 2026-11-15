---
name: p0434_mserpt_jump_is_the_twin_rank_crossing_its_held_max_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov: the M-SERPT jump at near-equal sizes is in the near twin residence and appears only once large classes lift its conditional remaining above its held rank max; a threshold in the large mass q, not a slope"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T05:40:00-05:00
  status: provisional
  evidence: "~/codex_fleet/runs/own_p0434/near_jump2.out, near_jump3.out, charge_limit2.out (8 Nov 05:0x-05:2x); research-repo codex-fleet fc025659"
---

Measured in ~/codex_fleet/runs/own_p0434 (near_jump2.out, near_jump3.out; NOTE.md 8 Nov 05:1x-05:2x; pushed to research-repo codex-fleet at fc025659).

Law 1, 338.27, 468.80 at rho 0.5, size 1 split into 1 and 1+1e-6: Gittins does not move, the large classes' Q and R do not move, and the small pair's M-SERPT Q goes 0.0634 -> 0.0677 and R 0.9902 -> 1.0583. M-SERPT's rank at the twin's left endpoint is 6.287 against 4.407 for the size-1 jobs, so for its last sliver of service the twin waits behind a busy period of newly arriving small work.

Falsifier: with no large class the split and merged T_MS agree to 8e-7 (the gap). With a large class of mass q the jump is +7.3e-2 at q 1e-2 and gone at q <= 1e-3, because the twin's conditional remaining q(338.27-1)/(p_twin+q) is 6.2 at q 1e-2 and 0.63 at q 1e-3, and the monotone rank moves only when the new value beats its held max 4.41. A threshold in q, not a slope.

So the positive size-cut prefixes are a residence charge priced by the large classes, consistent with charge_limit.out (the excess vanishes as q -> 0, ratio to Q_G(>k) at most 1e-2 on the laws tried). Refines [[p0434_prefix_lemmas_fail_because_mserpt_jumps_at_near_equal_sizes_2026_11_08]]; no earlier memory says this. Next: bound (busy period of rank-below work) x p_twin by the large classes' Gittins waiting.

Refines [[p0434_prefix_lemmas_fail_because_mserpt_jumps_at_near_equal_sizes_2026_11_08]]. Filed by direct write at 05:40 because brain.py remember timed out four times on the shared memory lock (05:1x-05:38); the index line is still owed.
