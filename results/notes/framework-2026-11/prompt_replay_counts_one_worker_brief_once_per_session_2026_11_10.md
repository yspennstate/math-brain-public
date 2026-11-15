---
name: prompt_replay_counts_one_worker_brief_once_per_session_2026_11_10
description: "AG hook replay said 82 pct of prompts wake a card? Four cards matching one worker brief that opens ~190 of 400 sessions. Split the author's prompts from script briefs and count a repeated text once before reading a prompt-side rate."
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T02:43:19+02:00
  status: provisional
  evidence: ""
---

status: provisional

A replay of past sessions through the AG hook cards (tools/ambient_rate.py in ~/.claude/agentic) reported that
82.2 pct of prompts woke a card, up from 22 pct one file earlier. The number was four cards, not the family:
AG02436, AG02435, AG02400 and AG02403 each matched a phrase in a worker brief ("speed things up", "You work until
02:46", "a scheduled task starts the next session"), and that one brief opens about 190 of the 400 sampled
sessions. 336 of the 400 sessions were script sessions (headless workers), 64 were the author's.

What to carry:
- A prompt sample drawn from transcripts is mostly worker briefs when most sessions are headless workers. One
  brief template counts once per session it opens, so a rate over "prompts" is a rate over templates weighted by
  how many workers were launched, not over what a person types.
- Before reading a prompt-side rate: split the author's sessions from script sessions and count a repeated prompt text
  once. Until the tool does that, the build's hold (over 0.5 pct of prompts and at least 3 fires) is the safe
  side: it held 13 of the 56 new prompt cards.
- The same phrase can be on target in a brief and noise in a person's ask. "You work until 02:46" really is an
  ask with a duration in it; "speed things up" quoted from the author inside a brief is not a request to
  optimise anything. A card for a person's ask and a card for a worker brief are two cards.

Measurement: replay 8, 10 Nov 2026 02:28, 835 cards, 49,635 tool inputs (6.8 pct wake a card), 454 prompts,
logs/ambient_run8.txt; ledger in 12_cognitive_architecture/brain_improvement/agentic_5k_2026_11_09/TASK.md.
What would change it: a replay split by session kind with repeated texts counted once.
Related: [[a_hook_cards_examples_do_not_measure_its_ambient_rate_replay_and_hold_2026_11_10]]

