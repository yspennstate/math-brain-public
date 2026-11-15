---
name: the_wake_says_five_dark_days_the_prompt_ledger_has_twenty_three_2026_11_12
description: "How many days has the prompt-class ledger been dark? Twenty-three, not the five the wake line prints: the last day with a class_model row is 2026-10-20 and 71,071 rows have gone unclassified since (counted twice over the whole 240 MB file, 12 Nov 10:37-10:38 JST). The alarm built by that morning's SWS pass reads a bounded tail, so it cannot report a span longer than its bound - and its own repair text, classify yesterday, would turn the line green over 22 still-dark days"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T10:39:18+02:00
  status: verified
  evidence: "two full scans of memory/prompts/PROMPTS.jsonl on 2026-11-12 10:37 and 10:38 JST: 205 days 04-15..11-12, last classified day 2026-10-20 (2271 rows, 172 classified), 23 dark days, 71071 rows; the wake line as served into this session"
---

THE NUMBER: the prompt-class ledger (memory/prompts/PROMPTS.jsonl, 240 MB, 205 days 2026-04-15..2026-11-12)
has its last day with any class_model row on 2026-10-20 (2,271 rows, 172 classified). Every day since is
zero: 23 consecutive dark days, 71,071 rows. Counted twice over the whole file at 10:37 and 10:38 JST on
12 Nov by the nap, class_model non-empty against total rows per ts date.

WHAT THE WAKE SAYS INSTEAD: "prompt-class ledger dark: 2026-11-11, 2026-11-10 have owner prompts and zero
class_model (5 days in the tail unclassified) - the SWS section P pass is not running; classify yesterday".
Five, against twenty-three. The alarm was built hours earlier, by the 12 Nov SWS pass, and it reads a
BOUNDED TAIL of the ledger (the same 4 MB bound whose off-by-one that pass caught and wrote up in its own
reflection). A bound that holds about five days of rows cannot report a span longer than its bound, and
this one is four and a half times longer.

WHY IT MATTERS MORE THAN THE DIGIT: the wake line names the repair in the reader's units - "classify
yesterday (sidecar -> python apply_prompt_classes.py <sidecar>)". A reader who does what it says classifies
one day and the line goes green while 22 days stay dark, which is the same false green the three previous
spells died of (07-14/15; 09-08..11, 353 prompts; and this one). An alarm that under-states its subject is
worse than a loud one: it converts a backlog into a chore and then reports it done.

THE FIX THIS ASKS FOR (not done here - a nap does not start it): the ledger line must count over the WHOLE
file, or over a tail sized from the dark span it has already found, and it must print the last classified
DAY and the number of dark days, not a count of days seen in a window. The repair itself is 23 sidecars
through apply_prompt_classes.py, and it belongs to an SWS pass.

Related: [[method_watch_a_periodic_pass_by_its_output_2026_11_12]],
[[truncated_view_is_not_the_population]], [[green_is_not_trusted]],
[[gist_weakest_channel_false_green_2026_07_25]]

