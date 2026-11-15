---
name: p0434_twice_gittins_waiting_plus_residence_fails_at_low_load_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov: E[T_MS] <= 2E[Q_G] + E[R_G] fails at low load with 12+ far-apart equal-work large classes (full SOAP split, rho 1e-3 and 1e-2); Conj 8.1 untouched, ratio 1.0009"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T08:37:15-05:00
  status: provisional
  evidence: "runs/own_p0434 full_slack.out lin_slack.out"
---

P0434 (M-SERPT against Gittins), 8 Nov 2026 08:3x. The strengthened target E[T_MS] <= 2 E[Q_G] + E[R_G] (twice Gittins' waiting plus Gittins' residence, stronger than Conjecture 8.1's E[T_MS] <= 2 E[T_G]) is false. It fails at low load on the family (1, 1+g, n large atoms of equal work, sizes 1e4 * 100^j), with the large mass at the M-SERPT tie and a = (3 - sqrt 5)/2, once n >= 12.

Full SOAP split at finite load (full_slack.out, split_T, no linearisation): T_MS - (2 Q_G + R_G) = -1.86e-5 (n 8), +2.64e-6 (n 12), +1.33e-5 (n 16) at rho = 1e-3, and ten times those at rho = 1e-2. E[T_MS]/E[T_G] there is 1.00009 (rho 1e-3) and 1.0009 (rho 1e-2), so Conjecture 8.1 is nowhere near in danger. The first-order sums (lin_slack.out) give sum_k D_k = -0.0185, +0.0026 at n = 8, 12, the same numbers once the factor E S = 2.618 is put back.

Mechanism: at the tie the small classes' first-order excess is 1/2 - a whatever the large side is (the twin waits for every new arrival's first unit). Each large class's slack is close to its own Gittins waiting, which tends to (1/2) work_k^2. The tie fixes the total large work at (1-a)/a, so spreading it over n far-apart sizes divides the slack by n until it no longer covers the small excess. Same mechanism as [[p0434_record_lemma_constant_grows_with_the_number_of_large_classes_2026_11_08]], here on the real slack instead of the Q_G stand-in.

Consequence: no proof of Conjecture 8.1 can go through the per-law inequality T_MS <= 2 Q_G + R_G. A proof must use Gittins' residence with a factor above 1 somewhere (the conjecture allows 2 R_G).

Evidence: ~/codex_fleet/runs/own_p0434/ lin_slack.py/.out, full_slack.py/.out, NOTE.md 08:3x; research-repo codex-fleet.

Update 8 Nov 08:4x, second route: in the limit E S * sum_k D_k -> (1/2 - a) - X^2/(2n), X = (1-a)/a, positive iff n > 1/f(a), least 11.09 at a = (3 - sqrt 5)/2. Predicted +0.008949 (n 12) and +0.036220 (n 16); full SOAP at sizes 1000^j gives +0.008724 and +0.036090 (full_slack2.out). Hand formula and SOAP numerics agree.
