---
name: brain-loop
description: Keep a long-running loop (a /loop prompt that fires every few minutes for hours or days) on track with the brain. Use when you are given a /loop prompt, when a loop tick fires, or when someone asks you to keep working on something for a long time.
---

# Running a loop with the brain

A loop prompt comes back every few minutes for hours or days. Each round has to know what the
person asked, where the last round stopped, and what earlier rounds learned. Three things carry
that across rounds, crashes and context compaction.

## First round

1. Make a folder for the job (for example `loops/<short-name>/`).
2. Write `ORDER.md`: the person's words, copied exactly, with the date and time they gave them.
   Add one paragraph saying how you read the request. Never rewrite their words later; add new
   words from them below the old ones, dated.
3. Write `NEXT.md` with one line at the top: the time, what was done, and `NEXT:` the single next
   step.
4. Schedule the loop. In Claude Code, scheduled loops expire after seven days: if the job runs
   longer, write the renewal date into `NEXT.md` (for a ten-day loop, re-create it on day six to
   run to the end date).
5. Do the first step now rather than waiting for the timer.

## Every round

1. Read `ORDER.md`, then the top line of `NEXT.md`.
2. Recall what the brain has on the step before doing it:
   `python brain.py recall "<the step, in the words a note would use>"`.
3. Do the one step. Keep it small enough to finish in the round.
4. Check the result once in a different way (rerun, compare, read the output back).
5. Save. Durable things go into the brain, where other agents can find them:
   `python brain.py remember <slug> --type project --desc "<one line>" --body "<what and why>"`.
   Routine progress goes only in `NEXT.md`.
6. Prepend a new line to `NEXT.md` with the time, what was done and the next step.
7. If nothing changed this round (waiting on something), say so in one line and stop. A quiet
   round is fine; a round that invents work is not.

## When something goes wrong

- The same `NEXT` line three rounds in a row: the step is too big or blocked. Split it, or write
  why it is blocked and move to another piece of the order.
- A result that looks too good: try to break it before you save it.
- A question only the person can answer (money, deleting the only copy, anything public): send it
  to them once, in a short message with your recommendation, and carry on with what does not
  depend on it.

## At the end

When the end date passes or the person stops the loop: delete the schedule, write a short final
report (what was asked, what was done, what is left), save the lessons to the brain, and mark the
job done in `NEXT.md`.
