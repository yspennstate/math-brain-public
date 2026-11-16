---
name: plain_append_in_hooks_overwrites_rows_on_windows_2026_11_14
description: "Hook log with rows starting mid-word? Concurrent plain open('a') appends on Windows overwrite each other; route through append_journal.append_text (instinct_prime emit errors fixed 14 Nov)"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T23:03:07+02:00
  status: verified
  evidence: "instinct_emit_errors.tsv 33/540 fragment rows; race control old 1063/1200 rows 120 malformed vs new 1200/1200 0"
  lesson: true
---

Rows in instinct_emit_errors.tsv that begin mid-word (no timestamp, a reflex-list tail)? They were left by concurrent hook calls. _note_emit_failure appended with a plain io.open(..., "a"); on Windows that is seek-to-end then write, so two hooks in the same instant wrote at the same offset, the shorter row covered the start of the longer, and the longer row's tail stayed behind. 33 of the file's 540 rows were such tails on 14 Nov 2026, and an unknown number of rows were lost outright. The fire log and suppressed log, which go through append_journal.append_text (a per-file lock), had 0 malformed rows in their last 50,000.

Fixed 14 Nov 23:0x (an agent, pushed): the row goes through _append_text first and the plain append is only the fallback. Race control (scratch emit_race.py, 8 processes x 150 rows): old 1063 of 1200 rows kept and 120 malformed; new 1200 of 1200 and 0 malformed. test_suppressed_log_failure.py and test_refill_ab_symmetry.py still pass.

**Why:** an error log is the instrument for lost writes; if it races, the loss it measures is itself undercounted.
**How to apply:** any log several hooks append to goes through append_journal.append_text, never a bare open("a"); see [[a_card_that_drops_input_must_name_it_2026_11_14]].

