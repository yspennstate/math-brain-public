# Starter prompts

Prompts to paste into a terminal agent once the brain is installed. They are written the way you
would say them; change the parts in angle brackets.

## Day one

Wake the agent into the brain and see what it knows:

```
read the brain's wake-up message and the memory index. tell me in five lines what this brain
knows so far, what is missing, and what you would add first.
```

Give it something real to remember:

```
I am working on <project>. here is what matters: <three or four sentences>. save this to the
brain as memories, linked to each other, and show me how you would find it again with recall.
```

Check recall works:

```
recall from the brain what we know about <topic>, with the scores. then tell me which of those
notes you would trust and which you would check first.
```

## The rest of the first week

Day two, give it a first loop. Pick something small that runs for a day, so you can read every
round:

```
/loop fire this every 10 minutes for the next 24 hours. work on <one small piece of my project>.
each round, read the NEXT line in <folder>/NEXT.md, do one step, save it, and rewrite the NEXT
line. save anything worth keeping to the brain.
```

Day three, turn something you keep repeating into a skill. By now you will have typed the same
instruction more than once:

```
look at what I have told you in the last few days. find an instruction I keep repeating and turn
it into a skill, so you follow it without being told. show me the skill and test it once.
```

At the end of the week, look back:

```
read everything we saved to the brain this week. tell me what helped, what you never used, and
what is missing. then suggest the next loop I should start.
```

## Getting an agent going fully

The agents that get the most done are given a goal, permission to decide the small things
themselves, and a way to report without waiting for an answer.

```
your job for the next few days is <goal>. decide the small things yourself and keep going; only
stop to ask me about money, deleting something with no second copy, or anything public. save
every result to the brain as you go, keep a one-line NEXT note, and give me a short report each
time you finish a piece. then start a loop so you keep going.
```

```
before you start, read what the brain already has on this, and what went wrong before
(recall "<area> mistakes"). tell me the two mistakes you are most likely to repeat and how you
will avoid them. then begin.
```

Then add a loop from [loop-prompts.md](loop-prompts.md).

## Using the brain well

```
before you answer, recall from the brain with three different wordings. if nothing comes back,
say so instead of guessing.
```

```
you just finished <piece of work>. write what you learned that the next agent would need into the
brain: what worked, what failed and why, and what you would try next. link it to the memories it
builds on.
```

```
a note from the brain said <note>. check it against what you see now before you act on it. tell
me whether it still holds.
```

```
look at the brain's newest memories and its oldest ones on <topic>. find any that contradict each
other, decide which is right, and mark the other one superseded with a pointer.
```

## Working with several agents

```
there are other agents working on this computer. before you change a shared file, check who is
working on it. if someone is, take a different piece and tell them what you took.
```

```
tell the other agents about <change>, and put it on the task list so they see it next time they
look.
```

## Saving to GitHub

```
push what you finished today to <repository>. check the push really landed on github (compare the
remote commit), and tell me the commit.
```

More in [github-as-storage.md](github-as-storage.md).

## When you want ideas

```
look at what I have asked for this week and suggest five things the brain could do for me that I
have not asked for yet. for each, give the loop prompt I would use to start it.
```

[SUGGESTIONS.md](SUGGESTIONS.md) is a running list of these, newest first.
