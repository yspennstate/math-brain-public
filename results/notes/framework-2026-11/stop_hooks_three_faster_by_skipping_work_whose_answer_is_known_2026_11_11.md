---
name: stop_hooks_three_faster_by_skipping_work_whose_answer_is_known_2026_11_11
description: "Stop hooks slow (resume_checkpoint, pre_report_check, verify_gate)? Since 11 Nov each skips work whose answer is known: cached foresight line, backward tail read, no-claim quick path; 110->4.5, 124->12, 350->41 ms"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T09:33:09+02:00
  status: verified
  evidence: "equivalence runs on cut real transcripts (520 and 270 cases, 0 mismatches), gate controls 0 failed, brain main dd28683898e9, ledger ee1159836b2d"
---

On 11 Nov 2026 (09:10-09:27 local) three Stop hooks stopped doing work whose answer was already known. Each runs on every Stop of every Claude session, and Stops come every few seconds in a loop session.

- resume_checkpoint.py (130 ms median): foresight.brief() re-parsed MISTAKES.md (580 KB) and instincts.tsv (540 KB) every Stop, about 95 ms plus a 28 ms import, for a line that changes only when those files do. The line is now kept in `~/.claude/dreaming/resume/foresight_brief.json`, keyed by size and mtime of foresight.py, MISTAKES.md, instincts.tsv and PREDICTIONS.md. 110 -> 4.5 ms in-process on a hit. If brief() ever reads a new file, add it to `_BRIEF_INPUTS` or the line goes stale.
- graph_fire/pre_report_check.py (98 ms): the tail reader decoded and split 4 MB and parsed every line twice to find the turn's boundary and the last assistant text. It now reads the same bounded tail backward in 256 KB blocks and parses only lines that name user or assistant. 520 cuts of 40 transcripts, 0 mismatches, 124 -> 12 ms mean. Side fix: the old reader threw on a JSON line that is a list, and the hook then said nothing.
- verify_gate.py (57 ms median, 0.1-3 s on long loop turns): claude_turn widens its read to 48 MB and parses every line after the prompt. But every rule needs LEAN_CLAIM, CODE_CLAIM or PROOF_CLAIM to match the final text. So with no block pending for the session and no claim match, the gate now writes the same seen row and state and returns without the walk (claude_final reads the final text backward). 270 cuts of 30 transcripts: decide() output identical, 268 took the quick path, 350 -> 41 ms mean. VERIFY_GATE_QUICK=0 turns it off.

How to verify: hook_profile rows for Stop (the flag `~/.claude/compute/hook_profile.on` lapses 3 h after its mtime); each gate's own controls (`verify_gate.py --selftest`, `pre_report_check.py --selftest`). Rollbacks are the `.bak_briefcache_20261111`, `.bak_revtail_20261111` and `.bak_quickfinal_20261111` files beside each hook.

How to apply elsewhere: before optimising a hook's parse, ask whether its answer is already decided by something cheap (a file's stamp, one regex on the final text, the last few lines read backward). The Stop hooks that read transcripts forward over megabytes are the usual case. A cheap check that decides most calls, with equivalence tested on cut real transcripts, beats a faster parser. Related: [[checklist_stop_bursts_written_once_by_a_flush_child_2026_11_11]], [[bm25_lazy_imports_save_30_ms_per_scoring_hook_2026_11_11]], [[hook_budget_agent_loop]].

