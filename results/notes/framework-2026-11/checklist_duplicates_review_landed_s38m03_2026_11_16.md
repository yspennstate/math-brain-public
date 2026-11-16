---
name: checklist_duplicates_review_landed_s38m03_2026_11_16
description: "[VERIFIED] task_checklist_hook.py duplicates --state <state.json> (landed 16 Nov from Codex S38M03, audit all-hold): read-only list of open checklist entries that are the same ask registered by several sessions; on the live list 19 groups, 38 aliases of 1250 open; precision 1, recall 4/17 on a labelled panel - a review aid, never a merge"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T10:31:25+02:00
  status: provisional
  evidence: ""
---

Built by Codex S37M03, repaired in S38M03 after audit, independently audited (AUD_S38M03, 12 of 12 claims hold). Rebased on the live hook with fuzz 1; selftest 0 failures. Use it to see which of the author's asks are duplicates before reporting the checklist to him; low recall means most duplicates are still missed (paraphrases), so absence of a group proves nothing. Ledger IL-20261116-S38M03. Related [[owner_task_checklist_every_agent_registers_his_asks_2026_09_18]] [[scij06_word_budget_detector_names_coded_labels_2026_11_16]].
