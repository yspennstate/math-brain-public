---
name: t240_stochastic_cone_lemma_window_44_n_1e24_2026_11_01
description: [PROVISIONAL] T240 stochastic cone lemma (L3) proved on paper: O(1) window 44, half cone held w.p. 1-O(1/log^2 N); asymptotic only (N~1e24); sigma>0 was already settled
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T23:46:48+04:00
  status: provisional
  evidence: "rows/T240/L3_stochastic_cone.md, moves d76f8868"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T240 (soft committee plateau escape), 1 Nov: the plan's (L3), the stochastic cone lemma, is written out and pushed (rows/T240/L3_stochastic_cone.md, move in moves.jsonl d76f8868).

From |u| >= U_c/8 with |s| <= kappa|u|/4, SGD stays in the half cone until |u| = U_c/2, with probability 1 - O(1/log^2 N), in at most 43.9 time units, with |s| <= 0.360 kappa|u| + O(N^{-1/2} log N). The trick: subtract the frame martingale (w = z - dM) so the rest is a pathwise ODE inequality, then use the 18 Oct interval constants (g 0.031614, |m_su| 7.382e-6, mu_ss -1.894e-3; r = 0.110).

What to carry: the window is O(1), so the slow stable rates (1/|mu| = 530) never enter. The lemma is purely asymptotic, though: the margin 3.5e-10 needs N around 1e24, so the cone phase at U_c 1e-5 can't be seen at simulable N (noise is 5e-3 at N 32k). Also checked 1 Nov: sigma > 0 at the plateau was already settled by w689 C2/C5 (sigma_a^2 1.42e-4 at eta 0.5), so don't redo it.

Open: c_D and the noise bound as numbers, the s-offsets of x* from the centre of X*, the early phase from N^{-1/2} log^2 N to U_c/8 (odd structure), (L4). Self-reviewed only.


ADDENDUM 1 (1 Nov): the offsets of x* from the box centre, the one loose constant, come out near 1.2e-8 in s against the 1.5e-8 the lemma needs (floats, about 20% room; moves ef0b4d6c). The exact interval values from kraw_tight.py should replace this; kappa 1/300 is the fallback.

ADDENDUM 2 (1 Nov): the early phase is written too (rows/T240/E_early_phase.md, moves 763f9aeb). From |u| = N^{-1/2} log^2 N it reaches the cone entry at U_c/8 with |s| <= 0.0216 kappa U_c. It works because F_o(0, e) = 0 exactly (teacher-swap symmetry): u gets no push from the even sector. The quadratic forcing (L4) needs no separate lemma, since the hull covers it. Start with |s| <= kappa U_c/128, not /64 (margin 1.9e-10 against 3.7e-11). Still open: the first O(log log N) of the escape (L2/L1, the plan), the constants as numbers, and an independent review.

ADDENDUM (2 Nov, an agent): reviewed by an agent (rows/T240/reviews_agent/REVIEW_L3_E.md, move f340d85a98). L3 ACCEPTED. E ACCEPTED WITH ONE CORRECTION: the hull u-s_4-u coupling is a constant rate (1.12e-9 per unit time, a factor N^{+-1.8e-8} over the log N window), not 1 + o(1); fixed in E revision 2 by an exact per-eta 2x2 diagonalization of the odd block (|T_eta - I| <= 1.2e-9, keeps parity), and the error in (i) is O(log^{-1/2} N), not O(1/log N). The x* offsets are not needed (the c9_cone hull is on X* + P Z); the exact offsets are max 1.01e-9 in s and 3.2e-10 in u, so the 1.2e-8 float estimate above is superseded. Lesson: a hull bound on a coupling gives a rate, and over a window of length log N a rate error of any fixed size is not o(1). Frontier T240 move m240d.

Related: [[t240_e_rev2_review_t_eta_certified_2p1e9_rate_integral_fix_2026_11_03]] (the 3 Nov review that accepted L3's second addendum).
