---
name: math_hook_repeat_memo_keeps_generic_and_no_chosen_verdicts_2026_11_12
description: "Math hook slow on a loop tick (1-5 s, same prompt again)? Its repeat memo kept only two verdicts until 12 Nov. It now also keeps generic_only_match and no_chosen_after_select for 2 h, across compactions, while the session's shown-ids shard is unchanged: 683 of 717 full runs in three days answered in 20 ms. 20 of 20 tests."
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T02:51:29+02:00
  status: provisional
  evidence: "agent_run/math_repeat/judge.txt (20 of 20; the old file 0 of the 6 cases meant to move), gain2.txt (683 of 717); ledger row of 12 Nov (m). Provisional until live rows of skip_repeat_known:generic_only_match appear"
---

The math hook (`math_sense.py`) runs in-process on every prompt, so its time is time the prompt waits. Its median is about 40 ms, but its mean was six times that: in the profile of 11 Nov 16:39-22:03 (1,626 prompts) the runs that reached ranking carried most of the time, and most of those were loop sessions sending the same tick again. The 5 Nov repeat memo answered only two verdicts (`incoherent_weak_block`, `all_dedup_suppressed`), both scoped to one context.

Two more silences, `generic_only_match` and `no_chosen_after_select`, are reached before the shown-ids guard. The prompt and the store decide them; the only thing of the session's that ranking reads before them is its shown-ids shard, through the use layer, and that shard is written only when a block is served. In the three days to 12 Nov, 717 full runs ended in one of the two, 688 on a prompt identical to one the same session had sent in the two hours before, 595 of those across a compaction. A run ending in `generic_only_match` took a median 1.4 s; a memo answer takes 20 ms.

Since 12 Nov the memo keeps both for two hours, does not scope them to the context, and answers only while the session's shard has the size and write time it had at the record. `MATHBRAIN_REPEAT_STORE_ONLY=0` restores the old memo. `judge_ms.py`: 20 of 20, the old file 0 of the 6 cases meant to move, dial-off equal to the old file on all 19. Replay of the three days under the new rule: 683 of 717 full runs answered from the memo, all in 4 loop sessions. Backup `math_sense.py.bak_repeatwide_20261112`.

What the same look found and left alone: 221 of the 234 math blocks served in three days were a session's same first card served again after a compaction (3 to 5 s each), which is the 5 Nov per-context rule working as written; whether a loop tick needs its card back after every compaction is the math lane's call. The 40 s runs of 11 Nov 18:39-18:42 were the box stalling, with fok_probe at 17.8 s in the same dispatch. `trading_text` (766 rows, 245 ms median) is prompt-only and could join the memo.

To check a memo change here, drive `_silence_note` and `_repeat_known_silence` on a module loaded with `HOME` and `SESSION_DIR` pointed at a scratch folder and `_repeat_ctx` replaced; a real session id in a test otherwise writes into the production silence log. Related: [[math_prefilter_per_token_sidecar_load_665_to_40_ms_2026_11_11]], [[rank_prompt_hooks_by_wait_parallel_children_are_off_the_critical_path_2026_11_11]], [[the_silence_log_was_counting_my_own_measurement_traffic_2026_09_13]].

