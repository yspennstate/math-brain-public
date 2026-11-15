---
name: hook_count_did_not_mean_delivery_2026_11_12
description: "New hooks pass isolated regex tests but never reach live worker stages"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:32:58+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: The owner repeatedly asked whether hooks actually fired. A supporting 8 Oct measurement found 0 of 137 landed hooks shown in 77 stages, and 177 math hooks depended on probability cards absent from stage input. In a separate evaluation, hook 230 scored USED 12/12 because the prompt already contained the advice.

Why it happened: Isolated matching omitted the live selector's ranking, text preparation and output limit. Uptake labels also credited advice already present in the prompt.

**Why:** Written, matchable, delivered and helpful are different claims.

**How to apply:** Inspect real receiver text through the live selector, report delivery counts, and withhold hooks in a comparison before calling uptake an added benefit.

Input evidence: L142, L185, L225, L227, L253.

[[w17_owner_prompt_evidence_2026_11_12]] [[landed_hooks_were_never_shown_can_fire_is_not_will_be_shown_2026_10_08]] [[a_hook_that_repeats_its_prompt_scores_as_used_echo_not_help_2026_10_08]]

Drafted by Codex worker W17 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

