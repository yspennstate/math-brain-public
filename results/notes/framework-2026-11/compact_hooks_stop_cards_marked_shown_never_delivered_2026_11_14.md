---
name: compact_hooks_stop_cards_marked_shown_never_delivered_2026_11_14
description: "[VERIFIED] compaction cards silenced? Fixed 14 Nov: on a Claude Stop compact_hooks.py marked cards shown (cooldown started) though Stop context is never delivered (171 'not delivered' rows by 11:00); now holds them, carries final_report/lesson_before_compact to the next event (2 h), cp52 verdict waits too"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T11:20:58+02:00
  status: provisional
  evidence: ""
---

hook_dispatch.py logs 'Stop: context from X not delivered (the event defines no hookSpecificOutput)' - Claude Code delivers no additionalContext on Stop. compact_hooks.py still ran choose() on Stop and wrote shown[id]=now, so CP02/CP41 (final_report), CP16/CP43 (lesson_before_compact) and the tokens_* cards were spent unseen and then silenced by their cooldown; a CP51/CP52 node verdict landing on a Stop was popped and lost. Fix (commit d960e272, live ~/.claude/dreaming/compact_hooks.py): stop_hold on a Claude Stop picks nothing, saves the Stop-only kinds as st['stop_carry'], the next non-compact event within STOP_CARRY_S=2 h adds them; cp52_pending is not resolved on a Claude Stop. Control: scratch area test_compact_stop_carry.py fails on the old file (prints on Stop), passes on the new. Codex path untouched. Still open: compact_on_task_end.py's informational print on Stop is also undelivered (harmless, its helper does the work). Generalises: any hook that records 'shown' on an event the harness cannot deliver silences itself - check TOP_LEVEL_EVENTS_WITHOUT_HSO in hook_dispatch.py before counting a fire.
