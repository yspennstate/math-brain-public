# One project from start to finish

The other pages explain the pieces one at a time. This page follows one made-up project from
the first sentence to the final report, so you can see how they fit together. The project is
small on purpose: a reading list on graph colouring, built from papers the agent finds, with
one short summary per paper.

## 1. The ask, in plain words

You open a terminal in an empty folder, start the agent, and say what you want the way you
would say it to a colleague. Spelling and polish do not matter.

```
i want a reading list on graph colouring, the main results from the last 30 years, one
paragraph per paper saying what it proves and why it matters. keep it in this folder.
```

## 2. The order file

Before anything runs on a timer, ask the agent to write your words down. Then every later
round can reread them, even after the conversation has been compacted or restarted.

```
write my request word for word into ORDER.md, then under it write how you read it: what
counts as done, what you will not do, and where the files go. show me the file.
```

Read what it wrote. If its reading is wrong ("it thinks I want a survey paper"), correct it
now. This costs one minute and saves a day of work aimed at the wrong thing.

## 3. The loop prompt

```
/loop fire this every 10 minutes for the next 2 days. read ORDER.md, then line 1 of NEXT.md.
do the next undone step: find one more paper, read it, write its paragraph into LIST.md.
check the paragraph against the paper before you save it. then write a new line 1 in
NEXT.md: the date, what you did, and what comes next.
```

The prompt names the files, the size of one step, a check, and where the next step is written
down. That last part matters most: the next round starts from NEXT.md, not from memory.

## 4. Three rounds of NEXT lines

After a few rounds the top of NEXT.md might read like this (newest first):

```
12 Mar 09:40 added Robertson-Sanders-Seymour-Thomas 1997 (four colour, shorter proof). NEXT: Reed's omega, delta, chi bound.
12 Mar 09:30 added Johansson 1996 (triangle-free graphs). NEXT: four colour theorem, 1997 proof.
12 Mar 09:20 added Kim 1995 (girth five). NEXT: Johansson 1996, triangle-free.
```

You can read three lines and know where things stand. If a line looks wrong, you can say so
in the window and the next round picks it up.

## 5. A skill from a repeated correction

Around round twelve you notice you have told the agent three times: "give the journal and the
year, and say if the result was later improved". That is the moment to make a skill (see
[skills.md](skills.md)).

```
make a skill called paper-paragraph from the corrections I keep giving you: journal and year
on the first line, what it proves, why it matters, and whether it was later improved and by
whom. use it for every paragraph from now on.
```

The correction now lives in a file, so it survives restarts and works in other projects too.

## 6. The final report

When the end date comes, or the list feels complete, ask for a report you can check.

```
stop the loop. write a short report: how many papers are in LIST.md, which ones you were
least sure about and why, and the path of every file you changed. then check that LIST.md
opens and every paragraph has a year.
```

Check one or two paragraphs yourself against the papers. If they hold up, the project is
done; if not, reopen the loop with the fix written into ORDER.md.

## What carried over

The same shape works for any project: words into ORDER.md, a loop that reads it and writes
NEXT.md, a skill when you repeat yourself, a report you can verify. Only the step in the
middle changes.
