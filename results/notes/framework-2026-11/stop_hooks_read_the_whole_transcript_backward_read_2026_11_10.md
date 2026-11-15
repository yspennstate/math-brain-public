---
name: stop_hooks_read_the_whole_transcript_backward_read_2026_11_10
description: "Stop hooks slow (3.3 s median)? registry_refresh.py and resume_checkpoint.py read up to 80 MB of the transcript on every Stop to find the last assistant message; since 10 Nov they read backward and stop at it: 0.5 s -> 5 ms a file, same output"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T10:13:09+02:00
  status: verified
  evidence: "scratch hookfast/last_assistant_equal.py: 806 cases on 120 transcripts, 0 differences, 241 -> 3.1 ms a file; installed_check.py on the 30 newest live transcripts 0 differences; registry_refresh --selftest PASS"
---

Two Stop hooks, registry_refresh.py and resume_checkpoint.py, carry the same `_last_assistant(tp)`: find the last
assistant text message of the session's transcript. Since 11 July it read the whole file (up to 80 MB), split it into
lines and walked forward keeping the last match, because the fixed tails before it (200 KB, 800 KB) returned a message
several turns old on a long session. On 10 Nov 2026 the sampled Stop profile put 1,038 ms and 884 ms of a 3,261 ms
median Stop in those two hooks, and on the 30 most recently written transcripts the function took 0.52 s and 0.64 s a
file (transcripts here run to tens of MB; 120 of them hold 65 GB, the largest 6 GB).

**Fix, installed 10:10 on 10 Nov.** The function reads backward from the end in 2 MB blocks and returns at the first
line that is an assistant text message. That is the line the forward scan ended on, so there is still no window to
miss it; the last message is almost always inside the final block. The 80 MB cap and its dropped cut first line are
kept. Per-line logic moved into `_assistant_text(ln)` unchanged. registry_refresh.py d8c4b3b0e4dc07f2,
resume_checkpoint.py 4a6df01e8128e455; backups `*.bak_backread_20261110` beside them; GitHub d7eac7e7 and 50400ff2.

**Measured.** Old against new on 120 real transcripts, whole, cut at random byte offsets (a transcript mid-write) and
with the cap set to 3 MB and 300 KB with a 256 KB block (the capped path): 806 cases, no difference; 241 ms -> 3.1 ms a
file. After the install, the live files against their own backups on the 30 newest transcripts: no difference,
0.5-0.6 s -> 5 ms a file. `registry_refresh.py --selftest` passes. Harnesses: scratch hookfast/last_assistant_equal.py
and installed_check.py of session agent.

**One behaviour differs, on purpose.** A transcript line that is valid JSON but not an object made the old function
return nothing at all (the exception left the loop). The new one only meets such a line if it lies after the last
assistant message. No transcript on this machine has one.

**Not changed.** pre_report_check.py, report_guards_hook.py, work_timer.py, claim_check.py and retraction_guard.py
have their own `_last_assistant`; they read tails, not the whole file. task_checklist_hook.py is the other large Stop
cost (0.9 s: a 13.6 MB state file and a 6.6 MB view rewritten on every prompt and Stop) and was left as it is.

Related: [[four_wired_hooks_off_the_fast_list_cost_every_tool_call_2026_11_10]] (the same morning's PreToolUse and
prompt fixes). What would change this: a Stop where the registry checkpoint or the Where-I-was file names a message
older than the session's last one.


Method drawn from this and two sibling fixes of the same morning: [[method_measure_what_an_event_reads_before_its_logic_2026_11_10]] (measure what an event reads or spawns before reading its logic).
