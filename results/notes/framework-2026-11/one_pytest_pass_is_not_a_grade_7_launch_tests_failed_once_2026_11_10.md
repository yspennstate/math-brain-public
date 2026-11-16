---
name: one_pytest_pass_is_not_a_grade_7_launch_tests_failed_once_2026_11_10
description: "[PROVISIONAL] No: one pytest pass of a hidden suite failed 7 launch tests that passed on 4 later passes (arm 2/6 -> 5/6, sign flipped); grade twice with private basetemps, third pass on disagreement; cause unmeasured"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T00:04:59+04:00
  status: provisional
  evidence: "brain-repo 12_cognitive_architecture/brain_improvement/long1_2026_11_09/amendment11 (commit 2087b59e09)"
---

Is one pytest pass of a test's hidden suite a grade? No. On 9 Nov 23:53 one pass over a Codex arm's repo failed 7
tests, every one a launch test, with the arm's launcher saying "Codex exited at startup (1)". The same repo, untouched,
then failed 1 test on each of 4 more passes: in place twice, on a copy, and under the runner's own environment
(including __PYVENV_LAUNCHER__). Read as graded, the arm scored 2 of 6 against the other arm's 4; regraded it was 5
against 4, and the sign of the comparison flipped.

The cause is not known. The failing pass used pytest's shared temp folder (pytest-of-<user>/pytest-N, the newest
three kept, shared by every pytest run of this user on the Mac), and that folder had been rotated away before anyone
looked, so its events log was gone. Keep the mechanism open; do not write it down as rotation or load until a probe
shows it.

How to apply when building a graded test:
- grade every repo twice, each pass with its own --basetemp beside the run's records; when the passes disagree, run
  a third and take the majority per test, and keep every pass's output in the grade file;
- remove those folders only after the last pass: a launch test's detached worker can finish after its pass and
  write its release into the folder (seen 10 Nov 00:00, 10 s after rmtree);
- when one arm's grade is far off its peers', regrade every arm of that rep in one pass before reading the
  comparison, and publish both rows.

Related: [[a_regrade_moves_statement_verdicts_compare_arms_within_one_pass_2026_09_29]] (same rule for judged
verdicts); [[grader_ab_controls_lie_by_environment_bank_and_module_cache_2026_10_09]] (grader results that move with
the environment).


Probe, 10 Nov 00:06 (an agent): rotation by other pytest runs is not it, at least not alone. One pass graded the same repo in pytest's shared folder while five other pytest sessions started beside it; they rotated the older numbered folders away, pytest kept the running pass's locked folder, and the pass failed only the 1 real test.
