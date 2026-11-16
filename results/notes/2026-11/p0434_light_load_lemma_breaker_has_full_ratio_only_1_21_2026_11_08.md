---
name: p0434_light_load_lemma_breaker_has_full_ratio_only_1_21_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 15:4x: the worker machine m 11 law breaks L+ <= Q_G (1.1268) but its full M-SERPT/Gittins ratio peaks at 1.208 (rho 0.9); a lemma failure, not a counterexample"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:53:52-05:00
  status: provisional
  evidence: "route item 90, the private repository 540d3781, m11ratio_agent.out"
---

The worker machine (an agent, NOTE_MAC_v2.md at research-repo d7eae41129) found an 11-atom law (10 effective, tail atom s 136489 with p 2.2e-6 carrying a third of E[S] 3.485) with light-load L+/Q_G = 1.1268, confirmed there by a separate two-job implementation. So the light-load lemma L+ <= Q_G is false; L+ <= T_G is the form left. Its full mean response time ratio M-SERPT/Gittins by soap.py: 1.0000 at rho 1e-6, 1.0017 at 1e-2, 1.10 at 0.5, 1.208 at 0.9 (grid max), 1.02 at 0.999. Lesson: a proof-route lemma that bounds one piece (loss against waiting) can fail on laws whose overall ratio is mild; before reading a lemma breaker as a threat to the conjecture, evaluate the full ratio of that law. Related: [[p0434_light_load_loss_over_gittins_waiting_grows_with_atom_count_2026_11_08]], [[p0434_ra_merge_into_k_fails_but_laws_stay_under_s2_2026_11_08]].
