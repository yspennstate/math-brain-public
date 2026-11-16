---
name: recall5_crossover_question_lead_top1_10_to_19_of_48_p0p004_2026_11_08
description: "Do plain-question descriptions lift recall on randomly chosen memories? Yes (8 Nov): pooled 48, top-1 10 to 19, 9 gained 0 lost, sign p 0.004; HOLD4 alone 4 to 9 (p 0.06); drift 1-2 places"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T11:30:23+04:00
  status: verified
  evidence: "~/codex_fleet/20261108_pro/workers/RECALL3s/SCORE5.json; GitHub 0f91a3f094 12_cognitive_architecture/brain_improvement/recall5_2026_11_08"
---

Do plain-question descriptions lift recall when the memories are picked at random? Yes (8 Nov 11:29), settled by the RECALL5 crossover. The 48 memories RECALL3 had left alone were split by seed 1108 into TREAT4 and HOLD4. RECALL4 rewrote TREAT4's descriptions. RECALL5 had a fresh blind Codex writer (gpt-6.1-sol high, `blind: yes`, bodies only) rewrite HOLD4's, applied all 24 at 11:13:16, and reran the same 120 questions.

- Pooled over all 48 treated memories, top-1 went from 10 to 19: 9 gained, 0 lost, sign p = 0.0039 (the co-primary).
- Top-5 went from 19 to 29 (11 gained, 1 lost, p = 0.0063). Top-20 went from 29 to 35 (6 gained, 0 lost, p = 0.031).
- HOLD4 alone (the primary) went from 4 to 9 (5 gained, 0 lost, p = 0.0625), short of 0.05 just as TREAT4 alone was in RECALL4. Three of its absent items came back, one straight to rank 1.
- Drift was small. The index grew by about 1,700 documents between runs. TREAT4 had three items move by one or two places, EDIT_APPLIED lost one at top-20, and W114_LEAD did not move.

Read it as about +19 points at top-1 on memories nobody had tuned. That is half the RECALL3 cross-sectional gap (27 of 47 against 10 of 48). The rule stands: lead a description with the question it answers.

A procedure scar for the next recall A/B: with BRAIN_RECALL_REFRESH=0 the edited memories are invisible until the lexical index publishes again. A recall spawns that publish only once the index is at least 600 s old (BRAIN_RECALL_SPAWN_AGE); otherwise the 15-minute task does it. So after an edit, wait for bm25_index.json.gz's mtime to pass the edit (or run one plain recall after the 600 s mark) and check the scan's placed count before you run. Also move the old after_* files and AFTER.tsv aside, because run_recall.py resumes from an existing AFTER.tsv.

Files: ~/codex_fleet/20261108_pro/workers/RECALL3s (PREREG5.md, SCORE5.json, AFTER.tsv private; RECALL4's after-run is in AFTER4.tsv and attic_recall4_after/), RECALL1b/apply5.py, backups5/, APPLIED5.jsonl. The writer's audited log has 8 commands and reads nothing outside its folder but ../../RULES.md. Pushed 0f91a3f094 to 12_cognitive_architecture/brain_improvement/recall5_2026_11_08 (ids, groups, ranks and hashes only).

Related: [[recall4_randomized_question_lead_desc_top1_6_to_10_hold_flat_p0p11_2026_11_08]] is the first half. [[recall3_blinded_bank_edited_desc_top1_27_of_47_vs_10_of_48_2026_11_08]] is the cross-section. [[codex_blind_brief_override_in_first_message_hooks_off_0_outside_paths_2026_11_08]] covers how the writer stays blind.

Later (8 Nov 14:46, an agent): the rule is not followed unprompted (53 of the 60 newest memories lacked a question lead); remember now warns, and RECALL6 rolls it out on 200 memories with 40 measured. See [[new_memories_skip_question_lead_53_of_60_remember_now_warns_2026_11_08]].

Later (8 Nov, RECALL6): on a fresh batch of 200 that already recalled well (top-1 16 of 40), the rule moved top-1 to 18 (2/0, p 0.5) with controls flat; the preregistered rollout stopped. See [[recall6_rollout_200_question_leads_top1_16_to_18_p0p5_stops_2026_11_08]].
