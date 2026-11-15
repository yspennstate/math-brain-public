---
name: prompt_class_ledger_dark_23_days_cleared_tool_reads_heads_2026_11_12
description: "Prompt-class ledger dark since 20 Oct, alarm on wake? Cleared 12 Nov: 10-12 Nov classified (43,489 rows); prompt_class_tool.py hands the pass only the author's unique typed texts; 21 Oct-9 Nov still open"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T19:42:54+02:00
  status: verified
  evidence: "hook_liveness line 12 Nov 19:3x: prompt-class ledger 11-10 575/575, 11-11 1425/1425, 11-12 1374/1386 - ok; apply_prompt_classes.py merged 43489; sidecar ~/.claude/dreaming/prompt_classes_agent_20261112.jsonl"
---

The prompt-class pass (SWS section P) wrote no class_model from 21 Oct to 12 Nov 2026. Measured on the whole ledger (memory/prompts/PROMPTS.jsonl, 121,995 rows): last classified day 2026-10-20; 1-12 Nov held 48,411 rows, 19,418 stamped owner, none classified.

Why it stopped, as far as the numbers show (my reading, not a logged cause): the instruction was "read yesterday's lines missing class_model". By November a day was 3,000-5,000 rows, of which the words the author typed were 15-120 unique texts; the rest were loop re-fires (repeat_of set, the same text hundreds of times) and headless-worker prompts. A pass with a 45-minute budget cannot read 4,000 rows, so it skipped the section.

What I did (an agent, 12 Nov, about 19:15 to 19:35, claim topic:prompt-class-ledger-backlog):
- Read and classified the unique owner texts of 10, 11 and 12 Nov (121 + 81 + 87, minus 3 typed on two days = 286 verdicts), boundary rules of section P, correction_present judged separately on each. Seven were machine-written prompts stamped owner (an agent's rewritten loop text, a startup test); those carry class automation and origin automation.
- Two mechanical rules for everything since 20 Oct: a text whose every row has origin automation gets class automation (2,541 texts, 37,752 rows); an unclassified owner row whose text already carries a class elsewhere inherits it (10 texts, 997 rows).
- One apply_prompt_classes.py run: 43,489 rows classified, tail-race guard carried 10 fresh lines. Sidecar ~/.claude/dreaming/prompt_classes_agent_20261112.jsonl.
- Verified two ways: a per-day recount (10 Nov 575/575 owner rows, 11 Nov 1,425/1,425, 12 Nov 1,374/1,386 with new rows still arriving) and hook_liveness.py, whose line now reads "prompt-class ledger 11-09 0/129, 11-10 575/575, 11-11 1425/1425, 11-12 1374/1386 - ok".

The standing fix: ~/.claude/dreaming/prompt_class_tool.py (count / heads DAY.. / build OUT DAY.. / mech OUT) does the mechanical half and hands the model only the unique texts the author typed; section P of dream_prompt_sws.md now says to use it and not to read the raw day. Scope stays "all" as in the 13 Oct sidecar, so a loop's re-fires keep the class of the order the author typed and remain the author's in the prompt layers (owner_prompts_hourly._is_owner drops class automation rows, so classing the author's re-fires automation would have removed the "re-fired xN" counts from the author's feed).

Still open: owner rows of 21 Oct - 9 Nov, about 610 unique texts (41, 47, 18, 9 for 9, 8, 7, 6 Nov). Newest first with the tool. The alarm trips again only if a completed day goes dark, so the nightly pass has to run the tool; if the 13 Nov SWS journal does not show section P done, that is the next bug.

What would change this: if the dream's own prompt is regenerated from a canonical copy that lacks the new paragraph, the instruction is lost; the canonical copy under 12_cognitive_architecture/dreaming was updated the same hour.

Related: [[owner_directive_every_prompt_saved_and_classified]], [[autostash_1837_rest_of_tree_restored_and_guard_refuses_tree_moves_2026_11_12]].

