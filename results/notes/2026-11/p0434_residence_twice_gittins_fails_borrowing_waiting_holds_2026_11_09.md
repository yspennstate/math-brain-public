---
name: p0434_residence_twice_gittins_fails_borrowing_waiting_holds_2026_11_09
description: "P0434 9 Nov 06:2x: (P0) R_MS <= 2 R_G FALSE (2.05 random, 3.07 Mac mini law); candidate (P) R_MS <= 2R_G + (2-c)Q_G alive, zP <= 0.644 (needs <= 1)"
metadata:
  node_type: memory
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T06:24:41-05:00
  status: verified
  superseded_by: p0434_residence_lemma_p_false_zp_1_51_three_paths_2026_11_09
  evidence: ~/codex_fleet/runs/own_p0434/resid_vs_gittins.out; resid_vs_gittins_twins_deep.out; zp_hunt.out
  originSessionId: 18a8f632-b336-4ece-9e3a-6682ec02c3a1
  modified: 2026-11-09T11:39:43.002Z
---

P0434 (M-SERPT vs Gittins, Scully et al. Conj. 8.1, T_MS <= 2 T_G), 9 Nov 06:1x-06:2x, an agent.

After the universal lower bounds on T_G died (kappa 2.263, max-bound 2.071), I compared policy against policy. Split
T = Q + R (waiting, residence) with soap's split_T. Lemma 5.6 gives Q_MS <= c Q_G, c = 2/(1+sqrt(1-rho)).

(P0) R_MS <= 2 R_G is FALSE.
- Random discrete laws (resid_vs_gittins.py, seed 1213, 31146 cases, 2-6 atoms, rho 0.3..0.99): max R_MS/R_G 2.051 at
  s [0.2233, 0.8321, 1.1887, 2.1479, 167.4655], p [3e-05, 0.58269, 0.39992, 0.01735, 1e-05], rho 0.99.
- Mac mini near-2 law along 1-rho (resid_vs_gittins_twins*.py): R_MS/R_G -> 3.069, but R_G/T_G is about 1e-4 there,
  so residence is a negligible part of T_G and the excess is paid out of waiting slack.

Candidate (P) R_MS <= 2 R_G + (2-c) Q_G (with Lemma 5.6 it gives Conj. 8.1) is still alive. zP = (R_MS-2R_G)/((2-c)Q_G),
(P) iff zP <= 1:
- random laws: max zP 0.0080 (31146 cases); max T_MS/T_G 1.279 as a control.
- Mac mini law: zP peaks 0.644 at 1-rho 3e-9 (0.568 at 1e-8, 0.536 at 1e-9) and tends to 0.002 at 1e-14; the
  conjecture's own slack zC = (R_MS-2R_G)/(2Q_G-Q_MS) stays under 0.005.
- zp_hunt.py (Nelder-Mead, 5 atoms, 12 starts, seed 1227): no start beat 0.644; jittered starts lose the twin tie.

Files: ~/codex_fleet/runs/own_p0434/resid_vs_gittins*.py/.out, zp_hunt.py/.out, NOTE.md section 06:1x.
Lesson: the per-component split (P0) is too greedy; any proof must let residence borrow from the Gittins waiting term.

