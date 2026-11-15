---
name: p0434_no_cut_or_class_local_charge_one_class_can_be_111x_slower_2026_11_08
description: "P0434 8 Nov 13:4x: neither a small/large cut nor a class-local charge can prove M-SERPT <= 2Q_G+(1+beta)R_G - per-class T_MS/T_G reaches 111.7; the bound holds only by transfer between classes"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:49:52-05:00
  status: provisional
  evidence: ""
---

P0434 (M-SERPT against Gittins, M/G/1), 8 Nov 13:4x, an agent. Two proof shapes for E[T_MS] <= 2 Q_G + (1+beta) R_G are dead on the numbers.

1. A cut (cut_lemma.py, 384 hunt laws, every cut): "the large classes do no worse under M-SERPT, and their doubled waiting pays the small excess" holds on the tie family (large-class T_MS/T_G = 1.0000), but 197 of 384 laws have no proper cut with the large classes no worse, and the large-class loss reaches +4.8 R_G (near family).
2. Class-local (class_local.py, same laws): per-class T_MS,k / T_G,k reaches 111.7 (near family, rho 0.999, a light class just above a heavy near twin) and 4.2 on random laws. On the tie family the 1+g class is 1.87 / 3.18 / 9.82 times slower at a = 0.5 / 0.7 / 0.9. Those laws' whole beta is still negative (-11 to -200 on the near/random worst cases).

So M-SERPT can make one class many times slower than Gittins, and the bound holds only by transfer: other classes gain. A proof has to move excess between classes, for example charging a delayed job's excess to the work that overtook it. Whole beta stayed <= -0.207 on all 384 laws, so the tie family (least beta >= 0.0677, [[p0434_least_beta_is_at_least_0_0677_once_a_passes_one_half_2026_11_08]]) is still the only place beta is positive.

Measurement: sampled laws (seed 68, m 3-6, K 3-1000, rho 0.5-0.999), not exhaustive. Files: ~/codex_fleet/runs/own_p0434/cut_lemma.py, class_local.py (+ .out), NOTE.md sections 13:4x; pushed (commit 46953b8c and after). Related: [[p0434_worst_family_excess_sits_in_the_small_classes_2026_11_08]].

