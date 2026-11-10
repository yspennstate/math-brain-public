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

## How do I stop a loop, or change what it is doing halfway?

To change it, type the change into the same window, as you would to a person: "from now on, skip
the tests and only write the docs". The agent treats your newest words as the ones that count. If
the loop rereads an ORDER file every round, you can also edit that file, and the next round picks
the change up even when you are not at that window.

To stop it, say "stop the loop" in its window, or close the window: a loop lives inside its
session. It also stops by itself at the end date you gave it. Before stopping a long loop, ask for
a short report of where things stand, so the next loop can start from there.

## What happens when the agent's context fills up?

It compacts: the conversation is summarised and the agent carries on from the summary. Anything
important should already be on disk (the NEXT file, the ORDER file, the brain), so a compaction
costs at most the current step.

## Does it cost a lot?

A loop uses your agent subscription or API allowance the way normal use does, just more of it.
Pushing to GitHub is free; repositories with automatic test runs can bill for those runs, so put
`[skip ci]` in commit messages for documentation and data.

## Does the agent need the internet, and what does it send out?

Yes. The model itself runs on the provider's servers, so the agent needs a connection, and
everything it reads to answer you goes there: your prompts, and any file or command output it
opens along the way. Files it never opens stay on your computer, and nothing reaches GitHub
unless it pushes. The brain's memories live on your disk as plain files, but a memory the agent
recalls is read like any other file, so it is sent too.

So keep passwords, keys and anything you would not paste into a chat out of the folders the
agent works in, and tell it which folders are off limits. Read the provider's data policy once
to know how long they keep what is sent. A fully offline setup needs a model you run yourself,
which the brain can work with but these pages do not cover.

## Can several agents work at once?

Yes. Give each one its own job folder, and have them claim files before they edit, so two agents
do not overwrite each other. The framework's mesh does the claiming.

## How many terminals can I run at once?

The computer is rarely the limit; the model runs on the provider's side and a terminal costs
almost nothing locally. The limits are your usage allowance, which every terminal draws on
together, and your own attention, since each one writes reports you will want to read. Start with
two or three, one job each (see [terminals.md](terminals.md)), and add another only when the ones
you have run for a day without needing you. If you find yourself scrolling through windows to
learn what is going on, you have more than you can follow; ask each for one line:

```
in one line: which job is this terminal on, what did the last round finish, and is anything
waiting on me?
```

## What should I use the brain for first?

Something you already work on every day and keep explaining again: a research project, a codebase,
a writing project. The brain pays off when the same ground comes up a second time.
[starter-prompts.md](starter-prompts.md)

## Can it keep working while I sleep?

Yes, if the computer stays on and awake and the terminal stays open. A loop with an end date a few
days out does the rest. Before you leave, ask the agent to check that sleep is off while its work
runs, and to keep its NEXT line current so that you can read in the morning what it did.
[struggling.md](struggling.md)

## Can it use more than one computer?

Yes. If the agent can log in to the other machine over your own network, it can start jobs there,
check on them and bring the results back. Ask it to split the work so no two machines do the same
piece, and to collect finished pieces in one place. [loop-prompts.md](loop-prompts.md)

## Can two computers share one brain?

Yes. Keep the brain in a private GitHub repository and have each computer pull it before work and
push what it learned after. Memories are small text files, so the two copies merge cleanly most of
the time; when they do not, ask the agent to keep both lines and mark which is newer.
[github-as-storage.md](github-as-storage.md)

## How do I know it really did what it says?

Mostly you don't, until you look. An agent can write "done" over a step that half worked, and a
loop that runs for days will do it sooner or later. So ask every report to come with something you
can open yourself: the link to the page or the commit, the path of the file, the line of test output
that passed. A claim with nothing behind it is a draft. Once in a while open one of those links at
random; if it does not show what the report said, tell the agent, and it will be more careful from
then on, especially if you ask it to save that as a rule in the brain.

```
when you say something is done, give me the link, file or test output that shows it. check each
result a second way before you report it, and if you could not check something, say so plainly
instead of calling it done.
```

## The brain does not seem to do anything. What now?

Check that the hooks run (the agent should mention the brain at the start of a session), that you
started the agent from the folder the brain expects, and that there is something in the brain about
your topic yet. [struggling.md](struggling.md)

## How do I teach the agent a habit once instead of every day?

Ask it to turn the habit into a skill or a hook. A skill is a page of instructions the agent loads
when the situation comes up; a hook runs on every prompt. [skills.md](skills.md) walks through
writing one; ready-made ones are in [../../agent_tools/skills/](../../agent_tools/skills/).

## What is the difference between a skill, a memory and a loop prompt?

A memory is something that happened or was learned ("the export breaks on files over 2 GB"). A
skill is how you want a kind of job done ("before publishing, scan every file and run the tests").
A loop prompt is the job itself, sent again on a timer ("every 10 minutes until Friday, do the next
step on the export"). The loop does the work, the memories carry what each round learned, and the
skills keep every round doing it your way. [loop-prompts.md](loop-prompts.md),
[skills.md](skills.md), [github-as-storage.md](github-as-storage.md)

## What happens to my notes if I stop using it?

Nothing. Every memory is an ordinary Markdown file in a folder on your computer, with a few lines
at the top saying what kind of note it is and when it was written. Stop running the agents and the
folder stays where it is; any text editor opens the files, and you can search them, print them or
copy them anywhere. If you move to a different agent or tool, point it at the folder and ask it to
read the notes. If you kept the brain on GitHub, a copy is there as well. To take it with you in
one piece:

```
put a copy of every note in the brain into one zip file in my Downloads folder, with a short
README that says what is in it and how the folders are arranged.
```
