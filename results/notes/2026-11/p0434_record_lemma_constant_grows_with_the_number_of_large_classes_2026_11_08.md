---
name: p0434_record_lemma_constant_grows_with_the_number_of_large_classes_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov: the record-lemma constant grows as 0.0902 n with n far-apart equal-work large classes and passes 1 at n = 12, so the record charge with theta < 1 cannot close the proof"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T08:26:33-05:00
  status: provisional
  evidence: "runs/own_p0434 lin_nlarge.out lin_nlarge2.out"
---

P0434 (M-SERPT against Gittins), 8 Nov 2026 08:2x. The record-lemma charge (at an M-SERPT record, the small classes' excess D_0 + D_1 is at most theta times the large classes' summed Gittins waiting, with theta < 1) fails once there are about a dozen large classes. With n large atoms of equal work, sizes far apart, and the small split a, the low-load constant is

    theta_n = n a^2 (1 - 2a) / (1 - a)^2,

so its sup is n (5 sqrt 5 - 11)/2 = 0.0902 n, which passes 1 at n = 12. Measured through the same theta_lin (sizes K1 100^j, K1 1e4, a = (3 - sqrt 5)/2): 0.0899, 0.1774, 0.2649, 0.3524, 0.4399 for n = 1..5, then 0.7024 (n 8), 1.0524 (n 12), 1.2274 (n 14). With sizes 1000^j the n = 1..5 values sit within 0.3 percent of n f.

Why: the derivation in [[p0434_record_constant_is_5_sqrt5_minus_11_2026_11_08]] shows the small excess is 1/2 - a at the tie, whatever the large side looks like, while the large classes' Gittins waiting tends to (1/2) times the sum of squared works. The tie fixes the total large work at (1-a)/a, so splitting it over n far-apart sizes divides the denominator by n.

This supersedes the general claim in [[p0434_record_lemma_constant_is_0_18_at_equal_large_work_2026_11_08]] ("a third large class gave 0.1739, not more"; "the margin is more than five"). That third-class run was a local search seeded at the two-class optimum and never spread the sizes apart. The 0.180 and the 5 sqrt 5 - 11 closed form stand for the two-large-class family only.

What it kills and what it does not: the record charge with a fixed constant against large-class Gittins waiting alone cannot close the proof. The conjecture is untouched, since at low load both policies' response times are near the sizes and the ratio stays near 1. A repair has to charge against more than Q_G of the large classes (their residence, or the load they bring), or use a constant that scales with how the large work is spread.

Evidence: ~/codex_fleet/runs/own_p0434/ lin_nlarge.py/.out, lin_nlarge2.py/.out, NOTE.md 08:2x; research-repo codex-fleet.

