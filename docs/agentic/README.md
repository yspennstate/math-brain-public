# Running the brain agentically

The brain is a store of memories, cards and links that an AI agent reads before it works and writes
back to when it learns something. Most of what makes it useful only happens when the agent runs for
a long time on its own: it recalls, works, saves, and comes back to the same job an hour later
knowing what it did. That needs three things, and this folder covers each one.

1. A terminal agent. Claude Code or Codex CLI, running in a terminal window on your computer. The
   brain's hooks, its compaction notes, its skills and its loops all work there and mostly do not
   work in a chat window. [terminals.md](terminals.md)
2. Loop prompts. One sentence that tells the agent to come back to a job every few minutes for days.
   This is where the agentic behaviour shows up. [loop-prompts.md](loop-prompts.md)
3. Somewhere permanent to keep things. A GitHub repository holds the memories, the results and the
   files the agent makes, so nothing lives only on one laptop. [github-as-storage.md](github-as-storage.md)

Then:

- [starter-prompts.md](starter-prompts.md): prompts to paste on day one, a plan for the rest of
  the first week (a first loop, a first skill, a look back), and prompts for using the brain well
  after that.
- [struggling.md](struggling.md): what to check when the brain does not seem to do anything, or
  when work stalls: the agent stops early, the computer sleeps, the disk fills, the usage runs out.
- [faq.md](faq.md): short answers to the questions people ask first (cost, how long a loop runs,
  what happens when the context fills up, working overnight, using more than one computer, running
  on a laptop, checking on it from a phone, sharing a brain with a team, checking that it really did
  what it says, undoing a bad change, keeping the agent and the brain up to date).
- [SUGGESTIONS.md](SUGGESTIONS.md): a running list of ideas, newest first, for prompts, loops and
  uses of the brain. New entries are added as they come up.
- [SUGGESTIONS_BY_TOPIC.md](SUGGESTIONS_BY_TOPIC.md): the same list grouped by topic (loops, checking
  results, several agents, setup, and so on).
- [skills.md](skills.md): how to turn an instruction you keep repeating into a skill, step by step,
  with one worked example.
- [worked-example.md](worked-example.md): one small project followed from the first sentence to the
  final report: the ask, ORDER.md, the loop prompt, NEXT lines, a skill, the report.
- [../../agent_tools/skills/](../../agent_tools/skills/): skills you can install so the agent itself
  knows how to orient in the brain, start a loop and keep one going.

## Where to start

If you are new to all of this, read in this order: terminals.md, then starter-prompts.md (do day
one), then loop-prompts.md (start one small loop), then worked-example.md to see the whole shape once, then skills.md once you catch yourself repeating an
instruction. Keep struggling.md and faq.md for when something does not work. Read SUGGESTIONS.md last, a few entries at a time, once you have a loop running and
want more ideas.

## The short version

Open a terminal, start Claude Code in your home folder, install the brain with
[framework/bootstrap](../../framework/bootstrap/README.md), and then type something like this:

```
/loop fire this every 10 minutes for the next 2 days. read the brain's notes on <your project>,
pick the most useful next step, do it, save what you learned to the brain, and keep a one-line
NEXT note so the next round knows where to start.
```

Leave the window open. Come back tomorrow and read what it did.

## How this relates to the rest of the repository

- [AGENTS_GUIDE.md](../../AGENTS_GUIDE.md) is the recall habit for the math store: how an agent
  searches cards and walks links.
- [docs/setup-with-brain-framework.md](../setup-with-brain-framework.md) installs the framework and
  points it at the math store.
- [docs/agency.md](../agency.md) is what the tests say an agent gains from the brain and the working
  loop inside one session.

This folder is the part around those: the terminal, the loop that keeps the agent working across
sessions, and the habits that make a brain grow instead of sitting still.
