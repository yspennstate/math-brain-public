---
name: reflex_prefilter_three_pieces_edits_live_at_compile_2026_11_14
description: "Reflex hook slow, or editing instinct_anchors.py? Pre-check keeps up to 3 required pieces per trigger since 14 Nov (197->162 ms/call, 0 fires lost on 36k pairs); an edit to the module goes live at the next compile by any agent - develop on a copy"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T03:06:07+02:00
  status: verified
  evidence: "commit ec401ed2; audits/reports/2026/11/14/prompt_to_rules_audit/evidence"
  lesson: true
---

The reflex hook's pre-check (instinct_anchors.py) used to keep one required literal per trigger, so a trigger shaped
"paper word ... then push word" passed whenever either word appeared and the full regex then ran its long lookahead.
Since 14 Nov 2026 02:5x it keeps up to three required pieces per trigger (all must appear), for 87 of 681 triggers.

Measured, same process, same inputs, old sidecar against new: 197.1 -> 162.1 ms of matching per tool call on 1,000
tool calls of a live session (box under load); 78.9 -> 67.8 ms on 1,500 calls earlier on a quieter box. 0 fires lost
on either set.

Soundness: the module's own harness (`instinct_anchors.py --verify`) did not finish in 30-40 min on this laptop,
twice. The check that did: the landed filter was already sound, so the regex only has to run where the new filter
skips a pair the old one passed. 5,500 texts (4,000 prompts, 1,500 memory bodies), 36,309 such pairs, 0 fires, 6 min.
A filter that skips everything reports 43 unsound pairs on 250 texts, so the check can fail.
Scripts and evidence: 12_cognitive_architecture/audits/reports/2026/11/14/prompt_to_rules_audit/ (scripts/diffcheck.py,
evidence/diffcheck_5500_texts_unsound0.txt, evidence/anchors_ab_1000_calls_after_land.txt). Commit ec401ed2.

The trap found on the way: instincts.py calls instinct_anchors.build() after every compile, and the hook imports
could_match from the module file. An edit to instinct_anchors.py on disk goes live at the next compile by ANY agent,
verified or not. Develop on a copy (here instinct_anchors.py.cand_t049_conj) and copy it in only after the check.

Rollback: ~/.claude/dreaming/instinct_anchors.py.bak_t049_conj_20261114 and instinct_anchors.json.bak_t049_conj_20261114.
Related: [[reflex_triggers_are_prefiltered_by_required_literals_2026_09_14]], [[audit_prompt_to_rules_2026_11_14]].

