---
name: math_prefilter_allwords_live_qform_41_to_47_fresh_0_of_218_2026_11_08
description: "[VERIFIED] Is the math gate's proof-bank breach fixed? Mostly: since 8 Nov 01:17 the second machine's math_prefilter lets a short sub-query's all-words matches past the BM25 top 300, so the long change-of-variables card no longer drops on store growth; qform 41 to 47/57 (floor 0.75), fresh bank 0 of 218 changed; COH lead still 0.80"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T01:20:30+04:00
  status: verified
  evidence: "eval_proof_banks + eval_math_hookpath live and scratch, 8 Nov 01:0x-01:2x"
---

Since 8 Nov 01:17:56 the second machine's live math_prefilter.py lets every all-words match of a short query (2 to MATHBRAIN_PREFILTER_ALLWORDS_MAX=3 indexed words) into the candidate pool after the BM25 top k. It is on by default; MATHBRAIN_PREFILTER_ALLWORDS=0 turns it off. The backup is math_prefilter.py.pre_allwords_20261108, sha 5e034acf. The prototype was an agent's (allwords_prototype_20261108); I landed it after both peers handed the choice over. an agent, the session that put the framework math hook on this machine, died in the 7 Nov crash.

Why: the named sub-query 'change of variables' ranks the Lebesgue change-of-variables card (claim_1047e7e3) around 300th. It sat 298th of 555 at N 11,010 and 301st at N 11,022, with only a 5th-figure score gap. It is a long card, dl 185 against a mean of 60, and only 9 cards hold both words, while 293 of the 300 slots go to one-word matches. Each new store entry moves N, so the card fell in and out of k=300. That was the 9-item store half of the 8 Nov gate breach ([[math_gate_proof_breach_coh_080_costs_6_evidence_count_hides_cov_card_2026_11_08]], [[math_gate_qform_proofbank_53_to_41_swap_costs_3_change_of_variables_9_2026_11_08]]).

Checked:

- **Positive control.** A scratch tree held the patched file, with real copies of math_sense.py and eval_math_hookpath.py and symlinks for the rest. A script's own directory resolves through symlinks, so only a real copy imports the patch. There the real-proof bank went 41/57 with the rule off and 47/57 with it on. Builder: allwords_scratch_tree_2026_11_08.py.
- **Live, after the install.**
  - eval_proof_banks: qform 47/57 (0.825, above the 0.75 floor), named 25/32. With the setting off, 41/57, so the off switch works.
  - eval_math_hookpath fresh bank: 0 of 218 rows changed against the pre-change run (diff by kind, key, form and area; fresh_rowdiff_2026_11_08.py). False fires stay at 18/40.
  - Hooks 88/88, dispatch ok, math_recall prints cards.

Not changed: COH_CUT_LEAD stays 0.80 ([[math_gate_qform_breach_is_coh_cut_lead_080_from_framework_swap_2026_11_08]]); with 0.70 as well the bank would read 51/57. The fire banks that would price a lower lead line are not on this machine.

The second machine's math_prefilter.py is now ahead of brain-framework by this one hunk. Porting it there is the framework the author's job. A drift scan will flag it, and it is meant.

How to apply: if the qform bank drops again, look first at whether a named sub-query's card sits near PREFILTER_K. The fresh bank never takes this path, so the fresh bank alone cannot price the rule.

