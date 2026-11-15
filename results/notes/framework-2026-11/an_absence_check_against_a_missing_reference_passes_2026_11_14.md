---
name: an_absence_check_against_a_missing_reference_passes_2026_11_14
description: "[VERIFIED] Secret 'absent' check passed? Make sure the value you test for was found: a check whose reference is None passes on everything"
metadata:
  type: feedback
  created: 2026-11-14
  created_at: 2026-11-14T19:55:29+02:00
  status: provisional
  evidence: ""
---

On 14 Nov the prompt-store pack script took the leaked password from the source ledger, the regex found nothing there (it lived only in the typed history), tok was None, and 'token absent from 15 files and the sqlite' printed while four card/network files and the sqlite still held it. Two files were queued for the Google bucket and dequeued before the pusher read them.

**Why:** a negative check is only as good as its reference; an empty or None reference makes every 'not in' true.
**How to apply:** assert the reference exists before testing absence (assert tok), and take it from where the leak was seen, not where you expect it. Related: [[a_card_that_drops_input_must_name_it_2026_11_14]], [[agents_audit_check_scars_smell_test_2026_07_31]].
