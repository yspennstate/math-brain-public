---
name: orphan_scripts_42_of_426_but_31_are_memory_evidence_no_prune_d10_68_2026_11_08
description: "No prune list (8 Nov): D10 #68 finds 42 of 426 dreaming scripts unwired, unnamed by code or docs and not run in 10 d, but 31 of the 42 are cited by memories as evidence; the 11 uncited are under 100 KB. Mac file mtimes all date from the 28 Oct port, so age must come from transcripts"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T06:37:44+04:00
  status: verified
  evidence: "d10_68_orphan_faculty_list_2026_11_08.py --days 10, grep -F over memory folder, 8 Nov 06:4x"
---

Is there an orphaned-faculty prune list worth keeping for ~/.claude/dreaming (1000-ways D10 #68)? Not as a prune list. Measured 8 Nov by an agent, read-only.

Of 426 top-level scripts:
- 69 are wired: settings.json, hook_dispatch_list.json or a com.brain.* LaunchAgent.
- 273 are named by other code.
- 47 are named in skills, CLAUDE.md or the keep-working queue.
- 355 appear in a Bash call in the last 10 days.

42 are none of these and older than 10 days, 250 KB in all. 31 of those 42 are cited by memories as their evidence: ascii_lint.py by 36, dream_unthrottle.py by 19, the rest mostly finished evals and tests. That count was taken twice, per file and by one grep -F over the memory folder. Deleting them would repeat [[memories_cited_34_mac_scripts_gone_16_rebuilt_from_transcripts_2026_11_08]]. The 11 uncited ones are under 100 KB and include working tools (remember_from_json.py, the literature_* pipeline).

File age cannot carry this test on the worker machine. Every script's mtime is 28 Oct or later, the day the port copied them in, so "not run in N days" has to come from the transcripts, not the file.

Not built: nothing here costs disk or attention, and the main thing a prune list would flag is evidence. If the author wants a smaller folder, the safe set is the 11 uncited files, moved to an archive and never deleted.

Script: d10_68_orphan_faculty_list_2026_11_08.py [--days N] [--show N].

**How to apply:** before calling any brain script dead, grep the memory folder for its file name; a script a memory cites is evidence, not padding.

