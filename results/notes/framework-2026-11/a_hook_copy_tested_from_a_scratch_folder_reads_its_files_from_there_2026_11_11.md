---
name: a_hook_copy_tested_from_a_scratch_folder_reads_its_files_from_there_2026_11_11
description: "[VERIFIED] Hook copy shows behaviour diffs only when run from a scratch folder? It reads files beside its own __file__ (math_sense vocab, proof_sense lean_check path); load the copy with __file__ in the live folder. Also: math_sense lazy regex live, ~15-27 ms/prompt saved"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T18:44:35+02:00
  status: verified
  evidence: "12_cognitive_architecture/brain_improvement/math_sense_lazy_regex_2026_11_11/README.md (ms_test.py --equiv: 48 diffs from scratch, 0 with live __file__; 0 post-swap)"
  lesson: true
---

A test of a hook copy run from a scratch folder can show a behaviour change that is not there, when the hook reads files beside its own __file__. On 11 Nov it happened twice in one evening: proof_sense builds the lean_check.py path from its folder, and math_sense reads math_vouch_vocab.json, math_anchor_vocab.json and math_coh_common_words.txt from its folder. The first old-against-new run of the lazy math_sense showed 48 differences, every one in _vouch_stage1: the scratch copy read an empty vocabulary and vouched for nothing.

The fix for the test: load the copy with __file__ in the live folder and the code from the scratch path (importlib.util.spec_from_file_location(name, live_dir/"_lazytest_x.py", loader=SourceFileLoader(name, scratch_path))), and check it with a control that both copies read the same thing (here 6,611 vocabulary words each). Before trusting a diff from a copy, grep the hook for __file__.

The change itself: math_sense.py's 80 re.compile calls build the same _lazy_re proxy as proof_sense (patch_lazy.py, generic). 0 differences on 3,409 texts (the author's last 3,000 prompts and .tex chunks; 471 through the maths gate), before and after the swap. Fresh process, live file: ordinary prompt about 36 ms against about 51, a mathematical one about 25 against about 52. Record and rollback: 12_cognitive_architecture/brain_improvement/math_sense_lazy_regex_2026_11_11/.

Related: [[proof_sense_import_compiled_344_regexes_every_prompt_now_lazy_2026_11_11]], [[checklist_task_20261110_092]].

