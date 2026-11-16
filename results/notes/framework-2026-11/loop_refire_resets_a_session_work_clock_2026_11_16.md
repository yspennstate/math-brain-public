---
name: loop_refire_resets_a_session_work_clock_2026_11_16
description: "A work-session hook that holds an agent to a stated duration restarted its clock every time a scheduled loop re-sent the original request, so a ten-hour task asked for at 03:41 was still being held open at 23:39. The end of a timed task is the time of the first request plus the stated duration; a re-sent copy of the same text is not a new request."
metadata:
  type: feedback
  created: 2026-11-16
  status: provisional
---

The mechanism. A hook reads each user turn; when the turn asks for work over a duration ("for the next ten
hours"), it records an end time and refuses to let the session stop before it. A scheduled loop then re-sends the
same request every three minutes. Each copy arrives as a new user turn, the hook reads the duration again, and the
end time moves forward by three minutes. Seen on 16 November: the request came at 03:41 for ten hours, so the work
ended at 13:41; the hook's end time had walked to 23:29, 23:30, 23:32 and on to 23:39, and after 13:41 the stop
hook kept holding the session to a time nobody had set.

How to apply.
- Compute the end of a timed task from the first request's time plus the duration it states.
- When the hook's clock and that computation disagree, close at the computed time: cancel the loop's schedule, mark
  the task done and say in one line why the hook's clock does not apply.
- The fix belongs in the hook: a turn whose text equals the running loop's own request is a re-fire, not a new
  request, and must not move the clock.

Status: provisional, one session. What would change it: the hook fixed and a second loop observed to end on time.

Related: [[agent_written_turns_stored_as_user_requests_2026_11_14]].
