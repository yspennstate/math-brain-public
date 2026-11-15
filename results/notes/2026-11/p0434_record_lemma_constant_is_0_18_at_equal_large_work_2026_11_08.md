---
name: p0434_record_lemma_constant_is_0_18_at_equal_large_work_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov: the record-lemma constant (small-class excess over the large classes' Gittins waiting at an M-SERPT record) is 0.180, an interior max at equal large-class work; needs < 1"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T06:41:32-05:00
  evidence: "own_p0434 limit_fine.out, commit 869a193a"
  status: superseded
  superseded_by: p0434_record_lemma_constant_grows_with_the_number_of_large_classes_2026_11_08
---

P0434 (M-SERPT against Gittins), 8 Nov 2026. The M-SERPT failure of the prefix lemmas is a record event: a near twin's SERPT value passes the running max (see [[p0434_mserpt_jump_is_the_twin_rank_crossing_its_held_max_2026_11_08]]). The repair is a charge: at a record, the small classes' excess D_0 + D_1 (D = Q_MS + R_MS - R_G - 2Q_G) is at most theta times the summed Gittins waiting Q_G of the large classes above the record.

Measured on the family (1, 1+g, K1, K2), large mass bisected to the record: the sup of theta is 0.180 (three digits, 0.1802). It is an interior maximum reached in the limit rho -> 0, sizes -> infinity, K2/K1 -> infinity, at small split a = 0.38 and c = (1 - w) K2/K1 = 1, i.e. the two large classes carry equal work. It is unchanged at rho 0.001 and K1 1e6 and falls on every side (0.140 at c 0.3, 0.144 at c 3). One large class gives 0.090; a third large class seeded from the optimum gave 0.1739, not more. The charge needs theta < 1, so the margin is more than five.

Two cautions from getting here. Grid values understated it twice: 0.087 and 0.119 were grid or box-edge values before the box was widened (rho down to 0.01, spread uncapped). Numbers here are numerical, not proved; a closed form in the first-order-in-rho limit is the next check.

Evidence: ~/codex_fleet/runs/own_p0434/ record_sweep*.out, theta_opt2-4.out, limit_scan.out, limit_max.out, limit_fine.out and NOTE.md sections 05:5x to 06:4x; research-repo codex-fleet commit 869a193a.

