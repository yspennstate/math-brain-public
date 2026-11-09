---
name: loop-writer
description: Write a loop prompt that keeps an agent working on one goal for hours or days - the cadence, the end time, the files it reads first, what one round does, and how it reports. Use when someone asks for a loop, says "keep working on this for the next few days", or wants an agent to run while they are away.
---

# Writing a loop prompt

A loop prompt is the same message sent to an agent again and again on a timer. Each round the
agent wakes with no memory of the last one except what is on disk and in the brain, so the prompt
has to carry everything a fresh round needs to pick up the thread.

## The six parts

1. Cadence and end. "every 5 minutes for the next 10 days" - and write the end as a date and
   time too ("until 19 November 03:15"), because some schedulers drop a recurring job after a few
   days. With the end inside the prompt, the agent knows to set the schedule up again and when to
   stop and report.
2. The goal in the person's words. Copy them, typos fixed, into `ORDER.md` in a job folder.
   The prompt points at that file instead of repeating a long request every round.
3. What to read first. "read NEXT.md first" - one line saying the next step. Optionally the
   brain: "recall what we know about <topic> before you start".
4. What one round does. "do the next undone step, save the result, rewrite the first line of
   NEXT.md". A round should be small enough to finish in a few minutes; if a step is bigger, split
   it in NEXT.md.
5. Limits. What the agent decides alone and what waits for the person (money, deleting
   something with no second copy, publishing). Questions go out once, by email or a shared file,
   with a recommendation, and the loop keeps working on what does not depend on the answer.
6. Reporting. "when you finish a piece, write two lines on what changed" - into a file, an
   email, or a page the person opens. Every report names the task it answers.

## A template

```
/loop fire this every <N> minutes until <date time>. goal: see <folder>/ORDER.md.
read <folder>/NEXT.md first, do the next undone step, save the result, and rewrite
the first line of NEXT.md with what you did and what comes next. decide small things
yourself; for anything that needs me, send one short email with your recommendation
and carry on. when you finish a piece, add two lines to <folder>/REPORT.md.
at <date time>, stop the schedule and write the final report.
```

## Choosing the cadence

- 3 to 5 minutes: active building where each round is short and there is always a next step.
- 10 to 20 minutes: checking or testing work that another loop produces.
- An hour or more: slow external things (a long computation, a review, a daily count).

A round that finds nothing to do should say so in one line and end. It should not invent work.

## Before handing the loop over

- Make the job folder with `ORDER.md` and `NEXT.md` so the first round has something to read.
- Run the first round by hand straight away rather than waiting for the timer.
- Check after an hour: if the first line of NEXT.md has not changed, the loop is stuck on one
  step. Split it or skip it.

## Two loops on one project

One loop builds, a second checks what the first made and writes problems down without fixing
them. The builder reads those notes at the start of its next round. This catches mistakes that a
single agent repeats because it trusts its own earlier work.
