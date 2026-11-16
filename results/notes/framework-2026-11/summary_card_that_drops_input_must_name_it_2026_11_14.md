---
name: summary_card_that_drops_input_must_name_it_2026_11_14
description: "A failure mechanism for any card, status line or report built from many inputs: one path (an early return, a skip, a carried value, a dedupe, a length cut in the sender) drops part of the inputs while the totals and the top line still print as if they covered everything. Nothing errors and the card is green. Seven cases from one audit of monitoring cards, and the prevention rule: every dropped input reaches the output by name, and a green 'all' line is checked against the count it claims."
metadata:
  type: project
  created: 2026-11-14
  status: verified
---

The mechanism. A summary is built from several inputs (sources, records, monitored jobs, readings). One path through
the code drops some of them while the totals and the top line are still printed. The reader sees a confident,
complete-looking number that covers less than it says.

Cases from one audit of monitoring cards sent to a phone:
- a source whose first read failed returned early, so its items vanished from an otherwise healthy card;
- a note written once per source counted one item present in three sources as three items;
- the shared sender stripped markup and cut everything past 4,000 characters, so a long card lost exactly the lines
  that said what was missing;
- one incomplete source emptied every source's section, and the card then went silent instead of saying why;
- with no time-zone database, a business-hours check returned always open, so a notice went out every hour all
  weekend;
- a fleet card skipped a tracked job whose output file was missing and still printed "all tracked jobs producing
  fresh data" under a green tick; off hours it judged late jobs by a relaxed rule, so 9 of 28 jobs 10-15 hours old
  read fresh;
- an alert card saved its new baseline before sending, so a failed send lost the alert for good.

When to look for it: when writing or changing code that turns many inputs into one summary someone reads and trusts
(a phone or email card, a status line, a dashboard tile, a report total, a "covers N of M" line) and any path can skip,
carry, merge or cut an input; or before trusting such a summary's total. Not when the code does arithmetic on one
input, or when the summary already names every dropped input with a count the reader can check.

Prevention.
- Every early return, skip, carry, dedupe and truncation makes the dropped thing reach the output as a named line, or
  a count with the names in a linked file.
- Count distinct objects, not notes about them.
- Budget the length before the sender cuts it, and put the lines that say what is missing above the long lists.
- A green "all" line is checked against the count it claims (fresh equals tracked) and never covers items judged by a
  relaxed rule.
- Advance a baseline only after the card is out.
- Test each path with a real input on it, and with the old code first: the test must fail on the old code.

Related: [[near_neutral_dial_is_not_a_noop_control_2026_11_16]].
