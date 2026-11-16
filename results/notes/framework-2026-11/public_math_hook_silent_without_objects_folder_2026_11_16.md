---
name: public_math_hook_silent_without_objects_folder_2026_11_16
description: "[VERIFIED] Why does the math hook serve nothing on a fresh math-brain-public install? Root src/math_brain/selection_integrity.py read artifacts from <store>/objects, which the public export never ships (81,654 of 89,410 cards declare one): FileNotFoundError -> integrity:read_failed_or_inconsistent -> silent. Fixed 0fe060548 (16 Nov); the framework copy had the fix since 30 Oct"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T00:42:20+02:00
  status: provisional
  evidence: ""
---

Found 16 Nov 2026 00:1x by the conformance kit (an agent) in a fresh sparse clone of math-brain-public b0b01c92 with an empty HOME.

Symptom: every hook prompt that passed the math gate ended silent after 2-8 min; silence note integrity:read_failed_or_inconsistent (SelectionUnavailable). Cause: selection_integrity.consistent_hits passed artifact_root=<store dir>/objects for any card whose metadata names artifact_path/artifact_digest (81,654 of 89,410 public cards); current_note._artifact_binding does Path(root).resolve(strict=True); tools/import_store.py builds only brain.sqlite3, origin/main has no objects/ anywhere. Before the fix 0 of 6 math prompts served; after, 2 of 2 by hand and most gate-passing conformance cases.

Fix: math-brain-public 0fe060548 (root used only when objects/ is a directory; the artifact is then NOT_REQUESTED, node digest and claim binding still checked) + two tests (the no-objects test fails without the fix). framework/mathbrain/src/math_brain/selection_integrity.py had carried the same fix since 30 Oct (a Mac clone without objects/ silenced 7,225 of 11,999 cards); the root src/ the public hook imports never got it. Lesson: a fix landed in one copy of a duplicated module is not landed; grep every copy (git ls-tree -r origin/main | grep <file>) when fixing one.

Also measured on the loaded workstation: the hook needs 42-222 s per prompt against its live 30 s budget (budget_exhausted_before_ranking), and the template 'I am working on this: <short title>. What is known...' is rejected by the math gate in 0.0 s. Related: [[math_recall_what_works_agents_2026_10_15]], [[the_math_hook_asks_each_package_for_refusal_in_its_own_form_2026_09_29]].
