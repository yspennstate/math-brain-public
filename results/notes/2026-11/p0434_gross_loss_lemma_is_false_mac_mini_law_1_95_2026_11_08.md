---
name: p0434_gross_loss_lemma_is_false_mac_mini_law_1_95_2026_11_08
description: "P0434 8 Nov 18:0x: L+ <= T_G is FALSE - worker-machine 5-atom law, L+/T_G 1.950217761 (T_MS/T_G 1.9668, gains 0.98 T_G) at rho 1-1e-6, recomputed digit for digit with split.py; proofs must net gains"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:14:40-05:00
  status: verified
  evidence: "lplus_macmini_check.out; a fleet message; soap_indep.py"
---

P0434 (M-SERPT vs Gittins, Conj. 8.1 T_MS <= 2 T_G), 8 Nov 18:0x, an agent. The gross-loss lemma
L+ = sum_k max(0, T_MS,k - T_G,k) <= T_G is FALSE.

Counterexample (found by an agent on the worker machine, a fleet message, exact rationals in an agent's
soap_indep.py; recomputed here with split.py in lplus_macmini_check.py, every printed digit equal):
s = [1, 1.1425662427309466, 2.190890054519936, 2.1942626527600324, 17258.972792519828],
p = [0.6965761184774704, 0.29450875117620223, 0.008878554489750173, 3.6573632642141504e-05, 2.223935047942356e-09].
At 1-rho = 1e-6 this gives L+/T_G 1.950217761, G-/T_G 0.983, T_MS/T_G 1.966801. At other loads L+/T_G is 1.243 at
1e-4, 1.768 at 1e-5, 1.913 at 1e-7 and 0.437 at 1e-9.

Mechanism: both of the families that each reach 1 work at once.
- The two small classes keep only 0.4 pct of their Gittins time, so G- is about 0.98 T_G.
- The far atom carries real load (p*s well above 1-rho), so the near-twin classes stall: they run 112x and 26613x
  their Gittins times, and R reaches 1.97.
- The conjecture holds there only because the class gains are netted against the losses.

Scar: my 17:5x local search (lplus_mix.py, 10 starts from the stall pair) found nothing above 0.9917, and I filed
that as "the lemma survives". A local search's best value is not a bound. The worker machine reached 1.95 by searching
5-atom laws from its own 4-atom law, with the far atom carrying real load.

How to apply: drop every proof route that bounds L+ alone. A proof of Conj. 8.1 has to pair each losing class with
the gains of the classes it trades against. For scale, T_MS/T_G = 1.9668 stays under the known family that tends
to 2 (Scully, Harchol-Balter and Scheller-Wolf, arXiv 1907.10792, Sec. 7).

Files: codex_fleet/runs/own_p0434 NOTE.md section 18:0x, lplus_macmini_check.py/.out; the worker machine's
tg_near_critical/NOTE_TG_v2.md.

Supersedes [[p0434_gross_loss_lemma_tight_on_a_stall_pair_with_gains_near_t_g_2026_11_08]]. Related:
[[p0434_gross_loss_stays_under_gittins_time_and_is_tight_2026_11_08]], [[p0434_fixed_law_heavy_traffic_ratio_tends_to_one_2026_11_08]].

