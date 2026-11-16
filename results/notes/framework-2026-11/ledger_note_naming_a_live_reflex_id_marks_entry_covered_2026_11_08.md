---
name: ledger_note_naming_a_live_reflex_id_marks_entry_covered_2026_11_08
description: "Scar: why did foresight's unguarded count drop when I only added a note to MISTAKES.md? Its parse reads any live reflex id anywhere in an entry's tail as coverage; a note naming a reflex to say it does NOT reach the slip flips the row. Write the name with hyphens, rerun the parse"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:11:23+04:00
  status: verified
  evidence: "foresight.py:147-158; parse 6->5->6 none on 8 Nov 03:10 with FORESIGHT_CACHE=0"
---

On 8 Nov 03:10 I wrote a measurement sub-bullet under the 18 Oct tautological-check entry in MISTAKES.md. To say the lesson already lives in another reflex's text, it named that reflex by its id. The entry was still marked `reflex: none yet` and I meant it to stay unguarded, but foresight's unguarded count went from 6 to 5.

The cause is foresight._mistakes_parse (foresight.py, lines 147-158). It follows mistake_graph's coverage rule: any live gut id that appears after `reflex:` anywhere in the entry, continuation lines included, resolves the row to that id. The "now covered - <id>" convention works this way on purpose. A note that only mentions a reflex, to say it does not reach the slip, also flips the row.

I reworded the note to give the name with hyphens (a-pass-needs-a-way-to-fail), which the id pattern `\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+\b` does not match. FORESIGHT_CACHE=0 and a rerun of the parse gave 95 rows with 6 none again.

How to apply: before writing a note under a ledger entry that should stay unguarded, leave out the underscore form of any live reflex id, or write the id with hyphens. Afterwards, rerun the parse with FORESIGHT_CACHE=0 and check that the unguarded count did not move. To mark an entry covered on purpose, write "now covered - <id>" as the ledger does.

Related: [[the_mistakes_ledger_changed_form_and_its_readers_did_not_2026_09_27]], [[wake_foresight_line_same_in_170_of_171_mac_wakes_names_no_task_d5_04_2026_11_01]].

Symptom as an agent meets it (SYMLEAD1, 8 Nov, written from this note alone): After adding only an explanatory note to MISTAKES.md, foresight reports five unguarded entries instead of six. The entry you annotated still says 'reflex: none yet', and no new guard was added.
