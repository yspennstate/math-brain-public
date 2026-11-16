---
name: p0434_coupled_lemma_t_ms_le_c_q_g_plus_2_r_g_holds_with_room_2026_11_09
description: "P0434 9 Nov 07:3x: coupled candidate (P') T_MS <= cQ_G + 2R_G (implies 8.1) unbroken; q = T_MS/(cQ_G+2R_G) reaches 0.989 on the Mac mini near-2 law, as tight as 8.1 in heavy traffic"
metadata:
  node_type: memory
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T07:08:42-05:00
  status: provisional
  evidence: ~/codex_fleet/runs/own_p0434/pprime_random.out; pprime_hunt.out; pprime_check.out
  modified: 2026-11-09T13:23:38.550Z
---

P0434 (M-SERPT vs Gittins, Scully et al. Conj. 8.1, T_MS <= 2 T_G), 9 Nov 07:0x, an agent.

After (P) died at zP 1.507 ([[p0434_residence_lemma_p_false_zp_1_51_three_paths_2026_11_09]]), the coupled candidate
  (P')  T_MS <= c Q_G + 2 R_G,   c = 2/(1+sqrt(1-rho))
is alive with a lot of room. It implies 8.1 because c <= 2. Equivalently zP' = (R_MS - 2R_G)/(c Q_G - Q_MS) <= 1, which
lets the residence excess spend Q_MS's distance below c Q_G instead of a fixed (2-c) Q_G.

Measured (soap.py/split.py):
- on the (P) breaker best6 (zP 1.507): zP' 0.00054 at its own 1-rho 8.2e-9; max 0.040 over 1-rho 1e-13..1e-2.
- Mac mini 5-atom near-2 law: max zP' 0.0070.
- pprime_hunt.py (Nelder-Mead from the four near-2 laws exactly, 12 runs): best zP' 0.0984, reached by best6 drifting to
  1-rho 0.0597. Heavy-traffic starts stayed under 0.013.
- pprime_random.py (random 2-6 atom laws, sizes log-uniform 1..1e4, Dirichlet(0.3), rho 0.3..0.99, seed 1249, 300 s,
  19242 cases): max T_MS/(c Q_G + 2 R_G) 0.747, max zP' -0.014 (the residence excess never even turns positive
  where c Q_G - Q_MS is the denominator), while T_MS/T_G reached 1.373.

Reading: the worst zP' sits at moderate load (1-rho near 0.06), not at the twin heavy-traffic laws that make 8.1 tight.
Next: hunt zP' at moderate load on 3-6 atom laws; if it holds, prove (P') class by class from SOAP.

07:2x update, q = T_MS/(c Q_G + 2 R_G), (P') iff q <= 1:
- pprime_hunt_mod.py (rho capped at 0.97): q 0.88066 on a 5-atom law, rho against the cap. Following that law over
  1-rho 1e-6..1e-1 (pprime_rho_scan.py) peaks at 0.88336 at 1-rho 0.0237 (soap_mp agrees), q -> 0.50 as rho -> 1.
- pprime_hunt_free.py (rho up to 0.99999): q 0.89442 on s [1, 103.173, 254.95254, 254.95263, 9018.89], p [0.002827,
  0.64909, 0.33476, 0.013084, 0.00023993], rho 0.997766. Three paths agree (soap float, soap_mp T ratio, grid N 2000
  and 8000): q 0.894419, T_MS/T_G 1.711315. The climb flattens 0.881 -> 0.891 -> 0.894 on a twin-atom shape.
- Those hunts started away from heavy traffic. Measured on the near-2 laws themselves (pprime_q_near2.py, soap.py and
  soap_mp at 50 digits agree): Mac mini law q 0.989193 at 1-rho 3.2e-7 (T_MS/T_G 1.977), best6 q 0.987642 at 1e-6.
  Since c -> 2 as rho -> 1, (P') has no more room than 8.1 itself there; zP' small does not mean q small. (P') is
  alive and unproved, and the measure of its room is q, not zP'. The moderate-load basin tops out near q 0.933
  (pprime_hunt_long.out).
- 07:4x, pprime_hunt_heavy.py (q hunted from the near-2 laws, 1-rho down to 1e-13): q 0.996932 on s [1, 2.0712683,
  3.129714801194438, 3.129714801208326, 127948.2], p [0.92008, 0.078824, 0.0010935, 1.4519e-06, 1.2333e-11], 1-rho
  4.94e-9; T_MS/T_G 1.993726. soap float and soap_mp at 50 digits agree; the grid path merges twins 1.4e-11 apart and
  reads 1.0, so it is no check at that tie width. q > 1 would need T_MS/T_G within 2 sqrt(1-rho) of 2; (P') is
  essentially as hard as the tightness of 8.1.

Files: ~/codex_fleet/runs/own_p0434/pprime_check.py/.out, pprime_hunt.py/.out, pprime_random.py/.out, NOTE.md 06:3x;
pprime_hunt_mod, pprime_rho_scan, pprime_hunt_free (.py/.out), pprime_free_recheck.out, NOTE.md 07:2x.

- 08:0x (measured): with the gap clip lowered to e^-32 the polish reached q 0.9972837, T_MS/T_G 1.9944561 (soap_mp, 50
  digits, exact input; pprime_polish_mp.out), s [1, 2.0727638366, 3.130565793545842, 3.130565793573316, 161521.28],
  p [0.924382, 0.0749729, 6.43994e-4, 1.10854e-6, 7.42474e-12], 1-rho 3.11e-9; the twin gap 2.7e-11 sits off the clip.
  Closest (P') has come to failing: 0.27%.
- 08:2x (measured): q ~ (T_MS/T_G)/c, so (P') at load eps = 1-rho reads g(eps) = 2 - sup T_MS/T_G >= 2 sqrt(eps)/(1+sqrt eps).
  pprime_gap_scan.py hunts q at fixed eps. The found gap and its ratio to 2 sqrt(eps): 9.2e-2 (x4.6) at 1e-4, 5.0e-2 (x7.9) at 1e-5,
  2.5e-2 (x12) at 1e-6, 1.2e-2 (x18) at 1e-7, 5.5e-3 (x28) at 1e-8, 4.2e-3 (x37) at 3.1e-9, 3.5e-3 (x56) at 1e-9,
  1.9e-3 (x307) at 1e-11. The giant sits on the e^14 clip at 1e-10 and below. The found gap falls about like eps^(1/3),
  slower than sqrt, so q rises toward 1 but the margin for q > 1 widens. These gaps are upper bounds on g; this is
  evidence, not proof. Confirmed best: q 0.998442 at 1e-9 (soap_mp at 50 digits, pprime_gap_mp_repr.out), on s
  [1, 2.1325308715576785, 3.1678424430897163, 3.1678424509947547, 752103.23193338] and p [0.8755361940711661,
  0.12330751734369959, 0.001155399842893117, 8.887408915465022e-07, 1.349665322459624e-12]. Found, not yet rechecked:
  0.99903 at 1e-11. Printed laws must be repr: see [[a_rounded_printout_broke_the_twin_tie_and_read_ratio_one_2026_11_09]].
