---
name: p0434_blending_trivial_residence_bound_gives_ratio_two_below_rho_0_626_2026_11_09
description: "[PROVISIONAL] P0434 9 Nov 02:1x: E[R_MS] <= E[X]/(1-rho) blended with Lemma 5.7 beats Scully Thm 5.1 for rho<0.9999 and proves ratio <= 2 (Conj 8.1) for rho <= 0.626; 2.90 at 8/9 vs published 3"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T02:16:25-05:00
  status: provisional
  evidence: "own_p0434/blend_bound.out (closed-form grid); lemmas read from src/scully1907.txt"
---

P0434 (Scully et al. 2020, arXiv 1907.10792, Conj. 8.1: M-SERPT is a 2-approximation of Gittins), 9 Nov 02:1x, an agent. Derived by hand from the paper's own lemmas; the numbers come from a closed-form grid (blend_bound.py), not a simulation.

The one new line: Prop. 4.8 is an equality for M-SERPT, E[R_MS(x)] = x/rhobar(y(x)), and rhobar(a) = 1 - lam E[min(X,a)] >= 1 - rho. So E[R_MS] <= E[X]/(1 - rho).

Blend it with Lemma 5.7 (E[R_MS] <= E[Q_MS] + l E[X], l = (1/rho) log 1/(1-rho)) with weight theta, and use Lemma 5.6 (Q_MS <= c Q_G, c = 2/(1 + sqrt(1-rho))) and Prop. 4.9 (E[X] <= R_G):
E[T_MS]/E[T_G] <= max((2-theta)c, theta/(1-rho) + (1-theta)l).
Route B instead uses l E[X] <= T_G: (1-theta) + max((2-theta)c, theta/(1-rho)).

Optimised over theta: 1.715 at rho 0.5, 2.035 at 0.64, 2.901 at 8/9 (published 2.343, 2.5, 3). The blended bound is <= 2 for rho <= 0.626, so Conj. 8.1 holds at those loads. It is below Theorem 5.1 for all rho < 0.9999 (equal near 0.98); the sup over all loads is still 5. theta = 1 alone gives ratio <= 1/(1-rho).

Status: provisional, referee asked (an agent).

Files: ~/codex_fleet/runs/own_p0434/blend_bound.py/.out, NOTE.md 9 Nov 02:1x.

Related: [[p0434_mserpt_residence_excess_beats_gittins_waiting_at_light_load_2026_11_09]], [[p0434_levels_on_a_gittins_block_wait_under_twice_by_record_telescoping_2026_11_09]].

Next: a literature check for a light-load bound in 2020-2026 citing work, then try the same blend inside Lemma 5.7's per-valley proof to push the <= 2 range past 0.626.


Addendum 9 Nov 02:4x (an agent, literature): the heavy-traffic end of Conj. 8.1 is already published. arXiv 2003.13232
(Scully, Grosof, Harchol-Balter, Perf. Eval. 2021) Theorem 3.2 with k = 1 gives lim_{rho->1} E[T_MS]/E[T_G] <= 2 for X in
OR(-inf,-2), MDA(Lambda) cap (QDHR cup QIMRL), or Bounded. So the open part is finite load in (0.626, 1) for every law, plus the
limit for laws outside those classes. Before calling a P0434 bound new, check both 1907.10792 and 2003.13232 (NOTE 9 Nov 02:4x).
