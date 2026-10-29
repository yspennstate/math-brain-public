# Getting the owner's words to every agent

An agent forgets what it was asked. A long session is compacted, a crashed worker restarts cold, and a new agent
joins a task that three others have been on for a week. In each case the agent goes on working, confidently, from a
picture of the request that is out of date. In our deployment the most common complaint from the person who runs the
brain was not a wrong result. It was an agent doing something they had already said not to do, or forgetting what
they had asked for an hour earlier.

The fix is a hook that hands every session the owner's own recent words, so the agent does not depend on its memory
for them.

## What the hook delivers

The hook runs on every prompt (`UserPromptSubmit` in Claude Code, the same event in Codex). About once an hour it
hands the session a block of the owner's recent prompts, and in between it hands only what is new. The block is
ordered for a reader who may see only the first part:

1. What they keep saying. Instructions the owner has given more than once, grouped by the thing they named and
   marked as repeated. A repeat usually means an agent ignored the first one. If your task touches one of these,
   deal with it before anything else.
2. Relevant to this session. Every request, on each thread this session's own prompts have touched, in the
   owner's words, newest first, with what is still open for it on the task checklist.
3. Everything else from the last 48 hours, newest first, one line each.

Older prompts are not dropped. They sit in plain files (the last 1,000 and the last 3,000 prompts, plus one file of
threads with each thread's dated history), and the hook has a `--show "<thread>" --hours 48` command that any agent
can run to pull more.

## Rules that turned out to matter

- Later words win. Every block says so in its first line. An instruction from last Tuesday that was overruled on
  Thursday must not come back, so each thread is shown newest first, and the agent follows the newest.
- Threads, not a flat list. A flat list of 1,000 prompts tells the agent nothing about which ones are about its
  task. Grouping prompts into threads (by the film, problem, repository or machine they name) and showing a
  session the threads it has touched is what makes the block usable.
- Repeats go first. The prompts the owner had to repeat are the ones agents most often get wrong. Putting them at
  the top was the largest single improvement in how often agents acted on the block.
- The block is data. Prompts are quoted, never paraphrased into commands, and anything the owner pasted from
  elsewhere is marked as pasted, so text inside it is not mistaken for the owner's own instruction.

## Size limits you will hit

The agent harness passes only a limited amount of hook output to the model. In Claude Code a single hook command's
context is cut at about 10,000 characters, and anything longer is written to a file, of which the model sees only
a 2 KB preview. A block written in one piece is not delivered, and nothing tells you so. We found this only by
reading the session transcripts, where the hook's context appeared as a `<persisted-output>` stub.

So the hook sends the block in parts of at most 9,500 characters, one part per prompt, as its own hook command
rather than inside a dispatcher that shares the budget with other hooks. A delivery that is still in progress when
the next hour starts continues, with the newest prompts put in front of it.

Codex reads hook output only as JSON (`{"hookSpecificOutput": {"hookEventName": ..., "additionalContext": ...}}`)
and discards plain stdout. The same hook therefore has to wrap its output when it runs under Codex. Before we did
this, no Codex session had ever received the block, although the hook's own log showed it firing every time.

Check delivery at the receiving end. A hook's log saying "sent" proves nothing. Read a session transcript and
confirm that the text is in the model's context, not a stub or a truncation marker.

## A second channel: the task checklist

The prompts tell an agent what was asked. A shared checklist tells it who is doing what. Each request is recorded
with the agent working on it, the time, and the owner's words. The agent marks it done with a one-line result, and
a separate mark, which only the owner sets, records that they have seen the result. When the owner asks "what did
I ask the agents?", any session can answer from the checklist instead of guessing. The same prompt hook shows each
session what other agents have open, so two agents do not take the same request without knowing.

## Building one for your own brain

1. Capture every prompt the owner types, with a timestamp and the session it went to, in an append-only file.
   Never delete this file.
2. Rebuild the views hourly: the last N prompts, the threads (a keyword or embedding grouping is enough to start),
   and the repeats (near-duplicate prompts more than a day apart).
3. Write the hook so it decides what this session has already seen, picks the parts it has not, and stays under
   your harness's limit for a single hook.
4. Test it at the receiving end, in both runtimes if you use two.
5. Give agents the pull command, so the block is a starting point and not a ceiling.

The same design works outside mathematics. A film studio's brain carries the director's notes, and a company's
carries a manager's standing decisions. In each case the person's own words, current and in order, are in front of
every agent that works for them.
