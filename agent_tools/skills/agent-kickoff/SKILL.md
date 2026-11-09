---
name: agent-kickoff
description: Turn a short request into a fully running agent job - goal, limits, files that survive restarts, a loop, and a reporting habit. Use when someone gives a broad goal ("keep improving X", "work on Y for the next few days") or asks how to get an agent working on its own.
---

# Getting an agent going fully

People get the most from an agent when it can keep working without them: it knows the goal,
decides the small things itself, saves as it goes and reports without waiting for an answer. When
you are handed a broad goal, set that up before starting.

1. Restate the goal in one sentence and the end condition (a date, a result, or "until stopped").
2. Write down the limits. By default: decide small things yourself; ask the person only about
   money, deleting something with no second copy, publishing, or anything their own rules reserve
   to them. Ask once, with a recommendation, and keep working on what does not depend on it.
3. Orient in the brain first (see the brain-orient skill): what is known, what failed before.
4. Make the job folder with `ORDER.md` (their words, exact, dated) and `NEXT.md` (one line: the
   next step). See the brain-loop skill.
5. Split the goal into steps that each fit in one round of work. Put the first three in `NEXT.md`.
6. Suggest a loop if the person has not given one, in this shape:

   ```
   /loop fire this every 5 minutes for the next <N days>. <the goal in their words>. save each
   result to the brain, keep the NEXT line current, and tell me when a piece is finished.
   ```

7. If other agents work on the same machine, check who is editing what before you change shared
   files, and tell them what you took.
8. Report briefly when a piece is finished: what changed, where it is saved, what is next. End by
   naming the request the report answers, so a person running several agents knows which one it is.
