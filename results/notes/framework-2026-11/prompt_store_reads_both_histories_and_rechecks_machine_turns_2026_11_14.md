---
name: prompt_store_reads_both_histories_and_rechecks_machine_turns_2026_11_14
description: "Owner-prompt store missing older prompts from the owner or showing agent ticks as the owner's? Since 14 Nov build.py folds ~/.claude and ~/.codex history.jsonl (8,502 more, back to 18 Mar), masks account numbers and typed passwords, and re-asks machine_turn per ledger row (third-person 'his ... order' ticks)"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T04:55:20+02:00
  status: verified
  evidence: "build_t049_history.txt: 23,569 distinct, 8,502 history-only; t049_thirdp_rule.py on the store: 14 new matches all agent ticks, controls both ways pass"
---

The owner-prompt store (12_cognitive_architecture/owner_prompt_subconscious, build.py) read only PROMPTS.jsonl until
14 Nov 2026. The two typed-prompt histories hold far more: ~/.claude/history.jsonl and ~/.codex/history.jsonl added
8,502 prompts the ledger never had (Claude 7,991, Codex 511), pushing the store to 23,569 distinct prompts and its first
date back to 18 Mar 2026 (the ledger starts 9 Jul).

How the fold works (add_histories): a history row whose text is already a ledger prompt adds nothing; a row with a paste
placeholder ("[Pasted text #1 ...]") matches the ledger by the words before the paste (bisect over sorted 300-char heads),
because the ledger holds the expanded paste and the history does not; a row older than the ledger's first row adds a time
to the matching record; bare slash commands and `!` shell lines are dropped; machine turns are dropped.

Two things the old build leaked and the new one masks: five account numbers (now masked to their last three digits) and one password typed in
a prompt ("password is ..."). The pushed copies before 14 Nov still hold them in git history; the repo is private.

Agent-written ticks: the ledger's origin stamp is set at write time, so a rule added to prompt_origin later does not reach
old rows. Since 14 Nov build.py re-asks machine_turn on every ledger row (STATS ledger_rows_skipped_as_machine_turns), and
prompt_origin has a third-person rule: a turn whose first 120 characters say "(his ... order", "of his ... goal",
"for his ... ask" is an agent's tick. The owner never writes "his" of their own orders. On the store: 43 matches, 29 already caught,
14 new (353 rows, 281 of them one cron tick "Loop tick of his ... order"), none the owner's.

What would change this: a prompt from the owner that does use "his" of the owner's own orders (quoting someone else) - check the
skipped count in STATS against the record list after any rule change.


Related: [[owner_prompt_subconscious_every_prompt_store_and_hook_2026_11_13]] (the store), [[agent_written_worker_briefs_were_stored_as_his_prompts_2026_11_14]] and [[agent_text_counted_as_his_words_2026_11_14]] (the same failure, earlier rules).
