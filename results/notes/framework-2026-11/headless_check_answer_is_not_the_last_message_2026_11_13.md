---
name: headless_check_answer_is_not_the_last_message_2026_11_13
description: "A weekly scheduled check that runs a headless Claude session and scores its answer gave no verdict for three weeks, and its last verdict scored the wrong text. Two causes: the session inherited a low process priority and starved past its timer, and the script scored only the session's last message, which a closing-summary hook had made a short summary. Fixed by Normal priority, a longer timer and scoring every assistant message from the transcript."
metadata:
  type: project
  created: 2026-11-13
  status: verified
---

The brain runs a weekly check on its own writing: a scheduled script starts a headless Claude session, asks it six
fixed questions, and scores the answers for the marks of machine-written prose. For three weeks running every log
ended with the watchdog killing the session at eight minutes and an empty output file. The task's exit code was 0
or 1 and nothing read the log, so nobody saw it. The last real verdict before that was WEAK, on an answer of 144
characters.

Three causes, each measured on a run started through the scheduler itself:

1. Priority. The scheduler started the script at BelowNormal and the headless session inherited it. On a loaded
   machine the session had 6.7 seconds of CPU in its first two minutes and had written nothing. Raised to Normal by
   its process id, it used 30 seconds in the next four minutes and answered at 9 minutes 43 seconds, which the
   eight-minute timer could never have allowed. The task's own priority setting now starts it at Normal, and the
   timer is 25 minutes.
2. What was scored. `--output-format json` returns only the session's last message. A Stop hook makes every
   headless session end on a short summary of what it was told and what it did (910 characters here). The six
   answers, 3,152 characters, sat one message earlier and were never scored; the 144-character WEAK verdict was
   this. The script now takes the session id from the JSON, opens that session's transcript, and scores every
   assistant text block, logging how many it read.
3. The model line named an older model; it now names the current one with a fallback, at high effort.

The proof run, started through the scheduler, answered in about 16.5 minutes on a machine that hit a memory alarm
part way through, and read "scanning all 4 assistant texts (5,465 characters; the last message alone is 863)",
then "AI-tells 0", PASS. The same answers scored on the closing summary alone had given a different count.

How to apply: any scheduled job that runs a headless session and reads its answer has the same two traps. Check
the child's priority class before blaming the timer, and read the transcript, not the `result` field, whenever the
answer you want may not be the last thing the session says. A check that can end without a verdict also needs
something that alarms when the newest log has no result line.

Related: [[gist_belownormal_starvation_on_a_saturated_box_2026_11_13]] (the shared mechanism behind cause 1).
