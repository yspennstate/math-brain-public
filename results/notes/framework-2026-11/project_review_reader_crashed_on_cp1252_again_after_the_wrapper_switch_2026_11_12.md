---
name: project_review_reader_crashed_on_cp1252_again_after_the_wrapper_switch_2026_11_12
description: "project_memory_cli.py read-offer dies with UnicodeEncodeError (cp1252), so an hourly review can never be read through or acknowledged? The 20 Aug UTF-8 fix sat in the nested wrapper only; on 11 Nov the hook line moved to the top-level wrapper. Fixed 12 Nov inside hourly_runner.main (reader commands reconfigure stdout to UTF-8), so both wrappers have it. A fix in a wrapper is lost when callers change wrapper"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:08:36+02:00
  status: verified
  evidence: "agent_run/project_context/reader_utf8_result.txt (rc 1 before, rc 0 after on the live file); ledger row of 12 Nov (e)"
---

The hot hook's hourly line tells a session to run `project_memory_cli.py read-latest --project P --session S`, and that prints one `read-offer <token> --shard N` command per shard. On 12 Nov 2026 `read-offer` on shard 0 of the live-brain review exited 1:

    UnicodeEncodeError: 'charmap' codec can't encode character '●' in position 17051

A Python whose stdout is a pipe on Windows encodes with the ANSI code page (cp1252). The shard held 648 characters outside it (box-drawing lines, a bullet, a minus sign: text pasted from terminals). The write failed before `mark_shard_served`, so the shard never counted as read, the review could not be acknowledged, and its "Hourly review N is due" line came back every hour. Only 12 of the 1,385 sessions in the signed cache hold any acknowledgement.

This was fixed once before, on 20 Aug 2026, in the wrapper `runtime/project_memory/project_memory_cli.py` (it reconfigures stdout to UTF-8). That wrapper loads the stale nested fork of the package, so on 11 Nov the hook's line was pointed at the top-level `runtime/project_memory_cli.py` instead, which never had the fix. The crash came back with that change and nobody saw it, because the line a session reads is the reminder, not the failure.

Fix, 12 Nov: `hourly_runner.main` calls `_utf8_stdout()` before the reader commands (`read-offer`, `read-latest`, `ack`), which reconfigures stdout and stderr to UTF-8 with `backslashreplace`. It lives in the package, so every wrapper has it; the hourly pass keeps the stream it was given. Backup `hourly_runner.py.bak_utf8reader_20261112`. Proof on the live file with no encoding variables set: rc 1 before, rc 0 after, output valid UTF-8 (`agent_run/project_context/reader_utf8_result.txt`).

What to keep from it: a fix placed in a wrapper is lost the day callers are pointed at another wrapper; put an encoding fix where the write happens. And when a reminder never goes away, run the command it names before assuming nobody bothered.

Not fixed: the size. The live-brain review is 56 shards of about 48,000 characters, 2.7 million in all, offered hourly to every session that ever had a prompt classed to the project (this session is offered eight projects). The reader works now; whether anyone should read that much each hour is a separate question. Related: [[project_memory_hook_writes_every_prompt_timing_it_ingested_4_test_rows_2026_11_03]].

