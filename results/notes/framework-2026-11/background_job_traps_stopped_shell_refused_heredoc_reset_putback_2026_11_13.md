---
name: background_job_traps_stopped_shell_refused_heredoc_reset_putback_2026_11_13
description: "Output file went empty after stopping a background job, or a job ran a script that was never written, or committed text is back on an old version after a clone reset? Stop the script's bash by id before its child; ffmpeg needs -nostdin; a refused command drops its heredoc file too; check a put-back per path against the pre-reset head"
metadata:
  type: feedback
  created: 2026-11-13
  created_at: 2026-11-13T18:16:47+02:00
  status: verified
  evidence: "this session's own errors of 13 Nov, each seen once and fixed"
---

A finished file went empty, a job ran a script that did not exist, and committed text was back on an old version for ten hours. Why? Four traps from one day (13 Nov 2026, one loop session), each with the check that catches it.

1. A stopped background job leaves its shell alive. Stopping the job through the harness ended the child (ffmpeg) but not the bash that ran the script; that bash went on to its next line and rewrote an output file that an earlier run had finished, leaving it at 0 bytes. Check: after a stop, list the script's bash by command line and stop it by id first, then its child by id, each stop alone. Then look at the sizes of the files the script writes.

2. ffmpeg in a background shell waits on the terminal. Without -nostdin and stdin from /dev/null it can sit forever at zero CPU with a growing-looking but stalled output. Check: every background ffmpeg line carries -nostdin and < /dev/null.

3. A command the ack gate refuses did not run at all, and that includes the heredoc inside it. I re-sent only the second half (the ssh that feeds the script file) and got "No such file or directory", because the cat > file <<EOF of the refused command never wrote the file. Worse, once a background job was launched for a script the gate had refused. Check: after a refusal, re-send the whole command; before launching a job on a script file, ls the file.

4. A reset of the shared brain clone drops local commits, and a put-back by hand can miss one. The dream's sync reset the clone at 06:21 (reflog: reset: moving to 7fb616b8b5f; head before it f4788ac6a2f, 124 local-only commits over 4,778 files). My put-back at 06:47 restored the files I remembered and missed one document commit, so the old version of that document stood until 16:0x and was nearly used. Check, per path, not from memory: git rev-parse f4788ac6a2f:<path> against git rev-parse HEAD:<path> and git hash-object <path>; restore with git show f4788ac6a2f:<path> into a temp file and a move, under a claim, then compare the blob hash. A whole-tree audit that evening found nothing still on the base version (0 lost, 150 changed again since).

What ties them together: in each case the thing I trusted was a report (job stopped, command sent, files restored) and the thing that was true was a file's size or hash. Read the file.

Related: [[a_pipe_reports_the_filters_verdict]], [[fresh_source_called_stale_on_negative_age_valuation_observer_2026_11_12]].

