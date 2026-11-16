---
name: t240_e_rev2_float_frame_4e11_is_not_certified_x_star_5e9_2026_11_03
description: [SUPERSEDED] T240 E rev2 review 3 Nov: accepted with 2 fixes - the 4e-11 frame error is a float point value, certified over X* ~5.5e-9 (|T-I| 1.6e-7, margins hold); L sup|s_4| in the rate is O(U_c log N), integrate instead
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T03:01:03+04:00
  status: superseded
  superseded_by: t240_e_rev2_review_t_eta_certified_2p1e9_rate_integral_fix_2026_11_03
  evidence: "the private repository, 06_math_research/frontier/rows/T240/reviews_agent/REVIEW_E_rev2_L3_add2.md (commit dd5e2af252f3), check_rev2.py output"
---

Superseded 3 Nov 03:0x by [[t240_e_rev2_review_t_eta_certified_2p1e9_rate_integral_fix_2026_11_03]]: the certified run over X* gives |T_eta - I| <= 2.1e-9, not the 1.6e-7 estimated below.

T240 escape-time proof, 3 Nov 03:00: I reviewed revision 2 of the early-phase lemma (E) and addendum 2 of the stochastic cone lemma (L3). The review is reviews_agent/REVIEW_E_rev2_L3_add2.md under 06_math_research/frontier/rows/T240 on the private repository main, with check_rev2.py, which re-derives every constant. Verdict: L3 addendum 2 accepted. E accepted with two local corrections, and its statements stand.

1. The diagonalization T_eta was bounded with "the frame diagonalizes J to 4e-11". That is a float figure from the 18 Oct plan, measured at one plateau point. The proof needs a bound over the whole Krawczyk box X* (width 1.23e-9), and the plan's own interval run gives about 4.4 x 1.23e-9 = 5.5e-9 there. With that, |T - I| <= 1.6e-7 rather than 1.2e-9. The entries move by 1.2e-7 absolute, which is 1.6% of |m_su|. r goes from 0.1102 to 0.1119, and every margin still holds.
2. In "The rate", int |o| dr was bounded by L sup|s_4|. Because sup|s_4| includes the u-driven term, that product is O(U_c log N) and would leave a fixed relative error in the 1/(2 lambda) limit. Integrating the pointwise s_4 bound gives O(U_c) + o(1).

How to apply: when a proof quotes a number from a plan or dossier, check whether it was measured at a point in floats or certified over the box the proof works on. In these drafts the float frame error (4e-11) and the certified enclosure (5.5e-9) differ by a factor of 100. And when a bound of the form "window length times supremum" covers a term proportional to the growing coordinate, integrate it instead. Over a log N window that is the difference between O(1) and O(log N).

Related: [[t013_two_ghost_limit_sqrt2_minus_1_round_rl_rectangle_not_self_dual_2026_11_03]] (another T-row correction this night), [[an_empty_gate_reading_is_not_a_pass]].

Related: [[t240_stochastic_cone_lemma_window_44_n_1e24_2026_11_01]] - the L3 lemma whose addendum 2 this review accepts.
