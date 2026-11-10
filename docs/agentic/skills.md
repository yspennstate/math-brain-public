# Skills: teaching the agent something once

A skill is a short file that tells the agent how to do one kind of job. The agent reads the first
few lines of every skill it has at the start of a session, and opens the whole file when a job
matches. So an instruction you would otherwise type again and again gets written down once, and the
agent follows it without being told.

Claude Code looks for skills in `~/.claude/skills/<name>/SKILL.md` (for every project) or in
`.claude/skills/<name>/SKILL.md` inside a project. Codex reads the same kind of file from its own
skills folder. Five ready-made ones are in [../../agent_tools/skills/](../../agent_tools/skills/).

## When something should become a skill

- You have typed the same instruction three times. That is the clearest sign.
- A loop keeps getting the same step wrong, and you keep correcting it in the loop prompt.
- A job has a fixed order that matters (check before publishing, save before reporting), and the
  agent sometimes skips a step.
- Someone else will run the same kind of job, and you want their agent to do it your way.

If an instruction only applies to one project, a note in that project's folder may be enough. A
skill is for something that comes up across jobs.

## Writing one, step by step

The worked example below is a skill most loops end up needing: keep one line at the top of a file
that says what comes next, so a fresh round (or a fresh agent after a crash) picks up the thread.

1. Write down what you keep saying, in your own words. For example: "before you stop, write the
   next step at the top of NEXT.md, and read it first when you start."
2. Say when it applies. The description is the part the agent reads every session, so it decides
   whether the skill gets used. Name the situations and the words people use: "a loop round",
   "keep working on this", "pick up where you left off".
3. Write the steps the way you would explain them to a new colleague. Short, in order, with the
   reason for each one in a few words. The reason matters: an agent that knows why a step exists
   handles the odd case better than one that only has the rule.
4. Add one example of the result, so the agent can see what good looks like.
5. Test it in a fresh session. Ask for a job the skill should cover, without mentioning the skill,
   and see whether the agent uses it. Then ask for something it should not cover, and check that it
   stays out of the way. If it misfires either way, the description is what to fix.

The file:

```
---
name: next-line
description: Keep a one-line NEXT note at the top of NEXT.md in the job folder so any round can
  pick up where the last one stopped. Use at the start and end of every loop round, when told to
  "keep working on this", "pick up where you left off", or after a crash or a context reset.
---

# The NEXT line

A loop round starts with no memory of the last round except what is on disk. One line at the top
of NEXT.md carries the thread.

## Start of a round
1. Read the first line of NEXT.md in the job folder. If there is none, read ORDER.md and write one.
2. Do what it says. If it is too big for one round, split it and do the first part.

## End of a round
1. Save the result to disk first, then update the note (a crash between the two should lose the
   note, not the work).
2. Add a new first line: the time, what you did in one sentence, where the result is, and the next
   step. Keep the older lines below it as a record.

## Example
10 Nov 14:05: added the install section to setup.md (saved, pushed). NEXT: write the
troubleshooting section, starting with "the agent stops after one round".
```

Save it as `~/.claude/skills/next-line/SKILL.md`. You can also let the agent do the writing:

```
I keep telling you to write the next step at the top of NEXT.md before you stop. turn that into a
skill called next-line in ~/.claude/skills. keep it short, give the reason for each step, add one
example. then open a fresh session in a scratch folder and test whether it gets used.
```

## Sharing a skill, and using someone else's

A skill is a folder, so sharing one is copying a folder. Put yours in a repository or send it as a
zip; the other person drops it into their own skills folder (`~/.claude/skills/<name>/` for Claude
Code) and starts a new session. The five in [../../agent_tools/skills/](../../agent_tools/skills/)
are installed the same way.

Read a skill before you install it. It is a set of instructions your agent will follow without
asking you, and some skills come with scripts the agent will run. A skill from someone you trust is
usually fine; one you found online deserves the same look you would give a script before running
it. The agent can do the reading for you:

```
read the skill in <folder> before I install it. tell me in plain words what it makes you do, what
commands or scripts it would run, and whether it sends anything off this computer or deletes
anything. if it looks safe, install it and test it in a fresh session.
```

## Keeping skills good

- Keep each one short. If a skill grows past a page, it is probably two skills.
- When the agent gets something wrong despite a skill, fix the skill, not just the one result.
  Ask: "you had a skill for this and still missed it. what in the skill made that easy to miss?
  change it."
- Look through your skills once a month and delete the ones you no longer use. A stale skill that
  fires on the wrong job costs more than a missing one.
- Skills and the brain work together. The brain remembers what happened; a skill remembers how you
  like a kind of job done. When a lesson from the brain keeps coming up, that lesson is a candidate
  for a skill.
