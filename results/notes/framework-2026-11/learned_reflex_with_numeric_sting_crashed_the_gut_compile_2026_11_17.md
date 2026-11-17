---
name: learned_reflex_with_numeric_sting_crashed_the_gut_compile_2026_11_17
description: "[VERIFIED] Gut stale (instincts_learned.json newer than instincts.tsv)? instincts.py crashed TypeError 'expected string, got float' in _assert_no_financial_oracles: REM 16 Nov wrote 'sting': 0.6 (meant charge). Fix the entry, recompile, check rc and tsv mtime"
metadata:
  type: feedback
  created: 2026-11-17
  created_at: 2026-11-17T03:31:57+02:00
  status: provisional
  evidence: ""
---

17 Nov 03:30. The waking check said the gut was stale: instincts_learned.json (16 Nov 19:17) newer than instincts.tsv (16 Nov 11:20). --parse-only passed (684 reflexes, 0 malformed), so the parser does not type-check fields; the full compile died in _assert_no_financial_oracles at _DOLLAR_ORACLE.search(it.get('sting')) because reflex a_lever_upstream_of_a_stage_that_re_decides, added by the 16 Nov REM dream, had 'sting': 0.6 where every other entry has 'charge': 0.6 and a text sting. Fixed with a byte-exact single-line replace (LF kept, 647 entries parse), sting written from its source field, charge 0.6. Recompiled rc 0, instincts.tsv 745,873 bytes at 03:30. Lesson: a parse-only pass is not a compile check; a reflex writer should run the full compile (or at least type-check gut/sting as strings) before it reports a reflex landed. The REM journal said 'the next build picks it up' and the next build is exactly what it broke. Related: [[a_python_rewrite_of_a_shared_ledger_truncates_first]].
