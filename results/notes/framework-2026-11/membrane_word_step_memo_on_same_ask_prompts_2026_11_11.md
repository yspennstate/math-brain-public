---
name: membrane_word_step_memo_on_same_ask_prompts_2026_11_11
description: "[PROVISIONAL] Membrane word step slow on loop prompts (~200 ms)? Since 11 Nov the raw BM25 hits are kept per session, keyed on query + index signature; same output, repeat 5 ms"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T02:34:40+02:00
  status: provisional
  evidence: ""
---

Question: the membrane's word step (the author's ask's words through BM25, judged on every prompt) costs about 200 ms of a prompt's evaluation. Does a loop prompt have to pay it again?

No, since 11 Nov 02:2x (an agent). A loop re-fire repeats the author's ask word for word, so the word step scored the same query on every tick. live_membrane.py now keeps the raw BM25 hits in the session state (st["bm25_memo"]["word"]). The key is the query text, topk and the postings header (signature, n, avgdl), so a rebuilt index scores again. The memory rows, the supersession hand-over and the seen filter still run fresh on a hit, which makes the result equal to a recompute. BRAIN_MEMBRANE_MEMO=0 turns it off. Backup: live_membrane.py.bak_wordmemo_20261111. Mirror: 12_cognitive_architecture/brain_graph/bin/live_membrane.py, which also carries the peer's one-query order lookup; that change had not reached GitHub before.

Checked on a copy. 17 controls pass (scratchpad lm_test.py): output equal to the plain call on a miss and on a hit read back through JSON, a newly seen slug filtered on a hit, another generation ignored, the switch off honoured, a different ask scored again, state 2.9 KB. End to end, old against new run() with every write redirected to a temp folder, three prompts with the same ask: the returned text and every fire-row field were identical apart from the step timings. The word step was 161-203 ms in the old module and 5 ms in the new one on the repeats, under load (box at 86-88 pct commit, PowerShell start over 30 s).

Not changed: the orders step (about 360 ms per prompt) recomputes because its query includes the names of what the session touched, which change every prompt. Making it reuse leaders on prompts would change the prospective_orders_check record, so that stays with the membrane's owner (proposal sent to an agent, topic graph-membrane-orders-cost, unanswered). The test_live_membrane.py negative controls write to the live sessions folder and create the live STOP file for a moment, so they were not run against the live paths; run them only with LM.SESS and LM.STOP redirected.

What would change this: profile rows after 02:30 in which graph_membrane_hook's prompt median does not fall on loop ticks.

Related: [[membrane_order_lookup_one_query_not_300_2026_11_10]] [[checklist_same_ask_fast_path_skips_the_state_parse_2026_11_11]] [[prompt_wait_is_the_in_process_hook_sum_not_the_spawned_hooks_2026_11_10]]


Measured in production, 11 Nov 03:0x (live fires.jsonl, word step = the 'word' mark minus the 'eval' mark, prompts where the evaluation ran): the win is smaller than the test suggested. Before the memo (23:00-02:30 local) the word step already took under 20 ms on 346 of 637 evaluated prompts (54 pct, median 0); after it (02:30-03:05) 138 of 220 (63 pct, median 1 ms). The memo adds about 9 points of prompts that save some 250 ms each: roughly 25 ms per prompt on average, not 200. The reason is that the index publishes about 10 times an hour, so a session ticking every 3 minutes usually meets a new generation and its key misses. A memo keyed on the index generation pays off only when the generation outlives the gap between prompts. The same check ruled out a matching memo for fok_probe's BM25 score.
