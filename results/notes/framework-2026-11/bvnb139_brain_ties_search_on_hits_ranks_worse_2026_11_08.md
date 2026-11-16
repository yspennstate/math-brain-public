---
name: bvnb139_brain_ties_search_on_hits_ranks_worse_2026_11_08
description: "BVNB139 8 Nov: brain 35/139 = clean search 35/139 in first 8, but they find different memories (union 47); merging search top 4 + brain gives 43/139 (+23 pct), MRR 0.21 best"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T17:10:57+02:00
  status: provisional
  evidence: ""
---

BVNB139 (139-question brain vs no-brain recall test, 8 Nov), both arms run as local Codex workers (gpt-6.1-sol, high, normal speed) from codex_local_1108; scored by an agent, who holds the key (scorer brainloop_c462/score_bvnb139.py; results brainloop_c462/bvnb139_scores.json and bvnb139_pair.json; IMPROVEMENT_LEDGER row 45).

Result, hit in the first 8: A brain 35/139 (MRR 0.124), B search 34/139 (MRR 0.176). Paired: 20 both, 15 A only, 14 B only, 90 neither. A tie on hits; when both hit, B ranks the answer higher (11 vs 2). Median seconds A 57, B 6, but B's figure leaves out its prep, so speed is not compared.

Doubts to carry: (1) B is not a clean no-brain control - a wake step showed it a brain digest; (2) A revised answers in a review pass (its originals, answers_A_before_review.jsonl, score the same 35 hits with MRR 0.134, so the review pass did not help). The answer files: bvnb139_worker/answers_A.jsonl and codex_local_1108/briefs/BVNBB/answers_B.jsonl.

What it says: on this bank the brain arm finds as many answers as plain search and ranks them worse, at about ten times the time. 90 of 139 found by neither arm points at the bank (or the store's coverage) more than at either method. What would change it: a rerun with B launched with hooks off (NOHOOKS in the brief dir) so it is a clean control, and a check of the 90 misses for whether the answer card exists in the store at all.


Related: [[hunt150_i2_c2_rerun_both_arms_complete_cost_splits_2026_11_08]] [[semantic_rescue_adds_no_recall_hits_costs_tail_slots_2026_11_08]]


## Clean rerun of the search arm (B2), scored 8 Nov 18:45

Arm B saw the wake digest, so B was rerun clean as B2 (local Codex, gpt-6.1-sol high, normal speed, no hooks, plain filename/text search only). Scored with score_bvnb139.py (key in brainloop_c462):

| arm | hits in first 8 | MRR | real prompts (137) | mean seconds |
|---|---|---|---|---|
| A brain | 35/139 | 0.124 | 33 | 212 |
| B search, saw wake digest | 34/139 | 0.176 | 32 | 8 |
| B2 search, clean | 35/139 | 0.202 | 33 | 444 |

Paired A vs B2: 23 hit by both, 12 only by the brain, 12 only by search; sign test p = 1. The union is 47/139. So the brain and plain search tie on whether the needed memory is found and search ranks it higher, but they find DIFFERENT memories: a brain-then-search (or merged) answer would lift hits from 35 to at most 47, about a third more. The B2 seconds are inflated by a starved PC (commit 0.96-0.97 all run) and include the worker's own reading, so they are not a speed result.

What would change this: a merged arm (brain top 4 + search top 4) run on the same 139, to see how much of the 47 survives an 8-slot cap.

### Merged arm, computed offline from the two answer files (18:47)

No new run: each question's brain list (A) and clean search list (B2) merged, duplicates dropped, cut at 8. Four orders, all scored with score_bvnb139.py:

| merge | hits /139 | MRR | real /137 |
|---|---|---|---|
| search top 4, then brain | 43 | 0.212 | 41 |
| interleave, brain first | 43 | 0.157 | 41 |
| interleave, search first | 42 | 0.207 | 40 |
| brain top 4, then search | 42 | 0.134 | 40 |

Every order lands at 42-43, so the gain does not depend on the choice: 35 -> 43 is +8 hits (+23 pct), keeping 8 of the 12 that only one side found. Search-first keeps search's better ranking (MRR 0.212, the best of all arms). Caveat: two runs cost both runs' time; the search arm is cheap when it is fast (arm B took 8 s a question), so the practical recipe is plain search for the first slots and the brain to fill the rest. Script: 12_cognitive_architecture/codex_local_1108/briefs/BVNBB2/merge_ab2.py.
