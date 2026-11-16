---
name: pw1k_prose_rules_missed_phrases_split_across_a_line_break_2026_11_12
description: "[VERIFIED] pw1k prose phrase rule (see below, recent work, usual estimate) silent though the phrase is in the paper? Fixed 12 Nov: a literal space in a prose rx now matches blanks with at most one line break"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T14:51:02+02:00
  status: provisional
  evidence: ""
---

pw1k's 93 prose-scope regex rules wrote word gaps as one literal space, but the prose scope keeps the source's line breaks and blanks commands to spaces, so 'see(newline)below' passed P0813 in the ising margin paper (12 Nov) and 'Earlier(newline)work' passed P0835 in the D/N monograph. Fix (pw1k.py _prose_ws, live and mirror f0e3bcc on the private repository main): at compile time, for lowercase scopes except h and t, each run of literal spaces outside a character class becomes one-or-more blanks holding at most one line break; inside a lookbehind a space becomes a single whitespace class (lookbehinds must stay fixed width: P0863 raised until that was handled). Measured on 22 of our papers: rule-id counts differ in 3 places, two new true fires (linear-polymer discussion.tex:49 'the usual estimate', dn monograph ch13 'Earlier work') and one gloss line pushed out of the capped output. The first version used plain one-or-more whitespace and made P0797 (heading over twelve words) fire on 20 of 22 papers, because it crossed from one heading to the next through the blanked body: a whitespace widening must stop at a paragraph break and skip span-joined scopes. Selftest 37/37 (four new checks). Backups pw1k.py.bak_ws_20261112 beside the live file. What would change it: a rule that relies on a single space meaning exactly one space (none found).
