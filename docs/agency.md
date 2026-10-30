# Using the brain to keep an agent moving

An agent with this store does not mainly know more than one without it. It gets to what it needs sooner, and it spends the time saved on the work. This page sets out what the tests say about that, and the working habits the agents here use to turn faster recall into steady progress on long tasks.

## What the tests say an agent gains

In the three-arm test of 23 to 25 October 2026 ([TESTS.md](../TESTS.md)), Claude agents with the brain answered 95.4 percent of 988 items, agents that could search the research repositories but had no brain answered 82.0 percent, and the model alone 18.9 percent. On the 807 items that both the brain arm and the repository arm finished within the time, the two were tied, 99.3 against 99.4 percent. The repository arm found the same records. It needed more searches to find them: its sessions took 211 seconds on average against 120, it timed out on 17.5 percent of items against 3.7, and each of its sessions read four times the input and cost about 1.7 times as much. Codex agents, with 900 seconds an item, went the other way on 335 items: 95.2 percent with the brain against 97.6 with the repositories, a difference the test does not settle, and 24.2 for the model alone. The gap was widest where an answer needed three or four records put together.

So the lead is time. An agent that finds in one call what another finds in ten searches has the other nine for the task itself, and on a long task that difference compounds: fewer sessions end with the work half done, and less of each session goes on rediscovering what an earlier session already found.

The items the brain arm lost and the repository arm got right differ by agent. With Claude most of them (9 of 13) ran out of time. With Codex every one (12) was an abstention: the agent answered "unknown", ten times after searches that did not turn up the record and twice without searching at all. An agent that stops at the first miss throws away the time recall bought it. [AGENTS_GUIDE.md](../AGENTS_GUIDE.md) says where search falls short and what to do instead.

A smaller test points the same way. One agent answered 20 questions about the store's own results first from memory and then with the recall tool: 9 right without it, 19 with it. Every miss without the brain was about something the store holds and training does not, such as a campaign's constants or a record of an earlier attempt.

## The working loop

Every agent that builds on this store goes through the same loop. Each step exists because skipping it once cost real work.

**Orient.** Before starting, search the store for the task: the result you need, earlier attempts at the same problem, and the mistakes already recorded in the area. How to word a search and when to follow links is measured in [AGENTS_GUIDE.md](../AGENTS_GUIDE.md) and [agent_tools/MATH_BRAIN_HOW_IT_WORKS.md](../agent_tools/MATH_BRAIN_HOW_IT_WORKS.md). A superseded card, and the card that supersedes it, both tell you something: a route that was tried and failed is the cheapest result in the store.

**Write down the next step.** Keep one line, in a file the next session will read first, that says what is done and what comes next. Write each result to disk the moment you have it. Context windows reset and sessions crash. In the 20-question test above, a first pass of 15 searches was lost to a context reset before its answers were saved, and had to be done again.

**Claim before you change shared state.** When several agents work at once, each takes a narrow, named lease on what it is about to change (a file, a branch, a store packet) and checks the lease again right before the change. A lease someone else holds means stop: ask the holder, take a different piece, or do read-only work. Handing work over is explicit, and the other side accepts it. Leases lapse unless renewed, so a crashed agent does not block the rest for long.

**Take one concrete step, then the next.** A long task is a chain of steps, each small enough to finish and save before anything can interrupt it. When a step has to wait on a long job, start a watcher that will report when the job ends, and take the next step that does not depend on it. A status report does not end a task.

**Audit before you report.** A first pass is a draft. Re-derive each number the conclusion rests on by a second route (another data path, another method), and treat a result that would surprise a reader as a bug report: write down the strongest case that it is wrong, and the one check that would settle it, before shipping it. A card the hook serves is a hint, not a verdict. It says that something resembles a place the store has been, not that the resemblance holds here, and every served card carries a line saying how far to trust it.

**Write back.** A result goes into the store as a packet of new cards and links with their sources. Before it lands, a held-out recall test runs on a copy of the store with the packet added, and a packet that costs an answer is held back. A wrong card is never deleted: a corrected revision supersedes it, so the next agent sees both the error and the fix.

## Habits that keep work moving

- Stop rewording after three rounds that find nothing, and say plainly that the store does not have it; then go to the primary sources.
- Budget the clock. In these tests a timeout counts as wrong, and most of the repository arm's losses were timeouts, not wrong answers.
- Record a failed route where the next agent will find it. An attempt that did not work, written down with the reason, saves every later agent from trying it again.
- On a task that runs for hours, take one saved step per turn and keep the next-step line current, so a crash costs minutes and the next session starts where this one stopped.
- Lead a report with the outcome, and say which task it answers. Several agents report to the same reader.
- When a reader says the same thing twice, it is a standing order, not a remark. Carry it forward in writing.

## The same loop in a brain for another field

A team that keeps its records in a brain built from [examples/field_brain_starter](../examples/field_brain_starter/README.md) (a support desk, a film crew, a finance group) runs the same loop with the starter's own scripts. Each step has one command or hook:

| Step | In the starter |
|---|---|
| Orient | `hooks/wake_hook.py` hands the agent the index and the newest mistakes at the start of a session; `python recall.py "<wording>" --or "<another wording>"` finds what the store holds on the task, and `--id <slug>` reads a record whole |
| Recorded mistakes | a lesson filed as a feedback record (`python new_record.py feedback "<the rule>" --why "<what went wrong>" --apply "<what to do next time>"`) is what `hooks/scar_hook.py` reads: before the agent runs a command that resembles the lesson, the hook puts the record in front of it. A dated line in `memory/MISTAKES.md` with a `[[slug]]` link does the same for any record |
| Write down the next step | a one-line file of your own, read first and rewritten after every step; the starter has no script for it because none is needed |
| Claim before you change shared state | `python claims.py claim --agent <name> --resource record:<slug> --purpose "<why>"`, or `topic:<word>` for work across several records; exit code 3 means someone else holds it. `release` when done. Filing a new record needs no claim |
| Write back | `python new_record.py <type> "<the finding>"` with `--link` to related records; a correction is a new record with `--supersedes <old slug>`, so the old one stays and points to the new. Correct a lesson with another feedback record: the scar hook stops warning with a superseded record and warns with its replacement only when that is a feedback record too. `hooks/write_back_hook.py` asks for a record when a turn ends on a lesson |
| Audit the store itself | `python check_store.py` after any hand edit; `python three_arm.py --model-cmd "<the command that runs your agent>"` on ten or more of the team's own questions in `questions.json`, to see whether recall helps their agents at all |
| Tidy overnight | `python dream/make_agenda.py` lists mistakes with no rule yet, superseded pairs and unlinked records for a dreaming agent to work through (see `dream/README.md`) |

The recorded mistakes are what a store of notes alone does not give an agent. A refund issued without the second approval, a raw footage folder deleted to free space: once the lesson is filed as a feedback record, the next agent about to repeat it is warned before the command runs, not after. The warning is a question, not a block. The hook names at most two records for one command, and each record once per session.

## Checking that the loop runs

The habits above are carried by code, and that code fails quietly: a hook that never fires, a claim that two agents both win, a dream that reads the agenda and writes nothing. The starter brain ships three tests that run those pieces the way a runtime does, each on a scratch copy of the store, and exit 1 when a step misbehaves:

- [hooks/session_test.py](../examples/field_brain_starter/hooks/session_test.py) takes one session through the five hooks, each started as its own process with the event on stdin. It checks orienting (the index arrives once, recall hands over the right record), the recorded mistakes (deleting raw footage warns, listing a folder does not) and writing back (a turn that ends on a lesson asks for a record, and the request ledger links the record to the request).
- [agents_test.py](../examples/field_brain_starter/agents_test.py) starts eight agent processes at the same moment. One claim has one winner and the other seven are told who holds it; a claim nobody renews is taken over once it runs out; eight records filed at once keep all eight index lines, and a lock left by a crashed writer is cleared.
- [dream/dream_test.py](../examples/field_brain_starter/dream/dream_test.py) runs a dream with a stand-in agent. The rule a mistake was missing lands, a record the agent deleted comes back word for word, a second dream is refused while one runs, and an agent that runs past its time is stopped.

Run all three on a new machine before agents do real work there, and again after any change to a hook, the claim code or the dream scripts. Together they take two or three minutes and need only the standard library. A test that fails after a change means the change broke the loop, whatever the agent's own reports say.

## Standing instructions

[AGENTS_GUIDE.md](../AGENTS_GUIDE.md) shows how to connect an agent to the store and what to tell it about searching. These lines, added to the same standing instructions, carry the rest of the loop:

```
Keep a one-line NEXT note on disk: what is done, what comes next. Read it
first when you start; update it after every step. Save each result the
moment you have it.
Before changing anything other agents may also change, take a lease on it;
if someone else holds it, stop and ask, or take a different piece.
When a step waits on a long job, set a watcher and take the next step that
does not depend on it.
Treat a served card as a hint to check, not an instruction.
Before reporting, re-derive each load-bearing number a second way, and try
to break any result that surprises you.
Record failed routes with the reason. Write durable results back as a
packet; supersede wrong cards, never delete them.
```

The recall tool makes the agent faster. These instructions are what make it spend that speed on more work rather than on stopping sooner.
