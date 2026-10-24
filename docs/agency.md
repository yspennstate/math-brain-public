# Using the brain to keep an agent moving

An agent with this store does not mainly know more than one without it. It gets to what it needs sooner, and it spends the time saved on the work. This page sets out what the tests say about that, and the working habits the agents here use to turn faster recall into steady progress on long tasks.

## What the tests say an agent gains

In the three-arm test of 23 and 24 October 2026 ([TESTS.md](../TESTS.md)), Claude agents with the brain answered 94.9 percent of 880 items, agents that could search the research repositories but had no brain answered 80.6 percent, and the model alone 19.5 percent. On the 713 items that both the brain arm and the repository arm finished within the time, the two were tied, 99.2 against 99.4 percent. The repository arm found the same records. It needed more searches to find them: its sessions took 223 seconds on average against 128, it timed out on 18.9 percent of items against 4.3, and it read four times as many input tokens. The gap was widest where an answer needed three or four records put together.

So the lead is time. An agent that finds in one call what another finds in ten searches has the other nine for the task itself, and on a long task that difference compounds: fewer sessions end with the work half done, and less of each session goes on rediscovering what an earlier session already found.

The few items the brain arm lost were mostly an agent giving up early: it answered "unknown" without calling the recall tool, or after a search that missed a record a plain text search would have found. An agent that stops at the first miss throws away the time recall bought it. [AGENTS_GUIDE.md](../AGENTS_GUIDE.md) says where search falls short and what to do instead.

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
