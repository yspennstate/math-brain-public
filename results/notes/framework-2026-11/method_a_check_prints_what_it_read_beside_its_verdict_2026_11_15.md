---
name: method_a_check_prints_what_it_read_beside_its_verdict_2026_11_15
description: "Scan says 0 hits, guard says 'limit seen', count says 0 drivers? Before believing it read WHAT THE CHECK READ: bytes scanned, files opened, the matched line, the field tested. 14-15 Nov: 0 hits over 12.46 GB never read (rg missing, rc 127); a pool stopped 70 min on a log line quoting the brain. A verdict with no input size beside it is unread"
metadata:
  node_type: memory
  type: reference
  created: 2026-11-15
  created_at: 2026-11-15T11:38:00+02:00
  status: provisional
  evidence: "the source memories' own numbers (read 15 Nov nap, not re-measured): a_scan_whose_tool_is_missing_reports_zero_hits_2026_11_15 (rc 127, windows.bin 0 bytes, 12.46 GB unread); codex_pool_usage_limit_grep_matched_quoted_brain_text_2026_11_15 (12 of 67 briefs unstarted, about 70 min idle); MISTAKES.md rows of 2026-09-02 (ps field) and 2026-09-13 (pgrep | head -1)"
  originSessionId: 8a4e6c91-ba50-4ffa-9bbc-07238aac5bd2
  modified: 2026-11-15T09:38:18.715Z
---

**The move.** A check's verdict is believed only with what the check READ printed beside it. For a search that
reports a count: bytes scanned and files opened, against the bytes on disk. For a guard that matches a phrase: the
matched line itself and where in the file it sat. For a process or lane count: every match with its command line,
never the first. If the input size is missing, zero, or the matched text is not the thing the check was written
for, the verdict is unread, whichever way it points.

**Where it worked (cases read from their memories on 15 Nov 2026, numbers theirs):**
- A secret scan before an irreversible bucket lock printed `hits_total 0`. The prefilter binary was not installed
  (exit 127), its output file was 0 bytes, and the exact scanner counted hits in nothing: 12.46 GB never read. The
  replacement scanner prints what it opened and passed controls both ways.
  [[a_scan_whose_tool_is_missing_reports_zero_hits_2026_11_15]]
- A Codex pool wrote STOP on "usage limit seen" with 12 of 67 briefs unstarted and sat about 70 minutes. The
  matched line was brain text a worker had echoed into its own log. The guard now counts a limit only in the last
  20 lines of an exited worker's log. [[codex_pool_usage_limit_grep_matched_quoted_brain_text_2026_11_15]]
- Same family, one day earlier: [[an_absence_check_against_a_missing_reference_passes_2026_11_14]] (an "absent"
  result when the thing compared against was itself missing).
- The September ancestors in MISTAKES.md fit after the fact: a driver count of zero on a box completing 800 lanes
  an hour (the wrong `ps` field was tested, 2 Sep), and `pgrep -f <pattern> | head -1` returning the caller's own
  wrapper at 3 MB (13 Sep). In both, printing the matched command line would have shown the miss at once.

The two directions are one fault. A clean result from an empty input and an alarm from the wrong line both come
from a check that reports its conclusion without its input. The first is the dangerous one before an irreversible
step; the second costs idle hours because a stop is rarely re-read.

**Where it would not work.** A check whose input is right and whose LOGIC is wrong (a threshold, a sign, a
timezone) prints a healthy input size and still lies; this move does not see that, and a positive control through
the same pipeline does. And on a check that fires thousands of times a day the extra line is noise: print the
input size always, the matched text only on the rare branch (a stop, a clean before a lock).

**The one check that breaks it.** Feed the check an input known to contain the thing and an input known to be
empty or unreadable, through the SAME pipeline. If the two print the same verdict line, the check cannot tell a
clean world from a blind instrument, and nothing it prints later counts. If a check that prints its input size
still passed a blind run, this method is not enough and the control is the method.

**The size of the doubt.** The remedy was applied in two cases (the scanner, the pool guard); the other three are
fits made afterwards. No count yet of how many of our guards print their input. Related methods:
[[method_liveness_needs_identity_and_rate_2026_11_11]] (the same idea for "is it running"),
[[method_watch_a_periodic_pass_by_its_output_2026_11_12]], and the scar [[a_scanner_piped_to_tail_fails_open_2026_09_10]].
