---
name: rules_appended_below_main_guard_unseen_by_script_run_2026_11_08
description: "Why did the live audit use the wrong rules while the control passed? Scar (8 Nov): definitions appended below the main guard; an importing control cannot see it"
metadata:
  type: feedback
  created: 2026-11-08
  created_at: 2026-11-08T15:28:15+04:00
  status: verified
  evidence: "brain_improvement/DIAG7_20261108 VALIDITY_NOTES.txt"
---

Why did a script's live audit use the wrong rules while its control passed? Scar (8 Nov, DIAG7): the new definitions were appended below the `if __name__ == "__main__": main()` line.

patch7.py appended BASE["recall"] and BASE["grep"] to the end of run_audit.py. control7.py imports the module, so the whole file ran and the rules were there: 25 of 25 allowed, 43 of 43 caught. Run as a script, main() ran first: the grep runs were audited by an older BT2 rule of the same name (denies all python) and voided wrongly, and the recall runs died with KeyError after the agents had finished, before writing their audit records.

How to apply: a patch that adds module-level definitions inserts them above the main guard, never appends. A control that imports a module does not test the script path; add one check that executes the file's text up to the guard (or runs main on a dry case) and asserts the new names exist. If it happens anyway, the transcripts are complete: re-audit them with the fixed module (DIAG7 rebuild_audit.py) and keep the as-run copy.

Evidence: private-repo 12_cognitive_architecture/brain_improvement/DIAG7_20261108 (VALIDITY_NOTES.txt, run_audit.as_run.py, rebuild_audit.py). Result in [[diag7_grep_32_recall_16_codex_17_15_agent_11_08]].

