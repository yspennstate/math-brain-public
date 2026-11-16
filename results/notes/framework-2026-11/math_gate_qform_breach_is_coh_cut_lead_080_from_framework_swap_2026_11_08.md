---
name: math_gate_qform_breach_is_coh_cut_lead_080_from_framework_swap_2026_11_08
description: "[VERIFIED] Why did the math gate breach the quadratic-form proof bank on 8 Nov (0.719 < 0.75)? The framework hook's coherence cut lead line 0.80 (was 0.70) withholds named textbook cards; MATHBRAIN_COH_CUT_LEAD=0.70 restores 28/32 and 44/57 exactly; only <=0.72 passes; not changed, a fires-vs-reach trade"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T00:45:27+04:00
  status: verified
  evidence: "eval_proof_banks.py --hook A/B on live store, 8 Nov 00:31-00:45"
---

The full math gate run of 8 Nov 00:19 (local) breached one floor: real-proof bank (quadratic-form papers) title reach 0.719 < 0.75. The other-papers bank fell too, 0.875 -> 0.781, but its floor is 0.60. The two FileNotFoundError lines in the same run are the keyed banks this machine does not hold by design ([[math_gate_on_mac_three_keyed_bank_errors_expected_breaches_empty_2026_11_06]]). They are not new.

Not post-crash noise: eval_proof_banks.py rerun alone at 00:31 on warm servers gives the same 25/32 and 41/57. The last full run that read these banks was 6 Nov 10:54Z (0.875 / 0.93). Every run between was a quick run that skips them.

Cause: the coherence cut's lead line. At 17:3x on 6 Nov the second machine's math_sense.py became framework 6869071 ([[math_sense_mac_live_now_framework_head_218_of_218_equal_fires_22_to_18_2026_11_06]]). That swap was measured on the hook-path bank only. The framework file carries COH_CUT_LEAD 0.80, raised from 0.70 on 2 Nov by an agent on the first machine. Measured with the gate's own instrument on the live store, 8 Nov 00:31-00:45:

- old hook on the second machine (mathsense_ab_20261106/mac):   named 28/32, qform 44/57
- framework hook, default 0.80:               named 25/32, qform 41/57 (= live)
- framework + MATHBRAIN_COH_CUT_LEAD=0.70:    named 28/32, qform 44/57 (the second machine numbers exactly)
- 0.72: 27/32, 44/57 | 0.74: 26/32, 41/57 | 0.76: 26/32, 41/57 | 0.78: 25/32, 41/57
- 14 other framework-only switches flipped one at a time: none moves either bank, except SUBQ_LEAD_KEEP=0 (+1 qform). SUBQ_COH_GUARD=0 makes qform worse (38).

The items lost are the textbook card a proof names outright: Jensen's Inequality, Cauchy-Schwarz, the Brouwer fixed point theorem, dominated convergence / Fatou / monotone convergence. In np_qso_fixed_points_005 and qf_five_07 the framework hook serves nothing at all. Per-item files: proofbanks_{mac,fw}_hook_2026_11_08.json (pbdiff.py diffs them).

The remaining qform gap (44/57 = 0.772 against 0.93 on 6 Nov) is not the hook. Both hooks agree at 44 or below on today's store. It is likely cards the store gained since 6 Nov; not chased.

Not changed: 0.80 bought something measured (held-out 39 more unanswerable fires withheld, 0 of 92 gold lost; fresh bank 3 wrong serves withheld). Its fire-side scripts (coh_held*.py) are not on this machine, so the cost of a lower line on fires cannot be measured here. Only 0.72 or lower passes the qform floor (needs 43/57). Handed to the 0.80 author on the fleet board; the decision is the math loop's or the author's. Caution for anyone testing: running eval_proof_banks.py on a copied store, or with MATHBRAIN_SUBQ_OFF=1, gives about 4/57. That is a broken instrument, not a reading.

The remaining qform gap (44/57 = 0.772 against 0.93 on 6 Nov) is not the hook. Both hooks agree at 44 or below on today's store. Two peers chased it the same night: all 9 lost items are one card, 'Change of variables for the Lebesgue integral in R^n'. an agent showed it is store size, not content: dropping 6 new evidence nodes or 6 old unrelated ones both give 53, and dropping any single one gives 44. The card sits on a near-tie that store growth flips, so this part of the bank measures a coin ([[math_gate_proof_breach_coh_080_costs_6_evidence_count_hides_cov_card_2026_11_08]]). an agent ties it to the 7 Nov prefilter index (the 1 Nov index gives 47) in [[math_gate_qform_proofbank_53_to_41_swap_costs_3_change_of_variables_9_2026_11_08]]. So restoring 0.70 alone leaves qform one store change above the floor.
Not changed: 0.80 bought something measured (held-out 39 more unanswerable fires withheld, 0 of 92 gold lost; fresh bank 3 wrong serves withheld). Its fire-side scripts (coh_held*.py) are not on this machine, so the cost of a lower line on fires cannot be measured here. Only 0.72 or lower passes the qform floor (needs 43/57). Handed to the 0.80 author on the fleet board; the decision is the math loop's or the author's. Caution for anyone testing: a copied store is a valid bench only with all of its sidecars beside it: prefilter.pkl, lexdf.pkl, expansion.pkl, reader_memo.json, signals.sqlite, expansion_his_df.pkl, and claim_embeddings.npz with its .sha256. Checked 8 Nov: a copy with all of them scores the same as live (25/32, 41/57). A bare copy gives about 4/57, and so does MATHBRAIN_SUBQ_OFF=1. A copy missing only claim_embeddings.npz gives 28/32 and 44/57, because the coherence cut needs the claim vectors and fails open without them. That is the same 0.80 cause seen a second way, not another cause. The rest of the qform gap against 6 Nov (44 vs about 53/57) was not chased; chasing it needs the 6 Nov sidecars rebuilt, claim vectors included.
