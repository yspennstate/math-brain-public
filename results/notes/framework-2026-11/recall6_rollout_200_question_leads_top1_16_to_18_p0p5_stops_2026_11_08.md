---
name: recall6_rollout_200_question_leads_top1_16_to_18_p0p5_stops_2026_11_08
description: "Did the question-lead rule carry to a fresh batch of 200 memories? Not measurably (RECALL6): top-1 16->18 of 40 (2/0, p 0.5), control 13->13; rollout stops, high baseline"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:23:59+04:00
  status: verified
  evidence: "~/codex_fleet/20261108_pro/recall6/RESULTS6.md; score6.log; pushed 3719d66df9"
---

Did RECALL5's question-lead rule carry to a fresh batch of 200 memories? Not measurably (8 Nov, RECALL6, preregistered). Top-1 on the 40 rewritten memories went from 16 to 18 (2 gained, 0 lost, sign p 0.50). The 40 untouched controls stayed at 13. Top-5 went 27 to 30 against 26 to 26, and top-20 31 to 35 against 33 to 33. No crowding harm. Under the preregistration the rollout stops. The 200 edits stay in, since they did no measured harm and a revert would be one more change.

Why this differs from RECALL5 (10 to 19 of 48): this batch already recalled well before any edit (16 of 40 at top-1, 27 at top-5), so there was little room, and 40 items cannot resolve a 2-item gain. Every move went the right way (top-1 2/0, top-20 4/0). What is missing is power, not direction. A next test needs memories that recall badly now (top-1 near a quarter) and about 100 per arm.

How it ran: descriptions written blind by Codex RECALL6W; 80 questions written blind by RECALL6Q from bodies with the slug masked, frozen and pushed before any recall. Baseline pass 1 straddled an index republish; pass 2 on a settled index gave the same top-1 counts. The after-pass ran once the index and the fresh-vector overlay were both rebuilt after the 15:14:20 edits.

A wait-loop trap I hit: bm25's .attempt files are per-generation markers that stay after a build, so "no .attempt file" never comes true. Wait on bm25_index.json.gz.postings.build.lock and a quiet mtime instead.

Files: ~/codex_fleet/20261108_pro/recall6 (RESULTS6.md, BASELINE6.tsv, AFTER6.tsv, score6.log, APPLIED6.jsonl). Pushed 3719d66df9 to 12_cognitive_architecture/brain_improvement/recall6_2026_11_08.

Related: [[recall5_crossover_question_lead_top1_10_to_19_of_48_p0p004_2026_11_08]] - the result this tried to roll out.

