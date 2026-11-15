---
name: project_review_wrapper_lost_utf8_fix_2026_11_12
description: "project_memory_cli read-offer cp1252 UnicodeEncodeError returns after switching wrappers and hourly review never acknowledges"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:30:40+02:00
  status: provisional
  evidence: ""
  lesson: true
---

On 12 Nov read-offer shard 0 exited 1 before mark_shard_served: the shard held 648 characters outside cp1252. The 20 Aug UTF-8 fix existed only in the nested wrapper; the 11 Nov hook switched to the top-level wrapper and bypassed it. Only 12 of 1,385 cached sessions held an acknowledgement, but the source does not show that this crash caused all missing acknowledgements. The package-level repair changed the live reader from rc 1 to rc 0 with no encoding environment override.

Windows piped stdout used the ANSI code page. Moving callers to a different wrapper discarded the wrapper-local fix; repeated reminders concealed the reader failure.

**Why:** Put encoding handling where output is written so every entry path shares it.

**How to apply:** Run the command a repeating reminder names, check served/ack state, and test both wrappers without UTF-8 environment overrides; keep the fix in hourly_runner.main for reader commands. The separate 56-shard, 2.7-million-character size problem remains unresolved.

[[project_review_reader_crashed_on_cp1252_again_after_the_wrapper_switch_2026_11_12]]

Drafted by Codex worker W07 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

