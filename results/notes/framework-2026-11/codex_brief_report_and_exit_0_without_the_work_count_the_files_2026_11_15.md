---
name: codex_brief_report_and_exit_0_without_the_work_count_the_files_2026_11_15
description: "Codex brief shows REPORT.md and exit 0 but the test never completes? 15 Nov: four writers ran while their script was missing, reported it and ended exit 0 with no pages; two more died as 'gave up' and as a page printed into the log. Count the work files by name, relaunch on three last-line shapes, move the stale report out first."
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T05:28:24+02:00
  status: provisional
  evidence: "codex_local_1108/briefs/WBAB4_T4, WBAB5_D1, WBH1_T1, WBH1_T3 (REPORT.md 03:03-03:10, no page files), WBAB5_D4 and WBAB4_C6 codex.log; relaunched 05:19 by the second relauncher"
---

Seen 15 November on the Codex rig (codex_local_1108/run_one.py), in four blind writing tests of thirty writers.

What happened. Between about 02:57 and 03:10 the script the treatment writers are told to run
(writing_brain/turn/turn.py) was missing from disk (the dream's sync had removed local copies that night; it was
restored at 03:18). Four writers (WBAB4_T4, WBAB5_D1, WBH1_T1, WBH1_T3) ran in that window. Each did the right thing:
it refused to substitute its own method, wrote a REPORT.md and a LOG.md saying the script was missing and the task
unfinished, and ended. The harness logged "exit 0". None wrote a page.

Why nobody saw it for two hours.
- The relauncher acted only on a last log line "exit 1".
- My state lister counted a brief as finished when REPORT.md existed.
- The stager, correctly, counted a writer only when its page files existed AND the log ended "exit 0", so it sat at
  9 of 18 and said nothing about why.
Two more deaths of the same kind the same night: a log ending "gave up after 4 network retries; relaunch the brief by
hand" (WBAB5_D4, dead from 00:25), and "exit 0" with the page printed into the log and no file written (WBAB4_C6,
from 02:14).

The rule. A brief is finished when the files it was asked for exist, counted by name (page1.md..pageN.md,
JUDGEMENT.json). REPORT.md, LOG.md and exit 0 say that a run ended, not that the work was done. A relauncher must act
on three last-line shapes, not one: "exit 1", "gave up ...", and "exit 0" with the work files missing. Before a
relaunch, move the stale REPORT.md and LOG.md out of the folder, or the fresh run reads its predecessor's refusal.
And when a test depends on a script, check that the script is on disk at each launch, not only when the test was
built.

Where the fix is. Second relauncher S/relaunch2.sh (this session's scratchpad; same id at most once in 25 minutes
and three times in all, windowless through one VBS), state lister writers_state.py now counting pages, stale notes
kept under failed_0300/. All six briefs were relaunched at 05:19.

What would change this: a harness that takes the expected output files as an argument and writes its own
"work missing" line; then the relauncher needs only that line.

Related: [[codex_rig_launch_slot_starves_waiters_and_gave_up_exit_0_2026_11_15]],
[[dream_sync_deleted_3055_local_copies_fallback_then_absent_mark_2026_11_15]],
[[a_scan_whose_tool_is_missing_reports_zero_hits_2026_11_15]].

