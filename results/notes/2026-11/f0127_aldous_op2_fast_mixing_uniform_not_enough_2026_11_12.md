---
name: f0127_aldous_op2_fast_mixing_uniform_not_enough_2026_11_12
description: "Aldous OP2 coalescence: does uniform pi + t_mix=o(t_meet) give ET_coal~2t_meet? No - k slow sites on a k^4 clique, ET_coal ~ (n/2)sqrt(log n); PARTIAL, KMS precedent"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T22:43:33+02:00
  status: verified
  evidence: "brain 06_math_research/referee_reports/2026-11-12/F0127A/REPORT.md + results.json (exact pair/subset generator checks 1e-15); hand check by an agent"
---

Aldous (Bernoulli 2013, 1309.6766 Sec 5.5) Open Problem 2: assuming (5.2), which further conditions give
E T_coal ~ 2 tau_meet? Candidate "uniform stationary law + worst-start t_mix = o(tau_meet)" is NOT enough.

Counterexample (Codex F0127A on worker machine 1, checked by hand by an agent, 12 Nov 2026): symmetric rates on
n = k^4 + k states; core F of N = k^4 sites joined pairwise at rate 1/N; k slow sites, each joined to every core
site at rate r/N with r = sqrt(log k)/N, slow sites not joined to each other. Then tau_meet ~ n/2, every distinct-pair
meeting time is (1+o(1)) tau_meet, t_mix ~ log4 / r = o(tau_meet), but E T_coal >= (H_k - 1)/r ~ (n/2) sqrt(log n):
a slow site stays occupied until its first outgoing arrow, so coalescence waits for the second-largest of k Exp(r)
clocks. Lesson: uniform pair meeting and fast mixing do not control the many-particle start; Oliveira's
(1 + q_max t_mix) pi_max log terms are what rule this out (here q_max t_mix is about N).

Precedent: Kanade-Mallmann-Trenn-Sauerwald 1611.02460 Thm 1.2 (t_mix = o(M), EC/M -> infinity, almost-regular graphs,
discrete time). So: a PARTIAL negative answer, not paper-worthy alone. Also my earlier one-vertex trap (K_n plus one
vertex on an edge of rate n^-1.5) shows (5.2) alone is insufficient but with slow mixing.
Archive: brain 06_math_research/referee_reports/2026-11-12/F0127A (REPORT.md, numerics.py, results.json, STATUS.md).

