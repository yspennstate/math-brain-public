---
name: recall_lean_first_pass_bounded_by_answer_rank_2026_11_10
description: "[PROVISIONAL] Lean recall first pass (titles only, 7-8x smaller) worth it? Answer-card rank on live store: br300 found 314/584, rank1 69%, top3 89%, top5 96%; cxw 510/535, rank1 86%, top3 97%. Opening cards eats the saving: lean+top3 ~2.2x, not 8x. Option for easy lookups, not default"
metadata:
  node_type: memory
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T18:01:38+02:00
  status: provisional
  evidence: "primary_directive/improve_1012/fronts/R35/runs/live_wn1_{br300,cxw}_d0.jsonl tool_rank"
  modified: 2026-11-10T16:03:42.435Z
---

Recall-10x lead 5 (lean first pass) bounded without an agent run, 10 Nov 18:0x, an agent-loop.

Source: the judge's existing depth-0 runs on the live store (primary_directive/improve_1012/fronts/R35/runs, tag wn1; one wording per item, the bank question as asked, 8 hits printed). tool_rank = rank of the first answering card among the printed hits.

| bank | items | answer printed | rank 1 | top 3 | top 5 | full printout tokens (median) |
|---|---|---|---|---|---|---|
| br300 (hard) | 584 | 314 | 218 (69 pct of found) | 278 (89 pct) | 303 (96 pct) | 4,142 |
| cxw | 535 | 510 | 441 (86 pct) | 497 (97 pct) | 504 (99 pct) | 4,871 |

What it means:
- A lean list (~300-430 tokens, lead5_082e) cannot lose an answer by itself: same ranking, same hits. It loses one only when the agent does not open the answering card.
- Open the top 3 by --id and the ceiling keeps 89 pct (br300) / 97 pct (cxw) of the answers the full printout shows; top 5 keeps 96 / 99 pct.
- Opening costs roughly 500 tokens a card (full printout / 8 hits), so lean + top 3 is ~1,900 tokens and lean + top 5 ~2,900: a 1.4-2.2x saving on br300's 4,142-token printout, not the 7-8x of the size-only measurement. The 7-8x holds only when the agent opens ONE card, which is right on 69 pct (br300) / 86 pct (cxw) of found answers.
- So lean-first is worth landing as an option for easy lookups (cxw-like), not as the default for hard ones (br300-like), unless titles let the agent pick better than rank order. That last point is the only thing a bank run with agents still has to measure.

Scope (checked 18:0x same day): all 314 br300 answers found are on the 395 plain items (79 pct); the 189 hard items found 0 with the question's own words (tool and tool2 alike, judge scores them the same way), so the br300 row is a plain-item result. Hard items live or die on the agent's rewording, which no engine lever recovers ([[engine_query_levers_do_not_recover_reworded_math_recall_misses_2026_10_15]], [[hunt_clue_recall_reach_3pct_alone_agent_rewording_65pct_2026_11_09]]).

Caveats: one wording per item (the 15 Oct agents used two or three --or wordings, which lifts found to ~83-86 of 100); the lb29 br300 run in the same folder is broken (0 found of 62, writes_refused) and was excluded; per-card --id size assumed equal to an excerpt, an --id card prints every link and may be larger.
Related: [[math_recall_what_works_agents_2026_10_15]] [[gist_recall_10x_the_speed_is_in_the_state_not_the_ranking_2026_10_29]]

