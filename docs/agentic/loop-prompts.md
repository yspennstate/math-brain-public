# Loop prompts

A loop is a prompt the agent runs again on a timer. In Claude Code you start one with `/loop`:

```
/loop fire this every 5 minutes for the next 10 days. keep working on improving the brain and
testing it, and write down what each test showed.
```

The agent schedules the prompt, runs it once straight away, and then gets the same prompt back
every five minutes for as long as the terminal stays open. Each time it wakes it reads where it got
to, does the next piece, saves it, and stops until the next round.

This is the single biggest change in how much an agent gets done. Without a loop an agent works
until it thinks it has answered you and then waits. With a loop it keeps picking up the next step
for days, and the brain is what lets it pick up where it left off instead of starting cold.

New to loops? Start with one small loop that runs for a day, as in the first-week plan in
[starter-prompts.md](starter-prompts.md#the-rest-of-the-first-week), so you can read every round.
Once you run more than one, give each its own terminal and folder
([terminals.md](terminals.md#several-terminals-one-job-each)).

## The shape of a good loop prompt

The loops that work best here share a shape. Most of them are one paragraph, written quickly, and
they say four things:

1. How often and for how long. "fire this every 5 minutes for the next 10 days". Five or ten
   minutes is the usual interval. Ten days is the usual length for an ongoing project; ten to
   thirty hours for a push on one thing.
2. The goal, in plain words. "keep trying to solve the open problems on the list", "make sure every
   film we made is uploaded and none got stuck", "keep improving recall and test it".
3. How to judge progress or what to keep. "learn as much as possible from it", "push the results to
   a public repository", "write a paper for each one we solve".
4. Who else should know. "tell the other agents", "put it in the task manager", "send me an email
   when you know if it is feasible".

Spelling does not matter. A loop prompt is a standing instruction, not an essay.

## What the agent should do with a loop

A loop prompt fires every few minutes for days, so the agent needs a way to not lose its place.
Ask it to keep two small files, or install the skill in
[../../agent_tools/skills/brain-loop/](../../agent_tools/skills/brain-loop/SKILL.md) which tells it to:

- `ORDER.md`: your words, copied once, word for word, with the time you gave them. Every round
  starts by reading it, so the job never drifts into something you did not ask for.
- `NEXT.md`: one line at the top saying what the next round should do. Each round does that step,
  saves the result, and rewrites the line. If the computer crashes, at most one step is lost.

It also helps to tell the agent to write anything durable into the brain (`brain.py remember`), not
only into the NEXT file, so other agents and later sessions can find it.

## Sizing one round

The prompt decides how much work one round does, and it is worth getting that roughly right. A
good round is one step that can be finished, saved and checked in a few minutes: one more paper
summarised, one test fixed, one section written.

You can tell the size from the NEXT lines after an hour or so:

- Rounds too big: the lines say "started X", "continued X", "still on X" and nothing is ever
  finished. A crash loses a lot, and the report on any one round is vague.
- Rounds too small: the lines say "checked, nothing to do" or rename and reformat the same file
  over and over. The loop is busy but nothing moves.
- About right: each line names one finished thing and the next one, and every line or two you can
  open a file and see the change.

Resizing does not need a new loop. Type it into the same window:

```
your rounds are too big. from now on do one step a round that you can finish and check in a
few minutes, save it, and write it in NEXT.md before you start anything else.
```

## Practical details

- A loop lives inside its terminal session. Close the window and it stops. Leave the window open,
  and if you restart the computer, start the session again and give the loop again (the ORDER and
  NEXT files mean nothing is lost).
- In Claude Code, scheduled loops expire after seven days. For a ten-day loop the agent should
  re-create it before day seven; tell it so in the prompt ("the loop expires after 7 days, re-create
  it to run to <date>"). The brain-loop skill does this.
- A loop only fires while the agent is idle. If one round takes twenty minutes, the next one waits.
  That is fine; it means the agent is working.
- `/loop` with no interval lets the agent choose its own pace. Give an interval when you want it to
  keep going on a fixed rhythm.
- Codex CLI has no `/loop` command at the time of writing. The same effect comes from a scheduled
  task that resumes the session with the loop prompt, or from running the loop in Claude Code and
  having it hand pieces to Codex.
- Several loops can run in one terminal. They queue behind each other. Different projects are
  easier to follow in different terminals.

## Example loops

Replace the parts in angle brackets. All of these assume the brain is installed; the agent reads it
at the start of every round through the hooks.

Building the brain itself

```
/loop fire this every 5 minutes for the next 10 days. keep improving the brain and testing it.
each round, pick one weakness in recall or in the cards, fix it on a copy, test it against the
old version on the same questions, and keep it only if it wins. write each result to the brain.
```

```
/loop fire this every 10 minutes for the next 2 days. go through my notes on <topic> and turn
everything worth keeping into memories with links to the memories they relate to. skip anything
that is already in the brain.
```

```
/loop fire this every 5 minutes for the next 10 hours. read the last 30 prompts I gave agents
here, write a summary of what I asked for, put it on the task list, and work on what is not done.
```

Research and math

```
/loop fire this every 5 minutes for the next 10 days. keep working on <problem>. use everything
in the brain on it first, record every route you try and why it failed, and push each result as
far as it goes. if you solve a piece, write it up properly and tell me.
```

```
/loop fire this every 10 minutes for the next 5 days. find results we have that are not yet
written up, write each one as a short paper with its proofs checked, put it in its own public
repository, then go to the next.
```

```
/loop fire this every 5 minutes for the next 2 days. run a test of the brain against no brain on
<kind of task>. make the test fair, use the same questions for both, and learn as much as possible
from where they differ.
```

Keeping work moving

```
/loop fire this every 5 minutes for the next 10 days. keep working on the top 10 tasks in the
task list, highest priority first. mark each one when it is done and say what was done.
```

```
/loop fire this every 10 minutes for the next 10 days. make sure everything we made is saved on
github, check each copy is really there, and then remove the local copy so the disk does not fill.
```

```
/loop fire this every 20 minutes for the next 30 hours. check that the other agents are still
working and not stuck. if one is stuck, read why, fix what you can, and tell me what you cannot.
```

Making things

```
/loop fire this every 5 minutes for the next 10 days. keep making <videos / articles / examples>
on <theme>. look at what people respond to and push in that direction, but keep some variety.
```

```
/loop fire this every 10 minutes for the next 10 hours. write the documentation for <project>
the way a person would want to read it: what it is, how to install it, one worked example. test
every command you write.
```

```
/loop fire this every 10 minutes for the next 5 days. keep improving my <CV / statement / report>.
each round, read it the way <the reader> would, pick the one weakest part and make it better,
using what the brain knows about me and my work. keep every version, never invent a fact, and
tell me only what you changed and why.
```

Learning from what you do

```
/loop fire this every 10 minutes for the next 10 days. study how I work with agents (my prompts,
what I correct, what I repeat) and turn each habit into a skill or a suggestion other people
can use. keep a dated list of the suggestions.
```

Lists that stay current

```
/loop fire this every 5 minutes for the next 10 days. search for new <openings / papers / grants>
that fit me and add each one to <list file> with the deadline, the link and the date you found it.
skip anything already there, drop anything whose deadline has passed, and tell me only what is new.
```

```
/loop fire this every 10 minutes for the next 3 days. go through my list of top <200> problems in
<field>. remove any that are solved or do not belong, with one line on why, and fill each gap with
a better one, with a source.
```

Long jobs on more than one computer

```
/loop fire this every 5 minutes for the next 2 days. keep the <render / batch> running on every
computer you can reach, splitting the work so no two machines do the same piece. each round, check
each machine is still working, restart what stopped, collect finished pieces in one place, and
tell me how many are done out of how many.
```

```
/loop fire this every 10 minutes for the next 10 days. check that <the other computer> is awake,
reachable and has free disk. if it went to sleep or filled up, fix it the safe way and write one
line to a log saying what you did. if you cannot fix it, tell me what to type on it.
```

## Why loops and the brain go together

A loop without a brain repeats itself: each round the agent has only the last summary to go on, so
it redoes work, forgets why a route failed, and drifts. A brain without a loop sits still: it only
grows when someone asks a question. Together, each round reads what earlier rounds learned, adds
one piece, and saves it where the next round and every other agent can find it. Over ten days that
is a few thousand rounds, and the brain is visibly different at the end.
