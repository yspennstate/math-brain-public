---
name: p0434_record_constant_is_5_sqrt5_minus_11_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov: record-lemma constant in the limit is theta(a) = 2a^2(1-2a)/(1-a)^2, max 5 sqrt5 - 11 = 0.18034 at a = (3-sqrt5)/2; read off an exact rational fit, numerics agree to 3e-7"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:27:24-05:00
  status: provisional
  evidence: "codex_fleet/runs/own_p0434/lin_closed.out"
---

P0434 (M-SERPT against Gittins), 8 Nov 2026. On the family (1, 1+g, K1, K2) with the large mass placed at the record, the two large classes carrying equal work, and the limit rho -> 0, sizes -> infinity, the record-lemma constant (small-class excess D_0 + D_1 over the large classes' Gittins waiting) is

    theta(a) = 2 a^2 (1 - 2a) / (1 - a)^2,

where a is the small atom's share of the small mass. Setting the log-derivative to zero gives 1/a - 1/(1-2a) + 1/(1-a) = 0, i.e. a^2 - 3a + 1 = 0, so a* = (3 - sqrt 5)/2 = 1 - 1/phi, and since a* = (1 - a*)^2 the value is theta* = 2 a*(1 - 2a*) = 5 sqrt 5 - 11 = 0.1803399. theta vanishes at a = 1/2 and is negative above it.

How it was found: at low load the SOAP gaps drop out exactly (1 - rho_new[c] = 1 - rho E[min(S,c)]/E[S]) and theta is a ratio of finite sums (lin_theta.py). Sampled at 21 values of a, it fits a cubic over a cubic to 3e-14 on held-out points, and the coefficients read 2a^2(1-2a)/(1-a)^2 (lin_ratfit.out, lin_ratexact.out). With the large mass taken 1+d times the record, the numerics go 0.180303561, 0.180339263, 0.180339620 at d = 1e-4, 1e-6, 1e-8 against 0.180339887, and the same at a = 0.30 and 0.45 (lin_closed.out).

Correction: the 0.180304 in [[p0434_record_constant_optimum_split_looks_golden_2026_11_08]] was the d = 1e-4 offset the earlier scripts used, not the limit.

Status: the formula is read off a numerical fit, not derived term by term from the sums; the margin against the needed theta < 1 is more than five. Next: derive it from the sums, then the cut-form proof.

Evidence: ~/codex_fleet/runs/own_p0434/ lin_ratfit.out, lin_ratexact.out, lin_closed.out, NOTE.md 07:2x; research-repo codex-fleet.


Update 07:3x: the dependence on the large-class work ratio c = (1-w)K2/K1 separates, theta(a, c) = 2a^2(1-2a)/(1-a)^2 * (1+c)^2/(2(1+c^2)) (lin_cdep.out: the ratio to c = 1 is identical at a = a* and a = 0.30 and matches (1+c)^2/(2(1+c^2)) at c = 0.1, 0.3, 0.5, 2, 3, 10 to 5e-7). The c factor is at most 1, with equality only at c = 1, by (1+c)^2 <= 2(1+c^2).

Update 8 Nov 08:1x: derived from the SOAP sums, not only fitted (NOTE.md 08:1x, lin_struct.out). The tie gives large work X = (1-a)/a; small classes give D_0 + D_1 = 1/2 - a (the twin's residence W(1) = 1 under M-SERPT is the whole excess); the large classes' Gittins waiting is (1/2)(1+c^2) X^2/(1+c)^2. Their ratio is a^2(1-2a)(1+c)^2/((1-a)^2(1+c^2)). Open: the interval structure is read off two sample points, not proved for all a < 1/2.
Update 8 Nov 08:1x: the interval structure now follows from the rank order (M-SERPT r0 < r1 << r2 < r3, Gittins about 1, g, K1, K2-K1) for every a in (0,1) under the limit order d -> 0+, g -> 0, K1 -> inf, r -> inf (NOTE.md 08:1x). The demoted side of the tie is needed: on the other side the twin's excess is 0. Open: that this family is the worst case, and the cut-form proof.
