---
name: t361_parity_tasks_drop_sharply_law_constant_2026_11_01
description: [PROVISIONAL] T361: in the escape ODE each k-parity task drops in (delta d)^(-(k-2)/2) of its onset (k=2 only log-sharp); total loss t*^-alpha/(alpha zeta(alpha+1)) to 1.5pct
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T23:05:44+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T361 (emergence plus scaling law on multitask sparse parity), 1 Nov. Worked in the decoupled escape-ODE model, dm/ds = p_t m^(k-1)(1 - m^2) from m0 = d^-1/2, with the task's squared loss 1 - m^2 as the skill metric. That metric starts at 1, which the dossier's audit asked for.

Per task, the drop from loss 0.9 to 0.1 takes a fraction C_k (delta d)^(-(k-2)/2) of the onset time. At k = 3 that is 0.116 at d = 1e3 and 0.011 at d = 1e5. A 2-parity is only log-sharp: 0.64 at d = 1e3.

With p_t ~ t^-(alpha+1), the total loss is t*^-alpha/(alpha zeta(alpha+1)) with t* = (s/(zeta S_half))^(1/(alpha+1)). Slopes and constants agree to within 1.5 percent for alpha = 0.5, 1, 2 over 2e6 tasks.

Lesson: the constant is right because each curve is narrow in log time, not because drops are separated. Drops overlap in the total loss once t* exceeds about d^((k-2)/2). My first draft said "to three digits"; that is fixed in place, and alpha = 2 is 1.4 percent off.

Not done: SGD fluctuation and decoupling bounds. Pushed 215e0ce (research_pushes/2026-11-01-loop-T361-sharp-drops); card claim_d4f7748bd3284fb6846069e967b70454 (3 links); frontier move.

Related: [[t350_proved_step_halves_the_compute_optimal_exponent_2026_10_31]] has the same Ren-Nichani-Wu-Lee decoupling; [[t334_tree_degree_is_galton_watson_2026_11_01]] is another exact law checked numerically.
