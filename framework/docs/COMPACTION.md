# Compaction: how sessions compact and what is kept

The agents that build and test the brain run for hours or days in one session. Every model call
re-reads the whole context, so the cost of a turn is the size of the context, not the size of the
new message. In one measured session on 9 October 2026 that was about 663,000 tokens a turn.
Compaction replaces the conversation so far with a written summary and the session continues from
it. This document describes how compaction is configured, when it is triggered, what the summary is
told to keep, how every summary becomes a node in the brain, and what went wrong on the way. The code
is in `framework/dreaming/`; the aggregate measurements are in Appendix I of
`papers/math-brain-2026-10-24` (`sections/I_compaction.tex`).

## The harness

What follows was read from the Claude Code binary and checked against session transcripts.

- Automatic compaction summarizes the conversation when context use approaches `autoCompactWindow`,
  a settings key between 100,000 and 1,000,000 tokens. The threshold is the smaller of that key and
  the model's window. The same knob exists as the environment variable
  `CLAUDE_CODE_AUTO_COMPACT_WINDOW`; `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` sets a percentage instead.
- The window is read when a session starts. A session that was running when the setting changed keeps
  compacting near the old limit: one session that started on 1 October compacted seven times on
  9 October at 966,643 to 969,909 tokens, two hours after the window was set to 300,000.
- A `PreCompact` hook receives the trigger (manual or automatic). Whatever it prints is handed to the
  summarizer as instructions. A `PostCompact` hook receives the trigger and the summary text.
- A hook cannot compact a session. No hook output field does it. An agent cannot type `/compact` to
  itself in an interactive session either; that is the user's command.
- Codex has no compaction hook. Its rollout files carry a `compacted` record, and it compacts at
  `model_auto_compact_token_limit` in `~/.codex/config.toml`. In the Codex build used here the record's
  message is empty and the summary is encrypted, so the text cannot be read back from the rollout.

## Settings

Both runtimes compact at 300,000 tokens: `autoCompactWindow` 300000 in `~/.claude/settings.json` and
`model_auto_compact_token_limit` 300000 in `~/.codex/config.toml` (it had been 800,000). The window
has to sit above the context a session carries right after a compaction. Here that baseline is
140,000 to 160,000 tokens: the summary, the kept tail of the conversation, the system prompt, tool
definitions and hook output. A 200,000-token window tried for headless workers sat close enough to
that baseline that sessions compacted every few minutes and the harness reported that auto-compact
was thrashing. Measure the baseline before choosing a window.

## Compacting by task, not only by size

A summary written when a subject is finished loses less than one written in the middle of a subject.
So 53 hooks (`compact_hooks.jsonl`, fired by `compact_hooks.py` on Claude through the hook dispatcher
and on Codex through `hooks.json` with JSON output) watch for the end of a piece of work and tell the
session to bring it to a stopping point. Their signals:

- a task closed on the checklist, a final report, a push, a commit, a released claim, a handoff sent,
  a report or gate decision written, tests passing, a checkpoint written;
- the user switching subject or correcting the agent (the correction goes on disk first);
- size: context bands from 200,000 to 500,000 tokens, a large tool result that now rides in every
  turn, many whole-file reads, long runs of small steps;
- an idle gap on a large context, repeated failures, a background job without a recorded handle;
- right after a compaction: start from the NEXT line, check claims and inbox, treat the user's newest
  words as current, answer from the records rather than the old context.

Each hook has a cooldown, at most one fires per action, small routine commands stay silent, and fires
are logged to `~/.claude/brain_graph/compactions/hook_fires.jsonl`. `compact_math.py` selects hooks for
mathematical work: a finished proof, a Lean compile or a resume pulls a compaction hook, an unrelated
computation does not.

Since no hook can compact a session, `compact_on_task_end.py` does it from outside. On `Stop`, when the
turn closed a task (a checklist `done` command outside a heredoc, or the end-of-task line) and the
context is 150,000 tokens or more, it starts a windowless helper that waits until the session is idle
and types `/compact` into it. Idle needs three things: the last turn ended, no queued prompt or loop
fire after it, and 15 seconds without keyboard or mouse input, so the keys never land inside text the
user is typing. The first version judged idle by the last assistant record alone and was wrongly
recorded as a failure: the keys had arrived, Claude Code queued `/compact`, and ran it at the end of a
turn that had started 16 seconds earlier. A `/compact` typed into a busy session is queued, not lost.

A headless worker compacts best by ending: one task per session, the next seeded from its NEXT line.
For Codex, `codex_manual_compact.py` saves a summary the agent writes itself (it must contain a NEXT
line) as a compaction node, because the harness's own summary is unreadable.

## What the summary is told to keep

On `PreCompact`, `compact_nodes.py` tells the summarizer to keep the open requests in the user's
words, task ids, commit hashes, file paths, held claims and the session's NEXT line, and never to copy
test questions or answer keys. Two scars shaped this list:

- A summary keeps what was written down, not the reasoning or the work that was done. On 24 September
  an agent told a peer that an experiment had never been run; two complete runs from before its
  compaction were on disk. After a compaction, search the artifacts, not the summary.
- A long `/goal` condition judged on the visible transcript can never read as met once the transcript
  has been compacted. Recognize that and do not loop on it.

## Every compaction is a node

On `PostCompact`, `compact_nodes.py` saves the summary as a node under
`~/.claude/brain_graph/compactions/<date>/` and an anchor memory of the same name in the memory folder.
The anchor holds the request, the pending work, the current work and the next step, and links to:

- a hub memory that describes compaction;
- the same session's previous compaction;
- the checklist tasks open under the session's agent, and other sessions' compactions on those tasks;
- the five memories recall finds closest to the summary.

The graph rebuild turns those links into edges, so recall can reach a session's compactions by
question. `INDEX.jsonl` holds one row per node (time, runtime, session, trigger, length, sha256, task
ids, previous node, related memories). An anchor whose summary mentions test material carries no
excerpt and is marked `test_adjacent`; the full text stays local. Compactions never enter the math
store: copying them in would carry test material and private review text, so the store grows from
memories instead.

`compact_nodes.py --sweep` backfills from Claude transcripts (the `compact_boundary` record and its
summary) and from Codex rollouts; the hook dispatcher starts it windowless at most every 15 minutes,
under a lock. `--list` counts compactions read-only, `--relink` adds related links later, and
`--paths-file` runs a disjoint shard in parallel. `compact_index.py` maintains the index. By 26 October
the index held 11,581 nodes: 10,158 from Claude sessions and 1,423 from Codex.

Two hooks close the loop with the session itself. Right after a compaction a session is told whether
its summary became a node, and how to rebuild it if not. `keep_working_after_compact.py` handles an
agent that writes a recap after compacting and stops while its tasks are still open: on the first
`Stop` after a compaction, and only when the checklist holds open entries under that agent, it answers
`{"decision": "block"}` and lists the open work. It fires once per compaction and never while a stop
hook is already active. An agent with nothing left says so in one line and stops. `wake_cached.py`
answers `SessionStart` with source `compact` by handing back the wake text the session already
received. Re-running the full wake after every compaction had stalled agents for 160 to 390 seconds
each time.

## What went wrong, and the fixes

- Lost to encoding (9 October). The hook read its input in the console code page, and a lone surrogate
  made the UTF-8 write fail. It now reads bytes as UTF-8, and a lone surrogate becomes U+FFFD.
- Only one node, in a place nobody looked (9 October). The early nodes lived only under
  `brain_graph`, where neither recall nor the graph reads, and only one compaction had ever been saved.
  The anchor memories fixed both.
- Busy sessions dropped (14 October). The backfill matched a transcript compaction to a hook row
  within 600 seconds by time alone, so a worker that compacted two or three times in ten minutes lost
  the later ones: 1,012 of 1,764 between 2 and 11 October. A match now needs 80 percent text overlap
  within 120 seconds, and targeted saves restored the missing nodes.
- Wrong session (12 October). A subagent's compaction reaches the hook with the parent's session id
  and no agent id, and the agent's own compact record is appended only after `PostCompact` returns. A
  late pass and the sweep now file it under the right agent (84 repaired). Workflow stream agents had
  also been filed under their coordinator.
- Codex (10 October). No Codex compaction had ever become a node: the record's message was empty, the
  summary encrypted, and the sweeper cut session ids to 35 of 36 UUID characters. Codex now gets
  metadata-only nodes, kept away from test working directories, plus the manual summary above.
- Off-topic links (14 October). Recall's top five were 55 to 62 percent on topic in a blind check. A
  rare-word overlap gate (above 0.03 by memory document frequency) raised that to about 83 percent, and
  the linker now reads the summary without session plumbing (identity blocks, standing constraints,
  launcher prompts). In a blind check of 20 nodes, all 8 that had no links gained some; of the 12 that
  had links, 5 got better, 3 got worse and 4 were unchanged.
- False notes (14 October). The hook said a claim had been released after a `--help` call. Its
  claim-released and gate-written notes now read the command and its result. Replaying 111,785 tool
  calls removed 66 false notes and added none. The hook also moved inside the dispatcher process, which
  cut the median `PostToolUse` time from 0.28 to 0.08 seconds.

## Measuring a compaction

The `postTokens` field of a compaction record (median about 19,000 tokens) is not what the next call
reads. The next call carries the summary plus the kept tail of the conversation and the hook output,
about 165,000 tokens in the sessions checked. Measure both sides from the API usage of the calls
around the boundary. Removed context is not billed tokens saved: that depends on the later calls,
caching and the cost of writing the summary. Appendix I of the paper gives the aggregates (8,416
compactions in 1,254 transcripts, a median reduction factor of 13.8) together with what they do and
do not measure.
