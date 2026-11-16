---
name: semantic_rescue_adds_no_recall_hits_costs_tail_slots_2026_11_08
description: "[VERIFIED] Does recall's semantic rescue (BRAIN_RECALL_SEM_RESCUE) help? Paired test 8 Nov, 139 held-out episodes: rescue on 31 hits@8 vs off 35, rescue-only 0, off-only 4 (p=0.125), +1.3 s/call; every loss = gold at rank 7-8 pushed out by inserted notes"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T08:09:27+02:00
  status: verified
  evidence: "12_cognitive_architecture/brain_improvement/semantic_rescue_paired_2026_11_08/out_20261108.jsonl (139 rows) + RESULT_an.txt, RESULT_disc.txt, RESULT_kinds.txt"
---

Question: does recall's semantic rescue (BRAIN_RECALL_SEM_RESCUE=1, which inserts one or two embedding-near notes into the ranked list) find memories that plain recall misses?

Test, 8 Nov (an agent on an agent's harness, semantic_rescue_paired_2026_11_08/semr_paired.py): 139 held-out episodes from the recall episode bank. For each, brain.recall() ran twice on the same query, rescue on then off, and was scored on whether a memory the session actually read appears in the top 8.

Result (139 of 139 episodes, 0 errors):
- rescue ON: hit@8 31/139, MRR 0.121, median 19.1 s per call
- rescue OFF: hit@8 35/139, MRR 0.126, median 17.8 s per call
- episodes only one arm got: rescue-only 0, off-only 4 (episodes 10, 13, 71, 107); exact two-sided McNemar p = 0.125, so the loss is not significant at this size, but rescue never won one
- where both hit, rescue ranked the gold higher 3 times and lower 4 times; the top 8 share 6.42 of 8 notes on average

Every loss has the same shape: the gold sat at rank 7 or 8 with rescue off, and rescue inserted one or two notes above it and pushed it out. In two other episodes (rank changes, not losses) the inserted notes were the generic identity hubs (identity_who_you_are_2026_07_07, narrative_self_and_partner_model_2026_07_08). Rescue never lifted a miss into the top 8. It costs about 1.3 s per call at the median.

Population: 137 of the 139 episodes are the author's own sessions (session_kinds.kind), so this is interactive recall, not script traffic.

Reading: on this bank rescue spends tail slots on near-duplicates of what lexical and graph recall already rank, and gains nothing at the head. The defensible change is rescue off by default, or rescue allowed only to fill slots left empty, never to displace a ranked note. What would change this: a bank where the gold has no lexical overlap with the query (the case rescue was built for); this bank has few such episodes.

Scripts and output: semr_an.py, semr_disc.py, semr_kinds.py, semr_row.py and out_20261108.jsonl in 12_cognitive_architecture/brain_improvement/semantic_rescue_paired_2026_11_08/. Related: [[belownormal_recall_eval_cpu_starved_not_slow_code_2026_11_08]], [[recall_episode_bank_read_trace_dried_up_no_held_out_after_october_2026_11_08]].

