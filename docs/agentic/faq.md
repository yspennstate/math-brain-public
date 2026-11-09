# Questions people ask

Short answers, with a link to the longer page where there is one.

## Do I need to know how to program?

No. You need to open a terminal and type one command to start the agent. After that you talk to
it in plain language, the same as in a chat window. If installing the terminal agent is the hard
part, a chat assistant you already use can walk you through it step by step.
[terminals.md](terminals.md)

## Why a terminal and not the chat window in my browser?

The brain works through programs that run on your own computer: hooks that hand the agent its
memories before every prompt, a scheduler that sends the loop prompt again, scripts that save and
fetch files. A browser chat cannot run any of these. A terminal agent can.

## What does a loop actually do?

It sends the same prompt to the agent on a timer, every five minutes for example, until a date you
choose. Each round the agent reads where it stopped, does one step, saves it and writes down the
next step. [loop-prompts.md](loop-prompts.md)

## Won't the agent just repeat itself every round?

Not if the prompt tells it to read a NEXT file first and rewrite it at the end. That one line is
how round fifty knows what round forty-nine did. If the line stops changing, the loop is stuck;
tell it to split the step or skip it.

## How long can a loop run?

Days. The practical limit is the scheduler: some drop a recurring job after about a week. Put the
end date inside the prompt so the agent knows to set the job up again when it lapses.

## What happens when the agent's context fills up?

It compacts: the conversation is summarised and the agent carries on from the summary. Anything
important should already be on disk (the NEXT file, the ORDER file, the brain), so a compaction
costs at most the current step.

## Does it cost a lot?

A loop uses your agent subscription or API allowance the way normal use does, just more of it.
Pushing to GitHub is free; repositories with automatic test runs can bill for those runs, so put
`[skip ci]` in commit messages for documentation and data.

## Can several agents work at once?

Yes. Give each one its own job folder, and have them claim files before they edit, so two agents
do not overwrite each other. The framework's mesh does the claiming.

## What should I use the brain for first?

Something you already work on every day and keep explaining again: a research project, a codebase,
a writing project. The brain pays off when the same ground comes up a second time.
[starter-prompts.md](starter-prompts.md)

## The brain does not seem to do anything. What now?

Check that the hooks run (the agent should mention the brain at the start of a session), that you
started the agent from the folder the brain expects, and that there is something in the brain about
your topic yet. [struggling.md](struggling.md)

## How do I teach the agent a habit once instead of every day?

Ask it to turn the habit into a skill or a hook. A skill is a page of instructions the agent loads
when the situation comes up; a hook runs on every prompt.
[../../agent_tools/skills/](../../agent_tools/skills/)
