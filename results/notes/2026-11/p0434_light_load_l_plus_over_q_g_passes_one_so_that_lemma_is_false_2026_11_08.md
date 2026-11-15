---
name: p0434_light_load_l_plus_over_q_g_passes_one_so_that_lemma_is_false_2026_11_08
description: "[VERIFIED] P0434 8 Nov 15:4x: at light load L+/Q_G reaches 1.1268 (Mac mini m 11 law, checked by a second implementation), so the lemma L+ <= Q_G is false; L+ <= T_G is the form left"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:50:14-05:00
  status: verified
  evidence: "Mac mini m 11 law 1.1268 (NOTE_MAC.md, main d7eae411); own_p0434/lowload_twojob.py, an independent two-job first-order sim sharing no code with soap.py, matches every class's (T-x)/rho to ~4 figures, L+/rho 0.69669 vs 0.69676"
---

Light-load sup of L+/Q_G by atom count: 0.508/0.691/0.829(m 6, merged)/0.854/0.891/0.968/1.127 (m 3..11; m 7+ from the Mac mini an agent). The m 11 law (s up to 136489, tail atom with p*s 0.30 of E[S]) is an open neighbourhood. Checked on yitz8 by lowload_twojob.py: to first order a tagged job meets one other job; two-job SOAP dynamics are exact with events at atom boundaries (M-SERPT rank constant within a size interval, Gittins rank falling), ties FCFS. Per-class T matches split.py under both policies. Caveat on definitions: split.py's Q_G is SOAP's waiting term (to the worst future rank), larger than arrival-to-first-service for big classes; with first-service waiting the ratio is 1.78. Lessons: my 15:1x 'levels near 0.78' read off shrinking increments was wrong - a seeded chain undershoots, and a tiny-work ladder adds nothing (adv_lowload_ladder.py), the gain needs a heavy-work tail atom. Supersedes the open question in [[p0434_light_load_loss_over_gittins_waiting_grows_with_atom_count_2026_11_08]]; see [[p0434_light_load_loss_is_class_residence_paid_by_small_class_waiting_2026_11_08]].
