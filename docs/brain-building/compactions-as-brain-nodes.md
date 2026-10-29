# Keeping what a compaction throws away

A long agent session runs out of context and is compacted: the harness replaces the conversation with a summary
and the agent carries on from that. The summary is written once and is usually lost when the session ends. It is
also the densest record the session will ever produce: what the agent was asked, what it did, what failed and how
it was fixed, and what comes next.

We now keep every compaction summary as a node in the brain.

## What is stored

Each compaction becomes one file under a `compactions/` folder in the brain's graph, plus a line in an append-only
index (`INDEX.jsonl`) with the session id, the agent, the time, and the task ids the summary names. An anchor note
in the memory folder links the node to:

- a hub node for all compactions, so recall can reach the set as a whole
- the same session's previous compaction, so a long session reads as a chain
- other sessions' compactions on the same open tasks
- the memories whose text is closest to the summary

Because the anchor sits in the memory folder, ordinary recall finds compactions the same way it finds memories.
A question like "what did we try on the render cache last week" can return the compaction that recorded it, even
when nobody wrote a memory at the time.

## What it fixes

- A summary can drop something the agent needed. The agent is told, right after compacting, where its node is and
  that the full summary is there, so it reads the node instead of redoing the work.
- A new agent on an old task can read the chain of compactions for that task, in order, instead of starting from
  the code.
- Several agents on one task can see each other's summaries without sending messages.

## Hooks around a compaction

Three small hooks make compactions cheaper and safer:

1. **Before.** At a large context size, the agent is told to finish its current step and write its next-step line
   to disk, so the automatic compaction lands at a boundary and not in the middle of an edit.
2. **After.** The first message after a compaction tells the agent to read its next-step line, its open checklist
   entries and its inbox before acting, and to trust what those record as done.
3. **At stop.** If an agent compacted and is about to stop with tasks still open under its id, a stop hook names
   them and asks it to continue, or to say in one line what each one is waiting on.

The third one matters most in practice. An agent that has just compacted often reads its own summary as a final
report and stops, with work still open.

## Building it for your own brain

Most harnesses let a hook run on the compaction event or on the session start that follows it. Copy the summary
out at that moment, write the node and the index line, and link the anchor with your brain's ordinary edge-writing
code. Never delete the nodes: they are raw material for the nightly consolidation, and the summary of a session
that has since ended exists nowhere else.
