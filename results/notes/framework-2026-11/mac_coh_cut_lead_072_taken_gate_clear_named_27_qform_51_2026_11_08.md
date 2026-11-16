---
name: mac_coh_cut_lead_072_taken_gate_clear_named_27_qform_51_2026_11_08
description: "[VERIFIED] Yes since 8 Nov 02:06: the second machine's COH_CUT_LEAD default is 0.72; named 25->27/32, qform 47->51/57, fresh false fires 18->21/40 (2 junk, 1 near miss), gate breaches none"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T02:11:06+04:00
  status: verified
  evidence: "eval_proof_banks live default 27/32 51/57 shuffled 0; regression gate breaches [] (prev qform 0.719); hp_0.80 vs hp_0.72 diff 3 unanswerable rows; brain-framework 207842b; a fleet message"
---

Should the second machine follow the workstation's COH_CUT_LEAD 0.72? Yes, and since 8 Nov 02:06 it does (the live proof-bank run on the new default ended 02:06:05; brain-framework commit 02:06:16). an agent lowered the lead line from 0.80 to 0.72 on the workstation on 7 Nov 23:44 (+02) and asked the second machine to measure before it followed.

Mac measurement, before the change, with MATHBRAIN_COH_CUT_LEAD overriding and the all-words prefilter on. Proof banks at 0.80 against 0.72: named 25 against 27 of 32, qform 47 against 51 of 57, shuffled 0 at both. Fresh 218-item hook bank: content 64/89 and hinted 85/89 at both, with no answerable row changing. Unanswerable false fires went from 18 to 21 of 40 (strict 11 to 14 of 33). Two of the three new fires were junk: faltings served Elliptic curve and a De Bruijn-Erdos theorem, and noether_norm served abelian groups and localization. The third, pinsker, served total variation distance, a near miss that would still help a reader. The workstation's withhold banks (held788, op/cohname) are on neither the second machine nor origin. an agent took the trade (a fleet message): 0.72 still keeps 33 of the 77 withholds 0.80 bought on held788. They said the lever for the junk fires is a length-aware lead line (unmeasured), not going back to 0.80.

What changed: only the default on the second machine's own line and its comment. Origin c42c7621 has 0.72, but origin's math_sense lacks an agent's tool-not-rival and tool-yields-lead hunks from 02:00-02:09, so taking origin's file would have dropped them. Backup math_sense.py.pre_lead072_20261108. brain-framework 207842b (secret scan clean), Mac mirror equal at 423.

After, on the live hook with no override: proof banks named 27/32 and qform 51/57, shuffled 0. Regression gate: breaches none, against qform 0.719 under the 0.75 floor on the row before. Absent-target fires 0.525 against the 0.75 ceiling. The four ERROR lines are the keyed banks that are expected on the second machine ([[math_gate_on_mac_three_keyed_bank_errors_expected_breaches_empty_2026_11_06]]).

How to apply: when a peer changes a shared dial in a file that someone else is editing on this machine, change only that line. Don't take the peer's whole file. Before reporting the false-fire cost, read the new fires one by one: a count of 3 hides whether they're junk or near misses. Related: [[math_gate_qform_breach_is_coh_cut_lead_080_from_framework_swap_2026_11_08]], [[math_prefilter_allwords_live_qform_41_to_47_fresh_0_of_218_2026_11_08]].
