---
name: prepush_gate_lazy_fetch_far_base_and_slow_tip_fetch_2026_11_12
description: "research-repo push hangs in the pre-push gate? Partial clone: --no-lazy-fetch on every lookup; the missing-tip fetch takes 25+ min while main moves; land via push_paths.sh (GraphQL lane)"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T23:34:53+02:00
  status: verified
  evidence: "brain 03e94d2b (gate fix), test_prepush_new_ref.py 10/10, gate_hand2.txt rc=124 secs=1643 scan clean, mrb 27ceac4b via push_paths"
  lesson: true
---

On 12 Nov 2026 a research-repo push sat for hours in the pre-push secret gate (~/.claude/dreaming/prepush_secret_gate.py) on this workstation. Three faults, all fixed and pushed (brain 03e94d2b, test_prepush_new_ref.py 10/10 after each):
1. Lazy fetch. research-repo is a partial clone (blob:none). The gate's cat-file and rev-list ran without --no-lazy-fetch, so an id the clone lacked was downloaded with its history: one push pulled a 452,792-object pack and sat 40 min. Every git object lookup in a hook on a partial clone needs --no-lazy-fetch.
2. Silent refusal. Under CREATE_NO_WINDOW the scanner's output was lost and a refusal said only "exit 2". The gate now captures and prints it.
3. Far base. When the remote tip had moved since the last fetch, the gate searched other branch tips for a base and picked one 14,074 commits back, so scan_secrets.py hit its 180 s git timeout on every try. The gate now fetches the missing tip first.

Measured afterwards (hand timing, 22:45-23:13): the fetch of the missing tip is the slow step, 25+ minutes on this box. Most of that is git's connectivity check (rev-list --objects, 1 GB). The secret scan itself was clean and quick. research-repo main moves every few minutes, so by the time the fetch ends the tip has moved again and git push can lose that race forever.

What landed it: ~/.claude/dreaming/push_paths.sh REPO "msg" <paths> run against the worktree. It builds one commit of the named paths on main's current tip, runs scan_secrets itself and lands by GraphQL when main is busy (mrb 27ceac4b, try 2). It refuses when main has lines your copy would drop. Before setting ALLOW_REMOVALS=1, check that main has not touched your files since your base (git --no-lazy-fetch log BASE..origin/main -- paths) and that the dropped lines are only your own replacements.


Related: [[a_shared_clones_origin_main_is_a_contended_ref_fetch_into_your_own]] [[scan_secrets_task_scheduler_status_values_blocked_nightly_push_2026_11_12]]
