---
name: bt2_arm_audit_missed_home_rooted_search_grader_ignored_budget_2026_11_08
description: "[VERIFIED] No (8 Nov): BT2's command-text audit could not see a search rooted at ~ or /, which reads the memory folder and repo mirrors unnamed; now banned (12/12 caught, 0/10 false); grader now cuts at the frozen 12-command budget"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T09:16:12+04:00
  status: provisional
  evidence: "~/codex_fleet/20261108_pro/bt2_controller/run_hunt.py"
---

Does a brain test's command audit catch an arm reading files it may not? Not if the arm searches from the home folder. On 8 Nov the BT2 run (brain vs grep vs bare, 30 ordered hunts, ~/codex_fleet/20261108_pro/bt2_controller) audited each arm by matching forbidden path names in the command text. After hunt H001 the bare Claude arm had run `cd ~; rg -il ...`. That one was caught only because its exclude globs happened to name a forbidden folder. A plain `rg foo ~` names nothing forbidden, yet it reads the memory folder, the repo mirrors (~/brain-repo holds the memories too, and the bare arm had been told "anything else on the Mac is allowed") and other arms' earlier answer files under ~/bt2_arms and keys_private/bt2_runs. The bank reuses source facts across hunts.

Fix (run_hunt.py, 8 Nov 09:1x): every arm is barred from searches rooted at ~, $HOME, ~, /Users, /private or /, and from `cd ~` followed by a command. The same goes for a Claude Grep/Glob call with such a path. grep and bare are also barred from the repo mirrors. A probe set of 12 bad and 10 fine commands gives 12 caught and 0 false alarms. reaudit.py puts the hunts run before the fix under the same rule.

Two more holes from the same morning:
(1) The grader ignored the frozen budget. SCORING.md says an exhausted allowance closes the hunt and every simple command in a pipeline counts, while controller.py grade counted every right answer, even one after a wrong answer. grade_budget.py now credits ordered depth cut at the 12th command, under the strict count and under the plain count the arm prompt described. Over-budget was common: 3 of 6 arms on H001, and brain_codex used 20 on H017.
(2) The recall env vars were only in the arm prompt. BRAIN_RECALL_LOG=0 and BRAIN_RECALL_REFRESH=0 now go into the child environment.

A headless `claude -p` arm with hooks off still loads the global CLAUDE.md, which holds rules and no memory facts. It does not get MEMORY.md, because its fresh working folder has an empty project memory dir (probed 8 Nov).

How to apply: in any arm audit, treat a search rooted at home or / as a violation in itself. Grep the grader for the budget before quoting a score. Never print an arm's commands unfiltered in the controller session: two H001 answers reached this session's transcript that way, and its compactions become brain nodes. grade_budget.py flags hunts whose transcripts mention an earlier session.


Related: the grader-budget half repeats [[btq2_p1_p2_own_budget_13_and_19_of_30_grader_had_p0_limits_2026_11_03]] (a grader on old limits); the earlier full-graph test that came out too easy is [[xaware2_full_graph_brain_87_grep_83_of_90_p0p29_bank_too_easy_2026_11_03]].
