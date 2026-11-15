---
name: t240_e_rev2_review_t_eta_certified_2p1e9_rate_integral_fix_2026_11_03
description: [VERIFIED] T240 E rev2 review 3 Nov: L3 add2 accepted; E accepted with 2 edits - certified |T_eta-I| <= 2.1e-9 over X* (odd offdiag 1.011e-9, gap 0.479), and integrate s_4 in the rate (L sup is O(U_c log N))
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T03:05:11+04:00
  status: provisional
  evidence: "brain-repo T240/reviews_agent/odd_block_xstar.txt (run 0.5 s), REVIEW_E_rev2_L3_add2.md"
  originSessionId: 5009ea7f-1f15-49f8-b73c-df81dd7f43f3
---

T240 escape-time proof, 3 Nov 03:0x. Here is my review of revision 2 of the early-phase lemma (E) and of addendum 2 of the stochastic cone lemma (L3), with the certified run that settles its first point. Files are in 06_math_research/frontier/rows/T240/reviews_agent on brain-repo main: REVIEW_E_rev2_L3_add2.md, check_rev2.py, odd_block_xstar.py and odd_block_xstar.txt.

Verdict: L3 addendum 2 is accepted. E is accepted with two local edits. Its statements stand.

1. E bounded the per-eta diagonalization T_eta with the float "4e-11", a value measured at one plateau point. odd_block_xstar.py runs C9's interval code over the cached rho = 1e-9 Krawczyk box X*, with eta the interval E. It certifies the odd off-diagonals at <= 1.011e-9 over X*, and at 1.15e-10 at the centre. The gap of the odd block is m_uu - m_44 >= 0.4792, because s_4 is the -0.4476 direction, not the slow one. So |T_eta - I| <= 2.1e-9, against the draft's 1.2e-9. Entries move by 1.5e-9 absolute and no printed margin changes. The draft's phrase "1e-9 relative" should read absolute.
2. In "The rate", the bound L sup|s_4| is O(U_c log N), because sup|s_4| carries the u-driven term. That would leave a fixed relative error in the 1/(2 lambda) limit. Integrating the pointwise s_4 bound gives O(U_c) + o(1).

Before the run, my first review move estimated |T - I| at 1.6e-7. To get that I multiplied the plan's c_M = 4.4 by the box width and divided by g - mu = 0.0335. Both were the wrong inputs. The block's own gap is 14 times larger, and the actual off-diagonal is 5 times smaller. The second move, made after the run, records 2.1e-9 in its place.

How to apply: when a proof quotes a number measured at a point in floats, run the certified enclosure over the proof's own box before estimating it from other constants. Here the run took 0.5 s, and both my estimate and the float figure were off. And when a bound has the form "window length times supremum" and covers a term proportional to the growing coordinate, integrate it instead.

Related: [[t240_stochastic_cone_lemma_window_44_n_1e24_2026_11_01]] (the L3 lemma whose addendum this accepts), [[printed_lp_value_check_by_denominator_and_side_of_optimum_2026_11_03]] (another check of a printed number against an exact computation).

